// Class __default
// Dafny class __default compiled into Java
package KeyMaterial_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>, dafny.DafnySequence<? extends Character>> BuildKeyMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    if ((java.math.BigInteger.valueOf((obj).length())).signum() == 0) {
      return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.fromElements());
    } else {
      dafny.DafnySequence<? extends Character> _0_name = (((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((obj).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor__0();
      Wrappers_Compile.Result<KeyMaterial, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = __default.ToKeyMaterial(mpl, _0_name, (((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)((obj).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))).dtor__1());
      if ((_1_valueOrError0).IsFailure(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_1_valueOrError0).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>>PropagateFailure(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()));
      } else {
        KeyMaterial _2_keyMaterial = (_1_valueOrError0).Extract(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = __default.BuildKeyMaterials(mpl, (obj).drop(java.math.BigInteger.ONE));
        if ((_3_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_3_valueOrError1).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()));
        } else {
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial> _4_tail = (_3_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          return Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeyMaterial>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, KeyMaterial>merge(dafny.DafnyMap.fromElements(new dafny.Tuple2(_0_name, _2_keyMaterial)), _4_tail));
        }
      }
    }
  }
  public static Wrappers_Compile.Result<KeyMaterial, dafny.DafnySequence<? extends Character>> ToKeyMaterial(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends Character> name, JSON_mValues_Compile.JSON obj)
  {
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (obj).is_Object(), dafny.DafnySequence.asString("KeyDescription not an object"));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _1_obj = (obj).dtor_obj();
      dafny.DafnySequence<? extends Character> _2_typString = dafny.DafnySequence.asString("type");
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _3_valueOrError1 = JSONHelpers_Compile.__default.GetString(_2_typString, _1_obj);
      if ((_3_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_3_valueOrError1).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends Character> _4_typ = (_3_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.KeyMaterialString_q(_4_typ), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unsupported KeyMaterial type:"), _4_typ));
        if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_5_valueOrError2).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
        } else {
          if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("static-material"))) {
            return __default.ToStaticMaterial(mpl, name, _1_obj);
          } else if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("static-branch-key"))) {
            return __default.ToStaticBranchKey(mpl, name, _1_obj);
          } else {
            Wrappers_Compile.Result<Boolean, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = JSONHelpers_Compile.__default.GetBool(dafny.DafnySequence.asString("encrypt"), _1_obj);
            if ((_6_valueOrError3).IsFailure(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_6_valueOrError3).<KeyMaterial>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
            } else {
              boolean _7_encrypt = (_6_valueOrError3).Extract(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              Wrappers_Compile.Result<Boolean, dafny.DafnySequence<? extends Character>> _8_valueOrError4 = JSONHelpers_Compile.__default.GetBool(dafny.DafnySequence.asString("decrypt"), _1_obj);
              if ((_8_valueOrError4).IsFailure(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                return (_8_valueOrError4).<KeyMaterial>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
              } else {
                boolean _9_decrypt = (_8_valueOrError4).Extract(dafny.TypeDescriptor.BOOLEAN, dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _10_valueOrError5 = JSONHelpers_Compile.__default.GetOptionalString(dafny.DafnySequence.asString("key-id"), _1_obj);
                if ((_10_valueOrError5).IsFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                  return (_10_valueOrError5).<KeyMaterial>PropagateFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                } else {
                  Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _11_keyIdentifierOption = (_10_valueOrError5).Extract(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                  dafny.DafnySequence<? extends Character> _12_keyIdentifier = (_11_keyIdentifierOption).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), name);
                  if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("aws-kms"))) {
                    return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_KMS(name, _7_encrypt, _9_decrypt, _12_keyIdentifier));
                  } else if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("aws-kms-ecdh"))) {
                    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _13_valueOrError6 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("algorithm"), _1_obj);
                    if ((_13_valueOrError6).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                      return (_13_valueOrError6).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                    } else {
                      dafny.DafnySequence<? extends Character> _14_algorithm = (_13_valueOrError6).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _15_valueOrError7 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("sender-material"), _1_obj);
                      if ((_15_valueOrError7).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                        return (_15_valueOrError7).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                      } else {
                        dafny.DafnySequence<? extends Character> _16_senderMaterial = (_15_valueOrError7).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _17_valueOrError8 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("recipient-material"), _1_obj);
                        if ((_17_valueOrError8).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                          return (_17_valueOrError8).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                        } else {
                          dafny.DafnySequence<? extends Character> _18_recipientMaterial = (_17_valueOrError8).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                          Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _19_valueOrError9 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("encoding"), _1_obj);
                          if ((_19_valueOrError9).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                            return (_19_valueOrError9).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                          } else {
                            dafny.DafnySequence<? extends Character> _20_encoding = (_19_valueOrError9).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                            Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _21_valueOrError10 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("sender-material-public-key"), _1_obj);
                            if ((_21_valueOrError10).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                              return (_21_valueOrError10).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                            } else {
                              dafny.DafnySequence<? extends Character> _22_senderPublicKey = (_21_valueOrError10).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                              Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _23_valueOrError11 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("recipient-material-public-key"), _1_obj);
                              if ((_23_valueOrError11).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                return (_23_valueOrError11).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                              } else {
                                dafny.DafnySequence<? extends Character> _24_recipientPublicKey = (_23_valueOrError11).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_KMSEcdh(name, _7_encrypt, _9_decrypt, _12_keyIdentifier, _14_algorithm, _16_senderMaterial, _18_recipientMaterial, _22_senderPublicKey, _24_recipientPublicKey));
                              }
                            }
                          }
                        }
                      }
                    }
                  } else if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("ecc-private"))) {
                    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _25_valueOrError12 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("algorithm"), _1_obj);
                    if ((_25_valueOrError12).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                      return (_25_valueOrError12).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                    } else {
                      dafny.DafnySequence<? extends Character> _26_algorithm = (_25_valueOrError12).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                      Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> _27_valueOrError13 = JSONHelpers_Compile.__default.GetNat(dafny.DafnySequence.asString("bits"), _1_obj);
                      if ((_27_valueOrError13).IsFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                        return (_27_valueOrError13).<KeyMaterial>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                      } else {
                        java.math.BigInteger _28_bits = (_27_valueOrError13).Extract(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _29_valueOrError14 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("encoding"), _1_obj);
                        if ((_29_valueOrError14).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                          return (_29_valueOrError14).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                        } else {
                          dafny.DafnySequence<? extends Character> _30_encoding = (_29_valueOrError14).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                          Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _31_valueOrError15 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("sender-material"), _1_obj);
                          if ((_31_valueOrError15).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                            return (_31_valueOrError15).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                          } else {
                            dafny.DafnySequence<? extends Character> _32_senderMaterial = (_31_valueOrError15).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                            Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _33_valueOrError16 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("recipient-material"), _1_obj);
                            if ((_33_valueOrError16).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                              return (_33_valueOrError16).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                            } else {
                              dafny.DafnySequence<? extends Character> _34_recipientMaterial = (_33_valueOrError16).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                              Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _35_valueOrError17 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("sender-material-public-key"), _1_obj);
                              if ((_35_valueOrError17).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                return (_35_valueOrError17).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                              } else {
                                dafny.DafnySequence<? extends Character> _36_senderPublicKey = (_35_valueOrError17).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _37_valueOrError18 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("recipient-material-public-key"), _1_obj);
                                if ((_37_valueOrError18).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                  return (_37_valueOrError18).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                                } else {
                                  dafny.DafnySequence<? extends Character> _38_recipientPublicKey = (_37_valueOrError18).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                  return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_PrivateECDH(name, _7_encrypt, _9_decrypt, _26_algorithm, _28_bits, _30_encoding, _32_senderMaterial, _34_recipientMaterial, _36_senderPublicKey, _38_recipientPublicKey, _12_keyIdentifier));
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  } else {
                    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _39_valueOrError19 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("algorithm"), _1_obj);
                    if ((_39_valueOrError19).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                      return (_39_valueOrError19).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                    } else {
                      dafny.DafnySequence<? extends Character> _40_algorithm = (_39_valueOrError19).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                      Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> _41_valueOrError20 = JSONHelpers_Compile.__default.GetNat(dafny.DafnySequence.asString("bits"), _1_obj);
                      if ((_41_valueOrError20).IsFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                        return (_41_valueOrError20).<KeyMaterial>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                      } else {
                        java.math.BigInteger _42_bits = (_41_valueOrError20).Extract(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _43_valueOrError21 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("encoding"), _1_obj);
                        if ((_43_valueOrError21).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                          return (_43_valueOrError21).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                        } else {
                          dafny.DafnySequence<? extends Character> _44_encoding = (_43_valueOrError21).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                          Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _45_valueOrError22 = JSONHelpers_Compile.__default.Get(dafny.DafnySequence.asString("material"), _1_obj);
                          if ((_45_valueOrError22).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                            return (_45_valueOrError22).<KeyMaterial>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                          } else {
                            JSON_mValues_Compile.JSON _46_material_q = (_45_valueOrError22).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                            Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _47_valueOrError23 = ((java.util.function.Function<JSON_mValues_Compile.JSON, Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>>)(_source0_boxed0) -> {
                              JSON_mValues_Compile.JSON _source0 = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_source0_boxed0));
                              if (_source0.is_Null()) {
                                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Unsupported material shape."));
                              } else if (_source0.is_Bool()) {
                                boolean _48___mcc_h0 = ((JSON_mValues_Compile.JSON_Bool)_source0)._b;
                                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Unsupported material shape."));
                              } else if (_source0.is_String()) {
                                dafny.DafnySequence<? extends Character> _49___mcc_h2 = ((JSON_mValues_Compile.JSON_String)_source0)._str;
                                dafny.DafnySequence<? extends Character> _50_str = _49___mcc_h2;
                                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _50_str);
                              } else if (_source0.is_Number()) {
                                JSON_mValues_Compile.Decimal _51___mcc_h4 = ((JSON_mValues_Compile.JSON_Number)_source0)._num;
                                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Unsupported material shape."));
                              } else if (_source0.is_Object()) {
                                dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _52___mcc_h6 = ((JSON_mValues_Compile.JSON_Object)_source0)._obj;
                                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Unsupported material shape."));
                              } else {
                                dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _53___mcc_h8 = ((JSON_mValues_Compile.JSON_Array)_source0)._arr;
                                dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _54_arr = _53___mcc_h8;
                                Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _55_valueOrError24 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.math.BigInteger.valueOf((_54_arr).length())).signum() == 1) && (((java.util.function.Function<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, Boolean>)(_56_arr) -> dafny.Helpers.Quantifier((_56_arr).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
                                  JSON_mValues_Compile.JSON _forall_var_0 = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_forall_var_0_boxed0));
                                  JSON_mValues_Compile.JSON _57_s = (JSON_mValues_Compile.JSON)_forall_var_0;
                                  return !((_56_arr).contains(_57_s)) || ((_57_s).is_String());
                                }))).apply(_54_arr)), dafny.DafnySequence.asString("Unsupported material shape."));
                                if ((_55_valueOrError24).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                  return (_55_valueOrError24).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                } else {
                                  dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _58_strings = Seq_Compile.__default.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Map(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>)(_59_s_boxed0) -> {
                                    JSON_mValues_Compile.JSON _59_s = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_59_s_boxed0));
                                    return (_59_s).dtor_str();
                                  }), _54_arr);
                                  dafny.DafnySequence<? extends Character> _60_material = StandardLibrary_Compile.__default.<Character>Join(dafny.TypeDescriptor.CHAR, _58_strings, dafny.DafnySequence.asString("\n"));
                                  return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _60_material);
                                }
                              }
                            }).apply(_46_material_q);
                            if ((_47_valueOrError23).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                              return (_47_valueOrError23).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                            } else {
                              dafny.DafnySequence<? extends Character> _61_material = (_47_valueOrError23).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                              if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("symmetric"))) {
                                Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _62_valueOrError25 = Base64_Compile.__default.Decode(_61_material);
                                if ((_62_valueOrError25).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                  return (_62_valueOrError25).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                                } else {
                                  dafny.DafnySequence<? extends java.lang.Byte> _63_materialBytes = (_62_valueOrError25).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                  return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_Symetric(name, _7_encrypt, _9_decrypt, _40_algorithm, _42_bits, _44_encoding, _63_materialBytes, _12_keyIdentifier));
                                }
                              } else if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("private"))) {
                                return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_PrivateRSA(name, _7_encrypt, _9_decrypt, _40_algorithm, _42_bits, _44_encoding, _61_material, _12_keyIdentifier));
                              } else if (java.util.Objects.equals(_4_typ, dafny.DafnySequence.asString("public"))) {
                                return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_PublicRSA(name, _7_encrypt, _9_decrypt, _42_bits, _40_algorithm, _44_encoding, _61_material, _12_keyIdentifier));
                              } else {
                                Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _64_valueOrError26 = UTF8.__default.Encode(_61_material);
                                if ((_64_valueOrError26).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                                  return (_64_valueOrError26).<KeyMaterial>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                                } else {
                                  dafny.DafnySequence<? extends java.lang.Byte> _65_publicKey = (_64_valueOrError26).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                                  return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_KMSAsymetric(name, _7_encrypt, _9_decrypt, _12_keyIdentifier, _42_bits, _40_algorithm, _44_encoding, _65_publicKey));
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<KeyMaterial, dafny.DafnySequence<? extends Character>> ToStaticMaterial(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.GetAlgorithmSuiteInfo(mpl, obj);
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<KeyMaterial>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (_0_valueOrError0).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = JSONHelpers_Compile.__default.SmallObjectToStringStringMap(dafny.DafnySequence.asString("encryptionContext"), obj);
      if ((_2_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<KeyMaterial>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
      } else {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _3_encryptionContextStrings = (_2_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = JSONHelpers_Compile.__default.utf8EncodeMap(_3_encryptionContextStrings);
        if ((_4_valueOrError2).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_4_valueOrError2).<KeyMaterial>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
        } else {
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_encryptionContext = (_4_valueOrError2).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = JSONHelpers_Compile.__default.GetArrayString(dafny.DafnySequence.asString("requiredEncryptionContextKeys"), obj);
          if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_6_valueOrError3).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
          } else {
            dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _7_keysAsStrings = (_6_valueOrError3).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
            Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _8_valueOrError4 = JSONHelpers_Compile.__default.utf8EncodeSeq(_7_keysAsStrings);
            if ((_8_valueOrError4).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_8_valueOrError4).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
            } else {
              dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _9_requiredEncryptionContextKeys = (_8_valueOrError4).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>, dafny.DafnySequence<? extends Character>> _10_valueOrError5 = JSONHelpers_Compile.__default.GetArrayObject(dafny.DafnySequence.asString("encryptedDataKeys"), obj);
              if ((_10_valueOrError5).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                return (_10_valueOrError5).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
              } else {
                dafny.DafnySequence<? extends dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>> _11_encryptedDataKeysJSON = (_10_valueOrError5).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>>_typeDescriptor(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()))), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, dafny.DafnySequence<? extends Character>> _12_valueOrError6 = Seq_Compile.__default.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, dafny.DafnySequence<? extends Character>>MapWithResult(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default::ToEncryptedDataKey, _11_encryptedDataKeysJSON);
                if ((_12_valueOrError6).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                  return (_12_valueOrError6).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                } else {
                  dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _13_encryptedDataKeys = (_12_valueOrError6).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                  Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _14_valueOrError7 = JSONHelpers_Compile.__default.GetOptionalString(dafny.DafnySequence.asString("plaintextDataKey"), obj);
                  if ((_14_valueOrError7).IsFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                    return (_14_valueOrError7).<KeyMaterial>PropagateFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                  } else {
                    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _15_plaintextDataKeyEncoded = (_14_valueOrError7).Extract(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                    Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>> _16_valueOrError8 = (((_15_plaintextDataKeyEncoded).is_Some()) ? (((Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>Let(Base64_Compile.__default.Decode((_15_plaintextDataKeyEncoded).dtor_value()), boxed12 -> {
                      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _pat_let6_0 = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed12));
                      return ((Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>, Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>>Let(_pat_let6_0, boxed13 -> {
                        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _17_result = ((Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>)(java.lang.Object)(boxed13));
                        return (((_17_result).is_Success()) ? (Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_17_result).dtor_value()))) : (Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Failure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_17_result).dtor_error())));
                      }
                      )));
                    }
                    )))) : (Wrappers_Compile.Result.<Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySequence<? extends Character>>create_Success(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())))));
                    if ((_16_valueOrError8).IsFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                      return (_16_valueOrError8).<KeyMaterial>PropagateFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                    } else {
                      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _18_plaintextDataKey = (_16_valueOrError8).Extract(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                      Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _19_valueOrError9 = JSONHelpers_Compile.__default.GetOptionalString(dafny.DafnySequence.asString("signingKey"), obj);
                      if ((_19_valueOrError9).IsFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                        return (_19_valueOrError9).<KeyMaterial>PropagateFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                      } else {
                        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _20_signingKey = (_19_valueOrError9).Extract(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                        Wrappers_Compile.Result<Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>>, dafny.DafnySequence<? extends Character>> _21_valueOrError10 = JSONHelpers_Compile.__default.GetOptionalString(dafny.DafnySequence.asString("verificationKey"), obj);
                        if ((_21_valueOrError10).IsFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                          return (_21_valueOrError10).<KeyMaterial>PropagateFailure(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                        } else {
                          Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _22_verificationKey = (_21_valueOrError10).Extract(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                          Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _23_symmetricSigningKeys = (JSONHelpers_Compile.__default.GetArrayString(dafny.DafnySequence.asString("symmetricSigningKeys"), obj)).ToOption(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                          return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_StaticMaterial(name, _1_algorithmSuite, _5_encryptionContext, _13_encryptedDataKeys, _9_requiredEncryptionContextKeys, _18_plaintextDataKey, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())))));
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<KeyMaterial, dafny.DafnySequence<? extends Character>> ToStaticBranchKey(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends Character> name, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("key-id"), obj);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _1_keyIdentifier = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("branchKeyVersion"), obj);
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends Character> _3_branchKeyVersionEncoded = (_2_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = UTF8.__default.Encode(_3_branchKeyVersionEncoded);
        if ((_4_valueOrError2).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_4_valueOrError2).<KeyMaterial>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
        } else {
          dafny.DafnySequence<? extends java.lang.Byte> _5_branchKeyVersion = (_4_valueOrError2).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("branchKey"), obj);
          if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_6_valueOrError3).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
          } else {
            dafny.DafnySequence<? extends Character> _7_branchKeyEncoded = (_6_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
            Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _8_valueOrError4 = Base64_Compile.__default.Decode(_7_branchKeyEncoded);
            if ((_8_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_8_valueOrError4).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
            } else {
              dafny.DafnySequence<? extends java.lang.Byte> _9_branchKey = (_8_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _10_valueOrError5 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("beaconKey"), obj);
              if ((_10_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                return (_10_valueOrError5).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
              } else {
                dafny.DafnySequence<? extends Character> _11_beaconKeyEncoded = (_10_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _12_valueOrError6 = Base64_Compile.__default.Decode(_11_beaconKeyEncoded);
                if ((_12_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                  return (_12_valueOrError6).<KeyMaterial>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial._typeDescriptor());
                } else {
                  dafny.DafnySequence<? extends java.lang.Byte> _13_beaconKey = (_12_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                  return Wrappers_Compile.Result.<KeyMaterial, dafny.DafnySequence<? extends Character>>create_Success(KeyMaterial._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), KeyMaterial.create_StaticKeyStoreInformation(_1_keyIdentifier, _5_branchKeyVersion, _9_branchKey, _13_beaconKey));
                }
              }
            }
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, dafny.DafnySequence<? extends Character>> ToEncryptedDataKey(dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("keyProviderId"), obj);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _1_keyProviderIdJSON = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("keyProviderInfo"), obj);
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends Character> _3_keyProviderInfoJSON = (_2_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("ciphertext"), obj);
        if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_4_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
        } else {
          dafny.DafnySequence<? extends Character> _5_ciphertextJSON = (_4_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = UTF8.__default.Encode(_1_keyProviderIdJSON);
          if ((_6_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
            return (_6_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
          } else {
            dafny.DafnySequence<? extends java.lang.Byte> _7_keyProviderId = (_6_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
            Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _8_valueOrError4 = Base64_Compile.__default.Decode(_3_keyProviderInfoJSON);
            if ((_8_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
              return (_8_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
            } else {
              dafny.DafnySequence<? extends java.lang.Byte> _9_keyProviderInfo = (_8_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _10_valueOrError5 = Base64_Compile.__default.Decode(_5_ciphertextJSON);
              if ((_10_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
                return (_10_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor());
              } else {
                dafny.DafnySequence<? extends java.lang.Byte> _11_ciphertext = (_10_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, dafny.DafnySequence<? extends Character>>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(_7_keyProviderId, _9_keyProviderInfo, _11_ciphertext));
              }
            }
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, dafny.DafnySequence<? extends Character>> GetAlgorithmSuiteInfo(software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient mpl, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("algorithmSuiteId"), obj);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _1_algorithmSuiteHex = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), HexStrings_Compile.__default.IsLooseHexString(_1_algorithmSuiteHex), dafny.DafnySequence.asString("Not hex encoded binary"));
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _3_binaryId = HexStrings_Compile.__default.FromHexString(_1_algorithmSuiteHex);
        return ((mpl).GetAlgorithmSuiteInfo(_3_binaryId)).<dafny.DafnySequence<? extends Character>>MapFailure(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, dafny.DafnySequence<? extends Character>>>)(_4_algorithmSuiteHex) -> ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.Error, dafny.DafnySequence<? extends Character>>)(_5_e_boxed0) -> {
          software.amazon.cryptography.materialproviders.internaldafny.types.Error _5_e = ((software.amazon.cryptography.materialproviders.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
          return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Invalid Suite:"), _4_algorithmSuiteHex);
        })).apply(_1_algorithmSuiteHex));
      }
    }
  }
  public static boolean KeyMaterialString_q(dafny.DafnySequence<? extends Character> s) {
    return (((((((((s).equals(dafny.DafnySequence.asString("static-material"))) || ((s).equals(dafny.DafnySequence.asString("aws-kms")))) || ((s).equals(dafny.DafnySequence.asString("symmetric")))) || ((s).equals(dafny.DafnySequence.asString("private")))) || ((s).equals(dafny.DafnySequence.asString("public")))) || ((s).equals(dafny.DafnySequence.asString("static-branch-key")))) || ((s).equals(dafny.DafnySequence.asString("aws-kms-rsa")))) || ((s).equals(dafny.DafnySequence.asString("ecc-private")))) || ((s).equals(dafny.DafnySequence.asString("aws-kms-ecdh")));
  }
  @Override
  public java.lang.String toString() {
    return "KeyMaterial._default";
  }
}
