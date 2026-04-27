// Class ReplicaStatus
// Dafny class ReplicaStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ReplicaStatus {
  public ReplicaStatus() {
  }
  private static final dafny.TypeDescriptor<ReplicaStatus> _TYPE = dafny.TypeDescriptor.<ReplicaStatus>referenceWithInitializer(ReplicaStatus.class, () -> ReplicaStatus.Default());
  public static dafny.TypeDescriptor<ReplicaStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaStatus theDefault = ReplicaStatus.create_CREATING();
  public static ReplicaStatus Default() {
    return theDefault;
  }
  public static ReplicaStatus create_CREATING() {
    return new ReplicaStatus_CREATING();
  }
  public static ReplicaStatus create_CREATION__FAILED() {
    return new ReplicaStatus_CREATION__FAILED();
  }
  public static ReplicaStatus create_UPDATING() {
    return new ReplicaStatus_UPDATING();
  }
  public static ReplicaStatus create_DELETING() {
    return new ReplicaStatus_DELETING();
  }
  public static ReplicaStatus create_ACTIVE() {
    return new ReplicaStatus_ACTIVE();
  }
  public static ReplicaStatus create_REGION__DISABLED() {
    return new ReplicaStatus_REGION__DISABLED();
  }
  public static ReplicaStatus create_INACCESSIBLE__ENCRYPTION__CREDENTIALS() {
    return new ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS();
  }
  public boolean is_CREATING() { return this instanceof ReplicaStatus_CREATING; }
  public boolean is_CREATION__FAILED() { return this instanceof ReplicaStatus_CREATION__FAILED; }
  public boolean is_UPDATING() { return this instanceof ReplicaStatus_UPDATING; }
  public boolean is_DELETING() { return this instanceof ReplicaStatus_DELETING; }
  public boolean is_ACTIVE() { return this instanceof ReplicaStatus_ACTIVE; }
  public boolean is_REGION__DISABLED() { return this instanceof ReplicaStatus_REGION__DISABLED; }
  public boolean is_INACCESSIBLE__ENCRYPTION__CREDENTIALS() { return this instanceof ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS; }
  public static java.util.ArrayList<ReplicaStatus> AllSingletonConstructors() {
    java.util.ArrayList<ReplicaStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ReplicaStatus_CREATING());
    singleton_iterator.add(new ReplicaStatus_CREATION__FAILED());
    singleton_iterator.add(new ReplicaStatus_UPDATING());
    singleton_iterator.add(new ReplicaStatus_DELETING());
    singleton_iterator.add(new ReplicaStatus_ACTIVE());
    singleton_iterator.add(new ReplicaStatus_REGION__DISABLED());
    singleton_iterator.add(new ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS());
    return singleton_iterator;
  }
}
