// Class GetResourcePolicyInput
// Dafny class GetResourcePolicyInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetResourcePolicyInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public GetResourcePolicyInput (dafny.DafnySequence<? extends Character> ResourceArn) {
    this._ResourceArn = ResourceArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetResourcePolicyInput o = (GetResourcePolicyInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GetResourcePolicyInput.GetResourcePolicyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetResourcePolicyInput> _TYPE = dafny.TypeDescriptor.<GetResourcePolicyInput>referenceWithInitializer(GetResourcePolicyInput.class, () -> GetResourcePolicyInput.Default());
  public static dafny.TypeDescriptor<GetResourcePolicyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetResourcePolicyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetResourcePolicyInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GetResourcePolicyInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetResourcePolicyInput Default() {
    return theDefault;
  }
  public static GetResourcePolicyInput create(dafny.DafnySequence<? extends Character> ResourceArn) {
    return new GetResourcePolicyInput(ResourceArn);
  }
  public static GetResourcePolicyInput create_GetResourcePolicyInput(dafny.DafnySequence<? extends Character> ResourceArn) {
    return create(ResourceArn);
  }
  public boolean is_GetResourcePolicyInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
}
