// Class __default
// Dafny class __default compiled into Java
package CreateKeyStoreTable_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean keyStoreHasExpectedConstruction_q(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription t) {
    return (((((((t).dtor_AttributeDefinitions()).is_Some()) && (((t).dtor_KeySchema()).is_Some())) && (((t).dtor_TableName()).is_Some())) && (((t).dtor_TableArn()).is_Some())) && ((Seq_Compile.__default.<software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition>ToSet(software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition._typeDescriptor(), __default.ATTRIBUTE__DEFINITIONS())).isSubsetOf(Seq_Compile.__default.<software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition>ToSet(software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition._typeDescriptor(), ((t).dtor_AttributeDefinitions()).dtor_value())))) && ((Seq_Compile.__default.<software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement>ToSet(software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement._typeDescriptor(), __default.KEY__SCHEMA())).isSubsetOf(Seq_Compile.__default.<software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement>ToSet(software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement._typeDescriptor(), ((t).dtor_KeySchema()).dtor_value())));
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> CreateKeyStoreTable(dafny.DafnySequence<? extends Character> tableName, software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ddbClient)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableOutput, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _0_maybeDescribeTableResponse;
      Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableOutput, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out0;
      _out0 = (ddbClient).DescribeTable(software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableInput.create(tableName));
      _0_maybeDescribeTableResponse = _out0;
      if ((_0_maybeDescribeTableResponse).is_Failure()) {
        software.amazon.cryptography.services.dynamodb.internaldafny.types.Error _1_error;
        _1_error = (_0_maybeDescribeTableResponse).dtor_error();
        if ((_1_error).is_ResourceNotFoundException()) {
          Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableOutput, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _2_maybeCreateTableResponse;
          Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableOutput, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> _out1;
          _out1 = (ddbClient).CreateTable(software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableInput.create(__default.ATTRIBUTE__DEFINITIONS(), tableName, __default.KEY__SCHEMA(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndex>>create_None(dafny.DafnySequence.<software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndex>_typeDescriptor(software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndex>>create_None(dafny.DafnySequence.<software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndex>_typeDescriptor(software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode>create_Some(software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode.create_PAY__PER__REQUEST()), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughput>create_None(software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamSpecification>create_None(software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamSpecification._typeDescriptor()), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.SSESpecification>create_None(software.amazon.cryptography.services.dynamodb.internaldafny.types.SSESpecification._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.Tag>>create_None(dafny.DafnySequence.<software.amazon.cryptography.services.dynamodb.internaldafny.types.Tag>_typeDescriptor(software.amazon.cryptography.services.dynamodb.internaldafny.types.Tag._typeDescriptor())), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClass>create_None(software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClass._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<software.amazon.cryptography.services.dynamodb.internaldafny.types.OnDemandThroughput>create_None(software.amazon.cryptography.services.dynamodb.internaldafny.types.OnDemandThroughput._typeDescriptor())));
          _2_maybeCreateTableResponse = _out1;
          if ((_2_maybeCreateTableResponse).is_Failure()) {
            res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsDynamodb((_2_maybeCreateTableResponse).dtor_error()));
          } else {
            Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
            _3_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((((_2_maybeCreateTableResponse).dtor_value()).dtor_TableDescription()).is_Some()) && (__default.keyStoreHasExpectedConstruction_q((((_2_maybeCreateTableResponse).dtor_value()).dtor_TableDescription()).dtor_value()))) && (software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableArn((((((_2_maybeCreateTableResponse).dtor_value()).dtor_TableDescription()).dtor_value()).dtor_TableArn()).dtor_value())), __default.E(dafny.DafnySequence.asString("Configured table name does not conform to expected Key Store construction.")));
            if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
              res = (_3_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              return res;
            }
            res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((((_2_maybeCreateTableResponse).dtor_value()).dtor_TableDescription()).dtor_value()).dtor_TableArn()).dtor_value());
          }
        } else {
          res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsDynamodb(_1_error));
        }
      } else {
        Wrappers_Compile.Outcome<software.amazon.cryptography.keystore.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.keystore.internaldafny.types.Error>Default(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor());
        _4_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.keystore.internaldafny.types.Error>Need(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((((_0_maybeDescribeTableResponse).dtor_value()).dtor_Table()).is_Some()) && (__default.keyStoreHasExpectedConstruction_q((((_0_maybeDescribeTableResponse).dtor_value()).dtor_Table()).dtor_value()))) && (software.amazon.cryptography.services.dynamodb.internaldafny.types.__default.IsValid__TableArn((((((_0_maybeDescribeTableResponse).dtor_value()).dtor_Table()).dtor_value()).dtor_TableArn()).dtor_value())), __default.E(dafny.DafnySequence.asString("Configured table name does not conform to expected Key Store construction.")));
        if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor())) {
          res = (_4_valueOrError1).<dafny.DafnySequence<? extends Character>>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          return res;
        }
        res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.keystore.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), (((((_0_maybeDescribeTableResponse).dtor_value()).dtor_Table()).dtor_value()).dtor_TableArn()).dtor_value());
      }
    }
    return res;
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.Error E(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.keystore.internaldafny.types.Error.create_KeyStoreException(s);
  }
  public static dafny.DafnySequence<? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition> ATTRIBUTE__DEFINITIONS()
  {
    return dafny.DafnySequence.<software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition> of(software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition.create(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD(), software.amazon.cryptography.services.dynamodb.internaldafny.types.ScalarAttributeType.create_S()), software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition.create(Structure_Compile.__default.TYPE__FIELD(), software.amazon.cryptography.services.dynamodb.internaldafny.types.ScalarAttributeType.create_S()));
  }
  public static dafny.DafnySequence<? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement> KEY__SCHEMA()
  {
    return dafny.DafnySequence.<software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement> of(software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement._typeDescriptor(), software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement.create(Structure_Compile.__default.BRANCH__KEY__IDENTIFIER__FIELD(), software.amazon.cryptography.services.dynamodb.internaldafny.types.KeyType.create_HASH()), software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement.create(Structure_Compile.__default.TYPE__FIELD(), software.amazon.cryptography.services.dynamodb.internaldafny.types.KeyType.create_RANGE()));
  }
  @Override
  public java.lang.String toString() {
    return "CreateKeyStoreTable._default";
  }
}
