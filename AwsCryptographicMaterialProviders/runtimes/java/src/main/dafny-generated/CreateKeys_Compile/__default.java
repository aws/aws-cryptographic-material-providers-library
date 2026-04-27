// Class __default
// Dafny class __default compiled into Java
package CreateKeys_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateBranchAndBeaconKeys(dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> customEncryptionContext, dafny.DafnySequence<? extends Character> timestamp, dafny.DafnySequence<? extends Character> branchKeyVersion, dafny.DafnySequence<? extends Character> ddbTableName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    if(true) {
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _0_decryptOnlyEncryptionContext;
      _0_decryptOnlyEncryptionContext = Structure_Compile.__default.DecryptOnlyBranchKeyEncryptionContext(branchKeyIdentifier, branchKeyVersion, timestamp, logicalKeyStoreName, KMSKeystoreOperations_Compile.__default.GetKeyId(kmsConfiguration), customEncryptionContext);
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _1_activeEncryptionContext;
      _1_activeEncryptionContext = Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_0_decryptOnlyEncryptionContext);
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_beaconEncryptionContext;
      _2_beaconEncryptionContext = Structure_Compile.__default.BeaconKeyEncryptionContext(_0_decryptOnlyEncryptionContext);
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _3_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), KMSKeystoreOperations_Compile.__default.AttemptKmsOperation_q(kmsConfiguration, _0_decryptOnlyEncryptionContext), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext in CreateBranchAndBeaconKeys.")));
      if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_3_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = KMSKeystoreOperations_Compile.__default.GenerateKey(_0_decryptOnlyEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _4_valueOrError1 = _out0;
      if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_4_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse _5_wrappedDecryptOnlyBranchKey;
      _5_wrappedDecryptOnlyBranchKey = (_4_valueOrError1).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _6_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), KMSKeystoreOperations_Compile.__default.AttemptKmsOperation_q(kmsConfiguration, _1_activeEncryptionContext), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid KMS Key ARN configured for ReEncrypt in CreateBranchAndBeaconKeys.")));
      if ((_6_valueOrError2).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_6_valueOrError2).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
      _out1 = KMSKeystoreOperations_Compile.__default.ReEncryptKey(((_5_wrappedDecryptOnlyBranchKey).dtor_CiphertextBlob()).dtor_value(), _0_decryptOnlyEncryptionContext, _1_activeEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _7_valueOrError3 = _out1;
      if ((_7_valueOrError3).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_7_valueOrError3).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse _8_wrappedActiveBranchKey;
      _8_wrappedActiveBranchKey = (_7_valueOrError3).Extract(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _9_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _9_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), KMSKeystoreOperations_Compile.__default.AttemptKmsOperation_q(kmsConfiguration, _2_beaconEncryptionContext), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext(beacon key) in CreateBranchAndBeaconKeys.")));
      if ((_9_valueOrError4).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_9_valueOrError4).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
      _out2 = KMSKeystoreOperations_Compile.__default.GenerateKey(_2_beaconEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _10_valueOrError5 = _out2;
      if ((_10_valueOrError5).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_10_valueOrError5).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse _11_wrappedBeaconKey;
      _11_wrappedBeaconKey = (_10_valueOrError5).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _12_decryptOnlyBranchKeyItem;
      _12_decryptOnlyBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_0_decryptOnlyEncryptionContext, ((_5_wrappedDecryptOnlyBranchKey).dtor_CiphertextBlob()).dtor_value());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _13_activeBranchKeyItem;
      _13_activeBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_1_activeEncryptionContext, ((_8_wrappedActiveBranchKey).dtor_CiphertextBlob()).dtor_value());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _14_beaconKeyItem;
      _14_beaconKeyItem = Structure_Compile.__default.ToAttributeMap(_2_beaconEncryptionContext, ((_11_wrappedBeaconKey).dtor_CiphertextBlob()).dtor_value());
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _15_valueOrError6 = Wrappers_Compile.Result.<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
      _out3 = DDBKeystoreOperations_Compile.__default.WriteNewKeyToStore(_12_decryptOnlyBranchKeyItem, _13_activeBranchKeyItem, _14_beaconKeyItem, ddbTableName, ddbClient);
      _15_valueOrError6 = _out3;
      if ((_15_valueOrError6).IsFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_15_valueOrError6).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput _16___v0;
      _16___v0 = (_15_valueOrError6).Extract(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.create(branchKeyIdentifier));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> VersionActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput input, dafny.DafnySequence<? extends Character> timestamp, dafny.DafnySequence<? extends Character> branchKeyVersion, dafny.DafnySequence<? extends Character> ddbTableName, dafny.DafnySequence<? extends Character> logicalKeyStoreName, software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration kmsConfiguration, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>, software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = DDBKeystoreOperations_Compile.__default.GetActiveBranchKeyItem((input).dtor_branchKeyIdentifier(), ddbTableName, ddbClient);
      _0_valueOrError0 = _out0;
      if ((_0_valueOrError0).IsFailure(Structure_Compile.ActiveBranchKeyItem._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(Structure_Compile.ActiveBranchKeyItem._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _1_oldActiveItem;
      _1_oldActiveItem = (_0_valueOrError0).Extract(Structure_Compile.ActiveBranchKeyItem._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_oldActiveEncryptionContext;
      _2_oldActiveEncryptionContext = Structure_Compile.__default.ToBranchKeyContext(_1_oldActiveItem, logicalKeyStoreName);
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _3_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (true) && (KMSKeystoreOperations_Compile.__default.AttemptKmsOperation_q(kmsConfiguration, _2_oldActiveEncryptionContext)), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.VERSION__KEY__KMS__KEY__ARN__DISAGREEMENT()));
      if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_3_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out1;
      _out1 = KMSKeystoreOperations_Compile.__default.ReEncryptKey((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_1_oldActiveItem).get(Structure_Compile.__default.BRANCH__KEY__FIELD())))).dtor_B(), _2_oldActiveEncryptionContext, _2_oldActiveEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _4_valueOrError2 = _out1;
      if ((_4_valueOrError2).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_4_valueOrError2).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse _5___v1;
      _5___v1 = (_4_valueOrError2).Extract(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _6_decryptOnlyEncryptionContext;
      _6_decryptOnlyEncryptionContext = Structure_Compile.__default.NewVersionFromActiveBranchKeyEncryptionContext(_2_oldActiveEncryptionContext, branchKeyVersion, timestamp);
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _7_activeEncryptionContext;
      _7_activeEncryptionContext = Structure_Compile.__default.ActiveBranchKeyEncryptionContext(_6_decryptOnlyEncryptionContext);
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
      _out2 = KMSKeystoreOperations_Compile.__default.GenerateKey(_6_decryptOnlyEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _8_valueOrError3 = _out2;
      if ((_8_valueOrError3).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_8_valueOrError3).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse _9_wrappedDecryptOnlyBranchKey;
      _9_wrappedDecryptOnlyBranchKey = (_8_valueOrError3).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
      _out3 = KMSKeystoreOperations_Compile.__default.ReEncryptKey(((_9_wrappedDecryptOnlyBranchKey).dtor_CiphertextBlob()).dtor_value(), _6_decryptOnlyEncryptionContext, _7_activeEncryptionContext, kmsConfiguration, grantTokens, kmsClient);
      _10_valueOrError4 = _out3;
      if ((_10_valueOrError4).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_10_valueOrError4).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse _11_wrappedActiveBranchKey;
      _11_wrappedActiveBranchKey = (_10_valueOrError4).Extract(software.amazon.cryptography.services.kms.internaldafny.types.ReEncryptResponse._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _12_decryptOnlyBranchKeyItem;
      _12_decryptOnlyBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_6_decryptOnlyEncryptionContext, ((_9_wrappedDecryptOnlyBranchKey).dtor_CiphertextBlob()).dtor_value());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _13_activeBranchKeyItem;
      _13_activeBranchKeyItem = Structure_Compile.__default.ToAttributeMap(_7_activeEncryptionContext, ((_11_wrappedActiveBranchKey).dtor_CiphertextBlob()).dtor_value());
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _14_valueOrError5 = Wrappers_Compile.Result.<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput.Default());
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out4;
      _out4 = DDBKeystoreOperations_Compile.__default.WriteNewBranchKeyVersionToKeystore(_12_decryptOnlyBranchKeyItem, _13_activeBranchKeyItem, ddbTableName, ddbClient);
      _14_valueOrError5 = _out4;
      if ((_14_valueOrError5).IsFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_14_valueOrError5).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput _15___v2;
      _15___v2 = (_14_valueOrError5).Extract(software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.create());
    }
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "CreateKeys._default";
  }
}
