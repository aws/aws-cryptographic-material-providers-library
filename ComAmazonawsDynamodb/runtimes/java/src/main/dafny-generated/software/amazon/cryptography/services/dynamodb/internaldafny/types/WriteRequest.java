// Class WriteRequest
// Dafny class WriteRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class WriteRequest {
  public Wrappers_Compile.Option<PutRequest> _PutRequest;
  public Wrappers_Compile.Option<DeleteRequest> _DeleteRequest;
  public WriteRequest (Wrappers_Compile.Option<PutRequest> PutRequest, Wrappers_Compile.Option<DeleteRequest> DeleteRequest) {
    this._PutRequest = PutRequest;
    this._DeleteRequest = DeleteRequest;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WriteRequest o = (WriteRequest)other;
    return true && java.util.Objects.equals(this._PutRequest, o._PutRequest) && java.util.Objects.equals(this._DeleteRequest, o._DeleteRequest);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PutRequest);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeleteRequest);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.WriteRequest.WriteRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PutRequest));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeleteRequest));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<WriteRequest> _TYPE = dafny.TypeDescriptor.<WriteRequest>referenceWithInitializer(WriteRequest.class, () -> WriteRequest.Default());
  public static dafny.TypeDescriptor<WriteRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<WriteRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final WriteRequest theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.WriteRequest.create(Wrappers_Compile.Option.<PutRequest>Default(PutRequest._typeDescriptor()), Wrappers_Compile.Option.<DeleteRequest>Default(DeleteRequest._typeDescriptor()));
  public static WriteRequest Default() {
    return theDefault;
  }
  public static WriteRequest create(Wrappers_Compile.Option<PutRequest> PutRequest, Wrappers_Compile.Option<DeleteRequest> DeleteRequest) {
    return new WriteRequest(PutRequest, DeleteRequest);
  }
  public static WriteRequest create_WriteRequest(Wrappers_Compile.Option<PutRequest> PutRequest, Wrappers_Compile.Option<DeleteRequest> DeleteRequest) {
    return create(PutRequest, DeleteRequest);
  }
  public boolean is_WriteRequest() { return true; }
  public Wrappers_Compile.Option<PutRequest> dtor_PutRequest() {
    return this._PutRequest;
  }
  public Wrappers_Compile.Option<DeleteRequest> dtor_DeleteRequest() {
    return this._DeleteRequest;
  }
}
