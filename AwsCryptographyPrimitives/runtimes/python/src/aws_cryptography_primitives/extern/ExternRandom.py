from aws_cryptography_primitives.internal_generated_dafny.ExternRandom import *
import aws_cryptography_primitives.internal_generated_dafny.ExternRandom
import secrets
import Wrappers
import _dafny

class default__:

    @staticmethod
    def GenerateBytes(i):
        #= compliance/data-format/message-header.txt#2.5.1.6
        # While
        # implementations cannot guarantee complete uniqueness, implementations
        # MUST use a good source of randomness when generating messages IDs in
        # order to make the chance of duplicate IDs negligible.
        return Wrappers.Result_Success(
            _dafny.Seq(secrets.token_bytes(i))
        )

aws_cryptography_primitives.internal_generated_dafny.ExternRandom.default__ = default__
