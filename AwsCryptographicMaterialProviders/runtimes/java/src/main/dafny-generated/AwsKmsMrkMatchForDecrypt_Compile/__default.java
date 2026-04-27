// Class __default
// Dafny class __default compiled into Java
package AwsKmsMrkMatchForDecrypt_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean AwsKmsMrkMatchForDecrypt(AwsArnParsing_Compile.AwsKmsIdentifier configuredAwsKmsIdentifier, AwsArnParsing_Compile.AwsKmsIdentifier messageAwsKmsIdentifer)
  {
    if (java.util.Objects.equals(configuredAwsKmsIdentifier, messageAwsKmsIdentifer)) {
      return true;
    } else {
      dafny.Tuple2<AwsArnParsing_Compile.AwsKmsIdentifier, AwsArnParsing_Compile.AwsKmsIdentifier> _source0 = dafny.Tuple2.<AwsArnParsing_Compile.AwsKmsIdentifier, AwsArnParsing_Compile.AwsKmsIdentifier>create(messageAwsKmsIdentifer, configuredAwsKmsIdentifier);
      AwsArnParsing_Compile.AwsKmsIdentifier _0___mcc_h0 = ((AwsArnParsing_Compile.AwsKmsIdentifier)(java.lang.Object)(((dafny.Tuple2<AwsArnParsing_Compile.AwsKmsIdentifier, AwsArnParsing_Compile.AwsKmsIdentifier>)_source0).dtor__0()));
      AwsArnParsing_Compile.AwsKmsIdentifier _1___mcc_h1 = ((AwsArnParsing_Compile.AwsKmsIdentifier)(java.lang.Object)(((dafny.Tuple2<AwsArnParsing_Compile.AwsKmsIdentifier, AwsArnParsing_Compile.AwsKmsIdentifier>)_source0).dtor__1()));
      AwsArnParsing_Compile.AwsKmsIdentifier _source1 = _0___mcc_h0;
      if (_source1.is_AwsKmsArnIdentifier()) {
        AwsArnParsing_Compile.AwsArn _2___mcc_h2 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source1)._a;
        AwsArnParsing_Compile.AwsKmsIdentifier _source2 = _1___mcc_h1;
        if (_source2.is_AwsKmsArnIdentifier()) {
          AwsArnParsing_Compile.AwsArn _3___mcc_h4 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source2)._a;
          AwsArnParsing_Compile.AwsArn _4_messageAwsKmsArn = _3___mcc_h4;
          AwsArnParsing_Compile.AwsArn _5_configuredAwsKmsArn = _2___mcc_h2;
          if ((!(AwsArnParsing_Compile.__default.IsMultiRegionAwsKmsArn(_5_configuredAwsKmsArn))) || (!(AwsArnParsing_Compile.__default.IsMultiRegionAwsKmsArn(_4_messageAwsKmsArn)))) {
            return false;
          } else {
            return (((((_4_messageAwsKmsArn).dtor_partition()).equals((_5_configuredAwsKmsArn).dtor_partition())) && (((_4_messageAwsKmsArn).dtor_service()).equals((_5_configuredAwsKmsArn).dtor_service()))) && (((_4_messageAwsKmsArn).dtor_account()).equals((_5_configuredAwsKmsArn).dtor_account()))) && (java.util.Objects.equals((_4_messageAwsKmsArn).dtor_resource(), (_5_configuredAwsKmsArn).dtor_resource()));
          }
        } else {
          AwsArnParsing_Compile.AwsResource _6___mcc_h6 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source2)._r;
          return false;
        }
      } else {
        AwsArnParsing_Compile.AwsResource _7___mcc_h8 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source1)._r;
        return false;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsMrkMatchForDecrypt._default";
  }
}
