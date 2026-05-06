// Class MultiKeyring
// Dafny class MultiKeyring compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MultiKeyring {
  public Wrappers_Compile.Option<KeyDescription> _generator;
  public dafny.DafnySequence<? extends KeyDescription> _childKeyrings;
  public MultiKeyring (Wrappers_Compile.Option<KeyDescription> generator, dafny.DafnySequence<? extends KeyDescription> childKeyrings) {
    this._generator = generator;
    this._childKeyrings = childKeyrings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MultiKeyring o = (MultiKeyring)other;
    return true && java.util.Objects.equals(this._generator, o._generator) && java.util.Objects.equals(this._childKeyrings, o._childKeyrings);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._generator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._childKeyrings);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring.MultiKeyring");
    s.append("(");
    s.append(dafny.Helpers.toString(this._generator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._childKeyrings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MultiKeyring> _TYPE = dafny.TypeDescriptor.<MultiKeyring>referenceWithInitializer(MultiKeyring.class, () -> MultiKeyring.Default());
  public static dafny.TypeDescriptor<MultiKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<MultiKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MultiKeyring theDefault = MultiKeyring.create(Wrappers_Compile.Option.<KeyDescription>Default(KeyDescription._typeDescriptor()), dafny.DafnySequence.<KeyDescription> empty(KeyDescription._typeDescriptor()));
  public static MultiKeyring Default() {
    return theDefault;
  }
  public static MultiKeyring create(Wrappers_Compile.Option<KeyDescription> generator, dafny.DafnySequence<? extends KeyDescription> childKeyrings) {
    return new MultiKeyring(generator, childKeyrings);
  }
  public static MultiKeyring create_MultiKeyring(Wrappers_Compile.Option<KeyDescription> generator, dafny.DafnySequence<? extends KeyDescription> childKeyrings) {
    return create(generator, childKeyrings);
  }
  public boolean is_MultiKeyring() { return true; }
  public Wrappers_Compile.Option<KeyDescription> dtor_generator() {
    return this._generator;
  }
  public dafny.DafnySequence<? extends KeyDescription> dtor_childKeyrings() {
    return this._childKeyrings;
  }
}
