// Class Endpoint
// Dafny class Endpoint compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Endpoint {
  public dafny.DafnySequence<? extends Character> _Address;
  public long _CachePeriodInMinutes;
  public Endpoint (dafny.DafnySequence<? extends Character> Address, long CachePeriodInMinutes) {
    this._Address = Address;
    this._CachePeriodInMinutes = CachePeriodInMinutes;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Endpoint o = (Endpoint)other;
    return true && java.util.Objects.equals(this._Address, o._Address) && this._CachePeriodInMinutes == o._CachePeriodInMinutes;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Address);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._CachePeriodInMinutes);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Endpoint.Endpoint");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Address));
    s.append(", ");
    s.append(this._CachePeriodInMinutes);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Endpoint> _TYPE = dafny.TypeDescriptor.<Endpoint>referenceWithInitializer(Endpoint.class, () -> Endpoint.Default());
  public static dafny.TypeDescriptor<Endpoint> _typeDescriptor() {
    return (dafny.TypeDescriptor<Endpoint>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Endpoint theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.Endpoint.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), 0L);
  public static Endpoint Default() {
    return theDefault;
  }
  public static Endpoint create(dafny.DafnySequence<? extends Character> Address, long CachePeriodInMinutes) {
    return new Endpoint(Address, CachePeriodInMinutes);
  }
  public static Endpoint create_Endpoint(dafny.DafnySequence<? extends Character> Address, long CachePeriodInMinutes) {
    return create(Address, CachePeriodInMinutes);
  }
  public boolean is_Endpoint() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_Address() {
    return this._Address;
  }
  public long dtor_CachePeriodInMinutes() {
    return this._CachePeriodInMinutes;
  }
}
