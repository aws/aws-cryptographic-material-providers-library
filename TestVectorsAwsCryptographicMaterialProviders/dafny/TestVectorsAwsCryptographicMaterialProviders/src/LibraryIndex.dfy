// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypesWrapped.dfy"
include "../../../../AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders/src/Index.dfy"

module
{:extern "software.amazon.cryptography.materialproviders.internaldafny.wrapped" }
  WrappedMaterialProviders refines WrappedAbstractAwsCryptographyMaterialProvidersService
{
  import WrappedService = MaterialProviders

  function method WrappedDefaultMaterialProvidersConfig(): MaterialProvidersConfig
  {
    MaterialProvidersConfig
  }

  method WrappedMaterialProviders(config: MaterialProvidersConfig)
    returns (res: Result<IAwsCryptographicMaterialProvidersClient, Error>)
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies)
              && fresh(res.value.History)
              && res.value.ValidState()
  {
	  res := WrappedService.MaterialProviders(config);
  }

}
