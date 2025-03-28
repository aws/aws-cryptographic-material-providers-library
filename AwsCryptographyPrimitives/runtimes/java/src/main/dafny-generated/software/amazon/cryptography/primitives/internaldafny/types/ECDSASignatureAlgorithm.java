// Class ECDSASignatureAlgorithm
// Dafny class ECDSASignatureAlgorithm compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ECDSASignatureAlgorithm {
  public ECDSASignatureAlgorithm() {
  }
  private static final dafny.TypeDescriptor<ECDSASignatureAlgorithm> _TYPE = dafny.TypeDescriptor.<ECDSASignatureAlgorithm>referenceWithInitializer(ECDSASignatureAlgorithm.class, () -> ECDSASignatureAlgorithm.Default());
  public static dafny.TypeDescriptor<ECDSASignatureAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECDSASignatureAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECDSASignatureAlgorithm theDefault = software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384();
  public static ECDSASignatureAlgorithm Default() {
    return theDefault;
  }
  public static ECDSASignatureAlgorithm create_ECDSA__P384() {
    return new ECDSASignatureAlgorithm_ECDSA__P384();
  }
  public static ECDSASignatureAlgorithm create_ECDSA__P256() {
    return new ECDSASignatureAlgorithm_ECDSA__P256();
  }
  public boolean is_ECDSA__P384() { return this instanceof ECDSASignatureAlgorithm_ECDSA__P384; }
  public boolean is_ECDSA__P256() { return this instanceof ECDSASignatureAlgorithm_ECDSA__P256; }
  public static java.util.ArrayList<ECDSASignatureAlgorithm> AllSingletonConstructors() {
    java.util.ArrayList<ECDSASignatureAlgorithm> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ECDSASignatureAlgorithm_ECDSA__P384());
    singleton_iterator.add(new ECDSASignatureAlgorithm_ECDSA__P256());
    return singleton_iterator;
  }
}
