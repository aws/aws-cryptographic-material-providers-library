// Class __default
// Dafny class __default compiled into Java
package KeyringFromKeyDescription_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> GetKeyId(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription input) {
    TAIL_CALL_START: while (true) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _source0 = input;
      if (_source0.is_Kms()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _0___mcc_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Kms)_source0)._Kms;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _1_i = _0___mcc_h0;
        return (_1_i).dtor_keyId();
      } else if (_source0.is_KmsMrk()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _2___mcc_h1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrk)_source0)._KmsMrk;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _3_i = _2___mcc_h1;
        return (_3_i).dtor_keyId();
      } else if (_source0.is_KmsMrkDiscovery()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _4___mcc_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrkDiscovery)_source0)._KmsMrkDiscovery;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _5_i = _4___mcc_h2;
        return (_5_i).dtor_keyId();
      } else if (_source0.is_RSA()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _6___mcc_h3 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA)_source0)._RSA;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _7_i = _6___mcc_h3;
        return (_7_i).dtor_keyId();
      } else if (_source0.is_AES()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _8___mcc_h4 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_AES)_source0)._AES;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _9_i = _8___mcc_h4;
        return (_9_i).dtor_keyId();
      } else if (_source0.is_ECDH()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _10___mcc_h5 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_ECDH)_source0)._ECDH;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _11_i = _10___mcc_h5;
        return (_11_i).dtor_senderKeyId();
      } else if (_source0.is_Static()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _12___mcc_h6 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Static)_source0)._Static;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _13_i = _12___mcc_h6;
        return (_13_i).dtor_keyId();
      } else if (_source0.is_KmsRsa()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _14___mcc_h7 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsRsa)_source0)._KmsRsa;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _15_i = _14___mcc_h7;
        return (_15_i).dtor_keyId();
      } else if (_source0.is_KmsECDH()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _16___mcc_h8 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsECDH)_source0)._KmsECDH;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _17_i = _16___mcc_h8;
        return (_17_i).dtor_senderKeyId();
      } else if (_source0.is_Hierarchy()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _18___mcc_h9 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Hierarchy)_source0)._Hierarchy;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _19_i = _18___mcc_h9;
        return (_19_i).dtor_keyId();
      } else if (_source0.is_Multi()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring _20___mcc_h10 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Multi)_source0)._Multi;
        return dafny.DafnySequence.asString("");
      } else {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM _21___mcc_h11 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RequiredEncryptionContext)_source0)._RequiredEncryptionContext;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM _22_i = _21___mcc_h11;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _in0 = (_22_i).dtor_underlying();
        input = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetSenderKeyId(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription input) {
    software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _source0 = input;
    if (_source0.is_Kms()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _0___mcc_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Kms)_source0)._Kms;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsMrk()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _1___mcc_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrk)_source0)._KmsMrk;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsMrkDiscovery()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _2___mcc_h4 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrkDiscovery)_source0)._KmsMrkDiscovery;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_RSA()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _3___mcc_h6 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA)_source0)._RSA;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_AES()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _4___mcc_h8 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_AES)_source0)._AES;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_ECDH()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _5___mcc_h10 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_ECDH)_source0)._ECDH;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _6_i = _5___mcc_h10;
      return (_6_i).dtor_senderKeyId();
    } else if (_source0.is_Static()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _7___mcc_h12 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Static)_source0)._Static;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsRsa()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _8___mcc_h14 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsRsa)_source0)._KmsRsa;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsECDH()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _9___mcc_h16 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsECDH)_source0)._KmsECDH;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_Hierarchy()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _10___mcc_h18 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Hierarchy)_source0)._Hierarchy;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_Multi()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring _11___mcc_h20 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Multi)_source0)._Multi;
      return dafny.DafnySequence.asString("");
    } else {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM _12___mcc_h22 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RequiredEncryptionContext)_source0)._RequiredEncryptionContext;
      return dafny.DafnySequence.asString("");
    }
  }
  public static dafny.DafnySequence<? extends Character> GetRecipientKeyId(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription input) {
    software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _source0 = input;
    if (_source0.is_Kms()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _0___mcc_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Kms)_source0)._Kms;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsMrk()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _1___mcc_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrk)_source0)._KmsMrk;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsMrkDiscovery()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _2___mcc_h4 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrkDiscovery)_source0)._KmsMrkDiscovery;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_RSA()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _3___mcc_h6 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA)_source0)._RSA;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_AES()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _4___mcc_h8 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_AES)_source0)._AES;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_ECDH()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _5___mcc_h10 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_ECDH)_source0)._ECDH;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _6_i = _5___mcc_h10;
      return (_6_i).dtor_recipientKeyId();
    } else if (_source0.is_Static()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _7___mcc_h12 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Static)_source0)._Static;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsRsa()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _8___mcc_h14 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsRsa)_source0)._KmsRsa;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_KmsECDH()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _9___mcc_h16 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsECDH)_source0)._KmsECDH;
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _10_i = _9___mcc_h16;
      return (_10_i).dtor_recipientKeyId();
    } else if (_source0.is_Hierarchy()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _11___mcc_h18 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Hierarchy)_source0)._Hierarchy;
      return dafny.DafnySequence.asString("");
    } else if (_source0.is_Multi()) {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring _12___mcc_h20 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Multi)_source0)._Multi;
      return dafny.DafnySequence.asString("");
    } else {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM _13___mcc_h22 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RequiredEncryptionContext)_source0)._RequiredEncryptionContext;
      return dafny.DafnySequence.asString("");
    }
  }
  public static Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> GetKeyMaterial(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription)
  {
    dafny.DafnySequence<? extends Character> _0_keyId = __default.GetKeyId(keyDescription);
    if ((keys).<dafny.DafnySequence<? extends Character>>contains(_0_keyId)) {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_Some(KeyMaterial_Compile.KeyMaterial._typeDescriptor(), ((KeyMaterial_Compile.KeyMaterial)(java.lang.Object)((keys).get(_0_keyId))));
    } else {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_None(KeyMaterial_Compile.KeyMaterial._typeDescriptor());
    }
  }
  public static Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> GetSenderKeyMaterial(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription)
  {
    dafny.DafnySequence<? extends Character> _0_keyId = __default.GetSenderKeyId(keyDescription);
    if ((keys).<dafny.DafnySequence<? extends Character>>contains(_0_keyId)) {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_Some(KeyMaterial_Compile.KeyMaterial._typeDescriptor(), ((KeyMaterial_Compile.KeyMaterial)(java.lang.Object)((keys).get(_0_keyId))));
    } else {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_None(KeyMaterial_Compile.KeyMaterial._typeDescriptor());
    }
  }
  public static Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> GetRecipientKeyMaterial(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription keyDescription)
  {
    dafny.DafnySequence<? extends Character> _0_keyId = __default.GetRecipientKeyId(keyDescription);
    if ((keys).<dafny.DafnySequence<? extends Character>>contains(_0_keyId)) {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_Some(KeyMaterial_Compile.KeyMaterial._typeDescriptor(), ((KeyMaterial_Compile.KeyMaterial)(java.lang.Object)((keys).get(_0_keyId))));
    } else {
      return Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>create_None(KeyMaterial_Compile.KeyMaterial._typeDescriptor());
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> ToKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> keys, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription description)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _0_material;
      _0_material = __default.GetKeyMaterial(keys, description);
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _source0 = description;
      if (_source0.is_Kms()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _1___mcc_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Kms)_source0)._Kms;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo _source1 = _1___mcc_h0;
        dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo)_source1)._keyId;
        dafny.DafnySequence<? extends Character> _3_key = _2___mcc_h1;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _4_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_KMS()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: KMS")));
          if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_4_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _5_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out0;
          _out0 = __default.getKmsClient(mpl, ((_0_material).dtor_value()).dtor_keyIdentifier());
          _5_valueOrError2 = _out0;
          if ((_5_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_5_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _6_kmsClient;
          _6_kmsClient = (_5_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput _7_input;
          _7_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput.create(((_0_material).dtor_value()).dtor_keyIdentifier(), _6_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
          _out1 = (mpl).CreateAwsKmsKeyring(_7_input);
          _8_keyring = _out1;
          output = (_8_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_9_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _9_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_9_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_9_e);
          }));
          return output;
        }
      } else if (_source0.is_KmsMrk()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _10___mcc_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrk)_source0)._KmsMrk;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware _source2 = _10___mcc_h2;
        dafny.DafnySequence<? extends Character> _11___mcc_h3 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware)_source2)._keyId;
        dafny.DafnySequence<? extends Character> _12_key = _11___mcc_h3;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _13_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _13_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_KMS()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: KMS")));
          if ((_13_valueOrError3).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_13_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _14_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out2;
          _out2 = __default.getKmsClient(mpl, ((_0_material).dtor_value()).dtor_keyIdentifier());
          _14_valueOrError4 = _out2;
          if ((_14_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_14_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _15_kmsClient;
          _15_kmsClient = (_14_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput _16_input;
          _16_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput.create(((_0_material).dtor_value()).dtor_keyIdentifier(), _15_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
          _out3 = (mpl).CreateAwsKmsMrkKeyring(_16_input);
          _17_keyring = _out3;
          output = (_17_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_18_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _18_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_18_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_18_e);
          }));
          return output;
        }
      } else if (_source0.is_KmsMrkDiscovery()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _19___mcc_h4 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsMrkDiscovery)_source0)._KmsMrkDiscovery;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery _source3 = _19___mcc_h4;
        dafny.DafnySequence<? extends Character> _20___mcc_h5 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery)_source3)._keyId;
        dafny.DafnySequence<? extends Character> _21___mcc_h6 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery)_source3)._defaultMrkRegion;
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _22___mcc_h7 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery)_source3)._awsKmsDiscoveryFilter;
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _23_awsKmsDiscoveryFilter = _22___mcc_h7;
        dafny.DafnySequence<? extends Character> _24_defaultMrkRegion = _21___mcc_h6;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _25_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _25_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), (_0_material).is_None(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Discovery has not key")));
          if ((_25_valueOrError8).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_25_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput _26_input;
          _26_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput.create(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _24_defaultMrkRegion), _23_awsKmsDiscoveryFilter, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
          _out4 = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(_26_input);
          _27_keyring = _out4;
          output = (_27_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_28_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _28_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_28_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_28_e);
          }));
          return output;
        }
      } else if (_source0.is_RSA()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _29___mcc_h8 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_RSA)_source0)._RSA;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _source4 = _29___mcc_h8;
        dafny.DafnySequence<? extends Character> _30___mcc_h9 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)_source4)._keyId;
        dafny.DafnySequence<? extends Character> _31___mcc_h10 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)_source4)._providerId;
        software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _32___mcc_h11 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)_source4)._padding;
        software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _33_padding = _32___mcc_h11;
        dafny.DafnySequence<? extends Character> _34_providerId = _31___mcc_h10;
        dafny.DafnySequence<? extends Character> _35_key = _30___mcc_h9;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _36_valueOrError11 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _36_valueOrError11 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && ((((_0_material).dtor_value()).is_PrivateRSA()) || (((_0_material).dtor_value()).is_PublicRSA())), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: PrivateRSA or PublicRSA")));
          if ((_36_valueOrError11).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_36_valueOrError11).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _source5 = _0_material;
          KeyMaterial_Compile.KeyMaterial _37___mcc_h39 = ((Wrappers_Compile.Option_Some<KeyMaterial_Compile.KeyMaterial>)_source5)._value;
          KeyMaterial_Compile.KeyMaterial _source6 = _37___mcc_h39;
          if (_source6.is_PrivateRSA()) {
            dafny.DafnySequence<? extends Character> _38___mcc_h48 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._name;
            boolean _39___mcc_h49 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._encrypt;
            boolean _40___mcc_h50 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._decrypt;
            dafny.DafnySequence<? extends Character> _41___mcc_h51 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._algorithm;
            java.math.BigInteger _42___mcc_h52 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._bits;
            dafny.DafnySequence<? extends Character> _43___mcc_h53 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._encoding;
            dafny.DafnySequence<? extends Character> _44___mcc_h54 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._material;
            dafny.DafnySequence<? extends Character> _45___mcc_h55 = ((KeyMaterial_Compile.KeyMaterial_PrivateRSA)_source6)._keyIdentifier;
            dafny.DafnySequence<? extends Character> _46_keyIdentifier = _45___mcc_h55;
            dafny.DafnySequence<? extends Character> _47_material = _44___mcc_h54;
            boolean _48_decrypt = _40___mcc_h50;
            {
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _49_valueOrError12 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _49_valueOrError12 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), _48_decrypt, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Private RSA keys only supports decrypt.")));
              if ((_49_valueOrError12).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_49_valueOrError12).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _50_valueOrError13 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _50_valueOrError13 = (UTF8.__default.Encode(_47_material)).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_51_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _51_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_51_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_51_e);
              }));
              if ((_50_valueOrError13).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_50_valueOrError13).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _52_privateKeyPemBytes;
              _52_privateKeyPemBytes = (_50_valueOrError13).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput _53_input;
              _53_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_34_providerId, _46_keyIdentifier, _33_padding, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), _52_privateKeyPemBytes));
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _54_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
              _out5 = (mpl).CreateRawRsaKeyring(_53_input);
              _54_keyring = _out5;
              output = (_54_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_55_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _55_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_55_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_55_e);
              }));
              return output;
            }
          } else {
            dafny.DafnySequence<? extends Character> _56___mcc_h56 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._name;
            boolean _57___mcc_h57 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._encrypt;
            boolean _58___mcc_h58 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._decrypt;
            java.math.BigInteger _59___mcc_h59 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._bits;
            dafny.DafnySequence<? extends Character> _60___mcc_h60 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._algorithm;
            dafny.DafnySequence<? extends Character> _61___mcc_h61 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._encoding;
            dafny.DafnySequence<? extends Character> _62___mcc_h62 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._material;
            dafny.DafnySequence<? extends Character> _63___mcc_h63 = ((KeyMaterial_Compile.KeyMaterial_PublicRSA)_source6)._keyIdentifier;
            dafny.DafnySequence<? extends Character> _64_keyIdentifier = _63___mcc_h63;
            dafny.DafnySequence<? extends Character> _65_material = _62___mcc_h62;
            boolean _66_encrypt = _57___mcc_h57;
            {
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _67_valueOrError14 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _67_valueOrError14 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), _66_encrypt, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Public RSA keys only supports encrypt.")));
              if ((_67_valueOrError14).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_67_valueOrError14).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _68_valueOrError15 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _68_valueOrError15 = (UTF8.__default.Encode(_65_material)).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_69_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _69_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_69_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_69_e);
              }));
              if ((_68_valueOrError15).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_68_valueOrError15).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _70_publicKeyPemBytes;
              _70_publicKeyPemBytes = (_68_valueOrError15).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput _71_input;
              _71_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput.create(_34_providerId, _64_keyIdentifier, _33_padding, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(UTF8.ValidUTF8Bytes._typeDescriptor(), _70_publicKeyPemBytes), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _72_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
              _out6 = (mpl).CreateRawRsaKeyring(_71_input);
              _72_keyring = _out6;
              output = (_72_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_73_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _73_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_73_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_73_e);
              }));
              return output;
            }
          }
        }
      } else if (_source0.is_AES()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _74___mcc_h12 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_AES)_source0)._AES;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES _source7 = _74___mcc_h12;
        dafny.DafnySequence<? extends Character> _75___mcc_h13 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES)_source7)._keyId;
        dafny.DafnySequence<? extends Character> _76___mcc_h14 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES)_source7)._providerId;
        dafny.DafnySequence<? extends Character> _77_providerId = _76___mcc_h14;
        dafny.DafnySequence<? extends Character> _78_key = _75___mcc_h13;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _79_valueOrError9 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _79_valueOrError9 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_Symetric()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: Symmetric")));
          if ((_79_valueOrError9).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_79_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _80_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.Default());
          if (java.util.Objects.equals(((_0_material).dtor_value()).dtor_bits(), java.math.BigInteger.valueOf(128L))) {
            _80_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES128__GCM__IV12__TAG16());
          } else if (java.util.Objects.equals(((_0_material).dtor_value()).dtor_bits(), java.math.BigInteger.valueOf(192L))) {
            _80_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES192__GCM__IV12__TAG16());
          } else if (java.util.Objects.equals(((_0_material).dtor_value()).dtor_bits(), java.math.BigInteger.valueOf(256L))) {
            _80_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16());
          } else {
            _80_valueOrError10 = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not a supported bit length")));
          }
          if ((_80_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_80_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg _81_wrappingAlg;
          _81_wrappingAlg = (_80_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput _82_input;
          _82_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput.create(_77_providerId, ((_0_material).dtor_value()).dtor_keyIdentifier(), ((_0_material).dtor_value()).dtor_wrappingKey(), _81_wrappingAlg);
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _83_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
          _out7 = (mpl).CreateRawAesKeyring(_82_input);
          _83_keyring = _out7;
          output = (_83_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_84_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _84_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_84_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_84_e);
          }));
          return output;
        }
      } else if (_source0.is_ECDH()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _85___mcc_h15 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_ECDH)_source0)._ECDH;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh _source8 = _85___mcc_h15;
        dafny.DafnySequence<? extends Character> _86___mcc_h16 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._senderKeyId;
        dafny.DafnySequence<? extends Character> _87___mcc_h17 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._recipientKeyId;
        dafny.DafnySequence<? extends Character> _88___mcc_h18 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._senderPublicKey;
        dafny.DafnySequence<? extends Character> _89___mcc_h19 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._recipientPublicKey;
        dafny.DafnySequence<? extends Character> _90___mcc_h20 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._providerId;
        dafny.DafnySequence<? extends Character> _91___mcc_h21 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._curveSpec;
        dafny.DafnySequence<? extends Character> _92___mcc_h22 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)_source8)._keyAgreementScheme;
        dafny.DafnySequence<? extends Character> _93_keyAgreementScheme = _92___mcc_h22;
        dafny.DafnySequence<? extends Character> _94_curveSpec = _91___mcc_h21;
        dafny.DafnySequence<? extends Character> _95_providerId = _90___mcc_h20;
        dafny.DafnySequence<? extends Character> _96_recipientPublicKey = _89___mcc_h19;
        dafny.DafnySequence<? extends Character> _97_senderPublicKey = _88___mcc_h18;
        dafny.DafnySequence<? extends Character> _98_recipientKeyId = _87___mcc_h17;
        dafny.DafnySequence<? extends Character> _99_senderKeyId = _86___mcc_h16;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _100_valueOrError16 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _100_valueOrError16 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), (KeyDescription_Compile.__default.Curve2EccAlgorithmSpec()).<dafny.DafnySequence<? extends Character>>contains(_94_curveSpec), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Unknown curve spec")));
          if ((_100_valueOrError16).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_100_valueOrError16).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _101_curveType;
          _101_curveType = ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((KeyDescription_Compile.__default.Curve2EccAlgorithmSpec()).get(_94_curveSpec)));
          Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _102_primitives_q;
          Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> _out8;
          _out8 = software.amazon.cryptography.primitives.internaldafny.__default.AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.__default.DefaultCryptoConfig());
          _102_primitives_q = _out8;
          Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _103_valueOrError17 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
          _103_valueOrError17 = (_102_primitives_q).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_104_e_boxed0) -> {
            software.amazon.cryptography.primitives.internaldafny.types.Error _104_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_104_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Unable to create primitives client"));
          }));
          if ((_103_valueOrError17).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_103_valueOrError17).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _105_primitives;
          _105_primitives = (_103_valueOrError17).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          if (java.util.Objects.equals(_93_keyAgreementScheme, dafny.DafnySequence.asString("static"))) {
            {
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _106_valueOrError18 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _106_valueOrError18 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_PrivateECDH()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: PrivateECDH")));
              if ((_106_valueOrError18).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_106_valueOrError18).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _107_valueOrError19 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _107_valueOrError19 = (UTF8.__default.Encode(((_0_material).dtor_value()).dtor_senderMaterial())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_108_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _108_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_108_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_108_e);
              }));
              if ((_107_valueOrError19).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_107_valueOrError19).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _109_senderMaterial;
              _109_senderMaterial = (_107_valueOrError19).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _110_valueOrError20 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _110_valueOrError20 = (UTF8.__default.Encode(((_0_material).dtor_value()).dtor_recipientMaterial())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_111_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _111_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_111_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_111_e);
              }));
              if ((_110_valueOrError20).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_110_valueOrError20).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _112_recipientMaterial;
              _112_recipientMaterial = (_110_valueOrError20).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _113_valueOrError21 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
              _113_valueOrError21 = (Base64_Compile.__default.Decode(((_0_material).dtor_value()).dtor_recipientPublicKey())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_114_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _114_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_114_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_114_e);
              }));
              if ((_113_valueOrError21).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_113_valueOrError21).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _115_recipientPublicKey;
              _115_recipientPublicKey = (_113_valueOrError21).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _116_schema;
              _116_schema = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_RawPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput.create(_109_senderMaterial, _115_recipientPublicKey));
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput _117_input;
              _117_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(_116_schema, _101_curveType);
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _118_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
              _out9 = (mpl).CreateRawEcdhKeyring(_117_input);
              _118_keyring = _out9;
              output = (_118_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_119_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _119_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_119_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_119_e);
              }));
              return output;
            }
          } else if (java.util.Objects.equals(_93_keyAgreementScheme, dafny.DafnySequence.asString("ephemeral"))) {
            {
              Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _120_recipientMaterial_q;
              _120_recipientMaterial_q = __default.GetRecipientKeyMaterial(keys, description);
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _121_valueOrError22 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _121_valueOrError22 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_120_recipientMaterial_q).is_Some()) && (((_120_recipientMaterial_q).dtor_value()).is_PrivateECDH()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: PrivateECDH")));
              if ((_121_valueOrError22).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_121_valueOrError22).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _122_valueOrError23 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _122_valueOrError23 = (UTF8.__default.Encode(((_120_recipientMaterial_q).dtor_value()).dtor_recipientMaterial())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_123_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _123_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_123_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_123_e);
              }));
              if ((_122_valueOrError23).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_122_valueOrError23).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _124_recipientMaterial;
              _124_recipientMaterial = (_122_valueOrError23).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _125_valueOrError24 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
              _125_valueOrError24 = (Base64_Compile.__default.Decode(((_120_recipientMaterial_q).dtor_value()).dtor_recipientPublicKey())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_126_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _126_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_126_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_126_e);
              }));
              if ((_125_valueOrError24).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_125_valueOrError24).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _127_recipientPublicKey;
              _127_recipientPublicKey = (_125_valueOrError24).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _128_schema;
              _128_schema = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_EphemeralPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput.create(_127_recipientPublicKey));
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput _129_input;
              _129_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(_128_schema, _101_curveType);
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _130_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
              _out10 = (mpl).CreateRawEcdhKeyring(_129_input);
              _130_keyring = _out10;
              output = (_130_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_131_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _131_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_131_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_131_e);
              }));
              return output;
            }
          } else if (java.util.Objects.equals(_93_keyAgreementScheme, dafny.DafnySequence.asString("discovery"))) {
            {
              Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _132_recipientMaterial_q;
              _132_recipientMaterial_q = __default.GetRecipientKeyMaterial(keys, description);
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _133_valueOrError25 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _133_valueOrError25 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_132_recipientMaterial_q).is_Some()) && (((_132_recipientMaterial_q).dtor_value()).is_PrivateECDH()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: PrivateECDH")));
              if ((_133_valueOrError25).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_133_valueOrError25).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _134_valueOrError26 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
              _134_valueOrError26 = (UTF8.__default.Encode(((_132_recipientMaterial_q).dtor_value()).dtor_recipientMaterial())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_135_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _135_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_135_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_135_e);
              }));
              if ((_134_valueOrError26).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_134_valueOrError26).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _136_recipientMaterial;
              _136_recipientMaterial = (_134_valueOrError26).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _137_schema;
              _137_schema = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_PublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput.create(_136_recipientMaterial));
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput _138_input;
              _138_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(_137_schema, _101_curveType);
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _139_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
              _out11 = (mpl).CreateRawEcdhKeyring(_138_input);
              _139_keyring = _out11;
              output = (_139_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_140_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _140_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_140_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_140_e);
              }));
              return output;
            }
          } else {
            {
              output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("key agreement schema not recognized")));
              return output;
            }
          }
        }
      } else if (_source0.is_Static()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _141___mcc_h23 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Static)_source0)._Static;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring _source9 = _141___mcc_h23;
        dafny.DafnySequence<? extends Character> _142___mcc_h24 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring)_source9)._keyId;
        dafny.DafnySequence<? extends Character> _143_key = _142___mcc_h24;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _144_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _144_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_StaticMaterial()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: StaticMaterial")));
          if ((_144_valueOrError0).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_144_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _145_encrypt;
          _145_encrypt = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials.create(((_0_material).dtor_value()).dtor_algorithmSuite(), ((_0_material).dtor_value()).dtor_encryptionContext(), ((_0_material).dtor_value()).dtor_encryptedDataKeys(), ((_0_material).dtor_value()).dtor_requiredEncryptionContextKeys(), ((_0_material).dtor_value()).dtor_plaintextDataKey(), ((_0_material).dtor_value()).dtor_signingKey(), ((_0_material).dtor_value()).dtor_symmetricSigningKeys());
          software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _146_decrypt;
          _146_decrypt = software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.create(((_0_material).dtor_value()).dtor_algorithmSuite(), ((_0_material).dtor_value()).dtor_encryptionContext(), ((_0_material).dtor_value()).dtor_requiredEncryptionContextKeys(), ((_0_material).dtor_value()).dtor_plaintextDataKey(), ((_0_material).dtor_value()).dtor_verificationKey(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
          software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _147_keyring;
          software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _out12;
          _out12 = CreateStaticKeyrings_Compile.__default.CreateStaticMaterialsKeyring(_145_encrypt, _146_decrypt);
          _147_keyring = _out12;
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), _147_keyring);
          return output;
        }
      } else if (_source0.is_KmsRsa()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _148___mcc_h25 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsRsa)_source0)._KmsRsa;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring _source10 = _148___mcc_h25;
        dafny.DafnySequence<? extends Character> _149___mcc_h26 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring)_source10)._keyId;
        software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _150___mcc_h27 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring)_source10)._encryptionAlgorithm;
        software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _151_encryptionAlgorithm = _150___mcc_h27;
        dafny.DafnySequence<? extends Character> _152_key = _149___mcc_h26;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _153_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _153_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_KMSAsymetric()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: KMSAsymetric")));
          if ((_153_valueOrError5).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_153_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _154_valueOrError6 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
          Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out13;
          _out13 = __default.getKmsClient(mpl, ((_0_material).dtor_value()).dtor_keyIdentifier());
          _154_valueOrError6 = _out13;
          if ((_154_valueOrError6).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_154_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _155_kmsClient;
          _155_kmsClient = (_154_valueOrError6).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput _156_input;
          _156_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_0_material).dtor_value()).dtor_publicKey()), ((_0_material).dtor_value()).dtor_keyIdentifier(), _151_encryptionAlgorithm, Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), _155_kmsClient), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _157_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out14;
          _out14 = (mpl).CreateAwsKmsRsaKeyring(_156_input);
          _157_keyring = _out14;
          output = (_157_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_158_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _158_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_158_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_158_e);
          }));
          return output;
        }
      } else if (_source0.is_KmsECDH()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _159___mcc_h28 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_KmsECDH)_source0)._KmsECDH;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring _source11 = _159___mcc_h28;
        dafny.DafnySequence<? extends Character> _160___mcc_h29 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._senderKeyId;
        dafny.DafnySequence<? extends Character> _161___mcc_h30 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._recipientKeyId;
        dafny.DafnySequence<? extends Character> _162___mcc_h31 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._senderPublicKey;
        dafny.DafnySequence<? extends Character> _163___mcc_h32 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._recipientPublicKey;
        dafny.DafnySequence<? extends Character> _164___mcc_h33 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._curveSpec;
        dafny.DafnySequence<? extends Character> _165___mcc_h34 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)_source11)._keyAgreementScheme;
        dafny.DafnySequence<? extends Character> _166_keyAgreementScheme = _165___mcc_h34;
        dafny.DafnySequence<? extends Character> _167_curveSpec = _164___mcc_h33;
        dafny.DafnySequence<? extends Character> _168_recipientPublicKey = _163___mcc_h32;
        dafny.DafnySequence<? extends Character> _169_senderPublicKey = _162___mcc_h31;
        dafny.DafnySequence<? extends Character> _170_recipientKeyId = _161___mcc_h30;
        dafny.DafnySequence<? extends Character> _171_senderKeyId = _160___mcc_h29;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _172_valueOrError27 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _172_valueOrError27 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), (KeyDescription_Compile.__default.KmsKey2EccAlgorithmSpec()).<dafny.DafnySequence<? extends Character>>contains(_167_curveSpec), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Unknown curve spec")));
          if ((_172_valueOrError27).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_172_valueOrError27).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _173_curveType;
          _173_curveType = ((software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec)(java.lang.Object)((KeyDescription_Compile.__default.KmsKey2EccAlgorithmSpec()).get(_167_curveSpec)));
          if (java.util.Objects.equals(_166_keyAgreementScheme, dafny.DafnySequence.asString("static"))) {
            {
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _174_valueOrError28 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _174_valueOrError28 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_KMSEcdh()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: KmsEcdh")));
              if ((_174_valueOrError28).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_174_valueOrError28).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends Character> _175_senderKmsKey;
              _175_senderKmsKey = ((_0_material).dtor_value()).dtor_senderMaterial();
              dafny.DafnySequence<? extends Character> _176_recipientKmsKey;
              _176_recipientKmsKey = ((_0_material).dtor_value()).dtor_recipientMaterial();
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _177_valueOrError29 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _177_valueOrError29 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(_175_senderKmsKey)) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(_176_recipientKmsKey)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not a valid Kms Key Id")));
              if ((_177_valueOrError29).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_177_valueOrError29).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _178_valueOrError30 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
              Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out15;
              _out15 = __default.getKmsClient(mpl, _175_senderKmsKey);
              _178_valueOrError30 = _out15;
              if ((_178_valueOrError30).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_178_valueOrError30).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _179_kmsClient;
              _179_kmsClient = (_178_valueOrError30).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _180_valueOrError31 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
              _180_valueOrError31 = (Base64_Compile.__default.Decode(((_0_material).dtor_value()).dtor_senderPublicKey())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_181_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _181_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_181_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_181_e);
              }));
              if ((_180_valueOrError31).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_180_valueOrError31).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _182_senderPublicKey;
              _182_senderPublicKey = (_180_valueOrError31).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _183_valueOrError32 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
              _183_valueOrError32 = (Base64_Compile.__default.Decode(((_0_material).dtor_value()).dtor_recipientPublicKey())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_184_e_boxed0) -> {
                dafny.DafnySequence<? extends Character> _184_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_184_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_184_e);
              }));
              if ((_183_valueOrError32).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_183_valueOrError32).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends java.lang.Byte> _185_recipientPublicKey;
              _185_recipientPublicKey = (_183_valueOrError32).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _186_schema;
              _186_schema = software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput.create(_175_senderKmsKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _182_senderPublicKey), _185_recipientPublicKey));
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput _187_input;
              _187_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(_186_schema, _173_curveType, _179_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _188_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out16;
              _out16 = (mpl).CreateAwsKmsEcdhKeyring(_187_input);
              _188_keyring = _out16;
              output = (_188_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_189_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _189_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_189_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_189_e);
              }));
              return output;
            }
          } else if (java.util.Objects.equals(_166_keyAgreementScheme, dafny.DafnySequence.asString("discovery"))) {
            {
              Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _190_recipientMaterial_q;
              _190_recipientMaterial_q = __default.GetRecipientKeyMaterial(keys, description);
              Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _191_valueOrError33 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              _191_valueOrError33 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_190_recipientMaterial_q).is_Some()) && (((_190_recipientMaterial_q).dtor_value()).is_KMSEcdh()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: KmsEcdh")));
              if ((_191_valueOrError33).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_191_valueOrError33).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              dafny.DafnySequence<? extends Character> _192_recipientKmsKey;
              _192_recipientKmsKey = ((_190_recipientMaterial_q).dtor_value()).dtor_recipientMaterial();
              Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _193_valueOrError34 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
              Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out17;
              _out17 = __default.getKmsClient(mpl, _192_recipientKmsKey);
              _193_valueOrError34 = _out17;
              if ((_193_valueOrError34).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
                output = (_193_valueOrError34).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
                return output;
              }
              software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _194_kmsClient;
              _194_kmsClient = (_193_valueOrError34).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
              software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _195_schema;
              _195_schema = software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput.create(_192_recipientKmsKey));
              software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput _196_input;
              _196_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput.create(_195_schema, _173_curveType, _194_kmsClient, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _197_keyring;
              Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out18;
              _out18 = (mpl).CreateAwsKmsEcdhKeyring(_196_input);
              _197_keyring = _out18;
              output = (_197_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_198_e_boxed0) -> {
                software.amazon.cryptography.materialproviders.internaldafny.types.Error _198_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_198_e_boxed0));
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_198_e);
              }));
              return output;
            }
          } else {
            {
              output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("key agreement schema not recognized")));
              return output;
            }
          }
        }
      } else if (_source0.is_Hierarchy()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _199___mcc_h35 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Hierarchy)_source0)._Hierarchy;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring _source12 = _199___mcc_h35;
        dafny.DafnySequence<? extends Character> _200___mcc_h36 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring)_source12)._keyId;
        dafny.DafnySequence<? extends Character> _201_key = _200___mcc_h36;
        {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _202_valueOrError7 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
          _202_valueOrError7 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_0_material).is_Some()) && (((_0_material).dtor_value()).is_StaticKeyStoreInformation()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Not type: StaticKeyStoreInformation")));
          if ((_202_valueOrError7).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
            output = (_202_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient _203_keyStore;
          software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient _out19;
          _out19 = CreateStaticKeyStores_Compile.__default.CreateStaticKeyStore((_0_material).dtor_value());
          _203_keyStore = _out19;
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput _204_input;
          _204_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((_0_material).dtor_value()).dtor_keyIdentifier()), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier.class))), _203_keyStore, (long) 11L, Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.CacheType>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _205_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out20;
          _out20 = (mpl).CreateAwsKmsHierarchicalKeyring(_204_input);
          _205_keyring = _out20;
          output = (_205_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_206_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _206_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_206_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_206_e);
          }));
          return output;
        }
      } else {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring _207___mcc_h37 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription_Multi)_source0)._Multi;
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring _208_MultiKeyring = _207___mcc_h37;
        {
          Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> _209_generator;
          _209_generator = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          if (((_208_MultiKeyring).dtor_generator()).is_Some()) {
            Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _210_valueOrError35 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
            _210_valueOrError35 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), KeyDescription_Compile.__default.Keyring_q(((_208_MultiKeyring).dtor_generator()).dtor_value()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Only Keyring key descriptions are supported.")));
            if ((_210_valueOrError35).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
              output = (_210_valueOrError35).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
              return output;
            }
            Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _211_valueOrError36 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
            Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out21;
            _out21 = __default.ToKeyring(mpl, keys, ((_208_MultiKeyring).dtor_generator()).dtor_value());
            _211_valueOrError36 = _out21;
            if ((_211_valueOrError36).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
              output = (_211_valueOrError36).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
              return output;
            }
            software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _212_generator_k;
            _212_generator_k = (_211_valueOrError36).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
            _209_generator = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>create_Some(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), _212_generator_k);
          }
          dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> _213_childKeyrings;
          _213_childKeyrings = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> empty(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          java.math.BigInteger _hi0 = java.math.BigInteger.valueOf(((_208_MultiKeyring).dtor_childKeyrings()).length());
          for (java.math.BigInteger _214_i = java.math.BigInteger.ZERO; _214_i.compareTo(_hi0) < 0; _214_i = _214_i.add(java.math.BigInteger.ONE)) {
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _215_child;
            _215_child = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(((_208_MultiKeyring).dtor_childKeyrings()).select(dafny.Helpers.toInt((_214_i)))));
            Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _216_valueOrError37 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
            _216_valueOrError37 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), KeyDescription_Compile.__default.Keyring_q(_215_child), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Only Keyring key descriptions are supported.")));
            if ((_216_valueOrError37).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
              output = (_216_valueOrError37).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
              return output;
            }
            Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _217_valueOrError38 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
            Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out22;
            _out22 = __default.ToKeyring(mpl, keys, _215_child);
            _217_valueOrError38 = _out22;
            if ((_217_valueOrError38).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
              output = (_217_valueOrError38).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
              return output;
            }
            software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _218_childKeyring;
            _218_childKeyring = (_217_valueOrError38).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
            _213_childKeyrings = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>concatenate(_213_childKeyrings, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> of(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), _218_childKeyring));
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput _219_input;
          _219_input = software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput.create(_209_generator, _213_childKeyrings);
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _220_keyring;
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out23;
          _out23 = (mpl).CreateMultiKeyring(_219_input);
          _220_keyring = _out23;
          output = (_220_keyring).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_221_e_boxed0) -> {
            software.amazon.cryptography.materialproviders.internaldafny.types.Error _221_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_221_e_boxed0));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_221_e);
          }));
          return output;
        }
      }
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> getKmsClient(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends Character> maybeKmsArn)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_maybeClientSupplier;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (mpl).CreateDefaultClientSupplier(software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
      _0_maybeClientSupplier = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _1_valueOrError0 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
      _1_valueOrError0 = (_0_maybeClientSupplier).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _2_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
        output = (_1_valueOrError0).<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)));
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _3_clientSupplier;
      _3_clientSupplier = (_1_valueOrError0).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>> _4_arn;
      _4_arn = AwsArnParsing_Compile.__default.IsAwsKmsIdentifierString(maybeKmsArn);
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _5_region;
      if ((_4_arn).is_Success()) {
        _5_region = AwsArnParsing_Compile.__default.GetRegion((_4_arn).dtor_value());
      } else {
        _5_region = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      }
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_tmp;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = (_3_clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create((_5_region).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString(""))));
      _6_tmp = _out1;
      output = (_6_tmp).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_7_e_boxed0) -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _7_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_7_e_boxed0));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_7_e);
      }));
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> GetEcdhPublicKey(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> awsKmsKey)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> res = (Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest _0_getPublicKeyRequest;
    _0_getPublicKeyRequest = software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(awsKmsKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor()));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _1_maybePublicKeyResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = (client).GetPublicKey(_0_getPublicKeyRequest);
    _1_maybePublicKeyResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse.Default());
    _2_valueOrError0 = (_1_maybePublicKeyResponse).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_3_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _3_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_ComAmazonawsKms(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse _4_getPublicKeyResponse;
    _4_getPublicKeyResponse = (_2_valueOrError0).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
    _5_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((((((_4_getPublicKeyResponse).dtor_KeyId()).is_Some()) && ((((_4_getPublicKeyResponse).dtor_KeyId()).dtor_value()).equals(awsKmsKey))) && (((_4_getPublicKeyResponse).dtor_KeyUsage()).is_Some())) && (java.util.Objects.equals(((_4_getPublicKeyResponse).dtor_KeyUsage()).dtor_value(), software.amazon.cryptography.services.kms.internaldafny.types.KeyUsageType.create_KEY__AGREEMENT()))) && (((_4_getPublicKeyResponse).dtor_PublicKey()).is_Some()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(dafny.DafnySequence.asString("Invalid response from KMS GetPublicKey")));
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor());
      return res;
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((_4_getPublicKeyResponse).dtor_PublicKey()).dtor_value());
    return res;
  }
  @Override
  public java.lang.String toString() {
    return "KeyringFromKeyDescription._default";
  }
}
