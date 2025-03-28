// Class DecryptionMaterials
// Dafny class DecryptionMaterials compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptionMaterials {
  public AlgorithmSuiteInfo _algorithmSuite;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _plaintextDataKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _verificationKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _symmetricSigningKey;
  public DecryptionMaterials (AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey) {
    this._algorithmSuite = algorithmSuite;
    this._encryptionContext = encryptionContext;
    this._requiredEncryptionContextKeys = requiredEncryptionContextKeys;
    this._plaintextDataKey = plaintextDataKey;
    this._verificationKey = verificationKey;
    this._symmetricSigningKey = symmetricSigningKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptionMaterials o = (DecryptionMaterials)other;
    return true && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext) && java.util.Objects.equals(this._requiredEncryptionContextKeys, o._requiredEncryptionContextKeys) && java.util.Objects.equals(this._plaintextDataKey, o._plaintextDataKey) && java.util.Objects.equals(this._verificationKey, o._verificationKey) && java.util.Objects.equals(this._symmetricSigningKey, o._symmetricSigningKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._requiredEncryptionContextKeys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextDataKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._symmetricSigningKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.DecryptionMaterials");
    s.append("(");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._requiredEncryptionContextKeys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._plaintextDataKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._symmetricSigningKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptionMaterials> _TYPE = dafny.TypeDescriptor.<DecryptionMaterials>referenceWithInitializer(DecryptionMaterials.class, () -> DecryptionMaterials.Default());
  public static dafny.TypeDescriptor<DecryptionMaterials> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptionMaterials>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptionMaterials theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials.create(AlgorithmSuiteInfo.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
  public static DecryptionMaterials Default() {
    return theDefault;
  }
  public static DecryptionMaterials create(AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey) {
    return new DecryptionMaterials(algorithmSuite, encryptionContext, requiredEncryptionContextKeys, plaintextDataKey, verificationKey, symmetricSigningKey);
  }
  public static DecryptionMaterials create_DecryptionMaterials(AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> plaintextDataKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> verificationKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> symmetricSigningKey) {
    return create(algorithmSuite, encryptionContext, requiredEncryptionContextKeys, plaintextDataKey, verificationKey, symmetricSigningKey);
  }
  public boolean is_DecryptionMaterials() { return true; }
  public AlgorithmSuiteInfo dtor_algorithmSuite() {
    return this._algorithmSuite;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_requiredEncryptionContextKeys() {
    return this._requiredEncryptionContextKeys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_plaintextDataKey() {
    return this._plaintextDataKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_verificationKey() {
    return this._verificationKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_symmetricSigningKey() {
    return this._symmetricSigningKey;
  }
}
