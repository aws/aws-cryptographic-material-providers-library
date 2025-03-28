// Class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>
// Dafny class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T> compiled into Java
package EdkWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T> extends WrapEdkMaterialOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _symmetricSigningKey;
  public T _wrapInfo;
  public WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    super(_td_T);
    this._wrappedMaterial = wrappedMaterial;
    this._symmetricSigningKey = symmetricSigningKey;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T> o = (WrapEdkMaterialOutput_WrapOnlyEdkMaterialOutput<T>)other;
    return true && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("EdkWrapping.WrapEdkMaterialOutput.WrapOnlyEdkMaterialOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
}
