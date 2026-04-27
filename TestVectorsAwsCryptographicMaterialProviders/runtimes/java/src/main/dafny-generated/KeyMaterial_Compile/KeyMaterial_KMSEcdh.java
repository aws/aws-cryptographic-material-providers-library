// Class KeyMaterial_KMSEcdh
// Dafny class KeyMaterial_KMSEcdh compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMaterial_KMSEcdh extends KeyMaterial {
  public dafny.DafnySequence<? extends Character> _name;
  public boolean _encrypt;
  public boolean _decrypt;
  public dafny.DafnySequence<? extends Character> _keyIdentifier;
  public dafny.DafnySequence<? extends Character> _algorithm;
  public dafny.DafnySequence<? extends Character> _senderMaterial;
  public dafny.DafnySequence<? extends Character> _recipientMaterial;
  public dafny.DafnySequence<? extends Character> _senderPublicKey;
  public dafny.DafnySequence<? extends Character> _recipientPublicKey;
  public KeyMaterial_KMSEcdh (dafny.DafnySequence<? extends Character> name, boolean encrypt, boolean decrypt, dafny.DafnySequence<? extends Character> keyIdentifier, dafny.DafnySequence<? extends Character> algorithm, dafny.DafnySequence<? extends Character> senderMaterial, dafny.DafnySequence<? extends Character> recipientMaterial, dafny.DafnySequence<? extends Character> senderPublicKey, dafny.DafnySequence<? extends Character> recipientPublicKey) {
    super();
    this._name = name;
    this._encrypt = encrypt;
    this._decrypt = decrypt;
    this._keyIdentifier = keyIdentifier;
    this._algorithm = algorithm;
    this._senderMaterial = senderMaterial;
    this._recipientMaterial = recipientMaterial;
    this._senderPublicKey = senderPublicKey;
    this._recipientPublicKey = recipientPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMaterial_KMSEcdh o = (KeyMaterial_KMSEcdh)other;
    return true && java.util.Objects.equals(this._name, o._name) && this._encrypt == o._encrypt && this._decrypt == o._decrypt && java.util.Objects.equals(this._keyIdentifier, o._keyIdentifier) && java.util.Objects.equals(this._algorithm, o._algorithm) && java.util.Objects.equals(this._senderMaterial, o._senderMaterial) && java.util.Objects.equals(this._recipientMaterial, o._recipientMaterial) && java.util.Objects.equals(this._senderPublicKey, o._senderPublicKey) && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._name);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._encrypt);
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._decrypt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyMaterial.KeyMaterial.KMSEcdh");
    s.append("(");
    s.append(dafny.Helpers.toString(this._name));
    s.append(", ");
    s.append(this._encrypt);
    s.append(", ");
    s.append(this._decrypt);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._senderMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._senderPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(")");
    return s.toString();
  }
}
