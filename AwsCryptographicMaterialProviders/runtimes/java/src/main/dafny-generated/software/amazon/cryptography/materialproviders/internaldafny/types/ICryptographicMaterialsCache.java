// Interface ICryptographicMaterialsCache
// Dafny trait ICryptographicMaterialsCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public interface ICryptographicMaterialsCache {
  public Wrappers_Compile.Result<dafny.Tuple0, Error> PutCacheEntry(PutCacheEntryInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> PutCacheEntry_k(PutCacheEntryInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UpdateUsageMetadata(UpdateUsageMetadataInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> UpdateUsageMetadata_k(UpdateUsageMetadataInput input);
  public Wrappers_Compile.Result<GetCacheEntryOutput, Error> GetCacheEntry(GetCacheEntryInput input);
  public Wrappers_Compile.Result<GetCacheEntryOutput, Error> GetCacheEntry_k(GetCacheEntryInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DeleteCacheEntry(DeleteCacheEntryInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DeleteCacheEntry_k(DeleteCacheEntryInput input);
}
