// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny;

import software.amazon.cryptography.services.dynamodb.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static DynamoDBClientConfigType DefaultDynamoDBClientConfigType() {
    return software.amazon.cryptography.services.dynamodb.internaldafny.DynamoDBClientConfigType.create();
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.services.dynamodb.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient, software.amazon.cryptography.services.dynamodb.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient.class)), software.amazon.cryptography.services.dynamodb.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "Com.Amazonaws.Dynamodb._default";
  }
}
