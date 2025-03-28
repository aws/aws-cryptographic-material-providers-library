// Class KeyState_PendingDeletion
// Dafny class KeyState_PendingDeletion compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyState_PendingDeletion extends KeyState {
  public KeyState_PendingDeletion () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyState_PendingDeletion o = (KeyState_PendingDeletion)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeyState.PendingDeletion");
    return s.toString();
  }
}
