// Class SerializeKeyDescriptionOutput
// Dafny class SerializeKeyDescriptionOutput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializeKeyDescriptionOutput {
  public dafny.DafnySequence<? extends java.lang.Byte> _json;
  public SerializeKeyDescriptionOutput (dafny.DafnySequence<? extends java.lang.Byte> json) {
    this._json = json;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializeKeyDescriptionOutput o = (SerializeKeyDescriptionOutput)other;
    return true && java.util.Objects.equals(this._json, o._json);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._json);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput.SerializeKeyDescriptionOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._json));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SerializeKeyDescriptionOutput> _TYPE = dafny.TypeDescriptor.<SerializeKeyDescriptionOutput>referenceWithInitializer(SerializeKeyDescriptionOutput.class, () -> SerializeKeyDescriptionOutput.Default());
  public static dafny.TypeDescriptor<SerializeKeyDescriptionOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<SerializeKeyDescriptionOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SerializeKeyDescriptionOutput theDefault = SerializeKeyDescriptionOutput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static SerializeKeyDescriptionOutput Default() {
    return theDefault;
  }
  public static SerializeKeyDescriptionOutput create(dafny.DafnySequence<? extends java.lang.Byte> json) {
    return new SerializeKeyDescriptionOutput(json);
  }
  public static SerializeKeyDescriptionOutput create_SerializeKeyDescriptionOutput(dafny.DafnySequence<? extends java.lang.Byte> json) {
    return create(json);
  }
  public boolean is_SerializeKeyDescriptionOutput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_json() {
    return this._json;
  }
}
