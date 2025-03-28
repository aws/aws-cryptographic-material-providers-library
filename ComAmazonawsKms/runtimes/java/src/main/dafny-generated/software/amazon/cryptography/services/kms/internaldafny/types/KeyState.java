// Class KeyState
// Dafny class KeyState compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyState {
  public KeyState() {
  }
  private static final dafny.TypeDescriptor<KeyState> _TYPE = dafny.TypeDescriptor.<KeyState>referenceWithInitializer(KeyState.class, () -> KeyState.Default());
  public static dafny.TypeDescriptor<KeyState> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyState>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyState theDefault = software.amazon.cryptography.services.kms.internaldafny.types.KeyState.create_Creating();
  public static KeyState Default() {
    return theDefault;
  }
  public static KeyState create_Creating() {
    return new KeyState_Creating();
  }
  public static KeyState create_Enabled() {
    return new KeyState_Enabled();
  }
  public static KeyState create_Disabled() {
    return new KeyState_Disabled();
  }
  public static KeyState create_PendingDeletion() {
    return new KeyState_PendingDeletion();
  }
  public static KeyState create_PendingImport() {
    return new KeyState_PendingImport();
  }
  public static KeyState create_PendingReplicaDeletion() {
    return new KeyState_PendingReplicaDeletion();
  }
  public static KeyState create_Unavailable() {
    return new KeyState_Unavailable();
  }
  public static KeyState create_Updating() {
    return new KeyState_Updating();
  }
  public boolean is_Creating() { return this instanceof KeyState_Creating; }
  public boolean is_Enabled() { return this instanceof KeyState_Enabled; }
  public boolean is_Disabled() { return this instanceof KeyState_Disabled; }
  public boolean is_PendingDeletion() { return this instanceof KeyState_PendingDeletion; }
  public boolean is_PendingImport() { return this instanceof KeyState_PendingImport; }
  public boolean is_PendingReplicaDeletion() { return this instanceof KeyState_PendingReplicaDeletion; }
  public boolean is_Unavailable() { return this instanceof KeyState_Unavailable; }
  public boolean is_Updating() { return this instanceof KeyState_Updating; }
  public static java.util.ArrayList<KeyState> AllSingletonConstructors() {
    java.util.ArrayList<KeyState> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyState_Creating());
    singleton_iterator.add(new KeyState_Enabled());
    singleton_iterator.add(new KeyState_Disabled());
    singleton_iterator.add(new KeyState_PendingDeletion());
    singleton_iterator.add(new KeyState_PendingImport());
    singleton_iterator.add(new KeyState_PendingReplicaDeletion());
    singleton_iterator.add(new KeyState_Unavailable());
    singleton_iterator.add(new KeyState_Updating());
    return singleton_iterator;
  }
}
