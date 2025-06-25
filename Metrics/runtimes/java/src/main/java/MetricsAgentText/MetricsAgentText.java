package MetricsAgentText;

import Wrappers_Compile.Option;
import Wrappers_Compile.Result;
import dafny.DafnySequence;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.internaldafny.types.IMetricsAgent;
import software.amazon.cryptography.metrics.internaldafny.types.PutCountInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutDateInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutOutput;
import software.amazon.cryptography.metrics.internaldafny.types.PutPropertyInput;
import software.amazon.cryptography.metrics.internaldafny.types.PutTimeInput;

public class MetricsAgentText {

  public static class TextLogger implements IMetricsAgent {
    public TextLogger(DafnySequence<? extends Character> fileName) {
    }

    public static Result<PutOutput, Error> PutCount(PutCountInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutCount_k(PutCountInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutDate(PutDateInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutDate_k(PutDateInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutTime(PutTimeInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutTime_k(PutTimeInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutProperty(PutPropertyInput input) {
      return null;
    }

    @Override
    public Result<PutOutput, Error> PutProperty_k(PutPropertyInput input) {
      return null;
    }
  }
}
