// Class __default
// Dafny class __default compiled into Java
package AwsKmsMrkDiscoveryKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> ToStringForRegion(AwsArnParsing_Compile.AwsArn arn, dafny.DafnySequence<? extends Character> region)
  {
    if (AwsArnParsing_Compile.__default.IsMultiRegionAwsKmsArn(arn)) {
      return (arn).ToArnString(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), region));
    } else {
      return (arn).ToString();
    }
  }
  public static boolean DiscoveryMatch(AwsArnParsing_Compile.AwsArn arn, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter, dafny.DafnySequence<? extends Character> region)
  {
    AwsArnParsing_Compile.AwsArn _pat_let_tv0 = arn;
    AwsArnParsing_Compile.AwsArn _pat_let_tv1 = arn;
    return (((java.util.function.Function<Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>, Boolean>)(_source0_boxed0) -> {
      Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _source0 = ((Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>)(java.lang.Object)(_source0_boxed0));
      if (_source0.is_None()) {
        return true;
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _0___mcc_h0 = ((Wrappers_Compile.Option_Some<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>)_source0)._value;
        software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _1_filter = _0___mcc_h0;
        return (((_1_filter).dtor_partition()).equals((_pat_let_tv0).dtor_partition())) && (((_1_filter).dtor_accountIds()).contains((_pat_let_tv1).dtor_account()));
      }
    }).apply(discoveryFilter)) && (((!(AwsArnParsing_Compile.__default.IsMultiRegionAwsKmsArn(arn))) ? ((region).equals((arn).dtor_region())) : (true)));
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsMrkDiscoveryKeyring._default";
  }
}
