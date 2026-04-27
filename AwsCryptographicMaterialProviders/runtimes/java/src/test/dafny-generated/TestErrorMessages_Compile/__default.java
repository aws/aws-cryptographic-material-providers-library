// Class __default
// Dafny class __default compiled into Java
package TestErrorMessages_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void TestIncorrectRawDataKeys()
  {
    dafny.DafnySequence<? extends Character> _0_datakey;
    _0_datakey = dafny.DafnySequence.asString("0");
    dafny.DafnySequence<? extends Character> _1_keyringName;
    _1_keyringName = dafny.DafnySequence.asString("RSAKeyring");
    dafny.DafnySequence<? extends Character> _2_keyProviderId;
    _2_keyProviderId = dafny.DafnySequence.asString("TestProvider");
    dafny.DafnySequence<? extends Character> _3_actualErrorMessage;
    _3_actualErrorMessage = ErrorMessages_Compile.__default.IncorrectRawDataKeys(_0_datakey, _1_keyringName, _2_keyProviderId);
    dafny.DafnySequence<? extends Character> _4_ExpectErrorMessage;
    _4_ExpectErrorMessage = dafny.DafnySequence.asString("EncryptedDataKey 0 did not match RSAKeyring. Expected: keyProviderId: TestProvider.\n");
    if (!((_3_actualErrorMessage).equals(_4_ExpectErrorMessage))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestErrorMessages.dfy(22,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestIncorrectDataKeys()
  {
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _0_dummyKey;
    _0_dummyKey = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(__default.awskms(), __default.keyproviderInfoA(), dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 2, (byte) 3, (byte) 4, (byte) 5)), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(__default.awskmsrsa(), __default.keyproviderInfoB(), dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 2, (byte) 3, (byte) 4, (byte) 5)), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(__default.awskmshierarchy(), __default.keyproviderInfoC(), dafny.DafnySequence.<java.lang.Byte> of((byte) 64, (byte) 92, (byte) 115, (byte) 7, (byte) 85, (byte) 121, (byte) 112, (byte) 79, (byte) 69, (byte) 12, (byte) 82, (byte) 25, (byte) 67, (byte) 34, (byte) 11, (byte) 66, (byte) 93, (byte) 45, (byte) 40, (byte) 23, (byte) 90, (byte) 61, (byte) 16, (byte) 28, (byte) 59, (byte) 114, (byte) 52, (byte) 122, (byte) 50, (byte) 23, (byte) 11, (byte) 101, (byte) 48, (byte) 53, (byte) 30, (byte) 120, (byte) 51, (byte) 74, (byte) 77, (byte) 53, (byte) 57, (byte) 99, (byte) 53, (byte) 13, (byte) 30, (byte) 21, (byte) 109, (byte) 85, (byte) 15, (byte) 86, (byte) 47, (byte) 84, (byte) 91, (byte) 85, (byte) 87, (byte) 60, (byte) 4, (byte) 56, (byte) 67, (byte) 74, (byte) 29, (byte) 87, (byte) 85, (byte) 106, (byte) 8, (byte) 82, (byte) 63, (byte) 114, (byte) 100, (byte) 110, (byte) 68, (byte) 58, (byte) 83, (byte) 24, (byte) 111, (byte) 41, (byte) 21, (byte) 91, (byte) 122, (byte) 61, (byte) 118, (byte) 37, (byte) 72, (byte) 38, (byte) 67, (byte) 2, (byte) 17, (byte) 61, (byte) 17, (byte) 121, (byte) 7, (byte) 90, (byte) 117, (byte) 49, (byte) 30, (byte) 20, (byte) 89, (byte) 68, (byte) 33, (byte) 111, (byte) 107, (byte) 5, (byte) 120, (byte) 20, (byte) 95, (byte) 78, (byte) 70, (byte) 2, (byte) 49, (byte) 84, (byte) 39, (byte) 50, (byte) 40, (byte) 40, (byte) 115, (byte) 114, (byte) 76, (byte) 18, (byte) 103, (byte) 84, (byte) 34, (byte) 123, (byte) 1, (byte) 125, (byte) 61, (byte) 33, (byte) 13, (byte) 18, (byte) 81, (byte) 24, (byte) 53, (byte) 53, (byte) 26, (byte) 60, (byte) 52, (byte) 85, (byte) 81, (byte) 96, (byte) 85, (byte) 72)));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _1_valueOrError0 = ErrorMessages_Compile.__default.IncorrectDataKeys(_0_dummyKey, AlgorithmSuites_Compile.__default.GetSuite(__default.TEST__DBE__ALG__SUITE__ID()), dafny.DafnySequence.asString(""));
    if (!(!((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestErrorMessages.dfy(82,30): " + java.lang.String.valueOf(_1_valueOrError0));
    }
    dafny.DafnySequence<? extends Character> _2_actualErrorMessage;
    _2_actualErrorMessage = (_1_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _3_ExpectErrorMessage;
    _3_ExpectErrorMessage = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n"), dafny.DafnySequence.asString("KeyProviderId: aws-kms, KeyProviderInfo: keyproviderInfoA\n")), dafny.DafnySequence.asString("KeyProviderId: aws-kms-rsa, KeyProviderInfo: keyproviderInfoB\n")), dafny.DafnySequence.asString("KeyProviderId: aws-kms-hierarchy, KeyProviderInfo: keyproviderInfoC, BranchKeyVersion: 155b7a3d-7625-4826-4302-113d1179075a\n"));
    if (!((_2_actualErrorMessage).equals(_3_ExpectErrorMessage))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestErrorMessages.dfy(87,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> awskms()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> keyproviderInfoA()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 107, (byte) 101, (byte) 121, (byte) 112, (byte) 114, (byte) 111, (byte) 118, (byte) 105, (byte) 100, (byte) 101, (byte) 114, (byte) 73, (byte) 110, (byte) 102, (byte) 111, (byte) 65);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> awskmsrsa()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115, (byte) 45, (byte) 114, (byte) 115, (byte) 97);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> keyproviderInfoB()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 107, (byte) 101, (byte) 121, (byte) 112, (byte) 114, (byte) 111, (byte) 118, (byte) 105, (byte) 100, (byte) 101, (byte) 114, (byte) 73, (byte) 110, (byte) 102, (byte) 111, (byte) 66);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> awskmshierarchy()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 119, (byte) 115, (byte) 45, (byte) 107, (byte) 109, (byte) 115, (byte) 45, (byte) 104, (byte) 105, (byte) 101, (byte) 114, (byte) 97, (byte) 114, (byte) 99, (byte) 104, (byte) 121);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> keyproviderInfoC()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 107, (byte) 101, (byte) 121, (byte) 112, (byte) 114, (byte) 111, (byte) 118, (byte) 105, (byte) 100, (byte) 101, (byte) 114, (byte) 73, (byte) 110, (byte) 102, (byte) 111, (byte) 67);
    return _0_s;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId TEST__DBE__ALG__SUITE__ID()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384());
  }
  @Override
  public java.lang.String toString() {
    return "TestErrorMessages._default";
  }
}
