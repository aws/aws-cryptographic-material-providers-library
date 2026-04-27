// Class Error_XksProxyVpcEndpointServiceInvalidConfigurationException
// Dafny class Error_XksProxyVpcEndpointServiceInvalidConfigurationException compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Error_XksProxyVpcEndpointServiceInvalidConfigurationException extends Error {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _message;
  public Error_XksProxyVpcEndpointServiceInvalidConfigurationException (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> message) {
    super();
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Error_XksProxyVpcEndpointServiceInvalidConfigurationException o = (Error_XksProxyVpcEndpointServiceInvalidConfigurationException)other;
    return true && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 46;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.Error.XksProxyVpcEndpointServiceInvalidConfigurationException");
    s.append("(");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
}
