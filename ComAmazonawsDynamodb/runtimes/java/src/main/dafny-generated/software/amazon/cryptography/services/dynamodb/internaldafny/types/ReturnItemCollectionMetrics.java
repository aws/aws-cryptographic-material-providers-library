// Class ReturnItemCollectionMetrics
// Dafny class ReturnItemCollectionMetrics compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ReturnItemCollectionMetrics {
  public ReturnItemCollectionMetrics() {
  }
  private static final dafny.TypeDescriptor<ReturnItemCollectionMetrics> _TYPE = dafny.TypeDescriptor.<ReturnItemCollectionMetrics>referenceWithInitializer(ReturnItemCollectionMetrics.class, () -> ReturnItemCollectionMetrics.Default());
  public static dafny.TypeDescriptor<ReturnItemCollectionMetrics> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReturnItemCollectionMetrics>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReturnItemCollectionMetrics theDefault = ReturnItemCollectionMetrics.create_SIZE();
  public static ReturnItemCollectionMetrics Default() {
    return theDefault;
  }
  public static ReturnItemCollectionMetrics create_SIZE() {
    return new ReturnItemCollectionMetrics_SIZE();
  }
  public static ReturnItemCollectionMetrics create_NONE() {
    return new ReturnItemCollectionMetrics_NONE();
  }
  public boolean is_SIZE() { return this instanceof ReturnItemCollectionMetrics_SIZE; }
  public boolean is_NONE() { return this instanceof ReturnItemCollectionMetrics_NONE; }
  public static java.util.ArrayList<ReturnItemCollectionMetrics> AllSingletonConstructors() {
    java.util.ArrayList<ReturnItemCollectionMetrics> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ReturnItemCollectionMetrics_SIZE());
    singleton_iterator.add(new ReturnItemCollectionMetrics_NONE());
    return singleton_iterator;
  }
}
