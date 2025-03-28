// Class PaddingScheme_PKCS1
// Dafny class PaddingScheme_PKCS1 compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class PaddingScheme_PKCS1 extends PaddingScheme {
  public PaddingScheme_PKCS1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PaddingScheme_PKCS1 o = (PaddingScheme_PKCS1)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.PaddingScheme.PKCS1");
    return s.toString();
  }
}
