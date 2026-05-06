// Class KeyMaterial_KMSAsymetric
// Dafny class KeyMaterial_KMSAsymetric compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_KMSAsymetric extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _name;
  public boolean _encrypt;
  public boolean _decrypt;
  public dafny.DafnySequence<? extends Character> _keyIdentifier;
  public java.math.BigInteger _bits;
  public dafny.DafnySequence<? extends Character> _algorithm;
  public dafny.DafnySequence<? extends Character> _encoding;
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public KeyMaterial_KMSAsymetric (dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier, java.math.BigInteger bits, dafny.DafnySequence<? extends Character> algorithm, dafny.DafnySequence<? extends Character> encoding, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    super();
    this._name = name;
    this._encrypt = encrypt;
    this._decrypt = decrypt;
    this._keyIdentifier = keyIdentifier;
    this._bits = bits;
    this._algorithm = algorithm;
    this._encoding = encoding;
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_KMSAsymetric o = (KeyMaterial_KMSAsymetric)other;
    return true && java.util.Objects.equals(this._name, o._name) && this._encrypt == o._encrypt && this._decrypt == o._decrypt && java.util.Objects.equals(this._keyIdentifier, o._keyIdentifier) && java.util.Objects.equals(this._bits, o._bits) && java.util.Objects.equals(this._algorithm, o._algorithm) && java.util.Objects.equals(this._encoding, o._encoding) && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._encrypt);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._decrypt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._bits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encoding);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.KMSAsymetric");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(this._encrypt);
    s.append(", ");
    s.append(this._decrypt);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._bits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encoding));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
}
