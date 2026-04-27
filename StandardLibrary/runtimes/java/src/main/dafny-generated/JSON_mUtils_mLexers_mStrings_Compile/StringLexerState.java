// Class StringLexerState
// Dafny class StringLexerState compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class StringLexerState {
  public StringLexerState() {
  }
  private static final dafny.TypeDescriptor<StringLexerState> _TYPE = dafny.TypeDescriptor.<StringLexerState>referenceWithInitializer(StringLexerState.class, () -> StringLexerState.Default());
  public static dafny.TypeDescriptor<StringLexerState> _typeDescriptor() {
    return (dafny.TypeDescriptor<StringLexerState>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StringLexerState theDefault = StringLexerState.create_Start();
  public static StringLexerState Default() {
    return theDefault;
  }
  public static StringLexerState create_Start() {
    return new StringLexerState_Start();
  }
  public static StringLexerState create_Body(boolean escaped) {
    return new StringLexerState_Body(escaped);
  }
  public static StringLexerState create_End() {
    return new StringLexerState_End();
  }
  public boolean is_Start() { return this instanceof StringLexerState_Start; }
  public boolean is_Body() { return this instanceof StringLexerState_Body; }
  public boolean is_End() { return this instanceof StringLexerState_End; }
  public boolean dtor_escaped() {
    StringLexerState d = this;
    return ((StringLexerState_Body)d)._escaped;
  }
}
