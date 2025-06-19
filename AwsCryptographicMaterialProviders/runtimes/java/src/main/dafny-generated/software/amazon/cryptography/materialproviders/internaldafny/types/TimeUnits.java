// Class TimeUnits
// Dafny class TimeUnits compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class TimeUnits {
  public TimeUnits() {
  }
  private static final dafny.TypeDescriptor<TimeUnits> _TYPE = dafny.TypeDescriptor.<TimeUnits>referenceWithInitializer(TimeUnits.class, () -> TimeUnits.Default());
  public static dafny.TypeDescriptor<TimeUnits> _typeDescriptor() {
    return (dafny.TypeDescriptor<TimeUnits>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TimeUnits theDefault = TimeUnits.create_Seconds();
  public static TimeUnits Default() {
    return theDefault;
  }
  public static TimeUnits create_Seconds() {
    return new TimeUnits_Seconds();
  }
  public static TimeUnits create_Milliseconds() {
    return new TimeUnits_Milliseconds();
  }
  public boolean is_Seconds() { return this instanceof TimeUnits_Seconds; }
  public boolean is_Milliseconds() { return this instanceof TimeUnits_Milliseconds; }
  public static java.util.ArrayList<TimeUnits> AllSingletonConstructors() {
    java.util.ArrayList<TimeUnits> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new TimeUnits_Seconds());
    singleton_iterator.add(new TimeUnits_Milliseconds());
    return singleton_iterator;
  }
}
