// Class jclose
// Dafny class jclose compiled into Java
package JSON_mZeroCopy_mDeserializer_mArrays_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jclose {
  public jclose() {
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Witness = JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(JSON_mZeroCopy_mDeserializer_mArrayParams_Compile.__default.CLOSE()));
  public static JSON_mUtils_mViews_mCore_Compile.View__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _TYPE = dafny.TypeDescriptor.<JSON_mUtils_mViews_mCore_Compile.View__>referenceWithInitializer(JSON_mUtils_mViews_mCore_Compile.View__.class, () -> jclose.defaultValue());
  public static dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
