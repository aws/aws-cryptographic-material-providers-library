// Class KeyDescription_RequiredEncryptionContext
// Dafny class KeyDescription_RequiredEncryptionContext compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_RequiredEncryptionContext extends KeyDescription {
  public RequiredEncryptionContextCMM _RequiredEncryptionContext;
  public KeyDescription_RequiredEncryptionContext (RequiredEncryptionContextCMM RequiredEncryptionContext) {
    super();
    this._RequiredEncryptionContext = RequiredEncryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_RequiredEncryptionContext o = (KeyDescription_RequiredEncryptionContext)other;
    return true && java.util.Objects.equals(this._RequiredEncryptionContext, o._RequiredEncryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 11;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RequiredEncryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.RequiredEncryptionContext");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RequiredEncryptionContext));
    s.append(")");
    return s.toString();
  }
}
