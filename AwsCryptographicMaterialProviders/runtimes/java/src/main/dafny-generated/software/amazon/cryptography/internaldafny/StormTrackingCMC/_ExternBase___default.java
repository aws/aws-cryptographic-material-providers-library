// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.internaldafny.StormTrackingCMC;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateGetCacheEntrySuccess(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput output) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateGetCacheEntryFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "StormTrackingCMC._default";
  }
}
