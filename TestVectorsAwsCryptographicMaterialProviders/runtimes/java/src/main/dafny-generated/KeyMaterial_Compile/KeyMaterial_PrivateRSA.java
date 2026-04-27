// Class KeyMaterial_PrivateRSA
// Dafny class KeyMaterial_PrivateRSA compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_PrivateRSA extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _name;
  public boolean _encrypt;
  public boolean _decrypt;
  public dafny.DafnySequence<? extends Character> _algorithm;
  public java.math.BigInteger _bits;
  public dafny.DafnySequence<? extends Character> _encoding;
  public dafny.DafnySequence<? extends Character> _material;
  public dafny.DafnySequence<? extends Character> _keyIdentifier;
  public KeyMaterial_PrivateRSA (dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> algorithm, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends Character> material, dafny.DafnySequence<? extends Character> keyIdentifier) {
    super();
    this._name = name;
    this._encrypt = encrypt;
    this._decrypt = decrypt;
    this._algorithm = algorithm;
    this._bits = bits;
    this._encoding = encoding;
    this._material = material;
    this._keyIdentifier = keyIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_PrivateRSA o = (KeyMaterial_PrivateRSA)other;
    return true && java.util.Objects.equals(this._name, o._name) && this._encrypt == o._encrypt && this._decrypt == o._decrypt && java.util.Objects.equals(this._algorithm, o._algorithm) && java.util.Objects.equals(this._bits, o._bits) && java.util.Objects.equals(this._encoding, o._encoding) && java.util.Objects.equals(this._material, o._material) && java.util.Objects.equals(this._keyIdentifier, o._keyIdentifier);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._encrypt);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._decrypt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._bits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encoding);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._material);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyIdentifier);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.PrivateRSA");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(this._encrypt);
    s.append(", ");
    s.append(this._decrypt);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._bits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encoding));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._material));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyIdentifier));
    s.append(")");
    return s.toString();
  }
}
