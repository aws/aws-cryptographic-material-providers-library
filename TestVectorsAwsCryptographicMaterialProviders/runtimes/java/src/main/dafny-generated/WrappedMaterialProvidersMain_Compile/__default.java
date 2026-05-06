// Class __default
// Dafny class __default compiled into Java
package WrappedMaterialProvidersMain_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void Main(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args)
  {
    GetOpt_Compile.Options _0_vectorOptions;
    _0_vectorOptions = GetOpt_Compile.Options.create(dafny.DafnySequence.asString("test-vectors"), dafny.DafnySequence.asString("?"), dafny.DafnySequence.<GetOpt_Compile.Param> of(GetOpt_Compile.Param._typeDescriptor(), GetOpt_Compile.Param.create_Command(GetOpt_Compile.Options.create(dafny.DafnySequence.asString("decrypt"), dafny.DafnySequence.asString("decrypt command for test-vectors"), dafny.DafnySequence.<GetOpt_Compile.Param> of(GetOpt_Compile.Param._typeDescriptor(), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("manifest-path"), dafny.DafnySequence.asString("relative path to the location of the manifest"), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_Required(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No()), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("test-name"), dafny.DafnySequence.asString("id of the test to run"), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_UnusedOk(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No())))), GetOpt_Compile.Param.create_Command(GetOpt_Compile.Options.create(dafny.DafnySequence.asString("encrypt"), dafny.DafnySequence.asString("encrypt command for test-vectors"), dafny.DafnySequence.<GetOpt_Compile.Param> of(GetOpt_Compile.Param._typeDescriptor(), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("manifest-path"), dafny.DafnySequence.asString("relative path to the location of the manifest"), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_Required(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No()), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("decrypt-manifest-path"), dafny.DafnySequence.asString("relative path to the location where the decrypted manifest will be written to."), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_Required(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No()), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("test-name"), dafny.DafnySequence.asString("id of the test to run"), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_UnusedOk(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No())))), GetOpt_Compile.Param.create_Command(GetOpt_Compile.Options.create(dafny.DafnySequence.asString("encrypt-manifest"), dafny.DafnySequence.asString("encryp manifest command for test-vectors"), dafny.DafnySequence.<GetOpt_Compile.Param> of(GetOpt_Compile.Param._typeDescriptor(), GetOpt_Compile.Param.create_Opt(dafny.DafnySequence.asString("encrypt-manifest-output"), dafny.DafnySequence.asString("relative path of where to store the encrypt-manifest produced"), dafny.DafnySequence.asString("arg"), GetOpt_Compile.__default.NullChar(), GetOpt_Compile.Unused.create_Required(), false, GetOpt_Compile.Visibility.create_Normal(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), GetOpt_Compile.Tri.create_No()))))));
    if (!((java.math.BigInteger.valueOf((args).length())).signum() == 1)) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(38,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<GetOpt_Compile.Parsed, dafny.DafnySequence<? extends Character>> _1_parsedOptions_q;
    _1_parsedOptions_q = GetOpt_Compile.__default.GetOptions(_0_vectorOptions, args);
    if ((_1_parsedOptions_q).is_Success()) {
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2_h;
      _2_h = GetOpt_Compile.__default.NeedsHelp(_0_vectorOptions, (_1_parsedOptions_q).dtor_value(), dafny.DafnySequence.asString(""));
      if ((_2_h).is_Some()) {
        System.out.print(((_2_h).dtor_value()).verbatimString());
        return;
      }
      Wrappers_Compile.Result<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>> _3_op_q;
      _3_op_q = __default.ParseCommandLineOptions((_1_parsedOptions_q).dtor_value());
      if ((_3_op_q).is_Success()) {
        MplManifestOptions_Compile.ManifestOptions _4_op;
        _4_op = (_3_op_q).dtor_value();
        MplManifestOptions_Compile.ManifestOptions _source0 = _4_op;
        if (_source0.is_Decrypt()) {
          dafny.DafnySequence<? extends Character> _5___mcc_h0 = ((MplManifestOptions_Compile.ManifestOptions_Decrypt)_source0)._manifestPath;
          Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _6___mcc_h1 = ((MplManifestOptions_Compile.ManifestOptions_Decrypt)_source0)._testName;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _7_result;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out0;
          _out0 = TestManifests_Compile.__default.StartDecrypt(_4_op);
          _7_result = _out0;
          if ((_7_result).is_Failure()) {
            System.out.print(((_7_result).dtor_error()).verbatimString());
          }
          if (!((_7_result).is_Success())) {
            throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(57,10): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
          }
        } else if (_source0.is_Encrypt()) {
          dafny.DafnySequence<? extends Character> _8___mcc_h2 = ((MplManifestOptions_Compile.ManifestOptions_Encrypt)_source0)._manifestPath;
          dafny.DafnySequence<? extends Character> _9___mcc_h3 = ((MplManifestOptions_Compile.ManifestOptions_Encrypt)_source0)._decryptManifestOutput;
          Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _10___mcc_h4 = ((MplManifestOptions_Compile.ManifestOptions_Encrypt)_source0)._testName;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _11_result;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out1;
          _out1 = TestManifests_Compile.__default.StartEncrypt(_4_op);
          _11_result = _out1;
          if ((_11_result).is_Failure()) {
            System.out.print(((_11_result).dtor_error()).verbatimString());
          }
          if (!((_11_result).is_Success())) {
            throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(63,10): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
          }
        } else {
          dafny.DafnySequence<? extends Character> _12___mcc_h5 = ((MplManifestOptions_Compile.ManifestOptions_EncryptManifest)_source0)._encryptManifestOutput;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _13_result;
          Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out2;
          _out2 = CompleteVectors_Compile.__default.WriteStuff(_4_op);
          _13_result = _out2;
          if ((_13_result).is_Failure()) {
            System.out.print(((_13_result).dtor_error()).verbatimString());
          }
          if (!((_13_result).is_Success())) {
            throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/Index.dfy(69,10): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
          }
        }
      } else {
        System.out.print((dafny.DafnySequence.<Character>concatenate((_3_op_q).dtor_error(), dafny.DafnySequence.asString("\n"))).verbatimString());
        System.out.print((dafny.DafnySequence.asString("help\n")).verbatimString());
      }
    } else {
      System.out.print((dafny.DafnySequence.<Character>concatenate((_1_parsedOptions_q).dtor_error(), dafny.DafnySequence.asString("\n"))).verbatimString());
    }
  }
  public static void __Main(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args) {
    __default.Main(args);
  }
  public static Wrappers_Compile.Result<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>> ParseCommandLineOptions(GetOpt_Compile.Parsed parsedOptions) {
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((parsedOptions).dtor_subcommand()).is_Some(), dafny.DafnySequence.asString("Must supply subcommand\n"));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<MplManifestOptions_Compile.ManifestOptions>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions._typeDescriptor());
    } else {
      if (java.util.Objects.equals((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_command(), dafny.DafnySequence.asString("decrypt"))) {
        return __default.ParseDecryptCmd((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_params());
      } else if (java.util.Objects.equals((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_command(), dafny.DafnySequence.asString("encrypt"))) {
        return __default.ParseEncryptCmd((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_params());
      } else if (java.util.Objects.equals((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_command(), dafny.DafnySequence.asString("encrypt-manifest"))) {
        return __default.ParseEncryptManifestCmd((((parsedOptions).dtor_subcommand()).dtor_value()).dtor_params());
      } else {
        return Wrappers_Compile.Result.<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>>create_Failure(MplManifestOptions_Compile.ManifestOptions._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Received unknown subcommand"));
      }
    }
  }
  public static Wrappers_Compile.Result<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>> ParseDecryptCmd(dafny.DafnySequence<? extends GetOpt_Compile.OneArg> params) {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _0_manifestPath_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("manifest-path"));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _1_testName_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("test-name"));
    dafny.DafnySequence<? extends Character> _2_manifestPath = (((_0_manifestPath_q).is_Some()) ? ((_0_manifestPath_q).dtor_value()) : (dafny.DafnySequence.asString(".")));
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (java.math.BigInteger.valueOf((_2_manifestPath).length())).signum() == 1, dafny.DafnySequence.asString("Invalid manifest path length\n"));
    if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_3_valueOrError0).<MplManifestOptions_Compile.ManifestOptions>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>>create_Success(MplManifestOptions_Compile.ManifestOptions._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions.create_Decrypt((((Seq_Compile.__default.<Character>Last(dafny.TypeDescriptor.CHAR, _2_manifestPath)) == ('/')) ? (_2_manifestPath) : (dafny.DafnySequence.<Character>concatenate(_2_manifestPath, dafny.DafnySequence.asString("/")))), (((_1_testName_q).is_Some()) ? (_1_testName_q) : (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))));
    }
  }
  public static Wrappers_Compile.Result<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>> ParseEncryptCmd(dafny.DafnySequence<? extends GetOpt_Compile.OneArg> params) {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _0_manifestPath_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("manifest-path"));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _1_decryptManifestPath_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("decrypt-manifest-path"));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _2_testName_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("test-name"));
    dafny.DafnySequence<? extends Character> _3_manifestPath = (((_0_manifestPath_q).is_Some()) ? ((_0_manifestPath_q).dtor_value()) : (dafny.DafnySequence.asString(".")));
    dafny.DafnySequence<? extends Character> _4_decryptManifestPath = (((_1_decryptManifestPath_q).is_Some()) ? ((_1_decryptManifestPath_q).dtor_value()) : (dafny.DafnySequence.asString(".")));
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.math.BigInteger.valueOf((_3_manifestPath).length())).signum() == 1) && ((java.math.BigInteger.valueOf((_4_decryptManifestPath).length())).signum() == 1), dafny.DafnySequence.asString("Invalid manifest or decrypt manifest path length\n"));
    if ((_5_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_5_valueOrError0).<MplManifestOptions_Compile.ManifestOptions>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>>create_Success(MplManifestOptions_Compile.ManifestOptions._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions.create_Encrypt((((Seq_Compile.__default.<Character>Last(dafny.TypeDescriptor.CHAR, _3_manifestPath)) == ('/')) ? (_3_manifestPath) : (dafny.DafnySequence.<Character>concatenate(_3_manifestPath, dafny.DafnySequence.asString("/")))), (((Seq_Compile.__default.<Character>Last(dafny.TypeDescriptor.CHAR, _4_decryptManifestPath)) == ('/')) ? (_4_decryptManifestPath) : (dafny.DafnySequence.<Character>concatenate(_4_decryptManifestPath, dafny.DafnySequence.asString("/")))), (((_2_testName_q).is_Some()) ? (_2_testName_q) : (Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))));
    }
  }
  public static Wrappers_Compile.Result<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>> ParseEncryptManifestCmd(dafny.DafnySequence<? extends GetOpt_Compile.OneArg> params) {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _0_encryptManifestOutput_q = GetOpt_Compile.__default.OptValue(params, dafny.DafnySequence.asString("encrypt-manifest-output"));
    dafny.DafnySequence<? extends Character> _1_encryptManifestOutput = (((_0_encryptManifestOutput_q).is_Some()) ? ((_0_encryptManifestOutput_q).dtor_value()) : (dafny.DafnySequence.asString(".")));
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (java.math.BigInteger.valueOf((_1_encryptManifestOutput).length())).signum() == 1, dafny.DafnySequence.asString("Invalid encrypt manifest output length"));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_2_valueOrError0).<MplManifestOptions_Compile.ManifestOptions>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<MplManifestOptions_Compile.ManifestOptions, dafny.DafnySequence<? extends Character>>create_Success(MplManifestOptions_Compile.ManifestOptions._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), MplManifestOptions_Compile.ManifestOptions.create_EncryptManifest((((Seq_Compile.__default.<Character>Last(dafny.TypeDescriptor.CHAR, _1_encryptManifestOutput)) == ('/')) ? (_1_encryptManifestOutput) : (dafny.DafnySequence.<Character>concatenate(_1_encryptManifestOutput, dafny.DafnySequence.asString("/"))))));
    }
  }
  public static boolean DecryptSingleOptions_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> op) {
    return (((java.util.Objects.equals(java.math.BigInteger.valueOf(3L), java.math.BigInteger.valueOf((op).size()))) && ((op).<dafny.DafnySequence<? extends Character>>contains(dafny.DafnySequence.asString("-keys-path")))) && ((op).<dafny.DafnySequence<? extends Character>>contains(dafny.DafnySequence.asString("-key-description")))) && ((op).<dafny.DafnySequence<? extends Character>>contains(dafny.DafnySequence.asString("-base64-bytes")));
  }
  @Override
  public java.lang.String toString() {
    return "WrappedMaterialProvidersMain._default";
  }
}
