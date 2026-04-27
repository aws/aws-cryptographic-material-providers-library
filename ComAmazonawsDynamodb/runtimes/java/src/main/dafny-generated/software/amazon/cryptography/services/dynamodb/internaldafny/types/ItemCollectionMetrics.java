// Class ItemCollectionMetrics
// Dafny class ItemCollectionMetrics compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ItemCollectionMetrics {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ItemCollectionKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _SizeEstimateRangeGB;
  public ItemCollectionMetrics (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ItemCollectionKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> SizeEstimateRangeGB) {
    this._ItemCollectionKey = ItemCollectionKey;
    this._SizeEstimateRangeGB = SizeEstimateRangeGB;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ItemCollectionMetrics o = (ItemCollectionMetrics)other;
    return true && java.util.Objects.equals(this._ItemCollectionKey, o._ItemCollectionKey) && java.util.Objects.equals(this._SizeEstimateRangeGB, o._SizeEstimateRangeGB);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCollectionKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SizeEstimateRangeGB);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ItemCollectionMetrics.ItemCollectionMetrics");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ItemCollectionKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SizeEstimateRangeGB));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ItemCollectionMetrics> _TYPE = dafny.TypeDescriptor.<ItemCollectionMetrics>referenceWithInitializer(ItemCollectionMetrics.class, () -> ItemCollectionMetrics.Default());
  public static dafny.TypeDescriptor<ItemCollectionMetrics> _typeDescriptor() {
    return (dafny.TypeDescriptor<ItemCollectionMetrics>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ItemCollectionMetrics theDefault = ItemCollectionMetrics.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(ItemCollectionSizeEstimateBound._typeDescriptor())));
  public static ItemCollectionMetrics Default() {
    return theDefault;
  }
  public static ItemCollectionMetrics create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ItemCollectionKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> SizeEstimateRangeGB) {
    return new ItemCollectionMetrics(ItemCollectionKey, SizeEstimateRangeGB);
  }
  public static ItemCollectionMetrics create_ItemCollectionMetrics(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ItemCollectionKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> SizeEstimateRangeGB) {
    return create(ItemCollectionKey, SizeEstimateRangeGB);
  }
  public boolean is_ItemCollectionMetrics() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ItemCollectionKey() {
    return this._ItemCollectionKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> dtor_SizeEstimateRangeGB() {
    return this._SizeEstimateRangeGB;
  }
}
