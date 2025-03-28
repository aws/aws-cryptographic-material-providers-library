// Interface IBranchKeyIdSupplier
// Dafny trait IBranchKeyIdSupplier compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class _Companion_IBranchKeyIdSupplier {
  public _Companion_IBranchKeyIdSupplier() {
  }
  private static final dafny.TypeDescriptor<IBranchKeyIdSupplier> _TYPE = dafny.TypeDescriptor.referenceWithInitializer(IBranchKeyIdSupplier.class, () -> null);
  public static dafny.TypeDescriptor<IBranchKeyIdSupplier> _typeDescriptor() {
    return (dafny.TypeDescriptor<IBranchKeyIdSupplier>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  public static Wrappers_Compile.Result<GetBranchKeyIdOutput, Error> GetBranchKeyId(IBranchKeyIdSupplier _this, GetBranchKeyIdInput input)
  {
    Wrappers_Compile.Result<GetBranchKeyIdOutput, Error> output = Wrappers_Compile.Result.<GetBranchKeyIdOutput, Error>Default(GetBranchKeyIdOutput._typeDescriptor(), Error._typeDescriptor(), GetBranchKeyIdOutput.Default());
    if(true) {
      Wrappers_Compile.Result<GetBranchKeyIdOutput, Error> _out0;
      _out0 = (_this).GetBranchKeyId_k(input);
      output = _out0;
    }
    return output;
  }
}
