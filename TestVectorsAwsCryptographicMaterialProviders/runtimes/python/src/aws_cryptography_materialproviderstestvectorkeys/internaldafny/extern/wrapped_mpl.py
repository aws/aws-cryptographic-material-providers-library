import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import standard_library.internaldafny.generated.Wrappers as Wrappers

class default__(WrappedMaterialProviders.default__):

  @staticmethod
  def WrappedMaterialProviders(config):  
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.config
    import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
    c = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client.AwsCryptographicMaterialProviders(
      dafny_client=MaterialProviders.default__.MaterialProviders(config).value
    )
    import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.shim as shim
    wrapped_client = shim.MaterialProvidersShim(c)
    return Wrappers.Result_Success(wrapped_client)

WrappedMaterialProviders.default__ = default__