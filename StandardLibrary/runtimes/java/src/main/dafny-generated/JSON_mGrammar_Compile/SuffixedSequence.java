// Class SuffixedSequence
// Dafny class SuffixedSequence compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SuffixedSequence<D, S> {
  protected dafny.TypeDescriptor<D> _td_D;
  protected dafny.TypeDescriptor<S> _td_S;
  public SuffixedSequence(dafny.TypeDescriptor<D> _td_D, dafny.TypeDescriptor<S> _td_S) {
    this._td_D = _td_D;
    this._td_S = _td_S;
  }
  public static <D, S> dafny.TypeDescriptor<dafny.DafnySequence<? extends Suffixed<D, S>>> _typeDescriptor(dafny.TypeDescriptor<D> _td_D, dafny.TypeDescriptor<S> _td_S) {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends Suffixed<D, S>>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<dafny.DafnySequence<? extends Suffixed<D, S>>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<Suffixed<D, S>> empty(Suffixed.<D, S>_typeDescriptor(_td_D, _td_S)));
  }
}
