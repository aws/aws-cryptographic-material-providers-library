// Class CacheType_StormTracking
// Dafny class CacheType_StormTracking compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_StormTracking extends CacheType {
  public StormTrackingCache _StormTracking;
  public CacheType_StormTracking (StormTrackingCache StormTracking) {
    super();
    this._StormTracking = StormTracking;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_StormTracking o = (CacheType_StormTracking)other;
    return true && java.util.Objects.equals(this._StormTracking, o._StormTracking);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StormTracking);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.StormTracking");
    s.append("(");
    s.append(dafny.Helpers.toString(this._StormTracking));
    s.append(")");
    return s.toString();
  }
}
