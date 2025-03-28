// Class GenerateRandomResponse
// Dafny class GenerateRandomResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateRandomResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _Plaintext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextForRecipient;
  public GenerateRandomResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    this._Plaintext = Plaintext;
    this._CiphertextForRecipient = CiphertextForRecipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateRandomResponse o = (GenerateRandomResponse)other;
    return true && java.util.Objects.equals(this._Plaintext, o._Plaintext) && java.util.Objects.equals(this._CiphertextForRecipient, o._CiphertextForRecipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Plaintext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextForRecipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateRandomResponse.GenerateRandomResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Plaintext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CiphertextForRecipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateRandomResponse> _TYPE = dafny.TypeDescriptor.<GenerateRandomResponse>referenceWithInitializer(GenerateRandomResponse.class, () -> GenerateRandomResponse.Default());
  public static dafny.TypeDescriptor<GenerateRandomResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateRandomResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateRandomResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateRandomResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()));
  public static GenerateRandomResponse Default() {
    return theDefault;
  }
  public static GenerateRandomResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return new GenerateRandomResponse(Plaintext, CiphertextForRecipient);
  }
  public static GenerateRandomResponse create_GenerateRandomResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return create(Plaintext, CiphertextForRecipient);
  }
  public boolean is_GenerateRandomResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_Plaintext() {
    return this._Plaintext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextForRecipient() {
    return this._CiphertextForRecipient;
  }
}
