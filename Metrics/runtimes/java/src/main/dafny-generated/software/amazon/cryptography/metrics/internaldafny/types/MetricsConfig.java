// Class MetricsConfig
// Dafny class MetricsConfig compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class MetricsConfig {
  public MetricsConfig () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MetricsConfig o = (MetricsConfig)other;
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
    s.append("AwsCryptographyMetricsTypes.MetricsConfig.MetricsConfig");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MetricsConfig> _TYPE = dafny.TypeDescriptor.<MetricsConfig>referenceWithInitializer(MetricsConfig.class, () -> MetricsConfig.Default());
  public static dafny.TypeDescriptor<MetricsConfig> _typeDescriptor() {
    return (dafny.TypeDescriptor<MetricsConfig>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MetricsConfig theDefault = software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig.create();
  public static MetricsConfig Default() {
    return theDefault;
  }
  public static MetricsConfig create() {
    return new MetricsConfig();
  }
  public static MetricsConfig create_MetricsConfig() {
    return create();
  }
  public boolean is_MetricsConfig() { return true; }
  public static java.util.ArrayList<MetricsConfig> AllSingletonConstructors() {
    java.util.ArrayList<MetricsConfig> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new MetricsConfig());
    return singleton_iterator;
  }
}
