// Class KmsMrkAwareDiscovery
// Dafny class KmsMrkAwareDiscovery compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsMrkAwareDiscovery {
  public dafny.DafnySequence<? extends Character> _keyId;
  public dafny.DafnySequence<? extends Character> _defaultMrkRegion;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _awsKmsDiscoveryFilter;
  public KmsMrkAwareDiscovery (dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> defaultMrkRegion, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> awsKmsDiscoveryFilter) {
    this._keyId = keyId;
    this._defaultMrkRegion = defaultMrkRegion;
    this._awsKmsDiscoveryFilter = awsKmsDiscoveryFilter;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsMrkAwareDiscovery o = (KmsMrkAwareDiscovery)other;
    return true && java.util.Objects.equals(this._keyId, o._keyId) && java.util.Objects.equals(this._defaultMrkRegion, o._defaultMrkRegion) && java.util.Objects.equals(this._awsKmsDiscoveryFilter, o._awsKmsDiscoveryFilter);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._defaultMrkRegion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._awsKmsDiscoveryFilter);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery.KmsMrkAwareDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._defaultMrkRegion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._awsKmsDiscoveryFilter));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsMrkAwareDiscovery> _TYPE = dafny.TypeDescriptor.<KmsMrkAwareDiscovery>referenceWithInitializer(KmsMrkAwareDiscovery.class, () -> KmsMrkAwareDiscovery.Default());
  public static dafny.TypeDescriptor<KmsMrkAwareDiscovery> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsMrkAwareDiscovery>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsMrkAwareDiscovery theDefault = KmsMrkAwareDiscovery.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>Default(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor()));
  public static KmsMrkAwareDiscovery Default() {
    return theDefault;
  }
  public static KmsMrkAwareDiscovery create(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> defaultMrkRegion, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> awsKmsDiscoveryFilter) {
    return new KmsMrkAwareDiscovery(keyId, defaultMrkRegion, awsKmsDiscoveryFilter);
  }
  public static KmsMrkAwareDiscovery create_KmsMrkAwareDiscovery(dafny.DafnySequence<? extends Character> keyId, dafny.DafnySequence<? extends Character> defaultMrkRegion, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> awsKmsDiscoveryFilter) {
    return create(keyId, defaultMrkRegion, awsKmsDiscoveryFilter);
  }
  public boolean is_KmsMrkAwareDiscovery() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_keyId() {
    return this._keyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_defaultMrkRegion() {
    return this._defaultMrkRegion;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> dtor_awsKmsDiscoveryFilter() {
    return this._awsKmsDiscoveryFilter;
  }
}
