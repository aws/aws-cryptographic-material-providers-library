// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "Materials.dfy"

module {:options "/functionSyntax:4" } CMM {
  import opened Wrappers
  import Types = AwsCryptographyMaterialProvidersTypes
  import Materials

  trait {:termination false} VerifiableInterface
    extends Types.ICryptographicMaterialsManager
  {

    ghost predicate GetEncryptionMaterialsEnsuresPublicly(input: Types.GetEncryptionMaterialsInput, output: Result<Types.GetEncryptionMaterialsOutput, Types.Error>)
      : (outcome: bool)
      ensures
        outcome ==>
          output.Success?
          ==>
            // if the output materials are valid then they contain the required fields
            //= aws-encryption-sdk-specification/framework/cmm-interface.md#get-encryption-materials
            //= type=implication
            //# The encryption materials returned MUST include the following:

            // See EncryptionMaterialsHasPlaintextDataKey for details
            //= aws-encryption-sdk-specification/framework/cmm-interface.md#get-encryption-materials
            //= type=implication
            //# The CMM MUST ensure that the encryption materials returned are valid.
            //# - The encryption materials returned MUST follow the specification for [encryption-materials](structures.md#encryption-materials).
            //# - The value of the plaintext data key MUST be non-NULL.
            //# - The plaintext data key length MUST be equal to the [key derivation input length](algorithm-suites.md#key-derivation-input-length).
            //# - The encrypted data keys list MUST contain at least one encrypted data key.
            //# - If the algorithm suite contains a signing algorithm, the encryption materials returned MUST include the generated signing key.
            //# - For every key in [Required Encryption Context Keys](structures.md#required-encryption-context-keys)
            //#   there MUST be a matching key in the [Encryption Context](structures.md#encryption-context-1).
            && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.encryptionMaterials)
            //= aws-encryption-sdk-specification/framework/cmm-interface.md#get-encryption-materials
            //= type=implication
            //# - The [Required Encryption Context Keys](structures.md#required-encryption-context-keys) MUST be
            //#   a super set of the Required Encryption Context Keys in the [encryption materials request](#encryption-materials-request).
            && RequiredEncryptionContextKeys?(input.requiredEncryptionContextKeys, output.value.encryptionMaterials)

    ghost predicate DecryptMaterialsEnsuresPublicly(input: Types.DecryptMaterialsInput, output: Result<Types.DecryptMaterialsOutput, Types.Error>)
      : (outcome: bool)
      ensures
        outcome ==>
          // if the output materials are valid then they contain the required fields
          //= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials
          //= type=implication
          //# The decryption materials returned MUST include the following:
          && (output.Success?
              //= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials
              //= type=implication
              //# The CMM MUST ensure that the decryption materials returned are valid.
              //# - The decryption materials returned MUST follow the specification for [decryption-materials](structures.md#decryption-materials).
              //# - The value of the plaintext data key MUST be non-NULL.
              ==> Materials.DecryptionMaterialsWithPlaintextDataKey(output.value.decryptionMaterials))
          //= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials
          //# The CMM MUST validate the [Encryption Context](structures.md#encryption-context)
          //# by comparing it to the customer supplied [Reproduced Encryption Context](structures.md#encryption-context)
          //# in [decrypt materials request](#decrypt-materials-request).
          //# For every key that exists in both [Reproduced Encryption Context](structures.md#encryption-context)
          //# and [Encryption Context](structures.md#encryption-context),
          //# the values MUST be equal or the operation MUST fail.
          && (output.Success? ==> ReproducedEncryptionContext?(input))
          && (!ReproducedEncryptionContext?(input) ==> output.Failure?)
          //= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials
          //# - All key-value pairs that exist in [Reproduced Encryption Context](structures.md#encryption-context)
          //# but do not exist in encryption context on the [decrypt materials request](#decrypt-materials-request)
          //# SHOULD be appended to the decryption materials.
          && (output.Success? ==> EncryptionContextComplete(input, output.value.decryptionMaterials))
  }

  predicate RequiredEncryptionContextKeys?(requiredEncryptionContextKeys: Option<Types.EncryptionContextKeys>, encryptionMaterials: Types.EncryptionMaterials) {
    forall k <- requiredEncryptionContextKeys.UnwrapOr([])
      :: k in encryptionMaterials.requiredEncryptionContextKeys
  }

  predicate EncryptionContextComplete(input: Types.DecryptMaterialsInput, decryptionMaterials: Types.DecryptionMaterials) {
    var reproducedEncryptionContext := input.reproducedEncryptionContext.UnwrapOr(map[]);
    forall k <- reproducedEncryptionContext
      ::
        && k in decryptionMaterials.encryptionContext
        && decryptionMaterials.encryptionContext[k] == reproducedEncryptionContext[k]
  }

  predicate ReproducedEncryptionContext?(input: Types.DecryptMaterialsInput) {
    var reproducedEncryptionContext := input.reproducedEncryptionContext.UnwrapOr(map[]);
    forall k <- reproducedEncryptionContext
           | k in input.encryptionContext
      :: input.encryptionContext[k] == reproducedEncryptionContext[k]
  }
}
