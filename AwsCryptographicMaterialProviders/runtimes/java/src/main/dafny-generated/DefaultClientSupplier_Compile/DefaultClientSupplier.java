// Class DefaultClientSupplier
// Dafny class DefaultClientSupplier compiled into Java
package DefaultClientSupplier_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DefaultClientSupplier implements software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier {
  public DefaultClientSupplier() {
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IClientSupplier.GetClient(this, input);
    return _out1;
  }
  public void __ctor()
  {
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetClient_k(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _0_maybeClient;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.services.kms.internaldafny.__default.KMSClientForRegion((input).dtor_region());
    _0_maybeClient = _out0;
    output = (_0_maybeClient).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_1_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _1_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_1_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_1_e);
    }));
    return output;
  }
  private static final dafny.TypeDescriptor<DefaultClientSupplier> _TYPE = dafny.TypeDescriptor.<DefaultClientSupplier>referenceWithInitializer(DefaultClientSupplier.class, () -> (DefaultClientSupplier) null);
  public static dafny.TypeDescriptor<DefaultClientSupplier> _typeDescriptor() {
    return (dafny.TypeDescriptor<DefaultClientSupplier>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "DefaultClientSupplier.DefaultClientSupplier";
  }
}
