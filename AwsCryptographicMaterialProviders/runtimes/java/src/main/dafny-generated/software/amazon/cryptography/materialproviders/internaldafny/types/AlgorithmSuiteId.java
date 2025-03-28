// Class AlgorithmSuiteId
// Dafny class AlgorithmSuiteId compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AlgorithmSuiteId {
  public AlgorithmSuiteId() {
  }
  private static final dafny.TypeDescriptor<AlgorithmSuiteId> _TYPE = dafny.TypeDescriptor.<AlgorithmSuiteId>referenceWithInitializer(AlgorithmSuiteId.class, () -> AlgorithmSuiteId.Default());
  public static dafny.TypeDescriptor<AlgorithmSuiteId> _typeDescriptor() {
    return (dafny.TypeDescriptor<AlgorithmSuiteId>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AlgorithmSuiteId theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(ESDKAlgorithmSuiteId.Default());
  public static AlgorithmSuiteId Default() {
    return theDefault;
  }
  public static AlgorithmSuiteId create_ESDK(ESDKAlgorithmSuiteId ESDK) {
    return new AlgorithmSuiteId_ESDK(ESDK);
  }
  public static AlgorithmSuiteId create_DBE(DBEAlgorithmSuiteId DBE) {
    return new AlgorithmSuiteId_DBE(DBE);
  }
  public boolean is_ESDK() { return this instanceof AlgorithmSuiteId_ESDK; }
  public boolean is_DBE() { return this instanceof AlgorithmSuiteId_DBE; }
  public ESDKAlgorithmSuiteId dtor_ESDK() {
    AlgorithmSuiteId d = this;
    return ((AlgorithmSuiteId_ESDK)d)._ESDK;
  }
  public DBEAlgorithmSuiteId dtor_DBE() {
    AlgorithmSuiteId d = this;
    return ((AlgorithmSuiteId_DBE)d)._DBE;
  }
}
