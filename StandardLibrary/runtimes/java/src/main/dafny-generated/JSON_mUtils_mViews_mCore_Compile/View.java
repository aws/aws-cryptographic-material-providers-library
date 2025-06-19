// Class View
// Dafny class View compiled into Java
package JSON_mUtils_mViews_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class View {
  public View() {
  }
  public static View__ Witness = View__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0);
  public static View__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<View__> _TYPE = dafny.TypeDescriptor.<View__>referenceWithInitializer(View__.class, () -> View.defaultValue());
  public static dafny.TypeDescriptor<View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
