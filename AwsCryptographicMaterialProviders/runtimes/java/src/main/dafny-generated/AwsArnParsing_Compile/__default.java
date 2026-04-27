// Class __default
// Dafny class __default compiled into Java
package AwsArnParsing_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean ValidAwsKmsResource(AwsResource resource) {
    return ((resource).Valid()) && ((((resource).dtor_resourceType()).equals(dafny.DafnySequence.asString("key"))) || (((resource).dtor_resourceType()).equals(dafny.DafnySequence.asString("alias"))));
  }
  public static boolean ValidAwsKmsArn(AwsArn arn) {
    return (((arn).Valid()) && (((arn).dtor_service()).equals(dafny.DafnySequence.asString("kms")))) && (__default.ValidAwsKmsResource((arn).dtor_resource()));
  }
  public static Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> ParseAwsKmsRawResources(dafny.DafnySequence<? extends Character> identifier) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _0_info = StandardLibrary_Compile.__default.<Character>Split(dafny.TypeDescriptor.CHAR, identifier, '/');
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), !(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_info).select(0)))).equals(dafny.DafnySequence.asString("key")), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed raw key id: "), identifier));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_1_valueOrError0).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsResource._typeDescriptor());
    } else {
      if (((long) (_0_info).cardinalityInt()) == ((long) 1L)) {
        return __default.ParseAwsKmsResources(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("key/"), identifier));
      } else {
        return __default.ParseAwsKmsResources(identifier);
      }
    }
  }
  public static Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> ParseAwsKmsResources(dafny.DafnySequence<? extends Character> identifier) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _0_info = StandardLibrary_Compile.__default.<Character>Split(dafny.TypeDescriptor.CHAR, identifier, '/');
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), java.lang.Long.compareUnsigned((long) (_0_info).cardinalityInt(), (long) 1L) > 0, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed resource: "), identifier));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_1_valueOrError0).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsResource._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _2_resourceType = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_info).select(0)));
      dafny.DafnySequence<? extends Character> _3_value = StandardLibrary_Compile.__default.<Character>Join(dafny.TypeDescriptor.CHAR, (_0_info).drop(1), dafny.DafnySequence.asString("/"));
      AwsResource _4_resource = AwsResource.create(_2_resourceType, _3_value);
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.ValidAwsKmsResource(_4_resource), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed resource: "), identifier));
      if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_5_valueOrError1).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsResource._typeDescriptor());
      } else {
        return Wrappers_Compile.Result.<AwsResource, dafny.DafnySequence<? extends Character>>create_Success(AwsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _4_resource);
      }
    }
  }
  public static boolean ValidAmazonDynamodbResource(AwsResource resource) {
    return ((resource).Valid()) && (((resource).dtor_resourceType()).equals(dafny.DafnySequence.asString("table")));
  }
  public static boolean ValidAmazonDynamodbArn(AwsArn arn) {
    return (((arn).Valid()) && (((arn).dtor_service()).equals(dafny.DafnySequence.asString("dynamodb")))) && (__default.ValidAmazonDynamodbResource((arn).dtor_resource()));
  }
  public static Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> ParseAmazonDynamodbResources(dafny.DafnySequence<? extends Character> identifier) {
    Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>> _0_info = StandardLibrary_Compile.__default.<Character>SplitOnce_q(dafny.TypeDescriptor.CHAR, identifier, '/');
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_0_info).is_Some(), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed resource: "), identifier));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_1_valueOrError0).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsResource._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _2_resourceType = ((_0_info).dtor_value()).dtor__0();
      dafny.DafnySequence<? extends Character> _3_value = ((_0_info).dtor_value()).dtor__1();
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _4_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName(_3_value), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Table Name invalid: "), identifier));
      if ((_4_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_4_valueOrError1).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsResource._typeDescriptor());
      } else {
        AwsResource _5_resource = AwsResource.create(_2_resourceType, _3_value);
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _6_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.ValidAmazonDynamodbResource(_5_resource), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed resource: "), identifier));
        if ((_6_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_6_valueOrError2).<AwsResource>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsResource._typeDescriptor());
        } else {
          return Wrappers_Compile.Result.<AwsResource, dafny.DafnySequence<? extends Character>>create_Success(AwsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _5_resource);
        }
      }
    }
  }
  public static Wrappers_Compile.Result<AwsArn, dafny.DafnySequence<? extends Character>> ParseAwsKmsArn(dafny.DafnySequence<? extends Character> identifier) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _0_components = StandardLibrary_Compile.__default.<Character>Split(dafny.TypeDescriptor.CHAR, identifier, ':');
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((long) 6L) == ((long) (_0_components).cardinalityInt()), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed arn: "), identifier));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_1_valueOrError0).<AwsArn>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
    } else {
      Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = __default.ParseAwsKmsResources(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(5))));
      if ((_2_valueOrError1).IsFailure(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<AwsArn>PropagateFailure(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
      } else {
        AwsResource _3_resource = (_2_valueOrError1).Extract(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        AwsArn _4_arn = AwsArn.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(0))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(1))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(2))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(3))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(4))), _3_resource);
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.ValidAwsKmsArn(_4_arn), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed Arn:"), identifier));
        if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_5_valueOrError2).<AwsArn>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
        } else {
          return Wrappers_Compile.Result.<AwsArn, dafny.DafnySequence<? extends Character>>create_Success(AwsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _4_arn);
        }
      }
    }
  }
  public static Wrappers_Compile.Result<AwsArn, dafny.DafnySequence<? extends Character>> ParseAmazonDynamodbTableArn(dafny.DafnySequence<? extends Character> identifier) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _0_components = StandardLibrary_Compile.__default.<Character>Split(dafny.TypeDescriptor.CHAR, identifier, ':');
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((long) 6L) == ((long) (_0_components).cardinalityInt()), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed arn: "), identifier));
    if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_1_valueOrError0).<AwsArn>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
    } else {
      Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = __default.ParseAmazonDynamodbResources(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(5))));
      if ((_2_valueOrError1).IsFailure(AmazonDynamodbResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<AwsArn>PropagateFailure(AmazonDynamodbResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
      } else {
        AwsResource _3_resource = (_2_valueOrError1).Extract(AmazonDynamodbResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        AwsArn _4_arn = AwsArn.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(0))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(1))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(2))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(3))), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_0_components).select(4))), _3_resource);
        Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.ValidAmazonDynamodbArn(_4_arn), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Malformed Arn:"), identifier));
        if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          return (_5_valueOrError2).<AwsArn>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArn._typeDescriptor());
        } else {
          return Wrappers_Compile.Result.<AwsArn, dafny.DafnySequence<? extends Character>>create_Success(AwsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _4_arn);
        }
      }
    }
  }
  public static Wrappers_Compile.Result<AwsKmsIdentifier, dafny.DafnySequence<? extends Character>> ParseAwsKmsIdentifier(dafny.DafnySequence<? extends Character> identifier) {
    if ((dafny.DafnySequence.asString("arn:")).isPrefixOf(identifier)) {
      Wrappers_Compile.Result<AwsArn, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.ParseAwsKmsArn(identifier);
      if ((_0_valueOrError0).IsFailure(AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_0_valueOrError0).<AwsKmsIdentifier>PropagateFailure(AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier._typeDescriptor());
      } else {
        AwsArn _1_arn = (_0_valueOrError0).Extract(AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        return Wrappers_Compile.Result.<AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>create_Success(AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier.create_AwsKmsArnIdentifier(_1_arn));
      }
    } else {
      Wrappers_Compile.Result<AwsResource, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = __default.ParseAwsKmsRawResources(identifier);
      if ((_2_valueOrError1).IsFailure(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_2_valueOrError1).<AwsKmsIdentifier>PropagateFailure(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier._typeDescriptor());
      } else {
        AwsResource _3_r = (_2_valueOrError1).Extract(AwsKmsResource._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        return Wrappers_Compile.Result.<AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>create_Success(AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier.create_AwsKmsRawResourceIdentifier(_3_r));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> ParseAmazonDynamodbTableName(dafny.DafnySequence<? extends Character> identifier) {
    Wrappers_Compile.Result<AwsArn, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = __default.ParseAmazonDynamodbTableArn(identifier);
    if ((_0_valueOrError0).IsFailure(AmazonDynamodbTableArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(AmazonDynamodbTableArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      AwsArn _1_arn = (_0_valueOrError0).Extract(AmazonDynamodbTableArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      AmazonDynamodbTableName _2_tableArn = AmazonDynamodbTableName.create(_1_arn);
      dafny.DafnySequence<? extends Character> _3_tableName = (_2_tableArn).GetTableName();
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _3_tableName);
    }
  }
  public static boolean IsMultiRegionAwsKmsArn(AwsArn arn) {
    return __default.IsMultiRegionAwsKmsResource((arn).dtor_resource());
  }
  public static boolean IsMultiRegionAwsKmsIdentifier(AwsKmsIdentifier identifier) {
    AwsKmsIdentifier _source0 = identifier;
    if (_source0.is_AwsKmsArnIdentifier()) {
      AwsArn _0___mcc_h0 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source0)._a;
      AwsArn _1_arn = _0___mcc_h0;
      return __default.IsMultiRegionAwsKmsArn(_1_arn);
    } else {
      AwsResource _2___mcc_h1 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source0)._r;
      AwsResource _3_r = _2___mcc_h1;
      return __default.IsMultiRegionAwsKmsResource(_3_r);
    }
  }
  public static boolean IsMultiRegionAwsKmsResource(AwsResource resource) {
    return (((resource).dtor_resourceType()).equals(dafny.DafnySequence.asString("key"))) && ((dafny.DafnySequence.asString("mrk-")).isPrefixOf((resource).dtor_value()));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GetRegion(AwsKmsIdentifier identifier) {
    AwsKmsIdentifier _source0 = identifier;
    if (_source0.is_AwsKmsArnIdentifier()) {
      AwsArn _0___mcc_h0 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source0)._a;
      AwsArn _1_a = _0___mcc_h0;
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_1_a).dtor_region());
    } else {
      AwsResource _2___mcc_h1 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source0)._r;
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    }
  }
  public static Wrappers_Compile.Result<AwsKmsIdentifier, dafny.DafnySequence<? extends Character>> IsAwsKmsIdentifierString(dafny.DafnySequence<? extends Character> s) {
    Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), UTF8.__default.IsASCIIString(s), dafny.DafnySequence.asString("Not a valid ASCII string."));
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      return (_0_valueOrError0).<AwsKmsIdentifier>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier._typeDescriptor());
    } else {
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _1_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((((long) (s).cardinalityInt()) == 0 ? 0 : 1) == 1) && (java.lang.Long.compareUnsigned((long) (s).cardinalityInt(), __default.MAX__AWS__KMS__IDENTIFIER__LENGTH()) <= 0), dafny.DafnySequence.asString("Identifier exceeds maximum length."));
      if ((_1_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        return (_1_valueOrError1).<AwsKmsIdentifier>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsKmsIdentifier._typeDescriptor());
      } else {
        return __default.ParseAwsKmsIdentifier(s);
      }
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Error Error(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(s);
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateDdbTableArn(dafny.DafnySequence<? extends Character> tableArn) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = (__default.ParseAmazonDynamodbTableName(tableArn)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableName._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default::Error);
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableName._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableName._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends Character> _1___v1 = (_0_valueOrError0).Extract(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableName._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.__default.IsASCIIString(tableArn), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Table Arn is not ASCII")));
      if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        return (_2_valueOrError1).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
      } else {
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableName((__default.ParseAmazonDynamodbTableName(tableArn)).dtor_value()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Table Name is too long")));
        if ((_3_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          return (_3_valueOrError2).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
        } else {
          return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
        }
      }
    }
  }
  public static long MAX__AWS__KMS__IDENTIFIER__LENGTH()
  {
    return (long) 2048L;
  }
  @Override
  public java.lang.String toString() {
    return "AwsArnParsing._default";
  }
}
