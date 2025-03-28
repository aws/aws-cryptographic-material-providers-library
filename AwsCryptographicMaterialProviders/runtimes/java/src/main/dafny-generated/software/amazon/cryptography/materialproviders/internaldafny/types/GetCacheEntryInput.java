// Class GetCacheEntryInput
// Dafny class GetCacheEntryInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetCacheEntryInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public Wrappers_Compile.Option<java.lang.Long> _bytesUsed;
  public GetCacheEntryInput (dafny.DafnySequence<? extends java.lang.Byte> identifier, Wrappers_Compile.Option<java.lang.Long> bytesUsed) {
    this._identifier = identifier;
    this._bytesUsed = bytesUsed;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetCacheEntryInput o = (GetCacheEntryInput)other;
    return true && java.util.Objects.equals(this._identifier, o._identifier) && java.util.Objects.equals(this._bytesUsed, o._bytesUsed);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._identifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._bytesUsed);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput.GetCacheEntryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._identifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._bytesUsed));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetCacheEntryInput> _TYPE = dafny.TypeDescriptor.<GetCacheEntryInput>referenceWithInitializer(GetCacheEntryInput.class, () -> GetCacheEntryInput.Default());
  public static dafny.TypeDescriptor<GetCacheEntryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetCacheEntryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetCacheEntryInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()));
  public static GetCacheEntryInput Default() {
    return theDefault;
  }
  public static GetCacheEntryInput create(dafny.DafnySequence<? extends java.lang.Byte> identifier, Wrappers_Compile.Option<java.lang.Long> bytesUsed) {
    return new GetCacheEntryInput(identifier, bytesUsed);
  }
  public static GetCacheEntryInput create_GetCacheEntryInput(dafny.DafnySequence<? extends java.lang.Byte> identifier, Wrappers_Compile.Option<java.lang.Long> bytesUsed) {
    return create(identifier, bytesUsed);
  }
  public boolean is_GetCacheEntryInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_identifier() {
    return this._identifier;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_bytesUsed() {
    return this._bytesUsed;
  }
}
