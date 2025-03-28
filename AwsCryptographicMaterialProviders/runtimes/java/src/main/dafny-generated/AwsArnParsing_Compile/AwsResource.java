// Class AwsResource
// Dafny class AwsResource compiled into Java
package AwsArnParsing_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsResource {
  public dafny.DafnySequence<? extends Character> _resourceType;
  public dafny.DafnySequence<? extends Character> _value;
  public AwsResource (dafny.DafnySequence<? extends Character> resourceType, dafny.DafnySequence<? extends Character> value) {
    this._resourceType = resourceType;
    this._value = value;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AwsResource o = (AwsResource)other;
    return true && java.util.Objects.equals(this._resourceType, o._resourceType) && java.util.Objects.equals(this._value, o._value);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._resourceType);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._value);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsArnParsing.AwsResource.AwsResource");
    s.append("(");
    s.append(dafny.Helpers.toString(this._resourceType));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._value));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AwsResource> _TYPE = dafny.TypeDescriptor.<AwsResource>referenceWithInitializer(AwsResource.class, () -> AwsResource.Default());
  public static dafny.TypeDescriptor<AwsResource> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsResource>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AwsResource theDefault = AwsArnParsing_Compile.AwsResource.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static AwsResource Default() {
    return theDefault;
  }
  public static AwsResource create(dafny.DafnySequence<? extends Character> resourceType, dafny.DafnySequence<? extends Character> value) {
    return new AwsResource(resourceType, value);
  }
  public static AwsResource create_AwsResource(dafny.DafnySequence<? extends Character> resourceType, dafny.DafnySequence<? extends Character> value) {
    return create(resourceType, value);
  }
  public boolean is_AwsResource() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_resourceType() {
    return this._resourceType;
  }
  public dafny.DafnySequence<? extends Character> dtor_value() {
    return this._value;
  }
  public boolean Valid() {
    return (true) && ((java.math.BigInteger.valueOf(((this).dtor_value()).length())).signum() == 1);
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate((this).dtor_resourceType(), dafny.DafnySequence.asString("/")), (this).dtor_value());
  }
}
