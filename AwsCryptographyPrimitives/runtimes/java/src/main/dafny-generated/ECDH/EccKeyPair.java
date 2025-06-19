// Class EccKeyPair
// Dafny class EccKeyPair compiled into Java
package ECDH;

@SuppressWarnings({"unchecked", "deprecation"})
public class EccKeyPair {
  public dafny.DafnySequence<? extends java.lang.Byte> _privateKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public EccKeyPair (dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    this._privateKey = privateKey;
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EccKeyPair o = (EccKeyPair)other;
    return true && java.util.Objects.equals(this._privateKey, o._privateKey) && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ECDH.EccKeyPair.EccKeyPair");
    s.append("(");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EccKeyPair> _TYPE = dafny.TypeDescriptor.<EccKeyPair>referenceWithInitializer(EccKeyPair.class, () -> EccKeyPair.Default());
  public static dafny.TypeDescriptor<EccKeyPair> _typeDescriptor() {
    return (dafny.TypeDescriptor<EccKeyPair>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EccKeyPair theDefault = EccKeyPair.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static EccKeyPair Default() {
    return theDefault;
  }
  public static EccKeyPair create(dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new EccKeyPair(privateKey, publicKey);
  }
  public static EccKeyPair create_EccKeyPair(dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return create(privateKey, publicKey);
  }
  public boolean is_EccKeyPair() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_privateKey() {
    return this._privateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
}
