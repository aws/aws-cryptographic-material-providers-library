// Class CreateKeyStoreInput
// Dafny class CreateKeyStoreInput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CreateKeyStoreInput {
  public CreateKeyStoreInput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateKeyStoreInput o = (CreateKeyStoreInput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.CreateKeyStoreInput.CreateKeyStoreInput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateKeyStoreInput> _TYPE = dafny.TypeDescriptor.<CreateKeyStoreInput>referenceWithInitializer(CreateKeyStoreInput.class, () -> CreateKeyStoreInput.Default());
  public static dafny.TypeDescriptor<CreateKeyStoreInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateKeyStoreInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateKeyStoreInput theDefault = software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput.create();
  public static CreateKeyStoreInput Default() {
    return theDefault;
  }
  public static CreateKeyStoreInput create() {
    return new CreateKeyStoreInput();
  }
  public static CreateKeyStoreInput create_CreateKeyStoreInput() {
    return create();
  }
  public boolean is_CreateKeyStoreInput() { return true; }
  public static java.util.ArrayList<CreateKeyStoreInput> AllSingletonConstructors() {
    java.util.ArrayList<CreateKeyStoreInput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CreateKeyStoreInput());
    return singleton_iterator;
  }
}
