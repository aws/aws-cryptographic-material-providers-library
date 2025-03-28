// Class GetCacheEntryOutput
// Dafny class GetCacheEntryOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetCacheEntryOutput {
  public Materials _materials;
  public long _creationTime;
  public long _expiryTime;
  public int _messagesUsed;
  public int _bytesUsed;
  public GetCacheEntryOutput (Materials materials, long creationTime, long expiryTime, int messagesUsed, int bytesUsed) {
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
    GetCacheEntryOutput o = (GetCacheEntryOutput)other;
    return true && java.util.Objects.equals(this._materials, o._materials) && this._creationTime == o._creationTime && this._expiryTime == o._expiryTime && this._messagesUsed == o._messagesUsed && this._bytesUsed == o._bytesUsed;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._materials);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._creationTime);
    hash = ((hash << 5) + hash) + java.lang.Long.hashCode(this._expiryTime);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._messagesUsed);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._bytesUsed);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput.GetCacheEntryOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(", ");
    s.append(this._creationTime);
    s.append(", ");
    s.append(this._expiryTime);
    s.append(", ");
    s.append(this._messagesUsed);
    s.append(", ");
    s.append(this._bytesUsed);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetCacheEntryOutput> _TYPE = dafny.TypeDescriptor.<GetCacheEntryOutput>referenceWithInitializer(GetCacheEntryOutput.class, () -> GetCacheEntryOutput.Default());
  public static dafny.TypeDescriptor<GetCacheEntryOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetCacheEntryOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetCacheEntryOutput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput.create(Materials.Default(), 0L, 0L, 0, 0);
  public static GetCacheEntryOutput Default() {
    return theDefault;
  }
  public static GetCacheEntryOutput create(Materials materials, long creationTime, long expiryTime, int messagesUsed, int bytesUsed) {
    return new GetCacheEntryOutput(materials, creationTime, expiryTime, messagesUsed, bytesUsed);
  }
  public static GetCacheEntryOutput create_GetCacheEntryOutput(Materials materials, long creationTime, long expiryTime, int messagesUsed, int bytesUsed) {
    return create(materials, creationTime, expiryTime, messagesUsed, bytesUsed);
  }
  public boolean is_GetCacheEntryOutput() { return true; }
  public Materials dtor_materials() {
    return this._materials;
  }
  public long dtor_creationTime() {
    return this._creationTime;
  }
  public long dtor_expiryTime() {
    return this._expiryTime;
  }
  public int dtor_messagesUsed() {
    return this._messagesUsed;
  }
  public int dtor_bytesUsed() {
    return this._bytesUsed;
  }
}
