// Class MacAlgorithmSpec
// Dafny class MacAlgorithmSpec compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class MacAlgorithmSpec {
  public MacAlgorithmSpec() {
  }
  private static final dafny.TypeDescriptor<MacAlgorithmSpec> _TYPE = dafny.TypeDescriptor.<MacAlgorithmSpec>referenceWithInitializer(MacAlgorithmSpec.class, () -> MacAlgorithmSpec.Default());
  public static dafny.TypeDescriptor<MacAlgorithmSpec> _typeDescriptor() {
    return (dafny.TypeDescriptor<MacAlgorithmSpec>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MacAlgorithmSpec theDefault = software.amazon.cryptography.services.kms.internaldafny.types.MacAlgorithmSpec.create_HMAC__SHA__224();
  public static MacAlgorithmSpec Default() {
    return theDefault;
  }
  public static MacAlgorithmSpec create_HMAC__SHA__224() {
    return new MacAlgorithmSpec_HMAC__SHA__224();
  }
  public static MacAlgorithmSpec create_HMAC__SHA__256() {
    return new MacAlgorithmSpec_HMAC__SHA__256();
  }
  public static MacAlgorithmSpec create_HMAC__SHA__384() {
    return new MacAlgorithmSpec_HMAC__SHA__384();
  }
  public static MacAlgorithmSpec create_HMAC__SHA__512() {
    return new MacAlgorithmSpec_HMAC__SHA__512();
  }
  public boolean is_HMAC__SHA__224() { return this instanceof MacAlgorithmSpec_HMAC__SHA__224; }
  public boolean is_HMAC__SHA__256() { return this instanceof MacAlgorithmSpec_HMAC__SHA__256; }
  public boolean is_HMAC__SHA__384() { return this instanceof MacAlgorithmSpec_HMAC__SHA__384; }
  public boolean is_HMAC__SHA__512() { return this instanceof MacAlgorithmSpec_HMAC__SHA__512; }
  public static java.util.ArrayList<MacAlgorithmSpec> AllSingletonConstructors() {
    java.util.ArrayList<MacAlgorithmSpec> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new MacAlgorithmSpec_HMAC__SHA__224());
    singleton_iterator.add(new MacAlgorithmSpec_HMAC__SHA__256());
    singleton_iterator.add(new MacAlgorithmSpec_HMAC__SHA__384());
    singleton_iterator.add(new MacAlgorithmSpec_HMAC__SHA__512());
    return singleton_iterator;
  }
}
