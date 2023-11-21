import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import Wrappers

class default__(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__):

  @staticmethod
  def WrappedMaterialProviders(config):
    import aws_cryptography_materialproviders.smithygenerated.client
    c = aws_cryptography_materialproviders.smithygenerated.client.AwsCryptographicMaterialProviders()
    # The default plugin.py implementation does not work here...
    # Need to dive into this...
    # This is similar to Dependencies extern..?
    # TODO-Python
    import software_amazon_cryptography_materialproviders_internaldafny
    c._config.dafnyImplInterface.impl = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(config).value
    import aws_cryptography_materialproviders.smithygenerated.shim
    wrapped_client = aws_cryptography_materialproviders.smithygenerated.shim.MaterialProvidersShim(c)
    return Wrappers.Result_Success(wrapped_client)

software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__ = default__