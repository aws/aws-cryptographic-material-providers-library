// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig DefaultKeyVectorsConfig() {
    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig.create(dafny.DafnySequence.asString(""));
  }
  public static Wrappers_Compile.Result<KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> KeyVectors(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig config)
  {
    Wrappers_Compile.Result<KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> res = (Wrappers_Compile.Result<KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = FileIO_Compile.__default.ReadBytesFromFile((config).dtor_keyManifestPath());
      _0_valueOrError0 = _out0;
      if (!(!((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/KeyVectors/src/Index.dfy(30,29): " + java.lang.String.valueOf(_0_valueOrError0));
      }
      dafny.DafnySequence<? extends java.lang.Byte> _1_keysManifestBytes;
      _1_keysManifestBytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<JSON_mValues_Compile.JSON, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(JSON_mValues_Compile.JSON._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), JSON_mValues_Compile.JSON.Default());
      _2_valueOrError1 = (JSON_mAPI_Compile.__default.Deserialize(_1_keysManifestBytes)).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<JSON_mErrors_Compile.DeserializationError, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_3_e_boxed0) -> {
        JSON_mErrors_Compile.DeserializationError _3_e = ((JSON_mErrors_Compile.DeserializationError)(java.lang.Object)(_3_e_boxed0));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException((_3_e).ToString());
      }));
      if ((_2_valueOrError1).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
        res = (_2_valueOrError1).<KeyVectorsClient>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyVectorsClient.class)));
        return res;
      }
      JSON_mValues_Compile.JSON _4_keysManifestJSON;
      _4_keysManifestJSON = (_2_valueOrError1).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
      if (!((_4_keysManifestJSON).is_Object())) {
        throw new dafny.DafnyHaltException("dafny/KeyVectors/src/Index.dfy(35,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Default(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON.Default());
      _5_valueOrError2 = JSONHelpers_Compile.__default.Get(dafny.DafnySequence.asString("keys"), (_4_keysManifestJSON).dtor_obj());
      if (!(!((_5_valueOrError2).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/KeyVectors/src/Index.dfy(36,22): " + java.lang.String.valueOf(_5_valueOrError2));
      }
      JSON_mValues_Compile.JSON _6_keysObject;
      _6_keysObject = (_5_valueOrError2).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      if (!((_6_keysObject).is_Object())) {
        throw new dafny.DafnyHaltException("dafny/KeyVectors/src/Index.dfy(37,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_maybeMpl;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = software.amazon.cryptography.materialproviders.internaldafny.__default.MaterialProviders(software.amazon.cryptography.materialproviders.internaldafny.__default.DefaultMaterialProvidersConfig());
      _7_maybeMpl = _out1;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _8_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
      _8_valueOrError3 = (_7_maybeMpl).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_9_e_boxed0) -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _9_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_9_e_boxed0));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_AwsCryptographyMaterialProviders(_9_e);
      }));
      if ((_8_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError3).<KeyVectorsClient>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyVectorsClient.class)));
        return res;
      }
      software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient _10_mpl;
      _10_mpl = (_8_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.MaterialProvidersClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _11_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial_Compile.KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial_Compile.KeyMaterial._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,KeyMaterial_Compile.KeyMaterial> empty());
      _11_valueOrError4 = (KeyMaterial_Compile.__default.BuildKeyMaterials(_10_mpl, (_6_keysObject).dtor_obj())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>MapFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial_Compile.KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial_Compile.KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)(_12_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _12_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_12_e_boxed0));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error.create_KeyVectorException(_12_e);
      }));
      if ((_11_valueOrError4).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial_Compile.KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial_Compile.KeyMaterial._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())) {
        res = (_11_valueOrError4).<KeyVectorsClient>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial_Compile.KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial_Compile.KeyMaterial._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyVectorsClient.class)));
        return res;
      }
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial_Compile.KeyMaterial> _13_keys;
      _13_keys = (_11_valueOrError4).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial_Compile.KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial_Compile.KeyMaterial._typeDescriptor()), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
      KeysVectorOperations_Compile.Config _14_config;
      _14_config = KeysVectorOperations_Compile.Config.create(_13_keys, _4_keysManifestJSON);
      KeyVectorsClient _15_client;
      KeyVectorsClient _nw0 = new KeyVectorsClient();
      _nw0.__ctor(_14_config);
      _15_client = _nw0;
      res = Wrappers_Compile.Result.<KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(KeyVectorsClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), _15_client);
    }
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.IKeyVectorsClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "KeyVectors._default";
  }
}
