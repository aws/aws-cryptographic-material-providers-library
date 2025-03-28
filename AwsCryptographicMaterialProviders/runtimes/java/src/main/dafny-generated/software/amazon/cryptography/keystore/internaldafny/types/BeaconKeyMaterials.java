// Class BeaconKeyMaterials
// Dafny class BeaconKeyMaterials compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BeaconKeyMaterials {
  public dafny.DafnySequence<? extends Character> _beaconKeyIdentifier;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _beaconKey;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _hmacKeys;
  public BeaconKeyMaterials (dafny.DafnySequence<? extends Character> beaconKeyIdentifier, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> beaconKey, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> hmacKeys) {
    this._beaconKeyIdentifier = beaconKeyIdentifier;
    this._encryptionContext = encryptionContext;
    this._beaconKey = beaconKey;
    this._hmacKeys = hmacKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BeaconKeyMaterials o = (BeaconKeyMaterials)other;
    return true && java.util.Objects.equals(this._beaconKeyIdentifier, o._beaconKeyIdentifier) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._beaconKey, o._beaconKey) && java.util.Objects.equals(this._hmacKeys, o._hmacKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._beaconKeyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._beaconKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._hmacKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.BeaconKeyMaterials.BeaconKeyMaterials");
    s.append("(");
    s.append(dafny.Helpers.toString(this._beaconKeyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._beaconKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._hmacKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BeaconKeyMaterials> _TYPE = dafny.TypeDescriptor.<BeaconKeyMaterials>referenceWithInitializer(BeaconKeyMaterials.class, () -> BeaconKeyMaterials.Default());
  public static dafny.TypeDescriptor<BeaconKeyMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<BeaconKeyMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BeaconKeyMaterials theDefault = software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
  public static BeaconKeyMaterials Default() {
    return theDefault;
  }
  public static BeaconKeyMaterials create(dafny.DafnySequence<? extends Character> beaconKeyIdentifier, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> beaconKey, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> hmacKeys) {
    return new BeaconKeyMaterials(beaconKeyIdentifier, encryptionContext, beaconKey, hmacKeys);
  }
  public static BeaconKeyMaterials create_BeaconKeyMaterials(dafny.DafnySequence<? extends Character> beaconKeyIdentifier, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> beaconKey, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> hmacKeys) {
    return create(beaconKeyIdentifier, encryptionContext, beaconKey, hmacKeys);
  }
  public boolean is_BeaconKeyMaterials() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_beaconKeyIdentifier() {
    return this._beaconKeyIdentifier;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_beaconKey() {
    return this._beaconKey;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_hmacKeys() {
    return this._hmacKeys;
  }
}
