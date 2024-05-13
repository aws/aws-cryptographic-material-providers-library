// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0


using software.amazon.cryptography.primitives.internaldafny.types;
using Wrappers_Compile;
using icharseq = Dafny.ISequence<char>;
using ibyteseq = Dafny.ISequence<byte>;
using byteseq = Dafny.Sequence<byte>;
using _IError = software.amazon.cryptography.primitives.internaldafny.types._IError;
using Error_Opaque = software.amazon.cryptography.primitives.internaldafny.types.Error_Opaque;

namespace ECDH
{
    public partial class KeyGeneration
    {
        public static _IResult<EccKeyPair, _IError> GenerateKeyPair(_IECDHCurveSpec x)
        {
            return Result<EccKeyPair, _IError>
                .create_Failure(new Error_Opaque("Implement me!"));

        }

    }
}
