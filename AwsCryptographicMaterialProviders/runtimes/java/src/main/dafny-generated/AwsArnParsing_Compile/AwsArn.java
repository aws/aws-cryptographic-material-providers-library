// Class AwsArn
// Dafny class AwsArn compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsArn {
  public dafny.DafnySequence<? extends Character> _arnLiteral;
  public dafny.DafnySequence<? extends Character> _partition;
  public dafny.DafnySequence<? extends Character> _service;
  public dafny.DafnySequence<? extends Character> _region;
  public dafny.DafnySequence<? extends Character> _account;
  public AwsResource _resource;
  public AwsArn (dafny.DafnySequence<? extends Character> arnLiteral, dafny.DafnySequence<? extends Character> partition, dafny.DafnySequence<? extends Character> service, dafny.DafnySequence<? extends Character> region, dafny.DafnySequence<? extends Character> account, AwsResource resource) {
    this._arnLiteral = arnLiteral;
    this._partition = partition;
    this._service = service;
    this._region = region;
    this._account = account;
    this._resource = resource;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AwsArn o = (AwsArn)other;
    return true && java.util.Objects.equals(this._arnLiteral, o._arnLiteral) && java.util.Objects.equals(this._partition, o._partition) && java.util.Objects.equals(this._service, o._service) && java.util.Objects.equals(this._region, o._region) && java.util.Objects.equals(this._account, o._account) && java.util.Objects.equals(this._resource, o._resource);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._arnLiteral);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._partition);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._service);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._region);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._account);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._resource);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsArnParsing.AwsArn.AwsArn");
    s.append("(");
    s.append(dafny.Helpers.toString(this._arnLiteral));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._partition));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._service));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._region));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._account));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._resource));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AwsArn> _TYPE = dafny.TypeDescriptor.<AwsArn>referenceWithInitializer(AwsArn.class, () -> AwsArn.Default());
  public static dafny.TypeDescriptor<AwsArn> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsArn>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AwsArn theDefault = AwsArnParsing_Compile.AwsArn.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), AwsResource.Default());
  public static AwsArn Default() {
    return theDefault;
  }
  public static AwsArn create(dafny.DafnySequence<? extends Character> arnLiteral, dafny.DafnySequence<? extends Character> partition, dafny.DafnySequence<? extends Character> service, dafny.DafnySequence<? extends Character> region, dafny.DafnySequence<? extends Character> account, AwsResource resource) {
    return new AwsArn(arnLiteral, partition, service, region, account, resource);
  }
  public static AwsArn create_AwsArn(dafny.DafnySequence<? extends Character> arnLiteral, dafny.DafnySequence<? extends Character> partition, dafny.DafnySequence<? extends Character> service, dafny.DafnySequence<? extends Character> region, dafny.DafnySequence<? extends Character> account, AwsResource resource) {
    return create(arnLiteral, partition, service, region, account, resource);
  }
  public boolean is_AwsArn() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_arnLiteral() {
    return this._arnLiteral;
  }
  public dafny.DafnySequence<? extends Character> dtor_partition() {
    return this._partition;
  }
  public dafny.DafnySequence<? extends Character> dtor_service() {
    return this._service;
  }
  public dafny.DafnySequence<? extends Character> dtor_region() {
    return this._region;
  }
  public dafny.DafnySequence<? extends Character> dtor_account() {
    return this._account;
  }
  public AwsResource dtor_resource() {
    return this._resource;
  }
  public boolean Valid() {
    return (((((((this).dtor_arnLiteral()).equals(dafny.DafnySequence.asString("arn"))) && ((java.math.BigInteger.valueOf(((this).dtor_partition()).length())).signum() == 1)) && ((java.math.BigInteger.valueOf(((this).dtor_service()).length())).signum() == 1)) && ((java.math.BigInteger.valueOf(((this).dtor_region()).length())).signum() == 1)) && ((java.math.BigInteger.valueOf(((this).dtor_account()).length())).signum() == 1)) && (((this).dtor_resource()).Valid());
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    return (this).ToArnString(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  }
  public dafny.DafnySequence<? extends Character> ToArnString(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> customRegion) {
    AwsArn _this = this;
    TAIL_CALL_START: while (true) {
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _source0 = customRegion;
      if (_source0.is_None()) {
        AwsArn _in0 = _this;
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _in1 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_this).dtor_region());
        _this = _in0;
        ;
        customRegion = _in1;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends Character>>)_source0)._value;
        dafny.DafnySequence<? extends Character> _1_customRegion = _0___mcc_h0;
        return StandardLibrary_Compile.__default.<Character>Join(dafny.TypeDescriptor.CHAR, dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_this).dtor_arnLiteral(), (_this).dtor_partition(), (_this).dtor_service(), _1_customRegion, (_this).dtor_account(), ((_this).dtor_resource()).ToString()), dafny.DafnySequence.asString(":"));
      }
    }
  }
}
