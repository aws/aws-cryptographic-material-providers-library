// Class OnDecryptHierarchyEncryptedDataKeyFilter
// Dafny class OnDecryptHierarchyEncryptedDataKeyFilter compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDecryptHierarchyEncryptedDataKeyFilter implements Actions_Compile.DeterministicActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.DeterministicAction<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public OnDecryptHierarchyEncryptedDataKeyFilter() {
    this._branchKeyId = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
  }
  public void __ctor(dafny.DafnySequence<? extends Character> branchKeyId)
  {
    (this)._branchKeyId = branchKeyId;
  }
  public Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    dafny.DafnySequence<? extends java.lang.Byte> _0_providerInfo;
    _0_providerInfo = (edk).dtor_keyProviderInfo();
    dafny.DafnySequence<? extends java.lang.Byte> _1_providerId;
    _1_providerId = (edk).dtor_keyProviderId();
    if (!(_1_providerId).equals(Constants_Compile.__default.PROVIDER__ID__HIERARCHY())) {
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _2_valueOrError0 = (UTF8.__default.Decode(_0_providerInfo)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_3_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _3_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_3_e_boxed0));
      return __default.E(dafny.DafnySequence.asString("Invalid encoding, provider info is not UTF8."));
    }));
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<Boolean>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
      return res;
    }
    dafny.DafnySequence<? extends Character> _4_branchKeyId;
    _4_branchKeyId = (_2_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).branchKeyId()).equals(_4_branchKeyId));
    return res;
  }
  public dafny.DafnySequence<? extends Character> _branchKeyId;
  public dafny.DafnySequence<? extends Character> branchKeyId()
  {
    return this._branchKeyId;
  }
  private static final dafny.TypeDescriptor<OnDecryptHierarchyEncryptedDataKeyFilter> _TYPE = dafny.TypeDescriptor.<OnDecryptHierarchyEncryptedDataKeyFilter>referenceWithInitializer(OnDecryptHierarchyEncryptedDataKeyFilter.class, () -> (OnDecryptHierarchyEncryptedDataKeyFilter) null);
  public static dafny.TypeDescriptor<OnDecryptHierarchyEncryptedDataKeyFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptHierarchyEncryptedDataKeyFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter";
  }
}
