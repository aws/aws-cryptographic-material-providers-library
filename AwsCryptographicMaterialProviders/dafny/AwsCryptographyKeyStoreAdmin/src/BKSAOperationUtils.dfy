// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../../dafny/AwsCryptographyKeyStore/src/KmsUtils.dfy"

/** Utilities to simplify the logic in AwsCryptographyKeyStoreAdminOperations. */
module {:options "/functionSyntax:4" } BKSAOperationUtils {
  import opened Wrappers
  import KeyStoreTypes = AwsCryptographyKeyStoreOperations.Types
  import KmsUtils

  // TODO-HV-2-FOLLOW : It may help the BKS proofs to use this datatype
  /** Constrains the relationship of the storage & KMS client(s), 
    ensuring they a valid but their histories are separate. */
  datatype KeyManagerAndStorage = KeyManagerAndStorage(
    storage : KeyStoreTypes.IKeyStorageInterface,
    keyManagerStrat: KmsUtils.keyManagerStrat
  )
  {
    ghost predicate ValidState()
    {
      && storage.ValidState()
      && keyManagerStrat.ValidState()
      && storage.Modifies !! keyManagerStrat.Modifies
    }
    ghost const Modifies := multiset(storage.Modifies) + multiset(keyManagerStrat.Modifies)
  }

}