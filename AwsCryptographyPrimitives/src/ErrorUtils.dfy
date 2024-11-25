// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyPrimitivesTypes.dfy"

module {:options "/functionSyntax:4"} ErrorUtils {
  import opened Wrappers
  import Types = AwsCryptographyPrimitivesTypes

  function ExtractMessageFromError(
    error: Types.Error
  ): (errorMessage?: Option<string>)
  {
    match error {
      case Opaque(obj) => None
      case AwsCryptographicPrimitivesError(s) => Some(s)
      case OpaqueWithText(obj, objMessage) => Some(objMessage)
      case CollectionOfErrors(_, s) => Some(s)
    }
  }

  function MessageOrUnknown(
    error: Types.Error
  ): (errorMessage: string)
  {
    var msg? := ExtractMessageFromError(error);
    if msg?.Some? then msg?.value else " unkown."
  }
}
