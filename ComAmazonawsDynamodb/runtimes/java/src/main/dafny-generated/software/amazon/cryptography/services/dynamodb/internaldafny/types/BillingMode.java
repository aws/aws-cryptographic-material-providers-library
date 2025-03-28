// Class BillingMode
// Dafny class BillingMode compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class BillingMode {
  public BillingMode() {
  }
  private static final dafny.TypeDescriptor<BillingMode> _TYPE = dafny.TypeDescriptor.<BillingMode>referenceWithInitializer(BillingMode.class, () -> BillingMode.Default());
  public static dafny.TypeDescriptor<BillingMode> _typeDescriptor() {
    return (dafny.TypeDescriptor<BillingMode>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BillingMode theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode.create_PROVISIONED();
  public static BillingMode Default() {
    return theDefault;
  }
  public static BillingMode create_PROVISIONED() {
    return new BillingMode_PROVISIONED();
  }
  public static BillingMode create_PAY__PER__REQUEST() {
    return new BillingMode_PAY__PER__REQUEST();
  }
  public boolean is_PROVISIONED() { return this instanceof BillingMode_PROVISIONED; }
  public boolean is_PAY__PER__REQUEST() { return this instanceof BillingMode_PAY__PER__REQUEST; }
  public static java.util.ArrayList<BillingMode> AllSingletonConstructors() {
    java.util.ArrayList<BillingMode> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new BillingMode_PROVISIONED());
    singleton_iterator.add(new BillingMode_PAY__PER__REQUEST());
    return singleton_iterator;
  }
}
