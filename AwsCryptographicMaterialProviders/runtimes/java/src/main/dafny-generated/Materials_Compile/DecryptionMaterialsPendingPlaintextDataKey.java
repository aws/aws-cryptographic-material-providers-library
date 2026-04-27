// Class DecryptionMaterialsPendingPlaintextDataKey
// Dafny class DecryptionMaterialsPendingPlaintextDataKey compiled into Java
package Materials_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptionMaterialsPendingPlaintextDataKey {
  public DecryptionMaterialsPendingPlaintextDataKey() {
  }
  public static boolean _Is(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials __source) {
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_d = __source;
    return __default.DecryptionMaterialsWithoutPlaintextDataKey(_0_d);
  }
  private static final dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> _TYPE = dafny.TypeDescriptor.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>referenceWithInitializer(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.class, () -> software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.Default());
  public static dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
