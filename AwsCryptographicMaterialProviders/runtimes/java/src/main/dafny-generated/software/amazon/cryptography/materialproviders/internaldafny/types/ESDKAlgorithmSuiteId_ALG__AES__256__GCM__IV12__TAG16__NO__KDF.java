// Class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF
// Dafny class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF extends ESDKAlgorithmSuiteId {
  public ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF o = (ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF");
    return s.toString();
  }
}
