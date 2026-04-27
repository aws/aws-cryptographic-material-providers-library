// Class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384
// Dafny class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384 compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384 extends ESDKAlgorithmSuiteId {
  public ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384 o = (ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384");
    return s.toString();
  }
}
