// Class GetBranchKeyIdInput
// Dafny class GetBranchKeyIdInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetBranchKeyIdInput {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _encryptionContext;
  public GetBranchKeyIdInput (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    this._encryptionContext = encryptionContext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetBranchKeyIdInput o = (GetBranchKeyIdInput)other;
    return true && java.util.Objects.equals(this._encryptionContext, o._encryptionContext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionContext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput.GetBranchKeyIdInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encryptionContext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetBranchKeyIdInput> _TYPE = dafny.TypeDescriptor.<GetBranchKeyIdInput>referenceWithInitializer(GetBranchKeyIdInput.class, () -> GetBranchKeyIdInput.Default());
  public static dafny.TypeDescriptor<GetBranchKeyIdInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetBranchKeyIdInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetBranchKeyIdInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput.create(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>,dafny.DafnySequence<? extends java.lang.Byte>> empty());
  public static GetBranchKeyIdInput Default() {
    return theDefault;
  }
  public static GetBranchKeyIdInput create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    return new GetBranchKeyIdInput(encryptionContext);
  }
  public static GetBranchKeyIdInput create_GetBranchKeyIdInput(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContext) {
    return create(encryptionContext);
  }
  public boolean is_GetBranchKeyIdInput() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> dtor_encryptionContext() {
    return this._encryptionContext;
  }
}
