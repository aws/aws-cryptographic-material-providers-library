// Class CommitmentPolicy
// Dafny class CommitmentPolicy compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CommitmentPolicy {
  public CommitmentPolicy() {
  }
  private static final dafny.TypeDescriptor<CommitmentPolicy> _TYPE = dafny.TypeDescriptor.<CommitmentPolicy>referenceWithInitializer(CommitmentPolicy.class, () -> CommitmentPolicy.Default());
  public static dafny.TypeDescriptor<CommitmentPolicy> _typeDescriptor() {
    return (dafny.TypeDescriptor<CommitmentPolicy>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CommitmentPolicy theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(ESDKCommitmentPolicy.Default());
  public static CommitmentPolicy Default() {
    return theDefault;
  }
  public static CommitmentPolicy create_ESDK(ESDKCommitmentPolicy ESDK) {
    return new CommitmentPolicy_ESDK(ESDK);
  }
  public static CommitmentPolicy create_DBE(DBECommitmentPolicy DBE) {
    return new CommitmentPolicy_DBE(DBE);
  }
  public boolean is_ESDK() { return this instanceof CommitmentPolicy_ESDK; }
  public boolean is_DBE() { return this instanceof CommitmentPolicy_DBE; }
  public ESDKCommitmentPolicy dtor_ESDK() {
    CommitmentPolicy d = this;
    return ((CommitmentPolicy_ESDK)d)._ESDK;
  }
  public DBECommitmentPolicy dtor_DBE() {
    CommitmentPolicy d = this;
    return ((CommitmentPolicy_DBE)d)._DBE;
  }
}
