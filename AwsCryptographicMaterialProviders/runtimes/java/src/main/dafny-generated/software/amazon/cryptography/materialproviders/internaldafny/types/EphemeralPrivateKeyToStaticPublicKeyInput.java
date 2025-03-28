// Class EphemeralPrivateKeyToStaticPublicKeyInput
// Dafny class EphemeralPrivateKeyToStaticPublicKeyInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class EphemeralPrivateKeyToStaticPublicKeyInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public EphemeralPrivateKeyToStaticPublicKeyInput (dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    this._recipientPublicKey = recipientPublicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EphemeralPrivateKeyToStaticPublicKeyInput o = (EphemeralPrivateKeyToStaticPublicKeyInput)other;
    return true && java.util.Objects.equals(this._recipientPublicKey, o._recipientPublicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientPublicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput.EphemeralPrivateKeyToStaticPublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._recipientPublicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EphemeralPrivateKeyToStaticPublicKeyInput> _TYPE = dafny.TypeDescriptor.<EphemeralPrivateKeyToStaticPublicKeyInput>referenceWithInitializer(EphemeralPrivateKeyToStaticPublicKeyInput.class, () -> EphemeralPrivateKeyToStaticPublicKeyInput.Default());
  public static dafny.TypeDescriptor<EphemeralPrivateKeyToStaticPublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<EphemeralPrivateKeyToStaticPublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EphemeralPrivateKeyToStaticPublicKeyInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static EphemeralPrivateKeyToStaticPublicKeyInput Default() {
    return theDefault;
  }
  public static EphemeralPrivateKeyToStaticPublicKeyInput create(dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return new EphemeralPrivateKeyToStaticPublicKeyInput(recipientPublicKey);
  }
  public static EphemeralPrivateKeyToStaticPublicKeyInput create_EphemeralPrivateKeyToStaticPublicKeyInput(dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey) {
    return create(recipientPublicKey);
  }
  public boolean is_EphemeralPrivateKeyToStaticPublicKeyInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_recipientPublicKey() {
    return this._recipientPublicKey;
  }
}
