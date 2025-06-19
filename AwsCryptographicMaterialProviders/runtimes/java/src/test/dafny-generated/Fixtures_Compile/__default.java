// Class __default
// Dafny class __default compiled into Java
package Fixtures_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> EncodeEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> input)
  {
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
    if(true) {
      dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>> _0_encodedEncryptionContext;
      _0_encodedEncryptionContext = ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>>)(_1_input) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>>)(() -> {
        java.util.ArrayList<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>> _coll0 = new java.util.ArrayList<>();
        for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (_1_input).keySet().Elements()) {
          dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
          dafny.DafnySequence<? extends Character> _2_k = (dafny.DafnySequence<? extends Character>)_compr_0;
          if ((_1_input).<dafny.DafnySequence<? extends Character>>contains(_2_k)) {
            _coll0.add(dafny.Tuple3.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create(UTF8.__default.Encode(_2_k), UTF8.__default.Encode(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_1_input).get(_2_k)))), _2_k));
          }
        }
        return new dafny.DafnySet<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>(_coll0);
      })).apply()).apply(input);
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _3_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>, Boolean>)(_4_encodedEncryptionContext) -> dafny.Helpers.Quantifier((_4_encodedEncryptionContext).Elements(), true, ((_forall_var_0_boxed0) -> {
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _forall_var_0 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(_forall_var_0_boxed0));
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _5_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>)_forall_var_0;
        return !((_4_encodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>contains(_5_i)) || (((((_5_i).dtor__0()).is_Success()) && (((_5_i).dtor__1()).is_Success())) && (((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Boolean>Let(UTF8.__default.Decode(((_5_i).dtor__0()).dtor_value()), boxed0 -> {
          Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _pat_let0_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed0));
          return ((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Boolean>Let(_pat_let0_0, boxed1 -> {
            Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _6_encoded = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed1));
            return ((_6_encoded).is_Success()) && (((_5_i).dtor__2()).equals((_6_encoded).dtor_value()));
          }
          )));
        }
        )))));
      }))).apply(_0_encodedEncryptionContext), dafny.DafnySequence.asString("Unable to encode string"));
      if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_3_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()));
        return output;
      }
      output = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(_7_encodedEncryptionContext) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(() -> {
  java.util.HashMap<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _coll1 = new java.util.HashMap<>();
  for (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _compr_1_boxed0 : (_7_encodedEncryptionContext).Elements()) {
    dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _compr_1 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(_compr_1_boxed0));
    dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _8_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>)_compr_1;
    if ((_7_encodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>>contains(_8_i)) {
      _coll1.put(((_8_i).dtor__0()).dtor_value(),((_8_i).dtor__1()).dtor_value());
    }
  }
  return new dafny.DafnyMap<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>>(_coll1);
})).apply()).apply(_0_encodedEncryptionContext));
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> DecodeEncryptionContext(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> input)
  {
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    if(true) {
      dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>> _0_decodedEncryptionContext;
      _0_decodedEncryptionContext = ((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_input) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
        java.util.ArrayList<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>> _coll0 = new java.util.ArrayList<>();
        for (dafny.DafnySequence<? extends java.lang.Byte> _compr_0_boxed0 : (_1_input).keySet().Elements()) {
          dafny.DafnySequence<? extends java.lang.Byte> _compr_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_compr_0_boxed0));
          dafny.DafnySequence<? extends java.lang.Byte> _2_k = (dafny.DafnySequence<? extends java.lang.Byte>)_compr_0;
          if ((_1_input).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_2_k)) {
            _coll0.add(dafny.Tuple3.<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>create(UTF8.__default.Decode(_2_k), UTF8.__default.Decode(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_1_input).get(_2_k)))), _2_k));
          }
        }
        return new dafny.DafnySet<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>(_coll0);
      })).apply()).apply(input);
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError0 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _3_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>, Boolean>)(_4_decodedEncryptionContext) -> dafny.Helpers.Quantifier((_4_decodedEncryptionContext).Elements(), true, ((_forall_var_0_boxed0) -> {
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _forall_var_0 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_forall_var_0_boxed0));
        dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _5_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)_forall_var_0;
        return !((_4_decodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_i)) || (((((_5_i).dtor__0()).is_Success()) && (((_5_i).dtor__1()).is_Success())) && (((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Boolean>Let(UTF8.__default.Encode(((_5_i).dtor__0()).dtor_value()), boxed2 -> {
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _pat_let1_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed2));
          return ((boolean)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Boolean>Let(_pat_let1_0, boxed3 -> {
            Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_decoded = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed3));
            return ((_6_decoded).is_Success()) && (((_5_i).dtor__2()).equals((_6_decoded).dtor_value()));
          }
          )));
        }
        )))));
      }))).apply(_0_decodedEncryptionContext), dafny.DafnySequence.asString("Unable to decode string"));
      if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_3_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
        return output;
      }
      output = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySet<? extends dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(_7_decodedEncryptionContext) -> ((dafny.Function0<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>)(() -> {
  java.util.HashMap<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _coll1 = new java.util.HashMap<>();
  for (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (_7_decodedEncryptionContext).Elements()) {
    dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
    dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>> _8_i = (dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
    if ((_7_decodedEncryptionContext).<dafny.Tuple3<Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends java.lang.Byte>>>contains(_8_i)) {
      _coll1.put(((_8_i).dtor__0()).dtor_value(),((_8_i).dtor__1()).dtor_value());
    }
  }
  return new dafny.DafnyMap<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>>(_coll1);
})).apply()).apply(_0_decodedEncryptionContext));
    }
    return output;
  }
  public static dafny.DafnySequence<? extends Character> branchKeyStoreName()
  {
    return dafny.DafnySequence.asString("KeyStoreDdbTable");
  }
  public static dafny.DafnySequence<? extends Character> logicalKeyStoreName()
  {
    return __default.branchKeyStoreName();
  }
  public static dafny.DafnySequence<? extends Character> MrkArnEast()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7");
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsConfigEast()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.MrkArnEast());
  }
  public static dafny.DafnySequence<? extends Character> MrkArnWest()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7");
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsConfigWest()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.MrkArnWest());
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsMrkConfigEast()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsMRKeyArn(__default.MrkArnEast());
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsMrkConfigWest()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsMRKeyArn(__default.MrkArnWest());
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsSrkConfigEast()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.MrkArnEast());
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsSrkConfigWest()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(__default.MrkArnWest());
  }
  public static dafny.DafnySequence<? extends Character> MrkArnAP()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7");
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration KmsMrkConfigAP()
  {
    return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsMRKeyArn(__default.MrkArnAP());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> abc()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 98, (byte) 99);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> x123()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 49, (byte) 50, (byte) 51);
    return _0_s;
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> KmsMrkEC()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.abc(), __default.x123()));
  }
  public static dafny.DafnySequence<? extends Character> branchKeyId()
  {
    return dafny.DafnySequence.asString("3f43a9af-08c5-4317-b694-3d3e883dcaef");
  }
  public static dafny.DafnySequence<? extends Character> branchKeyIdActiveVersion()
  {
    return dafny.DafnySequence.asString("a4905627-4b7f-4272-a847-f50dae245737");
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> branchKeyIdActiveVersionUtf8Bytes()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 52, (byte) 57, (byte) 48, (byte) 53, (byte) 54, (byte) 50, (byte) 55, (byte) 45, (byte) 52, (byte) 98, (byte) 55, (byte) 102, (byte) 45, (byte) 52, (byte) 50, (byte) 55, (byte) 50, (byte) 45, (byte) 97, (byte) 56, (byte) 52, (byte) 55, (byte) 45, (byte) 102, (byte) 53, (byte) 48, (byte) 100, (byte) 97, (byte) 101, (byte) 50, (byte) 52, (byte) 53, (byte) 55, (byte) 51, (byte) 55);
  }
  public static dafny.DafnySequence<? extends Character> branchKeyIdWithEC()
  {
    return dafny.DafnySequence.asString("4bb57643-07c1-419e-92ad-0df0df149d7c");
  }
  public static dafny.DafnySequence<? extends Character> keyArn()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126");
  }
  public static dafny.DafnySequence<? extends Character> keyId()
  {
    return dafny.DafnySequence.asString("9d989aa2-2f9c-438c-a745-cc57d3ad0126");
  }
  public static dafny.DafnySequence<? extends Character> mrkRsaKeyArn()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297");
  }
  public static dafny.DafnySequence<? extends Character> EastBranchKey()
  {
    return dafny.DafnySequence.asString("MyEastBranch2");
  }
  public static dafny.DafnySequence<? extends Character> WestBranchKey()
  {
    return dafny.DafnySequence.asString("MyWestBranch2");
  }
  public static dafny.DafnySequence<? extends Character> publicKeyArn()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f");
  }
  public static dafny.DafnySequence<? extends Character> postalHornKeyArn()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
  }
  public static dafny.DafnySequence<? extends Character> kmsKeyAlias()
  {
    return dafny.DafnySequence.asString("arn:aws:kms:us-west-2:370957321024:alias/postalHorn");
  }
  public static dafny.DafnySequence<? extends Character> postalHornBranchKeyId()
  {
    return dafny.DafnySequence.asString("682dfba7-4c35-491d-8d6a-5a9c56194061");
  }
  public static dafny.DafnySequence<? extends Character> postalHornBranchKeyActiveVersion()
  {
    return dafny.DafnySequence.asString("6b7a8ef4-8c1c-4f63-b196-a6ef7e496e50");
  }
  public static dafny.DafnySequence<? extends Character> lyingBranchKeyId()
  {
    return dafny.DafnySequence.asString("kms-arn-attribute-is-lying");
  }
  public static dafny.DafnySequence<? extends Character> lyingBranchKeyDecryptOnlyVersion()
  {
    return dafny.DafnySequence.asString("129c5c87-308a-41c9-8b9d-a27f66e915f4");
  }
  @Override
  public java.lang.String toString() {
    return "Fixtures._default";
  }
}
