// Class ListContributorInsightsLimit
// Dafny class ListContributorInsightsLimit compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListContributorInsightsLimit {
  public ListContributorInsightsLimit() {
  }
  public static boolean _Is(int __source) {
    int _14_x = (__source);
    if (true) {
      return __default.IsValid__ListContributorInsightsLimit(_14_x);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
