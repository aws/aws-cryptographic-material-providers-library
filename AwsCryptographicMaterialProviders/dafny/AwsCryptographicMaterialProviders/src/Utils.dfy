// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module {:options "/functionSyntax:4" } Utils {
  import Crypto = AwsCryptographyPrimitivesTypes
  import AtomicPrimitives
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened Seq
  import opened Wrappers

  method {:vcs_split_on_every_assert} GetPublicKey(
    curveSpec: Crypto.ECDHCurveSpec,
    privateKey: Crypto.ECCPrivateKey,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res: Result<seq<uint8>, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.GetPublicKeyFromPrivateKey| > 0
              && Last(crypto.History.GetPublicKeyFromPrivateKey).output.Success?
              && Last(crypto.History.GetPublicKeyFromPrivateKey).input
                 == Crypto.GetPublicKeyFromPrivateKeyInput(
                      eccCurve :=  curveSpec,
                      privateKey := privateKey
                    )
  {
    var maybePublicKey := crypto.GetPublicKeyFromPrivateKey(
      Crypto.GetPublicKeyFromPrivateKeyInput(
        eccCurve :=  curveSpec,
        privateKey := privateKey
      )
    );

    var keyPairOutput :- maybePublicKey.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));
    res := Success(keyPairOutput.publicKey);
  }
}
