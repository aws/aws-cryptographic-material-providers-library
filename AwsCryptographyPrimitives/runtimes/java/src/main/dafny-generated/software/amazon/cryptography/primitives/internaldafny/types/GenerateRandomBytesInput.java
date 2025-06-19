// Class GenerateRandomBytesInput
// Dafny class GenerateRandomBytesInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateRandomBytesInput {
  public int _length;
  public GenerateRandomBytesInput (int length) {
    this._length = length;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateRandomBytesInput o = (GenerateRandomBytesInput)other;
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
    s.append("AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput.GenerateRandomBytesInput");
    s.append("(");
    s.append(this._length);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateRandomBytesInput> _TYPE = dafny.TypeDescriptor.<GenerateRandomBytesInput>referenceWithInitializer(GenerateRandomBytesInput.class, () -> GenerateRandomBytesInput.Default());
  public static dafny.TypeDescriptor<GenerateRandomBytesInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateRandomBytesInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateRandomBytesInput theDefault = GenerateRandomBytesInput.create(0);
  public static GenerateRandomBytesInput Default() {
    return theDefault;
  }
  public static GenerateRandomBytesInput create(int length) {
    return new GenerateRandomBytesInput(length);
  }
  public static GenerateRandomBytesInput create_GenerateRandomBytesInput(int length) {
    return create(length);
  }
  public boolean is_GenerateRandomBytesInput() { return true; }
  public int dtor_length() {
    return this._length;
  }
}
