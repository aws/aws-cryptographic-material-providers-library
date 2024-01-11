import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import Wrappers

class default__(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__):

  @staticmethod
  def WrappedMaterialProviders(config):    
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.config
    import software_amazon_cryptography_materialproviders_internaldafny
    print(f"{config=}")
    c = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client.AwsCryptographicMaterialProviders(
      dafny_client=software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(config).value
    )
    # The default plugin.py implementation does not work here...
    # Need to dive into this...
    # This is similar to Dependencies extern..?
    # TODO-Python
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.shim
    wrapped_client = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.shim.MaterialProvidersShim(c)
    return Wrappers.Result_Success(wrapped_client)

software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__ = default__