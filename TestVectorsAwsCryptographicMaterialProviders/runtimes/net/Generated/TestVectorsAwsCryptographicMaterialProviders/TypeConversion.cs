// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.MaterialProviders.Wrapped
{
  public static class TypeConversion
  {
    private const string ISO8601DateFormat = "yyyy-MM-dd\\THH:mm:ss.fff\\Z";

    private const string ISO8601DateFormatNoMS = "yyyy-MM-dd\\THH:mm:ss\\Z";

    public static AWS.Cryptography.MaterialProviders.AesWrappingAlg FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_AesWrappingAlg(software.amazon.cryptography.materialproviders.internaldafny.types._IAesWrappingAlg value)
    {
      if (value.is_ALG__AES128__GCM__IV12__TAG16) return AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16;
      if (value.is_ALG__AES192__GCM__IV12__TAG16) return AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES192_GCM_IV12_TAG16;
      if (value.is_ALG__AES256__GCM__IV12__TAG16) return AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.AesWrappingAlg value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAesWrappingAlg ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_AesWrappingAlg(AWS.Cryptography.MaterialProviders.AesWrappingAlg value)
    {
      if (AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES128__GCM__IV12__TAG16();
      if (AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES192_GCM_IV12_TAG16.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES192__GCM__IV12__TAG16();
      if (AWS.Cryptography.MaterialProviders.AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg.create_ALG__AES256__GCM__IV12__TAG16();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.AesWrappingAlg value");
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId)value;
      var converted = new AWS.Cryptography.MaterialProviders.AlgorithmSuiteId(); if (value.is_ESDK)
      {
        converted.ESDK = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M4_ESDK(concrete.dtor_ESDK);
        return converted;
      }
      if (value.is_DBE)
      {
        converted.DBE = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M3_DBE(concrete.dtor_DBE);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.AlgorithmSuiteId state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      value.Validate(); if (value.IsSetESDK())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M4_ESDK(value.ESDK));
      }
      if (value.IsSetDBE())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M3_DBE(value.DBE));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.AlgorithmSuiteId state");
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)value; AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo converted = new AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo(); converted.Id = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M2_id(concrete._id);
      converted.BinaryId = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M8_binaryId(concrete._binaryId);
      converted.MessageVersion = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M14_messageVersion(concrete._messageVersion);
      converted.Encrypt = (AWS.Cryptography.MaterialProviders.Encrypt)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M7_encrypt(concrete._encrypt);
      converted.Kdf = (AWS.Cryptography.MaterialProviders.DerivationAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M3_kdf(concrete._kdf);
      converted.Commitment = (AWS.Cryptography.MaterialProviders.DerivationAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M10_commitment(concrete._commitment);
      converted.Signature = (AWS.Cryptography.MaterialProviders.SignatureAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M9_signature(concrete._signature);
      converted.SymmetricSignature = (AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M18_symmetricSignature(concrete._symmetricSignature);
      converted.EdkWrapping = (AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M11_edkWrapping(concrete._edkWrapping); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M2_id(value.Id), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M8_binaryId(value.BinaryId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M14_messageVersion(value.MessageVersion), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M7_encrypt(value.Encrypt), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M3_kdf(value.Kdf), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M10_commitment(value.Commitment), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M9_signature(value.Signature), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M18_symmetricSignature(value.SymmetricSignature), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M11_edkWrapping(value.EdkWrapping));
    }
    public static AWS.Cryptography.MaterialProviders.AwsCryptographicMaterialProvidersException FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException(software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException value)
    {
      return new AWS.Cryptography.MaterialProviders.AwsCryptographicMaterialProvidersException(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException(AWS.Cryptography.MaterialProviders.AwsCryptographicMaterialProvidersException value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.CacheType FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType(software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CacheType concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CacheType)value;
      var converted = new AWS.Cryptography.MaterialProviders.CacheType(); if (value.is_Default)
      {
        converted.Default = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M7_Default(concrete.dtor_Default);
        return converted;
      }
      if (value.is_No)
      {
        converted.No = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M2_No(concrete.dtor_No);
        return converted;
      }
      if (value.is_SingleThreaded)
      {
        converted.SingleThreaded = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M14_SingleThreaded(concrete.dtor_SingleThreaded);
        return converted;
      }
      if (value.is_MultiThreaded)
      {
        converted.MultiThreaded = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_MultiThreaded(concrete.dtor_MultiThreaded);
        return converted;
      }
      if (value.is_StormTracking)
      {
        converted.StormTracking = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_StormTracking(concrete.dtor_StormTracking);
        return converted;
      }
      if (value.is_Shared)
      {
        converted.Shared = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M6_Shared(concrete.dtor_Shared);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.CacheType state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType(AWS.Cryptography.MaterialProviders.CacheType value)
    {
      value.Validate(); if (value.IsSetDefault())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M7_Default(value.Default));
      }
      if (value.IsSetNo())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_No(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M2_No(value.No));
      }
      if (value.IsSetSingleThreaded())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_SingleThreaded(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M14_SingleThreaded(value.SingleThreaded));
      }
      if (value.IsSetMultiThreaded())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_MultiThreaded(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_MultiThreaded(value.MultiThreaded));
      }
      if (value.IsSetStormTracking())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_StormTracking(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_StormTracking(value.StormTracking));
      }
      if (value.IsSetShared())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Shared(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M6_Shared(value.Shared));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.CacheType state");
    }
    public static AWS.Cryptography.MaterialProviders.CommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)value;
      var converted = new AWS.Cryptography.MaterialProviders.CommitmentPolicy(); if (value.is_ESDK)
      {
        converted.ESDK = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M4_ESDK(concrete.dtor_ESDK);
        return converted;
      }
      if (value.is_DBE)
      {
        converted.DBE = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M3_DBE(concrete.dtor_DBE);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.CommitmentPolicy state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(AWS.Cryptography.MaterialProviders.CommitmentPolicy value)
    {
      value.Validate(); if (value.IsSetESDK())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_ESDK(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M4_ESDK(value.ESDK));
      }
      if (value.IsSetDBE())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy.create_DBE(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M3_DBE(value.DBE));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.CommitmentPolicy state");
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsDiscoveryKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryKeyringInput(); converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._discoveryFilter.is_Some) converted.DiscoveryFilter = (AWS.Cryptography.MaterialProviders.DiscoveryFilter)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M15_discoveryFilter(concrete._discoveryFilter);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsDiscoveryKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryKeyringInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.DiscoveryFilter var_discoveryFilter = value.IsSetDiscoveryFilter() ? value.DiscoveryFilter : (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M9_kmsClient(value.KmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M15_discoveryFilter(var_discoveryFilter), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryMultiKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsDiscoveryMultiKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryMultiKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryMultiKeyringInput(); converted.Regions = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M7_regions(concrete._regions);
      if (concrete._discoveryFilter.is_Some) converted.DiscoveryFilter = (AWS.Cryptography.MaterialProviders.DiscoveryFilter)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M15_discoveryFilter(concrete._discoveryFilter);
      if (concrete._clientSupplier.is_Some) converted.ClientSupplier = (AWS.Cryptography.MaterialProviders.IClientSupplier)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M14_clientSupplier(concrete._clientSupplier);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsDiscoveryMultiKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsDiscoveryMultiKeyringInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.DiscoveryFilter var_discoveryFilter = value.IsSetDiscoveryFilter() ? value.DiscoveryFilter : (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null;
      AWS.Cryptography.MaterialProviders.IClientSupplier var_clientSupplier = value.IsSetClientSupplier() ? value.ClientSupplier : (AWS.Cryptography.MaterialProviders.IClientSupplier)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M7_regions(value.Regions), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M15_discoveryFilter(var_discoveryFilter), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M14_clientSupplier(var_clientSupplier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsEcdhKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsEcdhKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsEcdhKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsEcdhKeyringInput(); converted.KeyAgreementScheme = (AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M18_KeyAgreementScheme(concrete._KeyAgreementScheme);
      converted.CurveSpec = (AWS.Cryptography.Primitives.ECDHCurveSpec)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_curveSpec(concrete._curveSpec);
      converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsEcdhKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsEcdhKeyringInput value)
    {
      value.Validate();
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M18_KeyAgreementScheme(value.KeyAgreementScheme), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_curveSpec(value.CurveSpec), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_kmsClient(value.KmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsHierarchicalKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsHierarchicalKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsHierarchicalKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsHierarchicalKeyringInput(); if (concrete._branchKeyId.is_Some) converted.BranchKeyId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_branchKeyId(concrete._branchKeyId);
      if (concrete._branchKeyIdSupplier.is_Some) converted.BranchKeyIdSupplier = (AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M19_branchKeyIdSupplier(concrete._branchKeyIdSupplier);
      converted.KeyStore = (AWS.Cryptography.KeyStore.KeyStore)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M8_keyStore(concrete._keyStore);
      converted.TtlSeconds = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M10_ttlSeconds(concrete._ttlSeconds);
      if (concrete._cache.is_Some) converted.Cache = (AWS.Cryptography.MaterialProviders.CacheType)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M5_cache(concrete._cache);
      if (concrete._partitionId.is_Some) converted.PartitionId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_partitionId(concrete._partitionId); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsHierarchicalKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsHierarchicalKeyringInput value)
    {
      value.Validate();
      string var_branchKeyId = value.IsSetBranchKeyId() ? value.BranchKeyId : (string)null;
      AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier var_branchKeyIdSupplier = value.IsSetBranchKeyIdSupplier() ? value.BranchKeyIdSupplier : (AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier)null;
      AWS.Cryptography.MaterialProviders.CacheType var_cache = value.IsSetCache() ? value.Cache : (AWS.Cryptography.MaterialProviders.CacheType)null;
      string var_partitionId = value.IsSetPartitionId() ? value.PartitionId : (string)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_branchKeyId(var_branchKeyId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M19_branchKeyIdSupplier(var_branchKeyIdSupplier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M8_keyStore(value.KeyStore), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M10_ttlSeconds(value.TtlSeconds), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M5_cache(var_cache), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_partitionId(var_partitionId));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsKeyringInput(); converted.KmsKeyId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M8_kmsKeyId(concrete._kmsKeyId);
      converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsKeyringInput value)
    {
      value.Validate();
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M8_kmsKeyId(value.KmsKeyId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M9_kmsClient(value.KmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkDiscoveryKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryKeyringInput(); converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._discoveryFilter.is_Some) converted.DiscoveryFilter = (AWS.Cryptography.MaterialProviders.DiscoveryFilter)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M15_discoveryFilter(concrete._discoveryFilter);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M11_grantTokens(concrete._grantTokens);
      converted.Region = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M6_region(concrete._region); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkDiscoveryKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryKeyringInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.DiscoveryFilter var_discoveryFilter = value.IsSetDiscoveryFilter() ? value.DiscoveryFilter : (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M9_kmsClient(value.KmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M15_discoveryFilter(var_discoveryFilter), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M11_grantTokens(var_grantTokens), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M6_region(value.Region));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryMultiKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkDiscoveryMultiKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryMultiKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryMultiKeyringInput(); converted.Regions = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M7_regions(concrete._regions);
      if (concrete._discoveryFilter.is_Some) converted.DiscoveryFilter = (AWS.Cryptography.MaterialProviders.DiscoveryFilter)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M15_discoveryFilter(concrete._discoveryFilter);
      if (concrete._clientSupplier.is_Some) converted.ClientSupplier = (AWS.Cryptography.MaterialProviders.IClientSupplier)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M14_clientSupplier(concrete._clientSupplier);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkDiscoveryMultiKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkDiscoveryMultiKeyringInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.DiscoveryFilter var_discoveryFilter = value.IsSetDiscoveryFilter() ? value.DiscoveryFilter : (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null;
      AWS.Cryptography.MaterialProviders.IClientSupplier var_clientSupplier = value.IsSetClientSupplier() ? value.ClientSupplier : (AWS.Cryptography.MaterialProviders.IClientSupplier)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M7_regions(value.Regions), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M15_discoveryFilter(var_discoveryFilter), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M14_clientSupplier(var_clientSupplier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkKeyringInput(); converted.KmsKeyId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M8_kmsKeyId(concrete._kmsKeyId);
      converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkKeyringInput value)
    {
      value.Validate();
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M8_kmsKeyId(value.KmsKeyId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M9_kmsClient(value.KmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkMultiKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkMultiKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkMultiKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkMultiKeyringInput(); if (concrete._generator.is_Some) converted.Generator = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_generator(concrete._generator);
      if (concrete._kmsKeyIds.is_Some) converted.KmsKeyIds = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_kmsKeyIds(concrete._kmsKeyIds);
      if (concrete._clientSupplier.is_Some) converted.ClientSupplier = (AWS.Cryptography.MaterialProviders.IClientSupplier)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M14_clientSupplier(concrete._clientSupplier);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMrkMultiKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsMrkMultiKeyringInput value)
    {
      value.Validate();
      string var_generator = value.IsSetGenerator() ? value.Generator : (string)null;
      System.Collections.Generic.List<string> var_kmsKeyIds = value.IsSetKmsKeyIds() ? value.KmsKeyIds : (System.Collections.Generic.List<string>)null;
      AWS.Cryptography.MaterialProviders.IClientSupplier var_clientSupplier = value.IsSetClientSupplier() ? value.ClientSupplier : (AWS.Cryptography.MaterialProviders.IClientSupplier)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_generator(var_generator), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_kmsKeyIds(var_kmsKeyIds), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M14_clientSupplier(var_clientSupplier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsMultiKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMultiKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsMultiKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsMultiKeyringInput(); if (concrete._generator.is_Some) converted.Generator = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_generator(concrete._generator);
      if (concrete._kmsKeyIds.is_Some) converted.KmsKeyIds = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_kmsKeyIds(concrete._kmsKeyIds);
      if (concrete._clientSupplier.is_Some) converted.ClientSupplier = (AWS.Cryptography.MaterialProviders.IClientSupplier)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M14_clientSupplier(concrete._clientSupplier);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsMultiKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsMultiKeyringInput value)
    {
      value.Validate();
      string var_generator = value.IsSetGenerator() ? value.Generator : (string)null;
      System.Collections.Generic.List<string> var_kmsKeyIds = value.IsSetKmsKeyIds() ? value.KmsKeyIds : (System.Collections.Generic.List<string>)null;
      AWS.Cryptography.MaterialProviders.IClientSupplier var_clientSupplier = value.IsSetClientSupplier() ? value.ClientSupplier : (AWS.Cryptography.MaterialProviders.IClientSupplier)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_generator(var_generator), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_kmsKeyIds(var_kmsKeyIds), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M14_clientSupplier(var_clientSupplier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateAwsKmsRsaKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsRsaKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateAwsKmsRsaKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateAwsKmsRsaKeyringInput(); if (concrete._publicKey.is_Some) converted.PublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_publicKey(concrete._publicKey);
      converted.KmsKeyId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M8_kmsKeyId(concrete._kmsKeyId);
      converted.EncryptionAlgorithm = (Amazon.KeyManagementService.EncryptionAlgorithmSpec)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M19_encryptionAlgorithm(concrete._encryptionAlgorithm);
      if (concrete._kmsClient.is_Some) converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_kmsClient(concrete._kmsClient);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M11_grantTokens(concrete._grantTokens); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateAwsKmsRsaKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput(AWS.Cryptography.MaterialProviders.CreateAwsKmsRsaKeyringInput value)
    {
      value.Validate();
      System.IO.MemoryStream var_publicKey = value.IsSetPublicKey() ? value.PublicKey : (System.IO.MemoryStream)null;
      Amazon.KeyManagementService.IAmazonKeyManagementService var_kmsClient = value.IsSetKmsClient() ? value.KmsClient : (Amazon.KeyManagementService.IAmazonKeyManagementService)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_publicKey(var_publicKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M8_kmsKeyId(value.KmsKeyId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M19_encryptionAlgorithm(value.EncryptionAlgorithm), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_kmsClient(var_kmsClient), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M11_grantTokens(var_grantTokens));
    }
    public static AWS.Cryptography.MaterialProviders.CreateCryptographicMaterialsCacheInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateCryptographicMaterialsCacheInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput)value; AWS.Cryptography.MaterialProviders.CreateCryptographicMaterialsCacheInput converted = new AWS.Cryptography.MaterialProviders.CreateCryptographicMaterialsCacheInput(); converted.Cache = (AWS.Cryptography.MaterialProviders.CacheType)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput__M5_cache(concrete._cache); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateCryptographicMaterialsCacheInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput(AWS.Cryptography.MaterialProviders.CreateCryptographicMaterialsCacheInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput__M5_cache(value.Cache));
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput__M14_materialsCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput__M14_materialsCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput__M16_materialsManager(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput__M16_materialsManager(value);
    }
    public static AWS.Cryptography.MaterialProviders.CreateDefaultClientSupplierInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateDefaultClientSupplierInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateDefaultClientSupplierInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput)value; AWS.Cryptography.MaterialProviders.CreateDefaultClientSupplierInput converted = new AWS.Cryptography.MaterialProviders.CreateDefaultClientSupplierInput(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateDefaultClientSupplierInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateDefaultClientSupplierInput(AWS.Cryptography.MaterialProviders.CreateDefaultClientSupplierInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput();
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput__M6_client(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput__M6_client(value);
    }
    public static AWS.Cryptography.MaterialProviders.CreateDefaultCryptographicMaterialsManagerInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateDefaultCryptographicMaterialsManagerInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput)value; AWS.Cryptography.MaterialProviders.CreateDefaultCryptographicMaterialsManagerInput converted = new AWS.Cryptography.MaterialProviders.CreateDefaultCryptographicMaterialsManagerInput(); converted.Keyring = (AWS.Cryptography.MaterialProviders.IKeyring)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput__M7_keyring(concrete._keyring); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateDefaultCryptographicMaterialsManagerInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput(AWS.Cryptography.MaterialProviders.CreateDefaultCryptographicMaterialsManagerInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput__M7_keyring(value.Keyring));
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(value);
    }
    public static AWS.Cryptography.MaterialProviders.CreateMultiKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateMultiKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateMultiKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateMultiKeyringInput(); if (concrete._generator.is_Some) converted.Generator = (AWS.Cryptography.MaterialProviders.IKeyring)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M9_generator(concrete._generator);
      converted.ChildKeyrings = (System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M13_childKeyrings(concrete._childKeyrings); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateMultiKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput(AWS.Cryptography.MaterialProviders.CreateMultiKeyringInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.IKeyring var_generator = value.IsSetGenerator() ? value.Generator : (AWS.Cryptography.MaterialProviders.IKeyring)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M9_generator(var_generator), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M13_childKeyrings(value.ChildKeyrings));
    }
    public static AWS.Cryptography.MaterialProviders.CreateRawAesKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawAesKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateRawAesKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateRawAesKeyringInput(); converted.KeyNamespace = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M12_keyNamespace(concrete._keyNamespace);
      converted.KeyName = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M7_keyName(concrete._keyName);
      converted.WrappingKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingKey(concrete._wrappingKey);
      converted.WrappingAlg = (AWS.Cryptography.MaterialProviders.AesWrappingAlg)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingAlg(concrete._wrappingAlg); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawAesKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput(AWS.Cryptography.MaterialProviders.CreateRawAesKeyringInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M12_keyNamespace(value.KeyNamespace), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M7_keyName(value.KeyName), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingKey(value.WrappingKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingAlg(value.WrappingAlg));
    }
    public static AWS.Cryptography.MaterialProviders.CreateRawEcdhKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawEcdhKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateRawEcdhKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateRawEcdhKeyringInput(); converted.KeyAgreementScheme = (AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M18_KeyAgreementScheme(concrete._KeyAgreementScheme);
      converted.CurveSpec = (AWS.Cryptography.Primitives.ECDHCurveSpec)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M9_curveSpec(concrete._curveSpec); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawEcdhKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput(AWS.Cryptography.MaterialProviders.CreateRawEcdhKeyringInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M18_KeyAgreementScheme(value.KeyAgreementScheme), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M9_curveSpec(value.CurveSpec));
    }
    public static AWS.Cryptography.MaterialProviders.CreateRawRsaKeyringInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawRsaKeyringInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput)value; AWS.Cryptography.MaterialProviders.CreateRawRsaKeyringInput converted = new AWS.Cryptography.MaterialProviders.CreateRawRsaKeyringInput(); converted.KeyNamespace = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M12_keyNamespace(concrete._keyNamespace);
      converted.KeyName = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M7_keyName(concrete._keyName);
      converted.PaddingScheme = (AWS.Cryptography.MaterialProviders.PaddingScheme)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M13_paddingScheme(concrete._paddingScheme);
      if (concrete._publicKey.is_Some) converted.PublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M9_publicKey(concrete._publicKey);
      if (concrete._privateKey.is_Some) converted.PrivateKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M10_privateKey(concrete._privateKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRawRsaKeyringInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput(AWS.Cryptography.MaterialProviders.CreateRawRsaKeyringInput value)
    {
      value.Validate();
      System.IO.MemoryStream var_publicKey = value.IsSetPublicKey() ? value.PublicKey : (System.IO.MemoryStream)null;
      System.IO.MemoryStream var_privateKey = value.IsSetPrivateKey() ? value.PrivateKey : (System.IO.MemoryStream)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M12_keyNamespace(value.KeyNamespace), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M7_keyName(value.KeyName), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M13_paddingScheme(value.PaddingScheme), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M9_publicKey(var_publicKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M10_privateKey(var_privateKey));
    }
    public static AWS.Cryptography.MaterialProviders.CreateRequiredEncryptionContextCMMInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput(software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRequiredEncryptionContextCMMInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput)value; AWS.Cryptography.MaterialProviders.CreateRequiredEncryptionContextCMMInput converted = new AWS.Cryptography.MaterialProviders.CreateRequiredEncryptionContextCMMInput(); if (concrete._underlyingCMM.is_Some) converted.UnderlyingCMM = (AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M13_underlyingCMM(concrete._underlyingCMM);
      if (concrete._keyring.is_Some) converted.Keyring = (AWS.Cryptography.MaterialProviders.IKeyring)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M7_keyring(concrete._keyring);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICreateRequiredEncryptionContextCMMInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput(AWS.Cryptography.MaterialProviders.CreateRequiredEncryptionContextCMMInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager var_underlyingCMM = value.IsSetUnderlyingCMM() ? value.UnderlyingCMM : (AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager)null;
      AWS.Cryptography.MaterialProviders.IKeyring var_keyring = value.IsSetKeyring() ? value.Keyring : (AWS.Cryptography.MaterialProviders.IKeyring)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M13_underlyingCMM(var_underlyingCMM), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M7_keyring(var_keyring), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys));
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput__M16_materialsManager(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput__M16_materialsManager(value);
    }
    public static AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBEAlgorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IDBEAlgorithmSuiteId value)
    {
      if (value.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384) return AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384;
      if (value.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384) return AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384_SYMSIG_HMAC_SHA384;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDBEAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBEAlgorithmSuiteId(AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId value)
    {
      if (AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384();
      if (AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384_SYMSIG_HMAC_SHA384.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId value");
    }
    public static AWS.Cryptography.MaterialProviders.DBECommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBECommitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._IDBECommitmentPolicy value)
    {
      if (value.is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT) return AWS.Cryptography.MaterialProviders.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DBECommitmentPolicy value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDBECommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBECommitmentPolicy(AWS.Cryptography.MaterialProviders.DBECommitmentPolicy value)
    {
      if (AWS.Cryptography.MaterialProviders.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.DBECommitmentPolicy.create();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DBECommitmentPolicy value");
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)value; AWS.Cryptography.MaterialProviders.DecryptionMaterials converted = new AWS.Cryptography.MaterialProviders.DecryptionMaterials(); converted.AlgorithmSuite = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M14_algorithmSuite(concrete._algorithmSuite);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M17_encryptionContext(concrete._encryptionContext);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys);
      if (concrete._plaintextDataKey.is_Some) converted.PlaintextDataKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M16_plaintextDataKey(concrete._plaintextDataKey);
      if (concrete._verificationKey.is_Some) converted.VerificationKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M15_verificationKey(concrete._verificationKey);
      if (concrete._symmetricSigningKey.is_Some) converted.SymmetricSigningKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M19_symmetricSigningKey(concrete._symmetricSigningKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      value.Validate();
      System.IO.MemoryStream var_plaintextDataKey = value.IsSetPlaintextDataKey() ? value.PlaintextDataKey : (System.IO.MemoryStream)null;
      System.IO.MemoryStream var_verificationKey = value.IsSetVerificationKey() ? value.VerificationKey : (System.IO.MemoryStream)null;
      System.IO.MemoryStream var_symmetricSigningKey = value.IsSetSymmetricSigningKey() ? value.SymmetricSigningKey : (System.IO.MemoryStream)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M14_algorithmSuite(value.AlgorithmSuite), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M16_plaintextDataKey(var_plaintextDataKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M15_verificationKey(var_verificationKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M19_symmetricSigningKey(var_symmetricSigningKey));
    }
    public static AWS.Cryptography.MaterialProviders.DecryptMaterialsInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptMaterialsInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput)value; AWS.Cryptography.MaterialProviders.DecryptMaterialsInput converted = new AWS.Cryptography.MaterialProviders.DecryptMaterialsInput(); converted.AlgorithmSuiteId = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_algorithmSuiteId(concrete._algorithmSuiteId);
      converted.CommitmentPolicy = (AWS.Cryptography.MaterialProviders.CommitmentPolicy)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_commitmentPolicy(concrete._commitmentPolicy);
      converted.EncryptedDataKeys = (System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptedDataKeys(concrete._encryptedDataKeys);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptionContext(concrete._encryptionContext);
      if (concrete._reproducedEncryptionContext.is_Some) converted.ReproducedEncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M27_reproducedEncryptionContext(concrete._reproducedEncryptionContext); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptMaterialsInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput(AWS.Cryptography.MaterialProviders.DecryptMaterialsInput value)
    {
      value.Validate();
      System.Collections.Generic.Dictionary<string, string> var_reproducedEncryptionContext = value.IsSetReproducedEncryptionContext() ? value.ReproducedEncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_algorithmSuiteId(value.AlgorithmSuiteId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_commitmentPolicy(value.CommitmentPolicy), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptedDataKeys(value.EncryptedDataKeys), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M27_reproducedEncryptionContext(var_reproducedEncryptionContext));
    }
    public static AWS.Cryptography.MaterialProviders.DecryptMaterialsOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptMaterialsOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput)value; AWS.Cryptography.MaterialProviders.DecryptMaterialsOutput converted = new AWS.Cryptography.MaterialProviders.DecryptMaterialsOutput(); converted.DecryptionMaterials = (AWS.Cryptography.MaterialProviders.DecryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput__M19_decryptionMaterials(concrete._decryptionMaterials); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptMaterialsOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput(AWS.Cryptography.MaterialProviders.DecryptMaterialsOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput__M19_decryptionMaterials(value.DecryptionMaterials));
    }
    public static AWS.Cryptography.MaterialProviders.DeleteCacheEntryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput(software.amazon.cryptography.materialproviders.internaldafny.types._IDeleteCacheEntryInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput)value; AWS.Cryptography.MaterialProviders.DeleteCacheEntryInput converted = new AWS.Cryptography.MaterialProviders.DeleteCacheEntryInput(); converted.Identifier = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput__M10_identifier(concrete._identifier); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDeleteCacheEntryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput(AWS.Cryptography.MaterialProviders.DeleteCacheEntryInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput__M10_identifier(value.Identifier));
    }
    public static AWS.Cryptography.MaterialProviders.DerivationAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm)value;
      var converted = new AWS.Cryptography.MaterialProviders.DerivationAlgorithm(); if (value.is_HKDF)
      {
        converted.HKDF = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_HKDF(concrete.dtor_HKDF);
        return converted;
      }
      if (value.is_IDENTITY)
      {
        converted.IDENTITY = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M8_IDENTITY(concrete.dtor_IDENTITY);
        return converted;
      }
      if (value.is_None)
      {
        converted.None = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_None(concrete.dtor_None);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DerivationAlgorithm state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(AWS.Cryptography.MaterialProviders.DerivationAlgorithm value)
    {
      value.Validate(); if (value.IsSetHKDF())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_HKDF(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_HKDF(value.HKDF));
      }
      if (value.IsSetIDENTITY())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_IDENTITY(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M8_IDENTITY(value.IDENTITY));
      }
      if (value.IsSetNone())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_None(value.None));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.DerivationAlgorithm state");
    }
    public static AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm(software.amazon.cryptography.materialproviders.internaldafny.types._IEdkWrappingAlgorithm value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm)value;
      var converted = new AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm(); if (value.is_DIRECT__KEY__WRAPPING)
      {
        converted.DIRECT__KEY__WRAPPING = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M19_DIRECT_KEY_WRAPPING(concrete.dtor_DIRECT__KEY__WRAPPING);
        return converted;
      }
      if (value.is_IntermediateKeyWrapping)
      {
        converted.IntermediateKeyWrapping = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M23_IntermediateKeyWrapping(concrete.dtor_IntermediateKeyWrapping);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEdkWrappingAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm(AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm value)
    {
      value.Validate(); if (value.IsSetDIRECT__KEY__WRAPPING())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M19_DIRECT_KEY_WRAPPING(value.DIRECT__KEY__WRAPPING));
      }
      if (value.IsSetIntermediateKeyWrapping())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_IntermediateKeyWrapping(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M23_IntermediateKeyWrapping(value.IntermediateKeyWrapping));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm state");
    }
    public static AWS.Cryptography.MaterialProviders.Encrypt FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt)value;
      var converted = new AWS.Cryptography.MaterialProviders.Encrypt(); if (value.is_AES__GCM)
      {
        converted.AES__GCM = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt__M7_AES_GCM(concrete.dtor_AES__GCM);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.Encrypt state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(AWS.Cryptography.MaterialProviders.Encrypt value)
    {
      value.Validate(); if (value.IsSetAES__GCM())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt.create(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt__M7_AES_GCM(value.AES__GCM));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.Encrypt state");
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)value; AWS.Cryptography.MaterialProviders.EncryptionMaterials converted = new AWS.Cryptography.MaterialProviders.EncryptionMaterials(); converted.AlgorithmSuite = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M14_algorithmSuite(concrete._algorithmSuite);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptionContext(concrete._encryptionContext);
      converted.EncryptedDataKeys = (System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptedDataKeys(concrete._encryptedDataKeys);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys);
      if (concrete._plaintextDataKey.is_Some) converted.PlaintextDataKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M16_plaintextDataKey(concrete._plaintextDataKey);
      if (concrete._signingKey.is_Some) converted.SigningKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M10_signingKey(concrete._signingKey);
      if (concrete._symmetricSigningKeys.is_Some) converted.SymmetricSigningKeys = (System.Collections.Generic.List<System.IO.MemoryStream>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M20_symmetricSigningKeys(concrete._symmetricSigningKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      value.Validate();
      System.IO.MemoryStream var_plaintextDataKey = value.IsSetPlaintextDataKey() ? value.PlaintextDataKey : (System.IO.MemoryStream)null;
      System.IO.MemoryStream var_signingKey = value.IsSetSigningKey() ? value.SigningKey : (System.IO.MemoryStream)null;
      System.Collections.Generic.List<System.IO.MemoryStream> var_symmetricSigningKeys = value.IsSetSymmetricSigningKeys() ? value.SymmetricSigningKeys : (System.Collections.Generic.List<System.IO.MemoryStream>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M14_algorithmSuite(value.AlgorithmSuite), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptedDataKeys(value.EncryptedDataKeys), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M16_plaintextDataKey(var_plaintextDataKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M10_signingKey(var_signingKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M20_symmetricSigningKeys(var_symmetricSigningKeys));
    }
    public static AWS.Cryptography.MaterialProviders.EntryAlreadyExists FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists(software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryAlreadyExists value)
    {
      return new AWS.Cryptography.MaterialProviders.EntryAlreadyExists(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryAlreadyExists ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists(AWS.Cryptography.MaterialProviders.EntryAlreadyExists value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryAlreadyExists(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.EntryDoesNotExist FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist(software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist value)
    {
      return new AWS.Cryptography.MaterialProviders.EntryDoesNotExist(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist(AWS.Cryptography.MaterialProviders.EntryDoesNotExist value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKAlgorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IESDKAlgorithmSuiteId value)
    {
      if (value.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_NO_KDF;
      if (value.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_NO_KDF;
      if (value.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF;
      if (value.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256;
      if (value.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256;
      if (value.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256;
      if (value.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256;
      if (value.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384;
      if (value.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384;
      if (value.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY;
      if (value.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384) return AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IESDKAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKAlgorithmSuiteId(AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId value)
    {
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_NO_KDF.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_NO_KDF.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY();
      if (AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId value");
    }
    public static AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKCommitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._IESDKCommitmentPolicy value)
    {
      if (value.is_FORBID__ENCRYPT__ALLOW__DECRYPT) return AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT;
      if (value.is_REQUIRE__ENCRYPT__ALLOW__DECRYPT) return AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT;
      if (value.is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT) return AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IESDKCommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKCommitmentPolicy(AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy value)
    {
      if (AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_FORBID__ENCRYPT__ALLOW__DECRYPT();
      if (AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__ALLOW__DECRYPT();
      if (AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.ESDKCommitmentPolicy.create_REQUIRE__ENCRYPT__REQUIRE__DECRYPT();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy value");
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput__M8_binaryId(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput(System.IO.MemoryStream value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput__M8_binaryId(value);
    }
    public static AWS.Cryptography.MaterialProviders.GetBranchKeyIdInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetBranchKeyIdInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput)value; AWS.Cryptography.MaterialProviders.GetBranchKeyIdInput converted = new AWS.Cryptography.MaterialProviders.GetBranchKeyIdInput(); converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput__M17_encryptionContext(concrete._encryptionContext); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetBranchKeyIdInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput(AWS.Cryptography.MaterialProviders.GetBranchKeyIdInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput__M17_encryptionContext(value.EncryptionContext));
    }
    public static AWS.Cryptography.MaterialProviders.GetBranchKeyIdOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetBranchKeyIdOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput)value; AWS.Cryptography.MaterialProviders.GetBranchKeyIdOutput converted = new AWS.Cryptography.MaterialProviders.GetBranchKeyIdOutput(); converted.BranchKeyId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput__M11_branchKeyId(concrete._branchKeyId); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetBranchKeyIdOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput(AWS.Cryptography.MaterialProviders.GetBranchKeyIdOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetBranchKeyIdOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput__M11_branchKeyId(value.BranchKeyId));
    }
    public static AWS.Cryptography.MaterialProviders.GetCacheEntryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetCacheEntryInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput)value; AWS.Cryptography.MaterialProviders.GetCacheEntryInput converted = new AWS.Cryptography.MaterialProviders.GetCacheEntryInput(); converted.Identifier = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M10_identifier(concrete._identifier);
      if (concrete._bytesUsed.is_Some) converted.BytesUsed = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M9_bytesUsed(concrete._bytesUsed); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetCacheEntryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput(AWS.Cryptography.MaterialProviders.GetCacheEntryInput value)
    {
      value.Validate();
      long? var_bytesUsed = value.IsSetBytesUsed() ? value.BytesUsed : (long?)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M10_identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M9_bytesUsed(var_bytesUsed));
    }
    public static AWS.Cryptography.MaterialProviders.GetCacheEntryOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetCacheEntryOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput)value; AWS.Cryptography.MaterialProviders.GetCacheEntryOutput converted = new AWS.Cryptography.MaterialProviders.GetCacheEntryOutput(); converted.Materials = (AWS.Cryptography.MaterialProviders.Materials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_materials(concrete._materials);
      converted.CreationTime = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_creationTime(concrete._creationTime);
      converted.ExpiryTime = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M10_expiryTime(concrete._expiryTime);
      converted.MessagesUsed = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_messagesUsed(concrete._messagesUsed);
      converted.BytesUsed = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_bytesUsed(concrete._bytesUsed); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetCacheEntryOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput(AWS.Cryptography.MaterialProviders.GetCacheEntryOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_materials(value.Materials), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_creationTime(value.CreationTime), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M10_expiryTime(value.ExpiryTime), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_messagesUsed(value.MessagesUsed), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_bytesUsed(value.BytesUsed));
    }
    public static AWS.Cryptography.MaterialProviders.GetClientInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetClientInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput)value; AWS.Cryptography.MaterialProviders.GetClientInput converted = new AWS.Cryptography.MaterialProviders.GetClientInput(); converted.Region = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput__M6_region(concrete._region); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetClientInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput(AWS.Cryptography.MaterialProviders.GetClientInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput__M6_region(value.Region));
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput__M6_client(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput__M6_client(value);
    }
    public static AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetEncryptionMaterialsInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)value; AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsInput converted = new AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsInput(); converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M17_encryptionContext(concrete._encryptionContext);
      converted.CommitmentPolicy = (AWS.Cryptography.MaterialProviders.CommitmentPolicy)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_commitmentPolicy(concrete._commitmentPolicy);
      if (concrete._algorithmSuiteId.is_Some) converted.AlgorithmSuiteId = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_algorithmSuiteId(concrete._algorithmSuiteId);
      if (concrete._maxPlaintextLength.is_Some) converted.MaxPlaintextLength = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M18_maxPlaintextLength(concrete._maxPlaintextLength);
      if (concrete._requiredEncryptionContextKeys.is_Some) converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetEncryptionMaterialsInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput(AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsInput value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.AlgorithmSuiteId var_algorithmSuiteId = value.IsSetAlgorithmSuiteId() ? value.AlgorithmSuiteId : (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)null;
      long? var_maxPlaintextLength = value.IsSetMaxPlaintextLength() ? value.MaxPlaintextLength : (long?)null;
      System.Collections.Generic.List<string> var_requiredEncryptionContextKeys = value.IsSetRequiredEncryptionContextKeys() ? value.RequiredEncryptionContextKeys : (System.Collections.Generic.List<string>)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_commitmentPolicy(value.CommitmentPolicy), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_algorithmSuiteId(var_algorithmSuiteId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M18_maxPlaintextLength(var_maxPlaintextLength), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(var_requiredEncryptionContextKeys));
    }
    public static AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IGetEncryptionMaterialsOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput)value; AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsOutput converted = new AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsOutput(); converted.EncryptionMaterials = (AWS.Cryptography.MaterialProviders.EncryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput__M19_encryptionMaterials(concrete._encryptionMaterials); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IGetEncryptionMaterialsOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput(AWS.Cryptography.MaterialProviders.GetEncryptionMaterialsOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput__M19_encryptionMaterials(value.EncryptionMaterials));
    }
    public static AWS.Cryptography.MaterialProviders.InFlightTTLExceeded FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InFlightTTLExceeded value)
    {
      return new AWS.Cryptography.MaterialProviders.InFlightTTLExceeded(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InFlightTTLExceeded ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded(AWS.Cryptography.MaterialProviders.InFlightTTLExceeded value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InFlightTTLExceeded(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.MaterialProviders.InitializeDecryptionMaterialsInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput(software.amazon.cryptography.materialproviders.internaldafny.types._IInitializeDecryptionMaterialsInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput)value; AWS.Cryptography.MaterialProviders.InitializeDecryptionMaterialsInput converted = new AWS.Cryptography.MaterialProviders.InitializeDecryptionMaterialsInput(); converted.AlgorithmSuiteId = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M16_algorithmSuiteId(concrete._algorithmSuiteId);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M17_encryptionContext(concrete._encryptionContext);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IInitializeDecryptionMaterialsInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput(AWS.Cryptography.MaterialProviders.InitializeDecryptionMaterialsInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M16_algorithmSuiteId(value.AlgorithmSuiteId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys));
    }
    public static AWS.Cryptography.MaterialProviders.InitializeEncryptionMaterialsInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput(software.amazon.cryptography.materialproviders.internaldafny.types._IInitializeEncryptionMaterialsInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput)value; AWS.Cryptography.MaterialProviders.InitializeEncryptionMaterialsInput converted = new AWS.Cryptography.MaterialProviders.InitializeEncryptionMaterialsInput(); converted.AlgorithmSuiteId = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M16_algorithmSuiteId(concrete._algorithmSuiteId);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M17_encryptionContext(concrete._encryptionContext);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys);
      if (concrete._signingKey.is_Some) converted.SigningKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M10_signingKey(concrete._signingKey);
      if (concrete._verificationKey.is_Some) converted.VerificationKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M15_verificationKey(concrete._verificationKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IInitializeEncryptionMaterialsInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput(AWS.Cryptography.MaterialProviders.InitializeEncryptionMaterialsInput value)
    {
      value.Validate();
      System.IO.MemoryStream var_signingKey = value.IsSetSigningKey() ? value.SigningKey : (System.IO.MemoryStream)null;
      System.IO.MemoryStream var_verificationKey = value.IsSetVerificationKey() ? value.VerificationKey : (System.IO.MemoryStream)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M16_algorithmSuiteId(value.AlgorithmSuiteId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M10_signingKey(var_signingKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M15_verificationKey(var_verificationKey));
    }
    public static AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfo FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfo value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfo(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfo ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo(AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfo value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfo(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnDecrypt FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnDecrypt value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnDecrypt(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnDecrypt ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt(AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnDecrypt value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnDecrypt(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnEncrypt FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnEncrypt value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnEncrypt(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnEncrypt ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt(AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnEncrypt value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnEncrypt(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterials value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterials(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials(AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterials value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterials(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterialsTransition FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterialsTransition value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterialsTransition(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterialsTransition ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition(AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterialsTransition value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterialsTransition(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterials value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterials(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials(AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterials value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterials(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterialsTransition FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition(software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterialsTransition value)
    {
      return new AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterialsTransition(
      FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterialsTransition ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition(AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterialsTransition value)
    {

      return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterialsTransition(
      ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProviders.KeyAgreementScheme FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IKeyAgreementScheme value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.KeyAgreementScheme concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.KeyAgreementScheme)value;
      var converted = new AWS.Cryptography.MaterialProviders.KeyAgreementScheme(); if (value.is_StaticConfiguration)
      {
        converted.StaticConfiguration = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme__M19_StaticConfiguration(concrete.dtor_StaticConfiguration);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.KeyAgreementScheme state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKeyAgreementScheme ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme(AWS.Cryptography.MaterialProviders.KeyAgreementScheme value)
    {
      value.Validate(); if (value.IsSetStaticConfiguration())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.KeyAgreementScheme.create(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme__M19_StaticConfiguration(value.StaticConfiguration));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.KeyAgreementScheme state");
    }
    public static AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations)value;
      var converted = new AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations(); if (value.is_KmsPublicKeyDiscovery)
      {
        converted.KmsPublicKeyDiscovery = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M21_KmsPublicKeyDiscovery(concrete.dtor_KmsPublicKeyDiscovery);
        return converted;
      }
      if (value.is_KmsPrivateKeyToStaticPublicKey)
      {
        converted.KmsPrivateKeyToStaticPublicKey = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M30_KmsPrivateKeyToStaticPublicKey(concrete.dtor_KmsPrivateKeyToStaticPublicKey);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations value)
    {
      value.Validate(); if (value.IsSetKmsPublicKeyDiscovery())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPublicKeyDiscovery(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M21_KmsPublicKeyDiscovery(value.KmsPublicKeyDiscovery));
      }
      if (value.IsSetKmsPrivateKeyToStaticPublicKey())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.create_KmsPrivateKeyToStaticPublicKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M30_KmsPrivateKeyToStaticPublicKey(value.KmsPrivateKeyToStaticPublicKey));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations state");
    }
    public static AWS.Cryptography.MaterialProviders.MaterialProvidersConfig FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_MaterialProvidersConfig(software.amazon.cryptography.materialproviders.internaldafny.types._IMaterialProvidersConfig value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig)value; AWS.Cryptography.MaterialProviders.MaterialProvidersConfig converted = new AWS.Cryptography.MaterialProviders.MaterialProvidersConfig(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMaterialProvidersConfig ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_MaterialProvidersConfig(AWS.Cryptography.MaterialProviders.MaterialProvidersConfig value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.MaterialProvidersConfig();
    }
    public static AWS.Cryptography.MaterialProviders.Materials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.Materials concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.Materials)value;
      var converted = new AWS.Cryptography.MaterialProviders.Materials(); if (value.is_Encryption)
      {
        converted.Encryption = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Encryption(concrete.dtor_Encryption);
        return converted;
      }
      if (value.is_Decryption)
      {
        converted.Decryption = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Decryption(concrete.dtor_Decryption);
        return converted;
      }
      if (value.is_BranchKey)
      {
        converted.BranchKey = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BranchKey(concrete.dtor_BranchKey);
        return converted;
      }
      if (value.is_BeaconKey)
      {
        converted.BeaconKey = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BeaconKey(concrete.dtor_BeaconKey);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.Materials state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(AWS.Cryptography.MaterialProviders.Materials value)
    {
      value.Validate(); if (value.IsSetEncryption())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_Encryption(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Encryption(value.Encryption));
      }
      if (value.IsSetDecryption())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_Decryption(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Decryption(value.Decryption));
      }
      if (value.IsSetBranchKey())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_BranchKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BranchKey(value.BranchKey));
      }
      if (value.IsSetBeaconKey())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_BeaconKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BeaconKey(value.BeaconKey));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.Materials state");
    }
    public static AWS.Cryptography.MaterialProviders.OnDecryptInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput(software.amazon.cryptography.materialproviders.internaldafny.types._IOnDecryptInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput)value; AWS.Cryptography.MaterialProviders.OnDecryptInput converted = new AWS.Cryptography.MaterialProviders.OnDecryptInput(); converted.Materials = (AWS.Cryptography.MaterialProviders.DecryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M9_materials(concrete._materials);
      converted.EncryptedDataKeys = (System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M17_encryptedDataKeys(concrete._encryptedDataKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IOnDecryptInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput(AWS.Cryptography.MaterialProviders.OnDecryptInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M9_materials(value.Materials), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M17_encryptedDataKeys(value.EncryptedDataKeys));
    }
    public static AWS.Cryptography.MaterialProviders.OnDecryptOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IOnDecryptOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput)value; AWS.Cryptography.MaterialProviders.OnDecryptOutput converted = new AWS.Cryptography.MaterialProviders.OnDecryptOutput(); converted.Materials = (AWS.Cryptography.MaterialProviders.DecryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput__M9_materials(concrete._materials); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IOnDecryptOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput(AWS.Cryptography.MaterialProviders.OnDecryptOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput__M9_materials(value.Materials));
    }
    public static AWS.Cryptography.MaterialProviders.OnEncryptInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput(software.amazon.cryptography.materialproviders.internaldafny.types._IOnEncryptInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput)value; AWS.Cryptography.MaterialProviders.OnEncryptInput converted = new AWS.Cryptography.MaterialProviders.OnEncryptInput(); converted.Materials = (AWS.Cryptography.MaterialProviders.EncryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput__M9_materials(concrete._materials); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IOnEncryptInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput(AWS.Cryptography.MaterialProviders.OnEncryptInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput__M9_materials(value.Materials));
    }
    public static AWS.Cryptography.MaterialProviders.OnEncryptOutput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput(software.amazon.cryptography.materialproviders.internaldafny.types._IOnEncryptOutput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput)value; AWS.Cryptography.MaterialProviders.OnEncryptOutput converted = new AWS.Cryptography.MaterialProviders.OnEncryptOutput(); converted.Materials = (AWS.Cryptography.MaterialProviders.EncryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput__M9_materials(concrete._materials); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IOnEncryptOutput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput(AWS.Cryptography.MaterialProviders.OnEncryptOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput__M9_materials(value.Materials));
    }
    public static AWS.Cryptography.MaterialProviders.PaddingScheme FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme value)
    {
      if (value.is_PKCS1) return AWS.Cryptography.MaterialProviders.PaddingScheme.PKCS1;
      if (value.is_OAEP__SHA1__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA1_MGF1;
      if (value.is_OAEP__SHA256__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA256_MGF1;
      if (value.is_OAEP__SHA384__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA384_MGF1;
      if (value.is_OAEP__SHA512__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA512_MGF1;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.PaddingScheme value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(AWS.Cryptography.MaterialProviders.PaddingScheme value)
    {
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.PKCS1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_PKCS1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA1_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA256_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA256__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA384_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA384__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA512_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA512__MGF1();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.PaddingScheme value");
    }
    public static AWS.Cryptography.MaterialProviders.PutCacheEntryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput(software.amazon.cryptography.materialproviders.internaldafny.types._IPutCacheEntryInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput)value; AWS.Cryptography.MaterialProviders.PutCacheEntryInput converted = new AWS.Cryptography.MaterialProviders.PutCacheEntryInput(); converted.Identifier = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_identifier(concrete._identifier);
      converted.Materials = (AWS.Cryptography.MaterialProviders.Materials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_materials(concrete._materials);
      converted.CreationTime = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_creationTime(concrete._creationTime);
      converted.ExpiryTime = (long)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_expiryTime(concrete._expiryTime);
      if (concrete._messagesUsed.is_Some) converted.MessagesUsed = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_messagesUsed(concrete._messagesUsed);
      if (concrete._bytesUsed.is_Some) converted.BytesUsed = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_bytesUsed(concrete._bytesUsed); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPutCacheEntryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput(AWS.Cryptography.MaterialProviders.PutCacheEntryInput value)
    {
      value.Validate();
      int? var_messagesUsed = value.IsSetMessagesUsed() ? value.MessagesUsed : (int?)null;
      int? var_bytesUsed = value.IsSetBytesUsed() ? value.BytesUsed : (int?)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_materials(value.Materials), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_creationTime(value.CreationTime), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_expiryTime(value.ExpiryTime), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_messagesUsed(var_messagesUsed), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_bytesUsed(var_bytesUsed));
    }
    public static AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations)value;
      var converted = new AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations(); if (value.is_PublicKeyDiscovery)
      {
        converted.PublicKeyDiscovery = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M18_PublicKeyDiscovery(concrete.dtor_PublicKeyDiscovery);
        return converted;
      }
      if (value.is_RawPrivateKeyToStaticPublicKey)
      {
        converted.RawPrivateKeyToStaticPublicKey = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M30_RawPrivateKeyToStaticPublicKey(concrete.dtor_RawPrivateKeyToStaticPublicKey);
        return converted;
      }
      if (value.is_EphemeralPrivateKeyToStaticPublicKey)
      {
        converted.EphemeralPrivateKeyToStaticPublicKey = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M36_EphemeralPrivateKeyToStaticPublicKey(concrete.dtor_EphemeralPrivateKeyToStaticPublicKey);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations value)
    {
      value.Validate(); if (value.IsSetPublicKeyDiscovery())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_PublicKeyDiscovery(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M18_PublicKeyDiscovery(value.PublicKeyDiscovery));
      }
      if (value.IsSetRawPrivateKeyToStaticPublicKey())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_RawPrivateKeyToStaticPublicKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M30_RawPrivateKeyToStaticPublicKey(value.RawPrivateKeyToStaticPublicKey));
      }
      if (value.IsSetEphemeralPrivateKeyToStaticPublicKey())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.create_EphemeralPrivateKeyToStaticPublicKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M36_EphemeralPrivateKeyToStaticPublicKey(value.EphemeralPrivateKeyToStaticPublicKey));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations state");
    }
    public static AWS.Cryptography.MaterialProviders.SignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm(software.amazon.cryptography.materialproviders.internaldafny.types._ISignatureAlgorithm value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm)value;
      var converted = new AWS.Cryptography.MaterialProviders.SignatureAlgorithm(); if (value.is_ECDSA)
      {
        converted.ECDSA = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M5_ECDSA(concrete.dtor_ECDSA);
        return converted;
      }
      if (value.is_None)
      {
        converted.None = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M4_None(concrete.dtor_None);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.SignatureAlgorithm state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm(AWS.Cryptography.MaterialProviders.SignatureAlgorithm value)
    {
      value.Validate(); if (value.IsSetECDSA())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M5_ECDSA(value.ECDSA));
      }
      if (value.IsSetNone())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M4_None(value.None));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.SignatureAlgorithm state");
    }
    public static AWS.Cryptography.MaterialProviders.StaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations(software.amazon.cryptography.materialproviders.internaldafny.types._IStaticConfigurations value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.StaticConfigurations concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.StaticConfigurations)value;
      var converted = new AWS.Cryptography.MaterialProviders.StaticConfigurations(); if (value.is_AWS__KMS__ECDH)
      {
        converted.AWS__KMS__ECDH = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M12_AWS_KMS_ECDH(concrete.dtor_AWS__KMS__ECDH);
        return converted;
      }
      if (value.is_RAW__ECDH)
      {
        converted.RAW__ECDH = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M8_RAW_ECDH(concrete.dtor_RAW__ECDH);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.StaticConfigurations state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations(AWS.Cryptography.MaterialProviders.StaticConfigurations value)
    {
      value.Validate(); if (value.IsSetAWS__KMS__ECDH())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.StaticConfigurations.create_AWS__KMS__ECDH(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M12_AWS_KMS_ECDH(value.AWS__KMS__ECDH));
      }
      if (value.IsSetRAW__ECDH())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.StaticConfigurations.create_RAW__ECDH(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M8_RAW_ECDH(value.RAW__ECDH));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.StaticConfigurations state");
    }
    public static AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm(software.amazon.cryptography.materialproviders.internaldafny.types._ISymmetricSignatureAlgorithm value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm)value;
      var converted = new AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm(); if (value.is_HMAC)
      {
        converted.HMAC = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_HMAC(concrete.dtor_HMAC);
        return converted;
      }
      if (value.is_None)
      {
        converted.None = FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_None(concrete.dtor_None);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm state");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISymmetricSignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm(AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm value)
    {
      value.Validate(); if (value.IsSetHMAC())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_HMAC(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_HMAC(value.HMAC));
      }
      if (value.IsSetNone())
      {
        return software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_None(value.None));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm state");
    }
    public static AWS.Cryptography.MaterialProviders.TimeUnits FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_TimeUnits(software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits value)
    {
      if (value.is_Seconds) return AWS.Cryptography.MaterialProviders.TimeUnits.Seconds;
      if (value.is_Milliseconds) return AWS.Cryptography.MaterialProviders.TimeUnits.Milliseconds;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.TimeUnits value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_TimeUnits(AWS.Cryptography.MaterialProviders.TimeUnits value)
    {
      if (AWS.Cryptography.MaterialProviders.TimeUnits.Seconds.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits.create_Seconds();
      if (AWS.Cryptography.MaterialProviders.TimeUnits.Milliseconds.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits.create_Milliseconds();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.TimeUnits value");
    }
    public static AWS.Cryptography.MaterialProviders.UpdateUsageMetadataInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput(software.amazon.cryptography.materialproviders.internaldafny.types._IUpdateUsageMetadataInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput)value; AWS.Cryptography.MaterialProviders.UpdateUsageMetadataInput converted = new AWS.Cryptography.MaterialProviders.UpdateUsageMetadataInput(); converted.Identifier = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M10_identifier(concrete._identifier);
      converted.BytesUsed = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M9_bytesUsed(concrete._bytesUsed); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IUpdateUsageMetadataInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput(AWS.Cryptography.MaterialProviders.UpdateUsageMetadataInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M10_identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M9_bytesUsed(value.BytesUsed));
    }
    public static AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnDecryptInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput(software.amazon.cryptography.materialproviders.internaldafny.types._IValidateCommitmentPolicyOnDecryptInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput)value; AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnDecryptInput converted = new AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnDecryptInput(); converted.Algorithm = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M9_algorithm(concrete._algorithm);
      converted.CommitmentPolicy = (AWS.Cryptography.MaterialProviders.CommitmentPolicy)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M16_commitmentPolicy(concrete._commitmentPolicy); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IValidateCommitmentPolicyOnDecryptInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput(AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnDecryptInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M9_algorithm(value.Algorithm), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M16_commitmentPolicy(value.CommitmentPolicy));
    }
    public static AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnEncryptInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput(software.amazon.cryptography.materialproviders.internaldafny.types._IValidateCommitmentPolicyOnEncryptInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput)value; AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnEncryptInput converted = new AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnEncryptInput(); converted.Algorithm = (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M9_algorithm(concrete._algorithm);
      converted.CommitmentPolicy = (AWS.Cryptography.MaterialProviders.CommitmentPolicy)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M16_commitmentPolicy(concrete._commitmentPolicy); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IValidateCommitmentPolicyOnEncryptInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput(AWS.Cryptography.MaterialProviders.ValidateCommitmentPolicyOnEncryptInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M9_algorithm(value.Algorithm), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M16_commitmentPolicy(value.CommitmentPolicy));
    }
    public static AWS.Cryptography.MaterialProviders.ValidDecryptionMaterialsTransitionInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput(software.amazon.cryptography.materialproviders.internaldafny.types._IValidDecryptionMaterialsTransitionInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput)value; AWS.Cryptography.MaterialProviders.ValidDecryptionMaterialsTransitionInput converted = new AWS.Cryptography.MaterialProviders.ValidDecryptionMaterialsTransitionInput(); converted.Start = (AWS.Cryptography.MaterialProviders.DecryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M5_start(concrete._start);
      converted.Stop = (AWS.Cryptography.MaterialProviders.DecryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M4_stop(concrete._stop); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IValidDecryptionMaterialsTransitionInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput(AWS.Cryptography.MaterialProviders.ValidDecryptionMaterialsTransitionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M5_start(value.Start), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M4_stop(value.Stop));
    }
    public static AWS.Cryptography.MaterialProviders.ValidEncryptionMaterialsTransitionInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput(software.amazon.cryptography.materialproviders.internaldafny.types._IValidEncryptionMaterialsTransitionInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput)value; AWS.Cryptography.MaterialProviders.ValidEncryptionMaterialsTransitionInput converted = new AWS.Cryptography.MaterialProviders.ValidEncryptionMaterialsTransitionInput(); converted.Start = (AWS.Cryptography.MaterialProviders.EncryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M5_start(concrete._start);
      converted.Stop = (AWS.Cryptography.MaterialProviders.EncryptionMaterials)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M4_stop(concrete._stop); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IValidEncryptionMaterialsTransitionInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput(AWS.Cryptography.MaterialProviders.ValidEncryptionMaterialsTransitionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M5_start(value.Start), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M4_stop(value.Stop));
    }
    public static AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M4_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types._IESDKAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKAlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IESDKAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M4_ESDK(AWS.Cryptography.MaterialProviders.ESDKAlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKAlgorithmSuiteId(value);
    }
    public static AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M3_DBE(software.amazon.cryptography.materialproviders.internaldafny.types._IDBEAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBEAlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDBEAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId__M3_DBE(AWS.Cryptography.MaterialProviders.DBEAlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBEAlgorithmSuiteId(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M2_id(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M2_id(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M8_binaryId(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M8_binaryId(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M14_messageVersion(int value)
    {
      return FromDafny_N6_smithy__N3_api__S7_Integer(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M14_messageVersion(int value)
    {
      return ToDafny_N6_smithy__N3_api__S7_Integer(value);
    }
    public static AWS.Cryptography.MaterialProviders.Encrypt FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M7_encrypt(software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M7_encrypt(AWS.Cryptography.MaterialProviders.Encrypt value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(value);
    }
    public static AWS.Cryptography.MaterialProviders.DerivationAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M3_kdf(software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M3_kdf(AWS.Cryptography.MaterialProviders.DerivationAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.DerivationAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M10_commitment(software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M10_commitment(AWS.Cryptography.MaterialProviders.DerivationAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.SignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M9_signature(software.amazon.cryptography.materialproviders.internaldafny.types._ISignatureAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M9_signature(AWS.Cryptography.MaterialProviders.SignatureAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M18_symmetricSignature(software.amazon.cryptography.materialproviders.internaldafny.types._ISymmetricSignatureAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISymmetricSignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M18_symmetricSignature(AWS.Cryptography.MaterialProviders.SymmetricSignatureAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M11_edkWrapping(software.amazon.cryptography.materialproviders.internaldafny.types._IEdkWrappingAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEdkWrappingAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo__M11_edkWrapping(AWS.Cryptography.MaterialProviders.EdkWrappingAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.DefaultCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M7_Default(software.amazon.cryptography.materialproviders.internaldafny.types._IDefaultCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDefaultCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M7_Default(AWS.Cryptography.MaterialProviders.DefaultCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.NoCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M2_No(software.amazon.cryptography.materialproviders.internaldafny.types._INoCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_NoCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INoCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M2_No(AWS.Cryptography.MaterialProviders.NoCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_NoCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.SingleThreadedCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M14_SingleThreaded(software.amazon.cryptography.materialproviders.internaldafny.types._ISingleThreadedCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISingleThreadedCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M14_SingleThreaded(AWS.Cryptography.MaterialProviders.SingleThreadedCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.MultiThreadedCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_MultiThreaded(software.amazon.cryptography.materialproviders.internaldafny.types._IMultiThreadedCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMultiThreadedCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_MultiThreaded(AWS.Cryptography.MaterialProviders.MultiThreadedCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.StormTrackingCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_StormTracking(software.amazon.cryptography.materialproviders.internaldafny.types._IStormTrackingCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IStormTrackingCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M13_StormTracking(AWS.Cryptography.MaterialProviders.StormTrackingCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M6_Shared(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType__M6_Shared(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M4_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types._IESDKCommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKCommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IESDKCommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M4_ESDK(AWS.Cryptography.MaterialProviders.ESDKCommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_ESDKCommitmentPolicy(value);
    }
    public static AWS.Cryptography.MaterialProviders.DBECommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M3_DBE(software.amazon.cryptography.materialproviders.internaldafny.types._IDBECommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBECommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDBECommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy__M3_DBE(AWS.Cryptography.MaterialProviders.DBECommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DBECommitmentPolicy(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M15_discoveryFilter(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M15_discoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter((AWS.Cryptography.MaterialProviders.DiscoveryFilter)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateAwsKmsDiscoveryKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M7_regions(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M7_regions(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M15_discoveryFilter(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M15_discoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter((AWS.Cryptography.MaterialProviders.DiscoveryFilter)value));
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M14_clientSupplier(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IClientSupplier)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M14_clientSupplier(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference((AWS.Cryptography.MaterialProviders.IClientSupplier)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateAwsKmsDiscoveryMultiKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M18_KeyAgreementScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M18_KeyAgreementScheme(AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(value);
    }
    public static AWS.Cryptography.Primitives.ECDHCurveSpec FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_curveSpec(software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_curveSpec(AWS.Cryptography.Primitives.ECDHCurveSpec value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_CreateAwsKmsEcdhKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_branchKeyId(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_branchKeyId(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M19_branchKeyIdSupplier(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_BranchKeyIdSupplierReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M19_branchKeyIdSupplier(AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_BranchKeyIdSupplierReference((AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier)value));
    }
    public static AWS.Cryptography.KeyStore.KeyStore FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M8_keyStore(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M8_keyStore(AWS.Cryptography.KeyStore.KeyStore value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M10_ttlSeconds(long value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M10_ttlSeconds(long value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static AWS.Cryptography.MaterialProviders.CacheType FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M5_cache(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.CacheType)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M5_cache(AWS.Cryptography.MaterialProviders.CacheType value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType((AWS.Cryptography.MaterialProviders.CacheType)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_partitionId(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsHierarchicalKeyringInput__M11_partitionId(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M8_kmsKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M8_kmsKeyId(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateAwsKmsKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M15_discoveryFilter(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M15_discoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter((AWS.Cryptography.MaterialProviders.DiscoveryFilter)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M6_region(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CreateAwsKmsMrkDiscoveryKeyringInput__M6_region(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M7_regions(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M7_regions(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M15_discoveryFilter(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M15_discoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter((AWS.Cryptography.MaterialProviders.DiscoveryFilter)value));
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M14_clientSupplier(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IClientSupplier)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M14_clientSupplier(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference((AWS.Cryptography.MaterialProviders.IClientSupplier)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateAwsKmsMrkDiscoveryMultiKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M8_kmsKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M8_kmsKeyId(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsMrkKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_generator(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_generator(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId((string)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_kmsKeyIds(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M9_kmsKeyIds(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M14_clientSupplier(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IClientSupplier)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M14_clientSupplier(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference((AWS.Cryptography.MaterialProviders.IClientSupplier)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S32_CreateAwsKmsMrkMultiKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_generator(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_generator(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId((string)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_kmsKeyIds(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M9_kmsKeyIds(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M14_clientSupplier(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IClientSupplier)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M14_clientSupplier(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference((AWS.Cryptography.MaterialProviders.IClientSupplier)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S29_CreateAwsKmsMultiKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_publicKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_publicKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M8_kmsKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M8_kmsKeyId(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Amazon.KeyManagementService.EncryptionAlgorithmSpec FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M19_encryptionAlgorithm(software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M19_encryptionAlgorithm(Amazon.KeyManagementService.EncryptionAlgorithmSpec value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_kmsClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> value)
    {
      return value.is_None ? (Amazon.KeyManagementService.IAmazonKeyManagementService)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference((Amazon.KeyManagementService.IAmazonKeyManagementService)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_CreateAwsKmsRsaKeyringInput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.CacheType FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput__M5_cache(software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICacheType ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CreateCryptographicMaterialsCacheInput__M5_cache(AWS.Cryptography.MaterialProviders.CacheType value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_CacheType(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput__M14_materialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateCryptographicMaterialsCacheOutput__M14_materialsCache(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput__M16_materialsManager(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_CreateCryptographicMaterialsManagerOutput__M16_materialsManager(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput__M6_client(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S33_CreateDefaultClientSupplierOutput__M6_client(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput__M7_keyring(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S47_CreateDefaultCryptographicMaterialsManagerInput__M7_keyring(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M9_generator(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IKeyring)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M9_generator(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference((AWS.Cryptography.MaterialProviders.IKeyring)value));
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M13_childKeyrings(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_CreateMultiKeyringInput__M13_childKeyrings(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M12_keyNamespace(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M12_keyNamespace(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M7_keyName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M7_keyName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.MaterialProviders.AesWrappingAlg FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingAlg(software.amazon.cryptography.materialproviders.internaldafny.types._IAesWrappingAlg value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_AesWrappingAlg(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAesWrappingAlg ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawAesKeyringInput__M11_wrappingAlg(AWS.Cryptography.MaterialProviders.AesWrappingAlg value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_AesWrappingAlg(value);
    }
    public static AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M18_KeyAgreementScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M18_KeyAgreementScheme(AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(value);
    }
    public static AWS.Cryptography.Primitives.ECDHCurveSpec FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M9_curveSpec(software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_CreateRawEcdhKeyringInput__M9_curveSpec(AWS.Cryptography.Primitives.ECDHCurveSpec value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M12_keyNamespace(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M12_keyNamespace(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M7_keyName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M7_keyName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.PaddingScheme FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M13_paddingScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M13_paddingScheme(AWS.Cryptography.MaterialProviders.PaddingScheme value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M9_publicKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N6_smithy__N3_api__S4_Blob(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M9_publicKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N6_smithy__N3_api__S4_Blob((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M10_privateKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N6_smithy__N3_api__S4_Blob(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_CreateRawRsaKeyringInput__M10_privateKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N6_smithy__N3_api__S4_Blob((System.IO.MemoryStream)value));
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M13_underlyingCMM(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M13_underlyingCMM(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference((AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager)value));
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M7_keyring(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.IKeyring)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M7_keyring(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference((AWS.Cryptography.MaterialProviders.IKeyring)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_CreateRequiredEncryptionContextCMMInput__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput__M16_materialsManager(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S40_CreateRequiredEncryptionContextCMMOutput__M16_materialsManager(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M14_algorithmSuite(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M14_algorithmSuite(AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M16_plaintextDataKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M16_plaintextDataKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M15_verificationKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M15_verificationKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M19_symmetricSigningKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials__M19_symmetricSigningKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_algorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_algorithmSuiteId(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static AWS.Cryptography.MaterialProviders.CommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_commitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M16_commitmentPolicy(AWS.Cryptography.MaterialProviders.CommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptedDataKeys(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptedDataKeys(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M27_reproducedEncryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DecryptMaterialsInput__M27_reproducedEncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput__M19_decryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S22_DecryptMaterialsOutput__M19_decryptionMaterials(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput__M10_identifier(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_DeleteCacheEntryInput__M10_identifier(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.MaterialProviders.HKDF FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_HKDF(software.amazon.cryptography.materialproviders.internaldafny.types._IHKDF value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IHKDF ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_HKDF(AWS.Cryptography.MaterialProviders.HKDF value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF(value);
    }
    public static AWS.Cryptography.MaterialProviders.IDENTITY FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M8_IDENTITY(software.amazon.cryptography.materialproviders.internaldafny.types._IIDENTITY value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_IDENTITY(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IIDENTITY ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M8_IDENTITY(AWS.Cryptography.MaterialProviders.IDENTITY value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_IDENTITY(value);
    }
    public static AWS.Cryptography.MaterialProviders.None FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_None(software.amazon.cryptography.materialproviders.internaldafny.types._INone value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INone ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm__M4_None(AWS.Cryptography.MaterialProviders.None value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M19_DIRECT_KEY_WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types._IDIRECT__KEY__WRAPPING value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DIRECT_KEY_WRAPPING(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDIRECT__KEY__WRAPPING ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M19_DIRECT_KEY_WRAPPING(AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DIRECT_KEY_WRAPPING(value);
    }
    public static AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M23_IntermediateKeyWrapping(software.amazon.cryptography.materialproviders.internaldafny.types._IIntermediateKeyWrapping value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IIntermediateKeyWrapping ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EdkWrappingAlgorithm__M23_IntermediateKeyWrapping(AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping(value);
    }
    public static AWS.Cryptography.Primitives.AES_GCM FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt__M7_AES_GCM(software.amazon.cryptography.primitives.internaldafny.types._IAES__GCM value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IAES__GCM ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt__M7_AES_GCM(AWS.Cryptography.Primitives.AES_GCM value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M14_algorithmSuite(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteInfo ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M14_algorithmSuite(AWS.Cryptography.MaterialProviders.AlgorithmSuiteInfo value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_AlgorithmSuiteInfo(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptedDataKeys(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M17_encryptedDataKeys(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M16_plaintextDataKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M16_plaintextDataKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M10_signingKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M10_signingKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.Collections.Generic.List<System.IO.MemoryStream> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M20_symmetricSigningKeys(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<System.IO.MemoryStream>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials__M20_symmetricSigningKeys(System.Collections.Generic.List<System.IO.MemoryStream> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList((System.Collections.Generic.List<System.IO.MemoryStream>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput__M8_binaryId(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_GetAlgorithmSuiteInfoInput__M8_binaryId(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetBranchKeyIdInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput__M11_branchKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_GetBranchKeyIdOutput__M11_branchKeyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M10_identifier(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M10_identifier(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static long? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M9_bytesUsed(Wrappers_Compile._IOption<long> value)
    {
      return value.is_None ? (long?)null : FromDafny_N6_smithy__N3_api__S4_Long(value.Extract());
    }
    public static Wrappers_Compile._IOption<long> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_GetCacheEntryInput__M9_bytesUsed(long? value)
    {
      return value == null ? Wrappers_Compile.Option<long>.create_None() : Wrappers_Compile.Option<long>.create_Some(ToDafny_N6_smithy__N3_api__S4_Long((long)value));
    }
    public static AWS.Cryptography.MaterialProviders.Materials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_materials(AWS.Cryptography.MaterialProviders.Materials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_creationTime(long value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_creationTime(long value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M10_expiryTime(long value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M10_expiryTime(long value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_messagesUsed(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M12_messagesUsed(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_bytesUsed(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_GetCacheEntryOutput__M9_bytesUsed(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput__M6_region(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GetClientInput__M6_region(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput__M6_client(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_GetClientOutput__M6_client(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static AWS.Cryptography.MaterialProviders.CommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_commitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_commitmentPolicy(AWS.Cryptography.MaterialProviders.CommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_algorithmSuiteId(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M16_algorithmSuiteId(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId((AWS.Cryptography.MaterialProviders.AlgorithmSuiteId)value));
    }
    public static long? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M18_maxPlaintextLength(Wrappers_Compile._IOption<long> value)
    {
      return value.is_None ? (long?)null : FromDafny_N6_smithy__N3_api__S4_Long(value.Extract());
    }
    public static Wrappers_Compile._IOption<long> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M18_maxPlaintextLength(long? value)
    {
      return value == null ? Wrappers_Compile.Option<long>.create_None() : Wrappers_Compile.Option<long>.create_Some(ToDafny_N6_smithy__N3_api__S4_Long((long)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_GetEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput__M19_encryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_GetEncryptionMaterialsOutput__M19_encryptionMaterials(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M16_algorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M16_algorithmSuiteId(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeDecryptionMaterialsInput__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M16_algorithmSuiteId(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M16_algorithmSuiteId(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M10_signingKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M10_signingKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M15_verificationKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InitializeEncryptionMaterialsInput__M15_verificationKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret((System.IO.MemoryStream)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.StaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme__M19_StaticConfiguration(software.amazon.cryptography.materialproviders.internaldafny.types._IStaticConfigurations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KeyAgreementScheme__M19_StaticConfiguration(AWS.Cryptography.MaterialProviders.StaticConfigurations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations(value);
    }
    public static AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M21_KmsPublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPublicKeyDiscoveryInput value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPublicKeyDiscoveryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M21_KmsPublicKeyDiscovery(AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput(value);
    }
    public static AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M30_KmsPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPrivateKeyToStaticPublicKeyInput value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations__M30_KmsPrivateKeyToStaticPublicKey(AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Encryption(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Encryption(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Decryption(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M10_Decryption(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static AWS.Cryptography.KeyStore.BranchKeyMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BranchKey(software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BranchKey(AWS.Cryptography.KeyStore.BranchKeyMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static AWS.Cryptography.KeyStore.BeaconKeyMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BeaconKey(software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials__M9_BeaconKey(AWS.Cryptography.KeyStore.BeaconKeyMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M9_materials(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M17_encryptedDataKeys(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnDecryptInput__M17_encryptedDataKeys(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(value);
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnDecryptOutput__M9_materials(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_OnEncryptInput__M9_materials(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_OnEncryptOutput__M9_materials(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_identifier(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_identifier(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.MaterialProviders.Materials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_materials(software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_materials(AWS.Cryptography.MaterialProviders.Materials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Materials(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_creationTime(long value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_creationTime(long value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_expiryTime(long value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M10_expiryTime(long value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_messagesUsed(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M12_messagesUsed(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger((int)value));
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_bytesUsed(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_PutCacheEntryInput__M9_bytesUsed(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger((int)value));
    }
    public static AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M18_PublicKeyDiscovery(software.amazon.cryptography.materialproviders.internaldafny.types._IPublicKeyDiscoveryInput value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPublicKeyDiscoveryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M18_PublicKeyDiscovery(AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput(value);
    }
    public static AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M30_RawPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types._IRawPrivateKeyToStaticPublicKeyInput value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IRawPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M30_RawPrivateKeyToStaticPublicKey(AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput(value);
    }
    public static AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M36_EphemeralPrivateKeyToStaticPublicKey(software.amazon.cryptography.materialproviders.internaldafny.types._IEphemeralPrivateKeyToStaticPublicKeyInput value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEphemeralPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations__M36_EphemeralPrivateKeyToStaticPublicKey(AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput(value);
    }
    public static AWS.Cryptography.MaterialProviders.ECDSA FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M5_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types._IECDSA value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IECDSA ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M5_ECDSA(AWS.Cryptography.MaterialProviders.ECDSA value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA(value);
    }
    public static AWS.Cryptography.MaterialProviders.None FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M4_None(software.amazon.cryptography.materialproviders.internaldafny.types._INone value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INone ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_SignatureAlgorithm__M4_None(AWS.Cryptography.MaterialProviders.None value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M12_AWS_KMS_ECDH(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M12_AWS_KMS_ECDH(AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_KmsEcdhStaticConfigurations(value);
    }
    public static AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M8_RAW_ECDH(software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IRawEcdhStaticConfigurations ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_StaticConfigurations__M8_RAW_ECDH(AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_RawEcdhStaticConfigurations(value);
    }
    public static AWS.Cryptography.Primitives.DigestAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_HMAC(software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_HMAC(AWS.Cryptography.Primitives.DigestAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.None FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_None(software.amazon.cryptography.materialproviders.internaldafny.types._INone value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INone ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S27_SymmetricSignatureAlgorithm__M4_None(AWS.Cryptography.MaterialProviders.None value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M10_identifier(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M10_identifier(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M9_bytesUsed(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S24_UpdateUsageMetadataInput__M9_bytesUsed(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M9_algorithm(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M9_algorithm(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static AWS.Cryptography.MaterialProviders.CommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M16_commitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnDecryptInput__M16_commitmentPolicy(AWS.Cryptography.MaterialProviders.CommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static AWS.Cryptography.MaterialProviders.AlgorithmSuiteId FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M9_algorithm(software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IAlgorithmSuiteId ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M9_algorithm(AWS.Cryptography.MaterialProviders.AlgorithmSuiteId value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_AlgorithmSuiteId(value);
    }
    public static AWS.Cryptography.MaterialProviders.CommitmentPolicy FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M16_commitmentPolicy(software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ICommitmentPolicy ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_ValidateCommitmentPolicyOnEncryptInput__M16_commitmentPolicy(AWS.Cryptography.MaterialProviders.CommitmentPolicy value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_CommitmentPolicy(value);
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M5_start(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M5_start(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.DecryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M4_stop(software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDecryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidDecryptionMaterialsTransitionInput__M4_stop(AWS.Cryptography.MaterialProviders.DecryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DecryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M5_start(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M5_start(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptionMaterials FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M4_stop(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptionMaterials ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S39_ValidEncryptionMaterialsTransitionInput__M4_stop(AWS.Cryptography.MaterialProviders.EncryptionMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_EncryptionMaterials(value);
    }
    public static System.IO.MemoryStream FromDafny_N6_smithy__N3_api__S4_Blob(Dafny.ISequence<byte> value)
    {
      return new System.IO.MemoryStream(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N6_smithy__N3_api__S4_Blob(System.IO.MemoryStream value)
    {
      if (value.ToArray().Length == 0 && value.Length > 0)
      {
        throw new System.ArgumentException("Fatal Error: MemoryStream instance not backed by an array!");
      }
      return Dafny.Sequence<byte>.FromArray(value.ToArray());

    }
    public static int FromDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static int ToDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static string FromDafny_N6_smithy__N3_api__S6_String(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N6_smithy__N3_api__S6_String(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static AWS.Cryptography.MaterialProviders.DefaultCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache(software.amazon.cryptography.materialproviders.internaldafny.types._IDefaultCache value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache)value; AWS.Cryptography.MaterialProviders.DefaultCache converted = new AWS.Cryptography.MaterialProviders.DefaultCache(); converted.EntryCapacity = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache__M13_entryCapacity(concrete._entryCapacity); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDefaultCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache(AWS.Cryptography.MaterialProviders.DefaultCache value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache__M13_entryCapacity(value.EntryCapacity));
    }
    public static AWS.Cryptography.MaterialProviders.NoCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_NoCache(software.amazon.cryptography.materialproviders.internaldafny.types._INoCache value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.NoCache concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.NoCache)value; AWS.Cryptography.MaterialProviders.NoCache converted = new AWS.Cryptography.MaterialProviders.NoCache(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INoCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_NoCache(AWS.Cryptography.MaterialProviders.NoCache value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.NoCache();
    }
    public static AWS.Cryptography.MaterialProviders.SingleThreadedCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache(software.amazon.cryptography.materialproviders.internaldafny.types._ISingleThreadedCache value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache)value; AWS.Cryptography.MaterialProviders.SingleThreadedCache converted = new AWS.Cryptography.MaterialProviders.SingleThreadedCache(); converted.EntryCapacity = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M13_entryCapacity(concrete._entryCapacity);
      if (concrete._entryPruningTailSize.is_Some) converted.EntryPruningTailSize = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M20_entryPruningTailSize(concrete._entryPruningTailSize); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._ISingleThreadedCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache(AWS.Cryptography.MaterialProviders.SingleThreadedCache value)
    {
      value.Validate();
      int? var_entryPruningTailSize = value.IsSetEntryPruningTailSize() ? value.EntryPruningTailSize : (int?)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M13_entryCapacity(value.EntryCapacity), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M20_entryPruningTailSize(var_entryPruningTailSize));
    }
    public static AWS.Cryptography.MaterialProviders.MultiThreadedCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache(software.amazon.cryptography.materialproviders.internaldafny.types._IMultiThreadedCache value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache)value; AWS.Cryptography.MaterialProviders.MultiThreadedCache converted = new AWS.Cryptography.MaterialProviders.MultiThreadedCache(); converted.EntryCapacity = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M13_entryCapacity(concrete._entryCapacity);
      if (concrete._entryPruningTailSize.is_Some) converted.EntryPruningTailSize = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M20_entryPruningTailSize(concrete._entryPruningTailSize); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IMultiThreadedCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache(AWS.Cryptography.MaterialProviders.MultiThreadedCache value)
    {
      value.Validate();
      int? var_entryPruningTailSize = value.IsSetEntryPruningTailSize() ? value.EntryPruningTailSize : (int?)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M13_entryCapacity(value.EntryCapacity), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M20_entryPruningTailSize(var_entryPruningTailSize));
    }
    public static AWS.Cryptography.MaterialProviders.StormTrackingCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache(software.amazon.cryptography.materialproviders.internaldafny.types._IStormTrackingCache value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)value; AWS.Cryptography.MaterialProviders.StormTrackingCache converted = new AWS.Cryptography.MaterialProviders.StormTrackingCache(); converted.EntryCapacity = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_entryCapacity(concrete._entryCapacity);
      if (concrete._entryPruningTailSize.is_Some) converted.EntryPruningTailSize = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M20_entryPruningTailSize(concrete._entryPruningTailSize);
      converted.GracePeriod = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_gracePeriod(concrete._gracePeriod);
      converted.GraceInterval = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_graceInterval(concrete._graceInterval);
      converted.FanOut = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M6_fanOut(concrete._fanOut);
      converted.InFlightTTL = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_inFlightTTL(concrete._inFlightTTL);
      converted.SleepMilli = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M10_sleepMilli(concrete._sleepMilli);
      if (concrete._timeUnits.is_Some) converted.TimeUnits = (AWS.Cryptography.MaterialProviders.TimeUnits)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M9_timeUnits(concrete._timeUnits); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IStormTrackingCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache(AWS.Cryptography.MaterialProviders.StormTrackingCache value)
    {
      value.Validate();
      int? var_entryPruningTailSize = value.IsSetEntryPruningTailSize() ? value.EntryPruningTailSize : (int?)null;
      AWS.Cryptography.MaterialProviders.TimeUnits var_timeUnits = value.IsSetTimeUnits() ? value.TimeUnits : (AWS.Cryptography.MaterialProviders.TimeUnits)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_entryCapacity(value.EntryCapacity), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M20_entryPruningTailSize(var_entryPruningTailSize), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_gracePeriod(value.GracePeriod), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_graceInterval(value.GraceInterval), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M6_fanOut(value.FanOut), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_inFlightTTL(value.InFlightTTL), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M10_sleepMilli(value.SleepMilli), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M9_timeUnits(var_timeUnits));
    }
    internal static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(value);
    }
    internal static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_CryptographicMaterialsCacheReference(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return new WrappedNativeWrapper_CryptographicMaterialsCache((CryptographicMaterialsCacheBase)value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_KmsClientReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter)value; AWS.Cryptography.MaterialProviders.DiscoveryFilter converted = new AWS.Cryptography.MaterialProviders.DiscoveryFilter(); converted.AccountIds = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(concrete._accountIds);
      converted.Partition = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(concrete._partition); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(value.AccountIds), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(value.Partition));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList__M6_member).ToArray());
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList__M6_member).ToArray());
    }
    internal static AWS.Cryptography.MaterialProviders.IClientSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(value);
    }
    internal static software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_ClientSupplierReference(AWS.Cryptography.MaterialProviders.IClientSupplier value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return new WrappedNativeWrapper_ClientSupplier((ClientSupplierBase)value);
    }
    public static AWS.Cryptography.Primitives.ECDHCurveSpec FromDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec value)
    {
      if (value.is_ECC__NIST__P256) return AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P256;
      if (value.is_ECC__NIST__P384) return AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P384;
      if (value.is_ECC__NIST__P521) return AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P521;
      if (value.is_SM2) return AWS.Cryptography.Primitives.ECDHCurveSpec.SM2;
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.ECDHCurveSpec value");
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IECDHCurveSpec ToDafny_N3_aws__N12_cryptography__N10_primitives__S13_ECDHCurveSpec(AWS.Cryptography.Primitives.ECDHCurveSpec value)
    {
      if (AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P256.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P256();
      if (AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P384.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P384();
      if (AWS.Cryptography.Primitives.ECDHCurveSpec.ECC_NIST_P521.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_ECC__NIST__P521();
      if (AWS.Cryptography.Primitives.ECDHCurveSpec.SM2.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.create_SM2();
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.ECDHCurveSpec value");
    }
    internal static AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_BranchKeyIdSupplierReference(software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_BranchKeyIdSupplierReference(value);
    }
    internal static software.amazon.cryptography.materialproviders.internaldafny.types.IBranchKeyIdSupplier ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S28_BranchKeyIdSupplierReference(AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return new WrappedNativeWrapper_BranchKeyIdSupplier((BranchKeyIdSupplierBase)value);
    }
    public static AWS.Cryptography.KeyStore.KeyStore FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStoreClient ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(AWS.Cryptography.KeyStore.KeyStore value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_KeyStoreReference(value);
    }
    public static long FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(long value)
    {
      return value;
    }
    public static long ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_PositiveLong(long value)
    {
      return value;
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList__M6_member).ToArray());
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(Dafny.ISequence<byte> value)
    {
      return new System.IO.MemoryStream(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(System.IO.MemoryStream value)
    {
      if (value.ToArray().Length == 0 && value.Length > 0)
      {
        throw new System.ArgumentException("Fatal Error: MemoryStream instance not backed by an array!");
      }
      return Dafny.Sequence<byte>.FromArray(value.ToArray());

    }
    public static Amazon.KeyManagementService.EncryptionAlgorithmSpec FromDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec value)
    {
      if (value.is_SYMMETRIC__DEFAULT) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT;
      if (value.is_RSAES__OAEP__SHA__1) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1;
      if (value.is_RSAES__OAEP__SHA__256) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256;
      throw new System.ArgumentException("Invalid Amazon.KeyManagementService.EncryptionAlgorithmSpec value");
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec ToDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(Amazon.KeyManagementService.EncryptionAlgorithmSpec value)
    {
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_SYMMETRIC__DEFAULT();
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__1();
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__256();
      throw new System.ArgumentException("Invalid Amazon.KeyManagementService.EncryptionAlgorithmSpec value");
    }
    internal static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    internal static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return new WrappedNativeWrapper_CryptographicMaterialsManager((CryptographicMaterialsManagerBase)value);
    }
    internal static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    internal static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return new WrappedNativeWrapper_Keyring((KeyringBase)value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.IKeyring> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList__M6_member).ToArray());
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<byte>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member).ToArray());
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return Dafny.Map<Dafny.ISequence<byte>, Dafny.ISequence<byte>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<byte>, Dafny.ISequence<byte>>(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M5_value(pair.Value))
     ));
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList(System.Collections.Generic.List<AWS.Cryptography.MaterialProviders.EncryptedDataKey> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList__M6_member).ToArray());
    }
    public static AWS.Cryptography.MaterialProviders.HKDF FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF(software.amazon.cryptography.materialproviders.internaldafny.types._IHKDF value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.HKDF concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.HKDF)value; AWS.Cryptography.MaterialProviders.HKDF converted = new AWS.Cryptography.MaterialProviders.HKDF(); converted.Hmac = (AWS.Cryptography.Primitives.DigestAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M4_hmac(concrete._hmac);
      converted.SaltLength = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M10_saltLength(concrete._saltLength);
      converted.InputKeyLength = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M14_inputKeyLength(concrete._inputKeyLength);
      converted.OutputKeyLength = (int)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M15_outputKeyLength(concrete._outputKeyLength); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IHKDF ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF(AWS.Cryptography.MaterialProviders.HKDF value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.HKDF(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M4_hmac(value.Hmac), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M10_saltLength(value.SaltLength), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M14_inputKeyLength(value.InputKeyLength), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M15_outputKeyLength(value.OutputKeyLength));
    }
    public static AWS.Cryptography.MaterialProviders.IDENTITY FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_IDENTITY(software.amazon.cryptography.materialproviders.internaldafny.types._IIDENTITY value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY)value; AWS.Cryptography.MaterialProviders.IDENTITY converted = new AWS.Cryptography.MaterialProviders.IDENTITY(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IIDENTITY ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_IDENTITY(AWS.Cryptography.MaterialProviders.IDENTITY value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY();
    }
    public static AWS.Cryptography.MaterialProviders.None FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(software.amazon.cryptography.materialproviders.internaldafny.types._INone value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.None concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.None)value; AWS.Cryptography.MaterialProviders.None converted = new AWS.Cryptography.MaterialProviders.None(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._INone ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_None(AWS.Cryptography.MaterialProviders.None value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.None();
    }
    public static AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DIRECT_KEY_WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types._IDIRECT__KEY__WRAPPING value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING)value; AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING converted = new AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING(); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDIRECT__KEY__WRAPPING ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DIRECT_KEY_WRAPPING(AWS.Cryptography.MaterialProviders.DIRECT_KEY_WRAPPING value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING();
    }
    public static AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping(software.amazon.cryptography.materialproviders.internaldafny.types._IIntermediateKeyWrapping value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.IntermediateKeyWrapping concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.IntermediateKeyWrapping)value; AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping converted = new AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping(); converted.KeyEncryptionKeyKdf = (AWS.Cryptography.MaterialProviders.DerivationAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_keyEncryptionKeyKdf(concrete._keyEncryptionKeyKdf);
      converted.MacKeyKdf = (AWS.Cryptography.MaterialProviders.DerivationAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M9_macKeyKdf(concrete._macKeyKdf);
      converted.PdkEncryptAlgorithm = (AWS.Cryptography.MaterialProviders.Encrypt)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_pdkEncryptAlgorithm(concrete._pdkEncryptAlgorithm); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IIntermediateKeyWrapping ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping(AWS.Cryptography.MaterialProviders.IntermediateKeyWrapping value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.IntermediateKeyWrapping(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_keyEncryptionKeyKdf(value.KeyEncryptionKeyKdf), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M9_macKeyKdf(value.MacKeyKdf), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_pdkEncryptAlgorithm(value.PdkEncryptAlgorithm));
    }
    public static AWS.Cryptography.Primitives.AES_GCM FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM(software.amazon.cryptography.primitives.internaldafny.types._IAES__GCM value)
    {
      software.amazon.cryptography.primitives.internaldafny.types.AES__GCM concrete = (software.amazon.cryptography.primitives.internaldafny.types.AES__GCM)value; AWS.Cryptography.Primitives.AES_GCM converted = new AWS.Cryptography.Primitives.AES_GCM(); converted.KeyLength = (int)FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_keyLength(concrete._keyLength);
      converted.TagLength = (int)FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_tagLength(concrete._tagLength);
      converted.IvLength = (int)FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M8_ivLength(concrete._ivLength); return converted;
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IAES__GCM ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM(AWS.Cryptography.Primitives.AES_GCM value)
    {
      value.Validate();

      return new software.amazon.cryptography.primitives.internaldafny.types.AES__GCM(ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_keyLength(value.KeyLength), ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_tagLength(value.TagLength), ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M8_ivLength(value.IvLength));
    }
    public static System.Collections.Generic.List<System.IO.MemoryStream> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return new System.Collections.Generic.List<System.IO.MemoryStream>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList(System.Collections.Generic.List<System.IO.MemoryStream> value)
    {
      return Dafny.Sequence<Dafny.ISequence<byte>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList__M6_member).ToArray());
    }
    public static long FromDafny_N6_smithy__N3_api__S4_Long(long value)
    {
      return value;
    }
    public static long ToDafny_N6_smithy__N3_api__S4_Long(long value)
    {
      return value;
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_PositiveInteger(int value)
    {
      return value;
    }
    public static AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPublicKeyDiscoveryInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput)value; AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput converted = new AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput(); converted.RecipientKmsIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput__M22_recipientKmsIdentifier(concrete._recipientKmsIdentifier); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPublicKeyDiscoveryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput(AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput__M22_recipientKmsIdentifier(value.RecipientKmsIdentifier));
    }
    public static AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput(software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPrivateKeyToStaticPublicKeyInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput)value; AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput converted = new AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput(); converted.SenderKmsIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M19_senderKmsIdentifier(concrete._senderKmsIdentifier);
      if (concrete._senderPublicKey.is_Some) converted.SenderPublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M15_senderPublicKey(concrete._senderPublicKey);
      converted.RecipientPublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(concrete._recipientPublicKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IKmsPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput(AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput value)
    {
      value.Validate();
      System.IO.MemoryStream var_senderPublicKey = value.IsSetSenderPublicKey() ? value.SenderPublicKey : (System.IO.MemoryStream)null;
      return new software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M19_senderKmsIdentifier(value.SenderKmsIdentifier), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M15_senderPublicKey(var_senderPublicKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(value.RecipientPublicKey));
    }
    public static AWS.Cryptography.KeyStore.BranchKeyMaterials FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials concrete = (software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials)value; AWS.Cryptography.KeyStore.BranchKeyMaterials converted = new AWS.Cryptography.KeyStore.BranchKeyMaterials(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M19_branchKeyIdentifier(concrete._branchKeyIdentifier);
      converted.BranchKeyVersion = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M16_branchKeyVersion(concrete._branchKeyVersion);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M17_encryptionContext(concrete._encryptionContext);
      converted.BranchKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M9_branchKey(concrete._branchKey); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(AWS.Cryptography.KeyStore.BranchKeyMaterials value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M19_branchKeyIdentifier(value.BranchKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M16_branchKeyVersion(value.BranchKeyVersion), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M9_branchKey(value.BranchKey));
    }
    public static AWS.Cryptography.KeyStore.BeaconKeyMaterials FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials concrete = (software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials)value; AWS.Cryptography.KeyStore.BeaconKeyMaterials converted = new AWS.Cryptography.KeyStore.BeaconKeyMaterials(); converted.BeaconKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M19_beaconKeyIdentifier(concrete._beaconKeyIdentifier);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M17_encryptionContext(concrete._encryptionContext);
      if (concrete._beaconKey.is_Some) converted.BeaconKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M9_beaconKey(concrete._beaconKey);
      if (concrete._hmacKeys.is_Some) converted.HmacKeys = (System.Collections.Generic.Dictionary<string, System.IO.MemoryStream>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M8_hmacKeys(concrete._hmacKeys); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(AWS.Cryptography.KeyStore.BeaconKeyMaterials value)
    {
      value.Validate();
      System.IO.MemoryStream var_beaconKey = value.IsSetBeaconKey() ? value.BeaconKey : (System.IO.MemoryStream)null;
      System.Collections.Generic.Dictionary<string, System.IO.MemoryStream> var_hmacKeys = value.IsSetHmacKeys() ? value.HmacKeys : (System.Collections.Generic.Dictionary<string, System.IO.MemoryStream>)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.BeaconKeyMaterials(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M19_beaconKeyIdentifier(value.BeaconKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M17_encryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M9_beaconKey(var_beaconKey), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M8_hmacKeys(var_hmacKeys));
    }
    public static AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput(software.amazon.cryptography.materialproviders.internaldafny.types._IPublicKeyDiscoveryInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput)value; AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput converted = new AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput(); converted.RecipientStaticPrivateKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput__M25_recipientStaticPrivateKey(concrete._recipientStaticPrivateKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPublicKeyDiscoveryInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput(AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput__M25_recipientStaticPrivateKey(value.RecipientStaticPrivateKey));
    }
    public static AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput(software.amazon.cryptography.materialproviders.internaldafny.types._IRawPrivateKeyToStaticPublicKeyInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput)value; AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput converted = new AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput(); converted.SenderStaticPrivateKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M22_senderStaticPrivateKey(concrete._senderStaticPrivateKey);
      converted.RecipientPublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(concrete._recipientPublicKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IRawPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput(AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M22_senderStaticPrivateKey(value.SenderStaticPrivateKey), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(value.RecipientPublicKey));
    }
    public static AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput(software.amazon.cryptography.materialproviders.internaldafny.types._IEphemeralPrivateKeyToStaticPublicKeyInput value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput)value; AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput converted = new AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput(); converted.RecipientPublicKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(concrete._recipientPublicKey); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEphemeralPrivateKeyToStaticPublicKeyInput ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput(AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(value.RecipientPublicKey));
    }
    public static AWS.Cryptography.MaterialProviders.ECDSA FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types._IECDSA value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA)value; AWS.Cryptography.MaterialProviders.ECDSA converted = new AWS.Cryptography.MaterialProviders.ECDSA(); converted.Curve = (AWS.Cryptography.Primitives.ECDSASignatureAlgorithm)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA__M5_curve(concrete._curve); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IECDSA ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA(AWS.Cryptography.MaterialProviders.ECDSA value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA__M5_curve(value.Curve));
    }
    public static AWS.Cryptography.Primitives.DigestAlgorithm FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm value)
    {
      if (value.is_SHA__512) return AWS.Cryptography.Primitives.DigestAlgorithm.SHA_512;
      if (value.is_SHA__384) return AWS.Cryptography.Primitives.DigestAlgorithm.SHA_384;
      if (value.is_SHA__256) return AWS.Cryptography.Primitives.DigestAlgorithm.SHA_256;
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.DigestAlgorithm value");
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(AWS.Cryptography.Primitives.DigestAlgorithm value)
    {
      if (AWS.Cryptography.Primitives.DigestAlgorithm.SHA_512.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512();
      if (AWS.Cryptography.Primitives.DigestAlgorithm.SHA_384.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384();
      if (AWS.Cryptography.Primitives.DigestAlgorithm.SHA_256.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256();
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.DigestAlgorithm value");
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache__M13_entryCapacity(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_DefaultCache__M13_entryCapacity(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M13_entryCapacity(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M13_entryCapacity(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M20_entryPruningTailSize(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_SingleThreadedCache__M20_entryPruningTailSize(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber((int)value));
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M13_entryCapacity(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M13_entryCapacity(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M20_entryPruningTailSize(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_MultiThreadedCache__M20_entryPruningTailSize(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber((int)value));
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_entryCapacity(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_entryCapacity(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M20_entryPruningTailSize(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M20_entryPruningTailSize(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber((int)value));
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_gracePeriod(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_gracePeriod(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_graceInterval(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M13_graceInterval(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M6_fanOut(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M6_fanOut(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_inFlightTTL(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M11_inFlightTTL(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M10_sleepMilli(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M10_sleepMilli(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(value);
    }
    public static AWS.Cryptography.MaterialProviders.TimeUnits FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M9_timeUnits(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.TimeUnits)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_TimeUnits(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_StormTrackingCache__M9_timeUnits(AWS.Cryptography.MaterialProviders.TimeUnits value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._ITimeUnits>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_TimeUnits((AWS.Cryptography.MaterialProviders.TimeUnits)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_GrantTokenList__M6_member(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S10_RegionList__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Region(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S12_KmsKeyIdList__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList__M6_member(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S11_KeyringList__M6_member(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M3_key(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M3_key(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M5_value(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EncryptionContext__M5_value(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static AWS.Cryptography.MaterialProviders.EncryptedDataKey FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList__M6_member(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S20_EncryptedDataKeyList__M6_member(AWS.Cryptography.MaterialProviders.EncryptedDataKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey(value);
    }
    public static AWS.Cryptography.Primitives.DigestAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M4_hmac(software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IDigestAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M4_hmac(AWS.Cryptography.Primitives.DigestAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_DigestAlgorithm(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M10_saltLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_PositiveInteger(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M10_saltLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_PositiveInteger(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M14_inputKeyLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M14_inputKeyLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M15_outputKeyLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S4_HKDF__M15_outputKeyLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static AWS.Cryptography.MaterialProviders.DerivationAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_keyEncryptionKeyKdf(software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_keyEncryptionKeyKdf(AWS.Cryptography.MaterialProviders.DerivationAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.DerivationAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M9_macKeyKdf(software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDerivationAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M9_macKeyKdf(AWS.Cryptography.MaterialProviders.DerivationAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_DerivationAlgorithm(value);
    }
    public static AWS.Cryptography.MaterialProviders.Encrypt FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_pdkEncryptAlgorithm(software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncrypt ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_IntermediateKeyWrapping__M19_pdkEncryptAlgorithm(AWS.Cryptography.MaterialProviders.Encrypt value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S7_Encrypt(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_keyLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_keyLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_tagLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S10_Uint8Bytes(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M9_tagLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S10_Uint8Bytes(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M8_ivLength(int value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S9_Uint8Bits(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S7_AES_GCM__M8_ivLength(int value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S9_Uint8Bits(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList__M6_member(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_SymmetricSigningKeyList__M6_member(System.IO.MemoryStream value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S6_Secret(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput__M22_recipientKmsIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_KmsPublicKeyDiscoveryInput__M22_recipientKmsIdentifier(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M19_senderKmsIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M19_senderKmsIdentifier(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S8_KmsKeyId(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M15_senderPublicKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N6_smithy__N3_api__S4_Blob(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M15_senderPublicKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N6_smithy__N3_api__S4_Blob((System.IO.MemoryStream)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_KmsPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M16_branchKeyVersion(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M16_branchKeyVersion(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M9_branchKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials__M9_branchKey(System.IO.MemoryStream value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M19_beaconKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M19_beaconKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M17_encryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value);
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M9_beaconKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M9_beaconKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret((System.IO.MemoryStream)value));
    }
    public static System.Collections.Generic.Dictionary<string, System.IO.MemoryStream> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M8_hmacKeys(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, System.IO.MemoryStream>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials__M8_hmacKeys(System.Collections.Generic.Dictionary<string, System.IO.MemoryStream> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap((System.Collections.Generic.Dictionary<string, System.IO.MemoryStream>)value));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput__M25_recipientStaticPrivateKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S23_PublicKeyDiscoveryInput__M25_recipientStaticPrivateKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M22_senderStaticPrivateKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M22_senderStaticPrivateKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S35_RawPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S41_EphemeralPrivateKeyToStaticPublicKeyInput__M18_recipientPublicKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.Primitives.ECDSASignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA__M5_curve(software.amazon.cryptography.primitives.internaldafny.types._IECDSASignatureAlgorithm value)
    {
      return FromDafny_N3_aws__N12_cryptography__N10_primitives__S23_ECDSASignatureAlgorithm(value);
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IECDSASignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S5_ECDSA__M5_curve(AWS.Cryptography.Primitives.ECDSASignatureAlgorithm value)
    {
      return ToDafny_N3_aws__N12_cryptography__N10_primitives__S23_ECDSASignatureAlgorithm(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S14_CountingNumber(int value)
    {
      return value;
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member).ToArray());
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(Dafny.ISequence<byte> value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return utf8.GetString(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(string value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return Dafny.Sequence<byte>.FromArray(utf8.GetBytes(value));
    }
    public static AWS.Cryptography.MaterialProviders.EncryptedDataKey FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey(software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)value; AWS.Cryptography.MaterialProviders.EncryptedDataKey converted = new AWS.Cryptography.MaterialProviders.EncryptedDataKey(); converted.KeyProviderId = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M13_keyProviderId(concrete._keyProviderId);
      converted.KeyProviderInfo = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M15_keyProviderInfo(concrete._keyProviderInfo);
      converted.Ciphertext = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M10_ciphertext(concrete._ciphertext); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IEncryptedDataKey ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey(AWS.Cryptography.MaterialProviders.EncryptedDataKey value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M13_keyProviderId(value.KeyProviderId), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M15_keyProviderInfo(value.KeyProviderInfo), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M10_ciphertext(value.Ciphertext));
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S15_PositiveInteger(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S15_PositiveInteger(int value)
    {
      return value;
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S18_SymmetricKeyLength(int value)
    {
      return value;
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S10_Uint8Bytes(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S10_Uint8Bytes(int value)
    {
      return value;
    }
    public static int FromDafny_N3_aws__N12_cryptography__N10_primitives__S9_Uint8Bits(int value)
    {
      return value;
    }
    public static int ToDafny_N3_aws__N12_cryptography__N10_primitives__S9_Uint8Bits(int value)
    {
      return value;
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(Dafny.ISequence<byte> value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return utf8.GetString(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(string value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return Dafny.Sequence<byte>.FromArray(utf8.GetBytes(value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return Dafny.Map<Dafny.ISequence<byte>, Dafny.ISequence<byte>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<byte>, Dafny.ISequence<byte>>(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(pair.Value))
     ));
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(Dafny.ISequence<byte> value)
    {
      return new System.IO.MemoryStream(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(System.IO.MemoryStream value)
    {
      if (value.ToArray().Length == 0 && value.Length > 0)
      {
        throw new System.ArgumentException("Fatal Error: MemoryStream instance not backed by an array!");
      }
      return Dafny.Sequence<byte>.FromArray(value.ToArray());

    }
    public static System.Collections.Generic.Dictionary<string, System.IO.MemoryStream> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap(System.Collections.Generic.Dictionary<string, System.IO.MemoryStream> value)
    {
      return Dafny.Map<Dafny.ISequence<char>, Dafny.ISequence<byte>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<char>, Dafny.ISequence<byte>>(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M5_value(pair.Value))
     ));
    }
    public static AWS.Cryptography.Primitives.ECDSASignatureAlgorithm FromDafny_N3_aws__N12_cryptography__N10_primitives__S23_ECDSASignatureAlgorithm(software.amazon.cryptography.primitives.internaldafny.types._IECDSASignatureAlgorithm value)
    {
      if (value.is_ECDSA__P384) return AWS.Cryptography.Primitives.ECDSASignatureAlgorithm.ECDSA_P384;
      if (value.is_ECDSA__P256) return AWS.Cryptography.Primitives.ECDSASignatureAlgorithm.ECDSA_P256;
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.ECDSASignatureAlgorithm value");
    }
    public static software.amazon.cryptography.primitives.internaldafny.types._IECDSASignatureAlgorithm ToDafny_N3_aws__N12_cryptography__N10_primitives__S23_ECDSASignatureAlgorithm(AWS.Cryptography.Primitives.ECDSASignatureAlgorithm value)
    {
      if (AWS.Cryptography.Primitives.ECDSASignatureAlgorithm.ECDSA_P384.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384();
      if (AWS.Cryptography.Primitives.ECDSASignatureAlgorithm.ECDSA_P256.Equals(value)) return software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P256();
      throw new System.ArgumentException("Invalid AWS.Cryptography.Primitives.ECDSASignatureAlgorithm value");
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M13_keyProviderId(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M13_keyProviderId(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M15_keyProviderInfo(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M15_keyProviderInfo(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M10_ciphertext(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_EncryptedDataKey__M10_ciphertext(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M3_key(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext__M5_value(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M3_key(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M3_key(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M5_value(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S10_HmacKeyMap__M5_value(System.IO.MemoryStream value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_Secret(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.materialproviders.internaldafny.types._IError value)
    {
      switch (value)
      {
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyKeyStore dafnyVal:
          return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyKeyStore
          );
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives dafnyVal:
          return AWS.Cryptography.Primitives.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyPrimitives
          );
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsDynamodb dafnyVal:
          return Com.Amazonaws.Dynamodb.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsDynamodb
          );
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_ComAmazonawsKms dafnyVal:
          // BEGIN MANUAL EDIT
          return Com.Amazonaws.Kms.TypeConversion.FromDafny_CommonError(
          // END MANUAL EDIT
            dafnyVal._ComAmazonawsKms
          );
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryAlreadyExists dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_EntryDoesNotExist dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InFlightTTLExceeded dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfo dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnDecrypt dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidAlgorithmSuiteInfoOnEncrypt dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterials dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidDecryptionMaterialsTransition dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterials dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_InvalidEncryptionMaterialsTransition dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition(dafnyVal);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
        case software.amazon.cryptography.materialproviders.internaldafny.types.Error_OpaqueWithText dafnyVal:
          return new OpaqueWithTextError(dafnyVal._obj, dafnyVal._obj.ToString());
        default:
          // The switch MUST be complete for _IError, so `value` MUST NOT be an _IError. (How did you get here?)
          return new OpaqueError();
      }
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IError ToDafny_CommonError(System.Exception value)
    {

      switch (value)
      {
        case AWS.Cryptography.MaterialProviders.AwsCryptographicMaterialProvidersException exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S42_AwsCryptographicMaterialProvidersException(exception);
        case AWS.Cryptography.MaterialProviders.EntryAlreadyExists exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S18_EntryAlreadyExists(exception);
        case AWS.Cryptography.MaterialProviders.EntryDoesNotExist exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S17_EntryDoesNotExist(exception);
        case AWS.Cryptography.MaterialProviders.InFlightTTLExceeded exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_InFlightTTLExceeded(exception);
        case AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfo exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S25_InvalidAlgorithmSuiteInfo(exception);
        case AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnDecrypt exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnDecrypt(exception);
        case AWS.Cryptography.MaterialProviders.InvalidAlgorithmSuiteInfoOnEncrypt exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S34_InvalidAlgorithmSuiteInfoOnEncrypt(exception);
        case AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterials exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidDecryptionMaterials(exception);
        case AWS.Cryptography.MaterialProviders.InvalidDecryptionMaterialsTransition exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidDecryptionMaterialsTransition(exception);
        case AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterials exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S26_InvalidEncryptionMaterials(exception);
        case AWS.Cryptography.MaterialProviders.InvalidEncryptionMaterialsTransition exception:
          return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S36_InvalidEncryptionMaterialsTransition(exception);
        case CollectionOfErrors collectionOfErrors:
          return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors(
            Dafny.Sequence<software.amazon.cryptography.materialproviders.internaldafny.types._IError>
              .FromArray(
                collectionOfErrors.list.Select
                    (x => TypeConversion.ToDafny_CommonError(x))
                  .ToArray()),
            Dafny.Sequence<char>.FromString(collectionOfErrors.Message)
          );
        // OpaqueError is redundant, but listed for completeness.
        case OpaqueError exception:
          return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_Opaque(exception);
        case System.Exception exception:
          return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_Opaque(exception);
        default:
          // The switch MUST be complete for System.Exception, so `value` MUST NOT be an System.Exception. (How did you get here?)
          return new software.amazon.cryptography.materialproviders.internaldafny.types.Error_Opaque(value);
      }
    }
  }
}
