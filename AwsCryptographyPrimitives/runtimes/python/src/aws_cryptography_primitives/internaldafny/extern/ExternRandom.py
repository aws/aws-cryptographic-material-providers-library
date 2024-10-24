# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import secrets

import _dafny

import aws_cryptography_primitives.internaldafny.generated.ExternRandom
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptography_primitives.internaldafny.generated.ExternRandom
from aws_cryptography_primitives.internaldafny.generated.ExternRandom import *

# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.ExternRandom.default__):

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

# Export extern-extended class into generated class
aws_cryptography_primitives.internaldafny.generated.ExternRandom.default__ = default__
