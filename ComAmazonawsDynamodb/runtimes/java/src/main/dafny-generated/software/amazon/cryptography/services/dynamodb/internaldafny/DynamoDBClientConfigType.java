// Class DynamoDBClientConfigType
// Dafny class DynamoDBClientConfigType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny;

import software.amazon.cryptography.services.dynamodb.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DynamoDBClientConfigType {
  public DynamoDBClientConfigType () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DynamoDBClientConfigType o = (DynamoDBClientConfigType)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Dynamodb.DynamoDBClientConfigType.DynamoDBClientConfigType");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DynamoDBClientConfigType> _TYPE = dafny.TypeDescriptor.<DynamoDBClientConfigType>referenceWithInitializer(DynamoDBClientConfigType.class, () -> DynamoDBClientConfigType.Default());
  public static dafny.TypeDescriptor<DynamoDBClientConfigType> _typeDescriptor() {
    return (dafny.TypeDescriptor<DynamoDBClientConfigType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DynamoDBClientConfigType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.DynamoDBClientConfigType.create();
  public static DynamoDBClientConfigType Default() {
    return theDefault;
  }
  public static DynamoDBClientConfigType create() {
    return new DynamoDBClientConfigType();
  }
  public static DynamoDBClientConfigType create_DynamoDBClientConfigType() {
    return create();
  }
  public boolean is_DynamoDBClientConfigType() { return true; }
  public static java.util.ArrayList<DynamoDBClientConfigType> AllSingletonConstructors() {
    java.util.ArrayList<DynamoDBClientConfigType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DynamoDBClientConfigType());
    return singleton_iterator;
  }
}
