// Class GrantOperation
// Dafny class GrantOperation compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class GrantOperation {
  public GrantOperation() {
  }
  private static final dafny.TypeDescriptor<GrantOperation> _TYPE = dafny.TypeDescriptor.<GrantOperation>referenceWithInitializer(GrantOperation.class, () -> GrantOperation.Default());
  public static dafny.TypeDescriptor<GrantOperation> _typeDescriptor() {
    return (dafny.TypeDescriptor<GrantOperation>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GrantOperation theDefault = GrantOperation.create_Decrypt();
  public static GrantOperation Default() {
    return theDefault;
  }
  public static GrantOperation create_Decrypt() {
    return new GrantOperation_Decrypt();
  }
  public static GrantOperation create_Encrypt() {
    return new GrantOperation_Encrypt();
  }
  public static GrantOperation create_GenerateDataKey() {
    return new GrantOperation_GenerateDataKey();
  }
  public static GrantOperation create_GenerateDataKeyWithoutPlaintext() {
    return new GrantOperation_GenerateDataKeyWithoutPlaintext();
  }
  public static GrantOperation create_ReEncryptFrom() {
    return new GrantOperation_ReEncryptFrom();
  }
  public static GrantOperation create_ReEncryptTo() {
    return new GrantOperation_ReEncryptTo();
  }
  public static GrantOperation create_Sign() {
    return new GrantOperation_Sign();
  }
  public static GrantOperation create_Verify() {
    return new GrantOperation_Verify();
  }
  public static GrantOperation create_GetPublicKey() {
    return new GrantOperation_GetPublicKey();
  }
  public static GrantOperation create_CreateGrant() {
    return new GrantOperation_CreateGrant();
  }
  public static GrantOperation create_RetireGrant() {
    return new GrantOperation_RetireGrant();
  }
  public static GrantOperation create_DescribeKey() {
    return new GrantOperation_DescribeKey();
  }
  public static GrantOperation create_GenerateDataKeyPair() {
    return new GrantOperation_GenerateDataKeyPair();
  }
  public static GrantOperation create_GenerateDataKeyPairWithoutPlaintext() {
    return new GrantOperation_GenerateDataKeyPairWithoutPlaintext();
  }
  public static GrantOperation create_GenerateMac() {
    return new GrantOperation_GenerateMac();
  }
  public static GrantOperation create_VerifyMac() {
    return new GrantOperation_VerifyMac();
  }
  public static GrantOperation create_DeriveSharedSecret() {
    return new GrantOperation_DeriveSharedSecret();
  }
  public boolean is_Decrypt() { return this instanceof GrantOperation_Decrypt; }
  public boolean is_Encrypt() { return this instanceof GrantOperation_Encrypt; }
  public boolean is_GenerateDataKey() { return this instanceof GrantOperation_GenerateDataKey; }
  public boolean is_GenerateDataKeyWithoutPlaintext() { return this instanceof GrantOperation_GenerateDataKeyWithoutPlaintext; }
  public boolean is_ReEncryptFrom() { return this instanceof GrantOperation_ReEncryptFrom; }
  public boolean is_ReEncryptTo() { return this instanceof GrantOperation_ReEncryptTo; }
  public boolean is_Sign() { return this instanceof GrantOperation_Sign; }
  public boolean is_Verify() { return this instanceof GrantOperation_Verify; }
  public boolean is_GetPublicKey() { return this instanceof GrantOperation_GetPublicKey; }
  public boolean is_CreateGrant() { return this instanceof GrantOperation_CreateGrant; }
  public boolean is_RetireGrant() { return this instanceof GrantOperation_RetireGrant; }
  public boolean is_DescribeKey() { return this instanceof GrantOperation_DescribeKey; }
  public boolean is_GenerateDataKeyPair() { return this instanceof GrantOperation_GenerateDataKeyPair; }
  public boolean is_GenerateDataKeyPairWithoutPlaintext() { return this instanceof GrantOperation_GenerateDataKeyPairWithoutPlaintext; }
  public boolean is_GenerateMac() { return this instanceof GrantOperation_GenerateMac; }
  public boolean is_VerifyMac() { return this instanceof GrantOperation_VerifyMac; }
  public boolean is_DeriveSharedSecret() { return this instanceof GrantOperation_DeriveSharedSecret; }
  public static java.util.ArrayList<GrantOperation> AllSingletonConstructors() {
    java.util.ArrayList<GrantOperation> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new GrantOperation_Decrypt());
    singleton_iterator.add(new GrantOperation_Encrypt());
    singleton_iterator.add(new GrantOperation_GenerateDataKey());
    singleton_iterator.add(new GrantOperation_GenerateDataKeyWithoutPlaintext());
    singleton_iterator.add(new GrantOperation_ReEncryptFrom());
    singleton_iterator.add(new GrantOperation_ReEncryptTo());
    singleton_iterator.add(new GrantOperation_Sign());
    singleton_iterator.add(new GrantOperation_Verify());
    singleton_iterator.add(new GrantOperation_GetPublicKey());
    singleton_iterator.add(new GrantOperation_CreateGrant());
    singleton_iterator.add(new GrantOperation_RetireGrant());
    singleton_iterator.add(new GrantOperation_DescribeKey());
    singleton_iterator.add(new GrantOperation_GenerateDataKeyPair());
    singleton_iterator.add(new GrantOperation_GenerateDataKeyPairWithoutPlaintext());
    singleton_iterator.add(new GrantOperation_GenerateMac());
    singleton_iterator.add(new GrantOperation_VerifyMac());
    singleton_iterator.add(new GrantOperation_DeriveSharedSecret());
    return singleton_iterator;
  }
}
