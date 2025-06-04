// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } PrefixUtils {
  // import opened Structure

  function AddingPrefixToKeysOfMapDoesNotCreateCollisions(
    nameonly prefix: string,
    nameonly aMap: map<string, string>
  ): (output: map<string, string>)
    ensures forall k <- aMap
              ::
                && k == (prefix + k)[|prefix|..]
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

  opaque function FilterMapForKeysThatDoNotBeginWithPrefix (
    nameonly prefix: string,
    nameonly aMap: map<string, string>
  ): (output: map<string, string>)
    ensures forall k <- output
              ::
                && !( prefix < k)
                && k in aMap
                && output[k] == aMap[k]
  {
    var filteredKeys
      :=
      set k <- aMap
          | !(prefix < k)
        ::
          k;
    map i <- filteredKeys :: i := aMap[i]
  }
}
