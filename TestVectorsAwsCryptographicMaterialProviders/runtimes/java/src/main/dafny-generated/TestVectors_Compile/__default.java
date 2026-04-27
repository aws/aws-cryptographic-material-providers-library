// Class __default
// Dafny class __default compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.Tuple2 TestGetEncryptionMaterials(EncryptTest test)
  {
    boolean testResult = false;
    Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> materials = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Default(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_result;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = ((test).dtor_cmm()).GetEncryptionMaterials((test).dtor_input());
      _0_result = _out0;
      EncryptTestVector _source0 = (test).dtor_vector();
      if (_source0.is_PositiveEncryptKeyringVector()) {
        dafny.DafnySequence<? extends Character> _1___mcc_h0 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._name;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2___mcc_h1 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._description;
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3___mcc_h2 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptionContext;
        software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _4___mcc_h3 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._commitmentPolicy;
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _5___mcc_h4 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._algorithmSuite;
        Wrappers_Compile.Option<java.lang.Long> _6___mcc_h5 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._maxPlaintextLength;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _7___mcc_h6 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._requiredEncryptionContextKeys;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _8___mcc_h7 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptDescription;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _9___mcc_h8 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._decryptDescription;
        Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _10___mcc_h9 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._reproducedEncryptionContext;
        testResult = (_0_result).is_Success();
      } else if (_source0.is_PositiveEncryptNegativeDecryptKeyringVector()) {
        dafny.DafnySequence<? extends Character> _11___mcc_h10 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._name;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _12___mcc_h11 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._description;
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _13___mcc_h12 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptionContext;
        software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _14___mcc_h13 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._commitmentPolicy;
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15___mcc_h14 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._algorithmSuite;
        Wrappers_Compile.Option<java.lang.Long> _16___mcc_h15 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._maxPlaintextLength;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _17___mcc_h16 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._requiredEncryptionContextKeys;
        dafny.DafnySequence<? extends Character> _18___mcc_h17 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptErrorDescription;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _19___mcc_h18 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptDescription;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _20___mcc_h19 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptDescription;
        Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _21___mcc_h20 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._reproducedEncryptionContext;
        testResult = (_0_result).is_Success();
      } else {
        dafny.DafnySequence<? extends Character> _22___mcc_h21 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._name;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _23___mcc_h22 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._description;
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _24___mcc_h23 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._encryptionContext;
        software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _25___mcc_h24 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._commitmentPolicy;
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _26___mcc_h25 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._algorithmSuite;
        Wrappers_Compile.Option<java.lang.Long> _27___mcc_h26 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._maxPlaintextLength;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _28___mcc_h27 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._requiredEncryptionContextKeys;
        dafny.DafnySequence<? extends Character> _29___mcc_h28 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._errorDescription;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _30___mcc_h29 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._keyDescription;
        testResult = !((_0_result).is_Success());
      }
      if ((testResult) && ((_0_result).is_Success())) {
        materials = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), ((_0_result).dtor_value()).dtor_encryptionMaterials());
      } else {
        materials = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor());
      }
      if (!(testResult)) {
        System.out.print((dafny.DafnySequence.asString("\nTEST===> ")).verbatimString());
        System.out.print((((test).dtor_vector()).dtor_name()).verbatimString());
        System.out.print(((((((test).dtor_vector()).dtor_description()).is_Some()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\n"), (((test).dtor_vector()).dtor_description()).dtor_value())) : (dafny.DafnySequence.asString("")))).verbatimString());
        System.out.print((((((test).dtor_vector()).is_NegativeEncryptKeyringVector()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\n"), ((test).dtor_vector()).dtor_errorDescription())) : (dafny.DafnySequence.asString("")))).verbatimString());
        System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
        if ((((test).dtor_vector()).is_PositiveEncryptKeyringVector()) || (((test).dtor_vector()).is_PositiveEncryptNegativeDecryptKeyringVector())) {
          System.out.print(java.lang.String.valueOf((_0_result).dtor_error()));
        }
        System.out.print((dafny.DafnySequence.asString("\nFAILED! <-----------\n")).verbatimString());
      }
    }
    return new dafny.Tuple2<>(testResult, materials);
  }
  public static boolean TestDecryptMaterials(DecryptTest test)
  {
    boolean output = false;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_result;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = ((test).dtor_cmm()).DecryptMaterials((test).dtor_input());
      _0_result = _out0;
      DecryptTestVector _source0 = (test).dtor_vector();
      if (_source0.is_PositiveDecryptKeyringTest()) {
        dafny.DafnySequence<? extends Character> _1___mcc_h0 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._name;
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2___mcc_h1 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._algorithmSuite;
        software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _3___mcc_h2 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._commitmentPolicy;
        dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _4___mcc_h3 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._encryptedDataKeys;
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _5___mcc_h4 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._encryptionContext;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _6___mcc_h5 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._keyDescription;
        DecryptResult _7___mcc_h6 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._expectedResult;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _8___mcc_h7 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._description;
        Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _9___mcc_h8 = ((TestVectors_Compile.DecryptTestVector_PositiveDecryptKeyringTest)_source0)._reproducedEncryptionContext;
        output = ((((_0_result).is_Success()) && (java.util.Objects.equals((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_plaintextDataKey(), (((test).dtor_vector()).dtor_expectedResult()).dtor_plaintextDataKey()))) && (java.util.Objects.equals((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_symmetricSigningKey(), (((test).dtor_vector()).dtor_expectedResult()).dtor_symmetricSigningKey()))) && ((((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_requiredEncryptionContextKeys()).asDafnyMultiset()).equals(((((test).dtor_vector()).dtor_expectedResult()).dtor_requiredEncryptionContextKeys()).asDafnyMultiset()));
      } else {
        dafny.DafnySequence<? extends Character> _10___mcc_h9 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._name;
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _11___mcc_h10 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._algorithmSuite;
        software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _12___mcc_h11 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._commitmentPolicy;
        dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _13___mcc_h12 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._encryptedDataKeys;
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _14___mcc_h13 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._encryptionContext;
        dafny.DafnySequence<? extends Character> _15___mcc_h14 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._errorDescription;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _16___mcc_h15 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._keyDescription;
        Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _17___mcc_h16 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._reproducedEncryptionContext;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _18___mcc_h17 = ((TestVectors_Compile.DecryptTestVector_NegativeDecryptKeyringTest)_source0)._description;
        output = !((_0_result).is_Success());
      }
      if (!(output)) {
        System.out.print((dafny.DafnySequence.asString("\nTEST===> ")).verbatimString());
        System.out.print((((test).dtor_vector()).dtor_name()).verbatimString());
        System.out.print(((((((test).dtor_vector()).dtor_description()).is_Some()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\n"), (((test).dtor_vector()).dtor_description()).dtor_value())) : (dafny.DafnySequence.asString("")))).verbatimString());
        System.out.print((((((test).dtor_vector()).is_NegativeDecryptKeyringTest()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("\n"), ((test).dtor_vector()).dtor_errorDescription())) : (dafny.DafnySequence.asString("\n")))).verbatimString());
        if (((test).dtor_vector()).is_PositiveDecryptKeyringTest()) {
          if ((_0_result).is_Failure()) {
            System.out.print((dafny.DafnySequence.asString("Error : ")).verbatimString());
            System.out.print(java.lang.String.valueOf((_0_result).dtor_error()));
            System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
          } else {
            if (!java.util.Objects.equals((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_plaintextDataKey(), (((test).dtor_vector()).dtor_expectedResult()).dtor_plaintextDataKey())) {
              System.out.print((dafny.DafnySequence.asString("Error : plaintextDataKey does not match.\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((test).dtor_vector()).dtor_expectedResult()).dtor_plaintextDataKey()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_plaintextDataKey()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
            }
            if (!java.util.Objects.equals((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_symmetricSigningKey(), (((test).dtor_vector()).dtor_expectedResult()).dtor_symmetricSigningKey())) {
              System.out.print((dafny.DafnySequence.asString("Error : symmetricSigningKey does not match.\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((test).dtor_vector()).dtor_expectedResult()).dtor_symmetricSigningKey()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_symmetricSigningKey()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
            }
            if (!(((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_requiredEncryptionContextKeys()).asDafnyMultiset()).equals(((((test).dtor_vector()).dtor_expectedResult()).dtor_requiredEncryptionContextKeys()).asDafnyMultiset())) {
              System.out.print((dafny.DafnySequence.asString("Error : requiredEncryptionContextKeys does not match.\n")).verbatimString());
              System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf(((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_requiredEncryptionContextKeys()).length())));
              System.out.print((dafny.DafnySequence.asString(" ")).verbatimString());
              System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf(((((test).dtor_vector()).dtor_expectedResult()).dtor_requiredEncryptionContextKeys()).length())));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((test).dtor_vector()).dtor_expectedResult()).dtor_requiredEncryptionContextKeys()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
              System.out.print(java.lang.String.valueOf((((_0_result).dtor_value()).dtor_decryptionMaterials()).dtor_requiredEncryptionContextKeys()));
              System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
            }
          }
        }
        System.out.print((dafny.DafnySequence.asString("\nFAILED! <-----------\n")).verbatimString());
      }
    }
    return output;
  }
  public static Wrappers_Compile.Result<EncryptTest, dafny.DafnySequence<? extends Character>> ToEncryptTest(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, EncryptTestVector vector)
  {
    Wrappers_Compile.Result<EncryptTest, dafny.DafnySequence<? extends Character>> output = (Wrappers_Compile.Result<EncryptTest, dafny.DafnySequence<? extends Character>>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput _0_input;
    EncryptTestVector _source0 = vector;
    if (_source0.is_PositiveEncryptKeyringVector()) {
      dafny.DafnySequence<? extends Character> _1___mcc_h0 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._name;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2___mcc_h1 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._description;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3___mcc_h2 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptionContext;
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _4___mcc_h3 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._commitmentPolicy;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _5___mcc_h4 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._algorithmSuite;
      Wrappers_Compile.Option<java.lang.Long> _6___mcc_h5 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._maxPlaintextLength;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _7___mcc_h6 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._requiredEncryptionContextKeys;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _8___mcc_h7 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _9___mcc_h8 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._decryptDescription;
      Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _10___mcc_h9 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._reproducedEncryptionContext;
      _0_input = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.create((vector).dtor_encryptionContext(), (vector).dtor_commitmentPolicy(), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId._typeDescriptor(), ((vector).dtor_algorithmSuite()).dtor_id()), (vector).dtor_maxPlaintextLength(), (vector).dtor_requiredEncryptionContextKeys());
    } else if (_source0.is_PositiveEncryptNegativeDecryptKeyringVector()) {
      dafny.DafnySequence<? extends Character> _11___mcc_h10 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._name;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _12___mcc_h11 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._description;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _13___mcc_h12 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptionContext;
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _14___mcc_h13 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._commitmentPolicy;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15___mcc_h14 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._algorithmSuite;
      Wrappers_Compile.Option<java.lang.Long> _16___mcc_h15 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._maxPlaintextLength;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _17___mcc_h16 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._requiredEncryptionContextKeys;
      dafny.DafnySequence<? extends Character> _18___mcc_h17 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptErrorDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _19___mcc_h18 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _20___mcc_h19 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptDescription;
      Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _21___mcc_h20 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._reproducedEncryptionContext;
      _0_input = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.create((vector).dtor_encryptionContext(), (vector).dtor_commitmentPolicy(), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId._typeDescriptor(), ((vector).dtor_algorithmSuite()).dtor_id()), (vector).dtor_maxPlaintextLength(), (vector).dtor_requiredEncryptionContextKeys());
    } else {
      dafny.DafnySequence<? extends Character> _22___mcc_h21 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._name;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _23___mcc_h22 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._description;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _24___mcc_h23 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._encryptionContext;
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _25___mcc_h24 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._commitmentPolicy;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _26___mcc_h25 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._algorithmSuite;
      Wrappers_Compile.Option<java.lang.Long> _27___mcc_h26 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._maxPlaintextLength;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _28___mcc_h27 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._requiredEncryptionContextKeys;
      dafny.DafnySequence<? extends Character> _29___mcc_h28 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._errorDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _30___mcc_h29 = ((TestVectors_Compile.EncryptTestVector_NegativeEncryptKeyringVector)_source0)._keyDescription;
      _0_input = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.create((vector).dtor_encryptionContext(), (vector).dtor_commitmentPolicy(), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId._typeDescriptor(), ((vector).dtor_algorithmSuite()).dtor_id()), (vector).dtor_maxPlaintextLength(), (vector).dtor_requiredEncryptionContextKeys());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _31_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.wrapped.__default.WrappedMaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.wrapped.__default.WrappedDefaultMaterialProvidersConfig());
    _31_valueOrError0 = _out0;
    if (!(!((_31_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(151,15): " + java.lang.String.valueOf(_31_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient _32_mpl;
    _32_mpl = (_31_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _33_cmm_k;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out1;
    _out1 = (keys).CreateWrappedTestVectorCmm(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput.create((((vector).is_PositiveEncryptKeyringVector()) ? ((vector).dtor_encryptDescription()) : ((((vector).is_PositiveEncryptNegativeDecryptKeyringVector()) ? ((vector).dtor_encryptDescription()) : ((vector).dtor_keyDescription())))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.CmmOperation.create_ENCRYPT()));
    _33_cmm_k = _out1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, dafny.DafnySequence<? extends Character>> _34_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, dafny.DafnySequence<? extends Character>>)null;
    _34_valueOrError1 = (_33_cmm_k).<dafny.DafnySequence<? extends Character>>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error, dafny.DafnySequence<? extends Character>>)(_35_e_boxed0) -> {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error _35_e = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error)(java.lang.Object)(_35_e_boxed0));
      return ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(dafny.Helpers.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Let(__default.printErr(_35_e), boxed14 -> {
        dafny.Tuple0 _pat_let7_0 = ((dafny.Tuple0)(java.lang.Object)(boxed14));
        return ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(dafny.Helpers.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Let(_pat_let7_0, boxed15 -> {
          dafny.Tuple0 _36___v78 = ((dafny.Tuple0)(java.lang.Object)(boxed15));
          return dafny.DafnySequence.asString("Cmm failure");
        }
        )));
      }
      )));
    }));
    if ((_34_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      output = (_34_valueOrError1).<EncryptTest>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), EncryptTest._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager _37_cmm;
    _37_cmm = (_34_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    output = Wrappers_Compile.Result.<EncryptTest, dafny.DafnySequence<? extends Character>>create_Success(EncryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), EncryptTest.create(_0_input, _37_cmm, vector));
    return output;
  }
  public static DecryptTestVector EncryptTestToDecryptVector(EncryptTest test, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials materials)
  {
    dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_keysToRemove = Seq_Compile.__default.<dafny.DafnySequence<? extends java.lang.Byte>>ToSet(UTF8.ValidUTF8Bytes._typeDescriptor(), (((test).dtor_vector()).dtor_requiredEncryptionContextKeys()).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())));
    EncryptTestVector _source0 = (test).dtor_vector();
    if (_source0.is_PositiveEncryptKeyringVector()) {
      dafny.DafnySequence<? extends Character> _1___mcc_h0 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._name;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2___mcc_h1 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._description;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3___mcc_h2 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptionContext;
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _4___mcc_h3 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._commitmentPolicy;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _5___mcc_h4 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._algorithmSuite;
      Wrappers_Compile.Option<java.lang.Long> _6___mcc_h5 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._maxPlaintextLength;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _7___mcc_h6 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._requiredEncryptionContextKeys;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _8___mcc_h7 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._encryptDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _9___mcc_h8 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._decryptDescription;
      Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _10___mcc_h9 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptKeyringVector)_source0)._reproducedEncryptionContext;
      return DecryptTestVector.create_PositiveDecryptKeyringTest(dafny.DafnySequence.<Character>concatenate(((test).dtor_vector()).dtor_name(), dafny.DafnySequence.asString("->Decryption")), ((test).dtor_vector()).dtor_algorithmSuite(), ((test).dtor_vector()).dtor_commitmentPolicy(), (materials).dtor_encryptedDataKeys(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>subtract((materials).dtor_encryptionContext(), _0_keysToRemove), ((test).dtor_vector()).dtor_decryptDescription(), DecryptResult.create((materials).dtor_plaintextDataKey(), (((((materials).dtor_symmetricSigningKeys()).is_Some()) && ((java.math.BigInteger.valueOf((((materials).dtor_symmetricSigningKeys()).dtor_value()).length())).signum() == 1)) ? (Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((((materials).dtor_symmetricSigningKeys()).dtor_value()).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) : (Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())))), (((test).dtor_vector()).dtor_requiredEncryptionContextKeys()).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()))), (((((test).dtor_vector()).dtor_description()).is_Some()) ? (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Decryption for "), (((test).dtor_vector()).dtor_description()).dtor_value()))) : (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))), ((test).dtor_vector()).dtor_reproducedEncryptionContext());
    } else {
      dafny.DafnySequence<? extends Character> _11___mcc_h10 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._name;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _12___mcc_h11 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._description;
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _13___mcc_h12 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptionContext;
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _14___mcc_h13 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._commitmentPolicy;
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _15___mcc_h14 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._algorithmSuite;
      Wrappers_Compile.Option<java.lang.Long> _16___mcc_h15 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._maxPlaintextLength;
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _17___mcc_h16 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._requiredEncryptionContextKeys;
      dafny.DafnySequence<? extends Character> _18___mcc_h17 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptErrorDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _19___mcc_h18 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._encryptDescription;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _20___mcc_h19 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._decryptDescription;
      Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _21___mcc_h20 = ((TestVectors_Compile.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector)_source0)._reproducedEncryptionContext;
      return DecryptTestVector.create_NegativeDecryptKeyringTest(dafny.DafnySequence.<Character>concatenate(((test).dtor_vector()).dtor_name(), dafny.DafnySequence.asString("->Decryption")), ((test).dtor_vector()).dtor_algorithmSuite(), ((test).dtor_vector()).dtor_commitmentPolicy(), (materials).dtor_encryptedDataKeys(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>subtract(((test).dtor_vector()).dtor_encryptionContext(), _0_keysToRemove), ((test).dtor_vector()).dtor_decryptErrorDescription(), ((test).dtor_vector()).dtor_decryptDescription(), ((test).dtor_vector()).dtor_reproducedEncryptionContext(), (((((test).dtor_vector()).dtor_description()).is_Some()) ? (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Decryption for "), (((test).dtor_vector()).dtor_description()).dtor_value()))) : (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)))));
    }
  }
  public static Wrappers_Compile.Result<DecryptTest, dafny.DafnySequence<? extends Character>> DecryptVectorToDecryptTest(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, DecryptTestVector vector)
  {
    Wrappers_Compile.Result<DecryptTest, dafny.DafnySequence<? extends Character>> output = (Wrappers_Compile.Result<DecryptTest, dafny.DafnySequence<? extends Character>>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput _0_input;
    _0_input = software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput.create(((vector).dtor_algorithmSuite()).dtor_id(), (vector).dtor_commitmentPolicy(), (vector).dtor_encryptedDataKeys(), (vector).dtor_encryptionContext(), (vector).dtor_reproducedEncryptionContext());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.wrapped.__default.WrappedMaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.wrapped.__default.WrappedDefaultMaterialProvidersConfig());
    _1_valueOrError0 = _out0;
    if (!(!((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestVectors.dfy(236,15): " + java.lang.String.valueOf(_1_valueOrError0));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient _2_mpl;
    _2_mpl = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _3_cmm_k;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out1;
    _out1 = (keys).CreateWrappedTestVectorCmm(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput.create((vector).dtor_keyDescription(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.CmmOperation.create_DECRYPT()));
    _3_cmm_k = _out1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, dafny.DafnySequence<? extends Character>> _4_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, dafny.DafnySequence<? extends Character>>)null;
    _4_valueOrError1 = (_3_cmm_k).<dafny.DafnySequence<? extends Character>>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default::ErrorToString);
    if ((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      output = (_4_valueOrError1).<DecryptTest>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), DecryptTest._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager _5_cmm;
    _5_cmm = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    output = Wrappers_Compile.Result.<DecryptTest, dafny.DafnySequence<? extends Character>>create_Success(DecryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), DecryptTest.create(_0_input, _5_cmm, vector));
    return output;
  }
  public static dafny.DafnySequence<? extends Character> ErrorToString(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error e) {
    software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error _source0 = e;
    if (_source0.is_KeyVectorException()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException)_source0)._message;
      dafny.DafnySequence<? extends Character> _1_message = _0___mcc_h0;
      return _1_message;
    } else if (_source0.is_AwsCryptographyMaterialProviders()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.Error _2___mcc_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders)_source0)._AwsCryptographyMaterialProviders;
      software.amazon.cryptography.materialproviders.internaldafny.types.Error _3_mplError = _2___mcc_h2;
      software.amazon.cryptography.materialproviders.internaldafny.types.Error _source1 = _3_mplError;
      if (_source1.is_AwsCryptographicMaterialProvidersException()) {
        dafny.DafnySequence<? extends Character> _4___mcc_h16 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException)_source1)._message;
        dafny.DafnySequence<? extends Character> _5_message = _4___mcc_h16;
        return _5_message;
      } else if (_source1.is_EntryAlreadyExists()) {
        dafny.DafnySequence<? extends Character> _6___mcc_h18 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryAlreadyExists)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_EntryDoesNotExist()) {
        dafny.DafnySequence<? extends Character> _7___mcc_h20 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InFlightTTLExceeded()) {
        dafny.DafnySequence<? extends Character> _8___mcc_h22 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InFlightTTLExceeded)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidAlgorithmSuiteInfo()) {
        dafny.DafnySequence<? extends Character> _9___mcc_h24 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfo)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidAlgorithmSuiteInfoOnDecrypt()) {
        dafny.DafnySequence<? extends Character> _10___mcc_h26 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnDecrypt)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidAlgorithmSuiteInfoOnEncrypt()) {
        dafny.DafnySequence<? extends Character> _11___mcc_h28 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnEncrypt)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidDecryptionMaterials()) {
        dafny.DafnySequence<? extends Character> _12___mcc_h30 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterials)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidDecryptionMaterialsTransition()) {
        dafny.DafnySequence<? extends Character> _13___mcc_h32 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterialsTransition)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidEncryptionMaterials()) {
        dafny.DafnySequence<? extends Character> _14___mcc_h34 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterials)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_InvalidEncryptionMaterialsTransition()) {
        dafny.DafnySequence<? extends Character> _15___mcc_h36 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterialsTransition)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_AwsCryptographyKeyStore()) {
        software.amazon.cryptography.keystore.internaldafny.types.Error _16___mcc_h38 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyKeyStore)_source1)._AwsCryptographyKeyStore;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_AwsCryptographyPrimitives()) {
        software.amazon.cryptography.primitives.internaldafny.types.Error _17___mcc_h40 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives)_source1)._AwsCryptographyPrimitives;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_ComAmazonawsDynamodb()) {
        software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _18___mcc_h42 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsDynamodb)_source1)._ComAmazonawsDynamodb;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_ComAmazonawsKms()) {
        software.amazon.cryptography.services.kms.internaldafny.types.Error _19___mcc_h44 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsKms)_source1)._ComAmazonawsKms;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_CollectionOfErrors()) {
        dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20___mcc_h46 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors)_source1)._list;
        dafny.DafnySequence<? extends Character> _21___mcc_h47 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors)_source1)._message;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else if (_source1.is_Opaque()) {
        Object _22___mcc_h50 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_Opaque)_source1)._obj;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      } else {
        Object _23___mcc_h52 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_OpaqueWithText)_source1)._obj;
        dafny.DafnySequence<? extends Character> _24___mcc_h53 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error_OpaqueWithText)_source1)._objMessage;
        return dafny.DafnySequence.asString("Unmapped AwsCryptographyMaterialProviders");
      }
    } else if (_source0.is_ComAmazonawsKms()) {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _25___mcc_h4 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_ComAmazonawsKms)_source0)._ComAmazonawsKms;
      return dafny.DafnySequence.asString("Unmapped KeyVectorException");
    } else if (_source0.is_CollectionOfErrors()) {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _26___mcc_h6 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_CollectionOfErrors)_source0)._list;
      dafny.DafnySequence<? extends Character> _27___mcc_h7 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_CollectionOfErrors)_source0)._message;
      return dafny.DafnySequence.asString("Unmapped KeyVectorException");
    } else if (_source0.is_Opaque()) {
      Object _28___mcc_h10 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_Opaque)_source0)._obj;
      return dafny.DafnySequence.asString("Unmapped KeyVectorException");
    } else {
      Object _29___mcc_h12 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_OpaqueWithText)_source0)._obj;
      dafny.DafnySequence<? extends Character> _30___mcc_h13 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_OpaqueWithText)_source0)._objMessage;
      return dafny.DafnySequence.asString("Unmapped KeyVectorException");
    }
  }
  public static dafny.Tuple0 printErr(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error e)
  {
    dafny.Tuple0 _hresult = dafny.Tuple0.Default();
    System.out.print(java.lang.String.valueOf(e));
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
    System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
    _hresult = dafny.Tuple0.create();
    return _hresult;
  }
  @Override
  public java.lang.String toString() {
    return "TestVectors._default";
  }
}
