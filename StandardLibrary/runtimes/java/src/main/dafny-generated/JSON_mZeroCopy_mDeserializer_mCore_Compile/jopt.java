// Class jopt
// Dafny class jopt compiled into Java
package JSON_mZeroCopy_mDeserializer_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jopt {
  public jopt() {
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Witness = JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static JSON_mUtils_mViews_mCore_Compile.View__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _TYPE = dafny.TypeDescriptor.<JSON_mUtils_mViews_mCore_Compile.View__>referenceWithInitializer(JSON_mUtils_mViews_mCore_Compile.View__.class, () -> jopt.defaultValue());
  public static dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
