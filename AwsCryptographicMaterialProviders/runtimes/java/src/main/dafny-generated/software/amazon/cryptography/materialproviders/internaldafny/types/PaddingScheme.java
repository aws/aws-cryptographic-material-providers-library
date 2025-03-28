// Class PaddingScheme
// Dafny class PaddingScheme compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class PaddingScheme {
  public PaddingScheme() {
  }
  private static final dafny.TypeDescriptor<PaddingScheme> _TYPE = dafny.TypeDescriptor.<PaddingScheme>referenceWithInitializer(PaddingScheme.class, () -> PaddingScheme.Default());
  public static dafny.TypeDescriptor<PaddingScheme> _typeDescriptor() {
    return (dafny.TypeDescriptor<PaddingScheme>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PaddingScheme theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_PKCS1();
  public static PaddingScheme Default() {
    return theDefault;
  }
  public static PaddingScheme create_PKCS1() {
    return new PaddingScheme_PKCS1();
  }
  public static PaddingScheme create_OAEP__SHA1__MGF1() {
    return new PaddingScheme_OAEP__SHA1__MGF1();
  }
  public static PaddingScheme create_OAEP__SHA256__MGF1() {
    return new PaddingScheme_OAEP__SHA256__MGF1();
  }
  public static PaddingScheme create_OAEP__SHA384__MGF1() {
    return new PaddingScheme_OAEP__SHA384__MGF1();
  }
  public static PaddingScheme create_OAEP__SHA512__MGF1() {
    return new PaddingScheme_OAEP__SHA512__MGF1();
  }
  public boolean is_PKCS1() { return this instanceof PaddingScheme_PKCS1; }
  public boolean is_OAEP__SHA1__MGF1() { return this instanceof PaddingScheme_OAEP__SHA1__MGF1; }
  public boolean is_OAEP__SHA256__MGF1() { return this instanceof PaddingScheme_OAEP__SHA256__MGF1; }
  public boolean is_OAEP__SHA384__MGF1() { return this instanceof PaddingScheme_OAEP__SHA384__MGF1; }
  public boolean is_OAEP__SHA512__MGF1() { return this instanceof PaddingScheme_OAEP__SHA512__MGF1; }
  public static java.util.ArrayList<PaddingScheme> AllSingletonConstructors() {
    java.util.ArrayList<PaddingScheme> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new PaddingScheme_PKCS1());
    singleton_iterator.add(new PaddingScheme_OAEP__SHA1__MGF1());
    singleton_iterator.add(new PaddingScheme_OAEP__SHA256__MGF1());
    singleton_iterator.add(new PaddingScheme_OAEP__SHA384__MGF1());
    singleton_iterator.add(new PaddingScheme_OAEP__SHA512__MGF1());
    return singleton_iterator;
  }
}
