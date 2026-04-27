// Class ValidateCommitmentPolicyOnDecryptInput
// Dafny class ValidateCommitmentPolicyOnDecryptInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ValidateCommitmentPolicyOnDecryptInput {
  public AlgorithmSuiteId _algorithm;
  public CommitmentPolicy _commitmentPolicy;
  public ValidateCommitmentPolicyOnDecryptInput (AlgorithmSuiteId algorithm, CommitmentPolicy commitmentPolicy) {
    this._algorithm = algorithm;
    this._commitmentPolicy = commitmentPolicy;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ValidateCommitmentPolicyOnDecryptInput o = (ValidateCommitmentPolicyOnDecryptInput)other;
    return true && java.util.Objects.equals(this._algorithm, o._algorithm) && java.util.Objects.equals(this._commitmentPolicy, o._commitmentPolicy);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._commitmentPolicy);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnDecryptInput.ValidateCommitmentPolicyOnDecryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._commitmentPolicy));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ValidateCommitmentPolicyOnDecryptInput> _TYPE = dafny.TypeDescriptor.<ValidateCommitmentPolicyOnDecryptInput>referenceWithInitializer(ValidateCommitmentPolicyOnDecryptInput.class, () -> ValidateCommitmentPolicyOnDecryptInput.Default());
  public static dafny.TypeDescriptor<ValidateCommitmentPolicyOnDecryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ValidateCommitmentPolicyOnDecryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ValidateCommitmentPolicyOnDecryptInput theDefault = ValidateCommitmentPolicyOnDecryptInput.create(AlgorithmSuiteId.Default(), CommitmentPolicy.Default());
  public static ValidateCommitmentPolicyOnDecryptInput Default() {
    return theDefault;
  }
  public static ValidateCommitmentPolicyOnDecryptInput create(AlgorithmSuiteId algorithm, CommitmentPolicy commitmentPolicy) {
    return new ValidateCommitmentPolicyOnDecryptInput(algorithm, commitmentPolicy);
  }
  public static ValidateCommitmentPolicyOnDecryptInput create_ValidateCommitmentPolicyOnDecryptInput(AlgorithmSuiteId algorithm, CommitmentPolicy commitmentPolicy) {
    return create(algorithm, commitmentPolicy);
  }
  public boolean is_ValidateCommitmentPolicyOnDecryptInput() { return true; }
  public AlgorithmSuiteId dtor_algorithm() {
    return this._algorithm;
  }
  public CommitmentPolicy dtor_commitmentPolicy() {
    return this._commitmentPolicy;
  }
}
