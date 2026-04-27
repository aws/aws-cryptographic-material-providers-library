// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__R> JSON_mUtils_mLexers_mCore_Compile.LexerResult<Boolean, __R> StringBody(dafny.TypeDescriptor<__R> _td___R, boolean escaped, short byte_)
  {
    if ((byte_) == (((short) ('\\')))) {
      return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<Boolean, __R>create_Partial(dafny.TypeDescriptor.BOOLEAN, _td___R, !(escaped));
    } else if (((byte_) == (((short) ('\"')))) && (!(escaped))) {
      return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<Boolean, __R>create_Accept(dafny.TypeDescriptor.BOOLEAN, _td___R);
    } else {
      return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<Boolean, __R>create_Partial(dafny.TypeDescriptor.BOOLEAN, _td___R, false);
    }
  }
  public static JSON_mUtils_mLexers_mCore_Compile.LexerResult<StringLexerState, dafny.DafnySequence<? extends Character>> String(StringLexerState st, short byte_)
  {
    StringLexerState _source0 = st;
    if (_source0.is_Start()) {
      if ((byte_) == (((short) ('\"')))) {
        return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Partial(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), StringLexerState.create_Body(false));
      } else {
        return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Reject(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("String must start with double quote"));
      }
    } else if (_source0.is_Body()) {
      boolean _0___mcc_h0 = ((JSON_mUtils_mLexers_mStrings_Compile.StringLexerState_Body)_source0)._escaped;
      boolean _1_escaped = _0___mcc_h0;
      if ((byte_) == (((short) ('\\')))) {
        return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Partial(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), StringLexerState.create_Body(!(_1_escaped)));
      } else if (((byte_) == (((short) ('\"')))) && (!(_1_escaped))) {
        return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Partial(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), StringLexerState.create_End());
      } else {
        return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Partial(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), StringLexerState.create_Body(false));
      }
    } else {
      return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<StringLexerState, dafny.DafnySequence<? extends Character>>create_Accept(StringLexerState._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    }
  }
  public static boolean StringBodyLexerStart()
  {
    return false;
  }
  public static StringLexerState StringLexerStart()
  {
    return StringLexerState.create_Start();
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Lexers.Strings._default";
  }
}
