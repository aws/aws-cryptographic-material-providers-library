// Class __default
// Dafny class __default compiled into Java
package KeyStoreErrorMessages_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> GET__KEY__ARN__DISAGREEMENT()
  {
    return dafny.DafnySequence.asString("Branch key's KMS Key ARN read from Dynamodb does not match Key Store's configured KMS Key ARN.");
  }
  public static dafny.DafnySequence<? extends Character> VERSION__KEY__KMS__KEY__ARN__DISAGREEMENT()
  {
    return __default.GET__KEY__ARN__DISAGREEMENT();
  }
  public static dafny.DafnySequence<? extends Character> KMS__CONFIG__KMS__ARN__INVALID()
  {
    return dafny.DafnySequence.asString("KMSConfiguration's KMS Key ARN is invalid.");
  }
  public static dafny.DafnySequence<? extends Character> CUSTOM__BRANCH__KEY__ID__NEED__EC()
  {
    return dafny.DafnySequence.asString("Custom branch key identifier requires custom encryption context.");
  }
  public static dafny.DafnySequence<? extends Character> DISCOVERY__CREATE__KEY__NOT__SUPPORTED()
  {
    return dafny.DafnySequence.asString("Key Store's kmsConfiguration MUST BE kmsKeyArn or kmsMRKeyArn to Create Branch Keys.");
  }
  public static dafny.DafnySequence<? extends Character> DISCOVERY__VERSION__KEY__NOT__SUPPORTED()
  {
    return dafny.DafnySequence.asString("Key Store's kmsConfiguration MUST BE kmsKeyArn or kmsMRKeyArn to Version Branch Keys.");
  }
  public static dafny.DafnySequence<? extends Character> UTF8__ENCODING__ENCRYPTION__CONTEXT__ERROR()
  {
    return dafny.DafnySequence.asString("Unable to UTF8 Encode element of Encryption Context.");
  }
  public static dafny.DafnySequence<? extends Character> ALIAS__NOT__ALLOWED()
  {
    return dafny.DafnySequence.asString("Key Store encountered a KMS Alias ARN instead of a KMS Key ARN, which is not allowed.");
  }
  public static dafny.DafnySequence<? extends Character> NO__CORRESPONDING__BRANCH__KEY()
  {
    return dafny.DafnySequence.asString("No item found for corresponding branch key identifier.");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ID__NEEDED()
  {
    return dafny.DafnySequence.asString("Empty string not supported for branch key identifier.");
  }
  public static dafny.DafnySequence<? extends Character> RETRIEVED__KEYSTORE__ITEM__INVALID__KMS__ARN()
  {
    return dafny.DafnySequence.asString("The `kms-arn` field for the requested branch key identifier is corrupted.");
  }
  @Override
  public java.lang.String toString() {
    return "KeyStoreErrorMessages._default";
  }
}
