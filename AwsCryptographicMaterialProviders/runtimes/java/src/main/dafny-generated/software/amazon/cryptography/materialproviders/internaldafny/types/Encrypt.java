// Class Encrypt
// Dafny class Encrypt compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Encrypt {
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _AES__GCM;
  public Encrypt (software.amazon.cryptography.primitives.internaldafny.types.AES__GCM AES__GCM) {
    this._AES__GCM = AES__GCM;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Encrypt o = (Encrypt)other;
    return true && java.util.Objects.equals(this._AES__GCM, o._AES__GCM);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AES__GCM);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.Encrypt.AES_GCM");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AES__GCM));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Encrypt> _TYPE = dafny.TypeDescriptor.<Encrypt>referenceWithInitializer(Encrypt.class, () -> Encrypt.Default());
  public static dafny.TypeDescriptor<Encrypt> _typeDescriptor() {
    return (dafny.TypeDescriptor<Encrypt>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Encrypt theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt.create(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.Default());
  public static Encrypt Default() {
    return theDefault;
  }
  public static Encrypt create(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM AES__GCM) {
    return new Encrypt(AES__GCM);
  }
  public static Encrypt create_AES__GCM(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM AES__GCM) {
    return create(AES__GCM);
  }
  public boolean is_AES__GCM() { return true; }
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM dtor_AES__GCM() {
    return this._AES__GCM;
  }
}
