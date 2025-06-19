// Class DigestAlgorithm
// Dafny class DigestAlgorithm compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DigestAlgorithm {
  public DigestAlgorithm() {
  }
  private static final dafny.TypeDescriptor<DigestAlgorithm> _TYPE = dafny.TypeDescriptor.<DigestAlgorithm>referenceWithInitializer(DigestAlgorithm.class, () -> DigestAlgorithm.Default());
  public static dafny.TypeDescriptor<DigestAlgorithm> _typeDescriptor() {
    return (dafny.TypeDescriptor<DigestAlgorithm>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DigestAlgorithm theDefault = DigestAlgorithm.create_SHA__512();
  public static DigestAlgorithm Default() {
    return theDefault;
  }
  public static DigestAlgorithm create_SHA__512() {
    return new DigestAlgorithm_SHA__512();
  }
  public static DigestAlgorithm create_SHA__384() {
    return new DigestAlgorithm_SHA__384();
  }
  public static DigestAlgorithm create_SHA__256() {
    return new DigestAlgorithm_SHA__256();
  }
  public boolean is_SHA__512() { return this instanceof DigestAlgorithm_SHA__512; }
  public boolean is_SHA__384() { return this instanceof DigestAlgorithm_SHA__384; }
  public boolean is_SHA__256() { return this instanceof DigestAlgorithm_SHA__256; }
  public static java.util.ArrayList<DigestAlgorithm> AllSingletonConstructors() {
    java.util.ArrayList<DigestAlgorithm> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DigestAlgorithm_SHA__512());
    singleton_iterator.add(new DigestAlgorithm_SHA__384());
    singleton_iterator.add(new DigestAlgorithm_SHA__256());
    return singleton_iterator;
  }
}
