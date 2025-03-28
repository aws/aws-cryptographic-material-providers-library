// Class SignRequest
// Dafny class SignRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SignRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends java.lang.Byte> _Message;
  public Wrappers_Compile.Option<MessageType> _MessageType;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public SigningAlgorithmSpec _SigningAlgorithm;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public SignRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._Message = Message;
    this._MessageType = MessageType;
    this._GrantTokens = GrantTokens;
    this._SigningAlgorithm = SigningAlgorithm;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SignRequest o = (SignRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Message, o._Message) && java.util.Objects.equals(this._MessageType, o._MessageType) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens) && java.util.Objects.equals(this._SigningAlgorithm, o._SigningAlgorithm) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Message);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MessageType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.SignRequest.SignRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Message));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MessageType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SignRequest> _TYPE = dafny.TypeDescriptor.<SignRequest>referenceWithInitializer(SignRequest.class, () -> SignRequest.Default());
  public static dafny.TypeDescriptor<SignRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<SignRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SignRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.SignRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<MessageType>Default(MessageType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()), SigningAlgorithmSpec.Default(), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static SignRequest Default() {
    return theDefault;
  }
  public static SignRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    return new SignRequest(KeyId, Message, MessageType, GrantTokens, SigningAlgorithm, DryRun);
  }
  public static SignRequest create_SignRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends java.lang.Byte> Message, Wrappers_Compile.Option<MessageType> MessageType, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens, SigningAlgorithmSpec SigningAlgorithm, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, Message, MessageType, GrantTokens, SigningAlgorithm, DryRun);
  }
  public boolean is_SignRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_Message() {
    return this._Message;
  }
  public Wrappers_Compile.Option<MessageType> dtor_MessageType() {
    return this._MessageType;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
  public SigningAlgorithmSpec dtor_SigningAlgorithm() {
    return this._SigningAlgorithm;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
