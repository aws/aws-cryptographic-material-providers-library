// Class ContributorInsightsAction
// Dafny class ContributorInsightsAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ContributorInsightsAction {
  public ContributorInsightsAction() {
  }
  private static final dafny.TypeDescriptor<ContributorInsightsAction> _TYPE = dafny.TypeDescriptor.<ContributorInsightsAction>referenceWithInitializer(ContributorInsightsAction.class, () -> ContributorInsightsAction.Default());
  public static dafny.TypeDescriptor<ContributorInsightsAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<ContributorInsightsAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ContributorInsightsAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsAction.create_ENABLE();
  public static ContributorInsightsAction Default() {
    return theDefault;
  }
  public static ContributorInsightsAction create_ENABLE() {
    return new ContributorInsightsAction_ENABLE();
  }
  public static ContributorInsightsAction create_DISABLE() {
    return new ContributorInsightsAction_DISABLE();
  }
  public boolean is_ENABLE() { return this instanceof ContributorInsightsAction_ENABLE; }
  public boolean is_DISABLE() { return this instanceof ContributorInsightsAction_DISABLE; }
  public static java.util.ArrayList<ContributorInsightsAction> AllSingletonConstructors() {
    java.util.ArrayList<ContributorInsightsAction> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ContributorInsightsAction_ENABLE());
    singleton_iterator.add(new ContributorInsightsAction_DISABLE());
    return singleton_iterator;
  }
}
