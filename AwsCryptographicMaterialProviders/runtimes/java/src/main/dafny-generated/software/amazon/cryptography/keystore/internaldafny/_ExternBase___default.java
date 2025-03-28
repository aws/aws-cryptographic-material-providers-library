// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.keystore.internaldafny;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig DefaultKeyStoreConfig() {
    return software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig.create(dafny.DafnySequence.asString("None"), software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(dafny.DafnySequence.asString("arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab")), dafny.DafnySequence.asString("None"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class))), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))));
  }
  public static Wrappers_Compile.Result<KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> KeyStore(software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig config)
  {
    Wrappers_Compile.Result<KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> res = (Wrappers_Compile.Result<KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _0_kmsClient = null;
    software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient _1_ddbClient = null;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2_inferredRegion;
    _2_inferredRegion = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    if (KMSKeystoreOperations_Compile.__default.HasKeyId((config).dtor_kmsConfiguration())) {
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError0 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      _3_valueOrError0 = KmsArn_Compile.__default.IsValidKeyArn(KMSKeystoreOperations_Compile.__default.GetKeyId((config).dtor_kmsConfiguration()));
      if ((_3_valueOrError0).IsFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_3_valueOrError0).<KeyStoreClient>PropagateFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      AwsArnParsing_Compile.AwsArn _4_parsedArn;
      _4_parsedArn = (_3_valueOrError0).Extract(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _2_inferredRegion = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_4_parsedArn).dtor_region());
    } else if (((config).dtor_kmsConfiguration()).is_mrDiscovery()) {
      _2_inferredRegion = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.RegionType._typeDescriptor(), (((config).dtor_kmsConfiguration()).dtor_mrDiscovery()).dtor_region());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_grantTokens;
    _5_grantTokens = AwsKmsUtils_Compile.__default.GetValidGrantTokens((config).dtor_grantTokens());
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (true) && ((_5_grantTokens).is_Success()), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Grant Tokens passed to Key Store configuration are invalid.")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<KeyStoreClient>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
      return res;
    }
    dafny.DafnySequence<? extends Character> _7_keyStoreId = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    if (((config).dtor_id()).is_Some()) {
      _7_keyStoreId = ((config).dtor_id()).dtor_value();
    } else {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _8_maybeUuid;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = UUID.__default.GenerateUUID();
      _8_maybeUuid = _out0;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _9_valueOrError2 = (_8_maybeUuid).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_10_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _10_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_10_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_10_e);
      }));
      if ((_9_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_9_valueOrError2).<KeyStoreClient>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      dafny.DafnySequence<? extends Character> _11_uuid;
      _11_uuid = (_9_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _7_keyStoreId = _11_uuid;
    }
    if (((config).dtor_kmsClient()).is_Some()) {
      _0_kmsClient = ((config).dtor_kmsClient()).dtor_value();
    } else if ((((config).dtor_kmsClient()).is_None()) && ((_2_inferredRegion).is_Some())) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _12_maybeKmsClient;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out1;
      _out1 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion((_2_inferredRegion).dtor_value());
      _12_maybeKmsClient = _out1;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _13_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      _13_valueOrError3 = (_12_maybeKmsClient).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_14_e_boxed0) -> {
        software.amazon.cryptography.services.kms.internaldafny.types.Error _14_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_14_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(_14_e);
      }));
      if ((_13_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_13_valueOrError3).<KeyStoreClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      _0_kmsClient = (_13_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    } else {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _15_maybeKmsClient;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out2;
      _out2 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClient();
      _15_maybeKmsClient = _out2;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _16_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      _16_valueOrError4 = (_15_maybeKmsClient).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_17_e_boxed0) -> {
        software.amazon.cryptography.services.kms.internaldafny.types.Error _17_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_17_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(_17_e);
      }));
      if ((_16_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_16_valueOrError4).<KeyStoreClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      _0_kmsClient = (_16_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    }
    if (((config).dtor_ddbClient()).is_Some()) {
      _1_ddbClient = ((config).dtor_ddbClient()).dtor_value();
    } else if ((((config).dtor_ddbClient()).is_None()) && ((_2_inferredRegion).is_Some())) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _18_maybeDdbClient;
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out3;
      _out3 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DDBClientForRegion((_2_inferredRegion).dtor_value());
      _18_maybeDdbClient = _out3;
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _19_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      _19_valueOrError5 = (_18_maybeDdbClient).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.dynamodb.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_20_e_boxed0) -> {
        software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _20_e = ((software.amazon.cryptography.services.dynamodb.internaldafny.types.Error)(java.lang.Object)(_20_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsDynamodb(_20_e);
      }));
      if ((_19_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_19_valueOrError5).<KeyStoreClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      _1_ddbClient = (_19_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    } else {
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _21_maybeDdbClient;
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out4;
      _out4 = software.amazon.cryptography.services.dynamodb.internaldafny.__default.DynamoDBClient();
      _21_maybeDdbClient = _out4;
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.keystore.internaldafny.types.Error> _22_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
      _22_valueOrError6 = (_21_maybeDdbClient).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.dynamodb.internaldafny.types.Error, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_23_e_boxed0) -> {
        software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _23_e = ((software.amazon.cryptography.services.dynamodb.internaldafny.types.Error)(java.lang.Object)(_23_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsDynamodb(_23_e);
      }));
      if ((_22_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        res = (_22_valueOrError6).<KeyStoreClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
        return res;
      }
      _1_ddbClient = (_22_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _24_valueOrError7 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
    _24_valueOrError7 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName((config).dtor_ddbTableName()), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Invalid Amazon DynamoDB Table Name")));
    if ((_24_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      res = (_24_valueOrError7).<KeyStoreClient>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)));
      return res;
    }
    KeyStoreClient _25_client;
    KeyStoreClient _nw0 = new KeyStoreClient();
    _nw0.__ctor(AwsCryptographyKeyStoreOperations_Compile.Config.create(_7_keyStoreId, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (_5_grantTokens).dtor_value(), _0_kmsClient, _1_ddbClient));
    _25_client = _nw0;
    res = Wrappers_Compile.Result.<KeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<KeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), _25_client);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.keystore.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient.class)), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "KeyStore._default";
  }
}
