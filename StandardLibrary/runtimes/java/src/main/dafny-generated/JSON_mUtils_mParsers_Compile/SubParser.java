// Class SubParser
// Dafny class SubParser compiled into Java
package JSON_mUtils_mParsers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SubParser<T, R> {
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public SubParser(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    this._td_T = _td_T;
    this._td_R = _td_R;
  }
  public static <T, R> SubParser__<T, R> defaultValue(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return __default.<T, R>SubParserWitness(_td_T, _td_R);
  }
  public static <T, R> dafny.TypeDescriptor<SubParser__<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<SubParser__<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<SubParser__<T, R>>referenceWithInitializer(SubParser__.class, () -> SubParser.defaultValue(_td_T, _td_R));
  }
}
