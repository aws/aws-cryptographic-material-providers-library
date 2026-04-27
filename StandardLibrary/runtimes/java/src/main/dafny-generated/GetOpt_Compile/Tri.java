// Class Tri
// Dafny class Tri compiled into Java
package GetOpt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Tri {
  public Tri() {
  }
  private static final dafny.TypeDescriptor<Tri> _TYPE = dafny.TypeDescriptor.<Tri>referenceWithInitializer(Tri.class, () -> Tri.Default());
  public static dafny.TypeDescriptor<Tri> _typeDescriptor() {
    return (dafny.TypeDescriptor<Tri>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Tri theDefault = Tri.create_Yes();
  public static Tri Default() {
    return theDefault;
  }
  public static Tri create_Yes() {
    return new Tri_Yes();
  }
  public static Tri create_No() {
    return new Tri_No();
  }
  public static Tri create_Maybe() {
    return new Tri_Maybe();
  }
  public boolean is_Yes() { return this instanceof Tri_Yes; }
  public boolean is_No() { return this instanceof Tri_No; }
  public boolean is_Maybe() { return this instanceof Tri_Maybe; }
  public static java.util.ArrayList<Tri> AllSingletonConstructors() {
    java.util.ArrayList<Tri> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Tri_Yes());
    singleton_iterator.add(new Tri_No());
    singleton_iterator.add(new Tri_Maybe());
    return singleton_iterator;
  }
}
