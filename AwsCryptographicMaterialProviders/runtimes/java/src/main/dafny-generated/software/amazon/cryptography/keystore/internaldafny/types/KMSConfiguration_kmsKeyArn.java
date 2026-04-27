// Class KMSConfiguration_kmsKeyArn
// Dafny class KMSConfiguration_kmsKeyArn compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KMSConfiguration_kmsKeyArn extends KMSConfiguration {
  public dafny.DafnySequence<? extends Character> _kmsKeyArn;
  public KMSConfiguration_kmsKeyArn (dafny.DafnySequence<? extends Character> kmsKeyArn) {
    super();
    this._kmsKeyArn = kmsKeyArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KMSConfiguration_kmsKeyArn o = (KMSConfiguration_kmsKeyArn)other;
    return true && java.util.Objects.equals(this._kmsKeyArn, o._kmsKeyArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsKeyArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.KMSConfiguration.kmsKeyArn");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsKeyArn));
    s.append(")");
    return s.toString();
  }
}
