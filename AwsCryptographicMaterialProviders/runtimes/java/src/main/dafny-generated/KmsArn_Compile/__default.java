// Class __default
// Dafny class __default compiled into Java
package KmsArn_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean ValidKmsArn_q(dafny.DafnySequence<? extends Character> input) {
    return (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(input)) && (((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>>, Boolean>Let(AwsArnParsing_Compile.__default.ParseAwsKmsArn(input), boxed0 -> {
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>> _pat_let0_0 = ((Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed0));
      return ((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>>, Boolean>Let(_pat_let0_0, boxed1 -> {
        Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>> _0_maybeParsed = ((Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed1));
        return ((_0_maybeParsed).is_Success()) && (((((_0_maybeParsed).dtor_value()).dtor_resource()).dtor_resourceType()).equals(dafny.DafnySequence.asString("key")));
      }
      )));
    }
    ))));
  }
  public static Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error> IsValidKeyArn(dafny.DafnySequence<? extends Character> input) {
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(input), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.KMS__CONFIG__KMS__ARN__INVALID()));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<AwsArnParsing_Compile.AwsArn>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), AwsArnParsing_Compile.AwsKmsArn._typeDescriptor());
    } else {
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error> _1_valueOrError1 = (AwsArnParsing_Compile.__default.ParseAwsKmsArn(input)).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_2_error_boxed0) -> {
        dafny.DafnySequence<? extends Character> _2_error = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_2_error_boxed0));
        return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(KeyStoreErrorMessages_Compile.__default.KMS__CONFIG__KMS__ARN__INVALID(), dafny.DafnySequence.asString(". ")), _2_error));
      }));
      if ((_1_valueOrError1).IsFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        return (_1_valueOrError1).<AwsArnParsing_Compile.AwsArn>PropagateFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), AwsArnParsing_Compile.AwsKmsArn._typeDescriptor());
      } else {
        AwsArnParsing_Compile.AwsArn _3_arn = (_1_valueOrError1).Extract(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
        if (!(((_3_arn).dtor_resource()).dtor_resourceType()).equals(dafny.DafnySequence.asString("key"))) {
          return Wrappers_Compile.Result.<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(KeyStoreErrorMessages_Compile.__default.ALIAS__NOT__ALLOWED()));
        } else {
          return Wrappers_Compile.Result.<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), _3_arn);
        }
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "KmsArn._default";
  }
}
