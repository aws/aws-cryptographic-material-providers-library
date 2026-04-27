// Class CommandMap
// Dafny class CommandMap compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CommandMap {
  public CommandMap() {
  }
  public static boolean _Is(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> __source) {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options> _0_x = __source;
    return ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>, Boolean>)(_1_x) -> dafny.Helpers.Quantifier((_1_x).keySet().Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends Character> _forall_var_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends Character> _2_k = (dafny.DafnySequence<? extends Character>)_forall_var_0;
      return !((_1_x).<dafny.DafnySequence<? extends Character>>contains(_2_k)) || (((((Options)(java.lang.Object)((_1_x).get(_2_k)))).dtor_name()).equals(_2_k));
    }))).apply(_0_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>> _TYPE = dafny.TypeDescriptor.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>referenceWithInitializer(dafny.DafnyMap.class, () -> dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,Options> empty());
  public static dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Options>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
