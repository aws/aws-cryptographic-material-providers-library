// Class KeyState_PendingReplicaDeletion
// Dafny class KeyState_PendingReplicaDeletion compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyState_PendingReplicaDeletion extends KeyState {
  public KeyState_PendingReplicaDeletion () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyState_PendingReplicaDeletion o = (KeyState_PendingReplicaDeletion)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeyState.PendingReplicaDeletion");
    return s.toString();
  }
}
