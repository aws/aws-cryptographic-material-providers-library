// Class __default
// Dafny class __default compiled into Java
package MultiKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean Verified_q(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring keyring) {
    return (((((((((((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed16 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_8 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed16));
      return _is_8 instanceof RawAESKeyring_Compile.RawAESKeyring;
    }
    )))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed17 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_9 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed17));
      return _is_9 instanceof RawECDHKeyring_Compile.RawEcdhKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed18 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_10 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed18));
      return _is_10 instanceof RawRSAKeyring_Compile.RawRSAKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed19 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_11 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed19));
      return _is_11 instanceof AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed20 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_12 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed20));
      return _is_12 instanceof AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed21 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_13 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed21));
      return _is_13 instanceof AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed22 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_14 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed22));
      return _is_14 instanceof AwsKmsKeyring_Compile.AwsKmsKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed23 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_15 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed23));
      return _is_15 instanceof AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed24 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_16 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed24));
      return _is_16 instanceof AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring;
    }
    ))))) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed25 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_17 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed25));
      return _is_17 instanceof AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring;
    }
    ))));
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> AttemptDecryptDataKey(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring keyring, software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (keyring).OnDecrypt(input);
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _1_output;
    _1_output = (_0_valueOrError0).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((__default.Verified_q(keyring)) || (((boolean)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, Boolean>Let(keyring, boxed26 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _is_18 = ((software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring)(java.lang.Object)(boxed26));
      return _is_18 instanceof MultiKeyring;
    }
    )))))) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsTransitionIsValid((input).dtor_materials(), (_1_output).dtor_materials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring performed invalid material transition")));
      if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _1_output);
    return res;
  }
  @Override
  public java.lang.String toString() {
    return "MultiKeyring._default";
  }
}
