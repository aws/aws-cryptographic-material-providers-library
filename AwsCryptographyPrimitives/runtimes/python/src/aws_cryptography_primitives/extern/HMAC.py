from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import hashes
import Wrappers
import _dafny
from aws_cryptography_primitives.internal_generated_dafny.HMAC import *
import aws_cryptography_primitives.internal_generated_dafny.Digest
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
      # Store a copy of the hmac at `Init` state,
      # so if we need to re-use this hmac after calling `GetResult`,
      # we can restore from this copy
      self.initted_hmac = self.hmac.copy()

    def BlockUpdate(self, input):
      input_bytes = bytes(input)
      self.hmac.update(input_bytes)

    def GetResult(self):
      digest = _dafny.Seq(self.hmac.finalize())
      # Dafny expects the hmac to be reset to its state at the `Init` call
      # after calling GetResult. Java mac provides this built-in,
      # but Python does not.
      self.hmac = self.initted_hmac.copy()
      return digest

aws_cryptography_primitives.internal_generated_dafny.HMAC.default__ = default__
aws_cryptography_primitives.internal_generated_dafny.HMAC.HMac = HMac