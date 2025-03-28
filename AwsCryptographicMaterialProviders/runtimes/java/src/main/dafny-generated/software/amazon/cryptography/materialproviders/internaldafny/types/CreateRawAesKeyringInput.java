// Class CreateRawAesKeyringInput
// Dafny class CreateRawAesKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateRawAesKeyringInput {
  public dafny.DafnySequence<? extends Character> _keyNamespace;
  public dafny.DafnySequence<? extends Character> _keyName;
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappingKey;
  public AesWrappingAlg _wrappingAlg;
  public CreateRawAesKeyringInput (dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, dafny.DafnySequence<? extends java.lang.Byte> wrappingKey, AesWrappingAlg wrappingAlg) {
    this._keyNamespace = keyNamespace;
    this._keyName = keyName;
    this._wrappingKey = wrappingKey;
    this._wrappingAlg = wrappingAlg;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateRawAesKeyringInput o = (CreateRawAesKeyringInput)other;
    return true && java.util.Objects.equals(this._keyNamespace, o._keyNamespace) && java.util.Objects.equals(this._keyName, o._keyName) && java.util.Objects.equals(this._wrappingKey, o._wrappingKey) && java.util.Objects.equals(this._wrappingAlg, o._wrappingAlg);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyNamespace);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappingKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappingAlg);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput.CreateRawAesKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyNamespace));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrappingKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrappingAlg));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateRawAesKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateRawAesKeyringInput>referenceWithInitializer(CreateRawAesKeyringInput.class, () -> CreateRawAesKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateRawAesKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateRawAesKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateRawAesKeyringInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), AesWrappingAlg.Default());
  public static CreateRawAesKeyringInput Default() {
    return theDefault;
  }
  public static CreateRawAesKeyringInput create(dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, dafny.DafnySequence<? extends java.lang.Byte> wrappingKey, AesWrappingAlg wrappingAlg) {
    return new CreateRawAesKeyringInput(keyNamespace, keyName, wrappingKey, wrappingAlg);
  }
  public static CreateRawAesKeyringInput create_CreateRawAesKeyringInput(dafny.DafnySequence<? extends Character> keyNamespace, dafny.DafnySequence<? extends Character> keyName, dafny.DafnySequence<? extends java.lang.Byte> wrappingKey, AesWrappingAlg wrappingAlg) {
    return create(keyNamespace, keyName, wrappingKey, wrappingAlg);
  }
  public boolean is_CreateRawAesKeyringInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyNamespace() {
    return this._keyNamespace;
  }
  public dafny.DafnySequence<? extends Character> dtor_keyName() {
    return this._keyName;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_wrappingKey() {
    return this._wrappingKey;
  }
  public AesWrappingAlg dtor_wrappingAlg() {
    return this._wrappingAlg;
  }
}
