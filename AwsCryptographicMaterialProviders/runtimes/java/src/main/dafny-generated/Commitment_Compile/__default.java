// Class __default
// Dafny class __default compiled into Java
package Commitment_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId algorithm, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite = AlgorithmSuites_Compile.__default.GetSuite(algorithm);
    if ((java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_FORBID__ENCRYPT__ALLOW__DECRYPT()))) && (!(((_0_suite).dtor_commitment()).is_None()))) {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidAlgorithmSuiteInfoOnEncrypt(dafny.DafnySequence.asString("Configuration conflict. Commitment policy requires only non-committing algorithm suites")));
    } else if ((((java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__ALLOW__DECRYPT()))) || (java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())))) || (java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy.create())))) && (((_0_suite).dtor_commitment()).is_None())) {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidAlgorithmSuiteInfoOnEncrypt(dafny.DafnySequence.asString("Configuration conflict. Commitment policy requires only committing algorithm suites")));
    } else {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
  }
  public static Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId algorithm, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy commitmentPolicy)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite = AlgorithmSuites_Compile.__default.GetSuite(algorithm);
    if (((true) && ((java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()))) || (java.util.Objects.equals(commitmentPolicy, software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy.create()))))) && (((_0_suite).dtor_commitment()).is_None())) {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidAlgorithmSuiteInfoOnDecrypt(dafny.DafnySequence.asString("Configuration conflict. Commitment policy requires only committing algorithm suites")));
    } else {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
  }
  @Override
  public java.lang.String toString() {
    return "Commitment._default";
  }
}
