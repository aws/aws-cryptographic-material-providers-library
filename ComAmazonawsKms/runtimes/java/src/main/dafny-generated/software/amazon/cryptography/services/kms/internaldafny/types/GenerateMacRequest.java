// Class GenerateMacRequest
// Dafny class GenerateMacRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateMacRequest {
  public dafny.DafnySequence<? extends java.lang.Byte> _Message;
  public dafny.DafnySequence<? extends Character> _KeyId;
  public MacAlgorithmSpec _MacAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public GenerateMacRequest (dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._Message = Message;
    this._KeyId = KeyId;
    this._MacAlgorithm = MacAlgorithm;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateMacRequest o = (GenerateMacRequest)other;
    return true && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._MacAlgorithm, o._MacAlgorithm) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateMacRequest.GenerateMacRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateMacRequest> _TYPE = dafny.TypeDescriptor.<GenerateMacRequest>referenceWithInitializer(GenerateMacRequest.class, () -> GenerateMacRequest.Default());
  public static dafny.TypeDescriptor<GenerateMacRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateMacRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateMacRequest theDefault = GenerateMacRequest.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), MacAlgorithmSpec.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static GenerateMacRequest Default() {
    return theDefault;
  }
  public static GenerateMacRequest create(dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new GenerateMacRequest(Message, KeyId, MacAlgorithm, GrantTokens, DryRun);
  }
  public static GenerateMacRequest create_GenerateMacRequest(dafny.DafnySequence<? extends java.lang.Byte> Message, dafny.DafnySequence<? extends Character> KeyId, MacAlgorithmSpec MacAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(Message, KeyId, MacAlgorithm, GrantTokens, DryRun);
  }
  public boolean is_GenerateMacRequest() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Message() {
    return this._Message;
  }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public MacAlgorithmSpec dtor_MacAlgorithm() {
    return this._MacAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
