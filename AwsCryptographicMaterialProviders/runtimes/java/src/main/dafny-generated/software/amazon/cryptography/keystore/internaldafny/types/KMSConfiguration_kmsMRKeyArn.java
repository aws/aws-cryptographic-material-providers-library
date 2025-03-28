// Class KMSConfiguration_kmsMRKeyArn
// Dafny class KMSConfiguration_kmsMRKeyArn compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KMSConfiguration_kmsMRKeyArn extends KMSConfiguration {
  public dafny.DafnySequence<? extends Character> _kmsMRKeyArn;
  public KMSConfiguration_kmsMRKeyArn (dafny.DafnySequence<? extends Character> kmsMRKeyArn) {
    super();
    this._kmsMRKeyArn = kmsMRKeyArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSConfiguration_kmsMRKeyArn o = (KMSConfiguration_kmsMRKeyArn)other;
    return true && java.util.Objects.equals(this._kmsMRKeyArn, o._kmsMRKeyArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsMRKeyArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.KMSConfiguration.kmsMRKeyArn");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsMRKeyArn));
    s.append(")");
    return s.toString();
  }
}
