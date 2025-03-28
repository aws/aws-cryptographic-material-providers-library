// Class None
// Dafny class None compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class None {
  public None () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    None o = (None)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.None.None");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<None> _TYPE = dafny.TypeDescriptor.<None>referenceWithInitializer(None.class, () -> None.Default());
  public static dafny.TypeDescriptor<None> _typeDescriptor() {
    return (dafny.TypeDescriptor<None>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final None theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.None.create();
  public static None Default() {
    return theDefault;
  }
  public static None create() {
    return new None();
  }
  public static None create_None() {
    return create();
  }
  public boolean is_None() { return true; }
  public static java.util.ArrayList<None> AllSingletonConstructors() {
    java.util.ArrayList<None> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new None());
    return singleton_iterator;
  }
}
