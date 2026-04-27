// Class _ExternBase___default
// Dafny class __default compiled into Java
package TestWrappedMaterialProvidersMain_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static void RunManifestTests()
  {
    __default.TestGenerateEncryptManifest();
    __default.TestEncryptManifest();
    __default.TestDecryptManifest();
  }
  public static void TestGenerateEncryptManifest()
  {
    dafny.DafnySequence<? extends Character> _0_directory;
    dafny.DafnySequence<? extends Character> _out0;
    _out0 = __default.GetTestVectorExecutionDirectory();
    _0_directory = _out0;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _1_result;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = CompleteVectors_Compile.__default.WriteStuff(MplManifestOptions_Compile.ManifestOptions.create_EncryptManifest(dafny.DafnySequence.<Character>concatenate(_0_directory, dafny.DafnySequence.asString("dafny/TestVectorsAwsCryptographicMaterialProviders/test/"))));
    _1_result = _out1;
    if ((_1_result).is_Failure()) {
      System.out.print(((_1_result).dtor_error()).verbatimString());
    }
    if (!((_1_result).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(37,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestEncryptManifest()
  {
    dafny.DafnySequence<? extends Character> _0_directory;
    dafny.DafnySequence<? extends Character> _out0;
    _out0 = __default.GetTestVectorExecutionDirectory();
    _0_directory = _out0;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _1_result;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = TestManifests_Compile.__default.StartEncrypt(MplManifestOptions_Compile.ManifestOptions.create_Encrypt(dafny.DafnySequence.<Character>concatenate(_0_directory, dafny.DafnySequence.asString("dafny/TestVectorsAwsCryptographicMaterialProviders/test/")), dafny.DafnySequence.<Character>concatenate(_0_directory, dafny.DafnySequence.asString("dafny/TestVectorsAwsCryptographicMaterialProviders/")), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _1_result = _out1;
    if ((_1_result).is_Failure()) {
      System.out.print(((_1_result).dtor_error()).verbatimString());
    }
    if (!((_1_result).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(51,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void TestDecryptManifest()
  {
    dafny.DafnySequence<? extends Character> _0_directory;
    dafny.DafnySequence<? extends Character> _out0;
    _out0 = __default.GetTestVectorExecutionDirectory();
    _0_directory = _out0;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _1_result;
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out1;
    _out1 = TestManifests_Compile.__default.StartDecrypt(MplManifestOptions_Compile.ManifestOptions.create_Decrypt(dafny.DafnySequence.<Character>concatenate(_0_directory, dafny.DafnySequence.asString("dafny/TestVectorsAwsCryptographicMaterialProviders/")), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    _1_result = _out1;
    if ((_1_result).is_Failure()) {
      System.out.print(java.lang.String.valueOf(_1_result));
    }
    if (!((_1_result).is_Success())) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(64,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestWrappedMaterialProvidersMain._default";
  }
}
