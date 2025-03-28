// Class DiscoveryFilter
// Dafny class DiscoveryFilter compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DiscoveryFilter {
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _accountIds;
  public dafny.DafnySequence<? extends Character> _partition;
  public DiscoveryFilter (dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> accountIds, dafny.DafnySequence<? extends Character> partition) {
    this._accountIds = accountIds;
    this._partition = partition;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DiscoveryFilter o = (DiscoveryFilter)other;
    return true && java.util.Objects.equals(this._accountIds, o._accountIds) && java.util.Objects.equals(this._partition, o._partition);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._accountIds);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._partition);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DiscoveryFilter.DiscoveryFilter");
    s.append("(");
    s.append(dafny.Helpers.toString(this._accountIds));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._partition));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DiscoveryFilter> _TYPE = dafny.TypeDescriptor.<DiscoveryFilter>referenceWithInitializer(DiscoveryFilter.class, () -> DiscoveryFilter.Default());
  public static dafny.TypeDescriptor<DiscoveryFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<DiscoveryFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DiscoveryFilter theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter.create(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DiscoveryFilter Default() {
    return theDefault;
  }
  public static DiscoveryFilter create(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> accountIds, dafny.DafnySequence<? extends Character> partition) {
    return new DiscoveryFilter(accountIds, partition);
  }
  public static DiscoveryFilter create_DiscoveryFilter(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> accountIds, dafny.DafnySequence<? extends Character> partition) {
    return create(accountIds, partition);
  }
  public boolean is_DiscoveryFilter() { return true; }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_accountIds() {
    return this._accountIds;
  }
  public dafny.DafnySequence<? extends Character> dtor_partition() {
    return this._partition;
  }
}
