// Class CreateDefaultClientSupplierInput
// Dafny class CreateDefaultClientSupplierInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateDefaultClientSupplierInput {
  public CreateDefaultClientSupplierInput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateDefaultClientSupplierInput o = (CreateDefaultClientSupplierInput)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput.CreateDefaultClientSupplierInput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateDefaultClientSupplierInput> _TYPE = dafny.TypeDescriptor.<CreateDefaultClientSupplierInput>referenceWithInitializer(CreateDefaultClientSupplierInput.class, () -> CreateDefaultClientSupplierInput.Default());
  public static dafny.TypeDescriptor<CreateDefaultClientSupplierInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateDefaultClientSupplierInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateDefaultClientSupplierInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create();
  public static CreateDefaultClientSupplierInput Default() {
    return theDefault;
  }
  public static CreateDefaultClientSupplierInput create() {
    return new CreateDefaultClientSupplierInput();
  }
  public static CreateDefaultClientSupplierInput create_CreateDefaultClientSupplierInput() {
    return create();
  }
  public boolean is_CreateDefaultClientSupplierInput() { return true; }
  public static java.util.ArrayList<CreateDefaultClientSupplierInput> AllSingletonConstructors() {
    java.util.ArrayList<CreateDefaultClientSupplierInput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CreateDefaultClientSupplierInput());
    return singleton_iterator;
  }
}
