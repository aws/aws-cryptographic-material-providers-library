// Class MaterialProvidersConfig
// Dafny class MaterialProvidersConfig compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class MaterialProvidersConfig {
  public MaterialProvidersConfig () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MaterialProvidersConfig o = (MaterialProvidersConfig)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig.MaterialProvidersConfig");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MaterialProvidersConfig> _TYPE = dafny.TypeDescriptor.<MaterialProvidersConfig>referenceWithInitializer(MaterialProvidersConfig.class, () -> MaterialProvidersConfig.Default());
  public static dafny.TypeDescriptor<MaterialProvidersConfig> _typeDescriptor() {
    return (dafny.TypeDescriptor<MaterialProvidersConfig>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MaterialProvidersConfig theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig.create();
  public static MaterialProvidersConfig Default() {
    return theDefault;
  }
  public static MaterialProvidersConfig create() {
    return new MaterialProvidersConfig();
  }
  public static MaterialProvidersConfig create_MaterialProvidersConfig() {
    return create();
  }
  public boolean is_MaterialProvidersConfig() { return true; }
  public static java.util.ArrayList<MaterialProvidersConfig> AllSingletonConstructors() {
    java.util.ArrayList<MaterialProvidersConfig> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new MaterialProvidersConfig());
    return singleton_iterator;
  }
}
