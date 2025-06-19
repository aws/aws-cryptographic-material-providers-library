// Class TestUnwrapKeyMaterial
// Dafny class TestUnwrapKeyMaterial compiled into Java
package TestIntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class TestUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<TestInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public TestUnwrapKeyMaterial() {
  }
  public void __ctor()
  {
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<TestInfo>Default(TestInfo._typeDescriptor(), TestInfo.Default()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((input).dtor_wrappedMaterial()).equals(__default.WRAPPED__MAT()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unexpected input on TestUnwrapMaterial")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<TestInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals((input).dtor_algorithmSuite(), __default.TEST__ALG__SUITE()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unexpected input on TestUnwrapMaterial")));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<TestInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<TestInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<TestInfo>_typeDescriptor(TestInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<TestInfo>create(TestInfo._typeDescriptor(), __default.PLAINTEXT__MAT(), TestInfo.create()));
    return res;
  }
  private static final dafny.TypeDescriptor<TestUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<TestUnwrapKeyMaterial>referenceWithInitializer(TestUnwrapKeyMaterial.class, () -> (TestUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<TestUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<TestUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "TestIntermediateKeyWrapping.TestUnwrapKeyMaterial";
  }
}
