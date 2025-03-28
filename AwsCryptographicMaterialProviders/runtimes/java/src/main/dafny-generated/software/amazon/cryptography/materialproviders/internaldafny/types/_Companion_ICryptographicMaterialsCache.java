// Interface ICryptographicMaterialsCache
// Dafny trait ICryptographicMaterialsCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_ICryptographicMaterialsCache {
  public _Companion_ICryptographicMaterialsCache() {
  }
  private static final dafny.TypeDescriptor<ICryptographicMaterialsCache> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(ICryptographicMaterialsCache.class, () -> null);
  public static dafny.TypeDescriptor<ICryptographicMaterialsCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<ICryptographicMaterialsCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, Error> PutCacheEntry(ICryptographicMaterialsCache _this, PutCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, Error> output = Wrappers_Compile.Result.<dafny.Tuple0, Error>Default(dafny.Tuple0._typeDescriptor(), Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.Tuple0, Error> _out0;
      _out0 = (_this).PutCacheEntry_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, Error> UpdateUsageMetadata(ICryptographicMaterialsCache _this, UpdateUsageMetadataInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, Error> output = Wrappers_Compile.Result.<dafny.Tuple0, Error>Default(dafny.Tuple0._typeDescriptor(), Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.Tuple0, Error> _out0;
      _out0 = (_this).UpdateUsageMetadata_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<GetCacheEntryOutput, Error> GetCacheEntry(ICryptographicMaterialsCache _this, GetCacheEntryInput input)
  {
    Wrappers_Compile.Result<GetCacheEntryOutput, Error> output = (Wrappers_Compile.Result<GetCacheEntryOutput, Error>)null;
    if(true) {
      Wrappers_Compile.Result<GetCacheEntryOutput, Error> _out0;
      _out0 = (_this).GetCacheEntry_k(input);
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, Error> DeleteCacheEntry(ICryptographicMaterialsCache _this, DeleteCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, Error> output = Wrappers_Compile.Result.<dafny.Tuple0, Error>Default(dafny.Tuple0._typeDescriptor(), Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.Tuple0, Error> _out0;
      _out0 = (_this).DeleteCacheEntry_k(input);
      output = _out0;
    }
    return output;
  }
}
