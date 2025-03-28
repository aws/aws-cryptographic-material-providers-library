// Class GenerateDataKeyResponse
// Dafny class GenerateDataKeyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _Plaintext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextForRecipient;
  public GenerateDataKeyResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    this._CiphertextBlob = CiphertextBlob;
    this._Plaintext = Plaintext;
    this._KeyId = KeyId;
    this._CiphertextForRecipient = CiphertextForRecipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyResponse o = (GenerateDataKeyResponse)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._Plaintext, o._Plaintext) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._CiphertextForRecipient, o._CiphertextForRecipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Plaintext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextForRecipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyResponse.GenerateDataKeyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Plaintext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CiphertextForRecipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyResponse> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyResponse>referenceWithInitializer(GenerateDataKeyResponse.class, () -> GenerateDataKeyResponse.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()));
  public static GenerateDataKeyResponse Default() {
    return theDefault;
  }
  public static GenerateDataKeyResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return new GenerateDataKeyResponse(CiphertextBlob, Plaintext, KeyId, CiphertextForRecipient);
  }
  public static GenerateDataKeyResponse create_GenerateDataKeyResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return create(CiphertextBlob, Plaintext, KeyId, CiphertextForRecipient);
  }
  public boolean is_GenerateDataKeyResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_Plaintext() {
    return this._Plaintext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextForRecipient() {
    return this._CiphertextForRecipient;
  }
}
