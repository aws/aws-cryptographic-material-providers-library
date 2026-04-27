// Class CreateAwsKmsHierarchicalKeyringInput
// Dafny class CreateAwsKmsHierarchicalKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsHierarchicalKeyringInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _branchKeyId;
  public Wrappers_Compile.Option<IBranchKeyIdSupplier> _branchKeyIdSupplier;
  public software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient _keyStore;
  public long _ttlSeconds;
  public Wrappers_Compile.Option<CacheType> _cache;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _partitionId;
  public CreateAwsKmsHierarchicalKeyringInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyId, Wrappers_Compile.Option<IBranchKeyIdSupplier> branchKeyIdSupplier, software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore, long ttlSeconds, Wrappers_Compile.Option<CacheType> cache, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> partitionId) {
    this._branchKeyId = branchKeyId;
    this._branchKeyIdSupplier = branchKeyIdSupplier;
    this._keyStore = keyStore;
    this._ttlSeconds = ttlSeconds;
    this._cache = cache;
    this._partitionId = partitionId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsHierarchicalKeyringInput o = (CreateAwsKmsHierarchicalKeyringInput)other;
    return true && java.util.Objects.equals(this._branchKeyId, o._branchKeyId) && java.util.Objects.equals(this._branchKeyIdSupplier, o._branchKeyIdSupplier) && this._keyStore == o._keyStore && this._ttlSeconds == o._ttlSeconds && java.util.Objects.equals(this._cache, o._cache) && java.util.Objects.equals(this._partitionId, o._partitionId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyIdSupplier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyStore);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._ttlSeconds);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cache);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._partitionId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput.CreateAwsKmsHierarchicalKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKeyIdSupplier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keyStore));
    s.append(", ");
    s.append(this._ttlSeconds);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cache));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._partitionId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsHierarchicalKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsHierarchicalKeyringInput>referenceWithInitializer(CreateAwsKmsHierarchicalKeyringInput.class, () -> CreateAwsKmsHierarchicalKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsHierarchicalKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsHierarchicalKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsHierarchicalKeyringInput theDefault = CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<IBranchKeyIdSupplier>Default(((dafny.TypeDescriptor<IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(IBranchKeyIdSupplier.class))), null, 0L, Wrappers_Compile.Option.<CacheType>Default(CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static CreateAwsKmsHierarchicalKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsHierarchicalKeyringInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyId, Wrappers_Compile.Option<IBranchKeyIdSupplier> branchKeyIdSupplier, software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore, long ttlSeconds, Wrappers_Compile.Option<CacheType> cache, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> partitionId) {
    return new CreateAwsKmsHierarchicalKeyringInput(branchKeyId, branchKeyIdSupplier, keyStore, ttlSeconds, cache, partitionId);
  }
  public static CreateAwsKmsHierarchicalKeyringInput create_CreateAwsKmsHierarchicalKeyringInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> branchKeyId, Wrappers_Compile.Option<IBranchKeyIdSupplier> branchKeyIdSupplier, software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore, long ttlSeconds, Wrappers_Compile.Option<CacheType> cache, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> partitionId) {
    return create(branchKeyId, branchKeyIdSupplier, keyStore, ttlSeconds, cache, partitionId);
  }
  public boolean is_CreateAwsKmsHierarchicalKeyringInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_branchKeyId() {
    return this._branchKeyId;
  }
  public Wrappers_Compile.Option<IBranchKeyIdSupplier> dtor_branchKeyIdSupplier() {
    return this._branchKeyIdSupplier;
  }
  public software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient dtor_keyStore() {
    return this._keyStore;
  }
  public long dtor_ttlSeconds() {
    return this._ttlSeconds;
  }
  public Wrappers_Compile.Option<CacheType> dtor_cache() {
    return this._cache;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_partitionId() {
    return this._partitionId;
  }
}
