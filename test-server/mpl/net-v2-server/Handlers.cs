// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Operation handlers: decode the rpcv2Cbor request, delegate to the .NET
// MaterialProviders client, and encode the response. Keyrings and CMMs are
// held in typed registries behind UUID handles; a handle is only looked up in
// the registry of the kind the operation expects. A library failure becomes an
// MPLClientError; a malformed request or bad handle a GenericServerError.

using System.Collections.Concurrent;
using System.Globalization;
using System.Reflection;
using AWS.Cryptography.MaterialProviders;

namespace MplTestServer;

internal sealed class Handlers
{
    private const string EsdkPolicyPrefix = "ESDK_";

    private readonly MaterialProviders _mpl = new(new MaterialProvidersConfig());
    private readonly ConcurrentDictionary<string, IKeyring> _keyrings = new();
    private readonly ConcurrentDictionary<string, ICryptographicMaterialsManager> _cmms = new();
    private readonly Dictionary<string, AlgorithmSuiteInfo> _suiteInfo = new();

    internal Handlers()
    {
        // The wire names suites by the MPL's constant name; resolve each one's
        // AlgorithmSuiteInfo once from its two-byte id.
        foreach (var field in ConstantFields<ESDKAlgorithmSuiteId>())
        {
            var suite = (ESDKAlgorithmSuiteId)field.GetValue(null);
            var hex = suite.Value.Substring(2);
            var binary = new byte[hex.Length / 2];
            for (var i = 0; i < binary.Length; i++)
            {
                binary[i] = byte.Parse(hex.Substring(i * 2, 2), NumberStyles.HexNumber);
            }
            _suiteInfo[field.Name] = _mpl.GetAlgorithmSuiteInfo(new MemoryStream(binary));
        }
    }

    internal byte[] Dispatch(string operation, Dictionary<string, object> request) => operation switch
    {
        "CreateRawAesKeyring" => CreateRawAesKeyring(request),
        "CreateDefaultCmm" => CreateDefaultCmm(request),
        "InitializeEncryptionMaterials" => InitializeEncryptionMaterials(request),
        "InitializeDecryptionMaterials" => InitializeDecryptionMaterials(request),
        "OnEncrypt" => OnEncrypt(request),
        "OnDecrypt" => OnDecrypt(request),
        "GetEncryptionMaterials" => GetEncryptionMaterials(request),
        "DecryptMaterials" => DecryptMaterials(request),
        _ => throw ServerErrorException.Generic($"unknown operation: {operation}"),
    };

    // ------------------------------------------------------------------
    // Construction
    // ------------------------------------------------------------------

    private byte[] CreateRawAesKeyring(Dictionary<string, object> request)
    {
        var input = new CreateRawAesKeyringInput
        {
            KeyNamespace = Model.Str(request, "keyNamespace"),
            KeyName = Model.Str(request, "keyName"),
            WrappingKey = new MemoryStream(Model.Bytes(request, "wrappingKey")),
            WrappingAlg = Constant<AesWrappingAlg>(Model.Str(request, "wrappingAlg"), "AES wrapping algorithm"),
        };
        var keyring = Call(() => _mpl.CreateRawAesKeyring(input));
        return Model.Write(new Dictionary<string, object> { ["keyringId"] = Register(_keyrings, keyring) });
    }

    private byte[] CreateDefaultCmm(Dictionary<string, object> request)
    {
        var keyring = Lookup(_keyrings, Model.Str(request, "keyringId"), "keyringId");
        var cmm = Call(() => _mpl.CreateDefaultCryptographicMaterialsManager(
            new CreateDefaultCryptographicMaterialsManagerInput { Keyring = keyring }));
        return Model.Write(new Dictionary<string, object> { ["cmmId"] = Register(_cmms, cmm) });
    }

    // ------------------------------------------------------------------
    // Materials initialization + keyring interface
    // ------------------------------------------------------------------

    private byte[] InitializeEncryptionMaterials(Dictionary<string, object> request)
    {
        var input = new InitializeEncryptionMaterialsInput
        {
            AlgorithmSuiteId = SuiteId(Model.Str(request, "algorithmSuiteId")),
            EncryptionContext = Model.StringMap(request, "encryptionContext"),
            RequiredEncryptionContextKeys = Model.StringList(request, "requiredEncryptionContextKeys"),
        };
        var materials = Call(() => _mpl.InitializeEncryptionMaterials(input));
        return Model.Write(new Dictionary<string, object> { ["materials"] = EncryptionMaterialsToWire(materials) });
    }

    private byte[] InitializeDecryptionMaterials(Dictionary<string, object> request)
    {
        var input = new InitializeDecryptionMaterialsInput
        {
            AlgorithmSuiteId = SuiteId(Model.Str(request, "algorithmSuiteId")),
            EncryptionContext = Model.StringMap(request, "encryptionContext"),
            RequiredEncryptionContextKeys = Model.StringList(request, "requiredEncryptionContextKeys"),
        };
        var materials = Call(() => _mpl.InitializeDecryptionMaterials(input));
        return Model.Write(new Dictionary<string, object> { ["materials"] = DecryptionMaterialsToWire(materials) });
    }

    private byte[] OnEncrypt(Dictionary<string, object> request)
    {
        var keyring = Lookup(_keyrings, Model.Str(request, "keyringId"), "keyringId");
        var materials = EncryptionMaterialsFromWire(Model.Map(request, "materials"));
        var output = Call(() => keyring.OnEncrypt(new OnEncryptInput { Materials = materials }));
        return Model.Write(new Dictionary<string, object> { ["materials"] = EncryptionMaterialsToWire(output.Materials) });
    }

    private byte[] OnDecrypt(Dictionary<string, object> request)
    {
        var keyring = Lookup(_keyrings, Model.Str(request, "keyringId"), "keyringId");
        var input = new OnDecryptInput
        {
            Materials = DecryptionMaterialsFromWire(Model.Map(request, "materials")),
            EncryptedDataKeys = EdksFromWire(request, "encryptedDataKeys"),
        };
        var output = Call(() => keyring.OnDecrypt(input));
        return Model.Write(new Dictionary<string, object> { ["materials"] = DecryptionMaterialsToWire(output.Materials) });
    }

    // ------------------------------------------------------------------
    // CMM
    // ------------------------------------------------------------------

    private byte[] GetEncryptionMaterials(Dictionary<string, object> request)
    {
        var cmm = Lookup(_cmms, Model.Str(request, "cmmId"), "cmmId");
        var input = new GetEncryptionMaterialsInput
        {
            EncryptionContext = Model.StringMap(request, "encryptionContext"),
            CommitmentPolicy = Policy(Model.Str(request, "commitmentPolicy")),
        };
        if (Model.Present(request, "algorithmSuiteId"))
        {
            input.AlgorithmSuiteId = SuiteId(Model.Str(request, "algorithmSuiteId"));
        }
        if (Model.Present(request, "maxPlaintextLength"))
        {
            input.MaxPlaintextLength = Model.Long(request, "maxPlaintextLength");
        }
        var materials = Call(() => cmm.GetEncryptionMaterials(input)).EncryptionMaterials;
        if (materials.PlaintextDataKey == null)
        {
            throw ServerErrorException.Mpl("no plaintext data key in materials");
        }
        return Model.Write(new Dictionary<string, object>
        {
            ["algorithmSuiteId"] = SuiteToWire(materials.AlgorithmSuite.Id),
            ["encryptionContext"] = materials.EncryptionContext,
            ["encryptedDataKeys"] = EdksToWire(materials.EncryptedDataKeys),
            ["plaintextDataKey"] = materials.PlaintextDataKey,
            ["signingKey"] = materials.SigningKey,
            ["symmetricSigningKeys"] = materials.SymmetricSigningKeys?.Cast<object>().ToList(),
        });
    }

    private byte[] DecryptMaterials(Dictionary<string, object> request)
    {
        var cmm = Lookup(_cmms, Model.Str(request, "cmmId"), "cmmId");
        var input = new DecryptMaterialsInput
        {
            AlgorithmSuiteId = SuiteId(Model.Str(request, "algorithmSuiteId")),
            CommitmentPolicy = Policy(Model.Str(request, "commitmentPolicy")),
            EncryptedDataKeys = EdksFromWire(request, "encryptedDataKeys"),
            EncryptionContext = Model.StringMap(request, "encryptionContext"),
        };
        if (Model.Present(request, "reproducedEncryptionContext"))
        {
            input.ReproducedEncryptionContext = Model.StringMap(request, "reproducedEncryptionContext");
        }
        var materials = Call(() => cmm.DecryptMaterials(input)).DecryptionMaterials;
        if (materials.PlaintextDataKey == null)
        {
            throw ServerErrorException.Mpl("no plaintext data key in materials");
        }
        return Model.Write(new Dictionary<string, object>
        {
            ["plaintextDataKey"] = materials.PlaintextDataKey,
            ["encryptionContext"] = materials.EncryptionContext,
            ["verificationKey"] = materials.VerificationKey,
            ["symmetricSigningKey"] = materials.SymmetricSigningKey,
        });
    }

    // ------------------------------------------------------------------
    // Materials conversion
    // ------------------------------------------------------------------

    private EncryptionMaterials EncryptionMaterialsFromWire(Dictionary<string, object> wire)
    {
        var materials = new EncryptionMaterials
        {
            AlgorithmSuite = SuiteInfo(Model.Str(wire, "algorithmSuiteId")),
            EncryptionContext = Model.StringMap(wire, "encryptionContext"),
            EncryptedDataKeys = EdksFromWire(wire, "encryptedDataKeys"),
            RequiredEncryptionContextKeys = Model.StringList(wire, "requiredEncryptionContextKeys"),
        };
        if (Model.Present(wire, "plaintextDataKey"))
        {
            materials.PlaintextDataKey = Model.OptionalBlob(wire, "plaintextDataKey");
        }
        if (Model.Present(wire, "signingKey"))
        {
            materials.SigningKey = Model.OptionalBlob(wire, "signingKey");
        }
        if (Model.Present(wire, "symmetricSigningKeys"))
        {
            materials.SymmetricSigningKeys = Model.OptionalBlobList(wire, "symmetricSigningKeys");
        }
        return materials;
    }

    private DecryptionMaterials DecryptionMaterialsFromWire(Dictionary<string, object> wire)
    {
        var materials = new DecryptionMaterials
        {
            AlgorithmSuite = SuiteInfo(Model.Str(wire, "algorithmSuiteId")),
            EncryptionContext = Model.StringMap(wire, "encryptionContext"),
            RequiredEncryptionContextKeys = Model.StringList(wire, "requiredEncryptionContextKeys"),
        };
        if (Model.Present(wire, "plaintextDataKey"))
        {
            materials.PlaintextDataKey = Model.OptionalBlob(wire, "plaintextDataKey");
        }
        if (Model.Present(wire, "verificationKey"))
        {
            materials.VerificationKey = Model.OptionalBlob(wire, "verificationKey");
        }
        if (Model.Present(wire, "symmetricSigningKey"))
        {
            materials.SymmetricSigningKey = Model.OptionalBlob(wire, "symmetricSigningKey");
        }
        return materials;
    }

    private static Dictionary<string, object> EncryptionMaterialsToWire(EncryptionMaterials materials) => new()
    {
        ["algorithmSuiteId"] = SuiteToWire(materials.AlgorithmSuite.Id),
        ["encryptionContext"] = materials.EncryptionContext ?? new Dictionary<string, string>(),
        ["encryptedDataKeys"] = EdksToWire(materials.EncryptedDataKeys),
        ["requiredEncryptionContextKeys"] =
            (materials.RequiredEncryptionContextKeys ?? new List<string>()).Cast<object>().ToList(),
        ["plaintextDataKey"] = materials.PlaintextDataKey,
        ["signingKey"] = materials.SigningKey,
        ["symmetricSigningKeys"] = materials.SymmetricSigningKeys?.Cast<object>().ToList(),
    };

    private static Dictionary<string, object> DecryptionMaterialsToWire(DecryptionMaterials materials) => new()
    {
        ["algorithmSuiteId"] = SuiteToWire(materials.AlgorithmSuite.Id),
        ["encryptionContext"] = materials.EncryptionContext ?? new Dictionary<string, string>(),
        ["requiredEncryptionContextKeys"] =
            (materials.RequiredEncryptionContextKeys ?? new List<string>()).Cast<object>().ToList(),
        ["plaintextDataKey"] = materials.PlaintextDataKey,
        ["verificationKey"] = materials.VerificationKey,
        ["symmetricSigningKey"] = materials.SymmetricSigningKey,
    };

    private static List<EncryptedDataKey> EdksFromWire(Dictionary<string, object> map, string member)
    {
        var edks = new List<EncryptedDataKey>();
        foreach (var element in Model.List(map, member))
        {
            var edk = element as Dictionary<string, object>
                ?? throw ServerErrorException.Generic($"list element is not a structure: {member}");
            edks.Add(new EncryptedDataKey
            {
                KeyProviderId = Model.Str(edk, "keyProviderId"),
                KeyProviderInfo = new MemoryStream(Model.Bytes(edk, "keyProviderInfo")),
                Ciphertext = new MemoryStream(Model.Bytes(edk, "ciphertext")),
            });
        }
        return edks;
    }

    private static List<object> EdksToWire(List<EncryptedDataKey> edks) =>
        (edks ?? new List<EncryptedDataKey>())
            .Select(edk => (object)new Dictionary<string, object>
            {
                ["keyProviderId"] = edk.KeyProviderId,
                ["keyProviderInfo"] = edk.KeyProviderInfo,
                ["ciphertext"] = edk.Ciphertext,
            })
            .ToList();

    // ------------------------------------------------------------------
    // Enums
    // ------------------------------------------------------------------

    private static AlgorithmSuiteId SuiteId(string wire) =>
        new() { ESDK = Constant<ESDKAlgorithmSuiteId>(wire, "algorithm suite") };

    private AlgorithmSuiteInfo SuiteInfo(string wire) =>
        _suiteInfo.TryGetValue(wire, out var info)
            ? info
            : throw ServerErrorException.Generic($"unknown algorithm suite: {wire}");

    private static string SuiteToWire(AlgorithmSuiteId id)
    {
        if (id.ESDK == null)
        {
            throw ServerErrorException.Generic("the MPL returned a non-ESDK algorithm suite, which the model cannot carry");
        }
        foreach (var field in ConstantFields<ESDKAlgorithmSuiteId>())
        {
            if (((ESDKAlgorithmSuiteId)field.GetValue(null)).Value == id.ESDK.Value)
            {
                return field.Name;
            }
        }
        throw ServerErrorException.Generic($"unrecognized ESDK algorithm suite {id.ESDK.Value}");
    }

    private static CommitmentPolicy Policy(string wire)
    {
        if (!wire.StartsWith(EsdkPolicyPrefix, StringComparison.Ordinal))
        {
            throw ServerErrorException.Generic($"unknown commitment policy: {wire}");
        }
        return new CommitmentPolicy
        {
            ESDK = Constant<ESDKCommitmentPolicy>(wire.Substring(EsdkPolicyPrefix.Length), "commitment policy"),
        };
    }

    /// The generated MPL enums are ConstantClass subclasses with one static
    /// field per constant, named exactly as the model (and the wire) names it.
    private static T Constant<T>(string name, string kind) where T : class
    {
        var field = typeof(T).GetField(name, BindingFlags.Public | BindingFlags.Static);
        return field?.FieldType == typeof(T)
            ? (T)field.GetValue(null)
            : throw ServerErrorException.Generic($"unknown {kind}: {name}");
    }

    private static IEnumerable<FieldInfo> ConstantFields<T>() =>
        typeof(T).GetFields(BindingFlags.Public | BindingFlags.Static).Where(f => f.FieldType == typeof(T));

    // ------------------------------------------------------------------
    // Registry + error boundary
    // ------------------------------------------------------------------

    private static string Register<T>(ConcurrentDictionary<string, T> registry, T resource)
    {
        var id = Guid.NewGuid().ToString();
        registry[id] = resource;
        return id;
    }

    private static T Lookup<T>(ConcurrentDictionary<string, T> registry, string id, string member)
    {
        if (string.IsNullOrEmpty(id))
        {
            throw ServerErrorException.Generic($"{member} must be non-empty");
        }
        return registry.TryGetValue(id, out var resource)
            ? resource
            : throw ServerErrorException.Generic($"unknown {member}: {id}");
    }

    /// Anything the MPL throws is the MPL's rejection.
    private static T Call<T>(Func<T> call)
    {
        try
        {
            return call();
        }
        catch (ServerErrorException)
        {
            throw;
        }
        catch (Exception e)
        {
            throw ServerErrorException.Mpl(e.Message);
        }
    }
}
