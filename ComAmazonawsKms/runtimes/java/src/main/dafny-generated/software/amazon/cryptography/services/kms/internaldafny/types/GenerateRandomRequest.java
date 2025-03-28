// Class GenerateRandomRequest
// Dafny class GenerateRandomRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateRandomRequest {
  public Wrappers_Compile.Option<java.lang.Integer> _NumberOfBytes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public Wrappers_Compile.Option<RecipientInfo> _Recipient;
  public GenerateRandomRequest (Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    this._NumberOfBytes = NumberOfBytes;
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._Recipient = Recipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateRandomRequest o = (GenerateRandomRequest)other;
    return true && java.util.Objects.equals(this._NumberOfBytes, o._NumberOfBytes) && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._Recipient, o._Recipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NumberOfBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Recipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateRandomRequest.GenerateRandomRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._NumberOfBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Recipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateRandomRequest> _TYPE = dafny.TypeDescriptor.<GenerateRandomRequest>referenceWithInitializer(GenerateRandomRequest.class, () -> GenerateRandomRequest.Default());
  public static dafny.TypeDescriptor<GenerateRandomRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateRandomRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateRandomRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateRandomRequest.create(Wrappers_Compile.Option.<java.lang.Integer>Default(NumberOfBytesType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()), Wrappers_Compile.Option.<RecipientInfo>Default(RecipientInfo._typeDescriptor()));
  public static GenerateRandomRequest Default() {
    return theDefault;
  }
  public static GenerateRandomRequest create(Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    return new GenerateRandomRequest(NumberOfBytes, CustomKeyStoreId, Recipient);
  }
  public static GenerateRandomRequest create_GenerateRandomRequest(Wrappers_Compile.Option<java.lang.Integer> NumberOfBytes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<RecipientInfo> Recipient) {
    return create(NumberOfBytes, CustomKeyStoreId, Recipient);
  }
  public boolean is_GenerateRandomRequest() { return true; }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_NumberOfBytes() {
    return this._NumberOfBytes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<RecipientInfo> dtor_Recipient() {
    return this._Recipient;
  }
}
