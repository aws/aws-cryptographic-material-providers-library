// Class XksKeyConfigurationType
// Dafny class XksKeyConfigurationType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class XksKeyConfigurationType {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Id;
  public XksKeyConfigurationType (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Id) {
    this._Id = Id;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    XksKeyConfigurationType o = (XksKeyConfigurationType)other;
    return true && java.util.Objects.equals(this._Id, o._Id);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Id);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.XksKeyConfigurationType.XksKeyConfigurationType");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Id));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<XksKeyConfigurationType> _TYPE = dafny.TypeDescriptor.<XksKeyConfigurationType>referenceWithInitializer(XksKeyConfigurationType.class, () -> XksKeyConfigurationType.Default());
  public static dafny.TypeDescriptor<XksKeyConfigurationType> _typeDescriptor() {
    return (dafny.TypeDescriptor<XksKeyConfigurationType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final XksKeyConfigurationType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.XksKeyConfigurationType.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(XksKeyIdType._typeDescriptor()));
  public static XksKeyConfigurationType Default() {
    return theDefault;
  }
  public static XksKeyConfigurationType create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Id) {
    return new XksKeyConfigurationType(Id);
  }
  public static XksKeyConfigurationType create_XksKeyConfigurationType(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Id) {
    return create(Id);
  }
  public boolean is_XksKeyConfigurationType() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Id() {
    return this._Id;
  }
}
