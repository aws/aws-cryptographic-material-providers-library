// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"

module {:options "/functionSyntax:4" } Structure {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UTF8

  //Attribute Names
  const BRANCH_KEY_IDENTIFIER_FIELD := "branch-key-id"
  const TYPE_FIELD := "type"
  const KEY_CREATE_TIME := "create-time"
  const HIERARCHY_VERSION := "hierarchy-version"
  const TABLE_FIELD := "tablename"
  const KMS_FIELD := "kms-arn"
  const BRANCH_KEY_FIELD := "enc"
  const ENC_FIELD := BRANCH_KEY_FIELD
  const BRANCH_KEY_ACTIVE_VERSION_FIELD := "version"
  const M_ORIGINAL := "original" // The DDB Attribute name for the original state, which is AttributeValue.B
  const M_TERMINAL := "terminal" // The DDB Attribute name for the terminal state, which is AttributeValue.B
  const M_INPUT := "input" // The DDB Attribute name for the input, which is AttributeValue.B
  const M_UUID := "uuid" // The DDB Attribute name for the uuid, which is AttributeValue.S
  const M_PAGE_INDEX := "pageIndex" // The DDB Attribute name for the pageIndex, which is AttributeValue.B

  const AWS_CRYPTO_EC := "aws-crypto-ec"
  const ENCRYPTION_CONTEXT_PREFIX := AWS_CRYPTO_EC + ":"
  const AES_256_LENGTH: uint8 := 32
  // BKC => Branch Key Context
  const BKC_DIGEST_LENGTH: uint8 := 48

  const BRANCH_KEY_RESTRICTED_FIELD_NAMES := {
    BRANCH_KEY_IDENTIFIER_FIELD,
    TYPE_FIELD,
    KEY_CREATE_TIME,
    HIERARCHY_VERSION,
    TABLE_FIELD,
    KMS_FIELD,
    BRANCH_KEY_FIELD,
    BRANCH_KEY_ACTIVE_VERSION_FIELD
  }

  //Attribute Values
  const HIERARCHY_VERSION_VALUE_1 := "1"
  const HIERARCHY_VERSION_VALUE_2 := "2"
  // TODO-HV-2-M1 : Find all HIERARCHY_VERSION_VALUE and replace them with something
  const HIERARCHY_VERSION_VALUE := HIERARCHY_VERSION_VALUE_1
  // TODO-HV-2-M1 : Find all HIERARCHY_VERSION_ATTRIBUTE_VALUE and replace them with something
  const HIERARCHY_VERSION_ATTRIBUTE_VALUE := DDB.AttributeValue.N(HIERARCHY_VERSION_VALUE)
  const HIERARCHY_VERSION_ATTRIBUTE_VALUE_1 := DDB.AttributeValue.N(HIERARCHY_VERSION_VALUE_1)
  const HIERARCHY_VERSION_ATTRIBUTE_VALUE_2 := DDB.AttributeValue.N(HIERARCHY_VERSION_VALUE_2)
  const BRANCH_KEY_TYPE_PREFIX := "branch:version:"
  const BRANCH_KEY_ACTIVE_TYPE := "branch:ACTIVE"
  const BEACON_KEY_TYPE_VALUE := "beacon:ACTIVE"
  const MUTATION_COMMITMENT_TYPE := "branch:MUTATION_COMMITMENT"
  const MUTATION_INDEX_TYPE := "branch:MUTATION_INDEX"
  //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context
  //= type=exception
  //# Across all versions of a Branch Key, the custom encryption context MUST be equal.
  // At this time, we have no operation that reads all the records of a Branch Key ID.

  type BranchKeyContext = m: map<string, string> | BranchKeyContext?(m) witness *
  predicate BranchKeyContext?(m: map<string, string>) {
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
    //= type=implication
    //# - MUST have a `branch-key-id` attribute
    && (BRANCH_KEY_IDENTIFIER_FIELD in m)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - MUST have a `type` attribute
    && (TYPE_FIELD in m)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - MUST have a `create-time` attribute
    && (KEY_CREATE_TIME in m)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - MUST have a `hierarchy-version`
    && (HIERARCHY_VERSION in m)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - MUST have a `tablename` attribute to store the logicalKeyStoreName
    && (TABLE_FIELD in m)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - MUST have a `kms-arn` attribute
    && (KMS_FIELD in m)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
    //= type=implication
    //# - MUST NOT have a `enc` attribute
    && BRANCH_KEY_FIELD !in m.Keys

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
    //= type=implication
    //# - The `branch-key-id` field MUST not be an empty string
    && 0 < |m[BRANCH_KEY_IDENTIFIER_FIELD]|
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
       //= type=implication
       //# - The `type` field MUST not be an empty string
    && 0 < |m[TYPE_FIELD]|

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#active-encryption-context
    //= type=implication
    //# The ACTIVE encryption context MUST have a `version` attribute.
    && (BRANCH_KEY_ACTIVE_VERSION_FIELD in m <==>
        && m[TYPE_FIELD] == BRANCH_KEY_ACTIVE_TYPE)
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#active-encryption-context
       //= type=implication
       //# The ACTIVE encryption context value of the `type` attribute MUST equal to `"branch:ACTIVE"`.
    && (BRANCH_KEY_ACTIVE_VERSION_FIELD in m ==>
          //= aws-encryption-sdk-specification/framework/branch-key-store.md#active-encryption-context
          //= type=implication
          //# The `version` attribute MUST store the branch key version formatted like `"branch:version:"` + `version`.
          && BRANCH_KEY_TYPE_PREFIX < m[BRANCH_KEY_ACTIVE_VERSION_FIELD])

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#beacon-key-encryption-context
    //= type=implication
    //# The Beacon key encryption context MUST NOT have a `version` attribute.

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#decrypt-only-encryption-context
    //= type=implication
    //# The DECRYPT_ONLY encryption context MUST NOT have a `version` attribute.
    && (BRANCH_KEY_ACTIVE_VERSION_FIELD !in m <==>
        //= aws-encryption-sdk-specification/framework/branch-key-store.md#beacon-key-encryption-context
        //= type=implication
        //# The Beacon key encryption context value of the `type` attribute MUST equal to `"beacon:ACTIVE"`.
        || m[TYPE_FIELD] == BEACON_KEY_TYPE_VALUE
           //= aws-encryption-sdk-specification/framework/branch-key-store.md#decrypt-only-encryption-context
           //= type=implication
           //# The `type` attribute MUST stores the branch key version formatted like `"branch:version:"` + `version`.
        || BRANCH_KEY_TYPE_PREFIX < m[TYPE_FIELD])
  }

  predicate EncryptedHierarchicalKeyFromStorage?(key: Types.EncryptedHierarchicalKey) {
    && BranchKeyContext?(key.EncryptionContext)
    && key.Identifier == key.EncryptionContext[BRANCH_KEY_IDENTIFIER_FIELD]
    && key.CreateTime == key.EncryptionContext[KEY_CREATE_TIME]
    && key.KmsArn == key.EncryptionContext[KMS_FIELD]

    && (match key.Type
        case ActiveHierarchicalSymmetricVersion(active) =>
          && BRANCH_KEY_ACTIVE_VERSION_FIELD in key.EncryptionContext
          && key.EncryptionContext[TYPE_FIELD] == BRANCH_KEY_ACTIVE_TYPE
          && key.EncryptionContext[BRANCH_KEY_ACTIVE_VERSION_FIELD] == BRANCH_KEY_TYPE_PREFIX + active.Version
        case HierarchicalSymmetricVersion(decryptOnly) =>
          && BRANCH_KEY_ACTIVE_VERSION_FIELD !in key.EncryptionContext
          && key.EncryptionContext[TYPE_FIELD] == BRANCH_KEY_TYPE_PREFIX + decryptOnly.Version
        case ActiveHierarchicalSymmetricBeacon(_) =>
          && BRANCH_KEY_ACTIVE_VERSION_FIELD !in key.EncryptionContext
          && key.EncryptionContext[TYPE_FIELD] == BEACON_KEY_TYPE_VALUE
       )
  }

  predicate ActiveHierarchicalSymmetricVersionEncryptionContext?(
    ec: Types.EncryptionContextString
  )
  {
    && BranchKeyContext?(ec)
    && BRANCH_KEY_ACTIVE_VERSION_FIELD in ec
    && ec[TYPE_FIELD] == BRANCH_KEY_ACTIVE_TYPE
  }


  function ToAttributeMap(
    key: Types.EncryptedHierarchicalKey
  ): (output: DDB.AttributeMap)
    requires (forall k <- key.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
    ensures EncryptedHierarchicalKeyFromStorage?(key) ==>
              && BranchKeyItem?(output)
              && ToEncryptedHierarchicalKey(output, key.EncryptionContext[TABLE_FIELD]) == key
  {
    map k <- key.EncryptionContext.Keys + {BRANCH_KEY_FIELD} - {TABLE_FIELD}
             // Working around https://github.com/dafny-lang/dafny/issues/5776
             //  that will make the following fail to compile
             // ::  k := match k
             // case HIERARCHY_VERSION => DDB.AttributeValue.N(key.EncryptionContext[HIERARCHY_VERSION])
             // case BRANCH_KEY_FIELD => DDB.AttributeValue.B(key.CiphertextBlob)
             // case _ => DDB.AttributeValue.S(key.EncryptionContext[k]);
      :: k := if k == HIERARCHY_VERSION then
        DDB.AttributeValue.N(key.EncryptionContext[HIERARCHY_VERSION])
      else if k == BRANCH_KEY_FIELD then
        DDB.AttributeValue.B(key.CiphertextBlob)
      else
        DDB.AttributeValue.S(key.EncryptionContext[k])
  }

  function ToEncryptedHierarchicalKey(
    item: DDB.AttributeMap,
    logicalKeyStoreName: string
  ): (output: Types.EncryptedHierarchicalKey)
    requires BranchKeyItem?(item)
    ensures EncryptedHierarchicalKeyFromStorage?(output)
  {
    var EncryptionContext := map k <- item.Keys - {BRANCH_KEY_FIELD} + {TABLE_FIELD}
                                      // Working around https://github.com/dafny-lang/dafny/issues/5776
                                      //  that will make the following fail to compile
                                      // match k
                                      // case HIERARCHY_VERSION => item[k].N
                                      // case TABLE_FIELD => logicalKeyStoreName
                                      // case _ => item[k].S
                               :: k := if k == HIERARCHY_VERSION then
                                 item[k].N
                               else if k == TABLE_FIELD then
                                 logicalKeyStoreName
                               else
                                 item[k].S;

    ConstructEncryptedHierarchicalKey(EncryptionContext, item[BRANCH_KEY_FIELD].B)
  }

  function ConstructEncryptedHierarchicalKey(
    EncryptionContext: map<string, string>,
    CiphertextBlob: seq<uint8>
  ): (output: Types.EncryptedHierarchicalKey)
    requires BranchKeyContext?(EncryptionContext)
    ensures EncryptedHierarchicalKeyFromStorage?(output)
  {
    var Type
      := if EncryptionContext[TYPE_FIELD] == BRANCH_KEY_ACTIVE_TYPE then
           Types.ActiveHierarchicalSymmetricVersion(
             Types.ActiveHierarchicalSymmetric(
               Version := EncryptionContext[BRANCH_KEY_ACTIVE_VERSION_FIELD][|BRANCH_KEY_TYPE_PREFIX|..]
             ))
         else if EncryptionContext[TYPE_FIELD] == BEACON_KEY_TYPE_VALUE then
           Types.HierarchicalKeyType.ActiveHierarchicalSymmetricBeacon(Types.ActiveHierarchicalSymmetricBeacon.ActiveHierarchicalSymmetricBeacon)
         else
           Types.HierarchicalSymmetricVersion(
             Types.HierarchicalSymmetric(
               Version := EncryptionContext[TYPE_FIELD][|BRANCH_KEY_TYPE_PREFIX|..]
             ));

    Types.EncryptedHierarchicalKey(
      Identifier := EncryptionContext[BRANCH_KEY_IDENTIFIER_FIELD],
      Type := Type,
      CreateTime := EncryptionContext[KEY_CREATE_TIME],
      KmsArn := EncryptionContext[KMS_FIELD],
      EncryptionContext := EncryptionContext,
      CiphertextBlob := CiphertextBlob
    )
  }

  function ToBranchKeyMaterials(
    key: Types.EncryptedHierarchicalKey,
    plaintextKey: seq<uint8>
  ): (output: Result<Types.BranchKeyMaterials, Types.Error>)

    requires EncryptedHierarchicalKeyFromStorage?(key)
    requires
      || key.Type.ActiveHierarchicalSymmetricVersion?
      || key.Type.HierarchicalSymmetricVersion?

    ensures output.Success?
            ==>
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
              //= type=implication
              //# - [Branch Key](./structures.md#branch-key) MUST be the [decrypted branch key material](#aws-kms-branch-key-decryption)
              && output.value.branchKey == plaintextKey
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
                 //= type=implication
                 //# - [Branch Key Id](./structures.md#branch-key-id) MUST be the `branch-key-id`
              && output.value.branchKeyIdentifier == key.Identifier

              && var versionInformation
                   := if BRANCH_KEY_ACTIVE_VERSION_FIELD in key.EncryptionContext then
                        //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
                        //= type=implication
                        //# If the `type` attribute is equal to `"branch:ACTIVE"`
                        //# then the authenticated encryption context MUST have a `version` attribute
                        //# and the version string is this value.
                        key.EncryptionContext[BRANCH_KEY_ACTIVE_VERSION_FIELD]
                      else
                        //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
                        //= type=implication
                        //# If the `type` attribute start with `"branch:version:"` then the version string MUST be equal to this value.
                        key.EncryptionContext[TYPE_FIELD];
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
              //= type=implication
              //# - [Branch Key Version](./structures.md#branch-key-version)
              //# The version string MUST start with `branch:version:`.
              && BRANCH_KEY_TYPE_PREFIX < versionInformation
              && UTF8.Encode(versionInformation[|BRANCH_KEY_TYPE_PREFIX|..]).Success?
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
                 //= type=implication
                 //# The remaining string encoded as UTF8 bytes MUST be the Branch Key version.
              && output.value.branchKeyVersion == UTF8.Encode(versionInformation[|BRANCH_KEY_TYPE_PREFIX|..]).value
              && output.value.branchKeyVersion == UTF8.Encode(
                                                    match key.Type
                                                    case ActiveHierarchicalSymmetricVersion(active) => active.Version
                                                    case HierarchicalSymmetricVersion(decrypt) => decrypt.Version
                                                  ).value

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
              //= type=implication
              //# - [Encryption Context](./structures.md#encryption-context-3) MUST be constructed by
              //# [Custom Encryption Context From Authenticated Encryption Context](#custom-encryption-context-from-authenticated-encryption-context)
              && ExtractCustomEncryptionContext(key.EncryptionContext).Success?
              && output.value.encryptionContext == ExtractCustomEncryptionContext(key.EncryptionContext).value

              && (forall k <- output.value.encryptionContext
                    ::
                      && UTF8.Decode(k).Success?
                      && UTF8.Decode(output.value.encryptionContext[k]).Success?
                      && (ENCRYPTION_CONTEXT_PREFIX + UTF8.Decode(k).value in key.EncryptionContext)
                      && key.EncryptionContext[ENCRYPTION_CONTEXT_PREFIX + UTF8.Decode(k).value] == UTF8.Decode(output.value.encryptionContext[k]).value)

  {
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-materials-from-authenticated-encryption-context
    //= type=implication
    //# The `type` attribute MUST either be equal to `"branch:ACTIVE"` or start with `"branch:version:"`.
    assert
      || key.EncryptionContext[TYPE_FIELD] == BRANCH_KEY_ACTIVE_TYPE
      || BRANCH_KEY_TYPE_PREFIX < key.EncryptionContext[TYPE_FIELD];

    var branchKeyVersion := match key.Type
      case ActiveHierarchicalSymmetricVersion(active) => active.Version
      case HierarchicalSymmetricVersion(decrypt) => decrypt.Version;

    var branchKeyVersionUtf8 :- UTF8.Encode(branchKeyVersion)
                                .MapFailure(e => Types.KeyStoreException( message := e ));

    var customEncryptionContext :- ExtractCustomEncryptionContext(key.EncryptionContext);

    Success(Types.BranchKeyMaterials(
              branchKeyIdentifier := key.Identifier,
              branchKeyVersion := branchKeyVersionUtf8,
              branchKey := plaintextKey,
              encryptionContext := customEncryptionContext
            ))
  }

  function ToBeaconKeyMaterials(
    key: Types.EncryptedHierarchicalKey,
    plaintextKey: seq<uint8>
  ): (output: Result<Types.BeaconKeyMaterials, Types.Error>)
    requires ActiveHierarchicalSymmetricBeaconKey?(key)
  {
    assert key.EncryptionContext[TYPE_FIELD] == BEACON_KEY_TYPE_VALUE;
    var customEncryptionContext :- ExtractCustomEncryptionContext(key.EncryptionContext);

    Success(Types.BeaconKeyMaterials(
              beaconKeyIdentifier := key.Identifier,
              beaconKey := Some(plaintextKey),
              hmacKeys := None,
              encryptionContext := customEncryptionContext
            ))
  }

  function ExtractCustomEncryptionContext(
    encryptionContext: BranchKeyContext
  ): (output: Result<Types.EncryptionContext, Types.Error>)

    ensures
      output.Success?
      ==>
        forall k <- output.value
          ::
            && UTF8.Decode(k).Success?
            && UTF8.Decode(output.value[k]).Success?
               //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context-from-authenticated-encryption-context
               //= type=implication
               //# For every key in the [encryption context](./structures.md#encryption-context-3)
               //# the string `aws-crypto-ec:` + the UTF8 decode of this key
               //# MUST exist as a key in the authenticated encryption context.
            && (ENCRYPTION_CONTEXT_PREFIX + UTF8.Decode(k).value in encryptionContext)
               //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context-from-authenticated-encryption-context
               //= type=implication
               //# Also, the value in the [encryption context](./structures.md#encryption-context-3) for this key
               //# MUST equal the value in the authenticated encryption context
               //# for the constructed key.
            && encryptionContext[ENCRYPTION_CONTEXT_PREFIX + UTF8.Decode(k).value] == UTF8.Decode(output.value[k]).value
  {

    // Dafny needs some help.
    // Adding a fixed string
    // will not make any of the keys collide.
    assert forall k <- encryptionContext.Keys | ENCRYPTION_CONTEXT_PREFIX < k
        ::
          k == ENCRYPTION_CONTEXT_PREFIX + k[|ENCRYPTION_CONTEXT_PREFIX|..];

    var encodedEncryptionContext
      := set k <- encryptionContext
             | ENCRYPTION_CONTEXT_PREFIX < k
           ::
             (UTF8.Encode(k[|ENCRYPTION_CONTEXT_PREFIX|..]), UTF8.Encode(encryptionContext[k]));

    // This SHOULD be impossible
    // A Dafny string SHOULD all be encodable
    :- Need(forall i <- encodedEncryptionContext
              :: i.0.Success? && i.1.Success?,
            Types.KeyStoreException( message :="Unable to encode string"));

    Success(map i <- encodedEncryptionContext :: i.0.value := i.1.value)
  }

  /** Selects the key-value pairs prefixed with ENCRYPTION_CONTEXT_PREFIX **/
  function SelectCustomEncryptionContextAsString(
    encryptionContext: Types.EncryptionContextString
  ): (output: Types.EncryptionContextString)
    ensures forall k <- output
              ::
                (|k| > |ENCRYPTION_CONTEXT_PREFIX|)
                && k[ .. |ENCRYPTION_CONTEXT_PREFIX|] == ENCRYPTION_CONTEXT_PREFIX
                && (k in encryptionContext)
                && encryptionContext[k] == output[k]
    ensures BRANCH_KEY_RESTRICTED_FIELD_NAMES !! output.Keys
  {
    var customKeys
      :=
      set k <- encryptionContext
          | ENCRYPTION_CONTEXT_PREFIX < k && (|k| > |ENCRYPTION_CONTEXT_PREFIX|)
            && k[0] == ENCRYPTION_CONTEXT_PREFIX[0]
            // //It really helps Dafny to have a specific check
        ::
          // assert HIERARCHY_VERSION != k by {assert k[0] != HIERARCHY_VERSION[0];}
          k;
    map i <- customKeys :: i := encryptionContext[i]
  }

  function ExtractCustomEncryptionContextAs(
    encryptionContext: BranchKeyContext
  ): (output: Types.EncryptionContextString)
    ensures
      forall k <- output
        ::
          && (ENCRYPTION_CONTEXT_PREFIX + k in encryptionContext)
          && encryptionContext[ENCRYPTION_CONTEXT_PREFIX + k] == output[k]
  {
    // Dafny needs some help.
    // Adding a fixed string
    // will not make any of the keys collide.
    assert forall k <- encryptionContext.Keys | ENCRYPTION_CONTEXT_PREFIX < k
        ::
          k == ENCRYPTION_CONTEXT_PREFIX + k[|ENCRYPTION_CONTEXT_PREFIX|..];

    var defixedCustomEncryptionContext
      := set k <- encryptionContext
             | ENCRYPTION_CONTEXT_PREFIX < k
           ::
             (k[|ENCRYPTION_CONTEXT_PREFIX|..], encryptionContext[k]);

    map i <- defixedCustomEncryptionContext :: i.0 := i.1
  }

  opaque function DecryptOnlyBranchKeyEncryptionContext(
    branchKeyId: string,
    branchKeyVersion: string,
    timestamp: string,
    logicalKeyStoreName: string,
    kmsKeyArn: string,
    hierarchyVersion: Types.HierarchyVersion,
    customEncryptionContext: map<string, string>
  ): (output: map<string, string>)
    requires 0 < |branchKeyId|
    requires 0 < |branchKeyVersion|
    ensures BranchKeyContext?(output)
    ensures BRANCH_KEY_TYPE_PREFIX < output[TYPE_FIELD]
    ensures BRANCH_KEY_ACTIVE_VERSION_FIELD !in output
    ensures output[KMS_FIELD] == kmsKeyArn
    ensures output[TABLE_FIELD] == logicalKeyStoreName
    ensures forall k <- customEncryptionContext
              ::
                && ENCRYPTION_CONTEXT_PREFIX + k in output
                && output[ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k]
  {
    // Dafny needs some help.
    // Adding a fixed string
    // will not make any of the keys collide.
    // However, this leaks a lot of complexity.
    // This is why the function is now opaque.
    // Otherwise things timeout
    assert forall k <- customEncryptionContext.Keys
        ::
          k == (ENCRYPTION_CONTEXT_PREFIX + k)[|ENCRYPTION_CONTEXT_PREFIX|..];

    map[
      BRANCH_KEY_IDENTIFIER_FIELD := branchKeyId,
      TYPE_FIELD := BRANCH_KEY_TYPE_PREFIX + branchKeyVersion,
      KEY_CREATE_TIME := timestamp,
      TABLE_FIELD := logicalKeyStoreName,
      KMS_FIELD := kmsKeyArn,
      HIERARCHY_VERSION := match hierarchyVersion
      case v1 => HIERARCHY_VERSION_VALUE_1
      case v2 => HIERARCHY_VERSION_VALUE_2
    ] + map k <- customEncryptionContext :: ENCRYPTION_CONTEXT_PREFIX + k := customEncryptionContext[k]
  }

  function ActiveBranchKeyEncryptionContext(
    decryptOnlyEncryptionContext: map<string, string>
  ): (output: map<string, string>)
    requires BranchKeyContext?(decryptOnlyEncryptionContext)
    requires
      && BRANCH_KEY_TYPE_PREFIX < decryptOnlyEncryptionContext[TYPE_FIELD]
      && BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext
    ensures BranchKeyContext?(output)
    ensures output[HIERARCHY_VERSION] == decryptOnlyEncryptionContext[HIERARCHY_VERSION]
    ensures BRANCH_KEY_ACTIVE_VERSION_FIELD in output
  {
    decryptOnlyEncryptionContext + map[
      BRANCH_KEY_ACTIVE_VERSION_FIELD := decryptOnlyEncryptionContext[TYPE_FIELD],
      TYPE_FIELD := BRANCH_KEY_ACTIVE_TYPE
    ]
  }

  function BeaconKeyEncryptionContext(
    decryptOnlyEncryptionContext: map<string, string>
  ): (output: map<string, string>)
    requires BranchKeyContext?(decryptOnlyEncryptionContext)
    requires
      && BRANCH_KEY_TYPE_PREFIX < decryptOnlyEncryptionContext[TYPE_FIELD]
      && BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext
    ensures BranchKeyContext?(output)
    ensures output[HIERARCHY_VERSION] == decryptOnlyEncryptionContext[HIERARCHY_VERSION]
    ensures output[TYPE_FIELD] == BEACON_KEY_TYPE_VALUE
  {
    decryptOnlyEncryptionContext + map[
      TYPE_FIELD := BEACON_KEY_TYPE_VALUE
    ]
  }

  function ReplaceMutableContext(
    branchKeyContext: map<string, string>,
    terminalKmsArn: string,
    terminalCustomEncryptionContext: map<string, string>
  ) : (output: map<string, string>)

    requires BranchKeyContext?(branchKeyContext)
    requires BRANCH_KEY_RESTRICTED_FIELD_NAMES !! terminalCustomEncryptionContext.Keys

    ensures BranchKeyContext?(output)
    ensures output[KMS_FIELD] == terminalKmsArn
    ensures
      && branchKeyContext[BRANCH_KEY_IDENTIFIER_FIELD] == output[BRANCH_KEY_IDENTIFIER_FIELD]
      && branchKeyContext[TYPE_FIELD] == output[TYPE_FIELD]
      && branchKeyContext[KEY_CREATE_TIME] == output[KEY_CREATE_TIME]
      && branchKeyContext[HIERARCHY_VERSION] == output[HIERARCHY_VERSION]
      && branchKeyContext[TABLE_FIELD] == output[TABLE_FIELD]
      && (BRANCH_KEY_ACTIVE_VERSION_FIELD in branchKeyContext
          <==>
          && BRANCH_KEY_ACTIVE_VERSION_FIELD in output
          && branchKeyContext[BRANCH_KEY_ACTIVE_VERSION_FIELD] == output[BRANCH_KEY_ACTIVE_VERSION_FIELD])
  {
    terminalCustomEncryptionContext
    + if BRANCH_KEY_ACTIVE_VERSION_FIELD in branchKeyContext then
      map[
        BRANCH_KEY_IDENTIFIER_FIELD := branchKeyContext[BRANCH_KEY_IDENTIFIER_FIELD],
        TYPE_FIELD := branchKeyContext[TYPE_FIELD],
        KEY_CREATE_TIME := branchKeyContext[KEY_CREATE_TIME],
        HIERARCHY_VERSION := branchKeyContext[HIERARCHY_VERSION],
        TABLE_FIELD := branchKeyContext[TABLE_FIELD],
        KMS_FIELD := terminalKmsArn,
        BRANCH_KEY_ACTIVE_VERSION_FIELD := branchKeyContext[BRANCH_KEY_ACTIVE_VERSION_FIELD]
      ]
    else
      map[
        BRANCH_KEY_IDENTIFIER_FIELD := branchKeyContext[BRANCH_KEY_IDENTIFIER_FIELD],
        TYPE_FIELD := branchKeyContext[TYPE_FIELD],
        KEY_CREATE_TIME := branchKeyContext[KEY_CREATE_TIME],
        HIERARCHY_VERSION := branchKeyContext[HIERARCHY_VERSION],
        TABLE_FIELD := branchKeyContext[TABLE_FIELD],
        KMS_FIELD := terminalKmsArn
      ]
  }

  function NewVersionFromActiveBranchKeyEncryptionContext(
    activeBranchKeyEncryptionContext: map<string, string>,
    branchKeyVersion: string,
    timestamp: string
  ): (output: map<string, string>)
    requires BranchKeyContext?(activeBranchKeyEncryptionContext)
    requires BRANCH_KEY_ACTIVE_VERSION_FIELD in activeBranchKeyEncryptionContext
    requires 0 < |branchKeyVersion|

    ensures BranchKeyContext?(output)
    ensures BRANCH_KEY_TYPE_PREFIX < output[TYPE_FIELD]
    ensures BRANCH_KEY_ACTIVE_VERSION_FIELD !in output
  {
    activeBranchKeyEncryptionContext
    + map[
      TYPE_FIELD := BRANCH_KEY_TYPE_PREFIX + branchKeyVersion,
      KEY_CREATE_TIME := timestamp
    ]
    - {BRANCH_KEY_ACTIVE_VERSION_FIELD}
  }

  //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#record-format
  //= type=implication
  //# A branch key record MAY include [custom encryption context](../branch-key-store.md#custom-encryption-context) key-value pairs.

  //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#record-format
  //= type=implication
  //# A branch key record MUST include the following key-value pairs:
  predicate BranchKeyItem?(m: DDB.AttributeMap) {
    && BRANCH_KEY_IDENTIFIER_FIELD in m && m[BRANCH_KEY_IDENTIFIER_FIELD].S?
    && TYPE_FIELD in m && m[TYPE_FIELD].S?
    && KEY_CREATE_TIME in m && m[KEY_CREATE_TIME].S?
    && HIERARCHY_VERSION in m && m[HIERARCHY_VERSION].N?
    && TABLE_FIELD !in m
    && KMS_FIELD in m && m[KMS_FIELD].S?
    && BRANCH_KEY_FIELD in m && m[BRANCH_KEY_FIELD].B?

    && 0 < |m[BRANCH_KEY_IDENTIFIER_FIELD].S|
    && 0 < |m[TYPE_FIELD].S|

    && (forall k <- m.Keys - {BRANCH_KEY_FIELD, HIERARCHY_VERSION} :: m[k].S?)

    && (BRANCH_KEY_ACTIVE_VERSION_FIELD in m <==>
        && m[TYPE_FIELD].S == BRANCH_KEY_ACTIVE_TYPE)
    && (BRANCH_KEY_ACTIVE_VERSION_FIELD in m ==>
          && BRANCH_KEY_TYPE_PREFIX < m[BRANCH_KEY_ACTIVE_VERSION_FIELD].S)

    && (BRANCH_KEY_ACTIVE_VERSION_FIELD !in m <==>
        || m[TYPE_FIELD].S == BEACON_KEY_TYPE_VALUE
        || BRANCH_KEY_TYPE_PREFIX < m[TYPE_FIELD].S)
  }

  predicate ActiveHierarchicalSymmetricKey?(key: Types.EncryptedHierarchicalKey) {
    && EncryptedHierarchicalKeyFromStorage?(key)
    && key.Type.ActiveHierarchicalSymmetricVersion?
  }

  predicate DecryptOnlyHierarchicalSymmetricKey?(key: Types.EncryptedHierarchicalKey) {
    && EncryptedHierarchicalKeyFromStorage?(key)
    && key.Type.HierarchicalSymmetricVersion?
  }

  predicate ActiveHierarchicalSymmetricBeaconKey?(key: Types.EncryptedHierarchicalKey) {
    && EncryptedHierarchicalKeyFromStorage?(key)
    && key.Type.ActiveHierarchicalSymmetricBeacon?
  }

  lemma BranchKeyItemsDoNotCollide(
    a: Types.EncryptedHierarchicalKey,
    b: Types.EncryptedHierarchicalKey,
    c: Types.EncryptedHierarchicalKey
  )
    requires
      && ActiveHierarchicalSymmetricKey?(a)
      && DecryptOnlyHierarchicalSymmetricKey?(b)
      && ActiveHierarchicalSymmetricBeaconKey?(c)
    requires a.Identifier == b.Identifier == c.Identifier
    ensures a.Type != b.Type
    ensures a.Type != c.Type
    ensures c.Type != b.Type
  {}

  lemma ToAttributeMapIsCorrect(
    key: Types.EncryptedHierarchicalKey,
    item: DDB.AttributeMap
  )
    requires EncryptedHierarchicalKeyFromStorage?(key)
    requires (forall k <- key.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
    requires item == ToAttributeMap(key)

    ensures item.Keys == key.EncryptionContext.Keys + {BRANCH_KEY_FIELD} - {TABLE_FIELD}
    ensures item[BRANCH_KEY_FIELD].B == key.CiphertextBlob
    ensures
      && (forall k <- item.Keys - {BRANCH_KEY_FIELD, HIERARCHY_VERSION}
            ::
              && item[k].S?
              && key.EncryptionContext[k] == item[k].S
         )
      && key.EncryptionContext[HIERARCHY_VERSION] == item[HIERARCHY_VERSION].N
      && key.CiphertextBlob == item[BRANCH_KEY_FIELD].B
  {}

  lemma ToEncryptedHierarchicalKeyIsCorrect(
    key: Types.EncryptedHierarchicalKey,
    logicalKeyStoreName: string,
    item: DDB.AttributeMap
  )
    requires BranchKeyItem?(item)
    requires key == ToEncryptedHierarchicalKey(item, logicalKeyStoreName)

    ensures key.EncryptionContext.Keys == item.Keys - {BRANCH_KEY_FIELD} + {TABLE_FIELD}
    ensures key.EncryptionContext[TABLE_FIELD] == logicalKeyStoreName

    ensures
      forall k <- key.EncryptionContext.Keys - {BRANCH_KEY_FIELD, TABLE_FIELD}
        ::
          match k
          case HIERARCHY_VERSION => key.EncryptionContext[k] == item[k].N
          case _ => key.EncryptionContext[k] == item[k].S

    ensures BRANCH_KEY_FIELD !in key.EncryptionContext
  {}

  lemma {:vcs_split_on_every_assert} EncryptionContextConstructorsAreCorrect(
    branchKeyId: string,
    branchKeyVersion: string,
    timestamp: string,
    logicalKeyStoreName: string,
    kmsKeyArn: string,
    hierarchyVersion: Types.HierarchyVersion,
    encryptionContext: map<string, string>
  )
    requires 0 < |branchKeyId|
    requires 0 < |branchKeyVersion|
    ensures
      var decryptOnly := DecryptOnlyBranchKeyEncryptionContext(
                           branchKeyId, branchKeyVersion, timestamp, logicalKeyStoreName, kmsKeyArn, hierarchyVersion, encryptionContext);
      var active := ActiveBranchKeyEncryptionContext(decryptOnly);
      var beacon := BeaconKeyEncryptionContext(decryptOnly);
      && decryptOnly[TYPE_FIELD] != active[TYPE_FIELD]
      && decryptOnly[TYPE_FIELD] != beacon[TYPE_FIELD]
      && active[TYPE_FIELD] != beacon[TYPE_FIELD]
      && (forall k <- decryptOnly.Keys - {TYPE_FIELD} ::
            && decryptOnly[k] == active[k] == beacon[k]
         )
      && active[BRANCH_KEY_ACTIVE_VERSION_FIELD] == decryptOnly[TYPE_FIELD]
         //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context
         //= type=implication
         //# If custom [encryption context](./structures.md#encryption-context-3)
         //# is associated with the branch key these values MUST be added to the AWS KMS encryption context.
      && (forall k <- encryptionContext ::
            //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context
            //= type=implication
            //# To avoid name collisions each added attribute from the custom [encryption context](./structures.md#encryption-context-3)
            //# MUST be prefixed with `aws-crypto-ec:`.
            && (ENCRYPTION_CONTEXT_PREFIX + k in decryptOnly)
            && (ENCRYPTION_CONTEXT_PREFIX + k in active)
            && (ENCRYPTION_CONTEXT_PREFIX + k in beacon)
               //= aws-encryption-sdk-specification/framework/branch-key-store.md#custom-encryption-context
               //= type=implication
               //# Across all versions of a Branch Key, the custom encryption context MUST be equal.
            && encryptionContext[k]
            == decryptOnly[ENCRYPTION_CONTEXT_PREFIX + k]
            == active[ENCRYPTION_CONTEXT_PREFIX + k]
            == beacon[ENCRYPTION_CONTEXT_PREFIX + k]
         )
  {
    reveal DecryptOnlyBranchKeyEncryptionContext();
  }

  lemma ToAttributeMapAndToEncryptedHierarchicalKeyAreInverse(
    key: Types.EncryptedHierarchicalKey,
    item: DDB.AttributeMap
  )
    requires BranchKeyItem?(item) && EncryptedHierarchicalKeyFromStorage?(key)

    ensures
      && (forall k <- key.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
      && item == ToAttributeMap(key)
         <==>
         ToEncryptedHierarchicalKey(item, key.EncryptionContext[TABLE_FIELD]) == key
  {}

  predicate MutationCommitmentAttribute?(m: DDB.AttributeMap) {
    && BRANCH_KEY_IDENTIFIER_FIELD in m && m[BRANCH_KEY_IDENTIFIER_FIELD].S?
    && KEY_CREATE_TIME in m && m[KEY_CREATE_TIME].S?
    && TYPE_FIELD in m && m[TYPE_FIELD].S?
    && M_UUID in m && m[M_UUID].S?
    && HIERARCHY_VERSION in m && m[HIERARCHY_VERSION].N? && m[HIERARCHY_VERSION].N == HIERARCHY_VERSION_VALUE

    && 0 < |m[BRANCH_KEY_IDENTIFIER_FIELD].S|
    && 0 < |m[TYPE_FIELD].S|
    && 0 < |m[M_UUID].S|

    && (forall k <- m.Keys - {M_ORIGINAL, M_TERMINAL, HIERARCHY_VERSION, ENC_FIELD, M_INPUT} :: m[k].S?)

    && m[TYPE_FIELD].S == MUTATION_COMMITMENT_TYPE

    // Structure & DefaultKeyStorage do not care about the Byte structure of the original or terminal.
    // That is the concern of Mutation State Structures.
    // Structure & DefaultKeyStorage care that these are non-empty Byte Fields.
    && M_ORIGINAL in m && m[M_ORIGINAL].B? && 0 < |m[M_ORIGINAL].B|
    && M_TERMINAL in m && m[M_TERMINAL].B? && 0 < |m[M_TERMINAL].B|
    && ENC_FIELD in m && m[ENC_FIELD].B? && 0 < |m[ENC_FIELD].B|
    && M_INPUT in m && m[M_INPUT].B? && 0 < |m[M_INPUT].B|

    && m.Keys == {
                   TYPE_FIELD,
                   HIERARCHY_VERSION,
                   BRANCH_KEY_IDENTIFIER_FIELD,
                   KEY_CREATE_TIME,
                   M_UUID,
                   M_ORIGINAL,
                   M_TERMINAL,
                   ENC_FIELD,
                   M_INPUT
                 }
  }

  predicate MutationCommitment?(m: Types.MutationCommitment)
  {
    && 0 < |m.Identifier|
    && 0 < |m.UUID|
    && 0 < |m.Original|
    && 0 < |m.Terminal|
    && 0 < |m.CiphertextBlob|
    && 0 < |m.Input|
  }

  function ToMutationCommitment(
    item: DDB.AttributeMap
  ): (output: Types.MutationCommitment)
    requires MutationCommitmentAttribute?(item)
    ensures MutationCommitment?(output)
  {
    Types.MutationCommitment(
      Identifier := item[BRANCH_KEY_IDENTIFIER_FIELD].S,
      CreateTime := item[KEY_CREATE_TIME].S,
      UUID := item[M_UUID].S,
      Original := item[M_ORIGINAL].B,
      Terminal := item[M_TERMINAL].B,
      CiphertextBlob := item[ENC_FIELD].B,
      Input := item[M_INPUT].B
    )
  }

  function MutationCommitmentToAttributeMap(
    lock: Types.MutationCommitment
  ): (output: DDB.AttributeMap)
    requires MutationCommitment?(lock)
    ensures MutationCommitmentAttribute?(output)
  {
    map[
      TYPE_FIELD := DDB.AttributeValue.S(MUTATION_COMMITMENT_TYPE),
      HIERARCHY_VERSION := HIERARCHY_VERSION_ATTRIBUTE_VALUE,
      BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(lock.Identifier),
      KEY_CREATE_TIME := DDB.AttributeValue.S(lock.CreateTime),
      M_UUID := DDB.AttributeValue.S(lock.UUID),
      M_ORIGINAL := DDB.AttributeValue.B(lock.Original),
      M_TERMINAL := DDB.AttributeValue.B(lock.Terminal),
      ENC_FIELD := DDB.AttributeValue.B(lock.CiphertextBlob),
      M_INPUT := DDB.AttributeValue.B(lock.Input)
    ]
  }

  lemma MutationCommitmentAndMutationCommitmentToAttributeMapAreInverse(
    item: DDB.AttributeMap,
    lock: Types.MutationCommitment
  )
    requires MutationCommitmentAttribute?(item)
    requires MutationCommitment?(lock)
    ensures
      ToMutationCommitment(item) == lock <==> MutationCommitmentToAttributeMap(lock) == item
  {}

  predicate MutationIndexAttribute?(m: DDB.AttributeMap) {
    && BRANCH_KEY_IDENTIFIER_FIELD in m && m[BRANCH_KEY_IDENTIFIER_FIELD].S? && 0 < |m[BRANCH_KEY_IDENTIFIER_FIELD].S|
    && KEY_CREATE_TIME in m && m[KEY_CREATE_TIME].S?
    && TYPE_FIELD in m && m[TYPE_FIELD].S? && 0 < |m[TYPE_FIELD].S|
    && HIERARCHY_VERSION in m && m[HIERARCHY_VERSION].N? && m[HIERARCHY_VERSION].N == HIERARCHY_VERSION_VALUE
    && M_UUID in m && m[M_UUID].S? && 0 < |m[M_UUID].S|

    && (forall k <- m.Keys - {M_PAGE_INDEX, HIERARCHY_VERSION, ENC_FIELD} :: m[k].S?)
    && m[TYPE_FIELD].S == MUTATION_INDEX_TYPE
       // Structure & DefaultKeyStorage do not care about these Byte structures.
       // That is the concern of Mutation State Structures.
       // Structure & DefaultKeyStorage care that these are non-empty Byte Fields.
    && ENC_FIELD in m && m[ENC_FIELD].B? && 0 < |m[ENC_FIELD].B|
    && M_PAGE_INDEX in m && m[M_PAGE_INDEX].B? && 0 < |m[M_PAGE_INDEX].B|

    && m.Keys == {
                   TYPE_FIELD,
                   HIERARCHY_VERSION,
                   BRANCH_KEY_IDENTIFIER_FIELD,
                   KEY_CREATE_TIME,
                   M_UUID,
                   M_PAGE_INDEX,
                   ENC_FIELD
                 }
  }

  predicate MutationIndex?(m: Types.MutationIndex)
  {
    && 0 < |m.Identifier|
    && 0 < |m.UUID|
    && 0 < |m.PageIndex|
    && 0 < |m.CiphertextBlob|
  }

  function ToMutationIndex(
    item: DDB.AttributeMap
  ): (output: Types.MutationIndex)
    requires MutationIndexAttribute?(item)
    ensures MutationIndex?(output)
  {
    Types.MutationIndex(
      Identifier := item[BRANCH_KEY_IDENTIFIER_FIELD].S,
      CreateTime := item[KEY_CREATE_TIME].S,
      UUID := item[M_UUID].S,
      PageIndex := item[M_PAGE_INDEX].B,
      CiphertextBlob := item[ENC_FIELD].B
    )
  }

  function MutationIndexToAttributeMap(
    index: Types.MutationIndex
  ): (output: DDB.AttributeMap)
    requires MutationIndex?(index)
    ensures MutationIndexAttribute?(output)
  {
    map[
      TYPE_FIELD := DDB.AttributeValue.S(MUTATION_INDEX_TYPE),
      HIERARCHY_VERSION := HIERARCHY_VERSION_ATTRIBUTE_VALUE,
      BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(index.Identifier),
      KEY_CREATE_TIME := DDB.AttributeValue.S(index.CreateTime),
      M_UUID := DDB.AttributeValue.S(index.UUID),
      M_PAGE_INDEX := DDB.AttributeValue.B(index.PageIndex),
      ENC_FIELD := DDB.AttributeValue.B(index.CiphertextBlob)
    ]
  }

  lemma MutationIndexAndMutationIndexToAttributeMapAreInverse(
    item: DDB.AttributeMap,
    index: Types.MutationIndex
  )
    requires MutationIndexAttribute?(item)
    requires MutationIndex?(index)
    ensures
      ToMutationIndex(item) == index <==> MutationIndexToAttributeMap(index) == item
  {}
}
