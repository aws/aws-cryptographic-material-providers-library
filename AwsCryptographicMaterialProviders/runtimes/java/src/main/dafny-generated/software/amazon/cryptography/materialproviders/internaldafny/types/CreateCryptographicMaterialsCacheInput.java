// Class CreateCryptographicMaterialsCacheInput
// Dafny class CreateCryptographicMaterialsCacheInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateCryptographicMaterialsCacheInput {
  public CacheType _cache;
  public CreateCryptographicMaterialsCacheInput (CacheType cache) {
    this._cache = cache;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateCryptographicMaterialsCacheInput o = (CreateCryptographicMaterialsCacheInput)other;
    return true && java.util.Objects.equals(this._cache, o._cache);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cache);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput.CreateCryptographicMaterialsCacheInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._cache));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateCryptographicMaterialsCacheInput> _TYPE = dafny.TypeDescriptor.<CreateCryptographicMaterialsCacheInput>referenceWithInitializer(CreateCryptographicMaterialsCacheInput.class, () -> CreateCryptographicMaterialsCacheInput.Default());
  public static dafny.TypeDescriptor<CreateCryptographicMaterialsCacheInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateCryptographicMaterialsCacheInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateCryptographicMaterialsCacheInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(CacheType.Default());
  public static CreateCryptographicMaterialsCacheInput Default() {
    return theDefault;
  }
  public static CreateCryptographicMaterialsCacheInput create(CacheType cache) {
    return new CreateCryptographicMaterialsCacheInput(cache);
  }
  public static CreateCryptographicMaterialsCacheInput create_CreateCryptographicMaterialsCacheInput(CacheType cache) {
    return create(cache);
  }
  public boolean is_CreateCryptographicMaterialsCacheInput() { return true; }
  public CacheType dtor_cache() {
    return this._cache;
  }
}
