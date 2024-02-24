from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import hashes
import Wrappers
import _dafny
from aws_cryptography_primitives.internaldafny.generated.HMAC import *
import aws_cryptography_primitives.internaldafny.generated.Digest
from software_amazon_cryptography_primitives_internaldafny_types import (
    HMacInput
)

class default__:

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

class HMac:

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
      # Store a copy of the HMAC at `Init` state.
      # The Dafny implementation expects that calling `GetResult` will reset
      #   the HMAC back to its initial state when `Init` is called.
      # This is the default behavior for our HMAC libraries in .NET and Java
      #   but PyCA HMAC does not do this.
      # We must manually reset the HMAC.
      self.initial_hmac = self.hmac.copy()

    def BlockUpdate(self, input):
      input_bytes = bytes(input)
      self.hmac.update(input_bytes)

    def GetResult(self):
      digest = _dafny.Seq(self.hmac.finalize())
      # Dafny expects the HMAC to be reset to its state at the `Init` call
      # after calling GetResult.
      self.hmac = self.initial_hmac.copy()
      return digest

aws_cryptography_primitives.internaldafny.generated.HMAC.default__ = default__
aws_cryptography_primitives.internaldafny.generated.HMAC.HMac = HMac