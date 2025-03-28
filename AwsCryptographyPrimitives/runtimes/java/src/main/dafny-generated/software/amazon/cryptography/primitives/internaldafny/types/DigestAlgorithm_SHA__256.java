// Class DigestAlgorithm_SHA__256
// Dafny class DigestAlgorithm_SHA__256 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DigestAlgorithm_SHA__256 extends DigestAlgorithm {
  public DigestAlgorithm_SHA__256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DigestAlgorithm_SHA__256 o = (DigestAlgorithm_SHA__256)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DigestAlgorithm.SHA_256");
    return s.toString();
  }
}
