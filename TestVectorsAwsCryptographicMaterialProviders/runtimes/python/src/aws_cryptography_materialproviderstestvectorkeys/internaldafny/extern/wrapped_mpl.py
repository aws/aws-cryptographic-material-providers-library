import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.config
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.shim as shim

class default__(WrappedMaterialProviders.default__):

  @staticmethod
  def WrappedMaterialProviders(config):  
    smithy_client = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client.AwsCryptographicMaterialProviders(
      dafny_client=MaterialProviders.default__.MaterialProviders(config).value
    )
    wrapped_client = shim.MaterialProvidersShim(smithy_client)
    return Wrappers.Result_Success(wrapped_client)

WrappedMaterialProviders.default__ = default__