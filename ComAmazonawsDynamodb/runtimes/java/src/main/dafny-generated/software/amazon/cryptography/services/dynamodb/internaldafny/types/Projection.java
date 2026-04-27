// Class Projection
// Dafny class Projection compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Projection {
  public Wrappers_Compile.Option<ProjectionType> _ProjectionType;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _NonKeyAttributes;
  public Projection (Wrappers_Compile.Option<ProjectionType> ProjectionType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> NonKeyAttributes) {
    this._ProjectionType = ProjectionType;
    this._NonKeyAttributes = NonKeyAttributes;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Projection o = (Projection)other;
    return true && java.util.Objects.equals(this._ProjectionType, o._ProjectionType) && java.util.Objects.equals(this._NonKeyAttributes, o._NonKeyAttributes);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NonKeyAttributes);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Projection.Projection");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ProjectionType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NonKeyAttributes));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Projection> _TYPE = dafny.TypeDescriptor.<Projection>referenceWithInitializer(Projection.class, () -> Projection.Default());
  public static dafny.TypeDescriptor<Projection> _typeDescriptor() {
    return (dafny.TypeDescriptor<Projection>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Projection theDefault = Projection.create(Wrappers_Compile.Option.<ProjectionType>Default(ProjectionType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(NonKeyAttributeNameList._typeDescriptor()));
  public static Projection Default() {
    return theDefault;
  }
  public static Projection create(Wrappers_Compile.Option<ProjectionType> ProjectionType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> NonKeyAttributes) {
    return new Projection(ProjectionType, NonKeyAttributes);
  }
  public static Projection create_Projection(Wrappers_Compile.Option<ProjectionType> ProjectionType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> NonKeyAttributes) {
    return create(ProjectionType, NonKeyAttributes);
  }
  public boolean is_Projection() { return true; }
  public Wrappers_Compile.Option<ProjectionType> dtor_ProjectionType() {
    return this._ProjectionType;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_NonKeyAttributes() {
    return this._NonKeyAttributes;
  }
}
