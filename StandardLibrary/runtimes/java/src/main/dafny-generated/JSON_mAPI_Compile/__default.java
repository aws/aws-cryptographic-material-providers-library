// Class __default
// Dafny class __default compiled into Java
package JSON_mAPI_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> Serialize(JSON_mValues_Compile.JSON js) {
    Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = JSON_mSerializer_Compile.__default.JSON(js);
    if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> _1_js = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return JSON_mZeroCopy_mAPI_Compile.__default.Serialize(_1_js);
    }
  }
  public static Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> SerializeAlloc(JSON_mValues_Compile.JSON js)
  {
    Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> bs = Wrappers_Compile.Result.<byte[], JSON_mErrors_Compile.SerializationError>Default(dafny.TypeDescriptor.BYTE_ARRAY, JSON_mErrors_Compile.SerializationError._typeDescriptor(), new byte[0]);
    if(true) {
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = Wrappers_Compile.Result.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError>Default(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>Default(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.Value.Default()));
      _0_valueOrError0 = JSON_mSerializer_Compile.__default.JSON(js);
      if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        bs = (_0_valueOrError0).<byte[]>PropagateFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.TypeDescriptor.BYTE_ARRAY);
        return bs;
      }
      JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> _1_js;
      _1_js = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mAPI_Compile.__default.SerializeAlloc(_1_js);
      bs = _out0;
    }
    return bs;
  }
  public static Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> SerializeInto(JSON_mValues_Compile.JSON js, byte[] bs)
  {
    Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> len = Wrappers_Compile.Result.<java.lang.Integer, JSON_mErrors_Compile.SerializationError>Default(BoundedInts_Compile.uint32._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), 0);
    if(true) {
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = Wrappers_Compile.Result.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError>Default(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>Default(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.Value.Default()));
      _0_valueOrError0 = JSON_mSerializer_Compile.__default.JSON(js);
      if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        len = (_0_valueOrError0).<java.lang.Integer>PropagateFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), BoundedInts_Compile.uint32._typeDescriptor());
        return len;
      }
      JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> _1_js;
      _1_js = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> _out0;
      _out0 = JSON_mZeroCopy_mAPI_Compile.__default.SerializeInto(_1_js, bs);
      len = _out0;
    }
    return len;
  }
  public static Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError> Deserialize(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.DeserializationError> _0_valueOrError0 = JSON_mZeroCopy_mAPI_Compile.__default.Deserialize(bs);
    if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mValues_Compile.JSON>PropagateFailure(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON._typeDescriptor());
    } else {
      JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> _1_js = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
      return JSON_mDeserializer_Compile.__default.JSON(_1_js);
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.API._default";
  }
}
