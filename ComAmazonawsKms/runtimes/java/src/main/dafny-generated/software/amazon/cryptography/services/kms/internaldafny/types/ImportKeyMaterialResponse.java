// Class ImportKeyMaterialResponse
// Dafny class ImportKeyMaterialResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ImportKeyMaterialResponse {
  public ImportKeyMaterialResponse () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ImportKeyMaterialResponse o = (ImportKeyMaterialResponse)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ImportKeyMaterialResponse.ImportKeyMaterialResponse");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ImportKeyMaterialResponse> _TYPE = dafny.TypeDescriptor.<ImportKeyMaterialResponse>referenceWithInitializer(ImportKeyMaterialResponse.class, () -> ImportKeyMaterialResponse.Default());
  public static dafny.TypeDescriptor<ImportKeyMaterialResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportKeyMaterialResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportKeyMaterialResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ImportKeyMaterialResponse.create();
  public static ImportKeyMaterialResponse Default() {
    return theDefault;
  }
  public static ImportKeyMaterialResponse create() {
    return new ImportKeyMaterialResponse();
  }
  public static ImportKeyMaterialResponse create_ImportKeyMaterialResponse() {
    return create();
  }
  public boolean is_ImportKeyMaterialResponse() { return true; }
  public static java.util.ArrayList<ImportKeyMaterialResponse> AllSingletonConstructors() {
    java.util.ArrayList<ImportKeyMaterialResponse> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ImportKeyMaterialResponse());
    return singleton_iterator;
  }
}
