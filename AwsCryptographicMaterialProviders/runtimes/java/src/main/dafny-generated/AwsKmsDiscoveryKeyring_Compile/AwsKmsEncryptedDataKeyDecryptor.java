// Class AwsKmsEncryptedDataKeyDecryptor
// Dafny class AwsKmsEncryptedDataKeyDecryptor compiled into Java
package AwsKmsDiscoveryKeyring_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEncryptedDataKeyDecryptor implements Actions_Compile.ActionWithResult<Constants_Compile.AwsKmsEdkHelper, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<Constants_Compile.AwsKmsEdkHelper, Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public AwsKmsEncryptedDataKeyDecryptor() {
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
    this._client = null;
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._materials = materials;
    (this)._client = client;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(Constants_Compile.AwsKmsEdkHelper helper)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    dafny.DafnySequence<? extends Character> _0_awsKmsKey;
    _0_awsKmsKey = ((helper).dtor_arn()).ToString();
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _1_valueOrError0 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId(((helper).dtor_arn()).ToString());
    if ((_1_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.Tuple0 _2___v0;
    _2___v0 = (_1_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsKeyring_Compile.KmsUnwrapKeyMaterial _3_kmsUnwrap;
    AwsKmsKeyring_Compile.KmsUnwrapKeyMaterial _nw0 = new AwsKmsKeyring_Compile.KmsUnwrapKeyMaterial();
    _nw0.__ctor((this).client(), _0_awsKmsKey, (this).grantTokens());
    _3_kmsUnwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AwsKmsKeyring_Compile.KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_unwrapOutputRes;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AwsKmsKeyring_Compile.KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = EdkWrapping_Compile.__default.<AwsKmsKeyring_Compile.KmsUnwrapInfo>UnwrapEdkMaterial(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor(), ((helper).dtor_edk()).dtor_ciphertext(), (this).materials(), _3_kmsUnwrap);
    _4_unwrapOutputRes = _out0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AwsKmsKeyring_Compile.KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AwsKmsKeyring_Compile.KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<AwsKmsKeyring_Compile.KmsUnwrapInfo>_typeDescriptor(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<AwsKmsKeyring_Compile.KmsUnwrapInfo>Default(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor(), AwsKmsKeyring_Compile.KmsUnwrapInfo.Default()));
    _5_valueOrError1 = _4_unwrapOutputRes;
    if ((_5_valueOrError1).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<AwsKmsKeyring_Compile.KmsUnwrapInfo>_typeDescriptor(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<AwsKmsKeyring_Compile.KmsUnwrapInfo>_typeDescriptor(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<AwsKmsKeyring_Compile.KmsUnwrapInfo> _6_unwrapOutput;
    _6_unwrapOutput = (_5_valueOrError1).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<AwsKmsKeyring_Compile.KmsUnwrapInfo>_typeDescriptor(AwsKmsKeyring_Compile.KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _7_valueOrError2 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_6_unwrapOutput).dtor_plaintextDataKey(), (_6_unwrapOutput).dtor_symmetricSigningKey());
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _8_result;
    _8_result = (_7_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_result);
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials()
  {
    return this._materials;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  private static final dafny.TypeDescriptor<AwsKmsEncryptedDataKeyDecryptor> _TYPE = dafny.TypeDescriptor.<AwsKmsEncryptedDataKeyDecryptor>referenceWithInitializer(AwsKmsEncryptedDataKeyDecryptor.class, () -> (AwsKmsEncryptedDataKeyDecryptor) null);
  public static dafny.TypeDescriptor<AwsKmsEncryptedDataKeyDecryptor> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsEncryptedDataKeyDecryptor>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor";
  }
}
