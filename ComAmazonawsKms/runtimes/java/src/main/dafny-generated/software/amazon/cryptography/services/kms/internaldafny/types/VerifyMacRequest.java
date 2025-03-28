// Class VerifyMacRequest
// Dafny class VerifyMacRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class VerifyMacRequest {
  public dafny.DafnySequence<? extends java.lang.Byte> _Message;
  public dafny.DafnySequence<? extends Character> _KeyId;
  public MacAlgorithmSpec _MacAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _Mac;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public VerifyMacRequest (dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> Mac, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._Message = Message;
    this._KeyId = KeyId;
    this._MacAlgorithm = MacAlgorithm;
    this._Mac = Mac;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VerifyMacRequest o = (VerifyMacRequest)other;
    return true && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._MacAlgorithm, o._MacAlgorithm) && java.util.Objects.equals(this._Mac, o._Mac) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Mac);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.VerifyMacRequest.VerifyMacRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Mac));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VerifyMacRequest> _TYPE = dafny.TypeDescriptor.<VerifyMacRequest>referenceWithInitializer(VerifyMacRequest.class, () -> VerifyMacRequest.Default());
  public static dafny.TypeDescriptor<VerifyMacRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<VerifyMacRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VerifyMacRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.VerifyMacRequest.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), MacAlgorithmSpec.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static VerifyMacRequest Default() {
    return theDefault;
  }
  public static VerifyMacRequest create(dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> Mac, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new VerifyMacRequest(Message, KeyId, MacAlgorithm, Mac, GrantTokens, DryRun);
  }
  public static VerifyMacRequest create_VerifyMacRequest(dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> Mac, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(Message, KeyId, MacAlgorithm, Mac, GrantTokens, DryRun);
  }
  public boolean is_VerifyMacRequest() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Message() {
    return this._Message;
  }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public MacAlgorithmSpec dtor_MacAlgorithm() {
    return this._MacAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Mac() {
    return this._Mac;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
