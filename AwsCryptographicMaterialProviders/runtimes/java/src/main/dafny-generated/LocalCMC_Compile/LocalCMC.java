// Class LocalCMC
// Dafny class LocalCMC compiled into Java
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
public class LocalCMC implements software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache {
  public LocalCMC() {
    this.queue = null;
    this.cache = null;
    this._entryCapacity = java.math.BigInteger.ZERO;
    this._entryPruningTailSize = java.math.BigInteger.ZERO;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeleteCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsCache.DeleteCacheEntry(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsCache.GetCacheEntry(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> PutCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsCache.PutCacheEntry(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> UpdateUsageMetadata(software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsCache.UpdateUsageMetadata(this, input);
    return _out1;
  }
  public DoublyLinkedCacheEntryList queue;
  public DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, CacheEntry> cache;
  public void __ctor(java.math.BigInteger entryCapacity_k, java.math.BigInteger entryPruningTailSize_k)
  {
    (this)._entryCapacity = entryCapacity_k;
    (this)._entryPruningTailSize = entryPruningTailSize_k;
    DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, CacheEntry> _nw0 = new DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, CacheEntry>(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    (this).cache = _nw0;
    DoublyLinkedCacheEntryList _nw1 = new DoublyLinkedCacheEntryList();
    _nw1.__ctor();
    (this).queue = _nw1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      long _0_now;
      long _out0;
      _out0 = Time.__default.CurrentRelativeTime();
      _0_now = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = (this).GetCacheEntryWithTime(input, _0_now);
      output = _out1;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetCacheEntryWithTime(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input, long now)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      if ((this.cache).HasKey((input).dtor_identifier())) {
        CacheEntry _0_entry;
        _0_entry = (this.cache).Select((input).dtor_identifier());
        if ((now) <= ((_0_entry).expiryTime())) {
          (this.queue).moveToFront(_0_entry);
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput.create((_0_entry).materials(), (_0_entry).creationTime(), (_0_entry).expiryTime(), _0_entry.messagesUsed, _0_entry.bytesUsed));
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
          _out0 = (this).pruning(now);
          _1_valueOrError0 = _out0;
          if ((_1_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_1_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor());
            return output;
          }
          dafny.Tuple0 _2___v0;
          _2___v0 = (_1_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        } else {
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
          _out1 = (this).DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create((input).dtor_identifier()));
          _3_valueOrError1 = _out1;
          if ((_3_valueOrError1).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor());
            return output;
          }
          dafny.Tuple0 _4___v1;
          _4___v1 = (_3_valueOrError1).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_EntryDoesNotExist(dafny.DafnySequence.asString("Entry past TTL")));
        }
      } else {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_EntryDoesNotExist(dafny.DafnySequence.asString("Entry does not exist")));
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> PutCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      if (((this).entryCapacity()).signum() == 0) {
        output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
        return output;
      }
      if ((this.cache).HasKey((input).dtor_identifier())) {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = (this).DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create((input).dtor_identifier()));
        _0_valueOrError0 = _out0;
        if ((_0_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
          return output;
        }
        dafny.Tuple0 _1___v2;
        _1___v2 = (_0_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      }
      if (java.util.Objects.equals((this).entryCapacity(), (this.cache).Size())) {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = (this).DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create(((this.queue.tail).dtor_deref()).identifier()));
        _2_valueOrError1 = _out1;
        if ((_2_valueOrError1).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_2_valueOrError1).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
          return output;
        }
        dafny.Tuple0 _3___v3;
        _3___v3 = (_2_valueOrError1).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      }
      CacheEntry _4_cell;
      CacheEntry _nw0 = new CacheEntry();
      _nw0.__ctor((input).dtor_materials(), (input).dtor_identifier(), (input).dtor_creationTime(), (input).dtor_expiryTime(), ((input).dtor_messagesUsed()).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor(), 0), ((input).dtor_bytesUsed()).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor(), 0));
      _4_cell = _nw0;
      (this.queue).pushCell(_4_cell);
      (this.cache).Put((input).dtor_identifier(), _4_cell);
      output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      if ((this.cache).HasKey((input).dtor_identifier())) {
        CacheEntry _0_cell;
        _0_cell = (this.cache).Select((input).dtor_identifier());
        goto_1: {
          (this.cache).Remove((input).dtor_identifier());
        }
        (this.queue).remove(_0_cell);
      }
      output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> UpdateUsageMetadata_k(software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if ((this.cache).HasKey((input).dtor_identifier())) {
      CacheEntry _0_cell;
      _0_cell = (this.cache).Select((input).dtor_identifier());
      if (((_0_cell.messagesUsed) <= ((int) ((__default.INT32__MAX__VALUE()) - (1)))) && ((_0_cell.bytesUsed) <= ((int) ((__default.INT32__MAX__VALUE()) - ((input).dtor_bytesUsed()))))) {
        int _rhs0 = (int) ((_0_cell.messagesUsed) + (1));
        int _rhs1 = (int) ((_0_cell.bytesUsed) + ((input).dtor_bytesUsed()));
        CacheEntry _lhs0 = _0_cell;
        CacheEntry _lhs1 = _0_cell;
        _lhs0.messagesUsed = _rhs0;
        _lhs1.bytesUsed = _rhs1;
      } else {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = (this).DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create((input).dtor_identifier()));
        _1_valueOrError0 = _out0;
        if ((_1_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_1_valueOrError0).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
          return output;
        }
        dafny.Tuple0 _2___v4;
        _2___v4 = (_1_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      }
    }
    output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> pruning(long now)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    java.math.BigInteger _hi0 = (this).entryPruningTailSize();
    for (java.math.BigInteger _0_i = java.math.BigInteger.ZERO; _0_i.compareTo(_hi0) < 0; _0_i = _0_i.add(java.math.BigInteger.ONE)) {
      if ((this.queue.tail).is_Ptr()) {
        if ((((this.queue.tail).dtor_deref()).expiryTime()) < (now)) {
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
          _out0 = (this).DeleteCacheEntry_k(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create(((this.queue.tail).dtor_deref()).identifier()));
          _1_valueOrError0 = _out0;
          if ((_1_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_1_valueOrError0).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
            return output;
          }
          dafny.Tuple0 _2___v5;
          _2___v5 = (_1_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        } else {
          output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
          return output;
        }
      } else {
        output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
        return output;
      }
    }
    output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    return output;
  }
  public java.math.BigInteger _entryCapacity;
  public java.math.BigInteger entryCapacity()
  {
    return this._entryCapacity;
  }
  public java.math.BigInteger _entryPruningTailSize;
  public java.math.BigInteger entryPruningTailSize()
  {
    return this._entryPruningTailSize;
  }
  private static final dafny.TypeDescriptor<LocalCMC> _TYPE = dafny.TypeDescriptor.<LocalCMC>referenceWithInitializer(LocalCMC.class, () -> (LocalCMC) null);
  public static dafny.TypeDescriptor<LocalCMC> _typeDescriptor() {
    return (dafny.TypeDescriptor<LocalCMC>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC.LocalCMC";
  }
}
