// Class Parser
// Dafny class Parser compiled into Java
package JSON_mUtils_mParsers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Parser<T, R> {
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public Parser(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    this._td_T = _td_T;
    this._td_R = _td_R;
  }
  public static <T, R> Parser__<T, R> defaultValue(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return __default.<T, R>ParserWitness(_td_T, _td_R);
  }
  public static <T, R> dafny.TypeDescriptor<Parser__<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<Parser__<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Parser__<T, R>>referenceWithInitializer(Parser__.class, () -> Parser.defaultValue(_td_T, _td_R));
  }
}
