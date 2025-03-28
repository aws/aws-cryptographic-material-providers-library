// Class WrapInput
// Dafny class WrapInput compiled into Java
package MaterialWrapping_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class WrapInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintextMaterial;
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _algorithmSuite;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public WrapInput (dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    this._plaintextMaterial = plaintextMaterial;
    this._algorithmSuite = algorithmSuite;
    this._encryptionContext = encryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrapInput o = (WrapInput)other;
    return true && java.util.Objects.equals(this._plaintextMaterial, o._plaintextMaterial) && java.util.Objects.equals(this._algorithmSuite, o._algorithmSuite) && java.util.Objects.equals(this._encryptionContext, o._encryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintextMaterial);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._algorithmSuite);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("MaterialWrapping.WrapInput.WrapInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._plaintextMaterial));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._algorithmSuite));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<WrapInput> _TYPE = dafny.TypeDescriptor.<WrapInput>referenceWithInitializer(WrapInput.class, () -> WrapInput.Default());
  public static dafny.TypeDescriptor<WrapInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<WrapInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final WrapInput theDefault = MaterialWrapping_Compile.WrapInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.Default(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
  public static WrapInput Default() {
    return theDefault;
  }
  public static WrapInput create(dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    return new WrapInput(plaintextMaterial, algorithmSuite, encryptionContext);
  }
  public static WrapInput create_WrapInput(dafny.DafnySequence<? extends java.lang.Byte> plaintextMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algorithmSuite, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    return create(plaintextMaterial, algorithmSuite, encryptionContext);
  }
  public boolean is_WrapInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintextMaterial() {
    return this._plaintextMaterial;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo dtor_algorithmSuite() {
    return this._algorithmSuite;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
}
