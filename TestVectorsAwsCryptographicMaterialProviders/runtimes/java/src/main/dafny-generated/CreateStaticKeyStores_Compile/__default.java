// Class __default
// Dafny class __default compiled into Java
package CreateStaticKeyStores_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient CreateStaticKeyStore(KeyMaterial_Compile.KeyMaterial staticKeyMaterial)
  {
    software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient keyStore = null;
    StaticKeyStore _nw0 = new StaticKeyStore();
    _nw0.__ctor(staticKeyMaterial);
    keyStore = _nw0;
    return keyStore;
  }
  @Override
  public java.lang.String toString() {
    return "CreateStaticKeyStores._default";
  }
}
