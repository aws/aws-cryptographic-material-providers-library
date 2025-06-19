// Class jopen
// Dafny class jopen compiled into Java
package JSON_mZeroCopy_mDeserializer_mObjects_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class jopen {
  public jopen() {
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Witness = JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(JSON_mZeroCopy_mDeserializer_mObjectParams_Compile.__default.OPEN()));
  public static JSON_mUtils_mViews_mCore_Compile.View__ defaultValue() {
    return Witness;
  }
  private static final dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _TYPE = dafny.TypeDescriptor.<JSON_mUtils_mViews_mCore_Compile.View__>referenceWithInitializer(JSON_mUtils_mViews_mCore_Compile.View__.class, () -> jopen.defaultValue());
  public static dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<JSON_mUtils_mViews_mCore_Compile.View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
