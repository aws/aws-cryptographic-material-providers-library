// Class CreateRawEcdhKeyringInput
// Dafny class CreateRawEcdhKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateRawEcdhKeyringInput {
  public RawEcdhStaticConfigurations _KeyAgreementScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public CreateRawEcdhKeyringInput (RawEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec) {
    this._KeyAgreementScheme = KeyAgreementScheme;
    this._curveSpec = curveSpec;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateRawEcdhKeyringInput o = (CreateRawEcdhKeyringInput)other;
    return true && java.util.Objects.equals(this._KeyAgreementScheme, o._KeyAgreementScheme) && java.util.Objects.equals(this._curveSpec, o._curveSpec);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementScheme);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._curveSpec);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput.CreateRawEcdhKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyAgreementScheme));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._curveSpec));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateRawEcdhKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateRawEcdhKeyringInput>referenceWithInitializer(CreateRawEcdhKeyringInput.class, () -> CreateRawEcdhKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateRawEcdhKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateRawEcdhKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateRawEcdhKeyringInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput.create(RawEcdhStaticConfigurations.Default(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default());
  public static CreateRawEcdhKeyringInput Default() {
    return theDefault;
  }
  public static CreateRawEcdhKeyringInput create(RawEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec) {
    return new CreateRawEcdhKeyringInput(KeyAgreementScheme, curveSpec);
  }
  public static CreateRawEcdhKeyringInput create_CreateRawEcdhKeyringInput(RawEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec) {
    return create(KeyAgreementScheme, curveSpec);
  }
  public boolean is_CreateRawEcdhKeyringInput() { return true; }
  public RawEcdhStaticConfigurations dtor_KeyAgreementScheme() {
    return this._KeyAgreementScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec dtor_curveSpec() {
    return this._curveSpec;
  }
}
