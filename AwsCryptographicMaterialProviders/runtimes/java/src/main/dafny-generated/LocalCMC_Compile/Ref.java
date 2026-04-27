// Class Ref<T>
// Dafny class Ref<T> compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Ref<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public Ref(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<Ref<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Ref<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Ref<T>>referenceWithInitializer(Ref.class, () -> Ref.<T>Default(_td_T));
  }

  public static <T> Ref<T> Default(dafny.TypeDescriptor<T> _td_T) {
    return Ref.<T>create_Null(_td_T);
  }
  @Deprecated()
  public static <T> Ref<T> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    return Ref.<T>create_Null(_td_T);
  }
  public static <T> Ref<T> create_Ptr(dafny.TypeDescriptor<T> _td_T, T deref) {
    return new Ref_Ptr<T>(_td_T, deref);
  }
  @Deprecated()
  public static <T> Ref<T> create_Ptr(T deref) {
    return new Ref_Ptr<T>(null, deref);
  }
  public static <T> Ref<T> create_Null(dafny.TypeDescriptor<T> _td_T) {
    return new Ref_Null<T>(_td_T);
  }
  @Deprecated()
  public static <T> Ref<T> create_Null() {
    return new Ref_Null<T>(null);
  }
  public boolean is_Ptr() { return this instanceof Ref_Ptr; }
  public boolean is_Null() { return this instanceof Ref_Null; }
  public T dtor_deref() {
    Ref<T> d = this;
    return ((Ref_Ptr<T>)d)._deref;
  }
}
