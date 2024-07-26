using byteseq = Dafny.Sequence<byte>;

namespace TestWrappedMaterialProvidersMain_Compile {

  public partial class __default {

    public Dafny.ISequence<char> GetTestVectorExecutionDirectory() {
        return byteseq.FromString("");
    }

  }

}