// Class PutCacheEntryInput
// Dafny class PutCacheEntryInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PutCacheEntryInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public Materials _materials;
  public long _creationTime;
  public long _expiryTime;
  public Wrappers_Compile.Option<java.lang.Integer> _messagesUsed;
  public Wrappers_Compile.Option<java.lang.Integer> _bytesUsed;
  public PutCacheEntryInput (dafny.DafnySequence<? extends java.lang.Byte> identifier, Materials materials, long creationTime, long expiryTime, Wrappers_Compile.Option<java.lang.Integer> messagesUsed, Wrappers_Compile.Option<java.lang.Integer> bytesUsed) {
    this._identifier = identifier;
    this._materials = materials;
    this._creationTime = creationTime;
    this._expiryTime = expiryTime;
    this._messagesUsed = messagesUsed;
    this._bytesUsed = bytesUsed;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutCacheEntryInput o = (PutCacheEntryInput)other;
    return true && java.util.Objects.equals(this._identifier, o._identifier) && java.util.Objects.equals(this._materials, o._materials) && this._creationTime == o._creationTime && this._expiryTime == o._expiryTime && java.util.Objects.equals(this._messagesUsed, o._messagesUsed) && java.util.Objects.equals(this._bytesUsed, o._bytesUsed);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._identifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._materials);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._creationTime);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._expiryTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._messagesUsed);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._bytesUsed);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput.PutCacheEntryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._identifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(", ");
    s.append(this._creationTime);
    s.append(", ");
    s.append(this._expiryTime);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._messagesUsed));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._bytesUsed));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutCacheEntryInput> _TYPE = dafny.TypeDescriptor.<PutCacheEntryInput>referenceWithInitializer(PutCacheEntryInput.class, () -> PutCacheEntryInput.Default());
  public static dafny.TypeDescriptor<PutCacheEntryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutCacheEntryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutCacheEntryInput theDefault = PutCacheEntryInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Materials.Default(), 0L, 0L, Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveInteger._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveInteger._typeDescriptor()));
  public static PutCacheEntryInput Default() {
    return theDefault;
  }
  public static PutCacheEntryInput create(dafny.DafnySequence<? extends java.lang.Byte> identifier, Materials materials, long creationTime, long expiryTime, Wrappers_Compile.Option<java.lang.Integer> messagesUsed, Wrappers_Compile.Option<java.lang.Integer> bytesUsed) {
    return new PutCacheEntryInput(identifier, materials, creationTime, expiryTime, messagesUsed, bytesUsed);
  }
  public static PutCacheEntryInput create_PutCacheEntryInput(dafny.DafnySequence<? extends java.lang.Byte> identifier, Materials materials, long creationTime, long expiryTime, Wrappers_Compile.Option<java.lang.Integer> messagesUsed, Wrappers_Compile.Option<java.lang.Integer> bytesUsed) {
    return create(identifier, materials, creationTime, expiryTime, messagesUsed, bytesUsed);
  }
  public boolean is_PutCacheEntryInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_identifier() {
    return this._identifier;
  }
  public Materials dtor_materials() {
    return this._materials;
  }
  public long dtor_creationTime() {
    return this._creationTime;
  }
  public long dtor_expiryTime() {
    return this._expiryTime;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_messagesUsed() {
    return this._messagesUsed;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_bytesUsed() {
    return this._bytesUsed;
  }
}
