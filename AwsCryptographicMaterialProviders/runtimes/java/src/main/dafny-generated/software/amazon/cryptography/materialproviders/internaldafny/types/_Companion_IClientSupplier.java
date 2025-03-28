// Interface IClientSupplier
// Dafny trait IClientSupplier compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_IClientSupplier {
  public _Companion_IClientSupplier() {
  }
  private static final dafny.TypeDescriptor<IClientSupplier> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(IClientSupplier.class, () -> null);
  public static dafny.TypeDescriptor<IClientSupplier> _typeDescriptor() {
    return (dafny.TypeDescriptor<IClientSupplier>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error> GetClient(IClientSupplier _this, GetClientInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, Error> _out0;
      _out0 = (_this).GetClient_k(input);
      output = _out0;
    }
    return output;
  }
}
