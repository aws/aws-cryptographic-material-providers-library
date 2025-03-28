// Class GetBeaconKeyOutput
// Dafny class GetBeaconKeyOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetBeaconKeyOutput {
  public BeaconKeyMaterials _beaconKeyMaterials;
  public GetBeaconKeyOutput (BeaconKeyMaterials beaconKeyMaterials) {
    this._beaconKeyMaterials = beaconKeyMaterials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBeaconKeyOutput o = (GetBeaconKeyOutput)other;
    return true && java.util.Objects.equals(this._beaconKeyMaterials, o._beaconKeyMaterials);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._beaconKeyMaterials);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.GetBeaconKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._beaconKeyMaterials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBeaconKeyOutput> _TYPE = dafny.TypeDescriptor.<GetBeaconKeyOutput>referenceWithInitializer(GetBeaconKeyOutput.class, () -> GetBeaconKeyOutput.Default());
  public static dafny.TypeDescriptor<GetBeaconKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBeaconKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBeaconKeyOutput theDefault = software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput.create(BeaconKeyMaterials.Default());
  public static GetBeaconKeyOutput Default() {
    return theDefault;
  }
  public static GetBeaconKeyOutput create(BeaconKeyMaterials beaconKeyMaterials) {
    return new GetBeaconKeyOutput(beaconKeyMaterials);
  }
  public static GetBeaconKeyOutput create_GetBeaconKeyOutput(BeaconKeyMaterials beaconKeyMaterials) {
    return create(beaconKeyMaterials);
  }
  public boolean is_GetBeaconKeyOutput() { return true; }
  public BeaconKeyMaterials dtor_beaconKeyMaterials() {
    return this._beaconKeyMaterials;
  }
}
