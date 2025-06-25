// Interface ILogger
// Dafny trait ILogger compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public interface ILogger {
  public Wrappers_Compile.Result<PutOutput, Error> Put(PutInput input);
  public Wrappers_Compile.Result<PutOutput, Error> Put_k(PutInput input);
  public Wrappers_Compile.Result<PublishOutput, Error> Publish(PublishInput input);
  public Wrappers_Compile.Result<PublishOutput, Error> Publish_k(PublishInput input);
}
