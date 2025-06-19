// Class WrappersInterop
// Dafny class WrappersInterop compiled into Java
package StandardLibraryInterop_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class WrappersInterop {
  public WrappersInterop() {
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreateStringSome(dafny.DafnySequence<? extends Character> s) {
    return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), s);
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreateStringNone() {
    return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
  }
  public static Wrappers_Compile.Option<Boolean> CreateBooleanSome(boolean b) {
    return Wrappers_Compile.Option.<Boolean>create_Some(dafny.TypeDescriptor.BOOLEAN, b);
  }
  public static Wrappers_Compile.Option<Boolean> CreateBooleanNone() {
    return Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN);
  }
  private static final dafny.TypeDescriptor<WrappersInterop> _TYPE = dafny.TypeDescriptor.<WrappersInterop>referenceWithInitializer(WrappersInterop.class, () -> (WrappersInterop) null);
  public static dafny.TypeDescriptor<WrappersInterop> _typeDescriptor() {
    return (dafny.TypeDescriptor<WrappersInterop>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibraryInterop.WrappersInterop";
  }
}
