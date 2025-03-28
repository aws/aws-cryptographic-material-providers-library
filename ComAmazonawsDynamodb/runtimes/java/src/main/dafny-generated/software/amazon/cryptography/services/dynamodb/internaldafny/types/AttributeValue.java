// Class AttributeValue
// Dafny class AttributeValue compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AttributeValue {
  public AttributeValue() {
  }
  private static final dafny.TypeDescriptor<AttributeValue> _TYPE = dafny.TypeDescriptor.<AttributeValue>referenceWithInitializer(AttributeValue.class, () -> AttributeValue.Default());
  public static dafny.TypeDescriptor<AttributeValue> _typeDescriptor() {
    return (dafny.TypeDescriptor<AttributeValue>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AttributeValue theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue.create_S(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static AttributeValue Default() {
    return theDefault;
  }
  public static AttributeValue create_S(dafny.DafnySequence<? extends Character> S) {
    return new AttributeValue_S(S);
  }
  public static AttributeValue create_N(dafny.DafnySequence<? extends Character> N) {
    return new AttributeValue_N(N);
  }
  public static AttributeValue create_B(dafny.DafnySequence<? extends java.lang.Byte> B) {
    return new AttributeValue_B(B);
  }
  public static AttributeValue create_SS(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> SS) {
    return new AttributeValue_SS(SS);
  }
  public static AttributeValue create_NS(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> NS) {
    return new AttributeValue_NS(NS);
  }
  public static AttributeValue create_BS(dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> BS) {
    return new AttributeValue_BS(BS);
  }
  public static AttributeValue create_M(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> M) {
    return new AttributeValue_M(M);
  }
  public static AttributeValue create_L(dafny.DafnySequence<? extends AttributeValue> L) {
    return new AttributeValue_L(L);
  }
  public static AttributeValue create_NULL(boolean NULL) {
    return new AttributeValue_NULL(NULL);
  }
  public static AttributeValue create_BOOL(boolean BOOL) {
    return new AttributeValue_BOOL(BOOL);
  }
  public boolean is_S() { return this instanceof AttributeValue_S; }
  public boolean is_N() { return this instanceof AttributeValue_N; }
  public boolean is_B() { return this instanceof AttributeValue_B; }
  public boolean is_SS() { return this instanceof AttributeValue_SS; }
  public boolean is_NS() { return this instanceof AttributeValue_NS; }
  public boolean is_BS() { return this instanceof AttributeValue_BS; }
  public boolean is_M() { return this instanceof AttributeValue_M; }
  public boolean is_L() { return this instanceof AttributeValue_L; }
  public boolean is_NULL() { return this instanceof AttributeValue_NULL; }
  public boolean is_BOOL() { return this instanceof AttributeValue_BOOL; }
  public dafny.DafnySequence<? extends Character> dtor_S() {
    AttributeValue d = this;
    return ((AttributeValue_S)d)._S;
  }
  public dafny.DafnySequence<? extends Character> dtor_N() {
    AttributeValue d = this;
    return ((AttributeValue_N)d)._N;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_B() {
    AttributeValue d = this;
    return ((AttributeValue_B)d)._B;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_SS() {
    AttributeValue d = this;
    return ((AttributeValue_SS)d)._SS;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_NS() {
    AttributeValue d = this;
    return ((AttributeValue_NS)d)._NS;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_BS() {
    AttributeValue d = this;
    return ((AttributeValue_BS)d)._BS;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_M() {
    AttributeValue d = this;
    return ((AttributeValue_M)d)._M;
  }
  public dafny.DafnySequence<? extends AttributeValue> dtor_L() {
    AttributeValue d = this;
    return ((AttributeValue_L)d)._L;
  }
  public boolean dtor_NULL() {
    AttributeValue d = this;
    return ((AttributeValue_NULL)d)._NULL;
  }
  public boolean dtor_BOOL() {
    AttributeValue d = this;
    return ((AttributeValue_BOOL)d)._BOOL;
  }
}
