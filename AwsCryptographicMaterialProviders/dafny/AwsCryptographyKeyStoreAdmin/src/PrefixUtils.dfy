// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } PrefixUtils {
  // import opened Structure

  opaque function AddingPrefixToKeysOfMapDoesNotCreateCollisions(
    nameonly prefix: string,
    nameonly aMap: map<string, string>
  ): (output: map<string, string>)
    ensures forall k <- aMap
              ::
                && prefix + k in output
                && output[prefix + k] == aMap[k]
  {
    // Dafny needs some help.
    // Adding a fixed string
    // will not make any of the keys collide.
    // However, this leaks a lot of complexity.
    // This is why the function is now opaque.
    // Otherwise things timeout
    assert forall k <- aMap.Keys
        ::
          k == (prefix + k)[|prefix|..];

    map k <- aMap :: prefix + k := aMap[k]
  }

  // opaque function AddingPrefixToCustomEncryptionContextDoesNotImpactReserved(
  //   input: map<string, string>
  // ): (output: map<string, string>
  //   requires input.Keys !! BRANCH_KEY_RESTRICTED_FIELD_NAMES
  //   ensures output.Keys !! BRANCH_KEY_RESTRICTED_FIELD_NAMES
  //   ensures forall k <-

  // opaque function RemovingAPrefixFromAllKeysOfMapDoesNotCreateCollisions(
  //   nameonly prefix: string,
  //   nameonly aMap: map<string, string>
  // ): (output: map<string, string>)
  //   requires forall k <- aMap :: |prefix| < |k| && prefix < k
  //   ensures forall k <- aMap
  //   ::
  //     && k in aMap
  //     && k[|prefix| ..] in output
  //     && output[k[|prefix| ..] ] == aMap[k]
  //   {
  //     // Dafny needs some help.
  //     // Adding a fixed string
  //     // will not make any of the keys collide.
  //     // However, this leaks a lot of complexity.
  //     // This is why the function is now opaque.
  //     // Otherwise things timeout
  //     // assert forall k <- aMap.Keys
  //     //   ::
  //     //   k[|prefix|..] == (k - prefix);

  //     map k <- aMap :: k[|prefix| ..] := aMap[k]
  //   }
}
