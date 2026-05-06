// Class __default
// Dafny class __default compiled into Java
package AllAlgorithmSuites_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy GetCompatibleCommitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _source0 = (algorithmSuite).dtor_id();
    if (_source0.is_ESDK()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_ESDK)_source0)._ESDK;
      if (((algorithmSuite).dtor_commitment()).is_None()) {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_FORBID__ENCRYPT__ALLOW__DECRYPT());
      } else {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT());
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _1___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_DBE)_source0)._DBE;
      return software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy.create());
    }
  }
  public static dafny.DafnySequence<? extends Character> ToHex(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite) {
    return HexStrings_Compile.__default.ToHexString((algorithmSuite).dtor_binaryId());
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> ESDKAlgorithmSuites()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _compr_0_boxed0 : software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.AllSingletonConstructors()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _compr_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _0_id = (software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId)_compr_0;
        _coll0.add(AlgorithmSuites_Compile.__default.GetESDKSuite(_0_id));
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> DBEAlgorithmSuites()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _compr_0_boxed0 : software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.AllSingletonConstructors()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _compr_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _0_id = (software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId)_compr_0;
        _coll0.add(AlgorithmSuites_Compile.__default.GetDBESuite(_0_id));
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> AllAlgorithmSuites()
  {
    return dafny.DafnySet.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>union(__default.ESDKAlgorithmSuites(), __default.DBEAlgorithmSuites());
  }
  @Override
  public java.lang.String toString() {
    return "AllAlgorithmSuites._default";
  }
}
