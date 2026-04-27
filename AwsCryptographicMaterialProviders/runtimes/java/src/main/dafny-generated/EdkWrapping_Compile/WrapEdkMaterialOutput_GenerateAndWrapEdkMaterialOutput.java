// Class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>
// Dafny class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T> compiled into Java
package EdkWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T> extends WrapEdkMaterialOutput<T> {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextDataKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappedMaterial;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _symmetricSigningKey;
  public T _wrapInfo;
  public WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput (dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends java.lang.Byte> plaintextDataKey, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey, T wrapInfo) {
    super(_td_T);
    this._plaintextDataKey = plaintextDataKey;
    this._wrappedMaterial = wrappedMaterial;
    this._symmetricSigningKey = symmetricSigningKey;
    this._wrapInfo = wrapInfo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T> o = (WrapEdkMaterialOutput_GenerateAndWrapEdkMaterialOutput<T>)other;
    return true && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._wrappedMaterial, o._wrappedMaterial) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey) && java.util.Objects.equals(this._wrapInfo, o._wrapInfo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrappedMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._wrapInfo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("EdkWrapping.WrapEdkMaterialOutput.GenerateAndWrapEdkMaterialOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrappedMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._wrapInfo));
    s.append(")");
    return s.toString();
  }
}
