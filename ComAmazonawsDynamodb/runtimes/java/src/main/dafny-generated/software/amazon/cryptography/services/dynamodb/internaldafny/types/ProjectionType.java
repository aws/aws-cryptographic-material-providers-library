// Class ProjectionType
// Dafny class ProjectionType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ProjectionType {
  public ProjectionType() {
  }
  private static final dafny.TypeDescriptor<ProjectionType> _TYPE = dafny.TypeDescriptor.<ProjectionType>referenceWithInitializer(ProjectionType.class, () -> ProjectionType.Default());
  public static dafny.TypeDescriptor<ProjectionType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ProjectionType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ProjectionType theDefault = ProjectionType.create_ALL();
  public static ProjectionType Default() {
    return theDefault;
  }
  public static ProjectionType create_ALL() {
    return new ProjectionType_ALL();
  }
  public static ProjectionType create_KEYS__ONLY() {
    return new ProjectionType_KEYS__ONLY();
  }
  public static ProjectionType create_INCLUDE() {
    return new ProjectionType_INCLUDE();
  }
  public boolean is_ALL() { return this instanceof ProjectionType_ALL; }
  public boolean is_KEYS__ONLY() { return this instanceof ProjectionType_KEYS__ONLY; }
  public boolean is_INCLUDE() { return this instanceof ProjectionType_INCLUDE; }
  public static java.util.ArrayList<ProjectionType> AllSingletonConstructors() {
    java.util.ArrayList<ProjectionType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ProjectionType_ALL());
    singleton_iterator.add(new ProjectionType_KEYS__ONLY());
    singleton_iterator.add(new ProjectionType_INCLUDE());
    return singleton_iterator;
  }
}
