// Class ReplicateKeyResponse
// Dafny class ReplicateKeyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicateKeyResponse {
  public Wrappers_Compile.Option<KeyMetadata> _ReplicaKeyMetadata;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ReplicaPolicy;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _ReplicaTags;
  public ReplicateKeyResponse (Wrappers_Compile.Option<KeyMetadata> ReplicaKeyMetadata, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaPolicy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> ReplicaTags) {
    this._ReplicaKeyMetadata = ReplicaKeyMetadata;
    this._ReplicaPolicy = ReplicaPolicy;
    this._ReplicaTags = ReplicaTags;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicateKeyResponse o = (ReplicateKeyResponse)other;
    return true && java.util.Objects.equals(this._ReplicaKeyMetadata, o._ReplicaKeyMetadata) && java.util.Objects.equals(this._ReplicaPolicy, o._ReplicaPolicy) && java.util.Objects.equals(this._ReplicaTags, o._ReplicaTags);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaKeyMetadata);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaPolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaTags);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ReplicateKeyResponse.ReplicateKeyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ReplicaKeyMetadata));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaPolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaTags));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicateKeyResponse> _TYPE = dafny.TypeDescriptor.<ReplicateKeyResponse>referenceWithInitializer(ReplicateKeyResponse.class, () -> ReplicateKeyResponse.Default());
  public static dafny.TypeDescriptor<ReplicateKeyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicateKeyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicateKeyResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ReplicateKeyResponse.create(Wrappers_Compile.Option.<KeyMetadata>Default(KeyMetadata._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())));
  public static ReplicateKeyResponse Default() {
    return theDefault;
  }
  public static ReplicateKeyResponse create(Wrappers_Compile.Option<KeyMetadata> ReplicaKeyMetadata, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaPolicy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> ReplicaTags) {
    return new ReplicateKeyResponse(ReplicaKeyMetadata, ReplicaPolicy, ReplicaTags);
  }
  public static ReplicateKeyResponse create_ReplicateKeyResponse(Wrappers_Compile.Option<KeyMetadata> ReplicaKeyMetadata, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaPolicy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> ReplicaTags) {
    return create(ReplicaKeyMetadata, ReplicaPolicy, ReplicaTags);
  }
  public boolean is_ReplicateKeyResponse() { return true; }
  public Wrappers_Compile.Option<KeyMetadata> dtor_ReplicaKeyMetadata() {
    return this._ReplicaKeyMetadata;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ReplicaPolicy() {
    return this._ReplicaPolicy;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_ReplicaTags() {
    return this._ReplicaTags;
  }
}
