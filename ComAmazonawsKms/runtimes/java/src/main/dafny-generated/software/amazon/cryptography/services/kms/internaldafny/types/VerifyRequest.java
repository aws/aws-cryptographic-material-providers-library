// Class VerifyRequest
// Dafny class VerifyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class VerifyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends java.lang.Byte> _Message;
  public Wrappers_Compile.Option<MessageType> _MessageType;
  public dafny.DafnySequence<? extends java.lang.Byte> _Signature;
  public SigningAlgorithmSpec _SigningAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public VerifyRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, dafny.DafnySequence<? extends java.lang.Byte> Signature, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._Message = Message;
    this._MessageType = MessageType;
    this._Signature = Signature;
    this._SigningAlgorithm = SigningAlgorithm;
    this._GrantTokens = GrantTokens;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VerifyRequest o = (VerifyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._MessageType, o._MessageType) && java.util.Objects.equals(this._Signature, o._Signature) && java.util.Objects.equals(this._SigningAlgorithm, o._SigningAlgorithm) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MessageType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Signature);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.VerifyRequest.VerifyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MessageType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Signature));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VerifyRequest> _TYPE = dafny.TypeDescriptor.<VerifyRequest>referenceWithInitializer(VerifyRequest.class, () -> VerifyRequest.Default());
  public static dafny.TypeDescriptor<VerifyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<VerifyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VerifyRequest theDefault = VerifyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<MessageType>Default(MessageType._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), SigningAlgorithmSpec.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static VerifyRequest Default() {
    return theDefault;
  }
  public static VerifyRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, dafny.DafnySequence<? extends java.lang.Byte> Signature, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return new VerifyRequest(KeyId, Message, MessageType, Signature, SigningAlgorithm, GrantTokens, DryRun);
  }
  public static VerifyRequest create_VerifyRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, dafny.DafnySequence<? extends java.lang.Byte> Signature, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, Message, MessageType, Signature, SigningAlgorithm, GrantTokens, DryRun);
  }
  public boolean is_VerifyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Message() {
    return this._Message;
  }
  public Wrappers_Compile.Option<MessageType> dtor_MessageType() {
    return this._MessageType;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Signature() {
    return this._Signature;
  }
  public SigningAlgorithmSpec dtor_SigningAlgorithm() {
    return this._SigningAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
