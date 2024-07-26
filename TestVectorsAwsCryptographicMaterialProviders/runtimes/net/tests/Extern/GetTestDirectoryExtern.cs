using byteseq = Dafny.Sequence<byte>;

namespace TestWrappedMaterialProvidersMain {

  public partial class __default {

    public Dafny.ISequence<char> GetTestVectorExecutionDirectory() {
        return byteseq.FromString("");
    }

  }

}