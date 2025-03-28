// Class DataKeySpec_AES__256
// Dafny class DataKeySpec_AES__256 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DataKeySpec_AES__256 extends DataKeySpec {
  public DataKeySpec_AES__256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DataKeySpec_AES__256 o = (DataKeySpec_AES__256)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DataKeySpec.AES_256");
    return s.toString();
  }
}
