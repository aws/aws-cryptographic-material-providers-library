// Class ManifestOptions_Encrypt
// Dafny class ManifestOptions_Encrypt compiled into Java
package MplManifestOptions_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class ManifestOptions_Encrypt extends ManifestOptions {
  public dafny.DafnySequence<? extends Character> _manifestPath;
  public dafny.DafnySequence<? extends Character> _decryptManifestOutput;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _testName;
  public ManifestOptions_Encrypt (dafny.DafnySequence<? extends Character> manifestPath, dafny.DafnySequence<? extends Character> decryptManifestOutput, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> testName) {
    super();
    this._manifestPath = manifestPath;
    this._decryptManifestOutput = decryptManifestOutput;
    this._testName = testName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ManifestOptions_Encrypt o = (ManifestOptions_Encrypt)other;
    return true && java.util.Objects.equals(this._manifestPath, o._manifestPath) && java.util.Objects.equals(this._decryptManifestOutput, o._decryptManifestOutput) && java.util.Objects.equals(this._testName, o._testName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._manifestPath);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._decryptManifestOutput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._testName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MplManifestOptions.ManifestOptions.Encrypt");
    s.append("(");
    s.append(dafny.Helpers.toString(this._manifestPath));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._decryptManifestOutput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._testName));
    s.append(")");
    return s.toString();
  }
}
