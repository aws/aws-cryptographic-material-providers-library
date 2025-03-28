// Class TestGenerateAndWrapKeyMaterial
// Dafny class TestGenerateAndWrapKeyMaterial compiled into Java
package TestIntermediateKeyWrapping_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class TestGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<TestInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public TestGenerateAndWrapKeyMaterial() {
  }
  public void __ctor()
  {
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<TestInfo>Default(TestInfo._typeDescriptor(), TestInfo.Default()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals((input).dtor_algorithmSuite(), __default.TEST__ALG__SUITE()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unexpected input on TestGenerateAndWrapMaterial")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<TestInfo>create(TestInfo._typeDescriptor(), __default.PLAINTEXT__MAT(), __default.WRAPPED__MAT(), TestIntermediateKeyWrapping_Compile.TestInfo.create()));
    return res;
  }
  private static final dafny.TypeDescriptor<TestGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<TestGenerateAndWrapKeyMaterial>referenceWithInitializer(TestGenerateAndWrapKeyMaterial.class, () -> (TestGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<TestGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<TestGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "TestIntermediateKeyWrapping.TestGenerateAndWrapKeyMaterial";
  }
}
