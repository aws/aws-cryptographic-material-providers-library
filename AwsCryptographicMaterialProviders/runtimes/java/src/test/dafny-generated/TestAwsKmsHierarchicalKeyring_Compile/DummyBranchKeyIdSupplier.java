// Class DummyBranchKeyIdSupplier
// Dafny class DummyBranchKeyIdSupplier compiled into Java
package TestAwsKmsHierarchicalKeyring_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;
import TestUtils_Compile.*;
import TestIntermediateKeyWrapping_Compile.*;
import TestErrorMessages_Compile.*;
import TestDefaultClientProvider_Compile.*;
import TestRawECDHKeyring_Compile.*;
import TestRawAESKeyring_Compile.*;
import TestMultiKeyring_Compile.*;
import TestRawRSAKeying_Compile.*;
import TestAwsKmsRsaKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DummyBranchKeyIdSupplier implements software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier {
  public DummyBranchKeyIdSupplier() {
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetBranchKeyId(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IBranchKeyIdSupplier.GetBranchKeyId(this, input);
    return _out0;
  }
  public void __ctor()
  {
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetBranchKeyId_k(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput.Default());
    if(true) {
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_context;
      _0_context = (input).dtor_encryptionContext();
      if ((((_0_context).keySet()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(__default.BRANCH__KEY())) && ((((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_0_context).get(__default.BRANCH__KEY())))).equals(__default.CASE__A()))) {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput.create(__default.BRANCH__KEY__ID__A()));
        return output;
      } else if ((((_0_context).keySet()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(__default.BRANCH__KEY())) && ((((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_0_context).get(__default.BRANCH__KEY())))).equals(__default.CASE__B()))) {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput.create(__default.BRANCH__KEY__ID__B()));
        return output;
      } else {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Can't determine branchKeyId from context")));
        return output;
      }
    }
    return output;
  }
  private static final dafny.TypeDescriptor<DummyBranchKeyIdSupplier> _TYPE = dafny.TypeDescriptor.<DummyBranchKeyIdSupplier>referenceWithInitializer(DummyBranchKeyIdSupplier.class, () -> (DummyBranchKeyIdSupplier) null);
  public static dafny.TypeDescriptor<DummyBranchKeyIdSupplier> _typeDescriptor() {
    return (dafny.TypeDescriptor<DummyBranchKeyIdSupplier>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier";
  }
}
