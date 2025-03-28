// Class CreateRequiredEncryptionContextCMMInput
// Dafny class CreateRequiredEncryptionContextCMMInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateRequiredEncryptionContextCMMInput {
  public Wrappers_Compile.Option<ICryptographicMaterialsManager> _underlyingCMM;
  public Wrappers_Compile.Option<IKeyring> _keyring;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public CreateRequiredEncryptionContextCMMInput (Wrappers_Compile.Option<ICryptographicMaterialsManager> underlyingCMM, Wrappers_Compile.Option<IKeyring> keyring, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    this._underlyingCMM = underlyingCMM;
    this._keyring = keyring;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateRequiredEncryptionContextCMMInput o = (CreateRequiredEncryptionContextCMMInput)other;
    return true && java.util.Objects.equals(this._underlyingCMM, o._underlyingCMM) && java.util.Objects.equals(this._keyring, o._keyring) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._underlyingCMM);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyring);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput.CreateRequiredEncryptionContextCMMInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._underlyingCMM));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyring));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateRequiredEncryptionContextCMMInput> _TYPE = dafny.TypeDescriptor.<CreateRequiredEncryptionContextCMMInput>referenceWithInitializer(CreateRequiredEncryptionContextCMMInput.class, () -> CreateRequiredEncryptionContextCMMInput.Default());
  public static dafny.TypeDescriptor<CreateRequiredEncryptionContextCMMInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateRequiredEncryptionContextCMMInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateRequiredEncryptionContextCMMInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput.create(Wrappers_Compile.Option.<ICryptographicMaterialsManager>Default(((dafny.TypeDescriptor<ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(ICryptographicMaterialsManager.class))), Wrappers_Compile.Option.<IKeyring>Default(((dafny.TypeDescriptor<IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(IKeyring.class))), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()));
  public static CreateRequiredEncryptionContextCMMInput Default() {
    return theDefault;
  }
  public static CreateRequiredEncryptionContextCMMInput create(Wrappers_Compile.Option<ICryptographicMaterialsManager> underlyingCMM, Wrappers_Compile.Option<IKeyring> keyring, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return new CreateRequiredEncryptionContextCMMInput(underlyingCMM, keyring, requiredEncryptionContextKeys);
  }
  public static CreateRequiredEncryptionContextCMMInput create_CreateRequiredEncryptionContextCMMInput(Wrappers_Compile.Option<ICryptographicMaterialsManager> underlyingCMM, Wrappers_Compile.Option<IKeyring> keyring, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return create(underlyingCMM, keyring, requiredEncryptionContextKeys);
  }
  public boolean is_CreateRequiredEncryptionContextCMMInput() { return true; }
  public Wrappers_Compile.Option<ICryptographicMaterialsManager> dtor_underlyingCMM() {
    return this._underlyingCMM;
  }
  public Wrappers_Compile.Option<IKeyring> dtor_keyring() {
    return this._keyring;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
}
