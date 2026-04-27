// Class DBEAlgorithmSuiteId
// Dafny class DBEAlgorithmSuiteId compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DBEAlgorithmSuiteId {
  public DBEAlgorithmSuiteId() {
  }
  private static final dafny.TypeDescriptor<DBEAlgorithmSuiteId> _TYPE = dafny.TypeDescriptor.<DBEAlgorithmSuiteId>referenceWithInitializer(DBEAlgorithmSuiteId.class, () -> DBEAlgorithmSuiteId.Default());
  public static dafny.TypeDescriptor<DBEAlgorithmSuiteId> _typeDescriptor() {
    return (dafny.TypeDescriptor<DBEAlgorithmSuiteId>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DBEAlgorithmSuiteId theDefault = DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384();
  public static DBEAlgorithmSuiteId Default() {
    return theDefault;
  }
  public static DBEAlgorithmSuiteId create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384() {
    return new DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384();
  }
  public static DBEAlgorithmSuiteId create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384() {
    return new DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384();
  }
  public boolean is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384() { return this instanceof DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384; }
  public boolean is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384() { return this instanceof DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384; }
  public static java.util.ArrayList<DBEAlgorithmSuiteId> AllSingletonConstructors() {
    java.util.ArrayList<DBEAlgorithmSuiteId> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384());
    singleton_iterator.add(new DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384());
    return singleton_iterator;
  }
}
