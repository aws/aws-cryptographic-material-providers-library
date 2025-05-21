// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.wrapped;

import Wrappers_Compile.Result;
import dafny.DafnySequence;
import dafny.Tuple0;
import dafny.TypeDescriptor;
import java.lang.Byte;
import java.lang.IllegalArgumentException;
import java.lang.RuntimeException;
import java.nio.ByteBuffer;
import java.util.Objects;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.ToDafny;
import software.amazon.cryptography.materialproviders.ToNative;
import software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials;
import software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials;
import software.amazon.cryptography.materialproviders.internaldafny.types.Error;
import software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient;
import software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier;
import software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager;
import software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring;
import software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput;
import software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput;

public class TestMaterialProviders
  implements IAwsCryptographicMaterialProvidersClient {

  private final MaterialProviders _impl;

  protected TestMaterialProviders(BuilderImpl builder) {
    this._impl = builder.impl();
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public Result<IKeyring, Error> CreateAwsKmsDiscoveryKeyring(
    CreateAwsKmsDiscoveryKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsDiscoveryKeyringInput nativeInput =
        ToNative.CreateAwsKmsDiscoveryKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsDiscoveryKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsDiscoveryMultiKeyring(
    CreateAwsKmsDiscoveryMultiKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsDiscoveryMultiKeyringInput nativeInput =
        ToNative.CreateAwsKmsDiscoveryMultiKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsDiscoveryMultiKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsEcdhKeyring(
    CreateAwsKmsEcdhKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsEcdhKeyringInput nativeInput =
        ToNative.CreateAwsKmsEcdhKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsEcdhKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsHierarchicalKeyring(
    CreateAwsKmsHierarchicalKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsHierarchicalKeyringInput nativeInput =
        ToNative.CreateAwsKmsHierarchicalKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsHierarchicalKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsKeyring(
    CreateAwsKmsKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsKeyringInput nativeInput =
        ToNative.CreateAwsKmsKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsMrkDiscoveryKeyring(
    CreateAwsKmsMrkDiscoveryKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsMrkDiscoveryKeyringInput nativeInput =
        ToNative.CreateAwsKmsMrkDiscoveryKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsMrkDiscoveryKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsMrkDiscoveryMultiKeyring(
    CreateAwsKmsMrkDiscoveryMultiKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsMrkDiscoveryMultiKeyringInput nativeInput =
        ToNative.CreateAwsKmsMrkDiscoveryMultiKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsMrkDiscoveryMultiKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsMrkKeyring(
    CreateAwsKmsMrkKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsMrkKeyringInput nativeInput =
        ToNative.CreateAwsKmsMrkKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsMrkKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsMrkMultiKeyring(
    CreateAwsKmsMrkMultiKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsMrkMultiKeyringInput nativeInput =
        ToNative.CreateAwsKmsMrkMultiKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsMrkMultiKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsMultiKeyring(
    CreateAwsKmsMultiKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsMultiKeyringInput nativeInput =
        ToNative.CreateAwsKmsMultiKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsMultiKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateAwsKmsRsaKeyring(
    CreateAwsKmsRsaKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateAwsKmsRsaKeyringInput nativeInput =
        ToNative.CreateAwsKmsRsaKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateAwsKmsRsaKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<
    ICryptographicMaterialsCache,
    Error
  > CreateCryptographicMaterialsCache(
    CreateCryptographicMaterialsCacheInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateCryptographicMaterialsCacheInput nativeInput =
        ToNative.CreateCryptographicMaterialsCacheInput(dafnyInput);
      software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache nativeOutput =
        this._impl.CreateCryptographicMaterialsCache(nativeInput);
      ICryptographicMaterialsCache dafnyOutput =
        ToDafny.CryptographicMaterialsCache(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(ICryptographicMaterialsCache.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(ICryptographicMaterialsCache.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IClientSupplier, Error> CreateDefaultClientSupplier(
    CreateDefaultClientSupplierInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateDefaultClientSupplierInput nativeInput =
        ToNative.CreateDefaultClientSupplierInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IClientSupplier nativeOutput =
        this._impl.CreateDefaultClientSupplier(nativeInput);
      IClientSupplier dafnyOutput = ToDafny.ClientSupplier(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IClientSupplier.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IClientSupplier.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<
    ICryptographicMaterialsManager,
    Error
  > CreateDefaultCryptographicMaterialsManager(
    CreateDefaultCryptographicMaterialsManagerInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateDefaultCryptographicMaterialsManagerInput nativeInput =
        ToNative.CreateDefaultCryptographicMaterialsManagerInput(dafnyInput);
      software.amazon.cryptography.materialproviders.ICryptographicMaterialsManager nativeOutput =
        this._impl.CreateDefaultCryptographicMaterialsManager(nativeInput);
      ICryptographicMaterialsManager dafnyOutput =
        ToDafny.CryptographicMaterialsManager(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(ICryptographicMaterialsManager.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(ICryptographicMaterialsManager.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateMultiKeyring(
    CreateMultiKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateMultiKeyringInput nativeInput =
        ToNative.CreateMultiKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateMultiKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateRawAesKeyring(
    CreateRawAesKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateRawAesKeyringInput nativeInput =
        ToNative.CreateRawAesKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateRawAesKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateRawEcdhKeyring(
    CreateRawEcdhKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateRawEcdhKeyringInput nativeInput =
        ToNative.CreateRawEcdhKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateRawEcdhKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<IKeyring, Error> CreateRawRsaKeyring(
    CreateRawRsaKeyringInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateRawRsaKeyringInput nativeInput =
        ToNative.CreateRawRsaKeyringInput(dafnyInput);
      software.amazon.cryptography.materialproviders.IKeyring nativeOutput =
        this._impl.CreateRawRsaKeyring(nativeInput);
      IKeyring dafnyOutput = ToDafny.Keyring(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(IKeyring.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<
    ICryptographicMaterialsManager,
    Error
  > CreateRequiredEncryptionContextCMM(
    CreateRequiredEncryptionContextCMMInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.CreateRequiredEncryptionContextCMMInput nativeInput =
        ToNative.CreateRequiredEncryptionContextCMMInput(dafnyInput);
      software.amazon.cryptography.materialproviders.ICryptographicMaterialsManager nativeOutput =
        this._impl.CreateRequiredEncryptionContextCMM(nativeInput);
      ICryptographicMaterialsManager dafnyOutput =
        ToDafny.CryptographicMaterialsManager(nativeOutput);
      return Result.create_Success(
        TypeDescriptor.reference(ICryptographicMaterialsManager.class),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        TypeDescriptor.reference(ICryptographicMaterialsManager.class),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> DecryptionMaterialsWithPlaintextDataKey(
    DecryptionMaterials dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.DecryptionMaterials nativeInput =
        ToNative.DecryptionMaterials(dafnyInput);
      this._impl.DecryptionMaterialsWithPlaintextDataKey(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> EncryptionMaterialsHasPlaintextDataKey(
    EncryptionMaterials dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.EncryptionMaterials nativeInput =
        ToNative.EncryptionMaterials(dafnyInput);
      this._impl.EncryptionMaterialsHasPlaintextDataKey(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<AlgorithmSuiteInfo, Error> GetAlgorithmSuiteInfo(
    DafnySequence<? extends Byte> dafnyInput
  ) {
    try {
      ByteBuffer nativeInput =
        software.amazon.smithy.dafny.conversion.ToNative.Simple.ByteBuffer(
          dafnyInput
        );
      software.amazon.cryptography.materialproviders.model.AlgorithmSuiteInfo nativeOutput =
        this._impl.GetAlgorithmSuiteInfo(nativeInput);
      AlgorithmSuiteInfo dafnyOutput = ToDafny.AlgorithmSuiteInfo(nativeOutput);
      return Result.create_Success(
        AlgorithmSuiteInfo._typeDescriptor(),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        AlgorithmSuiteInfo._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<DecryptionMaterials, Error> InitializeDecryptionMaterials(
    InitializeDecryptionMaterialsInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.InitializeDecryptionMaterialsInput nativeInput =
        ToNative.InitializeDecryptionMaterialsInput(dafnyInput);
      software.amazon.cryptography.materialproviders.model.DecryptionMaterials nativeOutput =
        this._impl.InitializeDecryptionMaterials(nativeInput);
      DecryptionMaterials dafnyOutput = ToDafny.DecryptionMaterials(
        nativeOutput
      );
      return Result.create_Success(
        DecryptionMaterials._typeDescriptor(),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        DecryptionMaterials._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<EncryptionMaterials, Error> InitializeEncryptionMaterials(
    InitializeEncryptionMaterialsInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.InitializeEncryptionMaterialsInput nativeInput =
        ToNative.InitializeEncryptionMaterialsInput(dafnyInput);
      software.amazon.cryptography.materialproviders.model.EncryptionMaterials nativeOutput =
        this._impl.InitializeEncryptionMaterials(nativeInput);
      EncryptionMaterials dafnyOutput = ToDafny.EncryptionMaterials(
        nativeOutput
      );
      return Result.create_Success(
        EncryptionMaterials._typeDescriptor(),
        Error._typeDescriptor(),
        dafnyOutput
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        EncryptionMaterials._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> ValidAlgorithmSuiteInfo(
    AlgorithmSuiteInfo dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.AlgorithmSuiteInfo nativeInput =
        ToNative.AlgorithmSuiteInfo(dafnyInput);
      this._impl.ValidAlgorithmSuiteInfo(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> ValidateCommitmentPolicyOnDecrypt(
    ValidateCommitmentPolicyOnDecryptInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.ValidateCommitmentPolicyOnDecryptInput nativeInput =
        ToNative.ValidateCommitmentPolicyOnDecryptInput(dafnyInput);
      this._impl.ValidateCommitmentPolicyOnDecrypt(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> ValidateCommitmentPolicyOnEncrypt(
    ValidateCommitmentPolicyOnEncryptInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.ValidateCommitmentPolicyOnEncryptInput nativeInput =
        ToNative.ValidateCommitmentPolicyOnEncryptInput(dafnyInput);
      this._impl.ValidateCommitmentPolicyOnEncrypt(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> ValidDecryptionMaterialsTransition(
    ValidDecryptionMaterialsTransitionInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.ValidDecryptionMaterialsTransitionInput nativeInput =
        ToNative.ValidDecryptionMaterialsTransitionInput(dafnyInput);
      this._impl.ValidDecryptionMaterialsTransition(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public Result<Tuple0, Error> ValidEncryptionMaterialsTransition(
    ValidEncryptionMaterialsTransitionInput dafnyInput
  ) {
    try {
      software.amazon.cryptography.materialproviders.model.ValidEncryptionMaterialsTransitionInput nativeInput =
        ToNative.ValidEncryptionMaterialsTransitionInput(dafnyInput);
      this._impl.ValidEncryptionMaterialsTransition(nativeInput);
      return Result.create_Success(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        Tuple0.create()
      );
    } catch (RuntimeException ex) {
      return Result.create_Failure(
        dafny.Tuple0._typeDescriptor(),
        Error._typeDescriptor(),
        ToDafny.Error(ex)
      );
    }
  }

  public interface Builder {
    Builder impl(MaterialProviders impl);

    MaterialProviders impl();

    TestMaterialProviders build();
  }

  static class BuilderImpl implements Builder {

    protected MaterialProviders impl;

    protected BuilderImpl() {}

    public Builder impl(MaterialProviders impl) {
      this.impl = impl;
      return this;
    }

    public MaterialProviders impl() {
      return this.impl;
    }

    public TestMaterialProviders build() {
      if (Objects.isNull(this.impl())) {
        throw new IllegalArgumentException(
          "Missing value for required field `impl`"
        );
      }
      return new TestMaterialProviders(this);
    }
  }
}
