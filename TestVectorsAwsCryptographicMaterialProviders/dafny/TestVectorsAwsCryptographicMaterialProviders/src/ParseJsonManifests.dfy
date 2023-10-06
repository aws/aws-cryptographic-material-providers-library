// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypesWrapped.dfy"
include "JSONHelpers.dfy"
include "TestVectors.dfy"
include "CompleteVectors.dfy"

module {:options "-functionSyntax:4"} ParseJsonManifests {

  import Types = AwsCryptographyMaterialProvidersTypes

  import JSON.API
  import opened JSON.Values
  import JSON.Errors
  import opened Wrappers
  import UTF8
  import Seq
  import opened StandardLibrary.UInt
  import BoundedInts
  import opened JSONHelpers
  import opened TestVectors
  import HexStrings
  import Base64
  import CompleteVectors
  import KeyVectors
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
    // This is a HACK!
    // This is *ONLY* because this is wrapping the MPL
  import AlgorithmSuites

  function BuildEncryptTestVector(keys: KeyVectors.KeyVectorsClient, obj: seq<(string, JSON)>)
    : Result<seq<EncryptTestVector>, string>
  {
    if |obj| == 0 then
      Success([])
    else
      var name := obj[0].0;
      var encryptVector :- ToEncryptTestVector(keys, name, obj[0].1);
      var tail :- BuildEncryptTestVector(keys, obj[1..]);
      Success([ encryptVector ] + tail)
  }

  function ToEncryptTestVector(keys: KeyVectors.KeyVectorsClient, name: string, obj: JSON)
    : Result<EncryptTestVector, string>
  {
    :- Need(obj.Object?, "EncryptTestVector not an object");
    var obj := obj.obj;
    var typString := "type";
    var typ :- GetString(typString, obj);

    var description := GetString("description", obj).ToOption();

    var encryptionContextStrings :- SmallObjectToStringStringMap("encryptionContext", obj);
    var encryptionContext :- utf8EncodeMap(encryptionContextStrings);

    // TODO change this to use AlgorithmSuiteInfoByHexString
    var algorithmSuiteHex :- GetString("algorithmSuiteId", obj);
    :- Need(HexStrings.IsLooseHexString(algorithmSuiteHex), "Not hex encoded binary");
    var binaryId := HexStrings.FromHexString(algorithmSuiteHex);
    var algorithmSuite :- AlgorithmSuites
                          .GetAlgorithmSuiteInfo(binaryId)
                          .MapFailure(e => "Invalid Suite:" + algorithmSuiteHex);

    var keysAsStrings := GetArrayString("requiredEncryptionContextKeys", obj).ToOption();
    var requiredEncryptionContextKeys :- match keysAsStrings
    case Some(s) =>
      var k :- utf8EncodeSeq(keysAsStrings.value);
      Success(Some(k))
    case None() => Success(None());
                                         
    var reproducedEncryptionContextStrings :- GetOptionalSmallObjectToStringStringMap("reproducedEncryptionContext", obj);
    var reproducedEncryptionContext :- match reproducedEncryptionContextStrings
      case Some(r) =>
        var e :- utf8EncodeMap(r);
        Success(Some(e))
      case None() => Success(None());

    // TODO fix me
    var commitmentPolicy := CompleteVectors.AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite);
    // This MAY be too flexible. If the length is say a string, this will return None
    var maxPlaintextLength := GetPositiveLong("maxPlaintextLength", obj).ToOption();

    match typ
    case "positive-keyring" =>
      var encryptKeyDescription :- GetKeyDescription(keys, "encryptKeyDescription", obj);
      var decryptKeyDescription :- GetKeyDescription(keys, "decryptKeyDescription", obj);

      Success(PositiveEncryptKeyringVector(
                name := name,
                description := description,
                encryptionContext := encryptionContext,
                commitmentPolicy := commitmentPolicy,
                algorithmSuite := algorithmSuite,
                maxPlaintextLength := maxPlaintextLength,
                requiredEncryptionContextKeys := requiredEncryptionContextKeys,
                encryptDescription := encryptKeyDescription,
                decryptDescription := decryptKeyDescription,
                reproducedEncryptionContext := reproducedEncryptionContext
              ))
    case "negative-encrypt-keyring" =>
      var keyDescription :- GetKeyDescription(keys, "keyDescription", obj);
      var errorDescription :- GetString("errorDescription", obj);

      Success(NegativeEncryptKeyringVector(
                name := name,
                description := description,
                encryptionContext := encryptionContext,
                commitmentPolicy := commitmentPolicy,
                algorithmSuite := algorithmSuite,
                maxPlaintextLength := maxPlaintextLength,
                requiredEncryptionContextKeys := requiredEncryptionContextKeys,
                errorDescription := errorDescription,
                keyDescription := keyDescription
              ))

    case "negative-decrypt-keyring" =>
      var encryptKeyDescription :- GetKeyDescription(keys, "encryptKeyDescription", obj);
      var decryptKeyDescription :- GetKeyDescription(keys, "decryptKeyDescription", obj);
      var decryptErrorDescription :- GetString("decryptErrorDescription", obj);

      Success(PositiveEncryptNegativeDecryptKeyringVector(
                name := name,
                description := description,
                decryptErrorDescription := decryptErrorDescription,
                encryptionContext := encryptionContext,
                commitmentPolicy := commitmentPolicy,
                algorithmSuite := algorithmSuite,
                maxPlaintextLength := maxPlaintextLength,
                requiredEncryptionContextKeys := requiredEncryptionContextKeys,
                encryptDescription := encryptKeyDescription,
                decryptDescription := decryptKeyDescription,
                reproducedEncryptionContext := reproducedEncryptionContext
              ))

    case _ => Failure("Unsupported EncryptTestVector type:" + typ)
  }

  function GetKeyDescription(
    keyVectorClient: KeyVectors.KeyVectorsClient,
    key: string,
    obj: seq<(string, JSON)>
  )
    : Result<KeyVectorsTypes.KeyDescription, string>
  {
    var keyDescriptionObject :- Get(key, obj);

    // Be nice if `document` mapped to `JSON.Values.JSON`
    var descriptionStr :- API.Serialize(keyDescriptionObject)
                          .MapFailure((e: Errors.SerializationError) => e.ToString());

    var keyDescriptionOutput :- keyVectorClient
                                .GetKeyDescription(KeyVectorsTypes.GetKeyDescriptionInput(
                                                     json := descriptionStr
                                                   ))
                                .MapFailure(ErrorToString);

    Success(keyDescriptionOutput.keyDescription)
  }

  function ErrorToString(e: KeyVectorsTypes.Error): string
  {
    match e
    case KeyVectorException(message) => message
    case AwsCryptographyMaterialProviders(mplError) => (
      match mplError
      case AwsCryptographicMaterialProvidersException(message) => message
      case _ => "Unmapped AwsCryptographyMaterialProviders" )
    case _ => "Unmapped KeyVectorException"
  }
}
