// Class ESDKAlgorithmSuiteId
// Dafny class ESDKAlgorithmSuiteId compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ESDKAlgorithmSuiteId {
  public ESDKAlgorithmSuiteId() {
  }
  private static final dafny.TypeDescriptor<ESDKAlgorithmSuiteId> _TYPE = dafny.TypeDescriptor.<ESDKAlgorithmSuiteId>referenceWithInitializer(ESDKAlgorithmSuiteId.class, () -> ESDKAlgorithmSuiteId.Default());
  public static dafny.TypeDescriptor<ESDKAlgorithmSuiteId> _typeDescriptor() {
    return (dafny.TypeDescriptor<ESDKAlgorithmSuiteId>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ESDKAlgorithmSuiteId theDefault = ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF();
  public static ESDKAlgorithmSuiteId Default() {
    return theDefault;
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF() {
    return new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF() {
    return new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF() {
    return new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256() {
    return new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256() {
    return new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256() {
    return new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256() {
    return new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() {
    return new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() {
    return new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY() {
    return new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY();
  }
  public static ESDKAlgorithmSuiteId create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384() {
    return new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384();
  }
  public boolean is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF; }
  public boolean is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF; }
  public boolean is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF; }
  public boolean is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256; }
  public boolean is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256; }
  public boolean is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256; }
  public boolean is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256; }
  public boolean is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384; }
  public boolean is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384; }
  public boolean is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY; }
  public boolean is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384() { return this instanceof ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384; }
  public static java.util.ArrayList<ESDKAlgorithmSuiteId> AllSingletonConstructors() {
    java.util.ArrayList<ESDKAlgorithmSuiteId> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY());
    singleton_iterator.add(new ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384());
    return singleton_iterator;
  }
}
