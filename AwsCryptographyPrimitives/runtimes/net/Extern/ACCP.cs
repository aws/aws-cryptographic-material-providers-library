// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

using software.amazon.cryptography.primitives.internaldafny.types;
using Wrappers_Compile;
using _IHKDFProvider = software.amazon.cryptography.primitives.internaldafny.types._IHKDFProvider;
using _HKDFProvider = software.amazon.cryptography.primitives.internaldafny.types.HKDFProvider;
using _IHkdfExtractInput = software.amazon.cryptography.primitives.internaldafny.types._IHkdfExtractInput;
using _IHkdfExpandInput = software.amazon.cryptography.primitives.internaldafny.types._IHkdfExpandInput;
using _IError = software.amazon.cryptography.primitives.internaldafny.types._IError;

namespace ACCP
{
    public partial class ACCPUtils
    {
        public static _IResult<_IHKDFProvider, _IError> ExternCheckForAccp()
        {
            return Result<_IHKDFProvider, _IError>.create_Success(_HKDFProvider.create_MPL());
        }
    }

    public partial class ACCP_HKDF
    {
        public static
          _IResult<Dafny.ISequence<byte>, _IError> ExternExtract(_IHkdfExtractInput input)
        {
            return Result<Dafny.ISequence<byte>, _IError>.create_Failure(
              software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(
                AWS.Cryptography.Primitives.TypeConversion.ToDafny_N6_smithy__N3_api__S6_String("ACCP is not supported in .NET")));
        }

        public static
          _IResult<Dafny.ISequence<byte>, _IError> ExternExpand(_IHkdfExpandInput input)
        {
            return Result<Dafny.ISequence<byte>, _IError>.create_Failure(
              software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(
                AWS.Cryptography.Primitives.TypeConversion.ToDafny_N6_smithy__N3_api__S6_String("ACCP is not supported in .NET")));
        }

        public static
          _IResult<Dafny.ISequence<byte>, _IError> ExternHkdf(_IHkdfInput input)
        {
            return Result<Dafny.ISequence<byte>, _IError>.create_Failure(
              software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(
                AWS.Cryptography.Primitives.TypeConversion.ToDafny_N6_smithy__N3_api__S6_String("ACCP is not supported in .NET")));
        }
    }
}
