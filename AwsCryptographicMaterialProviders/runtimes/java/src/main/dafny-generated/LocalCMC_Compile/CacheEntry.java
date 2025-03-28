// Class CacheEntry
// Dafny class CacheEntry compiled into Java
package LocalCMC_Compile;

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
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheEntry {
  public CacheEntry() {
    this.prev = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    this.next = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    this.messagesUsed = 0;
    this.bytesUsed = 0;
    this._identifier = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.Materials)null;
    this._creationTime = 0L;
    this._expiryTime = 0L;
  }
  public Ref<CacheEntry> prev;
  public Ref<CacheEntry> next;
  public int messagesUsed;
  public int bytesUsed;
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.Materials materials_k, dafny.DafnySequence<? extends java.lang.Byte> identifier_k, long creationTime_k, long expiryTime_k, int messagesUsed_k, int bytesUsed_k)
  {
    (this)._materials = materials_k;
    (this)._identifier = identifier_k;
    (this)._creationTime = creationTime_k;
    (this)._expiryTime = expiryTime_k;
    (this).messagesUsed = messagesUsed_k;
    (this).bytesUsed = bytesUsed_k;
    (this).prev = __default.NULL();
    (this).next = __default.NULL();
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public dafny.DafnySequence<? extends java.lang.Byte> identifier()
  {
    return this._identifier;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.Materials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.Materials materials()
  {
    return this._materials;
  }
  public long _creationTime;
  public long creationTime()
  {
    return this._creationTime;
  }
  public long _expiryTime;
  public long expiryTime()
  {
    return this._expiryTime;
  }
  private static final dafny.TypeDescriptor<CacheEntry> _TYPE = dafny.TypeDescriptor.<CacheEntry>referenceWithInitializer(CacheEntry.class, () -> (CacheEntry) null);
  public static dafny.TypeDescriptor<CacheEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<CacheEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC.CacheEntry";
  }
}
