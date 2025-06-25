// Interface IMetricsAgent
// Dafny trait IMetricsAgent compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface IMetricsAgent {
  public Wrappers_Compile.Result<PutOutput, Error> PutCount(PutCountInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutCount_k(PutCountInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutDate(PutDateInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutDate_k(PutDateInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutTime(PutTimeInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutTime_k(PutTimeInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutProperty(PutPropertyInput input);
  public Wrappers_Compile.Result<PutOutput, Error> PutProperty_k(PutPropertyInput input);
}
