# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives import (
    AtomicPrimitivesClient,
)
from .dafny_protocol import DafnyRequest


class DafnyImplInterface:
    impl: AtomicPrimitivesClient | None = None

    # operation_map cannot be created at dafnyImplInterface create time,
    # as the map's values reference values inside `self.impl`,
    # and impl is only populated at runtime.
    # Accessing these before impl is populated results in an error.
    # At runtime, the map is populated once and cached.
    operation_map = None

    def handle_request(self, input: DafnyRequest):
        if self.operation_map is None:
            self.operation_map = {
                "GenerateRandomBytes": self.impl.GenerateRandomBytes,
                "Digest": self.impl.Digest,
                "HMac": self.impl.HMac,
                "HkdfExtract": self.impl.HkdfExtract,
                "HkdfExpand": self.impl.HkdfExpand,
                "Hkdf": self.impl.Hkdf,
                "KdfCounterMode": self.impl.KdfCounterMode,
                "AesKdfCounterMode": self.impl.AesKdfCounterMode,
                "AESEncrypt": self.impl.AESEncrypt,
                "AESDecrypt": self.impl.AESDecrypt,
                "GenerateRSAKeyPair": self.impl.GenerateRSAKeyPair,
                "GetRSAKeyModulusLength": self.impl.GetRSAKeyModulusLength,
                "RSADecrypt": self.impl.RSADecrypt,
                "RSAEncrypt": self.impl.RSAEncrypt,
                "GenerateECDSASignatureKey": self.impl.GenerateECDSASignatureKey,
                "ECDSASign": self.impl.ECDSASign,
                "ECDSAVerify": self.impl.ECDSAVerify,
                "GenerateECCKeyPair": self.impl.GenerateECCKeyPair,
                "GetPublicKeyFromPrivateKey": self.impl.GetPublicKeyFromPrivateKey,
                "ValidatePublicKey": self.impl.ValidatePublicKey,
                "DeriveSharedSecret": self.impl.DeriveSharedSecret,
                "CompressPublicKey": self.impl.CompressPublicKey,
                "DecompressPublicKey": self.impl.DecompressPublicKey,
                "ParsePublicKey": self.impl.ParsePublicKey,
            }

        # This logic is where a typical Smithy client would expect the "server" to be.
        # This code can be thought of as logic our Dafny "server" uses
        #   to route incoming client requests to the correct request handler code.
        if input.dafny_operation_input is None:
            return self.operation_map[input.operation_name]()
        else:
            return self.operation_map[input.operation_name](input.dafny_operation_input)
