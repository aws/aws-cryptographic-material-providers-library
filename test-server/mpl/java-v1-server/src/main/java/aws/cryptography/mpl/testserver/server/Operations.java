package aws.cryptography.mpl.testserver.server;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsManager;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.CreateDefaultCryptographicMaterialsManagerInput;
import software.amazon.cryptography.materialproviders.model.CreateRawAesKeyringInput;
import software.amazon.cryptography.materialproviders.model.DecryptMaterialsInput;
import software.amazon.cryptography.materialproviders.model.DecryptionMaterials;
import software.amazon.cryptography.materialproviders.model.EncryptedDataKey;
import software.amazon.cryptography.materialproviders.model.EncryptionMaterials;
import software.amazon.cryptography.materialproviders.model.GetEncryptionMaterialsInput;
import software.amazon.cryptography.materialproviders.model.InitializeDecryptionMaterialsInput;
import software.amazon.cryptography.materialproviders.model.InitializeEncryptionMaterialsInput;
import software.amazon.cryptography.materialproviders.model.OnDecryptInput;
import software.amazon.cryptography.materialproviders.model.OnEncryptInput;

/**
 * Maps each TestServer operation to the Java MaterialProviders client. Keyrings
 * and CMMs live in typed registries keyed by an opaque UUID handle; a handle is
 * only ever looked up in the registry of the kind the operation expects, so a
 * wrong-kind handle is simply unknown there.
 */
final class Operations {

  private final MaterialProviders materialProviders;
  private final Enums enums;
  private final Map<String, IKeyring> keyrings = new ConcurrentHashMap<>();
  private final Map<String, ICryptographicMaterialsManager> cmms =
    new ConcurrentHashMap<>();

  Operations(MaterialProviders materialProviders) {
    this.materialProviders = materialProviders;
    this.enums = new Enums(materialProviders);
  }

  ObjectNode dispatch(String operation, JsonNode request) {
    switch (operation) {
      case "CreateRawAesKeyring":
        return createRawAesKeyring(request);
      case "CreateDefaultCmm":
        return createDefaultCmm(request);
      case "InitializeEncryptionMaterials":
        return initializeEncryptionMaterials(request);
      case "InitializeDecryptionMaterials":
        return initializeDecryptionMaterials(request);
      case "OnEncrypt":
        return onEncrypt(request);
      case "OnDecrypt":
        return onDecrypt(request);
      case "GetEncryptionMaterials":
        return getEncryptionMaterials(request);
      case "DecryptMaterials":
        return decryptMaterials(request);
      default:
        throw ModeledError.generic("unknown operation: " + operation);
    }
  }

  // ---------------------------------------------------------------------
  // Construction
  // ---------------------------------------------------------------------

  private ObjectNode createRawAesKeyring(JsonNode request) {
    IKeyring keyring = materialProviders.CreateRawAesKeyring(
      CreateRawAesKeyringInput
        .builder()
        .keyNamespace(Cbor.string(request, "keyNamespace"))
        .keyName(Cbor.string(request, "keyName"))
        .wrappingKey(ByteBuffer.wrap(Cbor.blob(request, "wrappingKey")))
        .wrappingAlg(Enums.aesWrappingAlg(Cbor.string(request, "wrappingAlg")))
        .build()
    );
    ObjectNode response = Cbor.object();
    response.put("keyringId", register(keyrings, keyring));
    return response;
  }

  private ObjectNode createDefaultCmm(JsonNode request) {
    IKeyring keyring = keyring(Cbor.string(request, "keyringId"));
    ICryptographicMaterialsManager cmm =
      materialProviders.CreateDefaultCryptographicMaterialsManager(
        CreateDefaultCryptographicMaterialsManagerInput
          .builder()
          .keyring(keyring)
          .build()
      );
    ObjectNode response = Cbor.object();
    response.put("cmmId", register(cmms, cmm));
    return response;
  }

  // ---------------------------------------------------------------------
  // Materials initialization + keyring interface
  // ---------------------------------------------------------------------

  private ObjectNode initializeEncryptionMaterials(JsonNode request) {
    EncryptionMaterials materials =
      materialProviders.InitializeEncryptionMaterials(
        InitializeEncryptionMaterialsInput
          .builder()
          .algorithmSuiteId(
            Enums.suiteId(Cbor.string(request, "algorithmSuiteId"))
          )
          .encryptionContext(Cbor.stringMap(request, "encryptionContext"))
          .requiredEncryptionContextKeys(
            Cbor.stringList(request, "requiredEncryptionContextKeys")
          )
          .build()
      );
    ObjectNode response = Cbor.object();
    response.set("materials", encryptionMaterialsToWire(materials));
    return response;
  }

  private ObjectNode initializeDecryptionMaterials(JsonNode request) {
    DecryptionMaterials materials =
      materialProviders.InitializeDecryptionMaterials(
        InitializeDecryptionMaterialsInput
          .builder()
          .algorithmSuiteId(
            Enums.suiteId(Cbor.string(request, "algorithmSuiteId"))
          )
          .encryptionContext(Cbor.stringMap(request, "encryptionContext"))
          .requiredEncryptionContextKeys(
            Cbor.stringList(request, "requiredEncryptionContextKeys")
          )
          .build()
      );
    ObjectNode response = Cbor.object();
    response.set("materials", decryptionMaterialsToWire(materials));
    return response;
  }

  private ObjectNode onEncrypt(JsonNode request) {
    IKeyring keyring = keyring(Cbor.string(request, "keyringId"));
    EncryptionMaterials materials = encryptionMaterialsFromWire(
      Cbor.member(request, "materials")
    );
    EncryptionMaterials out = keyring
      .OnEncrypt(OnEncryptInput.builder().materials(materials).build())
      .materials();
    ObjectNode response = Cbor.object();
    response.set("materials", encryptionMaterialsToWire(out));
    return response;
  }

  private ObjectNode onDecrypt(JsonNode request) {
    IKeyring keyring = keyring(Cbor.string(request, "keyringId"));
    DecryptionMaterials materials = decryptionMaterialsFromWire(
      Cbor.member(request, "materials")
    );
    DecryptionMaterials out = keyring
      .OnDecrypt(
        OnDecryptInput
          .builder()
          .materials(materials)
          .encryptedDataKeys(edksFromWire(request, "encryptedDataKeys"))
          .build()
      )
      .materials();
    ObjectNode response = Cbor.object();
    response.set("materials", decryptionMaterialsToWire(out));
    return response;
  }

  // ---------------------------------------------------------------------
  // CMM
  // ---------------------------------------------------------------------

  private ObjectNode getEncryptionMaterials(JsonNode request) {
    ICryptographicMaterialsManager cmm = cmm(Cbor.string(request, "cmmId"));
    GetEncryptionMaterialsInput.Builder input = GetEncryptionMaterialsInput
      .builder()
      .encryptionContext(Cbor.stringMap(request, "encryptionContext"))
      .commitmentPolicy(
        Enums.commitmentPolicy(Cbor.string(request, "commitmentPolicy"))
      );
    if (Cbor.present(request, "algorithmSuiteId")) {
      input.algorithmSuiteId(
        Enums.suiteId(Cbor.string(request, "algorithmSuiteId"))
      );
    }
    if (Cbor.present(request, "maxPlaintextLength")) {
      input.maxPlaintextLength(Cbor.longValue(request, "maxPlaintextLength"));
    }
    EncryptionMaterials materials = cmm
      .GetEncryptionMaterials(input.build())
      .encryptionMaterials();
    if (materials.plaintextDataKey() == null) {
      throw ModeledError.mpl("no plaintext data key in materials");
    }

    ObjectNode response = Cbor.object();
    response.put(
      "algorithmSuiteId",
      Enums.suiteToWire(materials.algorithmSuite().id())
    );
    Cbor.putMap(response, "encryptionContext", materials.encryptionContext());
    response.set(
      "encryptedDataKeys",
      edksToWire(materials.encryptedDataKeys())
    );
    response.put("plaintextDataKey", Cbor.bytes(materials.plaintextDataKey()));
    Cbor.putOptionalBlob(response, "signingKey", materials.signingKey());
    Cbor.putOptionalBlobList(
      response,
      "symmetricSigningKeys",
      materials.symmetricSigningKeys()
    );
    return response;
  }

  private ObjectNode decryptMaterials(JsonNode request) {
    ICryptographicMaterialsManager cmm = cmm(Cbor.string(request, "cmmId"));
    DecryptMaterialsInput.Builder input = DecryptMaterialsInput
      .builder()
      .algorithmSuiteId(Enums.suiteId(Cbor.string(request, "algorithmSuiteId")))
      .commitmentPolicy(
        Enums.commitmentPolicy(Cbor.string(request, "commitmentPolicy"))
      )
      .encryptedDataKeys(edksFromWire(request, "encryptedDataKeys"))
      .encryptionContext(Cbor.stringMap(request, "encryptionContext"));
    if (Cbor.present(request, "reproducedEncryptionContext")) {
      input.reproducedEncryptionContext(
        Cbor.stringMap(request, "reproducedEncryptionContext")
      );
    }
    DecryptionMaterials materials = cmm
      .DecryptMaterials(input.build())
      .decryptionMaterials();
    if (materials.plaintextDataKey() == null) {
      throw ModeledError.mpl("no plaintext data key in materials");
    }

    ObjectNode response = Cbor.object();
    response.put("plaintextDataKey", Cbor.bytes(materials.plaintextDataKey()));
    Cbor.putMap(response, "encryptionContext", materials.encryptionContext());
    Cbor.putOptionalBlob(
      response,
      "verificationKey",
      materials.verificationKey()
    );
    Cbor.putOptionalBlob(
      response,
      "symmetricSigningKey",
      materials.symmetricSigningKey()
    );
    return response;
  }

  // ---------------------------------------------------------------------
  // Registry
  // ---------------------------------------------------------------------

  private static <T> String register(Map<String, T> registry, T resource) {
    String id = UUID.randomUUID().toString();
    registry.put(id, resource);
    return id;
  }

  private IKeyring keyring(String id) {
    return lookup(keyrings, id, "keyringId");
  }

  private ICryptographicMaterialsManager cmm(String id) {
    return lookup(cmms, id, "cmmId");
  }

  private static <T> T lookup(
    Map<String, T> registry,
    String id,
    String member
  ) {
    if (id.isEmpty()) {
      throw ModeledError.generic(member + " must be non-empty");
    }
    T resource = registry.get(id);
    if (resource == null) {
      throw ModeledError.generic("unknown " + member + ": " + id);
    }
    return resource;
  }

  // ---------------------------------------------------------------------
  // Materials conversion
  // ---------------------------------------------------------------------

  private EncryptionMaterials encryptionMaterialsFromWire(JsonNode wire) {
    EncryptionMaterials.Builder builder = EncryptionMaterials
      .builder()
      .algorithmSuite(enums.suiteInfo(Cbor.string(wire, "algorithmSuiteId")))
      .encryptionContext(Cbor.stringMap(wire, "encryptionContext"))
      .encryptedDataKeys(edksFromWire(wire, "encryptedDataKeys"))
      .requiredEncryptionContextKeys(
        Cbor.stringList(wire, "requiredEncryptionContextKeys")
      );
    ByteBuffer plaintextDataKey = Cbor.optionalBlob(wire, "plaintextDataKey");
    if (plaintextDataKey != null) {
      builder.plaintextDataKey(plaintextDataKey);
    }
    ByteBuffer signingKey = Cbor.optionalBlob(wire, "signingKey");
    if (signingKey != null) {
      builder.signingKey(signingKey);
    }
    List<ByteBuffer> symmetricSigningKeys = Cbor.optionalBlobList(
      wire,
      "symmetricSigningKeys"
    );
    if (symmetricSigningKeys != null) {
      builder.symmetricSigningKeys(symmetricSigningKeys);
    }
    return builder.build();
  }

  private DecryptionMaterials decryptionMaterialsFromWire(JsonNode wire) {
    DecryptionMaterials.Builder builder = DecryptionMaterials
      .builder()
      .algorithmSuite(enums.suiteInfo(Cbor.string(wire, "algorithmSuiteId")))
      .encryptionContext(Cbor.stringMap(wire, "encryptionContext"))
      .requiredEncryptionContextKeys(
        Cbor.stringList(wire, "requiredEncryptionContextKeys")
      );
    ByteBuffer plaintextDataKey = Cbor.optionalBlob(wire, "plaintextDataKey");
    if (plaintextDataKey != null) {
      builder.plaintextDataKey(plaintextDataKey);
    }
    ByteBuffer verificationKey = Cbor.optionalBlob(wire, "verificationKey");
    if (verificationKey != null) {
      builder.verificationKey(verificationKey);
    }
    ByteBuffer symmetricSigningKey = Cbor.optionalBlob(
      wire,
      "symmetricSigningKey"
    );
    if (symmetricSigningKey != null) {
      builder.symmetricSigningKey(symmetricSigningKey);
    }
    return builder.build();
  }

  private static ObjectNode encryptionMaterialsToWire(
    EncryptionMaterials materials
  ) {
    ObjectNode wire = Cbor.object();
    wire.put(
      "algorithmSuiteId",
      Enums.suiteToWire(materials.algorithmSuite().id())
    );
    Cbor.putMap(wire, "encryptionContext", materials.encryptionContext());
    wire.set("encryptedDataKeys", edksToWire(materials.encryptedDataKeys()));
    Cbor.putStringList(
      wire,
      "requiredEncryptionContextKeys",
      materials.requiredEncryptionContextKeys()
    );
    Cbor.putOptionalBlob(
      wire,
      "plaintextDataKey",
      materials.plaintextDataKey()
    );
    Cbor.putOptionalBlob(wire, "signingKey", materials.signingKey());
    Cbor.putOptionalBlobList(
      wire,
      "symmetricSigningKeys",
      materials.symmetricSigningKeys()
    );
    return wire;
  }

  private static ObjectNode decryptionMaterialsToWire(
    DecryptionMaterials materials
  ) {
    ObjectNode wire = Cbor.object();
    wire.put(
      "algorithmSuiteId",
      Enums.suiteToWire(materials.algorithmSuite().id())
    );
    Cbor.putMap(wire, "encryptionContext", materials.encryptionContext());
    Cbor.putStringList(
      wire,
      "requiredEncryptionContextKeys",
      materials.requiredEncryptionContextKeys()
    );
    Cbor.putOptionalBlob(
      wire,
      "plaintextDataKey",
      materials.plaintextDataKey()
    );
    Cbor.putOptionalBlob(wire, "verificationKey", materials.verificationKey());
    Cbor.putOptionalBlob(
      wire,
      "symmetricSigningKey",
      materials.symmetricSigningKey()
    );
    return wire;
  }

  private static List<EncryptedDataKey> edksFromWire(
    JsonNode node,
    String field
  ) {
    List<EncryptedDataKey> edks = new ArrayList<>();
    for (JsonNode edk : Cbor.list(node, field)) {
      edks.add(
        EncryptedDataKey
          .builder()
          .keyProviderId(Cbor.string(edk, "keyProviderId"))
          .keyProviderInfo(ByteBuffer.wrap(Cbor.blob(edk, "keyProviderInfo")))
          .ciphertext(ByteBuffer.wrap(Cbor.blob(edk, "ciphertext")))
          .build()
      );
    }
    return edks;
  }

  private static ArrayNode edksToWire(List<EncryptedDataKey> edks) {
    ArrayNode wire = Cbor.object().arrayNode();
    if (edks != null) {
      for (EncryptedDataKey edk : edks) {
        ObjectNode entry = wire.addObject();
        entry.put("keyProviderId", edk.keyProviderId());
        entry.put("keyProviderInfo", Cbor.bytes(edk.keyProviderInfo()));
        entry.put("ciphertext", Cbor.bytes(edk.ciphertext()));
      }
    }
    return wire;
  }
}
