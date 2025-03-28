// Class CreateAwsKmsMrkDiscoveryMultiKeyringInput
// Dafny class CreateAwsKmsMrkDiscoveryMultiKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsMrkDiscoveryMultiKeyringInput {
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _regions;
  public Wrappers_Compile.Option<DiscoveryFilter> _discoveryFilter;
  public Wrappers_Compile.Option<IClientSupplier> _clientSupplier;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsMrkDiscoveryMultiKeyringInput (dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> regions, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._regions = regions;
    this._discoveryFilter = discoveryFilter;
    this._clientSupplier = clientSupplier;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsMrkDiscoveryMultiKeyringInput o = (CreateAwsKmsMrkDiscoveryMultiKeyringInput)other;
    return true && java.util.Objects.equals(this._regions, o._regions) && java.util.Objects.equals(this._discoveryFilter, o._discoveryFilter) && java.util.Objects.equals(this._clientSupplier, o._clientSupplier) && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._regions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._discoveryFilter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._clientSupplier);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput.CreateAwsKmsMrkDiscoveryMultiKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._regions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._discoveryFilter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._clientSupplier));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryMultiKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsMrkDiscoveryMultiKeyringInput>referenceWithInitializer(CreateAwsKmsMrkDiscoveryMultiKeyringInput.class, () -> CreateAwsKmsMrkDiscoveryMultiKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryMultiKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryMultiKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsMrkDiscoveryMultiKeyringInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput.create(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<DiscoveryFilter>Default(DiscoveryFilter._typeDescriptor()), Wrappers_Compile.Option.<IClientSupplier>Default(((dafny.TypeDescriptor<IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(IClientSupplier.class))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsMrkDiscoveryMultiKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsMrkDiscoveryMultiKeyringInput create(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> regions, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsMrkDiscoveryMultiKeyringInput(regions, discoveryFilter, clientSupplier, grantTokens);
  }
  public static CreateAwsKmsMrkDiscoveryMultiKeyringInput create_CreateAwsKmsMrkDiscoveryMultiKeyringInput(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> regions, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<IClientSupplier> clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(regions, discoveryFilter, clientSupplier, grantTokens);
  }
  public boolean is_CreateAwsKmsMrkDiscoveryMultiKeyringInput() { return true; }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_regions() {
    return this._regions;
  }
  public Wrappers_Compile.Option<DiscoveryFilter> dtor_discoveryFilter() {
    return this._discoveryFilter;
  }
  public Wrappers_Compile.Option<IClientSupplier> dtor_clientSupplier() {
    return this._clientSupplier;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
