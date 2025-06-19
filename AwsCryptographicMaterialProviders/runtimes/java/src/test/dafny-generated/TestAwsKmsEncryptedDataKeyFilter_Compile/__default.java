// Class __default
// Dafny class __default compiled into Java
package TestAwsKmsEncryptedDataKeyFilter_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestFailsNonKeyResource()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _0_discoveryFilter;
    software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _out0;
    _out0 = __default.GetDiscoveryFilter();
    _0_discoveryFilter = _out0;
    AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter _1_edkFilter;
    AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter _nw0 = new AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter();
    _nw0.__ctor(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor(), _0_discoveryFilter));
    _1_edkFilter = _nw0;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _2_badEdk;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out1;
    _out1 = __default.GetNonKeyEncryptedDataKey();
    _2_badEdk = _out1;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_filterResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _1_edkFilter, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _2_badEdk));
    _3_filterResult = _out2;
    if (!((_3_filterResult).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(32,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.Error _4_test;
    _4_test = (_3_filterResult).dtor_error();
    if (!((_4_test).is_AwsCryptographicMaterialProvidersException())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(34,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_4_test).dtor_message()).equals(dafny.DafnySequence.asString("Only AWS KMS Keys supported")))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(35,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestMatchesKeyringsConfiguration()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _0_matchingEdk;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out0;
    _out0 = TestUtils_Compile.__default.GenerateMockEncryptedDataKey(dafny.DafnySequence.asString("aws-kms"), TestUtils_Compile.__default.SHARED__TEST__KEY__ARN());
    _0_matchingEdk = _out0;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _1_mismatchEdkPartition;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out1;
    _out1 = TestUtils_Compile.__default.GenerateMockEncryptedDataKey(dafny.DafnySequence.asString("aws-kms"), dafny.DafnySequence.asString("arn:aws-cn:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"));
    _1_mismatchEdkPartition = _out1;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _2_mismatchEdkAccount;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out2;
    _out2 = TestUtils_Compile.__default.GenerateMockEncryptedDataKey(dafny.DafnySequence.asString("aws-kms"), dafny.DafnySequence.asString("arn:aws:kms:us-west-2:827585335069:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"));
    _2_mismatchEdkAccount = _out2;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _3_mismatchEdkProviderId;
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out3;
    _out3 = TestUtils_Compile.__default.GenerateMockEncryptedDataKey(dafny.DafnySequence.asString("aws"), TestUtils_Compile.__default.SHARED__TEST__KEY__ARN());
    _3_mismatchEdkProviderId = _out3;
    software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _4_discoveryFilter;
    software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter _out4;
    _out4 = __default.GetDiscoveryFilter();
    _4_discoveryFilter = _out4;
    AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter _5_edkFilter;
    AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter _nw0 = new AwsKmsDiscoveryKeyring_Compile.AwsKmsEncryptedDataKeyFilter();
    _nw0.__ctor(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor(), _4_discoveryFilter));
    _5_edkFilter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_filterResult;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _5_edkFilter, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _0_matchingEdk, _1_mismatchEdkPartition, _2_mismatchEdkAccount, _3_mismatchEdkProviderId));
    _6_filterResult = _out5;
    if (!((_6_filterResult).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(65,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(java.math.BigInteger.valueOf(((_6_filterResult).dtor_value()).length()), java.math.BigInteger.ONE))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(66,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(java.util.Objects.equals(((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((_6_filterResult).dtor_value()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), _0_matchingEdk))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(67,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter GetDiscoveryFilter()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter discoveryFilter = software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter.Default();
    discoveryFilter = software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter.create(TestUtils_Compile.__default.ACCOUNT__IDS(), TestUtils_Compile.__default.PARTITION());
    return discoveryFilter;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey GetNonKeyEncryptedDataKey()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.Default();
    if(true) {
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _out0;
      _out0 = TestUtils_Compile.__default.GenerateMockEncryptedDataKey(dafny.DafnySequence.asString("aws-kms"), dafny.DafnySequence.asString("arn:aws:kms:us-west-2:658956600833:alias/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"));
      edk = _out0;
    }
    return edk;
  }
  @Override
  public java.lang.String toString() {
    return "TestAwsKmsEncryptedDataKeyFilter._default";
  }
}
