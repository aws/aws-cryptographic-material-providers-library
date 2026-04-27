// Class __default
// Dafny class __default compiled into Java
package ErrorMessages_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> IncorrectRawDataKeys(dafny.DafnySequence<? extends Character> datakey, dafny.DafnySequence<? extends Character> keyringName, dafny.DafnySequence<? extends Character> keyProviderId)
  {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("EncryptedDataKey "), datakey), dafny.DafnySequence.asString(" did not match ")), keyringName), dafny.DafnySequence.asString(". ")), dafny.DafnySequence.asString("Expected: keyProviderId: ")), keyProviderId), dafny.DafnySequence.asString(".\n"));
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> IncorrectDataKeys(dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo material, dafny.DafnySequence<? extends Character> errMsg)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = __default.IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      dafny.DafnySequence<? extends Character> _1_expectedValue = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n"), _1_expectedValue));
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> IncorrectDataKeysExpectedValues(dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> encryptedDataKeys, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo material, dafny.DafnySequence<? extends Character> errMsg)
  {
    TAIL_CALL_START: while (true) {
      if ((((long) (encryptedDataKeys).cardinalityInt()) == 0 ? 0 : 1) == 0) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), errMsg);
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _0_encryptedDataKey = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)((encryptedDataKeys).select(0)));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = (UTF8.__default.Decode((_0_encryptedDataKey).dtor_keyProviderId())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
          dafny.DafnySequence<? extends Character> _2_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_2_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_2_e);
        }));
        if ((_1_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          return (_1_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        } else {
          dafny.DafnySequence<? extends Character> _3_extractedKeyProviderId = (_1_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = (UTF8.__default.Decode((_0_encryptedDataKey).dtor_keyProviderInfo())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
            dafny.DafnySequence<? extends Character> _5_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_5_e_boxed0));
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_5_e);
          }));
          if ((_4_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            return (_4_valueOrError1).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
          } else {
            dafny.DafnySequence<? extends Character> _6_extractedKeyProviderInfo = (_4_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
            if (!(_3_extractedKeyProviderId).equals(dafny.DafnySequence.asString("aws-kms-hierarchy"))) {
              dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _in0 = (encryptedDataKeys).drop(1);
              software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _in1 = material;
              dafny.DafnySequence<? extends Character> _in2 = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(errMsg, dafny.DafnySequence.asString("KeyProviderId: ")), _3_extractedKeyProviderId), dafny.DafnySequence.asString(", KeyProviderInfo: ")), _6_extractedKeyProviderInfo), dafny.DafnySequence.asString("\n"));
              encryptedDataKeys = _in0;
              material = _in1;
              errMsg = _in2;
              continue TAIL_CALL_START;
            } else {
              Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = EdkWrapping_Compile.__default.GetProviderWrappedMaterial((_0_encryptedDataKey).dtor_ciphertext(), material);
              if ((_7_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
                return (_7_valueOrError2).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
              } else {
                dafny.DafnySequence<? extends java.lang.Byte> _8_providerWrappedMaterial = (_7_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
                long _9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX = (long) (long) ((__default.SALT__LENGTH()) + (__default.IV__LENGTH()));
                long _10_EDK__CIPHERTEXT__VERSION__INDEX = (long) (long) ((_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX) + (__default.VERSION__LENGTH()));
                Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned(_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX, _10_EDK__CIPHERTEXT__VERSION__INDEX) < 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Wrong branch key version index.")));
                if ((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
                  return (_11_valueOrError3).<dafny.DafnySequence<? extends Character>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                } else {
                  Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (_8_providerWrappedMaterial).cardinalityInt(), _10_EDK__CIPHERTEXT__VERSION__INDEX) >= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Incorrect ciphertext structure.")));
                  if ((_12_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
                    return (_12_valueOrError4).<dafny.DafnySequence<? extends Character>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                  } else {
                    dafny.DafnySequence<? extends java.lang.Byte> _13_branchKeyVersionUuid = (_8_providerWrappedMaterial).subsequence(dafny.Helpers.unsignedToInt(_9_EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX), dafny.Helpers.unsignedToInt(_10_EDK__CIPHERTEXT__VERSION__INDEX));
                    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError5 = (UUID.__default.FromByteArray(_13_branchKeyVersionUuid)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_15_e_boxed0) -> {
                      dafny.DafnySequence<? extends Character> _15_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_15_e_boxed0));
                      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_15_e);
                    }));
                    if ((_14_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
                      return (_14_valueOrError5).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
                    } else {
                      dafny.DafnySequence<? extends Character> _16_branchVersion = (_14_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
                      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _in3 = (encryptedDataKeys).drop(1);
                      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _in4 = material;
                      dafny.DafnySequence<? extends Character> _in5 = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(errMsg, dafny.DafnySequence.asString("KeyProviderId: ")), _3_extractedKeyProviderId), dafny.DafnySequence.asString(", KeyProviderInfo: ")), _6_extractedKeyProviderInfo), dafny.DafnySequence.asString(", BranchKeyVersion: ")), _16_branchVersion), dafny.DafnySequence.asString("\n"));
                      encryptedDataKeys = _in3;
                      material = _in4;
                      errMsg = _in5;
                      continue TAIL_CALL_START;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  public static long SALT__LENGTH()
  {
    return (long) 16L;
  }
  public static long IV__LENGTH()
  {
    return (long) 12L;
  }
  public static long VERSION__LENGTH()
  {
    return (long) 16L;
  }
  public static dafny.DafnySequence<? extends Character> KMS__ECDH__DISCOVERY__ENCRYPT__ERROR()
  {
    return dafny.DafnySequence.asString("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.");
  }
  public static dafny.DafnySequence<? extends Character> RAW__ECDH__DISCOVERY__ENCRYPT__ERROR()
  {
    return dafny.DafnySequence.asString("PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.");
  }
  public static dafny.DafnySequence<? extends Character> RAW__ECDH__EPHEMERAL__DECRYPT__ERROR()
  {
    return dafny.DafnySequence.asString("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.");
  }
  @Override
  public java.lang.String toString() {
    return "ErrorMessages._default";
  }
}
