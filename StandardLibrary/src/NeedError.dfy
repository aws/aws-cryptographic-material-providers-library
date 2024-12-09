// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../libraries/src/Wrappers.dfy"

module {:options "/functionSyntax:4"} StandardLibrary.NeedError {
  import opened Wrappers

  function NeedOutcome<E>(
    condition: bool,
    error: () --> E)
    : (result: Outcome2<E>)
    requires !condition ==> error.requires()
  {
    if condition then Outcome2.Pass else Outcome2.Fail(error())
  }

  datatype Outcome2<E> = Pass | Fail(error: E)
  {
    predicate IsFailure() {
      Fail?
    }
    // Note: PropagateFailure returns a Result, not an Outcome.
    function PropagateFailure(): Outcome<E>
      requires Fail?
    {
      Outcome.Fail(this.error)
    }
    // Note: no Extract method
  }
}
