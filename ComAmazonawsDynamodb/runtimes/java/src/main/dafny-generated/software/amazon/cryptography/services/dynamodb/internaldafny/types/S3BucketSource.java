// Class S3BucketSource
// Dafny class S3BucketSource compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class S3BucketSource {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3BucketOwner;
  public dafny.DafnySequence<? extends Character> _S3Bucket;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _S3KeyPrefix;
  public S3BucketSource (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3KeyPrefix) {
    this._S3BucketOwner = S3BucketOwner;
    this._S3Bucket = S3Bucket;
    this._S3KeyPrefix = S3KeyPrefix;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    S3BucketSource o = (S3BucketSource)other;
    return true && java.util.Objects.equals(this._S3BucketOwner, o._S3BucketOwner) && java.util.Objects.equals(this._S3Bucket, o._S3Bucket) && java.util.Objects.equals(this._S3KeyPrefix, o._S3KeyPrefix);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3BucketOwner);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3Bucket);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._S3KeyPrefix);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.S3BucketSource.S3BucketSource");
    s.append("(");
    s.append(dafny.Helpers.toString(this._S3BucketOwner));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3Bucket));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._S3KeyPrefix));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<S3BucketSource> _TYPE = dafny.TypeDescriptor.<S3BucketSource>referenceWithInitializer(S3BucketSource.class, () -> S3BucketSource.Default());
  public static dafny.TypeDescriptor<S3BucketSource> _typeDescriptor() {
    return (dafny.TypeDescriptor<S3BucketSource>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final S3BucketSource theDefault = S3BucketSource.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(S3Prefix._typeDescriptor()));
  public static S3BucketSource Default() {
    return theDefault;
  }
  public static S3BucketSource create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3KeyPrefix) {
    return new S3BucketSource(S3BucketOwner, S3Bucket, S3KeyPrefix);
  }
  public static S3BucketSource create_S3BucketSource(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3BucketOwner, dafny.DafnySequence<? extends Character> S3Bucket, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> S3KeyPrefix) {
    return create(S3BucketOwner, S3Bucket, S3KeyPrefix);
  }
  public boolean is_S3BucketSource() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3BucketOwner() {
    return this._S3BucketOwner;
  }
  public dafny.DafnySequence<? extends Character> dtor_S3Bucket() {
    return this._S3Bucket;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_S3KeyPrefix() {
    return this._S3KeyPrefix;
  }
}
