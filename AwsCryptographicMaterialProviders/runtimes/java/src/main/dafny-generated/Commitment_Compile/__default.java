// Class __default
// Dafny class __default compiled into Java
package Commitment_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;
import EcdhEdkWrapping_Compile.*;
import RawECDHKeyring_Compile.*;
import AwsKmsEcdhKeyring_Compile.*;
import RawAESKeyring_Compile.*;
import RawRSAKeyring_Compile.*;
import CMM_Compile.*;
import Defaults_Compile.*;

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
