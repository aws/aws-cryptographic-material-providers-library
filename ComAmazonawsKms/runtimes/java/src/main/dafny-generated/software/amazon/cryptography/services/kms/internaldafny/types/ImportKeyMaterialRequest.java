// Class ImportKeyMaterialRequest
// Dafny class ImportKeyMaterialRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportKeyMaterialRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends java.lang.Byte> _ImportToken;
  public dafny.DafnySequence<? extends java.lang.Byte> _EncryptedKeyMaterial;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ValidTo;
  public Wrappers_Compile.Option<ExpirationModelType> _ExpirationModel;
  public ImportKeyMaterialRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> ImportToken, dafny.DafnySequence<? extends java.lang.Byte> EncryptedKeyMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel) {
    this._KeyId = KeyId;
    this._ImportToken = ImportToken;
    this._EncryptedKeyMaterial = EncryptedKeyMaterial;
    this._ValidTo = ValidTo;
    this._ExpirationModel = ExpirationModel;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportKeyMaterialRequest o = (ImportKeyMaterialRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._ImportToken, o._ImportToken) && java.util.Objects.equals(this._EncryptedKeyMaterial, o._EncryptedKeyMaterial) && java.util.Objects.equals(this._ValidTo, o._ValidTo) && java.util.Objects.equals(this._ExpirationModel, o._ExpirationModel);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptedKeyMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ValidTo);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpirationModel);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ImportKeyMaterialRequest.ImportKeyMaterialRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ImportToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptedKeyMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ValidTo));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpirationModel));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportKeyMaterialRequest> _TYPE = dafny.TypeDescriptor.<ImportKeyMaterialRequest>referenceWithInitializer(ImportKeyMaterialRequest.class, () -> ImportKeyMaterialRequest.Default());
  public static dafny.TypeDescriptor<ImportKeyMaterialRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportKeyMaterialRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportKeyMaterialRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ImportKeyMaterialRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ExpirationModelType>Default(ExpirationModelType._typeDescriptor()));
  public static ImportKeyMaterialRequest Default() {
    return theDefault;
  }
  public static ImportKeyMaterialRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> ImportToken, dafny.DafnySequence<? extends java.lang.Byte> EncryptedKeyMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel) {
    return new ImportKeyMaterialRequest(KeyId, ImportToken, EncryptedKeyMaterial, ValidTo, ExpirationModel);
  }
  public static ImportKeyMaterialRequest create_ImportKeyMaterialRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> ImportToken, dafny.DafnySequence<? extends java.lang.Byte> EncryptedKeyMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel) {
    return create(KeyId, ImportToken, EncryptedKeyMaterial, ValidTo, ExpirationModel);
  }
  public boolean is_ImportKeyMaterialRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ImportToken() {
    return this._ImportToken;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_EncryptedKeyMaterial() {
    return this._EncryptedKeyMaterial;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ValidTo() {
    return this._ValidTo;
  }
  public Wrappers_Compile.Option<ExpirationModelType> dtor_ExpirationModel() {
    return this._ExpirationModel;
  }
}
