// Class DecryptResult
// Dafny class DecryptResult compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptResult {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _plaintextDataKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _symmetricSigningKey;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public DecryptResult (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    this._plaintextDataKey = plaintextDataKey;
    this._symmetricSigningKey = symmetricSigningKey;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptResult o = (DecryptResult)other;
    return true && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestVectors.DecryptResult.DecryptResult");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptResult> _TYPE = dafny.TypeDescriptor.<DecryptResult>referenceWithInitializer(DecryptResult.class, () -> DecryptResult.Default());
  public static dafny.TypeDescriptor<DecryptResult> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptResult>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptResult theDefault = DecryptResult.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()));
  public static DecryptResult Default() {
    return theDefault;
  }
  public static DecryptResult create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return new DecryptResult(plaintextDataKey, symmetricSigningKey, requiredEncryptionContextKeys);
  }
  public static DecryptResult create_DecryptResult(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys) {
    return create(plaintextDataKey, symmetricSigningKey, requiredEncryptionContextKeys);
  }
  public boolean is_DecryptResult() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
}
