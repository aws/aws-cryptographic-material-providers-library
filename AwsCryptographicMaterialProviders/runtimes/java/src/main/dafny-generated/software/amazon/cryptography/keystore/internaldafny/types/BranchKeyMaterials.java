// Class BranchKeyMaterials
// Dafny class BranchKeyMaterials compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BranchKeyMaterials {
  public dafny.DafnySequence<? extends Character> _branchKeyIdentifier;
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKeyVersion;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends java.lang.Byte> _branchKey;
  public BranchKeyMaterials (dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> branchKey) {
    this._branchKeyIdentifier = branchKeyIdentifier;
    this._branchKeyVersion = branchKeyVersion;
    this._encryptionContext = encryptionContext;
    this._branchKey = branchKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BranchKeyMaterials o = (BranchKeyMaterials)other;
    return true && java.util.Objects.equals(this._branchKeyIdentifier, o._branchKeyIdentifier) && java.util.Objects.equals(this._branchKeyVersion, o._branchKeyVersion) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._branchKey, o._branchKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyIdentifier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKeyVersion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._branchKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyKeyStoreTypes.BranchKeyMaterials.BranchKeyMaterials");
    s.append("(");
    s.append(dafny.Helpers.toString(this._branchKeyIdentifier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKeyVersion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._branchKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BranchKeyMaterials> _TYPE = dafny.TypeDescriptor.<BranchKeyMaterials>referenceWithInitializer(BranchKeyMaterials.class, () -> BranchKeyMaterials.Default());
  public static dafny.TypeDescriptor<BranchKeyMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<BranchKeyMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BranchKeyMaterials theDefault = BranchKeyMaterials.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), UTF8.ValidUTF8Bytes.defaultValue(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static BranchKeyMaterials Default() {
    return theDefault;
  }
  public static BranchKeyMaterials create(dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> branchKey) {
    return new BranchKeyMaterials(branchKeyIdentifier, branchKeyVersion, encryptionContext, branchKey);
  }
  public static BranchKeyMaterials create_BranchKeyMaterials(dafny.DafnySequence<? extends Character> branchKeyIdentifier, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends java.lang.Byte> branchKey) {
    return create(branchKeyIdentifier, branchKeyVersion, encryptionContext, branchKey);
  }
  public boolean is_BranchKeyMaterials() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_branchKeyIdentifier() {
    return this._branchKeyIdentifier;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_branchKeyVersion() {
    return this._branchKeyVersion;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_branchKey() {
    return this._branchKey;
  }
}
