using byteseq = Dafny.Sequence<byte>;

namespace TestWrappedMaterialProvidersMain {

  public partial class __default {

    public Wrappers._IResult<Dafny.ISequence<char>, AwsCryptographyMaterialProvidersTestVectorKeysTypes._IError> GetTestVectorExecutionDirectory() {
        return Result<Dafny.ISequence<char>, AwsCryptographyMaterialProvidersTestVectorKeysTypes._IError>.create_Success(byteseq.FromString(""));
    }

  }

}