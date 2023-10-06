// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTestVectorKeysTypes.dfy"
  // Yes, this is reaching across.
  // idealy all these functions would exist in the STD Library.
include "../../TestVectorsAwsCryptographicMaterialProviders/src/LibraryIndex.dfy"
include "../../TestVectorsAwsCryptographicMaterialProviders/src/JSONHelpers.dfy"
include "KeyDescription.dfy"
include "KeyMaterial.dfy"
include "KeyringFromKeyDescription.dfy"
include "CmmFromKeyDescription.dfy"

module {:options "-functionSyntax:4"} KeysVectorOperations refines AbstractAwsCryptographyMaterialProvidersTestVectorKeysOperations {
  import JSON.API
  import JSON.Errors
  import JSON.Values
  import KeyDescription
  import MPL = AwsCryptographyMaterialProvidersTypes
  import KeyMaterial
  import KeyringFromKeyDescription
  import CmmFromKeyDescription
  import WrappedMaterialProviders
  import MaterialProviders

  datatype Config = Config(
    keys: map<string, KeyMaterial.KeyMaterial>
  )

  type InternalConfig = Config
  ghost predicate ValidInternalConfig?(config: InternalConfig)
  {
    true
  }
  ghost function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    {}
  }

  predicate CreateTestVectorKeyringEnsuresPublicly(
    input: TestVectorKeyringInput ,
    output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  {true}
  method CreateTestVectorKeyring ( config: InternalConfig , input: TestVectorKeyringInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  {

    :- Need(
      && !input.keyDescription.RequiredEncryptionContext?
      && !input.keyDescription.Caching?,
      KeyVectorException( message := "CMM key descriptions are not supported ")
    );

    var info := ToKeyringInfo(config, input.keyDescription);

    var maybeMpl := MaterialProviders.MaterialProviders();
    var mpl :- maybeMpl.MapFailure(e => AwsCryptographyMaterialProviders(e));
    output := KeyringFromKeyDescription.ToKeyring(mpl, info);
  }

  predicate CreateWappedTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput ,
                                                         output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  {true}

  method CreateWappedTestVectorKeyring ( config: InternalConfig , input: TestVectorKeyringInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  {

    :- Need(
      && !input.keyDescription.RequiredEncryptionContext?
      && !input.keyDescription.Caching?,
      KeyVectorException( message := "CMM key descriptions are not supported ")
    );

    var info := ToKeyringInfo(config, input.keyDescription);

    var maybeMpl := WrappedMaterialProviders.WrappedMaterialProviders();
    var wrappedMPL :- maybeMpl.MapFailure(e => AwsCryptographyMaterialProviders(e));

    output := KeyringFromKeyDescription.ToKeyring(wrappedMPL, info);
  }

  predicate CreateWrappedTestVectorCmmEnsuresPublicly(
    input: TestVectorCmmInput ,
    output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
  {true}

  method CreateWrappedTestVectorCmm ( config: InternalConfig , input: TestVectorCmmInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
  {
    var info := ToKeyringInfo(config, input.keyDescription);
    var maybeMpl := WrappedMaterialProviders.WrappedMaterialProviders();
    var wrappedMPL :- maybeMpl.MapFailure(e => AwsCryptographyMaterialProviders(e));

    output := CmmFromKeyDescription.ToCmm(wrappedMPL, info, input.forOperation);
  }

  function GetKeyDescription ( config: InternalConfig , input: GetKeyDescriptionInput )
    : (output: Result<GetKeyDescriptionOutput, Error>)
  {
    var keyDescriptionJSON :- API.Deserialize(input.json)
                              .MapFailure((e: Errors.DeserializationError)  => AwsCryptographyMaterialProviders(
                                              AwsCryptographyMaterialProvidersTypes.AwsCryptographicMaterialProvidersException(
                                                message := e.ToString()
                                              )));
    var keyDescription :- KeyDescription.ToKeyDescription(keyDescriptionJSON)
                          .MapFailure(e => AwsCryptographyMaterialProviders(
                                          AwsCryptographyMaterialProvidersTypes.AwsCryptographicMaterialProvidersException(
                                            message := e
                                          )));
    Success(GetKeyDescriptionOutput(
              keyDescription := keyDescription
            ))
  }

  function SerializeKeyDescription ( config: InternalConfig , input: SerializeKeyDescriptionInput )
    : (output: Result<SerializeKeyDescriptionOutput, Error>)
  {
    Failure(KeyVectorException( message := "Not Supported"))
  }

  function GetKeyId(input: Types.KeyDescription)
    : string
  {
    match input
    case Kms(i) => i.keyId
    case KmsMrk(i) => i.keyId
    case KmsMrkDiscovery(i) => i.keyId
    case RSA(i) => i.keyId
    case AES(i) => i.keyId
    case Static(i) => i.keyId
    case Hierarchy(i) => i.keyId
    case KmsRsa(i) => i.keyId
    case RequiredEncryptionContext(i) => GetKeyId(i.underlying)
    case Caching(i) => GetKeyId(i.underlying)
  }

  function ToKeyringInfo(
    config: InternalConfig,
    keyDescription: Types.KeyDescription
  )
    : KeyringFromKeyDescription.KeyringInfo
  {
    var keyId := GetKeyId(keyDescription);

    KeyringFromKeyDescription.KeyringInfo(
      keyDescription,
      if keyId in config.keys then
        Some(config.keys[keyId])
      else
        None
    )
  }

}
