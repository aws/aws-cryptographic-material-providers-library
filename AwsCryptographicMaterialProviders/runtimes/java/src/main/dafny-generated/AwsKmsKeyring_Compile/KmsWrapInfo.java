// Class KmsWrapInfo
// Dafny class KmsWrapInfo compiled into Java
package AwsKmsKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsWrapInfo {
  public dafny.DafnySequence<? extends Character> _kmsKeyArn;
  public KmsWrapInfo (dafny.DafnySequence<? extends Character> kmsKeyArn) {
    this._kmsKeyArn = kmsKeyArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsWrapInfo o = (KmsWrapInfo)other;
    return true && java.util.Objects.equals(this._kmsKeyArn, o._kmsKeyArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsKeyArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsKmsKeyring.KmsWrapInfo.KmsWrapInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsKeyArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsWrapInfo> _TYPE = dafny.TypeDescriptor.<KmsWrapInfo>referenceWithInitializer(KmsWrapInfo.class, () -> KmsWrapInfo.Default());
  public static dafny.TypeDescriptor<KmsWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsWrapInfo theDefault = AwsKmsKeyring_Compile.KmsWrapInfo.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KmsWrapInfo Default() {
    return theDefault;
  }
  public static KmsWrapInfo create(dafny.DafnySequence<? extends Character> kmsKeyArn) {
    return new KmsWrapInfo(kmsKeyArn);
  }
  public static KmsWrapInfo create_KmsWrapInfo(dafny.DafnySequence<? extends Character> kmsKeyArn) {
    return create(kmsKeyArn);
  }
  public boolean is_KmsWrapInfo() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_kmsKeyArn() {
    return this._kmsKeyArn;
  }
}
