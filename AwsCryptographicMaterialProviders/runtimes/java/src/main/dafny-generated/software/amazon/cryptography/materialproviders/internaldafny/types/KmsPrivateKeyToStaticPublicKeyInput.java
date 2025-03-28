// Class KmsPrivateKeyToStaticPublicKeyInput
// Dafny class KmsPrivateKeyToStaticPublicKeyInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsPrivateKeyToStaticPublicKeyInput {
  public dafny.DafnySequence<? extends Character> _senderKmsIdentifier;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _senderPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public KmsPrivateKeyToStaticPublicKeyInput (dafny.DafnySequence<? extends Character> senderKmsIdentifier, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    this._senderKmsIdentifier = senderKmsIdentifier;
    this._senderPublicKey = senderPublicKey;
    this._recipientPublicKey = recipientPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsPrivateKeyToStaticPublicKeyInput o = (KmsPrivateKeyToStaticPublicKeyInput)other;
    return true && java.util.Objects.equals(this._senderKmsIdentifier, o._senderKmsIdentifier) && java.util.Objects.equals(this._senderPublicKey, o._senderPublicKey) && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderKmsIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._senderPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput.KmsPrivateKeyToStaticPublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._senderKmsIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._senderPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsPrivateKeyToStaticPublicKeyInput> _TYPE = dafny.TypeDescriptor.<KmsPrivateKeyToStaticPublicKeyInput>referenceWithInitializer(KmsPrivateKeyToStaticPublicKeyInput.class, () -> KmsPrivateKeyToStaticPublicKeyInput.Default());
  public static dafny.TypeDescriptor<KmsPrivateKeyToStaticPublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsPrivateKeyToStaticPublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsPrivateKeyToStaticPublicKeyInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static KmsPrivateKeyToStaticPublicKeyInput Default() {
    return theDefault;
  }
  public static KmsPrivateKeyToStaticPublicKeyInput create(dafny.DafnySequence<? extends Character> senderKmsIdentifier, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return new KmsPrivateKeyToStaticPublicKeyInput(senderKmsIdentifier, senderPublicKey, recipientPublicKey);
  }
  public static KmsPrivateKeyToStaticPublicKeyInput create_KmsPrivateKeyToStaticPublicKeyInput(dafny.DafnySequence<? extends Character> senderKmsIdentifier, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return create(senderKmsIdentifier, senderPublicKey, recipientPublicKey);
  }
  public boolean is_KmsPrivateKeyToStaticPublicKeyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_senderKmsIdentifier() {
    return this._senderKmsIdentifier;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_senderPublicKey() {
    return this._senderPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_recipientPublicKey() {
    return this._recipientPublicKey;
  }
}
