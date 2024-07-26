using byteseq = Dafny.Sequence<byte>;
using AwsCryptographyMaterialProvidersTestVectorKeysTypes;

namespace TestWrappedMaterialProvidersMain {

  public partial class __default {

    public Wrappers_Compile._IResult<Dafny.ISequence<char>, AwsCryptographyMaterialProvidersTestVectorKeysTypes._IError> GetTestVectorExecutionDirectory() {
        return Result<Dafny.ISequence<char>, AwsCryptographyMaterialProvidersTestVectorKeysTypes._IError>.create_Success(byteseq.FromString(""));
    }

  }

}