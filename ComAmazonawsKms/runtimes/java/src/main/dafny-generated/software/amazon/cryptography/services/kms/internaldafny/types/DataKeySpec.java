// Class DataKeySpec
// Dafny class DataKeySpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DataKeySpec {
  public DataKeySpec() {
  }
  private static final dafny.TypeDescriptor<DataKeySpec> _TYPE = dafny.TypeDescriptor.<DataKeySpec>referenceWithInitializer(DataKeySpec.class, () -> DataKeySpec.Default());
  public static dafny.TypeDescriptor<DataKeySpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<DataKeySpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DataKeySpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec.create_AES__256();
  public static DataKeySpec Default() {
    return theDefault;
  }
  public static DataKeySpec create_AES__256() {
    return new DataKeySpec_AES__256();
  }
  public static DataKeySpec create_AES__128() {
    return new DataKeySpec_AES__128();
  }
  public boolean is_AES__256() { return this instanceof DataKeySpec_AES__256; }
  public boolean is_AES__128() { return this instanceof DataKeySpec_AES__128; }
  public static java.util.ArrayList<DataKeySpec> AllSingletonConstructors() {
    java.util.ArrayList<DataKeySpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DataKeySpec_AES__256());
    singleton_iterator.add(new DataKeySpec_AES__128());
    return singleton_iterator;
  }
}
