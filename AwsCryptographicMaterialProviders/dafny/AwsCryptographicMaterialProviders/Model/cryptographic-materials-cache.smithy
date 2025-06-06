namespace aws.cryptography.materialProviders

use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable
use aws.polymorph#javadoc

@range(min: 1)
integer CountingNumber

@smithy.api#suppress(["MutableLocalStateTrait"])
@aws.polymorph#mutableLocalState
@aws.polymorph#extendable
resource CryptographicMaterialsCache {

  //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#overview
  //= type=implication
  //# Cryptographic materials cache (CMC) is used by the [caching cryptographic materials manager (CMM)](caching-cmm.md)
  //# to store cryptographic materials for reuse.
  //# This document describes the interface that all CMCs MUST implement.
  operations: [PutCacheEntry, GetCacheEntry, UpdateUsageMetadata, DeleteCacheEntry]
}

@aws.polymorph#reference(resource: CryptographicMaterialsCache)
structure CryptographicMaterialsCacheReference {}

//= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#put-cache-entry
//= type=implication
//# This operation MUST NOT return the inserted cache entry.
operation PutCacheEntry {
  input: PutCacheEntryInput,
}

structure PutCacheEntryInput {
  @required
  identifier: Blob,
  @required
  materials: Materials,
  @required
  creationTime: PositiveLong,
  @required
  //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#put-cache-entry
  //= type=implication
  //# The cache entry MUST include all [usage metadata](#usage-metadata)
  //# since this information can not be updated after the put operation.
  expiryTime: PositiveLong,
  messagesUsed: PositiveInteger,
  bytesUsed: PositiveInteger,
}

operation GetCacheEntry {
  input: GetCacheEntryInput,
  output: GetCacheEntryOutput,
  errors: [
    InFlightTTLExceeded
    EntryDoesNotExist
    //Technically, numerous other errors, depending on the implementation
  ]
}

structure GetCacheEntryInput {
  @required
  identifier: Blob,
  bytesUsed: Long

}

//= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#cache-entry
//= type=implication
//# A cache entry represents an entry in the cryptographic materials cache
//# and MUST have the following information.
//# 
//# - [Materials](#materials)
//# - [Creation Time](#creation-time)
//# - [Expiry Time](#expiry-time)
//# - [Usage Metadata](#usage-metadata)
structure GetCacheEntryOutput {
  @required
  materials: Materials,
  @required
  creationTime: PositiveLong,
  //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#time-to-live-ttl
  //= type=implication
  //# Each cache entry has a time-to-live (TTL)
  //# that represents a point in time at which the cache entry
  //# MUST be considered invalid.
  @required
  expiryTime: PositiveLong,
  @required
  messagesUsed: PositiveInteger,
  @required
  bytesUsed: PositiveInteger,
}

union Materials {
  Encryption: EncryptionMaterials,
  Decryption: DecryptionMaterials,
  BranchKey: aws.cryptography.keyStore#BranchKeyMaterials,
  BeaconKey: aws.cryptography.keyStore#BeaconKeyMaterials
}

operation DeleteCacheEntry {
  input: DeleteCacheEntryInput
}

structure DeleteCacheEntryInput {
  @required
  identifier: Blob
}

operation UpdateUsageMetadata {
  input: UpdateUsageMetadataInput
}

structure UpdateUsageMetadataInput {
  @required
  identifier: Blob,
  @required
  bytesUsed: PositiveInteger,
}

@error("client")
@documentation("The requested element is not in the cache; AWS Crypto Tools intends to deprecate this for a non-error control scheme.")
structure EntryDoesNotExist {
  @required
  message: String,
}

@error("client")
structure EntryAlreadyExists {
  @required
  message: String,
}

@error("client")
@documentation(
"Thrown if a request is waiting for longer than `inflightTTL`.
The Storm Tracking Cache protects against unbounded parallelism.
The Storm Tracking Cache will only work `fanOut` number of concurrent requests.
As requests are completed,
queued requests are worked.
If a request is not worked in less than `inflightTTL`,
this exception is thrown.

Note that this exception does NOT imply that the material requested
is invalid or unreachable;
it only implies that the cache had more requests to handle than it could
with the given `fanOut` and `inflightTTL` constraints.")
structure InFlightTTLExceeded {
  @required
  message: String,
}

// Materials Cache Constructors

@positional
structure CreateCryptographicMaterialsCacheOutput {
  @required
  materialsCache: CryptographicMaterialsCacheReference 
}

operation CreateCryptographicMaterialsCache {
  input: CreateCryptographicMaterialsCacheInput,
  output: CreateCryptographicMaterialsCacheOutput,
}

@javadoc("The best choice for most situations. Probably a StormTrackingCache.")
structure DefaultCache {
  @required
  @javadoc("Maximum number of entries cached.")
  entryCapacity: CountingNumber
}

@javadoc("Nothing should ever be cached.")
structure NoCache {}

@javadoc("A cache that is NOT safe for use in a multi threaded environment.")
structure SingleThreadedCache {
  //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#initialization
  //= type=implication
  //# On initialization of the local CMC,
  //# the caller MUST provide the following:
  //#
  //# - [Entry Capacity](#entry-capacity)
  //#
  //# The local CMC MUST also define the following:
  //#
  //# - [Entry Pruning Tail Size](#entry-pruning-tail-size)
  @required
  @javadoc("Maximum number of entries cached.")
  entryCapacity: CountingNumber,

  @javadoc("Number of entries to prune at a time.")
  entryPruningTailSize: CountingNumber,
}

@javadoc("A cache that is safe for use in a multi threaded environment, but no extra functionality.")
structure MultiThreadedCache {
  @required
  @javadoc("Maximum number of entries cached.")
  entryCapacity: CountingNumber,

  @javadoc("Number of entries to prune at a time.")
  entryPruningTailSize: CountingNumber,
}

@javadoc("A cache that is safe for use in a multi threaded environment,
and tries to prevent redundant or overly parallel backend calls.")
structure StormTrackingCache {
  @required
  @javadoc("Maximum number of entries cached.")
  entryCapacity: CountingNumber,

  @javadoc("Number of entries to prune at a time.")
  entryPruningTailSize: CountingNumber,

  @required
  @javadoc("How much time before expiration should an attempt be made to refresh the materials.
  If zero, use a simple cache with no storm tracking.")
  gracePeriod: CountingNumber,

  @required
  @javadoc("How much time between attempts to refresh the materials.")
  graceInterval: CountingNumber,

  @required
  @javadoc("How many simultaneous attempts to refresh the materials.")
  fanOut: CountingNumber,

  @required
  @javadoc("How much time until an attempt to refresh the materials should be forgotten.")
  inFlightTTL: CountingNumber,

  @required
  @javadoc("How many milliseconds should a thread sleep if fanOut is exceeded.")
  sleepMilli: CountingNumber,

  @javadoc("The time unit for gracePeriod, graceInterval, and inFlightTTL.
  The default is seconds.
  If this is set to milliseconds, then these values will be treated as milliseconds.")
  timeUnits: TimeUnits
}

@enum([
  {
    name: "Seconds",
    value: "Seconds",
  },
  {
    name: "Milliseconds",
    value: "Milliseconds",
  },
])
string TimeUnits

union CacheType {
  Default : DefaultCache,
  No: NoCache,
  SingleThreaded: SingleThreadedCache,
  MultiThreaded: MultiThreadedCache,
  StormTracking: StormTrackingCache,
  @documentation("Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.")
  Shared: CryptographicMaterialsCacheReference
}

structure CreateCryptographicMaterialsCacheInput {
  @required
  @javadoc("Which type of local cache to use.")
  cache: CacheType
}
