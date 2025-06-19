// Class Writer
// Dafny class Writer compiled into Java
package JSON_mUtils_mViews_mWriters_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Writer {
  public Writer() {
  }
  public static Writer__ Witness = Writer__.create(0, Chain.create_Empty());
  public static Writer__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<Writer__> _TYPE = dafny.TypeDescriptor.<Writer__>referenceWithInitializer(Writer__.class, () -> Writer.defaultValue());
  public static dafny.TypeDescriptor<Writer__> _typeDescriptor() {
    return (dafny.TypeDescriptor<Writer__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
