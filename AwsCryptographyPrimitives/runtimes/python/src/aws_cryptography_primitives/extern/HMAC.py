# from cryptography.hazmat.primitives.hmac import HMAC
# from cryptography.hazmat.primitives import hashes
import hmac
import hashlib
from cryptography.exceptions import AlreadyFinalized
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
      print("digest")
      print(digest)
      print(digest.is_SHA__256)
      if digest.is_SHA__256:
        self.algorithm = hashlib.sha256
      elif digest.is_SHA__384:
        self.algorithm = hashlib.sha384
      elif digest.is_SHA__512:
        self.algorithm = hashlib.sha512
      else:
        raise ValueError()

      # if digest.is_SHA__256:
      #   self.algorithm = hashes.SHA256()
      # elif digest.is_SHA__384:
      #   self.algorithm = hashes.SHA384()
      # elif digest.is_SHA__512:
      #   self.algorithm = hashes.SHA512()
      # else:
      #   raise ValueError()
      # self.hmac cannot be used until Init is called

    def Init(self, key):
      key_bytes = bytes(key)
      # self.hmac = HMAC(key_bytes, self.algorithm)
      print("INIT")
      print(self.algorithm)
      self.hmac = hmac.new(key_bytes, msg=None, digestmod=self.algorithm)

    def BlockUpdate(self, input):
      print("INPUT")
      print(_dafny.string_of(input))
      input_bytes = bytes(input)
      # self.hmac.update(input_bytes)
      self.hmac.update(input_bytes)
      print(_dafny.string_of(_dafny.Seq(self.hmac.digest())))

    def GetResult(self):
      # temp_hmac = self.hmac.copy()
      # print("temp_hmac")
      # print(temp_hmac)
      # a = temp_hmac.finalize()
      # print(a)
      # return _dafny.Seq(a)
      return _dafny.Seq(self.hmac.digest())

aws_cryptography_primitives.internal_generated_dafny.HMAC.default__ = default__
aws_cryptography_primitives.internal_generated_dafny.HMAC.HMac = HMac