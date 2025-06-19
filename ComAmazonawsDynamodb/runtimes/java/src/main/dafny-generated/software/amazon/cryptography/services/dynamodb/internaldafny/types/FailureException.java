// Class FailureException
// Dafny class FailureException compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class FailureException {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExceptionName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExceptionDescription;
  public FailureException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionDescription) {
    this._ExceptionName = ExceptionName;
    this._ExceptionDescription = ExceptionDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    FailureException o = (FailureException)other;
    return true && java.util.Objects.equals(this._ExceptionName, o._ExceptionName) && java.util.Objects.equals(this._ExceptionDescription, o._ExceptionDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExceptionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExceptionDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.FailureException.FailureException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExceptionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExceptionDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<FailureException> _TYPE = dafny.TypeDescriptor.<FailureException>referenceWithInitializer(FailureException.class, () -> FailureException.Default());
  public static dafny.TypeDescriptor<FailureException> _typeDescriptor() {
    return (dafny.TypeDescriptor<FailureException>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final FailureException theDefault = FailureException.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static FailureException Default() {
    return theDefault;
  }
  public static FailureException create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionDescription) {
    return new FailureException(ExceptionName, ExceptionDescription);
  }
  public static FailureException create_FailureException(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExceptionDescription) {
    return create(ExceptionName, ExceptionDescription);
  }
  public boolean is_FailureException() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExceptionName() {
    return this._ExceptionName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExceptionDescription() {
    return this._ExceptionDescription;
  }
}
