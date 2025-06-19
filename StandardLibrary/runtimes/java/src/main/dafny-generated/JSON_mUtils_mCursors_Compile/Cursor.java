// Class Cursor
// Dafny class Cursor compiled into Java
package JSON_mUtils_mCursors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Cursor {
  public Cursor() {
  }
  public static Cursor__ Witness = Cursor__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0, 0);
  public static Cursor__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<Cursor__> _TYPE = dafny.TypeDescriptor.<Cursor__>referenceWithInitializer(Cursor__.class, () -> Cursor.defaultValue());
  public static dafny.TypeDescriptor<Cursor__> _typeDescriptor() {
    return (dafny.TypeDescriptor<Cursor__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
