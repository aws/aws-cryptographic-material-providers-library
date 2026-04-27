// Class AesWrappingAlg
// Dafny class AesWrappingAlg compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AesWrappingAlg {
  public AesWrappingAlg() {
  }
  private static final dafny.TypeDescriptor<AesWrappingAlg> _TYPE = dafny.TypeDescriptor.<AesWrappingAlg>referenceWithInitializer(AesWrappingAlg.class, () -> AesWrappingAlg.Default());
  public static dafny.TypeDescriptor<AesWrappingAlg> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesWrappingAlg>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesWrappingAlg theDefault = AesWrappingAlg.create_ALG__AES128__GCM__IV12__TAG16();
  public static AesWrappingAlg Default() {
    return theDefault;
  }
  public static AesWrappingAlg create_ALG__AES128__GCM__IV12__TAG16() {
    return new AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16();
  }
  public static AesWrappingAlg create_ALG__AES192__GCM__IV12__TAG16() {
    return new AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16();
  }
  public static AesWrappingAlg create_ALG__AES256__GCM__IV12__TAG16() {
    return new AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16();
  }
  public boolean is_ALG__AES128__GCM__IV12__TAG16() { return this instanceof AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16; }
  public boolean is_ALG__AES192__GCM__IV12__TAG16() { return this instanceof AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16; }
  public boolean is_ALG__AES256__GCM__IV12__TAG16() { return this instanceof AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16; }
  public static java.util.ArrayList<AesWrappingAlg> AllSingletonConstructors() {
    java.util.ArrayList<AesWrappingAlg> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16());
    singleton_iterator.add(new AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16());
    singleton_iterator.add(new AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16());
    return singleton_iterator;
  }
}
