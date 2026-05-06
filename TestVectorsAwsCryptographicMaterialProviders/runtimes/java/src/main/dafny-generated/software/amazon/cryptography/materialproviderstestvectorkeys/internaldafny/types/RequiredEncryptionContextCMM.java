// Class RequiredEncryptionContextCMM
// Dafny class RequiredEncryptionContextCMM compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RequiredEncryptionContextCMM {
  public KeyDescription _underlying;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public RequiredEncryptionContextCMM (KeyDescription underlying, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    this._underlying = underlying;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RequiredEncryptionContextCMM o = (RequiredEncryptionContextCMM)other;
    return true && java.util.Objects.equals(this._underlying, o._underlying) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._underlying);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM.RequiredEncryptionContextCMM");
    s.append("(");
    s.append(dafny.Helpers.toString(this._underlying));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RequiredEncryptionContextCMM> _TYPE = dafny.TypeDescriptor.<RequiredEncryptionContextCMM>referenceWithInitializer(RequiredEncryptionContextCMM.class, () -> RequiredEncryptionContextCMM.Default());
  public static dafny.TypeDescriptor<RequiredEncryptionContextCMM> _typeDescriptor() {
    return (dafny.TypeDescriptor<RequiredEncryptionContextCMM>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RequiredEncryptionContextCMM theDefault = RequiredEncryptionContextCMM.create(KeyDescription.Default(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()));
  public static RequiredEncryptionContextCMM Default() {
    return theDefault;
  }
  public static RequiredEncryptionContextCMM create(KeyDescription underlying, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return new RequiredEncryptionContextCMM(underlying, requiredEncryptionContextKeys);
  }
  public static RequiredEncryptionContextCMM create_RequiredEncryptionContextCMM(KeyDescription underlying, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return create(underlying, requiredEncryptionContextKeys);
  }
  public boolean is_RequiredEncryptionContextCMM() { return true; }
  public KeyDescription dtor_underlying() {
    return this._underlying;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
}
