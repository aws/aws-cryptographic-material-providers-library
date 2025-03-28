// Class AttributeValue_NS
// Dafny class AttributeValue_NS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValue_NS extends AttributeValue {
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _NS;
  public AttributeValue_NS (dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> NS) {
    super();
    this._NS = NS;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValue_NS o = (AttributeValue_NS)other;
    return true && java.util.Objects.equals(this._NS, o._NS);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NS);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValue.NS");
    s.append("(");
    s.append(dafny.Helpers.toString(this._NS));
    s.append(")");
    return s.toString();
  }
}
