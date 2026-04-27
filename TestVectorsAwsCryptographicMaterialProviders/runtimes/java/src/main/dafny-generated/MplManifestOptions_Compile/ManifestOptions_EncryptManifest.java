// Class ManifestOptions_EncryptManifest
// Dafny class ManifestOptions_EncryptManifest compiled into Java
package MplManifestOptions_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class ManifestOptions_EncryptManifest extends ManifestOptions {
  public dafny.DafnySequence<? extends Character> _encryptManifestOutput;
  public ManifestOptions_EncryptManifest (dafny.DafnySequence<? extends Character> encryptManifestOutput) {
    super();
    this._encryptManifestOutput = encryptManifestOutput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ManifestOptions_EncryptManifest o = (ManifestOptions_EncryptManifest)other;
    return true && java.util.Objects.equals(this._encryptManifestOutput, o._encryptManifestOutput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptManifestOutput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MplManifestOptions.ManifestOptions.EncryptManifest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encryptManifestOutput));
    s.append(")");
    return s.toString();
  }
}
