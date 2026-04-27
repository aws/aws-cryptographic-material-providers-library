// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mAPI_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Serialize(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), (JSON_mZeroCopy_mSerializer_Compile.__default.Text(js)).Bytes());
  }
  public static Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> SerializeAlloc(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js)
  {
    Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> bs = Wrappers_Compile.Result.<byte[], JSON_mErrors_Compile.SerializationError>Default(dafny.TypeDescriptor.BYTE_ARRAY, JSON_mErrors_Compile.SerializationError._typeDescriptor(), new byte[0]);
    if(true) {
      Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mSerializer_Compile.__default.Serialize(js);
      bs = _out0;
    }
    return bs;
  }
  public static Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> SerializeInto(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js, byte[] bs)
  {
    Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> len = Wrappers_Compile.Result.<java.lang.Integer, JSON_mErrors_Compile.SerializationError>Default(BoundedInts_Compile.uint32._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), 0);
    if(true) {
      Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mSerializer_Compile.__default.SerializeTo(js, bs);
      len = _out0;
    }
    return len;
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError> Deserialize(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    return JSON_mZeroCopy_mDeserializer_mAPI_Compile.__default.OfBytes(bs);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.API._default";
  }
}
