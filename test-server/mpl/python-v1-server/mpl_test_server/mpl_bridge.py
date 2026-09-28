# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Delegates each MPL TestServer operation to the Python MaterialProviders client
from the published ``aws-cryptographic-material-providers`` package.

Each handler takes the decoded rpcv2Cbor request map, calls the client, and
returns the response member map. A malformed request or bad handle raises
``ServerError`` (serialized as ``GenericServerError``); a failure raised by the
MPL raises ``MplError`` (serialized as ``MPLClientError``).

Keyrings and CMMs live in typed registries behind UUID handles. A handle is only
looked up in the registry of the kind the operation expects, so a wrong-kind
handle is simply unknown there.
"""

import threading
import uuid

from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.client import (
    AwsCryptographicMaterialProviders,
)
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.config import (
    MaterialProvidersConfig,
)
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders import (
    models,
)


class ServerError(Exception):
    """Framework-side failure: malformed request, unknown enum, bad handle."""


class MplError(Exception):
    """Failure raised by the Material Providers Library."""


_ESDK_POLICY_PREFIX = "ESDK_"

_CLIENT = AwsCryptographicMaterialProviders(MaterialProvidersConfig())

# The wire names ESDK suites by the MPL's constant name; the generated class
# maps each name to its two-byte hex id.
_SUITE_HEX_BY_NAME = {
    name: value
    for name, value in vars(models.ESDKAlgorithmSuiteId).items()
    if isinstance(value, str) and value in models.ESDKAlgorithmSuiteId.values
}
_SUITE_NAME_BY_HEX = {value: name for name, value in _SUITE_HEX_BY_NAME.items()}


def _call(function, *args):
    """Run an MPL call; anything it raises is the MPL's rejection."""
    try:
        return function(*args)
    except (ServerError, MplError):
        raise
    except Exception as exc:  # noqa: BLE001
        raise MplError(str(exc)) from exc


_SUITE_INFO = {
    name: _call(_CLIENT.get_algorithm_suite_info, bytes.fromhex(hex_id[2:]))
    for name, hex_id in _SUITE_HEX_BY_NAME.items()
}

_LOCK = threading.Lock()
_KEYRINGS = {}
_CMMS = {}


# ---------------------------------------------------------------------------
# Request accessors
# ---------------------------------------------------------------------------


def _present(request, name):
    return isinstance(request, dict) and request.get(name) is not None


def _require(request, name, kind):
    if not _present(request, name) or not isinstance(request[name], kind):
        raise ServerError(f"missing or mistyped required member: {name}")
    return request[name]


def _string(request, name):
    return _require(request, name, str)


def _blob(request, name):
    return bytes(_require(request, name, (bytes, bytearray)))


def _optional_blob(request, name):
    return _blob(request, name) if _present(request, name) else None


def _string_map(request, name):
    if not _present(request, name):
        return {}
    value = _require(request, name, dict)
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()):
        raise ServerError(f"map is not string-to-string: {name}")
    return dict(value)


def _string_list(request, name):
    if not _present(request, name):
        return []
    value = _require(request, name, list)
    if not all(isinstance(item, str) for item in value):
        raise ServerError(f"list is not a list of strings: {name}")
    return list(value)


def _optional_blob_list(request, name):
    if not _present(request, name):
        return None
    value = _require(request, name, list)
    if not all(isinstance(item, (bytes, bytearray)) for item in value):
        raise ServerError(f"list is not a list of blobs: {name}")
    return [bytes(item) for item in value]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


def _suite_id(name):
    hex_id = _SUITE_HEX_BY_NAME.get(name)
    if hex_id is None:
        raise ServerError(f"unknown algorithm suite: {name}")
    return models.AlgorithmSuiteIdESDK(hex_id)


def _suite_info(name):
    info = _SUITE_INFO.get(name)
    if info is None:
        raise ServerError(f"unknown algorithm suite: {name}")
    return info


def _suite_to_wire(suite_id):
    if not isinstance(suite_id, models.AlgorithmSuiteIdESDK):
        raise ServerError("the MPL returned a non-ESDK algorithm suite, which the model cannot carry")
    name = _SUITE_NAME_BY_HEX.get(suite_id.value)
    if name is None:
        raise ServerError(f"unrecognized ESDK algorithm suite {suite_id.value}")
    return name


def _commitment_policy(name):
    policy = name[len(_ESDK_POLICY_PREFIX):] if name.startswith(_ESDK_POLICY_PREFIX) else None
    if policy not in models.ESDKCommitmentPolicy.values:
        raise ServerError(f"unknown commitment policy: {name}")
    return models.CommitmentPolicyESDK(policy)


def _aes_wrapping_alg(name):
    if name not in models.AesWrappingAlg.values:
        raise ServerError(f"unknown AES wrapping algorithm: {name}")
    return name


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _register(registry, resource):
    handle = str(uuid.uuid4())
    with _LOCK:
        registry[handle] = resource
    return handle


def _lookup(registry, request, member):
    handle = _string(request, member)
    if not handle:
        raise ServerError(f"{member} must be non-empty")
    with _LOCK:
        resource = registry.get(handle)
    if resource is None:
        raise ServerError(f"unknown {member}: {handle}")
    return resource


# ---------------------------------------------------------------------------
# Materials conversion
# ---------------------------------------------------------------------------


def _edks_from_wire(request, name):
    edks = []
    for edk in _require(request, name, list):
        if not isinstance(edk, dict):
            raise ServerError(f"list element is not a structure: {name}")
        edks.append(
            models.EncryptedDataKey(
                key_provider_id=_string(edk, "keyProviderId"),
                key_provider_info=_blob(edk, "keyProviderInfo"),
                ciphertext=_blob(edk, "ciphertext"),
            )
        )
    return edks


def _edks_to_wire(edks):
    return [
        {
            "keyProviderId": edk.key_provider_id,
            "keyProviderInfo": bytes(edk.key_provider_info),
            "ciphertext": bytes(edk.ciphertext),
        }
        for edk in edks or []
    ]


def _without_none(members):
    """Absent optional members are omitted rather than sent as null."""
    return {k: v for k, v in members.items() if v is not None}


def _bytes_or_none(value):
    return bytes(value) if value is not None else None


def _encryption_materials_from_wire(wire):
    return models.EncryptionMaterials(
        algorithm_suite=_suite_info(_string(wire, "algorithmSuiteId")),
        encryption_context=_string_map(wire, "encryptionContext"),
        encrypted_data_keys=_edks_from_wire(wire, "encryptedDataKeys"),
        required_encryption_context_keys=_string_list(wire, "requiredEncryptionContextKeys"),
        plaintext_data_key=_optional_blob(wire, "plaintextDataKey"),
        signing_key=_optional_blob(wire, "signingKey"),
        symmetric_signing_keys=_optional_blob_list(wire, "symmetricSigningKeys"),
    )


def _decryption_materials_from_wire(wire):
    return models.DecryptionMaterials(
        algorithm_suite=_suite_info(_string(wire, "algorithmSuiteId")),
        encryption_context=_string_map(wire, "encryptionContext"),
        required_encryption_context_keys=_string_list(wire, "requiredEncryptionContextKeys"),
        plaintext_data_key=_optional_blob(wire, "plaintextDataKey"),
        verification_key=_optional_blob(wire, "verificationKey"),
        symmetric_signing_key=_optional_blob(wire, "symmetricSigningKey"),
    )


def _encryption_materials_to_wire(materials):
    return _without_none(
        {
            "algorithmSuiteId": _suite_to_wire(materials.algorithm_suite.id),
            "encryptionContext": dict(materials.encryption_context or {}),
            "encryptedDataKeys": _edks_to_wire(materials.encrypted_data_keys),
            "requiredEncryptionContextKeys": list(materials.required_encryption_context_keys or []),
            "plaintextDataKey": _bytes_or_none(materials.plaintext_data_key),
            "signingKey": _bytes_or_none(materials.signing_key),
            "symmetricSigningKeys": (
                [bytes(k) for k in materials.symmetric_signing_keys]
                if materials.symmetric_signing_keys is not None
                else None
            ),
        }
    )


def _decryption_materials_to_wire(materials):
    return _without_none(
        {
            "algorithmSuiteId": _suite_to_wire(materials.algorithm_suite.id),
            "encryptionContext": dict(materials.encryption_context or {}),
            "requiredEncryptionContextKeys": list(materials.required_encryption_context_keys or []),
            "plaintextDataKey": _bytes_or_none(materials.plaintext_data_key),
            "verificationKey": _bytes_or_none(materials.verification_key),
            "symmetricSigningKey": _bytes_or_none(materials.symmetric_signing_key),
        }
    )


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------


def create_raw_aes_keyring(request):
    keyring = _call(
        _CLIENT.create_raw_aes_keyring,
        models.CreateRawAesKeyringInput(
            key_namespace=_string(request, "keyNamespace"),
            key_name=_string(request, "keyName"),
            wrapping_key=_blob(request, "wrappingKey"),
            wrapping_alg=_aes_wrapping_alg(_string(request, "wrappingAlg")),
        ),
    )
    return {"keyringId": _register(_KEYRINGS, keyring)}


def create_default_cmm(request):
    keyring = _lookup(_KEYRINGS, request, "keyringId")
    cmm = _call(
        _CLIENT.create_default_cryptographic_materials_manager,
        models.CreateDefaultCryptographicMaterialsManagerInput(keyring=keyring),
    )
    return {"cmmId": _register(_CMMS, cmm)}


def initialize_encryption_materials(request):
    materials = _call(
        _CLIENT.initialize_encryption_materials,
        models.InitializeEncryptionMaterialsInput(
            algorithm_suite_id=_suite_id(_string(request, "algorithmSuiteId")),
            encryption_context=_string_map(request, "encryptionContext"),
            required_encryption_context_keys=_string_list(request, "requiredEncryptionContextKeys"),
        ),
    )
    return {"materials": _encryption_materials_to_wire(materials)}


def initialize_decryption_materials(request):
    materials = _call(
        _CLIENT.initialize_decryption_materials,
        models.InitializeDecryptionMaterialsInput(
            algorithm_suite_id=_suite_id(_string(request, "algorithmSuiteId")),
            encryption_context=_string_map(request, "encryptionContext"),
            required_encryption_context_keys=_string_list(request, "requiredEncryptionContextKeys"),
        ),
    )
    return {"materials": _decryption_materials_to_wire(materials)}


def on_encrypt(request):
    keyring = _lookup(_KEYRINGS, request, "keyringId")
    materials = _encryption_materials_from_wire(_require(request, "materials", dict))
    output = _call(keyring.on_encrypt, models.OnEncryptInput(materials=materials))
    return {"materials": _encryption_materials_to_wire(output.materials)}


def on_decrypt(request):
    keyring = _lookup(_KEYRINGS, request, "keyringId")
    input = models.OnDecryptInput(
        materials=_decryption_materials_from_wire(_require(request, "materials", dict)),
        encrypted_data_keys=_edks_from_wire(request, "encryptedDataKeys"),
    )
    output = _call(keyring.on_decrypt, input)
    return {"materials": _decryption_materials_to_wire(output.materials)}


def get_encryption_materials(request):
    cmm = _lookup(_CMMS, request, "cmmId")
    input = models.GetEncryptionMaterialsInput(
        encryption_context=_string_map(request, "encryptionContext"),
        commitment_policy=_commitment_policy(_string(request, "commitmentPolicy")),
        algorithm_suite_id=(
            _suite_id(_string(request, "algorithmSuiteId"))
            if _present(request, "algorithmSuiteId")
            else None
        ),
        max_plaintext_length=(
            _require(request, "maxPlaintextLength", int)
            if _present(request, "maxPlaintextLength")
            else None
        ),
    )
    materials = _call(cmm.get_encryption_materials, input).encryption_materials
    if materials.plaintext_data_key is None:
        raise MplError("no plaintext data key in materials")
    return _without_none(
        {
            "algorithmSuiteId": _suite_to_wire(materials.algorithm_suite.id),
            "encryptionContext": dict(materials.encryption_context or {}),
            "encryptedDataKeys": _edks_to_wire(materials.encrypted_data_keys),
            "plaintextDataKey": bytes(materials.plaintext_data_key),
            "signingKey": _bytes_or_none(materials.signing_key),
            "symmetricSigningKeys": (
                [bytes(k) for k in materials.symmetric_signing_keys]
                if materials.symmetric_signing_keys is not None
                else None
            ),
        }
    )


def decrypt_materials(request):
    cmm = _lookup(_CMMS, request, "cmmId")
    input = models.DecryptMaterialsInput(
        algorithm_suite_id=_suite_id(_string(request, "algorithmSuiteId")),
        commitment_policy=_commitment_policy(_string(request, "commitmentPolicy")),
        encrypted_data_keys=_edks_from_wire(request, "encryptedDataKeys"),
        encryption_context=_string_map(request, "encryptionContext"),
        reproduced_encryption_context=(
            _string_map(request, "reproducedEncryptionContext")
            if _present(request, "reproducedEncryptionContext")
            else None
        ),
    )
    materials = _call(cmm.decrypt_materials, input).decryption_materials
    if materials.plaintext_data_key is None:
        raise MplError("no plaintext data key in materials")
    return _without_none(
        {
            "plaintextDataKey": bytes(materials.plaintext_data_key),
            "encryptionContext": dict(materials.encryption_context or {}),
            "verificationKey": _bytes_or_none(materials.verification_key),
            "symmetricSigningKey": _bytes_or_none(materials.symmetric_signing_key),
        }
    )


OPERATIONS = {
    "CreateRawAesKeyring": create_raw_aes_keyring,
    "CreateDefaultCmm": create_default_cmm,
    "InitializeEncryptionMaterials": initialize_encryption_materials,
    "InitializeDecryptionMaterials": initialize_decryption_materials,
    "OnEncrypt": on_encrypt,
    "OnDecrypt": on_decrypt,
    "GetEncryptionMaterials": get_encryption_materials,
    "DecryptMaterials": decrypt_materials,
}
