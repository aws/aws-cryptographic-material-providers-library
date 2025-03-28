// Class DBECommitmentPolicy
// Dafny class DBECommitmentPolicy compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DBECommitmentPolicy {
  public DBECommitmentPolicy () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DBECommitmentPolicy o = (DBECommitmentPolicy)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DBECommitmentPolicy> _TYPE = dafny.TypeDescriptor.<DBECommitmentPolicy>referenceWithInitializer(DBECommitmentPolicy.class, () -> DBECommitmentPolicy.Default());
  public static dafny.TypeDescriptor<DBECommitmentPolicy> _typeDescriptor() {
    return (dafny.TypeDescriptor<DBECommitmentPolicy>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DBECommitmentPolicy theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy.create();
  public static DBECommitmentPolicy Default() {
    return theDefault;
  }
  public static DBECommitmentPolicy create() {
    return new DBECommitmentPolicy();
  }
  public static DBECommitmentPolicy create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT() {
    return create();
  }
  public boolean is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT() { return true; }
  public static java.util.ArrayList<DBECommitmentPolicy> AllSingletonConstructors() {
    java.util.ArrayList<DBECommitmentPolicy> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DBECommitmentPolicy());
    return singleton_iterator;
  }
}
