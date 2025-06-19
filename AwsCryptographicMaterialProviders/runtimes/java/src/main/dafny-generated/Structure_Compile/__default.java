// Class __default
// Dafny class __default compiled into Java
package Structure_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean BranchKeyContext_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> m) {
    return ((((((((((((((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__IDENTIFIER__FIELD())) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.TYPE__FIELD()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.KEY__CREATE__TIME()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.HIERARCHY__VERSION()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.TABLE__FIELD()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.KMS__FIELD()))) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.KMS__FIELD())))))) && (!((m).keySet()).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__FIELD()))) && ((((long) (((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.BRANCH__KEY__IDENTIFIER__FIELD())))).cardinalityInt()) == 0 ? 0 : 1) == 1)) && ((((long) (((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).cardinalityInt()) == 0 ? 0 : 1) == 1)) && (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, Boolean>)(_0_m) -> dafny.Helpers.Quantifier(((_0_m).keySet()).Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends Character> _forall_var_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends Character> _1_k = (dafny.DafnySequence<? extends Character>)_forall_var_0;
      return !(((_0_m).keySet()).<dafny.DafnySequence<? extends Character>>contains(_1_k)) || (software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__AttributeName(_1_k));
    }))).apply(m))) && (((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) == ((true) && ((((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).equals(__default.BRANCH__KEY__ACTIVE__TYPE()))))) && (!((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) || ((true) && ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())))))))) && ((!(m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) == (((((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).equals(__default.BEACON__KEY__TYPE__VALUE())) || ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((m).get(__default.TYPE__FIELD())))))));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> ToAttributeMap(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> encryptedKey)
  {
    return ((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>>)(_0_encryptionContext, _1_encryptedKey) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>>)(() -> {
      java.util.HashMap<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> _coll0 = new java.util.HashMap<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union((_0_encryptionContext).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD())), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.TABLE__FIELD()))).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        if (true) {
          dafny.DafnySequence<? extends Character> _2_k = (dafny.DafnySequence<? extends Character>)_compr_0;
          if (software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeName._Is(_2_k)) {
            if ((dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union((_0_encryptionContext).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD())), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.TABLE__FIELD()))).<dafny.DafnySequence<? extends Character>>contains(_2_k)) {
              _coll0.put(_2_k,(((_2_k).equals(__default.HIERARCHY__VERSION())) ? (software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue.create_N(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_encryptionContext).get(__default.HIERARCHY__VERSION()))))) : ((((_2_k).equals(__default.BRANCH__KEY__FIELD())) ? (software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue.create_B(_1_encryptedKey)) : (software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue.create_S(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_encryptionContext).get(_2_k)))))))));
            }
          }
        }
      }
      return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>(_coll0);
    })).apply()).apply(encryptionContext, encryptedKey);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> ToBranchKeyContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> item, dafny.DafnySequence<? extends Character> logicalKeyStoreName)
  {
    return ((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>, dafny.DafnySequence<? extends Character>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(_0_item, _1_logicalKeyStoreName) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(() -> {
      java.util.HashMap<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _coll0 = new java.util.HashMap<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference((_0_item).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD())), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.TABLE__FIELD()))).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _2_k = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((dafny.DafnySet.<dafny.DafnySequence<? extends Character>>union(dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference((_0_item).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD())), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.TABLE__FIELD()))).<dafny.DafnySequence<? extends Character>>contains(_2_k)) {
          _coll0.put(_2_k,(((_2_k).equals(__default.HIERARCHY__VERSION())) ? ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_0_item).get(_2_k)))).dtor_N()) : ((((_2_k).equals(__default.TABLE__FIELD())) ? (_1_logicalKeyStoreName) : ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_0_item).get(_2_k)))).dtor_S())))));
        }
      }
      return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>>(_coll0);
    })).apply()).apply(item, logicalKeyStoreName);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.keystore.internaldafny.types.Error> ToBranchKeyMaterials(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> plaintextKey)
  {
    dafny.DafnySequence<? extends Character> _0_versionInformation = (((encryptionContext).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) ? (((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())))) : (((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(__default.TYPE__FIELD())))));
    dafny.DafnySequence<? extends Character> _1_branchKeyVersion = (_0_versionInformation).drop((__default.BRANCH__KEY__TYPE__PREFIX()).cardinalityInt());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.keystore.internaldafny.types.Error> _2_valueOrError0 = (UTF8.__default.Encode(_1_branchKeyVersion)).<software.amazon.cryptography.keystore.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>)(_3_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _3_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_3_e_boxed0));
      return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(_3_e);
    }));
    if ((_2_valueOrError0).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      return (_2_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _4_branchKeyVersionUtf8 = (_2_valueOrError0).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.keystore.internaldafny.types.Error> _5_valueOrError1 = __default.ExtractCustomEncryptionContext(encryptionContext);
      if ((_5_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
        return (_5_valueOrError1).<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor());
      } else {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _6_customEncryptionContext = (_5_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
        return Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(__default.BRANCH__KEY__IDENTIFIER__FIELD()))), _4_branchKeyVersionUtf8, _6_customEncryptionContext, plaintextKey));
      }
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials, software.amazon.cryptography.keystore.internaldafny.types.Error> ToBeaconKeyMaterials(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> plaintextKey)
  {
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.keystore.internaldafny.types.Error> _0_valueOrError0 = __default.ExtractCustomEncryptionContext(encryptionContext);
    if ((_0_valueOrError0).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials._typeDescriptor());
    } else {
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_customEncryptionContext = (_0_valueOrError0).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
      return Wrappers_Compile.Result.<software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((encryptionContext).get(__default.BRANCH__KEY__IDENTIFIER__FIELD()))), _1_customEncryptionContext, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), plaintextKey), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())))));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.keystore.internaldafny.types.Error> ExtractCustomEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> encryptionContext) {
    dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _0_prefixKeys = ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>>)(_1_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>>)(() -> {
      java.util.ArrayList<dafny.DafnySequence<? extends Character>> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : ((_1_encryptionContext).keySet()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _2_k = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((((_1_encryptionContext).keySet()).<dafny.DafnySequence<? extends Character>>contains(_2_k)) && ((__default.ENCRYPTION__CONTEXT__PREFIX()).isPrefixOf(_2_k))) {
          _coll0.add(_2_k);
        }
      }
      return new dafny.DafnySet<dafny.DafnySequence<? extends Character>>(_coll0);
    })).apply()).apply(encryptionContext);
    dafny.DafnySet<? extends dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>> _3_encodedEncryptionContext = ((dafny.Function2<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySet<? extends dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>>)(_4_prefixKeys, _5_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>>)(() -> {
      java.util.ArrayList<dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>> _coll1 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_1_boxed0 : (_4_prefixKeys).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_1 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_1_boxed0));
        dafny.DafnySequence<? extends Character> _6_k = (dafny.DafnySequence<? extends Character>)_compr_1;
        if ((_4_prefixKeys).<dafny.DafnySequence<? extends Character>>contains(_6_k)) {
          _coll1.add(dafny.Tuple2.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>create(UTF8.__default.Encode((_6_k).drop((__default.ENCRYPTION__CONTEXT__PREFIX()).cardinalityInt())), UTF8.__default.Encode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_5_encryptionContext).get(_6_k))))));
        }
      }
      return new dafny.DafnySet<dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>(_coll1);
    })).apply()).apply(_0_prefixKeys, encryptionContext);
    Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _7_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>, Boolean>)(_8_encodedEncryptionContext) -> dafny.Helpers.Quantifier((_8_encodedEncryptionContext).Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _forall_var_0 = ((dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _9_i = (dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>)_forall_var_0;
      return !((_8_encodedEncryptionContext).<dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>contains(_9_i)) || ((((_9_i).dtor__0()).is_Success()) && (((_9_i).dtor__1()).is_Success()));
    }))).apply(_3_encodedEncryptionContext), software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(dafny.DafnySequence.asString("Unable to encode string")));
    if ((_7_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
      return (_7_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()));
    } else {
      return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(_10_encodedEncryptionContext) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(() -> {
  java.util.HashMap<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _coll2 = new java.util.HashMap<>();
  for (dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _compr_2_boxed0 : (_10_encodedEncryptionContext).Elements()) {
    dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _compr_2 = ((dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>)(java.lang.Object)(_compr_2_boxed0));
    dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>> _11_i = (dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>)_compr_2;
    if ((_10_encodedEncryptionContext).<dafny.Tuple2<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>>>contains(_11_i)) {
      _coll2.put(((_11_i).dtor__0()).dtor_value(),((_11_i).dtor__1()).dtor_value());
    }
  }
  return new dafny.DafnyMap<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>>(_coll2);
})).apply()).apply(_3_encodedEncryptionContext));
    }
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> DecryptOnlyBranchKeyEncryptionContext(dafny.DafnySequence<? extends Character> branchKeyId, dafny.DafnySequence<? extends Character> branchKeyVersion, dafny.DafnySequence<? extends Character> timestamp, dafny.DafnySequence<? extends Character> logicalKeyStoreName, dafny.DafnySequence<? extends Character> kmsKeyArn, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> customEncryptionContext)
  {
    return dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>merge(dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.BRANCH__KEY__IDENTIFIER__FIELD(), branchKeyId), new dafny.Tuple2(__default.TYPE__FIELD(), dafny.DafnySequence.<Character>concatenate(__default.BRANCH__KEY__TYPE__PREFIX(), branchKeyVersion)), new dafny.Tuple2(__default.KEY__CREATE__TIME(), timestamp), new dafny.Tuple2(__default.TABLE__FIELD(), logicalKeyStoreName), new dafny.Tuple2(__default.KMS__FIELD(), kmsKeyArn), new dafny.Tuple2(__default.HIERARCHY__VERSION(), dafny.DafnySequence.asString("1"))), ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(_0_customEncryptionContext) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(() -> {
      java.util.HashMap<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _coll0 = new java.util.HashMap<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (_0_customEncryptionContext).keySet().Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _1_k = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((_0_customEncryptionContext).<dafny.DafnySequence<? extends Character>>contains(_1_k)) {
          _coll0.put(dafny.DafnySequence.<Character>concatenate(__default.ENCRYPTION__CONTEXT__PREFIX(), _1_k),((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_customEncryptionContext).get(_1_k))));
        }
      }
      return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>>(_coll0);
    })).apply()).apply(customEncryptionContext));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> ActiveBranchKeyEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> decryptOnlyEncryptionContext) {
    return dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>merge(decryptOnlyEncryptionContext, dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD(), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((decryptOnlyEncryptionContext).get(__default.TYPE__FIELD())))), new dafny.Tuple2(__default.TYPE__FIELD(), __default.BRANCH__KEY__ACTIVE__TYPE())));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> BeaconKeyEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> decryptOnlyEncryptionContext) {
    return dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>merge(decryptOnlyEncryptionContext, dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.TYPE__FIELD(), __default.BEACON__KEY__TYPE__VALUE())));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> NewVersionFromActiveBranchKeyEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> activeBranchKeyEncryptionContext, dafny.DafnySequence<? extends Character> branchKeyVersion, dafny.DafnySequence<? extends Character> timestamp)
  {
    return dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>subtract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>merge(activeBranchKeyEncryptionContext, dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.TYPE__FIELD(), dafny.DafnySequence.<Character>concatenate(__default.BRANCH__KEY__TYPE__PREFIX(), branchKeyVersion)), new dafny.Tuple2(__default.KEY__CREATE__TIME(), timestamp))), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()));
  }
  public static boolean BranchKeyItem_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> m) {
    return (((((((((((((((((((((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__IDENTIFIER__FIELD())) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__IDENTIFIER__FIELD())))).is_S())) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.TYPE__FIELD()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).is_S())) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.KEY__CREATE__TIME()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.KEY__CREATE__TIME())))).is_S())) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.HIERARCHY__VERSION()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.HIERARCHY__VERSION())))).is_N())) && (!(m).<dafny.DafnySequence<? extends Character>>contains(__default.TABLE__FIELD()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.KMS__FIELD()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.KMS__FIELD())))).is_S())) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.KMS__FIELD())))).dtor_S()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__FIELD()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__FIELD())))).is_B())) && ((((long) ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__IDENTIFIER__FIELD())))).dtor_S()).cardinalityInt()) == 0 ? 0 : 1) == 1)) && ((((long) ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()).cardinalityInt()) == 0 ? 0 : 1) == 1)) && (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue>, Boolean>)(_0_m) -> dafny.Helpers.Quantifier((dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference((_0_m).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD(), __default.HIERARCHY__VERSION()))).Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends Character> _forall_var_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends Character> _1_k = (dafny.DafnySequence<? extends Character>)_forall_var_0;
      return !((dafny.DafnySet.<dafny.DafnySequence<? extends Character>>difference((_0_m).keySet(), dafny.DafnySet.<dafny.DafnySequence<? extends Character>> of(__default.BRANCH__KEY__FIELD(), __default.HIERARCHY__VERSION()))).<dafny.DafnySequence<? extends Character>>contains(_1_k)) || ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((_0_m).get(_1_k)))).is_S());
    }))).apply(m))) && (((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) == ((true) && (((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()).equals(__default.BRANCH__KEY__ACTIVE__TYPE()))))) && (!((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) || ((true) && ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())))).dtor_S()))))) && ((!(m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())) == ((((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()).equals(__default.BEACON__KEY__TYPE__VALUE())) || ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()))))) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__FIELD())))).dtor_B()));
  }
  public static boolean ActiveBranchKeyItem_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> m) {
    return ((((__default.BranchKeyItem_q(m)) && (((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()).equals(__default.BRANCH__KEY__ACTIVE__TYPE()))) && ((m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()))) && ((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())))).is_S())) && ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD())))).dtor_S()));
  }
  public static boolean VersionBranchKeyItem_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> m) {
    return ((__default.BranchKeyItem_q(m)) && (!(m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()))) && ((__default.BRANCH__KEY__TYPE__PREFIX()).isProperPrefixOf((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()));
  }
  public static boolean BeaconKeyItem_q(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue> m) {
    return ((__default.BranchKeyItem_q(m)) && (!(m).<dafny.DafnySequence<? extends Character>>contains(__default.BRANCH__KEY__ACTIVE__VERSION__FIELD()))) && (((((software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue)(java.lang.Object)((m).get(__default.TYPE__FIELD())))).dtor_S()).equals(__default.BEACON__KEY__TYPE__VALUE()));
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__IDENTIFIER__FIELD()
  {
    return dafny.DafnySequence.asString("branch-key-id");
  }
  public static dafny.DafnySequence<? extends Character> TYPE__FIELD()
  {
    return dafny.DafnySequence.asString("type");
  }
  public static dafny.DafnySequence<? extends Character> KEY__CREATE__TIME()
  {
    return dafny.DafnySequence.asString("create-time");
  }
  public static dafny.DafnySequence<? extends Character> HIERARCHY__VERSION()
  {
    return dafny.DafnySequence.asString("hierarchy-version");
  }
  public static dafny.DafnySequence<? extends Character> TABLE__FIELD()
  {
    return dafny.DafnySequence.asString("tablename");
  }
  public static dafny.DafnySequence<? extends Character> KMS__FIELD()
  {
    return dafny.DafnySequence.asString("kms-arn");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__FIELD()
  {
    return dafny.DafnySequence.asString("enc");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ACTIVE__VERSION__FIELD()
  {
    return dafny.DafnySequence.asString("version");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__ACTIVE__TYPE()
  {
    return dafny.DafnySequence.asString("branch:ACTIVE");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__TYPE__PREFIX()
  {
    return dafny.DafnySequence.asString("branch:version:");
  }
  public static dafny.DafnySequence<? extends Character> BEACON__KEY__TYPE__VALUE()
  {
    return dafny.DafnySequence.asString("beacon:ACTIVE");
  }
  public static dafny.DafnySequence<? extends Character> ENCRYPTION__CONTEXT__PREFIX()
  {
    return dafny.DafnySequence.asString("aws-crypto-ec:");
  }
  @Override
  public java.lang.String toString() {
    return "Structure._default";
  }
}
