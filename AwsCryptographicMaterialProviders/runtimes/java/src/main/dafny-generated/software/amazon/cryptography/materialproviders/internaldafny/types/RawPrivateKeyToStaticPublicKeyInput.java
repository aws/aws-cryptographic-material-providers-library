// Class RawPrivateKeyToStaticPublicKeyInput
// Dafny class RawPrivateKeyToStaticPublicKeyInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawPrivateKeyToStaticPublicKeyInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _senderStaticPrivateKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public RawPrivateKeyToStaticPublicKeyInput (dafny.DafnySequence<? extends java.lang.Byte> senderStaticPrivateKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    this._senderStaticPrivateKey = senderStaticPrivateKey;
    this._recipientPublicKey = recipientPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RawPrivateKeyToStaticPublicKeyInput o = (RawPrivateKeyToStaticPublicKeyInput)other;
    return true && java.util.Objects.equals(this._senderStaticPrivateKey, o._senderStaticPrivateKey) && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderStaticPrivateKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput.RawPrivateKeyToStaticPublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._senderStaticPrivateKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RawPrivateKeyToStaticPublicKeyInput> _TYPE = dafny.TypeDescriptor.<RawPrivateKeyToStaticPublicKeyInput>referenceWithInitializer(RawPrivateKeyToStaticPublicKeyInput.class, () -> RawPrivateKeyToStaticPublicKeyInput.Default());
  public static dafny.TypeDescriptor<RawPrivateKeyToStaticPublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawPrivateKeyToStaticPublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RawPrivateKeyToStaticPublicKeyInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static RawPrivateKeyToStaticPublicKeyInput Default() {
    return theDefault;
  }
  public static RawPrivateKeyToStaticPublicKeyInput create(dafny.DafnySequence<? extends java.lang.Byte> senderStaticPrivateKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return new RawPrivateKeyToStaticPublicKeyInput(senderStaticPrivateKey, recipientPublicKey);
  }
  public static RawPrivateKeyToStaticPublicKeyInput create_RawPrivateKeyToStaticPublicKeyInput(dafny.DafnySequence<? extends java.lang.Byte> senderStaticPrivateKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return create(senderStaticPrivateKey, recipientPublicKey);
  }
  public boolean is_RawPrivateKeyToStaticPublicKeyInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_senderStaticPrivateKey() {
    return this._senderStaticPrivateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_recipientPublicKey() {
    return this._recipientPublicKey;
  }
}
