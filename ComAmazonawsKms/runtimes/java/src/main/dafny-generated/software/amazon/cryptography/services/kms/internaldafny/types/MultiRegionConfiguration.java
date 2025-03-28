// Class MultiRegionConfiguration
// Dafny class MultiRegionConfiguration compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class MultiRegionConfiguration {
  public Wrappers_Compile.Option<MultiRegionKeyType> _MultiRegionKeyType;
  public Wrappers_Compile.Option<MultiRegionKey> _PrimaryKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends MultiRegionKey>> _ReplicaKeys;
  public MultiRegionConfiguration (Wrappers_Compile.Option<MultiRegionKeyType> MultiRegionKeyType, Wrappers_Compile.Option<MultiRegionKey> PrimaryKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends MultiRegionKey>> ReplicaKeys) {
    this._MultiRegionKeyType = MultiRegionKeyType;
    this._PrimaryKey = PrimaryKey;
    this._ReplicaKeys = ReplicaKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MultiRegionConfiguration o = (MultiRegionConfiguration)other;
    return true && java.util.Objects.equals(this._MultiRegionKeyType, o._MultiRegionKeyType) && java.util.Objects.equals(this._PrimaryKey, o._PrimaryKey) && java.util.Objects.equals(this._ReplicaKeys, o._ReplicaKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MultiRegionKeyType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PrimaryKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.MultiRegionConfiguration.MultiRegionConfiguration");
    s.append("(");
    s.append(dafny.Helpers.toString(this._MultiRegionKeyType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PrimaryKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MultiRegionConfiguration> _TYPE = dafny.TypeDescriptor.<MultiRegionConfiguration>referenceWithInitializer(MultiRegionConfiguration.class, () -> MultiRegionConfiguration.Default());
  public static dafny.TypeDescriptor<MultiRegionConfiguration> _typeDescriptor() {
    return (dafny.TypeDescriptor<MultiRegionConfiguration>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MultiRegionConfiguration theDefault = software.amazon.cryptography.services.kms.internaldafny.types.MultiRegionConfiguration.create(Wrappers_Compile.Option.<MultiRegionKeyType>Default(MultiRegionKeyType._typeDescriptor()), Wrappers_Compile.Option.<MultiRegionKey>Default(MultiRegionKey._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends MultiRegionKey>>Default(dafny.DafnySequence.<MultiRegionKey>_typeDescriptor(MultiRegionKey._typeDescriptor())));
  public static MultiRegionConfiguration Default() {
    return theDefault;
  }
  public static MultiRegionConfiguration create(Wrappers_Compile.Option<MultiRegionKeyType> MultiRegionKeyType, Wrappers_Compile.Option<MultiRegionKey> PrimaryKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends MultiRegionKey>> ReplicaKeys) {
    return new MultiRegionConfiguration(MultiRegionKeyType, PrimaryKey, ReplicaKeys);
  }
  public static MultiRegionConfiguration create_MultiRegionConfiguration(Wrappers_Compile.Option<MultiRegionKeyType> MultiRegionKeyType, Wrappers_Compile.Option<MultiRegionKey> PrimaryKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends MultiRegionKey>> ReplicaKeys) {
    return create(MultiRegionKeyType, PrimaryKey, ReplicaKeys);
  }
  public boolean is_MultiRegionConfiguration() { return true; }
  public Wrappers_Compile.Option<MultiRegionKeyType> dtor_MultiRegionKeyType() {
    return this._MultiRegionKeyType;
  }
  public Wrappers_Compile.Option<MultiRegionKey> dtor_PrimaryKey() {
    return this._PrimaryKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends MultiRegionKey>> dtor_ReplicaKeys() {
    return this._ReplicaKeys;
  }
}
