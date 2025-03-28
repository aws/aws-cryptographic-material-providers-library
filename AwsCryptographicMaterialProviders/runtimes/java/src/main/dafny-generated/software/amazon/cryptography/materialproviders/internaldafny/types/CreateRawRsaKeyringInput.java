// Class CreateRawRsaKeyringInput
// Dafny class CreateRawRsaKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateRawRsaKeyringInput {
  public dafny.DafnySequence<? extends Character> _keyNamespace;
  public dafny.DafnySequence<? extends Character> _keyName;
  public PaddingScheme _paddingScheme;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _publicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _privateKey;
  public CreateRawRsaKeyringInput (dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, PaddingScheme paddingScheme, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey) {
    this._keyNamespace = keyNamespace;
    this._keyName = keyName;
    this._paddingScheme = paddingScheme;
    this._publicKey = publicKey;
    this._privateKey = privateKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateRawRsaKeyringInput o = (CreateRawRsaKeyringInput)other;
    return true && java.util.Objects.equals(this._keyNamespace, o._keyNamespace) && java.util.Objects.equals(this._keyName, o._keyName) && java.util.Objects.equals(this._paddingScheme, o._paddingScheme) && java.util.Objects.equals(this._publicKey, o._publicKey) && java.util.Objects.equals(this._privateKey, o._privateKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyNamespace);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._paddingScheme);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput.CreateRawRsaKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyNamespace));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._paddingScheme));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateRawRsaKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateRawRsaKeyringInput>referenceWithInitializer(CreateRawRsaKeyringInput.class, () -> CreateRawRsaKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateRawRsaKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateRawRsaKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateRawRsaKeyringInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), PaddingScheme.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
  public static CreateRawRsaKeyringInput Default() {
    return theDefault;
  }
  public static CreateRawRsaKeyringInput create(dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, PaddingScheme paddingScheme, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey) {
    return new CreateRawRsaKeyringInput(keyNamespace, keyName, paddingScheme, publicKey, privateKey);
  }
  public static CreateRawRsaKeyringInput create_CreateRawRsaKeyringInput(dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, PaddingScheme paddingScheme, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey) {
    return create(keyNamespace, keyName, paddingScheme, publicKey, privateKey);
  }
  public boolean is_CreateRawRsaKeyringInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyNamespace() {
    return this._keyNamespace;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyName() {
    return this._keyName;
  }
  public PaddingScheme dtor_paddingScheme() {
    return this._paddingScheme;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_publicKey() {
    return this._publicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_privateKey() {
    return this._privateKey;
  }
}
