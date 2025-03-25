// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public static class TypeConversion
  {
    private const string ISO8601DateFormat = "yyyy-MM-dd\\THH:mm:ss.fff\\Z";

    private const string ISO8601DateFormatNoMS = "yyyy-MM-dd\\THH:mm:ss\\Z";

    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput)value; AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput(); converted.MutationToken = (AWS.Cryptography.KeyStoreAdmin.MutationToken)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(concrete._MutationToken);
      if (concrete._PageSize.is_Some) converted.PageSize = (int)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(concrete._PageSize);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(concrete._Strategy);
      converted.SystemKey = (AWS.Cryptography.KeyStoreAdmin.SystemKey)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(concrete._SystemKey); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput(AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput value)
    {
      value.Validate();
      int? var_pageSize = value.IsSetPageSize() ? value.PageSize : (int?)null;
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(value.MutationToken), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(var_pageSize), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(var_strategy), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(value.SystemKey));
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput(); converted.MutationResult = (AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(concrete._MutationResult);
      converted.MutatedBranchKeyItems = (System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(concrete._MutatedBranchKeyItems); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput(AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(value.MutationResult), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(value.MutatedBranchKeyItems));
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult(); if (value.is_ContinueMutation)
      {
        converted.ContinueMutation = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(concrete.dtor_ContinueMutation);
        return converted;
      }
      if (value.is_CompleteMutation)
      {
        converted.CompleteMutation = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(concrete.dtor_CompleteMutation);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult value)
    {
      value.Validate(); if (value.IsSetContinueMutation())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult.create_ContinueMutation(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(value.ContinueMutation));
      }
      if (value.IsSetCompleteMutation())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.ApplyMutationResult.create_CompleteMutation(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(value.CompleteMutation));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyInput(); if (concrete._Identifier.is_Some) converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(concrete._Identifier);
      if (concrete._EncryptionContext.is_Some) converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(concrete._EncryptionContext);
      converted.KmsArn = (AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(concrete._KmsArn);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(concrete._Strategy);
      if (concrete._HierarchyVersion.is_Some) converted.HierarchyVersion = (AWS.Cryptography.KeyStore.HierarchyVersion)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M16_HierarchyVersion(concrete._HierarchyVersion); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(AWS.Cryptography.KeyStoreAdmin.CreateKeyInput value)
    {
      value.Validate();
      string var_identifier = value.IsSetIdentifier() ? value.Identifier : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_encryptionContext = value.IsSetEncryptionContext() ? value.EncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      AWS.Cryptography.KeyStore.HierarchyVersion var_hierarchyVersion = value.IsSetHierarchyVersion() ? value.HierarchyVersion : (AWS.Cryptography.KeyStore.HierarchyVersion)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(var_identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(var_encryptionContext), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(var_strategy), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M16_HierarchyVersion(var_hierarchyVersion));
    }
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(concrete._Identifier);
      converted.HierarchyVersion = (AWS.Cryptography.KeyStore.HierarchyVersion)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M16_HierarchyVersion(concrete._HierarchyVersion); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M16_HierarchyVersion(value.HierarchyVersion));
    }
    public static AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput)value; AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput(AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput(); converted.MutationInFlight = (AWS.Cryptography.KeyStoreAdmin.MutationInFlight)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M16_MutationInFlight(concrete._MutationInFlight); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput(AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.DescribeMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M16_MutationInFlight(value.MutationInFlight));
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag value)
    {
      if (value.is_Created) return AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.Created;
      if (value.is_Resumed) return AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.Resumed;
      if (value.is_ResumedWithoutIndex) return AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.ResumedWithoutIndex;
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value)
    {
      if (AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.Created.Equals(value)) return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_Created();
      if (AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.Resumed.Equals(value)) return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_Resumed();
      if (AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag.ResumedWithoutIndex.Equals(value)) return software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationFlag.create_ResumedWithoutIndex();
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value");
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput)value; AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput converted = new AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(concrete._Identifier);
      converted.Mutations = (AWS.Cryptography.KeyStoreAdmin.Mutations)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(concrete._Mutations);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(concrete._Strategy);
      converted.SystemKey = (AWS.Cryptography.KeyStoreAdmin.SystemKey)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(concrete._SystemKey);
      if (concrete._DoNotVersion.is_Some) converted.DoNotVersion = (bool)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M12_DoNotVersion(concrete._DoNotVersion); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput(AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      bool? var_doNotVersion = value.IsSetDoNotVersion() ? value.DoNotVersion : (bool?)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(value.Mutations), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(var_strategy), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(value.SystemKey), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M12_DoNotVersion(var_doNotVersion));
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput)value; AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput converted = new AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput(); converted.MutationToken = (AWS.Cryptography.KeyStoreAdmin.MutationToken)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(concrete._MutationToken);
      converted.MutatedBranchKeyItems = (System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(concrete._MutatedBranchKeyItems);
      converted.InitializeMutationFlag = (AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(concrete._InitializeMutationFlag); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput(AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.InitializeMutationOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(value.MutationToken), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(value.MutatedBranchKeyItems), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(value.InitializeMutationFlag));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy(); if (value.is_AwsKmsReEncrypt)
      {
        converted.AwsKmsReEncrypt = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(concrete.dtor_AwsKmsReEncrypt);
        return converted;
      }
      if (value.is_AwsKmsDecryptEncrypt)
      {
        converted.AwsKmsDecryptEncrypt = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M20_AwsKmsDecryptEncrypt(concrete.dtor_AwsKmsDecryptEncrypt);
        return converted;
      }
      if (value.is_AwsKmsSimple)
      {
        converted.AwsKmsSimple = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M12_AwsKmsSimple(concrete.dtor_AwsKmsSimple);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      value.Validate(); if (value.IsSetAwsKmsReEncrypt())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy.create_AwsKmsReEncrypt(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(value.AwsKmsReEncrypt));
      }
      if (value.IsSetAwsKmsDecryptEncrypt())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy.create_AwsKmsDecryptEncrypt(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M20_AwsKmsDecryptEncrypt(value.AwsKmsDecryptEncrypt));
      }
      if (value.IsSetAwsKmsSimple())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyManagementStrategy.create_AwsKmsSimple(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M12_AwsKmsSimple(value.AwsKmsSimple));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig)value; AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig converted = new AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig(); converted.LogicalKeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(concrete._logicalKeyStoreName);
      converted.Storage = (AWS.Cryptography.KeyStore.Storage)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(concrete._storage); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(value.LogicalKeyStoreName), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(value.Storage));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricKeyArn concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricKeyArn)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn(); if (value.is_KmsKeyArn)
      {
        converted.KmsKeyArn = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M9_KmsKeyArn(concrete.dtor_KmsKeyArn);
        return converted;
      }
      if (value.is_KmsMRKey)
      {
        converted.KmsMRKey = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M8_KmsMRKey(concrete.dtor_KmsMRKey);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn value)
    {
      value.Validate(); if (value.IsSetKmsKeyArn())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricKeyArn.create_KmsKeyArn(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M9_KmsKeyArn(value.KmsKeyArn));
      }
      if (value.IsSetKmsMRKey())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricKeyArn.create_KmsMRKey(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M8_KmsMRKey(value.KmsMRKey));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationConflictException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationConflictException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(AWS.Cryptography.KeyStoreAdmin.MutationConflictException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationFromException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationFromException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(AWS.Cryptography.KeyStoreAdmin.MutationFromException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationInFlight FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationInFlight value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationInFlight concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationInFlight)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.MutationInFlight(); if (value.is_Yes)
      {
        converted.Yes = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M3_Yes(concrete.dtor_Yes);
        return converted;
      }
      if (value.is_No)
      {
        converted.No = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M2_No(concrete.dtor_No);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.MutationInFlight state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationInFlight ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight(AWS.Cryptography.KeyStoreAdmin.MutationInFlight value)
    {
      value.Validate(); if (value.IsSetYes())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationInFlight.create_Yes(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M3_Yes(value.Yes));
      }
      if (value.IsSetNo())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationInFlight.create_No(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M2_No(value.No));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.MutationInFlight state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationInvalidException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationInvalidException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(AWS.Cryptography.KeyStoreAdmin.MutationInvalidException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationToException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(AWS.Cryptography.KeyStoreAdmin.MutationToException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationVerificationException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.MutationVerificationException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(AWS.Cryptography.KeyStoreAdmin.MutationVerificationException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey)value;
      var converted = new AWS.Cryptography.KeyStoreAdmin.SystemKey(); if (value.is_kmsSymmetricEncryption)
      {
        converted.KmsSymmetricEncryption = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M22_kmsSymmetricEncryption(concrete.dtor_kmsSymmetricEncryption);
        return converted;
      }
      if (value.is_trustStorage)
      {
        converted.TrustStorage = FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_trustStorage(concrete.dtor_trustStorage);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.SystemKey state");
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      value.Validate(); if (value.IsSetKmsSymmetricEncryption())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey.create_kmsSymmetricEncryption(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M22_kmsSymmetricEncryption(value.KmsSymmetricEncryption));
      }
      if (value.IsSetTrustStorage())
      {
        return software.amazon.cryptography.keystoreadmin.internaldafny.types.SystemKey.create_trustStorage(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_trustStorage(value.TrustStorage));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStoreAdmin.SystemKey state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.UnsupportedFeatureException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnsupportedFeatureException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.UnsupportedFeatureException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnsupportedFeatureException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException(AWS.Cryptography.KeyStoreAdmin.UnsupportedFeatureException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnsupportedFeatureException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStoreAdmin.VersionKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput)value; AWS.Cryptography.KeyStoreAdmin.VersionKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.VersionKeyInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(concrete._Identifier);
      converted.KmsArn = (AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(concrete._KmsArn);
      if (concrete._Strategy.is_Some) converted.Strategy = (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(concrete._Strategy); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(AWS.Cryptography.KeyStoreAdmin.VersionKeyInput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy var_strategy = value.IsSetStrategy() ? value.Strategy : (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(var_strategy));
    }
    public static AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_VersionKeyOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput)value; AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput converted = new AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_VersionKeyOutput(AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyOutput();
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static int? FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(Wrappers_Compile._IOption<int> value)
    {
      return value.is_None ? (int?)null : FromDafny_N6_smithy__N3_api__S7_Integer(value.Extract());
    }
    public static Wrappers_Compile._IOption<int> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_PageSize(int? value)
    {
      return value == null ? Wrappers_Compile.Option<int>.create_None() : Wrappers_Compile.Option<int>.create_Some(ToDafny_N6_smithy__N3_api__S7_Integer((int)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput__M9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationResult ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M14_MutationResult(AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput__M21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_ContinueMutation(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationComplete FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationResult__M16_CompleteMutation(AWS.Cryptography.KeyStoreAdmin.MutationComplete value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M10_Identifier(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_KmsArn(AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStore.HierarchyVersion FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M16_HierarchyVersion(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.HierarchyVersion)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M16_HierarchyVersion(AWS.Cryptography.KeyStore.HierarchyVersion value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion((AWS.Cryptography.KeyStore.HierarchyVersion)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.HierarchyVersion FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M16_HierarchyVersion(software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M16_HierarchyVersion(AWS.Cryptography.KeyStore.HierarchyVersion value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationInFlight FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M16_MutationInFlight(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationInFlight value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationInFlight ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput__M16_MutationInFlight(AWS.Cryptography.KeyStoreAdmin.MutationInFlight value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.Mutations FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_Mutations(AWS.Cryptography.KeyStoreAdmin.Mutations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.SystemKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ISystemKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M9_SystemKey(AWS.Cryptography.KeyStoreAdmin.SystemKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey(value);
    }
    public static bool? FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M12_DoNotVersion(Wrappers_Compile._IOption<bool> value)
    {
      return value.is_None ? (bool?)null : FromDafny_N6_smithy__N3_api__S7_Boolean(value.Extract());
    }
    public static Wrappers_Compile._IOption<bool> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput__M12_DoNotVersion(bool? value)
    {
      return value == null ? Wrappers_Compile.Option<bool>.create_None() : Wrappers_Compile.Option<bool>.create_Some(ToDafny_N6_smithy__N3_api__S7_Boolean((bool)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationFlag ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput__M22_InitializeMutationFlag(AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_InitializeMutationFlag(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M15_AwsKmsReEncrypt(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M20_AwsKmsDecryptEncrypt(software.amazon.cryptography.keystoreadmin.internaldafny.types._IAwsKmsDecryptEncrypt value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IAwsKmsDecryptEncrypt ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M20_AwsKmsDecryptEncrypt(AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M12_AwsKmsSimple(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy__M12_AwsKmsSimple(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(software.amazon.cryptography.keystore.internaldafny.types._IStorage value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(AWS.Cryptography.KeyStore.Storage value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M9_KmsKeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M9_KmsKeyArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsMRKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M8_KmsMRKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsMRKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsMRKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn__M8_KmsMRKey(AWS.Cryptography.KeyStoreAdmin.KmsMRKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationDescription FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M3_Yes(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDescription ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M3_Yes(AWS.Cryptography.KeyStoreAdmin.MutationDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M2_No(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationInFlight__M2_No(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M22_kmsSymmetricEncryption(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricEncryption value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricEncryption ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M22_kmsSymmetricEncryption(AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.TrustStorage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_trustStorage(software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_SystemKey__M12_trustStorage(AWS.Cryptography.KeyStoreAdmin.TrustStorage value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricKeyArn ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_KmsArn(AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsSymmetricKeyArn(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)null : FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M8_Strategy(AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyManagementStrategy>.create_Some(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_KeyManagementStrategy((AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken)value; AWS.Cryptography.KeyStoreAdmin.MutationToken converted = new AWS.Cryptography.KeyStoreAdmin.MutationToken(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(concrete._Identifier);
      converted.UUID = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(concrete._UUID);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(concrete._CreateTime); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationToken(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(value.UUID), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(value.CreateTime));
    }
    public static int FromDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static int ToDafny_N6_smithy__N3_api__S7_Integer(int value)
    {
      return value;
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems(System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member).ToArray());
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationComplete FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete)value; AWS.Cryptography.KeyStoreAdmin.MutationComplete converted = new AWS.Cryptography.KeyStoreAdmin.MutationComplete(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationComplete ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_MutationComplete(AWS.Cryptography.KeyStoreAdmin.MutationComplete value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationComplete();
    }
    public static string FromDafny_N6_smithy__N3_api__S6_String(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N6_smithy__N3_api__S6_String(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
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
    public static AWS.Cryptography.KeyStore.HierarchyVersion FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion value)
    {
      if (value.is_v1) return AWS.Cryptography.KeyStore.HierarchyVersion.v1;
      if (value.is_v2) return AWS.Cryptography.KeyStore.HierarchyVersion.v2;
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.HierarchyVersion value");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(AWS.Cryptography.KeyStore.HierarchyVersion value)
    {
      if (AWS.Cryptography.KeyStore.HierarchyVersion.v1.Equals(value)) return software.amazon.cryptography.keystore.internaldafny.types.HierarchyVersion.create_v1();
      if (AWS.Cryptography.KeyStore.HierarchyVersion.v2.Equals(value)) return software.amazon.cryptography.keystore.internaldafny.types.HierarchyVersion.create_v2();
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.HierarchyVersion value");
    }
    public static AWS.Cryptography.KeyStoreAdmin.Mutations FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations)value; AWS.Cryptography.KeyStoreAdmin.Mutations converted = new AWS.Cryptography.KeyStoreAdmin.Mutations(); if (concrete._TerminalKmsArn.is_Some) converted.TerminalKmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(concrete._TerminalKmsArn);
      if (concrete._TerminalEncryptionContext.is_Some) converted.TerminalEncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(concrete._TerminalEncryptionContext);
      if (concrete._TerminalHierarchyVersion.is_Some) converted.TerminalHierarchyVersion = (AWS.Cryptography.KeyStore.HierarchyVersion)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M24_TerminalHierarchyVersion(concrete._TerminalHierarchyVersion); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(AWS.Cryptography.KeyStoreAdmin.Mutations value)
    {
      value.Validate();
      string var_terminalKmsArn = value.IsSetTerminalKmsArn() ? value.TerminalKmsArn : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_terminalEncryptionContext = value.IsSetTerminalEncryptionContext() ? value.TerminalEncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      AWS.Cryptography.KeyStore.HierarchyVersion var_terminalHierarchyVersion = value.IsSetTerminalHierarchyVersion() ? value.TerminalHierarchyVersion : (AWS.Cryptography.KeyStore.HierarchyVersion)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Mutations(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(var_terminalKmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(var_terminalEncryptionContext), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M24_TerminalHierarchyVersion(var_terminalHierarchyVersion));
    }
    public static bool FromDafny_N6_smithy__N3_api__S7_Boolean(bool value)
    {
      return value;
    }
    public static bool ToDafny_N6_smithy__N3_api__S7_Boolean(bool value)
    {
      return value;
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.AwsKms concrete = (software.amazon.cryptography.keystore.internaldafny.types.AwsKms)value; AWS.Cryptography.KeyStore.AwsKms converted = new AWS.Cryptography.KeyStore.AwsKms(); if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(concrete._grantTokens);
      if (concrete._kmsClient.is_Some) converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(concrete._kmsClient); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(AWS.Cryptography.KeyStore.AwsKms value)
    {
      value.Validate();
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      Amazon.KeyManagementService.IAmazonKeyManagementService var_kmsClient = value.IsSetKmsClient() ? value.KmsClient : (Amazon.KeyManagementService.IAmazonKeyManagementService)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.AwsKms(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(var_grantTokens), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(var_kmsClient));
    }
    public static AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt(software.amazon.cryptography.keystoreadmin.internaldafny.types._IAwsKmsDecryptEncrypt value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.AwsKmsDecryptEncrypt concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.AwsKmsDecryptEncrypt)value; AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt converted = new AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt(); if (concrete._decrypt.is_Some) converted.Decrypt = (AWS.Cryptography.KeyStore.AwsKms)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_decrypt(concrete._decrypt);
      if (concrete._encrypt.is_Some) converted.Encrypt = (AWS.Cryptography.KeyStore.AwsKms)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_encrypt(concrete._encrypt); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IAwsKmsDecryptEncrypt ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt(AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt value)
    {
      value.Validate();
      AWS.Cryptography.KeyStore.AwsKms var_decrypt = value.IsSetDecrypt() ? value.Decrypt : (AWS.Cryptography.KeyStore.AwsKms)null;
      AWS.Cryptography.KeyStore.AwsKms var_encrypt = value.IsSetEncrypt() ? value.Encrypt : (AWS.Cryptography.KeyStore.AwsKms)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.AwsKmsDecryptEncrypt(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_decrypt(var_decrypt), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_encrypt(var_encrypt));
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(software.amazon.cryptography.keystore.internaldafny.types._IStorage value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.Storage concrete = (software.amazon.cryptography.keystore.internaldafny.types.Storage)value;
      var converted = new AWS.Cryptography.KeyStore.Storage(); if (value.is_ddb)
      {
        converted.Ddb = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(concrete.dtor_ddb);
        return converted;
      }
      if (value.is_custom)
      {
        converted.Custom = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(concrete.dtor_custom);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.Storage state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IStorage ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(AWS.Cryptography.KeyStore.Storage value)
    {
      value.Validate(); if (value.IsSetDdb())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.Storage.create_ddb(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(value.Ddb));
      }
      if (value.IsSetCustom())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.Storage.create_custom(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(value.Custom));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.Storage state");
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsMRKey FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsMRKey value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsMRKey concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsMRKey)value; AWS.Cryptography.KeyStoreAdmin.KmsMRKey converted = new AWS.Cryptography.KeyStoreAdmin.KmsMRKey(); converted.KeyArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_KeyArn(concrete._KeyArn);
      converted.Region = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_Region(concrete._Region); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsMRKey ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey(AWS.Cryptography.KeyStoreAdmin.KmsMRKey value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsMRKey(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_KeyArn(value.KeyArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_Region(value.Region));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationDescription FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDescription value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDescription concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDescription)value; AWS.Cryptography.KeyStoreAdmin.MutationDescription converted = new AWS.Cryptography.KeyStoreAdmin.MutationDescription(); converted.MutationDetails = (AWS.Cryptography.KeyStoreAdmin.MutationDetails)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M15_MutationDetails(concrete._MutationDetails);
      converted.MutationToken = (AWS.Cryptography.KeyStoreAdmin.MutationToken)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M13_MutationToken(concrete._MutationToken); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDescription ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription(AWS.Cryptography.KeyStoreAdmin.MutationDescription value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDescription(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M15_MutationDetails(value.MutationDetails), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M13_MutationToken(value.MutationToken));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricEncryption value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricEncryption concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricEncryption)value; AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption converted = new AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption(); converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_KmsArn(concrete._KmsArn);
      converted.AwsKms = (AWS.Cryptography.KeyStore.AwsKms)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_AwsKms(concrete._AwsKms); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKmsSymmetricEncryption ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption(AWS.Cryptography.KeyStoreAdmin.KmsSymmetricEncryption value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KmsSymmetricEncryption(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_AwsKms(value.AwsKms));
    }
    public static AWS.Cryptography.KeyStoreAdmin.TrustStorage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage)value; AWS.Cryptography.KeyStoreAdmin.TrustStorage converted = new AWS.Cryptography.KeyStoreAdmin.TrustStorage(); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ITrustStorage ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S12_TrustStorage(AWS.Cryptography.KeyStoreAdmin.TrustStorage value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.TrustStorage();
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M4_UUID(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutatedBranchKeyItems__M6_member(AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(value);
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
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M14_TerminalKmsArn(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M25_TerminalEncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static AWS.Cryptography.KeyStore.HierarchyVersion FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M24_TerminalHierarchyVersion(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.HierarchyVersion)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations__M24_TerminalHierarchyVersion(AWS.Cryptography.KeyStore.HierarchyVersion value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion((AWS.Cryptography.KeyStore.HierarchyVersion)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> value)
    {
      return value.is_None ? (Amazon.KeyManagementService.IAmazonKeyManagementService)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference((Amazon.KeyManagementService.IAmazonKeyManagementService)value));
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_decrypt(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.AwsKms)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_decrypt(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms((AWS.Cryptography.KeyStore.AwsKms)value));
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_encrypt(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.AwsKms)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_AwsKmsDecryptEncrypt__M7_encrypt(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IAwsKms>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms((AWS.Cryptography.KeyStore.AwsKms)value));
    }
    public static AWS.Cryptography.KeyStore.DynamoDBTable FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(AWS.Cryptography.KeyStore.DynamoDBTable value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static AWS.Cryptography.KeyStore.IKeyStorageInterface FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(AWS.Cryptography.KeyStore.IKeyStorageInterface value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_KeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_KeyArn(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_Region(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S8_KmsMRKey__M6_Region(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationDetails FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M15_MutationDetails(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDetails value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDetails ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M15_MutationDetails(AWS.Cryptography.KeyStoreAdmin.MutationDetails value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationToken FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M13_MutationToken(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationToken ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationDescription__M13_MutationToken(AWS.Cryptography.KeyStoreAdmin.MutationToken value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S13_MutationToken(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_KmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_KmsArn(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_AwsKms(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KmsSymmetricEncryption__M6_AwsKms(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem)value; AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem converted = new AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem(); converted.ItemType = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(concrete._ItemType);
      converted.Description = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(concrete._Description); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutatedBranchKeyItem ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem(AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutatedBranchKeyItem(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(value.ItemType), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(value.Description));
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
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> value)
    {
      return value.ItemEnumerable.ToDictionary(pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(pair.Car), pair => FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(pair.Cdr));
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(System.Collections.Generic.Dictionary<string, string> value)
    {
      return Dafny.Map<Dafny.ISequence<char>, Dafny.ISequence<char>>.FromCollection(value.Select(pair =>
         new Dafny.Pair<Dafny.ISequence<char>, Dafny.ISequence<char>>(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(pair.Key), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(pair.Value))
     ));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member).ToArray());
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value);
    }
    public static AWS.Cryptography.KeyStore.DynamoDBTable FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable concrete = (software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable)value; AWS.Cryptography.KeyStore.DynamoDBTable converted = new AWS.Cryptography.KeyStore.DynamoDBTable(); converted.DdbTableName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(concrete._ddbTableName);
      if (concrete._ddbClient.is_Some) converted.DdbClient = (Amazon.DynamoDBv2.IAmazonDynamoDB)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(concrete._ddbClient); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(AWS.Cryptography.KeyStore.DynamoDBTable value)
    {
      value.Validate();
      Amazon.DynamoDBv2.IAmazonDynamoDB var_ddbClient = value.IsSetDdbClient() ? value.DdbClient : (Amazon.DynamoDBv2.IAmazonDynamoDB)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.DynamoDBTable(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(value.DdbTableName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(var_ddbClient));
    }
    public static AWS.Cryptography.KeyStore.IKeyStorageInterface FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(AWS.Cryptography.KeyStore.IKeyStorageInterface value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(value);
    }
    public static string FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static string FromDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutationDetails FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDetails value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDetails concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDetails)value; AWS.Cryptography.KeyStoreAdmin.MutationDetails converted = new AWS.Cryptography.KeyStoreAdmin.MutationDetails(); converted.Original = (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Original(concrete._Original);
      converted.Terminal = (AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Terminal(concrete._Terminal);
      converted.Input = (AWS.Cryptography.KeyStoreAdmin.Mutations)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M5_Input(concrete._Input);
      converted.SystemKey = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M9_SystemKey(concrete._SystemKey);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M10_CreateTime(concrete._CreateTime);
      converted.UUID = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M4_UUID(concrete._UUID); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutationDetails ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails(AWS.Cryptography.KeyStoreAdmin.MutationDetails value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutationDetails(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Original(value.Original), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Terminal(value.Terminal), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M5_Input(value.Input), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M9_SystemKey(value.SystemKey), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M10_CreateTime(value.CreateTime), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M4_UUID(value.UUID));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M8_ItemType(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_MutatedBranchKeyItem__M11_Description(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M3_key(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString__M5_value(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M12_ddbTableName(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(value);
    }
    public static Amazon.DynamoDBv2.IAmazonDynamoDB FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> value)
    {
      return value.is_None ? (Amazon.DynamoDBv2.IAmazonDynamoDB)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable__M9_ddbClient(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference((Amazon.DynamoDBv2.IAmazonDynamoDB)value));
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Original(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Original(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Terminal(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M8_Terminal(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.Mutations FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M5_Input(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutations ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M5_Input(AWS.Cryptography.KeyStoreAdmin.Mutations value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S9_Mutations(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M9_SystemKey(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M9_SystemKey(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M4_UUID(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_MutationDetails__M4_UUID(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static Amazon.DynamoDBv2.IAmazonDynamoDB FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value);
    }
    public static software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value);
    }
    public static AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyContext concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyContext)value; AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext converted = new AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext(); converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M6_KmsArn(concrete._KmsArn);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M17_EncryptionContext(concrete._EncryptionContext);
      converted.HierarchyVersion = (AWS.Cryptography.KeyStore.HierarchyVersion)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M16_HierarchyVersion(concrete._HierarchyVersion); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IMutableBranchKeyContext ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext(AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.MutableBranchKeyContext(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M17_EncryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M16_HierarchyVersion(value.HierarchyVersion));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M6_KmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M6_KmsArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M17_EncryptionContext(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static AWS.Cryptography.KeyStore.HierarchyVersion FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M16_HierarchyVersion(software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchyVersion ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_MutableBranchKeyContext__M16_HierarchyVersion(AWS.Cryptography.KeyStore.HierarchyVersion value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_HierarchyVersion(value);
    }
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.keystoreadmin.internaldafny.types._IError value)
    {
      switch (value)
      {
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_AwsCryptographyKeyStore dafnyVal:
          return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyKeyStore
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_AwsCryptographyPrimitives dafnyVal:
          return AWS.Cryptography.Primitives.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyPrimitives
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsDynamodb dafnyVal:
          return Com.Amazonaws.Dynamodb.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsDynamodb
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsKms dafnyVal:
          // MANUAL EDIT KMS -> Kms
          return Com.Amazonaws.Kms.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsKms
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationConflictException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationFromException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationInvalidException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationToException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_MutationVerificationException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnexpectedStateException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_UnsupportedFeatureException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_OpaqueWithText dafnyVal:
          return new OpaqueWithTextError(dafnyVal._obj, dafnyVal._obj.ToString());
        default:
          // The switch MUST be complete for _IError, so `value` MUST NOT be an _IError. (How did you get here?)
          return new OpaqueError();
      }
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IError ToDafny_CommonError(System.Exception value)
    {
      switch (value.GetType().Namespace)
      {
        case "AWS.Cryptography.KeyStore":
          return software.amazon.cryptography.keystoreadmin.internaldafny.types.Error.create_AwsCryptographyKeyStore(
            AWS.Cryptography.KeyStore.TypeConversion.ToDafny_CommonError(value)
          );
        case "Com.Amazonaws.Dynamodb":
          return software.amazon.cryptography.keystoreadmin.internaldafny.types.Error.create_ComAmazonawsDynamodb(
            Com.Amazonaws.Dynamodb.TypeConversion.ToDafny_CommonError(value)
          );
      }
      switch (value)
      {
        case AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationConflictException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S25_MutationConflictException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationFromException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_MutationFromException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationInvalidException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_MutationInvalidException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationToException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_MutationToException(exception);
        case AWS.Cryptography.KeyStoreAdmin.MutationVerificationException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S29_MutationVerificationException(exception);
        case AWS.Cryptography.KeyStoreAdmin.UnexpectedStateException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_UnexpectedStateException(exception);
        case AWS.Cryptography.KeyStoreAdmin.UnsupportedFeatureException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S27_UnsupportedFeatureException(exception);
        case CollectionOfErrors collectionOfErrors:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors(
            Dafny.Sequence<software.amazon.cryptography.keystoreadmin.internaldafny.types._IError>
              .FromArray(
                collectionOfErrors.list.Select
                    (x => TypeConversion.ToDafny_CommonError(x))
                  .ToArray()),
            Dafny.Sequence<char>.FromString(collectionOfErrors.Message)
          );
        // OpaqueError is redundant, but listed for completeness.
        case OpaqueError exception:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(exception);
        case System.Exception exception:
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(exception);
        default:
          // The switch MUST be complete for System.Exception, so `value` MUST NOT be an System.Exception. (How did you get here?)
          return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque(value);
      }
    }
  }
}
