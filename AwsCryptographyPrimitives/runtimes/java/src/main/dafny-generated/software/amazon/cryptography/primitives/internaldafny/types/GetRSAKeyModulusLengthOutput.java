// Class GetRSAKeyModulusLengthOutput
// Dafny class GetRSAKeyModulusLengthOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetRSAKeyModulusLengthOutput {
  public int _length;
  public GetRSAKeyModulusLengthOutput (int length) {
    this._length = length;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetRSAKeyModulusLengthOutput o = (GetRSAKeyModulusLengthOutput)other;
    return true && this._length == o._length;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._length);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput.GetRSAKeyModulusLengthOutput");
    s.append("(");
    s.append(this._length);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetRSAKeyModulusLengthOutput> _TYPE = dafny.TypeDescriptor.<GetRSAKeyModulusLengthOutput>referenceWithInitializer(GetRSAKeyModulusLengthOutput.class, () -> GetRSAKeyModulusLengthOutput.Default());
  public static dafny.TypeDescriptor<GetRSAKeyModulusLengthOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetRSAKeyModulusLengthOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetRSAKeyModulusLengthOutput theDefault = software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput.create(0);
  public static GetRSAKeyModulusLengthOutput Default() {
    return theDefault;
  }
  public static GetRSAKeyModulusLengthOutput create(int length) {
    return new GetRSAKeyModulusLengthOutput(length);
  }
  public static GetRSAKeyModulusLengthOutput create_GetRSAKeyModulusLengthOutput(int length) {
    return create(length);
  }
  public boolean is_GetRSAKeyModulusLengthOutput() { return true; }
  public int dtor_length() {
    return this._length;
  }
}
