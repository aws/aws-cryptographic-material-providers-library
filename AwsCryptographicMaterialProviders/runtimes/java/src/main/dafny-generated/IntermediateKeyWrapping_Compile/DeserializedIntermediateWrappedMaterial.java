// Class DeserializedIntermediateWrappedMaterial
// Dafny class DeserializedIntermediateWrappedMaterial compiled into Java
package IntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializedIntermediateWrappedMaterial {
  public dafny.DafnySequence<? extends java.lang.Byte> _encryptedPdk;
  public dafny.DafnySequence<? extends java.lang.Byte> _providerWrappedIkm;
  public DeserializedIntermediateWrappedMaterial (dafny.DafnySequence<? extends java.lang.Byte> encryptedPdk, dafny.DafnySequence<? extends java.lang.Byte> providerWrappedIkm) {
    this._encryptedPdk = encryptedPdk;
    this._providerWrappedIkm = providerWrappedIkm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializedIntermediateWrappedMaterial o = (DeserializedIntermediateWrappedMaterial)other;
    return true && java.util.Objects.equals(this._encryptedPdk, o._encryptedPdk) && java.util.Objects.equals(this._providerWrappedIkm, o._providerWrappedIkm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedPdk);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._providerWrappedIkm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial.DeserializedIntermediateWrappedMaterial");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encryptedPdk));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._providerWrappedIkm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeserializedIntermediateWrappedMaterial> _TYPE = dafny.TypeDescriptor.<DeserializedIntermediateWrappedMaterial>referenceWithInitializer(DeserializedIntermediateWrappedMaterial.class, () -> DeserializedIntermediateWrappedMaterial.Default());
  public static dafny.TypeDescriptor<DeserializedIntermediateWrappedMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeserializedIntermediateWrappedMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeserializedIntermediateWrappedMaterial theDefault = DeserializedIntermediateWrappedMaterial.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static DeserializedIntermediateWrappedMaterial Default() {
    return theDefault;
  }
  public static DeserializedIntermediateWrappedMaterial create(dafny.DafnySequence<? extends java.lang.Byte> encryptedPdk, dafny.DafnySequence<? extends java.lang.Byte> providerWrappedIkm) {
    return new DeserializedIntermediateWrappedMaterial(encryptedPdk, providerWrappedIkm);
  }
  public static DeserializedIntermediateWrappedMaterial create_DeserializedIntermediateWrappedMaterial(dafny.DafnySequence<? extends java.lang.Byte> encryptedPdk, dafny.DafnySequence<? extends java.lang.Byte> providerWrappedIkm) {
    return create(encryptedPdk, providerWrappedIkm);
  }
  public boolean is_DeserializedIntermediateWrappedMaterial() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_encryptedPdk() {
    return this._encryptedPdk;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_providerWrappedIkm() {
    return this._providerWrappedIkm;
  }
}
