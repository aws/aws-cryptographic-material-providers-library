// Class AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16
// Dafny class AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16 compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16 extends AesWrappingAlg {
  public AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16 o = (AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16");
    return s.toString();
  }
}
