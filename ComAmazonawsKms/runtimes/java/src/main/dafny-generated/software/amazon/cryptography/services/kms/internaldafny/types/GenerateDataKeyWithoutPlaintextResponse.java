// Class GenerateDataKeyWithoutPlaintextResponse
// Dafny class GenerateDataKeyWithoutPlaintextResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyWithoutPlaintextResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public GenerateDataKeyWithoutPlaintextResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    this._CiphertextBlob = CiphertextBlob;
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyWithoutPlaintextResponse o = (GenerateDataKeyWithoutPlaintextResponse)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._KeyId, o._KeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.GenerateDataKeyWithoutPlaintextResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextResponse> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyWithoutPlaintextResponse>referenceWithInitializer(GenerateDataKeyWithoutPlaintextResponse.class, () -> GenerateDataKeyWithoutPlaintextResponse.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyWithoutPlaintextResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyWithoutPlaintextResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyWithoutPlaintextResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()));
  public static GenerateDataKeyWithoutPlaintextResponse Default() {
    return theDefault;
  }
  public static GenerateDataKeyWithoutPlaintextResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return new GenerateDataKeyWithoutPlaintextResponse(CiphertextBlob, KeyId);
  }
  public static GenerateDataKeyWithoutPlaintextResponse create_GenerateDataKeyWithoutPlaintextResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return create(CiphertextBlob, KeyId);
  }
  public boolean is_GenerateDataKeyWithoutPlaintextResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
}
