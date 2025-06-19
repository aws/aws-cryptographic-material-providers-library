// Class ContributorInsightsStatus
// Dafny class ContributorInsightsStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ContributorInsightsStatus {
  public ContributorInsightsStatus() {
  }
  private static final dafny.TypeDescriptor<ContributorInsightsStatus> _TYPE = dafny.TypeDescriptor.<ContributorInsightsStatus>referenceWithInitializer(ContributorInsightsStatus.class, () -> ContributorInsightsStatus.Default());
  public static dafny.TypeDescriptor<ContributorInsightsStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<ContributorInsightsStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ContributorInsightsStatus theDefault = ContributorInsightsStatus.create_ENABLING();
  public static ContributorInsightsStatus Default() {
    return theDefault;
  }
  public static ContributorInsightsStatus create_ENABLING() {
    return new ContributorInsightsStatus_ENABLING();
  }
  public static ContributorInsightsStatus create_ENABLED() {
    return new ContributorInsightsStatus_ENABLED();
  }
  public static ContributorInsightsStatus create_DISABLING() {
    return new ContributorInsightsStatus_DISABLING();
  }
  public static ContributorInsightsStatus create_DISABLED() {
    return new ContributorInsightsStatus_DISABLED();
  }
  public static ContributorInsightsStatus create_FAILED() {
    return new ContributorInsightsStatus_FAILED();
  }
  public boolean is_ENABLING() { return this instanceof ContributorInsightsStatus_ENABLING; }
  public boolean is_ENABLED() { return this instanceof ContributorInsightsStatus_ENABLED; }
  public boolean is_DISABLING() { return this instanceof ContributorInsightsStatus_DISABLING; }
  public boolean is_DISABLED() { return this instanceof ContributorInsightsStatus_DISABLED; }
  public boolean is_FAILED() { return this instanceof ContributorInsightsStatus_FAILED; }
  public static java.util.ArrayList<ContributorInsightsStatus> AllSingletonConstructors() {
    java.util.ArrayList<ContributorInsightsStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ContributorInsightsStatus_ENABLING());
    singleton_iterator.add(new ContributorInsightsStatus_ENABLED());
    singleton_iterator.add(new ContributorInsightsStatus_DISABLING());
    singleton_iterator.add(new ContributorInsightsStatus_DISABLED());
    singleton_iterator.add(new ContributorInsightsStatus_FAILED());
    return singleton_iterator;
  }
}
