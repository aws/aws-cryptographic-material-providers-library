// Class __default
// Dafny class __default compiled into Java
package RawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput DeserializeEDKCiphertext(dafny.DafnySequence<? extends java.lang.Byte> ciphertext, long tagLen)
  {
    long _0_encryptedKeyLength = (long) (long) (((long) (ciphertext).cardinalityInt()) - (tagLen));
    return software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.create((ciphertext).take(_0_encryptedKeyLength), (ciphertext).drop(_0_encryptedKeyLength));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SerializeEDKCiphertext(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput encOutput) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate((encOutput).dtor_cipherText(), (encOutput).dtor_authTag());
  }
  public static long AUTH__TAG__LEN__LEN()
  {
    return (long) 4L;
  }
  public static long IV__LEN__LEN()
  {
    return (long) 4L;
  }
  @Override
  public java.lang.String toString() {
    return "RawAESKeyring._default";
  }
}
