// Class AesWrapInfo
// Dafny class AesWrapInfo compiled into Java
package RawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesWrapInfo {
  public dafny.DafnySequence<? extends java.lang.Byte> _iv;
  public AesWrapInfo (dafny.DafnySequence<? extends java.lang.Byte> iv) {
    this._iv = iv;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesWrapInfo o = (AesWrapInfo)other;
    return true && java.util.Objects.equals(this._iv, o._iv);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._iv);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("RawAESKeyring.AesWrapInfo.AesWrapInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._iv));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AesWrapInfo> _TYPE = dafny.TypeDescriptor.<AesWrapInfo>referenceWithInitializer(AesWrapInfo.class, () -> AesWrapInfo.Default());
  public static dafny.TypeDescriptor<AesWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesWrapInfo theDefault = AesWrapInfo.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static AesWrapInfo Default() {
    return theDefault;
  }
  public static AesWrapInfo create(dafny.DafnySequence<? extends java.lang.Byte> iv) {
    return new AesWrapInfo(iv);
  }
  public static AesWrapInfo create_AesWrapInfo(dafny.DafnySequence<? extends java.lang.Byte> iv) {
    return create(iv);
  }
  public boolean is_AesWrapInfo() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_iv() {
    return this._iv;
  }
}
