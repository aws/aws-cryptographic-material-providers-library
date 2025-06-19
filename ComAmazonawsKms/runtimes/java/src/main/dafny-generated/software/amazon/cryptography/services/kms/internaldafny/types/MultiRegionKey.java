// Class MultiRegionKey
// Dafny class MultiRegionKey compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MultiRegionKey {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Arn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Region;
  public MultiRegionKey (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Region) {
    this._Arn = Arn;
    this._Region = Region;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MultiRegionKey o = (MultiRegionKey)other;
    return true && java.util.Objects.equals(this._Arn, o._Arn) && java.util.Objects.equals(this._Region, o._Region);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Arn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Region);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.MultiRegionKey.MultiRegionKey");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Arn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Region));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MultiRegionKey> _TYPE = dafny.TypeDescriptor.<MultiRegionKey>referenceWithInitializer(MultiRegionKey.class, () -> MultiRegionKey.Default());
  public static dafny.TypeDescriptor<MultiRegionKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<MultiRegionKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MultiRegionKey theDefault = MultiRegionKey.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ArnType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(RegionType._typeDescriptor()));
  public static MultiRegionKey Default() {
    return theDefault;
  }
  public static MultiRegionKey create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Region) {
    return new MultiRegionKey(Arn, Region);
  }
  public static MultiRegionKey create_MultiRegionKey(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Region) {
    return create(Arn, Region);
  }
  public boolean is_MultiRegionKey() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Arn() {
    return this._Arn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Region() {
    return this._Region;
  }
}
