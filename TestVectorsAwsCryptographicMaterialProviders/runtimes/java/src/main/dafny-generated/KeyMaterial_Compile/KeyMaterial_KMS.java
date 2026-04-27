// Class KeyMaterial_KMS
// Dafny class KeyMaterial_KMS compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_KMS extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _name;
  public boolean _encrypt;
  public boolean _decrypt;
  public dafny.DafnySequence<? extends Character> _keyIdentifier;
  public KeyMaterial_KMS (dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier) {
    super();
    this._name = name;
    this._encrypt = encrypt;
    this._decrypt = decrypt;
    this._keyIdentifier = keyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_KMS o = (KeyMaterial_KMS)other;
    return true && java.util.Objects.equals(this._name, o._name) && this._encrypt == o._encrypt && this._decrypt == o._decrypt && java.util.Objects.equals(this._keyIdentifier, o._keyIdentifier);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._encrypt);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._decrypt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyIdentifier);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.KMS");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(this._encrypt);
    s.append(", ");
    s.append(this._decrypt);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyIdentifier));
    s.append(")");
    return s.toString();
  }
}
