// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
 include "../src/Index.dfy"
 abstract module WrappedAbstractAwsCryptographyKeyStoreService {
 import opened Wrappers
 import opened StandardLibrary.UInt
 import opened UTF8
 import opened Types = AwsCryptographyKeyStoreTypes
 import WrappedService : AbstractAwsCryptographyKeyStoreService
 function method WrappedDefaultKeyStoreConfig(): KeyStoreConfig
 method {:extern} WrappedKeyStore(config: KeyStoreConfig := WrappedDefaultKeyStoreConfig())
 returns (res: Result<IKeyStoreClient, Error>)
 ensures res.Success? ==> 
 && fresh(res.value)
 && fresh(res.value.Modifies)
 && fresh(res.value.History)
 && res.value.ValidState()
}
