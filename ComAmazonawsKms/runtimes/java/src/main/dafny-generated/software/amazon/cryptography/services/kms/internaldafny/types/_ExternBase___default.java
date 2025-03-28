// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static boolean IsValid__AliasNameType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__ArnType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(20L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(2048L)) <= 0);
  }
  public static boolean IsValid__AttestationDocumentType(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(262144L)) <= 0);
  }
  public static boolean IsValid__CiphertextType(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(6144L)) <= 0);
  }
  public static boolean IsValid__CloudHsmClusterIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(19L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(24L)) <= 0);
  }
  public static boolean IsValid__CustomKeyStoreIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(64L)) <= 0);
  }
  public static boolean IsValid__CustomKeyStoreNameType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__DescriptionType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0);
  }
  public static boolean IsValid__GrantIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__GrantNameType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__GrantTokenList(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(10L)) <= 0);
  }
  public static boolean IsValid__GrantTokenType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0);
  }
  public static boolean IsValid__KeyIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(2048L)) <= 0);
  }
  public static boolean IsValid__KeyStorePasswordType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(7L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(32L)) <= 0);
  }
  public static boolean IsValid__LimitType(int x) {
    return ((1) <= (x)) && ((x) <= (1000));
  }
  public static boolean IsValid__MarkerType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(1024L)) <= 0);
  }
  public static boolean IsValid__NumberOfBytesType(int x) {
    return ((1) <= (x)) && ((x) <= (1024));
  }
  public static boolean IsValid__PendingWindowInDaysType(int x) {
    return ((1) <= (x)) && ((x) <= (365));
  }
  public static boolean IsValid__PlaintextType(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(4096L)) <= 0);
  }
  public static boolean IsValid__PolicyNameType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__PolicyType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(131072L)) <= 0);
  }
  public static boolean IsValid__PrincipalIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__PublicKeyType(dafny.DafnySequence<? extends java.lang.Byte> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(8192L)) <= 0);
  }
  public static boolean IsValid__RegionType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(32L)) <= 0);
  }
  public static boolean IsValid__RotationPeriodInDaysType(int x) {
    return ((90) <= (x)) && ((x) <= (2560));
  }
  public static boolean IsValid__TagKeyType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__TagValueType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() != -1) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(256L)) <= 0);
  }
  public static boolean IsValid__TrustAnchorCertificateType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(5000L)) <= 0);
  }
  public static boolean IsValid__XksKeyIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__XksProxyAuthenticationAccessKeyIdType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(20L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(30L)) <= 0);
  }
  public static boolean IsValid__XksProxyAuthenticationRawSecretAccessKeyType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(43L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(64L)) <= 0);
  }
  public static boolean IsValid__XksProxyUriEndpointType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(10L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__XksProxyUriPathType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(10L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(128L)) <= 0);
  }
  public static boolean IsValid__XksProxyVpcEndpointServiceNameType(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf(20L)).compareTo(java.math.BigInteger.valueOf((x).length())) <= 0) && ((java.math.BigInteger.valueOf((x).length())).compareTo(java.math.BigInteger.valueOf(64L)) <= 0);
  }
  public static boolean IsDummySubsetType(java.math.BigInteger x) {
    return (x).signum() == 1;
  }
  @Override
  public java.lang.String toString() {
    return "ComAmazonawsKmsTypes._default";
  }
}
