// Class EncryptionMaterials
// Dafny class EncryptionMaterials compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptionMaterials {
  public AlgorithmSuiteInfo _algorithmSuite;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends EncryptedDataKey> _encryptedDataKeys;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _plaintextDataKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _signingKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _symmetricSigningKeys;
  public EncryptionMaterials (AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> symmetricSigningKeys) {
    this._algorithmSuite = algorithmSuite;
    this._encryptionContext = encryptionContext;
    this._encryptedDataKeys = encryptedDataKeys;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
    this._plaintextDataKey = plaintextDataKey;
    this._signingKey = signingKey;
    this._symmetricSigningKeys = symmetricSigningKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptionMaterials o = (EncryptionMaterials)other;
    return true && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._encryptedDataKeys, o._encryptedDataKeys) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys) && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._signingKey, o._signingKey) && java.util.Objects.equals(this._symmetricSigningKeys, o._symmetricSigningKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptedDataKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.EncryptionMaterials.EncryptionMaterials");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptedDataKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EncryptionMaterials> _TYPE = dafny.TypeDescriptor.<EncryptionMaterials>referenceWithInitializer(EncryptionMaterials.class, () -> EncryptionMaterials.Default());
  public static dafny.TypeDescriptor<EncryptionMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptionMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptionMaterials theDefault = EncryptionMaterials.create(AlgorithmSuiteInfo.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), dafny.DafnySequence.<EncryptedDataKey> empty(EncryptedDataKey._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))));
  public static EncryptionMaterials Default() {
    return theDefault;
  }
  public static EncryptionMaterials create(AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> symmetricSigningKeys) {
    return new EncryptionMaterials(algorithmSuite, encryptionContext, encryptedDataKeys, requiredEncryptionContextKeys, plaintextDataKey, signingKey, symmetricSigningKeys);
  }
  public static EncryptionMaterials create_EncryptionMaterials(AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends EncryptedDataKey> encryptedDataKeys, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> signingKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> symmetricSigningKeys) {
    return create(algorithmSuite, encryptionContext, encryptedDataKeys, requiredEncryptionContextKeys, plaintextDataKey, signingKey, symmetricSigningKeys);
  }
  public boolean is_EncryptionMaterials() { return true; }
  public AlgorithmSuiteInfo dtor_algorithmSuite() {
    return this._algorithmSuite;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public dafny.DafnySequence<? extends EncryptedDataKey> dtor_encryptedDataKeys() {
    return this._encryptedDataKeys;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_signingKey() {
    return this._signingKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_symmetricSigningKeys() {
    return this._symmetricSigningKeys;
  }
}
