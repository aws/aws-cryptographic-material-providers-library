// Class __default
// Dafny class __default compiled into Java
package Defaults_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId GetAlgorithmSuiteForCommitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy) {
    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _source0 = commitmentPolicy;
    if (_source0.is_ESDK()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy_ESDK)_source0)._ESDK;
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy _1_c = _0___mcc_h0;
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy _source1 = _1_c;
      if (_source1.is_FORBID__ENCRYPT__ALLOW__DECRYPT()) {
        return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384());
      } else if (_source1.is_REQUIRE__ENCRYPT__ALLOW__DECRYPT()) {
        return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384());
      } else {
        return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384());
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy _2___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy_DBE)_source0)._DBE;
      return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384());
    }
  }
  @Override
  public java.lang.String toString() {
    return "Defaults._default";
  }
}
