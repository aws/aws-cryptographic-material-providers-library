// Class Visibility
// Dafny class Visibility compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Visibility {
  public Visibility() {
  }
  private static final dafny.TypeDescriptor<Visibility> _TYPE = dafny.TypeDescriptor.<Visibility>referenceWithInitializer(Visibility.class, () -> Visibility.Default());
  public static dafny.TypeDescriptor<Visibility> _typeDescriptor() {
    return (dafny.TypeDescriptor<Visibility>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Visibility theDefault = Visibility.create_Normal();
  public static Visibility Default() {
    return theDefault;
  }
  public static Visibility create_Normal() {
    return new Visibility_Normal();
  }
  public static Visibility create_Hidden() {
    return new Visibility_Hidden();
  }
  public static Visibility create_Deprecated() {
    return new Visibility_Deprecated();
  }
  public boolean is_Normal() { return this instanceof Visibility_Normal; }
  public boolean is_Hidden() { return this instanceof Visibility_Hidden; }
  public boolean is_Deprecated() { return this instanceof Visibility_Deprecated; }
  public static java.util.ArrayList<Visibility> AllSingletonConstructors() {
    java.util.ArrayList<Visibility> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Visibility_Normal());
    singleton_iterator.add(new Visibility_Hidden());
    singleton_iterator.add(new Visibility_Deprecated());
    return singleton_iterator;
  }
}
