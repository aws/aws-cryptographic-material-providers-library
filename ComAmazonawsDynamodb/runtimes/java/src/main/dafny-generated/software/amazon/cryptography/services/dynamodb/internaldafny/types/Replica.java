// Class Replica
// Dafny class Replica compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Replica {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RegionName;
  public Replica (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    this._RegionName = RegionName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Replica o = (Replica)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Replica.Replica");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Replica> _TYPE = dafny.TypeDescriptor.<Replica>referenceWithInitializer(Replica.class, () -> Replica.Default());
  public static dafny.TypeDescriptor<Replica> _typeDescriptor() {
    return (dafny.TypeDescriptor<Replica>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Replica theDefault = Replica.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static Replica Default() {
    return theDefault;
  }
  public static Replica create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    return new Replica(RegionName);
  }
  public static Replica create_Replica(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    return create(RegionName);
  }
  public boolean is_Replica() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RegionName() {
    return this._RegionName;
  }
}
