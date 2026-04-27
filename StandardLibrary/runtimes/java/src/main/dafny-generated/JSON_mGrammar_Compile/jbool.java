// Class jbool
// Dafny class jbool compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jbool {
  public jbool() {
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Witness = JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(__default.TRUE());
  public static JSON_mUtils_mViews_mCore_Compile.View__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _TYPE = dafny.TypeDescriptor.<JSON_mUtils_mViews_mCore_Compile.View__>referenceWithInitializer(JSON_mUtils_mViews_mCore_Compile.View__.class, () -> jbool.defaultValue());
  public static dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
