// Class TimeUnits_Seconds
// Dafny class TimeUnits_Seconds compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TimeUnits_Seconds extends TimeUnits {
  public TimeUnits_Seconds () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TimeUnits_Seconds o = (TimeUnits_Seconds)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.TimeUnits.Seconds");
    return s.toString();
  }
}
