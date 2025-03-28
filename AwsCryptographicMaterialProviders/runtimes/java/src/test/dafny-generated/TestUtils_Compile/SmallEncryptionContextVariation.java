// Class SmallEncryptionContextVariation
// Dafny class SmallEncryptionContextVariation compiled into Java
package TestUtils_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SmallEncryptionContextVariation {
  public SmallEncryptionContextVariation() {
  }
  private static final dafny.TypeDescriptor<SmallEncryptionContextVariation> _TYPE = dafny.TypeDescriptor.<SmallEncryptionContextVariation>referenceWithInitializer(SmallEncryptionContextVariation.class, () -> SmallEncryptionContextVariation.Default());
  public static dafny.TypeDescriptor<SmallEncryptionContextVariation> _typeDescriptor() {
    return (dafny.TypeDescriptor<SmallEncryptionContextVariation>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SmallEncryptionContextVariation theDefault = TestUtils_Compile.SmallEncryptionContextVariation.create_Empty();
  public static SmallEncryptionContextVariation Default() {
    return theDefault;
  }
  public static SmallEncryptionContextVariation create_Empty() {
    return new SmallEncryptionContextVariation_Empty();
  }
  public static SmallEncryptionContextVariation create_A() {
    return new SmallEncryptionContextVariation_A();
  }
  public static SmallEncryptionContextVariation create_AB() {
    return new SmallEncryptionContextVariation_AB();
  }
  public static SmallEncryptionContextVariation create_BA() {
    return new SmallEncryptionContextVariation_BA();
  }
  public boolean is_Empty() { return this instanceof SmallEncryptionContextVariation_Empty; }
  public boolean is_A() { return this instanceof SmallEncryptionContextVariation_A; }
  public boolean is_AB() { return this instanceof SmallEncryptionContextVariation_AB; }
  public boolean is_BA() { return this instanceof SmallEncryptionContextVariation_BA; }
  public static java.util.ArrayList<SmallEncryptionContextVariation> AllSingletonConstructors() {
    java.util.ArrayList<SmallEncryptionContextVariation> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new SmallEncryptionContextVariation_Empty());
    singleton_iterator.add(new SmallEncryptionContextVariation_A());
    singleton_iterator.add(new SmallEncryptionContextVariation_AB());
    singleton_iterator.add(new SmallEncryptionContextVariation_BA());
    return singleton_iterator;
  }
}
