// Class __default
// Dafny class __default compiled into Java
package AwsCryptographyKeyStoreOperations_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetKeyStoreInfo(Config config)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput.create((config).dtor_id(), (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_grantTokens(), (config).dtor_kmsConfiguration()));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKeyStore(Config config, software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = CreateKeyStoreTable_Compile.__default.CreateKeyStoreTable((config).dtor_ddbTableName(), (config).dtor_ddbClient());
      _0_valueOrError0 = _out0;
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _1_ddbTableArn;
      _1_ddbTableArn = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_tableName;
      _2_tableName = AwsArnParsing_Compile.__default.ParseAmazonDynamodbTableName(_1_ddbTableArn);
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _3_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((_2_tableName).is_Success()) && (((_2_tableName).dtor_value()).equals((config).dtor_ddbTableName())), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")));
      if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_3_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput._typeDescriptor());
        return output;
      }
      output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput.create(_1_ddbTableArn));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKey(Config config, software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), !(((input).dtor_branchKeyIdentifier()).is_Some()) || ((((input).dtor_encryptionContext()).is_Some()) && ((java.math.BigInteger.valueOf((((input).dtor_encryptionContext()).dtor_value()).size())).signum() == 1)), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.CUSTOM__BRANCH__KEY__ID__NEED__EC()));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), KMSKeystoreOperations_Compile.__default.HasKeyId((config).dtor_kmsConfiguration()), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.DISCOVERY__CREATE__KEY__NOT__SUPPORTED()));
      if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_1_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _2_branchKeyIdentifier = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
      if (((input).dtor_branchKeyIdentifier()).is_None()) {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _3_maybeBranchKeyId;
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
        _out0 = UUID.__default.GenerateUUID();
        _3_maybeBranchKeyId = _out0;
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        _4_valueOrError2 = (_3_maybeBranchKeyId).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_5_e_boxed0) -> {
          dafny.DafnySequence<? extends Character> _5_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_5_e_boxed0));
          return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_5_e);
        }));
        if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
          output = (_4_valueOrError2).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
          return output;
        }
        _2_branchKeyIdentifier = (_4_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      } else {
        Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _6_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
        _6_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((((input).dtor_branchKeyIdentifier()).dtor_value()).length())).signum() == 1, software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Custom branch key id can not be an empty string.")));
        if ((_6_valueOrError3).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
          output = (_6_valueOrError3).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
          return output;
        }
        _2_branchKeyIdentifier = ((input).dtor_branchKeyIdentifier()).dtor_value();
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _7_timestamp_q;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out1;
      _out1 = Time.__default.GetCurrentTimeStamp();
      _7_timestamp_q = _out1;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _8_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _8_valueOrError4 = (_7_timestamp_q).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_9_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _9_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_9_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_9_e);
      }));
      if ((_8_valueOrError4).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_8_valueOrError4).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _10_timestamp;
      _10_timestamp = (_8_valueOrError4).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _11_maybeBranchKeyVersion;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out2;
      _out2 = UUID.__default.GenerateUUID();
      _11_maybeBranchKeyVersion = _out2;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _12_valueOrError5 = (_11_maybeBranchKeyVersion).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_13_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _13_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_13_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_13_e);
      }));
      if ((_12_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_12_valueOrError5).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _14_branchKeyVersion;
      _14_branchKeyVersion = (_12_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _15_unwrapEncryptionContext;
      _15_unwrapEncryptionContext = ((input).dtor_encryptionContext()).UnwrapOr(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnyMap.fromElements());
      dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>> _16_encodedEncryptionContext;
      _16_encodedEncryptionContext = ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>>)(_17_unwrapEncryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
        java.util.ArrayList<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>> _coll0 = new java.util.ArrayList<>();
        for (dafny.DafnySequence<? extends java.lang.Byte> _compr_0_boxed0 : (_17_unwrapEncryptionContext).keySet().Elements()) {
          dafny.DafnySequence<? extends java.lang.Byte> _compr_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_compr_0_boxed0));
          dafny.DafnySequence<? extends java.lang.Byte> _18_k = (dafny.DafnySequence<? extends java.lang.Byte>)_compr_0;
          if (UTF8.ValidUTF8Bytes._Is(_18_k)) {
            if ((_17_unwrapEncryptionContext).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_18_k)) {
              _coll0.add(dafny.Tuple3.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>create(UTF8.__default.Decode(_18_k), UTF8.__default.Decode(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_17_unwrapEncryptionContext).get(_18_k)))), _18_k));
            }
          }
        }
        return new dafny.DafnySet<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>(_coll0);
      })).apply()).apply(_15_unwrapEncryptionContext);
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _19_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _19_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>, Boolean>)(_20_encodedEncryptionContext) -> dafny.Helpers.Quantifier((_20_encodedEncryptionContext).Elements(), true, ((_forall_var_0_boxed0) -> {
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _forall_var_0 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_forall_var_0_boxed0));
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _21_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)_forall_var_0;
        return !((_20_encodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>contains(_21_i)) || ((((((_21_i).dtor__0()).is_Success()) && (((_21_i).dtor__1()).is_Success())) && (software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__AttributeName(dafny.DafnySequence.<Character>concatenate(Structure_Compile.__default.ENCRYPTION__CONTEXT__PREFIX(), ((_21_i).dtor__0()).dtor_value())))) && (((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Boolean>Let(UTF8.__default.Encode(((_21_i).dtor__0()).dtor_value()), boxed2 -> {
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _pat_let1_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed2));
          return ((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Boolean>Let(_pat_let1_0, boxed3 -> {
            Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _22_encoded = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed3));
            return ((_22_encoded).is_Success()) && (((_21_i).dtor__2()).equals((_22_encoded).dtor_value()));
          }
          )));
        }
        )))));
      }))).apply(_16_encodedEncryptionContext), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.UTF8__ENCODING__ENCRYPTION__CONTEXT__ERROR()));
      if ((_19_valueOrError6).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_19_valueOrError6).<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out3;
      _out3 = CreateKeys_Compile.__default.CreateBranchAndBeaconKeys(_2_branchKeyIdentifier, ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(_23_encodedEncryptionContext) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(() -> {
        java.util.HashMap<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _coll1 = new java.util.HashMap<>();
        for (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (_23_encodedEncryptionContext).Elements()) {
          dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
          dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _24_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
          if ((_23_encodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>contains(_24_i)) {
            _coll1.put(((_24_i).dtor__0()).dtor_value(),((_24_i).dtor__1()).dtor_value());
          }
        }
        return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>>(_coll1);
      })).apply()).apply(_16_encodedEncryptionContext), _10_timestamp, _14_branchKeyVersion, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (config).dtor_grantTokens(), (config).dtor_kmsClient(), (config).dtor_ddbClient());
      output = _out3;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> VersionKey(Config config, software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), KMSKeystoreOperations_Compile.__default.HasKeyId((config).dtor_kmsConfiguration()), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.DISCOVERY__VERSION__KEY__NOT__SUPPORTED()));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf(((input).dtor_branchKeyIdentifier()).length())).signum() == 1, software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.BRANCH__KEY__ID__NEEDED()));
      if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_1_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_timestamp_q;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = Time.__default.GetCurrentTimeStamp();
      _2_timestamp_q = _out0;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _3_valueOrError2 = (_2_timestamp_q).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_4_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _4_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_4_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_4_e);
      }));
      if ((_3_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_3_valueOrError2).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _5_timestamp;
      _5_timestamp = (_3_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _6_maybeBranchKeyVersion;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out1;
      _out1 = UUID.__default.GenerateUUID();
      _6_maybeBranchKeyVersion = _out1;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _7_valueOrError3 = (_6_maybeBranchKeyVersion).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_8_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _8_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_8_e_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_8_e);
      }));
      if ((_7_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        output = (_7_valueOrError3).<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends Character> _9_branchKeyVersion;
      _9_branchKeyVersion = (_7_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out2;
      _out2 = CreateKeys_Compile.__default.VersionActiveBranchKey(input, _5_timestamp, _9_branchKeyVersion, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (config).dtor_grantTokens(), (config).dtor_kmsClient(), (config).dtor_ddbClient());
      output = _out2;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetActiveBranchKey(Config config, software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = GetKeys_Compile.__default.GetActiveKeyAndUnwrap(input, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (config).dtor_grantTokens(), (config).dtor_kmsClient(), (config).dtor_ddbClient());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBranchKeyVersion(Config config, software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = GetKeys_Compile.__default.GetBranchKeyVersion(input, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (config).dtor_grantTokens(), (config).dtor_kmsClient(), (config).dtor_ddbClient());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> GetBeaconKey(Config config, software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out0;
      _out0 = GetKeys_Compile.__default.GetBeaconKeyAndUnwrap(input, (config).dtor_ddbTableName(), (config).dtor_logicalKeyStoreName(), (config).dtor_kmsConfiguration(), (config).dtor_grantTokens(), (config).dtor_kmsClient(), (config).dtor_ddbClient());
      output = _out0;
    }
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyKeyStoreOperations._default";
  }
}
