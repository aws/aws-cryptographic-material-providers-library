// Class ManifestData_DecryptManifest
// Dafny class ManifestData_DecryptManifest compiled into Java
package TestManifests_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class ManifestData_DecryptManifest extends ManifestData {
  public java.math.BigInteger _version;
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient _keys;
  public JSON_mValues_Compile.JSON _client;
  public dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _jsonTests;
  public ManifestData_DecryptManifest (java.math.BigInteger version, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, JSON_mValues_Compile.JSON client, dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> jsonTests) {
    super();
    this._version = version;
    this._keys = keys;
    this._client = client;
    this._jsonTests = jsonTests;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ManifestData_DecryptManifest o = (ManifestData_DecryptManifest)other;
    return true && java.util.Objects.equals(this._version, o._version) && this._keys == o._keys && java.util.Objects.equals(this._client, o._client) && java.util.Objects.equals(this._jsonTests, o._jsonTests);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._version);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._client);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._jsonTests);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestManifests.ManifestData.DecryptManifest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._version));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._keys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._client));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._jsonTests));
    s.append(")");
    return s.toString();
  }
}
