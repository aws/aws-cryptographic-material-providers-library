// Class StaticKeyring
// Dafny class StaticKeyring compiled into Java
package TestMultiKeyring_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;
import TestUtils_Compile.*;
import TestIntermediateKeyWrapping_Compile.*;
import TestErrorMessages_Compile.*;
import TestDefaultClientProvider_Compile.*;
import TestRawECDHKeyring_Compile.*;
import TestRawAESKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class StaticKeyring implements software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public StaticKeyring() {
    this._encryptionMaterials = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>Default(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor());
    this._decryptionMaterials = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>Default(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out0;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out0;
  }
  public void __ctor(Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> encryptionMaterials, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> decryptionMaterials)
  {
    (this)._encryptionMaterials = encryptionMaterials;
    (this)._decryptionMaterials = decryptionMaterials;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      if (((this).encryptionMaterials()).is_Some()) {
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(((this).encryptionMaterials()).dtor_value()));
        return res;
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _0_exception;
        _0_exception = software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Failure"));
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _0_exception);
        return res;
      }
    }
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      if (((this).decryptionMaterials()).is_Some()) {
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(((this).decryptionMaterials()).dtor_value()));
        return res;
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _0_exception;
        _0_exception = software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Failure"));
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _0_exception);
        return res;
      }
    }
    return res;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> _encryptionMaterials;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> encryptionMaterials()
  {
    return this._encryptionMaterials;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> _decryptionMaterials;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials> decryptionMaterials()
  {
    return this._decryptionMaterials;
  }
  private static final dafny.TypeDescriptor<StaticKeyring> _TYPE = dafny.TypeDescriptor.<StaticKeyring>referenceWithInitializer(StaticKeyring.class, () -> (StaticKeyring) null);
  public static dafny.TypeDescriptor<StaticKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<StaticKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "TestMultiKeyring.StaticKeyring";
  }
}
