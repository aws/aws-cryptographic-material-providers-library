// Class __default
// Dafny class __default compiled into Java
package FileIO_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> ReadBytesFromFile(dafny.DafnySequence<? extends Character> path)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    boolean _0_isError;
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytesRead;
    dafny.DafnySequence<? extends Character> _2_errorMsg;
    boolean _out0;
    dafny.DafnySequence<? extends java.lang.Byte> _out1;
    dafny.DafnySequence<? extends Character> _out2;
    dafny.Tuple3<Boolean, dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _outcollector0 = DafnyLibraries.FileIO.INTERNAL_ReadBytesFromFile(path);
    _out0 = (boolean) (Object) _outcollector0.dtor__0();
    _out1 = (dafny.DafnySequence<? extends java.lang.Byte>) (Object) _outcollector0.dtor__1();
    _out2 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__2();
    _0_isError = _out0;
    _1_bytesRead = _out1;
    _2_errorMsg = _out2;
    if (_0_isError) {
      res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_errorMsg);
    } else {
      res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_bytesRead);
    }
    return res;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> WriteBytesToFile(dafny.DafnySequence<? extends Character> path, dafny.DafnySequence<? extends java.lang.Byte> bytes)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    boolean _0_isError;
    dafny.DafnySequence<? extends Character> _1_errorMsg;
    boolean _out0;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.Tuple2<Boolean, dafny.DafnySequence<? extends Character>> _outcollector0 = DafnyLibraries.FileIO.INTERNAL_WriteBytesToFile(path, bytes);
    _out0 = (boolean) (Object) _outcollector0.dtor__0();
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _0_isError = _out0;
    _1_errorMsg = _out1;
    if (_0_isError) {
      res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_errorMsg);
    } else {
      res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return res;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> AppendBytesToFile(dafny.DafnySequence<? extends Character> path, dafny.DafnySequence<? extends java.lang.Byte> bytes)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    boolean _0_isError;
    dafny.DafnySequence<? extends Character> _1_errorMsg;
    boolean _out0;
    dafny.DafnySequence<? extends Character> _out1;
    dafny.Tuple2<Boolean, dafny.DafnySequence<? extends Character>> _outcollector0 = DafnyLibraries.FileIO.INTERNAL_AppendBytesToFile(path, bytes);
    _out0 = (boolean) (Object) _outcollector0.dtor__0();
    _out1 = (dafny.DafnySequence<? extends Character>) (Object) _outcollector0.dtor__1();
    _0_isError = _out0;
    _1_errorMsg = _out1;
    if (_0_isError) {
      res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Failure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_errorMsg);
    } else {
      res = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return res;
  }
  @Override
  public java.lang.String toString() {
    return "FileIO._default";
  }
}
