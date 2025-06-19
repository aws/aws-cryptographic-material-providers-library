// Class __default
// Dafny class __default compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean cacheEntryWithinLimits(long creationTime, long now, long ttlSeconds)
  {
    return ((long) (long) ((now) - (creationTime))) <= (ttlSeconds);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeriveEncryptionKeyFromBranchKey(dafny.DafnySequence<? extends java.lang.Byte> branchKey, dafny.DafnySequence<? extends java.lang.Byte> salt, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> purpose, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeDerivedBranchKey;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = (cryptoPrimitives).KdfCounterMode(software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput.create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256(), branchKey, __default.DERIVED__BRANCH__KEY__EXPECTED__LENGTH(), purpose, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), salt)));
      _0_maybeDerivedBranchKey = _out0;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _1_valueOrError0 = (_0_maybeDerivedBranchKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_1_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        return output;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _3_derivedBranchKey;
      _3_derivedBranchKey = (_1_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _3_derivedBranchKey);
    }
    return output;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> WrappingAad(dafny.DafnySequence<? extends java.lang.Byte> branchKeyId, dafny.DafnySequence<? extends java.lang.Byte> branchKeyVersion, dafny.DafnySequence<? extends java.lang.Byte> aad)
  {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(Constants_Compile.__default.PROVIDER__ID__HIERARCHY(), branchKeyId), branchKeyVersion), aad);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SerializeEDKCiphertext(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput encOutput) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate((encOutput).dtor_cipherText(), (encOutput).dtor_authTag());
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Error E(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(s);
  }
  public static int AES__256__ENC__KEY__LENGTH()
  {
    return 32;
  }
  public static int AES__256__ENC__TAG__LENGTH()
  {
    return 16;
  }
  public static int AES__256__ENC__IV__LENGTH()
  {
    return 12;
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.AES__GCM AES__256__ENC__ALG()
  {
    return software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(__default.AES__256__ENC__KEY__LENGTH(), __default.AES__256__ENC__TAG__LENGTH(), __default.AES__256__ENC__IV__LENGTH());
  }
  public static int H__WRAP__SALT__LEN()
  {
    return 16;
  }
  public static int H__WRAP__NONCE__LEN()
  {
    return 12;
  }
  public static int EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX()
  {
    return (int) ((__default.H__WRAP__SALT__LEN()) + (__default.H__WRAP__NONCE__LEN()));
  }
  public static int EDK__CIPHERTEXT__VERSION__LENGTH()
  {
    return 16;
  }
  public static int EDK__CIPHERTEXT__VERSION__INDEX()
  {
    return (int) ((__default.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX()) + (__default.EDK__CIPHERTEXT__VERSION__LENGTH()));
  }
  public static int EXPECTED__EDK__CIPHERTEXT__OVERHEAD()
  {
    return (int) ((__default.EDK__CIPHERTEXT__VERSION__INDEX()) + (__default.AES__256__ENC__TAG__LENGTH()));
  }
  public static int DERIVED__BRANCH__KEY__EXPECTED__LENGTH()
  {
    return 32;
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__STORE__GSI()
  {
    return dafny.DafnySequence.asString("Active-Keys");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__FIELD()
  {
    return dafny.DafnySequence.asString("enc");
  }
  public static dafny.DafnySequence<? extends Character> VERSION__FIELD()
  {
    return dafny.DafnySequence.asString("version");
  }
  public static dafny.DafnySequence<? extends Character> BRANCH__KEY__IDENTIFIER__FIELD()
  {
    return dafny.DafnySequence.asString("branch-key-id");
  }
  public static dafny.DafnySequence<? extends Character> KEY__CONDITION__EXPRESSION()
  {
    return dafny.DafnySequence.asString("#status = :status and #branch_key_id = :branch_key_id");
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> EXPRESSION__ATTRIBUTE__NAMES()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.asString("#status"), dafny.DafnySequence.asString("status")), new dafny.Tuple2(dafny.DafnySequence.asString("#branch_key_id"), dafny.DafnySequence.asString("branch-key-id")));
  }
  public static dafny.DafnySequence<? extends Character> EXPRESSION__ATTRIBUTE__VALUE__STATUS__KEY()
  {
    return dafny.DafnySequence.asString(":status");
  }
  public static dafny.DafnySequence<? extends Character> EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE()
  {
    return dafny.DafnySequence.asString("ACTIVE");
  }
  public static dafny.DafnySequence<? extends Character> EXPRESSION__ATTRIBUTE__VALUE__BRANCH__KEY()
  {
    return dafny.DafnySequence.asString(":branch_key_id");
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsHierarchicalKeyring._default";
  }
}
