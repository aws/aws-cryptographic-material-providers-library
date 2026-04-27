// Class MRDiscovery
// Dafny class MRDiscovery compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MRDiscovery {
  public dafny.DafnySequence<? extends Character> _region;
  public MRDiscovery (dafny.DafnySequence<? extends Character> region) {
    this._region = region;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MRDiscovery o = (MRDiscovery)other;
    return true && java.util.Objects.equals(this._region, o._region);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._region);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.MRDiscovery.MRDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._region));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MRDiscovery> _TYPE = dafny.TypeDescriptor.<MRDiscovery>referenceWithInitializer(MRDiscovery.class, () -> MRDiscovery.Default());
  public static dafny.TypeDescriptor<MRDiscovery> _typeDescriptor() {
    return (dafny.TypeDescriptor<MRDiscovery>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MRDiscovery theDefault = MRDiscovery.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static MRDiscovery Default() {
    return theDefault;
  }
  public static MRDiscovery create(dafny.DafnySequence<? extends Character> region) {
    return new MRDiscovery(region);
  }
  public static MRDiscovery create_MRDiscovery(dafny.DafnySequence<? extends Character> region) {
    return create(region);
  }
  public boolean is_MRDiscovery() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_region() {
    return this._region;
  }
}
