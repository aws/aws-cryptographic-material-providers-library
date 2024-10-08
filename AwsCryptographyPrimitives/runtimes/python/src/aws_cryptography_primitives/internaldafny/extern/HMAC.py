# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import hashes

import _dafny

import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptography_primitives.internaldafny.generated.Digest
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    HMacInput
)
import aws_cryptography_primitives.internaldafny.generated.HMAC
from aws_cryptography_primitives.internaldafny.generated.HMAC import *

# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.HMAC.default__):

  @staticmethod
  def Digest(input: HMacInput):
      maybe_hmac = HMac.Build(input.digestAlgorithm)
      if maybe_hmac.IsFailure():
        return maybe_hmac.PropagateFailure()
      hmac = maybe_hmac.Extract()
      hmac.Init(input.key)
      hmac.BlockUpdate(input.message)
      output = hmac.GetResult()
      return Wrappers.Result_Success(_dafny.Seq(output))

# Extend generated class
class HMac(aws_cryptography_primitives.internaldafny.generated.HMAC.HMac):

    @staticmethod
    def Build(digest):
      output = HMac(digest)
      return Wrappers.Result_Success(output)

    def __init__(self, digest):
      if digest.is_SHA__256:
        self.algorithm = hashes.SHA256()
      elif digest.is_SHA__384:
        self.algorithm = hashes.SHA384()
      elif digest.is_SHA__512:
        self.algorithm = hashes.SHA512()
      else:
        raise ValueError()
      # self.hmac cannot be used until Init is called

    def Init(self, key):
      key_bytes = bytes(key)
      self.hmac = HMAC(key_bytes, self.algorithm)
      # Store a copy of the key_bytes at `Init` state.
      # The Dafny implementation expects that calling `GetResult` will reset
      #   the HMAC back to its initial state when `Init` is called.
      # This is the default behavior for our HMAC libraries in .NET and Java
      #   but PyCA HMAC does not do this.
      # We must manually reset the HMAC.
      self.initial_key_bytes = key_bytes

    def BlockUpdate(self, input):
      input_bytes = bytes(input)
      self.hmac.update(input_bytes)

    def GetResult(self):
      """
      Finishes the MAC operation.
      A call to this method resets this
      Mac object to the state it was in when
      previously initialized via a call to Init(Key).
      That is, the object is reset and available to
      generate another MAC from the same key, if desired,
      via new calls to update and doFinal. 
      """
      digest = _dafny.Seq(self.hmac.finalize())
      self.hmac = HMAC(self.initial_key_bytes, self.algorithm)
      return digest

# Export extern-extended classes into generated classes
aws_cryptography_primitives.internaldafny.generated.HMAC.default__ = default__
aws_cryptography_primitives.internaldafny.generated.HMAC.HMac = HMac