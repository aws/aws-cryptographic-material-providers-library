// Class __default
// Dafny class __default compiled into Java
package TestUtils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> GenerateInvalidEncryptionContext()
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encCtx = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty();
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _0_valueOrError0 = UTF8.__default.Encode(dafny.DafnySequence.asString("a"));
      if (!(!((_0_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(115,46): " + java.lang.String.valueOf(_0_valueOrError0));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _1_validUTF8char;
      _1_validUTF8char = (_0_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      dafny.DafnySequence<? extends java.lang.Byte> _2_key;
      _2_key = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
      while ((java.math.BigInteger.valueOf((_2_key).length())).compareTo(StandardLibrary_mUInt_Compile.__default.UINT16__LIMIT()) < 0) {
        _2_key = dafny.DafnySequence.<java.lang.Byte>concatenate(_2_key, _1_validUTF8char);
      }
      encCtx = dafny.DafnyMap.fromElements(new dafny.Tuple2(_2_key, dafny.DafnySequence.<java.lang.Byte> of((byte) 0)));
    }
    return encCtx;
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> GenerateLargeValidEncryptionContext()
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> r = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty();
    java.math.BigInteger _0_numMaxPairs = java.math.BigInteger.ZERO;
    _0_numMaxPairs = java.math.BigInteger.valueOf(9361L);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _1_valueOrError0 = UTF8.__default.Encode(dafny.DafnySequence.asString("a"));
    if (!(!((_1_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(135,15): " + java.lang.String.valueOf(_1_valueOrError0));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _2_val;
    _2_val = (_1_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encCtx;
    _3_encCtx = dafny.DafnyMap.fromElements();
    java.math.BigInteger _4_i = java.math.BigInteger.ZERO;
    _4_i = java.math.BigInteger.ZERO;
    while (((java.math.BigInteger.valueOf((_3_encCtx).size())).compareTo(_0_numMaxPairs) < 0) && ((_4_i).compareTo(java.math.BigInteger.valueOf(65536L)) < 0)) {
      dafny.DafnySequence<? extends java.lang.Byte> _5_key;
      _5_key = StandardLibrary_mUInt_Compile.__default.UInt16ToSeq((_4_i).shortValue());
      if (UTF8.__default.ValidUTF8Seq(_5_key)) {
        _3_encCtx = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>update(_3_encCtx, _5_key, _2_val);
      }
      _4_i = (_4_i).add(java.math.BigInteger.ONE);
    }
    r = _3_encCtx;
    return r;
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> SmallEncryptionContext(SmallEncryptionContextVariation v)
  {
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext = dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty();
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _0_valueOrError0 = UTF8.__default.Encode(dafny.DafnySequence.asString("keyA"));
      if (!(!((_0_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(163,16): " + java.lang.String.valueOf(_0_valueOrError0));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _1_keyA;
      _1_keyA = (_0_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _2_valueOrError1 = UTF8.__default.Encode(dafny.DafnySequence.asString("valA"));
      if (!(!((_2_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(164,16): " + java.lang.String.valueOf(_2_valueOrError1));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _3_valA;
      _3_valA = (_2_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _4_valueOrError2 = UTF8.__default.Encode(dafny.DafnySequence.asString("keyB"));
      if (!(!((_4_valueOrError2).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(165,16): " + java.lang.String.valueOf(_4_valueOrError2));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _5_keyB;
      _5_keyB = (_4_valueOrError2).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
      _6_valueOrError3 = UTF8.__default.Encode(dafny.DafnySequence.asString("valB"));
      if (!(!((_6_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(166,16): " + java.lang.String.valueOf(_6_valueOrError3));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _7_valB;
      _7_valB = (_6_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      SmallEncryptionContextVariation _source0 = v;
      if (_source0.is_Empty()) {
        encryptionContext = dafny.DafnyMap.fromElements();
      } else if (_source0.is_A()) {
        encryptionContext = dafny.DafnyMap.fromElements(new dafny.Tuple2(_1_keyA, _3_valA));
      } else if (_source0.is_AB()) {
        encryptionContext = dafny.DafnyMap.fromElements(new dafny.Tuple2(_1_keyA, _3_valA), new dafny.Tuple2(_5_keyB, _7_valB));
      } else {
        encryptionContext = dafny.DafnyMap.fromElements(new dafny.Tuple2(_5_keyB, _7_valB), new dafny.Tuple2(_1_keyA, _3_valA));
      }
    }
    return encryptionContext;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey GenerateMockEncryptedDataKey(dafny.DafnySequence<? extends Character> keyProviderId, dafny.DafnySequence<? extends Character> keyProviderInfo)
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.Default();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _0_valueOrError0 = UTF8.__default.Encode(keyProviderId);
    if (!(!((_0_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(186,32): " + java.lang.String.valueOf(_0_valueOrError0));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_encodedkeyProviderId;
    _1_encodedkeyProviderId = (_0_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _2_valueOrError1 = UTF8.__default.Encode(keyProviderInfo);
    if (!(!((_2_valueOrError1).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(187,34): " + java.lang.String.valueOf(_2_valueOrError1));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_encodedKeyProviderInfo;
    _3_encodedKeyProviderInfo = (_2_valueOrError1).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue());
    _4_valueOrError2 = UTF8.__default.Encode(dafny.DafnySequence.asString("fakeCiphertext"));
    if (!(!((_4_valueOrError2).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/TestUtils.dfy(188,26): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    dafny.DafnySequence<? extends java.lang.Byte> _5_fakeCiphertext;
    _5_fakeCiphertext = (_4_valueOrError2).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(_1_encodedkeyProviderId, _3_encodedKeyProviderInfo, _5_fakeCiphertext);
    return edk;
  }
  public static dafny.Tuple2 NamespaceAndName(java.math.BigInteger n)
  {
    dafny.DafnySequence<? extends Character> namespace = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    dafny.DafnySequence<? extends Character> name = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    if(true) {
      dafny.DafnySequence<? extends Character> _0_s;
      _0_s = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("child"), dafny.DafnySequence.<Character> of((char) (((char)dafny.Helpers.toInt((n))) + ('0'))));
      namespace = dafny.DafnySequence.<Character>concatenate(_0_s, dafny.DafnySequence.asString(" Namespace"));
      name = dafny.DafnySequence.<Character>concatenate(_0_s, dafny.DafnySequence.asString(" Name"));
    }
    return new dafny.Tuple2<>(namespace, name);
  }
  public static dafny.DafnySequence<? extends Character> KMS__RSA__PUBLIC__KEY()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PUBLIC KEY-----\n"), dafny.DafnySequence.asString("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27Uc/fBaMVhxCE/SpCMQ\n")), dafny.DafnySequence.asString("oSBRSzQJw+o2hBaA+FiPGtiJ/aPy7sn18aCkelaSj4kwoC79b/arNHlkjc7OJFsN\n")), dafny.DafnySequence.asString("/GoFKgNvaiY4lOeJqEiWQGSSgHtsJLdbO2u4OOSxh8qIRAMKbMgQDVX4FR/PLKeK\n")), dafny.DafnySequence.asString("fc2aCDvcNSpAM++8NlNmv7+xQBJydr5ce91eISbHkFRkK3/bAM+1iddupoRw4Wo2\n")), dafny.DafnySequence.asString("r3avzrg5xBHmzR7u1FTab22Op3Hgb2dBLZH43wNKAceVwKqKA8UNAxashFON7xK9\n")), dafny.DafnySequence.asString("yy4kfOL0Z/nhxRKe4jRZ/5v508qIzgzCksYy7Y3QbMejAtiYnr7s5/d5KWw0swou\n")), dafny.DafnySequence.asString("twIDAQAB\n")), dafny.DafnySequence.asString("-----END PUBLIC KEY-----"));
  }
  public static dafny.DafnySequence<? extends Character> KMS__RSA__PRIVATE__KEY__ARN()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297");
  }
  public static dafny.DafnySequence<? extends Character> SHARED__TEST__KEY__ARN()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f");
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> ACCOUNT__IDS()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("658956600833"));
  }
  public static dafny.DafnySequence<? extends Character> PARTITION()
  {
    return dafny.DafnySequence.asString("aws");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__256__KEY__ARN__S()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__256__KEY__ARN__R()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__384__KEY__ARN__S()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__384__KEY__ARN__R()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/29f0bef9-1677-4e74-b67e-acefab1295ff");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__521__KEY__ARN__S()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/41b502e3-cc9d-442f-bd7b-d67faed0f22e");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__521__KEY__ARN__R()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/c45f1043-53bb-4f37-adc5-4d25d4a84f9d");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__256__PUBLIC__KEY__S()
  {
    return dafny.DafnySequence.asString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE18m54QsLUnhWU7gT8hkAceNbZ/WBGNUUSPCeIKqOyX5psiqyC1TXPOJXqKKaVv5Mg91WV9UjpboblOhNU35nRw==");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__256__PUBLIC__KEY__R()
  {
    return dafny.DafnySequence.asString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9istdPCuX9nF8EmA4tioe/k0TCa2M9VeBW1N9n0sxPA6uPVOfLtE4+KuYxAGT0dYoK6CY93nowUy1yS+R7A+wA==");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__384__PUBLIC__KEY__S()
  {
    return dafny.DafnySequence.asString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEfQ0OHFvwskFVjQwfqV7jpo62I6uyGY+5SPRZb6CuJ96bVreLZXh485BcPv09O/DWnpTBm8LL+YcfsqM3ECvi2ee3bDGpH6xIdr28uvyG75t5wqBjYYtZQFDf/ydfG9mm");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__384__PUBLIC__KEY__R()
  {
    return dafny.DafnySequence.asString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEWgGNWQ+vEwlMxyMQkSsOAYGfT6IlgEkcanEOSjbeEpEnh8JHEiBHQ6QaROxJ7c3nEkbjbi0m+7ejBEGtkiqaY5Dsv5u1iV4fc/2v1RzPba1ZtudEmM16Eyy9LHswdJ7v");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__521__PUBLIC__KEY__S()
  {
    return dafny.DafnySequence.asString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAz86qnfp3s0cl+73PQhlUstfdg9EZDA/jtLjBTWYp/1EB7RHNm8q5hMg5kBfjRDUFhbRBMlUV1xBOTgqzoSWj4oAABnQKiXXGGyu6PMN4D9nVMDsOpJ1pWU7rQexWDahBrK+5hx3beFXUpvvFRQrGAt2icUXm18VO6Qwbp0da9jyGDSY=");
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECC__521__PUBLIC__KEY__R()
  {
    return dafny.DafnySequence.asString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAxLxcjtYfqc4+4oJZY0gGv2Ehu++CnVFea6uwXgEgLifq4eDSSVmQYvU8majsufpBXQwVjnDlQ7pGRw1j6K4FaLAAgYuMrmrwKtx/ZZtkbXzCwrqJY+sfCk8U5m89DX331cdBAhR2uVSPL2d5hp8up5v+EBpNArtdC5lZMx2ZrwKKYuQ=");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P256__PRIVATE()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n")), dafny.DafnySequence.asString("22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n")), dafny.DafnySequence.asString("7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P256__PUBLIC()
  {
    return dafny.DafnySequence.asString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp1IMe0q5R4TyJ9zHGX3N3BCLPPlxX+yb4XLldcFhCxmfAI7sJyoxNInpRMEmOR2M1ghe+9xbyWlhmBmBoUm2vA==");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P256__PRIVATE__R()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgxpnoWJBwDUkwvLHA\n")), dafny.DafnySequence.asString("YZgRRby9FdJtxAMvAcPPW6iaD+2hRANCAASihMmHeVwzccmYmFKPO5rlR+M3MBRH\n")), dafny.DafnySequence.asString("zdCaw8TGxfX25tCKkhQUm6kUlPqaCzirEYPbUt3wK8XJ6jF5iRzuGxad\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----\n"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P256__PUBLIC__R()
  {
    return dafny.DafnySequence.asString("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEooTJh3lcM3HJmJhSjzua5UfjNzAUR83QmsPExsX19ubQipIUFJupFJT6mgs4qxGD21Ld8CvFyeoxeYkc7hsWnQ==");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P384__PRIVATE()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n")), dafny.DafnySequence.asString("6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n")), dafny.DafnySequence.asString("GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n")), dafny.DafnySequence.asString("b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P384__PUBLIC()
  {
    return dafny.DafnySequence.asString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGsj1ugd2lRilhQWwx90nrjIYmNhiDxvrQRB5jGd0FGhuqjZ0MV0vkKUfeSFskFmYyJ8g5NrqXm9U4rz9FGGsvnSEvDKwRTO6CwbCSKsRokUNRDxSKQS7+JprXjpmuarf");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P384__PRIVATE__R()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDBX0BpijAta/CndWCkA\n")), dafny.DafnySequence.asString("hl4fu2mIlnsh8umliaBBDHjA2T/3eeYWid5m96Bs2QxYIn6hZANiAAR/qhoNylqV\n")), dafny.DafnySequence.asString("2084hlZEXr8XWj9DuZ0WHgJ/rniicwqxXEFwPCkeh7VvpO7+tN8HxUoWpPLSdkCK\n")), dafny.DafnySequence.asString("nWeq6senikNb4RNp3Na43wPyF2SjQI/uzujHjlrVrea2zvJP7rsLdAI=\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----\n"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P384__PUBLIC__R()
  {
    return dafny.DafnySequence.asString("MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEf6oaDcpaldtPOIZWRF6/F1o/Q7mdFh4Cf654onMKsVxBcDwpHoe1b6Tu/rTfB8VKFqTy0nZAip1nqurHp4pDW+ETadzWuN8D8hdko0CP7s7ox45a1a3mts7yT+67C3QC");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P521__PRIVATE()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n")), dafny.DafnySequence.asString("xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n")), dafny.DafnySequence.asString("oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n")), dafny.DafnySequence.asString("I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n")), dafny.DafnySequence.asString("C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n")), dafny.DafnySequence.asString("Qg==\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P521__PUBLIC()
  {
    return dafny.DafnySequence.asString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB3jJzJGnYdp5HrVE3A7yhOFgnHU3SBSmg6sLTCG6v8uTeBCO+zsWMCj+yHRgQvZ/xpHDSFsekfdc3NwCHfWu1azkBffh4rZ25Qci9btzepFoVHwt7q8tdU/HZDVvi21ZJl/Ad/rOlWhEFimvkmAXpj1dOWiYVNMWmhfzIbCxsCi6T6UI=");
  }
  public static dafny.DafnySequence<? extends Character> ECC__P521__PRIVATE__R()
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-----BEGIN PRIVATE KEY-----\n"), dafny.DafnySequence.asString("MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIAGQrViOzSEfLFHdlp\n")), dafny.DafnySequence.asString("rFcl/iWrPt7vWyga71fnLOzj4nTWBJ/Pua+xOVfTGjgplH4t16sRl4qk113Zv8zY\n")), dafny.DafnySequence.asString("XfgTJvChgYkDgYYABACKN7raKlNTwzxw97HarkQB7+9cTvw1grfhwW6AkUIS8b6J\n")), dafny.DafnySequence.asString("7CgTTSKZ6M5XQ0leYOZMkqXgjlpUfki4G3XXa4hw0wBUw+x9qtoAlwJNYhUsYg7N\n")), dafny.DafnySequence.asString("bm7IF9TQSuAzWgrSfIjOJfjrHjBR0TLmtk26xxKZIw36JSl9qb9b8LqlLk8uW6eE\n")), dafny.DafnySequence.asString("Lw==\n")), dafny.DafnySequence.asString("-----END PRIVATE KEY-----"));
  }
  public static dafny.DafnySequence<? extends Character> ECC__P521__PUBLIC__R()
  {
    return dafny.DafnySequence.asString("MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAije62ipTU8M8cPex2q5EAe/vXE78NYK34cFugJFCEvG+iewoE00imejOV0NJXmDmTJKl4I5aVH5IuBt112uIcNMAVMPsfaraAJcCTWIVLGIOzW5uyBfU0ErgM1oK0nyIziX46x4wUdEy5rZNuscSmSMN+iUpfam/W/C6pS5PLlunhC8=");
  }
  @Override
  public java.lang.String toString() {
    return "TestUtils._default";
  }
}
