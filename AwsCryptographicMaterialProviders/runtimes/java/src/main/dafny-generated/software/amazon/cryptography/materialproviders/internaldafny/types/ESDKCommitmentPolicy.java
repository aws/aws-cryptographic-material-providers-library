// Class ESDKCommitmentPolicy
// Dafny class ESDKCommitmentPolicy compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ESDKCommitmentPolicy {
  public ESDKCommitmentPolicy() {
  }
  private static final dafny.TypeDescriptor<ESDKCommitmentPolicy> _TYPE = dafny.TypeDescriptor.<ESDKCommitmentPolicy>referenceWithInitializer(ESDKCommitmentPolicy.class, () -> ESDKCommitmentPolicy.Default());
  public static dafny.TypeDescriptor<ESDKCommitmentPolicy> _typeDescriptor() {
    return (dafny.TypeDescriptor<ESDKCommitmentPolicy>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ESDKCommitmentPolicy theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_FORBID__ENCRYPT__ALLOW__DECRYPT();
  public static ESDKCommitmentPolicy Default() {
    return theDefault;
  }
  public static ESDKCommitmentPolicy create_FORBID__ENCRYPT__ALLOW__DECRYPT() {
    return new ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT();
  }
  public static ESDKCommitmentPolicy create_REQUIRE__ENCRYPT__ALLOW__DECRYPT() {
    return new ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT();
  }
  public static ESDKCommitmentPolicy create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT() {
    return new ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT();
  }
  public boolean is_FORBID__ENCRYPT__ALLOW__DECRYPT() { return this instanceof ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT; }
  public boolean is_REQUIRE__ENCRYPT__ALLOW__DECRYPT() { return this instanceof ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT; }
  public boolean is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT() { return this instanceof ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT; }
  public static java.util.ArrayList<ESDKCommitmentPolicy> AllSingletonConstructors() {
    java.util.ArrayList<ESDKCommitmentPolicy> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT());
    singleton_iterator.add(new ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT());
    singleton_iterator.add(new ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT());
    return singleton_iterator;
  }
}
