// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.KeyStore
{
  public static class TypeConversion
  {
    private const string ISO8601DateFormat = "yyyy-MM-dd\\THH:mm:ss.fff\\Z";

    private const string ISO8601DateFormatNoMS = "yyyy-MM-dd\\THH:mm:ss\\Z";

    public static AWS.Cryptography.KeyStore.AlreadyExistsConditionFailed FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed(software.amazon.cryptography.keystore.internaldafny.types.Error_AlreadyExistsConditionFailed value)
    {
      return new AWS.Cryptography.KeyStore.AlreadyExistsConditionFailed(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_AlreadyExistsConditionFailed ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed(AWS.Cryptography.KeyStore.AlreadyExistsConditionFailed value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_AlreadyExistsConditionFailed(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.BranchKeyCiphertextException FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException(software.amazon.cryptography.keystore.internaldafny.types.Error_BranchKeyCiphertextException value)
    {
      return new AWS.Cryptography.KeyStore.BranchKeyCiphertextException(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_BranchKeyCiphertextException ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException(AWS.Cryptography.KeyStore.BranchKeyCiphertextException value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_BranchKeyCiphertextException(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.CreateKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput(software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput)value; AWS.Cryptography.KeyStore.CreateKeyInput converted = new AWS.Cryptography.KeyStore.CreateKeyInput(); if (concrete._branchKeyIdentifier.is_Some) converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier);
      if (concrete._encryptionContext.is_Some) converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M17_encryptionContext(concrete._encryptionContext); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput(AWS.Cryptography.KeyStore.CreateKeyInput value)
    {
      value.Validate();
      string var_branchKeyIdentifier = value.IsSetBranchKeyIdentifier() ? value.BranchKeyIdentifier : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_encryptionContext = value.IsSetEncryptionContext() ? value.EncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.CreateKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M19_branchKeyIdentifier(var_branchKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M17_encryptionContext(var_encryptionContext));
    }
    public static AWS.Cryptography.KeyStore.CreateKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput)value; AWS.Cryptography.KeyStore.CreateKeyOutput converted = new AWS.Cryptography.KeyStore.CreateKeyOutput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput(AWS.Cryptography.KeyStore.CreateKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.CreateKeyOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput__M19_branchKeyIdentifier(value.BranchKeyIdentifier));
    }
    public static AWS.Cryptography.KeyStore.CreateKeyStoreInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_CreateKeyStoreInput(software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyStoreInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput)value; AWS.Cryptography.KeyStore.CreateKeyStoreInput converted = new AWS.Cryptography.KeyStore.CreateKeyStoreInput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyStoreInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_CreateKeyStoreInput(AWS.Cryptography.KeyStore.CreateKeyStoreInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreInput();
    }
    public static AWS.Cryptography.KeyStore.CreateKeyStoreOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput(software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyStoreOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput)value; AWS.Cryptography.KeyStore.CreateKeyStoreOutput converted = new AWS.Cryptography.KeyStore.CreateKeyStoreOutput(); converted.TableArn = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput__M8_tableArn(concrete._tableArn); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._ICreateKeyStoreOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput(AWS.Cryptography.KeyStore.CreateKeyStoreOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.CreateKeyStoreOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput__M8_tableArn(value.TableArn));
    }
    public static AWS.Cryptography.KeyStore.DeleteMutationInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput)value; AWS.Cryptography.KeyStore.DeleteMutationInput converted = new AWS.Cryptography.KeyStore.DeleteMutationInput(); converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput__M18_MutationCommitment(concrete._MutationCommitment); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput(AWS.Cryptography.KeyStore.DeleteMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput__M18_MutationCommitment(value.MutationCommitment));
    }
    public static AWS.Cryptography.KeyStore.DeleteMutationOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_DeleteMutationOutput(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput)value; AWS.Cryptography.KeyStore.DeleteMutationOutput converted = new AWS.Cryptography.KeyStore.DeleteMutationOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_DeleteMutationOutput(AWS.Cryptography.KeyStore.DeleteMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.DeleteMutationOutput();
    }
    public static AWS.Cryptography.KeyStore.GetActiveBranchKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IGetActiveBranchKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput)value; AWS.Cryptography.KeyStore.GetActiveBranchKeyInput converted = new AWS.Cryptography.KeyStore.GetActiveBranchKeyInput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetActiveBranchKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput(AWS.Cryptography.KeyStore.GetActiveBranchKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput__M19_branchKeyIdentifier(value.BranchKeyIdentifier));
    }
    public static AWS.Cryptography.KeyStore.GetActiveBranchKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetActiveBranchKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput)value; AWS.Cryptography.KeyStore.GetActiveBranchKeyOutput converted = new AWS.Cryptography.KeyStore.GetActiveBranchKeyOutput(); converted.BranchKeyMaterials = (AWS.Cryptography.KeyStore.BranchKeyMaterials)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput__M18_branchKeyMaterials(concrete._branchKeyMaterials); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetActiveBranchKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput(AWS.Cryptography.KeyStore.GetActiveBranchKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetActiveBranchKeyOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput__M18_branchKeyMaterials(value.BranchKeyMaterials));
    }
    public static AWS.Cryptography.KeyStore.GetBeaconKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput)value; AWS.Cryptography.KeyStore.GetBeaconKeyInput converted = new AWS.Cryptography.KeyStore.GetBeaconKeyInput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput(AWS.Cryptography.KeyStore.GetBeaconKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput__M19_branchKeyIdentifier(value.BranchKeyIdentifier));
    }
    public static AWS.Cryptography.KeyStore.GetBeaconKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput)value; AWS.Cryptography.KeyStore.GetBeaconKeyOutput converted = new AWS.Cryptography.KeyStore.GetBeaconKeyOutput(); converted.BeaconKeyMaterials = (AWS.Cryptography.KeyStore.BeaconKeyMaterials)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput__M18_beaconKeyMaterials(concrete._beaconKeyMaterials); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput(AWS.Cryptography.KeyStore.GetBeaconKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetBeaconKeyOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput__M18_beaconKeyMaterials(value.BeaconKeyMaterials));
    }
    public static AWS.Cryptography.KeyStore.GetBranchKeyVersionInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput(software.amazon.cryptography.keystore.internaldafny.types._IGetBranchKeyVersionInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput)value; AWS.Cryptography.KeyStore.GetBranchKeyVersionInput converted = new AWS.Cryptography.KeyStore.GetBranchKeyVersionInput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier);
      converted.BranchKeyVersion = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M16_branchKeyVersion(concrete._branchKeyVersion); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetBranchKeyVersionInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput(AWS.Cryptography.KeyStore.GetBranchKeyVersionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M19_branchKeyIdentifier(value.BranchKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M16_branchKeyVersion(value.BranchKeyVersion));
    }
    public static AWS.Cryptography.KeyStore.GetBranchKeyVersionOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetBranchKeyVersionOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput)value; AWS.Cryptography.KeyStore.GetBranchKeyVersionOutput converted = new AWS.Cryptography.KeyStore.GetBranchKeyVersionOutput(); converted.BranchKeyMaterials = (AWS.Cryptography.KeyStore.BranchKeyMaterials)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput__M18_branchKeyMaterials(concrete._branchKeyMaterials); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetBranchKeyVersionOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput(AWS.Cryptography.KeyStore.GetBranchKeyVersionOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetBranchKeyVersionOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput__M18_branchKeyMaterials(value.BranchKeyMaterials));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput)value; AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput converted = new AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput)value; AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput converted = new AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput(); converted.Item = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput__M4_Item(concrete._Item); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedActiveBranchKeyOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput__M4_Item(value.Item));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput)value; AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput converted = new AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput)value; AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput converted = new AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput(); converted.Item = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput__M4_Item(concrete._Item); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBeaconKeyOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput__M4_Item(value.Item));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput)value; AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput converted = new AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M10_Identifier(concrete._Identifier);
      converted.Version = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M7_Version(concrete._Version); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M7_Version(value.Version));
    }
    public static AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput)value; AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput converted = new AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput(); converted.Item = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput__M4_Item(concrete._Item); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetEncryptedBranchKeyVersionOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput__M4_Item(value.Item));
    }
    public static AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput(software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput)value; AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput converted = new AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput)value; AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput converted = new AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput(); converted.ActiveItem = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_ActiveItem(concrete._ActiveItem);
      converted.BeaconItem = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_BeaconItem(concrete._BeaconItem);
      if (concrete._MutationCommitment.is_Some) converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M18_MutationCommitment(concrete._MutationCommitment);
      if (concrete._MutationIndex.is_Some) converted.MutationIndex = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M13_MutationIndex(concrete._MutationIndex); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStore.MutationCommitment var_mutationCommitment = value.IsSetMutationCommitment() ? value.MutationCommitment : (AWS.Cryptography.KeyStore.MutationCommitment)null;
      AWS.Cryptography.KeyStore.MutationIndex var_mutationIndex = value.IsSetMutationIndex() ? value.MutationIndex : (AWS.Cryptography.KeyStore.MutationIndex)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.GetItemsForInitializeMutationOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_ActiveItem(value.ActiveItem), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_BeaconItem(value.BeaconItem), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M18_MutationCommitment(var_mutationCommitment), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M13_MutationIndex(var_mutationIndex));
    }
    public static AWS.Cryptography.KeyStore.GetKeyStorageInfoInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_GetKeyStorageInfoInput(software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput)value; AWS.Cryptography.KeyStore.GetKeyStorageInfoInput converted = new AWS.Cryptography.KeyStore.GetKeyStorageInfoInput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_GetKeyStorageInfoInput(AWS.Cryptography.KeyStore.GetKeyStorageInfoInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoInput();
    }
    public static AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput)value; AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput converted = new AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput(); converted.Name = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M4_Name(concrete._Name);
      converted.LogicalName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M11_LogicalName(concrete._LogicalName); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput(AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetKeyStorageInfoOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M4_Name(value.Name), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M11_LogicalName(value.LogicalName));
    }
    public static AWS.Cryptography.KeyStore.GetKeyStoreInfoOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStoreInfoOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput)value; AWS.Cryptography.KeyStore.GetKeyStoreInfoOutput converted = new AWS.Cryptography.KeyStore.GetKeyStoreInfoOutput(); converted.KeyStoreId = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M10_keyStoreId(concrete._keyStoreId);
      converted.KeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M12_keyStoreName(concrete._keyStoreName);
      converted.LogicalKeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M19_logicalKeyStoreName(concrete._logicalKeyStoreName);
      converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M11_grantTokens(concrete._grantTokens);
      converted.KmsConfiguration = (AWS.Cryptography.KeyStore.KMSConfiguration)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M16_kmsConfiguration(concrete._kmsConfiguration); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStoreInfoOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput(AWS.Cryptography.KeyStore.GetKeyStoreInfoOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M10_keyStoreId(value.KeyStoreId), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M12_keyStoreName(value.KeyStoreName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M19_logicalKeyStoreName(value.LogicalKeyStoreName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M11_grantTokens(value.GrantTokens), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M16_kmsConfiguration(value.KmsConfiguration));
    }
    public static AWS.Cryptography.KeyStore.GetMutationInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput)value; AWS.Cryptography.KeyStore.GetMutationInput converted = new AWS.Cryptography.KeyStore.GetMutationInput(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput__M10_Identifier(concrete._Identifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetMutationInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput(AWS.Cryptography.KeyStore.GetMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.GetMutationInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput__M10_Identifier(value.Identifier));
    }
    public static AWS.Cryptography.KeyStore.GetMutationOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput)value; AWS.Cryptography.KeyStore.GetMutationOutput converted = new AWS.Cryptography.KeyStore.GetMutationOutput(); if (concrete._MutationCommitment.is_Some) converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M18_MutationCommitment(concrete._MutationCommitment);
      if (concrete._MutationIndex.is_Some) converted.MutationIndex = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M13_MutationIndex(concrete._MutationIndex); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput(AWS.Cryptography.KeyStore.GetMutationOutput value)
    {
      value.Validate();
      AWS.Cryptography.KeyStore.MutationCommitment var_mutationCommitment = value.IsSetMutationCommitment() ? value.MutationCommitment : (AWS.Cryptography.KeyStore.MutationCommitment)null;
      AWS.Cryptography.KeyStore.MutationIndex var_mutationIndex = value.IsSetMutationIndex() ? value.MutationIndex : (AWS.Cryptography.KeyStore.MutationIndex)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.GetMutationOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M18_MutationCommitment(var_mutationCommitment), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M13_MutationIndex(var_mutationIndex));
    }
    public static AWS.Cryptography.KeyStore.HierarchicalKeyType FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType(software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalKeyType value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType concrete = (software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType)value;
      var converted = new AWS.Cryptography.KeyStore.HierarchicalKeyType(); if (value.is_ActiveHierarchicalSymmetricVersion)
      {
        converted.ActiveHierarchicalSymmetricVersion = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M34_ActiveHierarchicalSymmetricVersion(concrete.dtor_ActiveHierarchicalSymmetricVersion);
        return converted;
      }
      if (value.is_HierarchicalSymmetricVersion)
      {
        converted.HierarchicalSymmetricVersion = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M28_HierarchicalSymmetricVersion(concrete.dtor_HierarchicalSymmetricVersion);
        return converted;
      }
      if (value.is_ActiveHierarchicalSymmetricBeacon)
      {
        converted.ActiveHierarchicalSymmetricBeacon = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M33_ActiveHierarchicalSymmetricBeacon(concrete.dtor_ActiveHierarchicalSymmetricBeacon);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.HierarchicalKeyType state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalKeyType ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType(AWS.Cryptography.KeyStore.HierarchicalKeyType value)
    {
      value.Validate(); if (value.IsSetActiveHierarchicalSymmetricVersion())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType.create_ActiveHierarchicalSymmetricVersion(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M34_ActiveHierarchicalSymmetricVersion(value.ActiveHierarchicalSymmetricVersion));
      }
      if (value.IsSetHierarchicalSymmetricVersion())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType.create_HierarchicalSymmetricVersion(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M28_HierarchicalSymmetricVersion(value.HierarchicalSymmetricVersion));
      }
      if (value.IsSetActiveHierarchicalSymmetricBeacon())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.HierarchicalKeyType.create_ActiveHierarchicalSymmetricBeacon(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M33_ActiveHierarchicalSymmetricBeacon(value.ActiveHierarchicalSymmetricBeacon));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.HierarchicalKeyType state");
    }
    public static AWS.Cryptography.KeyStore.KeyManagement FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement(software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.KeyManagement concrete = (software.amazon.cryptography.keystore.internaldafny.types.KeyManagement)value;
      var converted = new AWS.Cryptography.KeyStore.KeyManagement(); if (value.is_kms)
      {
        converted.Kms = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement__M3_kms(concrete.dtor_kms);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.KeyManagement state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement(AWS.Cryptography.KeyStore.KeyManagement value)
    {
      value.Validate(); if (value.IsSetKms())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.KeyManagement.create(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement__M3_kms(value.Kms));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.KeyManagement state");
    }
    public static AWS.Cryptography.KeyStore.KeyManagementException FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException(software.amazon.cryptography.keystore.internaldafny.types.Error_KeyManagementException value)
    {
      return new AWS.Cryptography.KeyStore.KeyManagementException(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_KeyManagementException ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException(AWS.Cryptography.KeyStore.KeyManagementException value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_KeyManagementException(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.KeyStorageException FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException(software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStorageException value)
    {
      return new AWS.Cryptography.KeyStore.KeyStorageException(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStorageException ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException(AWS.Cryptography.KeyStore.KeyStorageException value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStorageException(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.KeyStoreConfig FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig(software.amazon.cryptography.keystore.internaldafny.types._IKeyStoreConfig value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig concrete = (software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig)value; AWS.Cryptography.KeyStore.KeyStoreConfig converted = new AWS.Cryptography.KeyStore.KeyStoreConfig(); converted.KmsConfiguration = (AWS.Cryptography.KeyStore.KMSConfiguration)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M16_kmsConfiguration(concrete._kmsConfiguration);
      converted.LogicalKeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M19_logicalKeyStoreName(concrete._logicalKeyStoreName);
      if (concrete._keyManagement.is_Some) converted.KeyManagement = (AWS.Cryptography.KeyStore.KeyManagement)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M13_keyManagement(concrete._keyManagement);
      if (concrete._ddbTableName.is_Some) converted.DdbTableName = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M12_ddbTableName(concrete._ddbTableName);
      if (concrete._id.is_Some) converted.Id = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M2_id(concrete._id);
      if (concrete._grantTokens.is_Some) converted.GrantTokens = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M11_grantTokens(concrete._grantTokens);
      if (concrete._storage.is_Some) converted.Storage = (AWS.Cryptography.KeyStore.Storage)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M7_storage(concrete._storage);
      if (concrete._ddbClient.is_Some) converted.DdbClient = (Amazon.DynamoDBv2.IAmazonDynamoDB)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_ddbClient(concrete._ddbClient);
      if (concrete._kmsClient.is_Some) converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_kmsClient(concrete._kmsClient); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IKeyStoreConfig ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig(AWS.Cryptography.KeyStore.KeyStoreConfig value)
    {
      value.Validate();
      AWS.Cryptography.KeyStore.KeyManagement var_keyManagement = value.IsSetKeyManagement() ? value.KeyManagement : (AWS.Cryptography.KeyStore.KeyManagement)null;
      string var_ddbTableName = value.IsSetDdbTableName() ? value.DdbTableName : (string)null;
      string var_id = value.IsSetId() ? value.Id : (string)null;
      System.Collections.Generic.List<string> var_grantTokens = value.IsSetGrantTokens() ? value.GrantTokens : (System.Collections.Generic.List<string>)null;
      AWS.Cryptography.KeyStore.Storage var_storage = value.IsSetStorage() ? value.Storage : (AWS.Cryptography.KeyStore.Storage)null;
      Amazon.DynamoDBv2.IAmazonDynamoDB var_ddbClient = value.IsSetDdbClient() ? value.DdbClient : (Amazon.DynamoDBv2.IAmazonDynamoDB)null;
      Amazon.KeyManagementService.IAmazonKeyManagementService var_kmsClient = value.IsSetKmsClient() ? value.KmsClient : (Amazon.KeyManagementService.IAmazonKeyManagementService)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.KeyStoreConfig(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M16_kmsConfiguration(value.KmsConfiguration), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M19_logicalKeyStoreName(value.LogicalKeyStoreName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M13_keyManagement(var_keyManagement), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M12_ddbTableName(var_ddbTableName), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M2_id(var_id), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M11_grantTokens(var_grantTokens), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M7_storage(var_storage), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_ddbClient(var_ddbClient), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_kmsClient(var_kmsClient));
    }
    public static AWS.Cryptography.KeyStore.KeyStoreException FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException(software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException value)
    {
      return new AWS.Cryptography.KeyStore.KeyStoreException(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException(AWS.Cryptography.KeyStore.KeyStoreException value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.KeyStore.KMSConfiguration FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration concrete = (software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration)value;
      var converted = new AWS.Cryptography.KeyStore.KMSConfiguration(); if (value.is_kmsKeyArn)
      {
        converted.KmsKeyArn = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_kmsKeyArn(concrete.dtor_kmsKeyArn);
        return converted;
      }
      if (value.is_kmsMRKeyArn)
      {
        converted.KmsMRKeyArn = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_kmsMRKeyArn(concrete.dtor_kmsMRKeyArn);
        return converted;
      }
      if (value.is_discovery)
      {
        converted.Discovery = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_discovery(concrete.dtor_discovery);
        return converted;
      }
      if (value.is_mrDiscovery)
      {
        converted.MrDiscovery = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_mrDiscovery(concrete.dtor_mrDiscovery);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.KMSConfiguration state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(AWS.Cryptography.KeyStore.KMSConfiguration value)
    {
      value.Validate(); if (value.IsSetKmsKeyArn())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsKeyArn(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_kmsKeyArn(value.KmsKeyArn));
      }
      if (value.IsSetKmsMRKeyArn())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_kmsMRKeyArn(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_kmsMRKeyArn(value.KmsMRKeyArn));
      }
      if (value.IsSetDiscovery())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_discovery(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_discovery(value.Discovery));
      }
      if (value.IsSetMrDiscovery())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.KMSConfiguration.create_mrDiscovery(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_mrDiscovery(value.MrDiscovery));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.KMSConfiguration state");
    }
    public static AWS.Cryptography.KeyStore.MutationCommitmentConditionFailed FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed(software.amazon.cryptography.keystore.internaldafny.types.Error_MutationCommitmentConditionFailed value)
    {
      return new AWS.Cryptography.KeyStore.MutationCommitmentConditionFailed(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_MutationCommitmentConditionFailed ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed(AWS.Cryptography.KeyStore.MutationCommitmentConditionFailed value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_MutationCommitmentConditionFailed(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.NoLongerExistsConditionFailed FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed(software.amazon.cryptography.keystore.internaldafny.types.Error_NoLongerExistsConditionFailed value)
    {
      return new AWS.Cryptography.KeyStore.NoLongerExistsConditionFailed(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_NoLongerExistsConditionFailed ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed(AWS.Cryptography.KeyStore.NoLongerExistsConditionFailed value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_NoLongerExistsConditionFailed(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.OldEncConditionFailed FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed(software.amazon.cryptography.keystore.internaldafny.types.Error_OldEncConditionFailed value)
    {
      return new AWS.Cryptography.KeyStore.OldEncConditionFailed(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_OldEncConditionFailed ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed(AWS.Cryptography.KeyStore.OldEncConditionFailed value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_OldEncConditionFailed(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.QueryForVersionsInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput(software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput)value; AWS.Cryptography.KeyStore.QueryForVersionsInput converted = new AWS.Cryptography.KeyStore.QueryForVersionsInput(); if (concrete._ExclusiveStartKey.is_Some) converted.ExclusiveStartKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M17_ExclusiveStartKey(concrete._ExclusiveStartKey);
      converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M10_Identifier(concrete._Identifier);
      converted.PageSize = (int)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M8_PageSize(concrete._PageSize); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput(AWS.Cryptography.KeyStore.QueryForVersionsInput value)
    {
      value.Validate();
      System.IO.MemoryStream var_exclusiveStartKey = value.IsSetExclusiveStartKey() ? value.ExclusiveStartKey : (System.IO.MemoryStream)null;
      return new software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M17_ExclusiveStartKey(var_exclusiveStartKey), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M8_PageSize(value.PageSize));
    }
    public static AWS.Cryptography.KeyStore.QueryForVersionsOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput(software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput)value; AWS.Cryptography.KeyStore.QueryForVersionsOutput converted = new AWS.Cryptography.KeyStore.QueryForVersionsOutput(); converted.ExclusiveStartKey = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M17_ExclusiveStartKey(concrete._ExclusiveStartKey);
      converted.Items = (System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M5_Items(concrete._Items); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput(AWS.Cryptography.KeyStore.QueryForVersionsOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.QueryForVersionsOutput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M17_ExclusiveStartKey(value.ExclusiveStartKey), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M5_Items(value.Items));
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
    public static AWS.Cryptography.KeyStore.VersionKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IVersionKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput)value; AWS.Cryptography.KeyStore.VersionKeyInput converted = new AWS.Cryptography.KeyStore.VersionKeyInput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IVersionKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput(AWS.Cryptography.KeyStore.VersionKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.VersionKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput__M19_branchKeyIdentifier(value.BranchKeyIdentifier));
    }
    public static AWS.Cryptography.KeyStore.VersionKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_VersionKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IVersionKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput)value; AWS.Cryptography.KeyStore.VersionKeyOutput converted = new AWS.Cryptography.KeyStore.VersionKeyOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IVersionKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_VersionKeyOutput(AWS.Cryptography.KeyStore.VersionKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput();
    }
    public static AWS.Cryptography.KeyStore.VersionRaceException FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException(software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException value)
    {
      return new AWS.Cryptography.KeyStore.VersionRaceException(
      FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException(AWS.Cryptography.KeyStore.VersionRaceException value)
    {

      return new software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException(
      ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException__M7_message(value.Message)
      );
    }
    public static AWS.Cryptography.KeyStore.WriteAtomicMutationInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput)value; AWS.Cryptography.KeyStore.WriteAtomicMutationInput converted = new AWS.Cryptography.KeyStore.WriteAtomicMutationInput(); converted.Active = (AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Active(concrete._Active);
      converted.Version = (AWS.Cryptography.KeyStore.WriteInitializeMutationVersion)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M7_Version(concrete._Version);
      converted.Beacon = (AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Beacon(concrete._Beacon);
      converted.Items = (System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M5_Items(concrete._Items); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput(AWS.Cryptography.KeyStore.WriteAtomicMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Active(value.Active), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M7_Version(value.Version), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Beacon(value.Beacon), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M5_Items(value.Items));
    }
    public static AWS.Cryptography.KeyStore.WriteAtomicMutationOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteAtomicMutationOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput)value; AWS.Cryptography.KeyStore.WriteAtomicMutationOutput converted = new AWS.Cryptography.KeyStore.WriteAtomicMutationOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteAtomicMutationOutput(AWS.Cryptography.KeyStore.WriteAtomicMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteAtomicMutationOutput();
    }
    public static AWS.Cryptography.KeyStore.WriteInitializeMutationInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput)value; AWS.Cryptography.KeyStore.WriteInitializeMutationInput converted = new AWS.Cryptography.KeyStore.WriteInitializeMutationInput(); converted.Active = (AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Active(concrete._Active);
      converted.Version = (AWS.Cryptography.KeyStore.WriteInitializeMutationVersion)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M7_Version(concrete._Version);
      converted.Beacon = (AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Beacon(concrete._Beacon);
      converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M18_MutationCommitment(concrete._MutationCommitment);
      converted.MutationIndex = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M13_MutationIndex(concrete._MutationIndex); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput(AWS.Cryptography.KeyStore.WriteInitializeMutationInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Active(value.Active), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M7_Version(value.Version), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Beacon(value.Beacon), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M18_MutationCommitment(value.MutationCommitment), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M13_MutationIndex(value.MutationIndex));
    }
    public static AWS.Cryptography.KeyStore.WriteInitializeMutationOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_WriteInitializeMutationOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput)value; AWS.Cryptography.KeyStore.WriteInitializeMutationOutput converted = new AWS.Cryptography.KeyStore.WriteInitializeMutationOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_WriteInitializeMutationOutput(AWS.Cryptography.KeyStore.WriteInitializeMutationOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationOutput();
    }
    public static AWS.Cryptography.KeyStore.WriteInitializeMutationVersion FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion)value;
      var converted = new AWS.Cryptography.KeyStore.WriteInitializeMutationVersion(); if (value.is_rotate)
      {
        converted.Rotate = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_rotate(concrete.dtor_rotate);
        return converted;
      }
      if (value.is_mutate)
      {
        converted.Mutate = FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_mutate(concrete.dtor_mutate);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.WriteInitializeMutationVersion state");
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(AWS.Cryptography.KeyStore.WriteInitializeMutationVersion value)
    {
      value.Validate(); if (value.IsSetRotate())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion.create_rotate(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_rotate(value.Rotate));
      }
      if (value.IsSetMutate())
      {
        return software.amazon.cryptography.keystore.internaldafny.types.WriteInitializeMutationVersion.create_mutate(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_mutate(value.Mutate));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.KeyStore.WriteInitializeMutationVersion state");
    }
    public static AWS.Cryptography.KeyStore.WriteMutatedVersionsInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput)value; AWS.Cryptography.KeyStore.WriteMutatedVersionsInput converted = new AWS.Cryptography.KeyStore.WriteMutatedVersionsInput(); converted.Items = (System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M5_Items(concrete._Items);
      converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M18_MutationCommitment(concrete._MutationCommitment);
      converted.MutationIndex = (AWS.Cryptography.KeyStore.OverWriteMutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M13_MutationIndex(concrete._MutationIndex);
      converted.EndMutation = (bool)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M11_EndMutation(concrete._EndMutation); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M5_Items(value.Items), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M18_MutationCommitment(value.MutationCommitment), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M13_MutationIndex(value.MutationIndex), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M11_EndMutation(value.EndMutation));
    }
    public static AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteMutatedVersionsOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput)value; AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput converted = new AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteMutatedVersionsOutput(AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteMutatedVersionsOutput();
    }
    public static AWS.Cryptography.KeyStore.WriteMutationIndexInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput)value; AWS.Cryptography.KeyStore.WriteMutationIndexInput converted = new AWS.Cryptography.KeyStore.WriteMutationIndexInput(); converted.MutationCommitment = (AWS.Cryptography.KeyStore.MutationCommitment)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M18_MutationCommitment(concrete._MutationCommitment);
      converted.MutationIndex = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M13_MutationIndex(concrete._MutationIndex); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput(AWS.Cryptography.KeyStore.WriteMutationIndexInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M18_MutationCommitment(value.MutationCommitment), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M13_MutationIndex(value.MutationIndex));
    }
    public static AWS.Cryptography.KeyStore.WriteMutationIndexOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteMutationIndexOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput)value; AWS.Cryptography.KeyStore.WriteMutationIndexOutput converted = new AWS.Cryptography.KeyStore.WriteMutationIndexOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteMutationIndexOutput(AWS.Cryptography.KeyStore.WriteMutationIndexOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteMutationIndexOutput();
    }
    public static AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput)value; AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput converted = new AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput(); converted.Active = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Active(concrete._Active);
      converted.Version = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M7_Version(concrete._Version);
      converted.Beacon = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Beacon(concrete._Beacon); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Active(value.Active), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M7_Version(value.Version), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Beacon(value.Beacon));
    }
    public static AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_WriteNewEncryptedBranchKeyOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput)value; AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput converted = new AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_WriteNewEncryptedBranchKeyOutput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyOutput();
    }
    public static AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionInput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput)value; AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput converted = new AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput(); converted.Active = (AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M6_Active(concrete._Active);
      converted.Version = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M7_Version(concrete._Version); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionInput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionInput(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M6_Active(value.Active), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M7_Version(value.Version));
    }
    public static AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput FromDafny_N3_aws__N12_cryptography__N8_keyStore__S39_WriteNewEncryptedBranchKeyVersionOutput(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput concrete = (software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput)value; AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput converted = new AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput ToDafny_N3_aws__N12_cryptography__N8_keyStore__S39_WriteNewEncryptedBranchKeyVersionOutput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.WriteNewEncryptedBranchKeyVersionOutput();
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M19_branchKeyIdentifier(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M19_branchKeyIdentifier(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M17_encryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_CreateKeyInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_CreateKeyOutput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput__M8_tableArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S8_TableArn(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_CreateKeyStoreOutput__M8_tableArn(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S8_TableArn(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput__M18_MutationCommitment(software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetActiveBranchKeyInput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.BranchKeyMaterials FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput__M18_branchKeyMaterials(software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetActiveBranchKeyOutput__M18_branchKeyMaterials(AWS.Cryptography.KeyStore.BranchKeyMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetBeaconKeyInput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.BeaconKeyMaterials FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput__M18_beaconKeyMaterials(software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBeaconKeyMaterials ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetBeaconKeyOutput__M18_beaconKeyMaterials(AWS.Cryptography.KeyStore.BeaconKeyMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BeaconKeyMaterials(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M16_branchKeyVersion(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_GetBranchKeyVersionInput__M16_branchKeyVersion(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.BranchKeyMaterials FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput__M18_branchKeyMaterials(software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IBranchKeyMaterials ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_GetBranchKeyVersionOutput__M18_branchKeyMaterials(AWS.Cryptography.KeyStore.BranchKeyMaterials value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_BranchKeyMaterials(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput__M4_Item(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput__M4_Item(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput__M4_Item(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput__M4_Item(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M7_Version(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput__M7_Version(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput__M4_Item(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput__M4_Item(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_ActiveItem(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_ActiveItem(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_BeaconItem(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M10_BeaconItem(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M18_MutationCommitment(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.MutationCommitment)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment((AWS.Cryptography.KeyStore.MutationCommitment)value));
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M13_MutationIndex(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.MutationIndex)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput__M13_MutationIndex(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex((AWS.Cryptography.KeyStore.MutationIndex)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M4_Name(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M4_Name(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M11_LogicalName(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput__M11_LogicalName(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Utf8Bytes(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M10_keyStoreId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M10_keyStoreId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M12_keyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M12_keyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M19_logicalKeyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M19_logicalKeyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M11_grantTokens(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(value);
    }
    public static AWS.Cryptography.KeyStore.KMSConfiguration FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M16_kmsConfiguration(software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetKeyStoreInfoOutput__M16_kmsConfiguration(AWS.Cryptography.KeyStore.KMSConfiguration value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M18_MutationCommitment(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.MutationCommitment)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment((AWS.Cryptography.KeyStore.MutationCommitment)value));
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M13_MutationIndex(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.MutationIndex)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput__M13_MutationIndex(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex((AWS.Cryptography.KeyStore.MutationIndex)value));
    }
    public static AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M34_ActiveHierarchicalSymmetricVersion(software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetric value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetric ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M34_ActiveHierarchicalSymmetricVersion(AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric(value);
    }
    public static AWS.Cryptography.KeyStore.HierarchicalSymmetric FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M28_HierarchicalSymmetricVersion(software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalSymmetric value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalSymmetric ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M28_HierarchicalSymmetricVersion(AWS.Cryptography.KeyStore.HierarchicalSymmetric value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric(value);
    }
    public static AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M33_ActiveHierarchicalSymmetricBeacon(software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetricBeacon value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_ActiveHierarchicalSymmetricBeacon(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetricBeacon ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType__M33_ActiveHierarchicalSymmetricBeacon(AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_ActiveHierarchicalSymmetricBeacon(value);
    }
    public static AWS.Cryptography.KeyStore.AwsKms FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement__M3_kms(software.amazon.cryptography.keystore.internaldafny.types._IAwsKms value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IAwsKms ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement__M3_kms(AWS.Cryptography.KeyStore.AwsKms value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S6_AwsKms(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.KMSConfiguration FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M16_kmsConfiguration(software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IKMSConfiguration ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M16_kmsConfiguration(AWS.Cryptography.KeyStore.KMSConfiguration value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M19_logicalKeyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M19_logicalKeyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.KeyManagement FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M13_keyManagement(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.KeyManagement)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M13_keyManagement(AWS.Cryptography.KeyStore.KeyManagement value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IKeyManagement>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_KeyManagement((AWS.Cryptography.KeyStore.KeyManagement)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M12_ddbTableName(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M12_ddbTableName(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S9_TableName((string)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M2_id(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M2_id(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M11_grantTokens(Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> value)
    {
      return value.is_None ? (System.Collections.Generic.List<string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<Dafny.ISequence<char>>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M11_grantTokens(System.Collections.Generic.List<string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<Dafny.ISequence<char>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList((System.Collections.Generic.List<string>)value));
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M7_storage(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IStorage> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.Storage)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IStorage> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M7_storage(AWS.Cryptography.KeyStore.Storage value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IStorage>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IStorage>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage((AWS.Cryptography.KeyStore.Storage)value));
    }
    public static Amazon.DynamoDBv2.IAmazonDynamoDB FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_ddbClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> value)
    {
      return value.is_None ? (Amazon.DynamoDBv2.IAmazonDynamoDB)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_ddbClient(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference((Amazon.DynamoDBv2.IAmazonDynamoDB)value));
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_kmsClient(Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> value)
    {
      return value.is_None ? (Amazon.KeyManagementService.IAmazonKeyManagementService)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_KeyStoreConfig__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference((Amazon.KeyManagementService.IAmazonKeyManagementService)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_kmsKeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_kmsKeyArn(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_kmsMRKeyArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_kmsMRKeyArn(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(value);
    }
    public static AWS.Cryptography.KeyStore.Discovery FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_discovery(software.amazon.cryptography.keystore.internaldafny.types._IDiscovery value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Discovery(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDiscovery ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M9_discovery(AWS.Cryptography.KeyStore.Discovery value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Discovery(value);
    }
    public static AWS.Cryptography.KeyStore.MRDiscovery FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_mrDiscovery(software.amazon.cryptography.keystore.internaldafny.types._IMRDiscovery value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMRDiscovery ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_KMSConfiguration__M11_mrDiscovery(AWS.Cryptography.KeyStore.MRDiscovery value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M17_ExclusiveStartKey(Wrappers_Compile._IOption<Dafny.ISequence<byte>> value)
    {
      return value.is_None ? (System.IO.MemoryStream)null : FromDafny_N6_smithy__N3_api__S4_Blob(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M17_ExclusiveStartKey(System.IO.MemoryStream value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<byte>>.create_Some(ToDafny_N6_smithy__N3_api__S4_Blob((System.IO.MemoryStream)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static int FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M8_PageSize(int value)
    {
      return FromDafny_N6_smithy__N3_api__S7_Integer(value);
    }
    public static int ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput__M8_PageSize(int value)
    {
      return ToDafny_N6_smithy__N3_api__S7_Integer(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M17_ExclusiveStartKey(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M17_ExclusiveStartKey(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M5_Items(Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput__M5_Items(System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys(value);
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
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_VersionKeyInput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Active(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Active(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.WriteInitializeMutationVersion FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M7_Version(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M7_Version(AWS.Cryptography.KeyStore.WriteInitializeMutationVersion value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Beacon(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M6_Beacon(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M5_Items(Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput__M5_Items(System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Active(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Active(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.WriteInitializeMutationVersion FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M7_Version(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationVersion ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M7_Version(AWS.Cryptography.KeyStore.WriteInitializeMutationVersion value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Beacon(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M6_Beacon(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M18_MutationCommitment(software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M13_MutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput__M13_MutationIndex(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_rotate(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_rotate(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_mutate(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_WriteInitializeMutationVersion__M6_mutate(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M5_Items(Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M5_Items(System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M18_MutationCommitment(software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteMutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M13_MutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteMutationIndex value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M13_MutationIndex(AWS.Cryptography.KeyStore.OverWriteMutationIndex value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex(value);
    }
    public static bool FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M11_EndMutation(bool value)
    {
      return FromDafny_N6_smithy__N3_api__S7_Boolean(value);
    }
    public static bool ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput__M11_EndMutation(bool value)
    {
      return ToDafny_N6_smithy__N3_api__S7_Boolean(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M18_MutationCommitment(software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(value);
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M13_MutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput__M13_MutationIndex(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Active(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Active(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M7_Version(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M7_Version(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Beacon(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput__M6_Beacon(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M6_Active(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M6_Active(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M7_Version(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput__M7_Version(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
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
    public static string FromDafny_N3_com__N9_amazonaws__N8_dynamodb__S8_TableArn(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N8_dynamodb__S8_TableArn(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static AWS.Cryptography.KeyStore.MutationCommitment FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.MutationCommitment concrete = (software.amazon.cryptography.keystore.internaldafny.types.MutationCommitment)value; AWS.Cryptography.KeyStore.MutationCommitment converted = new AWS.Cryptography.KeyStore.MutationCommitment(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_Identifier(concrete._Identifier);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_CreateTime(concrete._CreateTime);
      converted.UUID = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M4_UUID(concrete._UUID);
      converted.Original = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Original(concrete._Original);
      converted.Terminal = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Terminal(concrete._Terminal);
      converted.Input = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M5_Input(concrete._Input);
      converted.CiphertextBlob = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M14_CiphertextBlob(concrete._CiphertextBlob); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationCommitment ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment(AWS.Cryptography.KeyStore.MutationCommitment value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.MutationCommitment(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_CreateTime(value.CreateTime), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M4_UUID(value.UUID), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Original(value.Original), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Terminal(value.Terminal), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M5_Input(value.Input), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M14_CiphertextBlob(value.CiphertextBlob));
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
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey concrete = (software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey)value; AWS.Cryptography.KeyStore.EncryptedHierarchicalKey converted = new AWS.Cryptography.KeyStore.EncryptedHierarchicalKey(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_Identifier(concrete._Identifier);
      converted.Type = (AWS.Cryptography.KeyStore.HierarchicalKeyType)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M4_Type(concrete._Type);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_CreateTime(concrete._CreateTime);
      converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M6_KmsArn(concrete._KmsArn);
      converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M17_EncryptionContext(concrete._EncryptionContext);
      converted.CiphertextBlob = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M14_CiphertextBlob(concrete._CiphertextBlob); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.EncryptedHierarchicalKey(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M4_Type(value.Type), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_CreateTime(value.CreateTime), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M6_KmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M17_EncryptionContext(value.EncryptionContext), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M14_CiphertextBlob(value.CiphertextBlob));
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.MutationIndex concrete = (software.amazon.cryptography.keystore.internaldafny.types.MutationIndex)value; AWS.Cryptography.KeyStore.MutationIndex converted = new AWS.Cryptography.KeyStore.MutationIndex(); converted.Identifier = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_Identifier(concrete._Identifier);
      converted.CreateTime = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_CreateTime(concrete._CreateTime);
      converted.UUID = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M4_UUID(concrete._UUID);
      converted.PageIndex = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M9_PageIndex(concrete._PageIndex);
      converted.LastModifiedTime = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M16_LastModifiedTime(concrete._LastModifiedTime);
      converted.CiphertextBlob = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M14_CiphertextBlob(concrete._CiphertextBlob); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.MutationIndex(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_Identifier(value.Identifier), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_CreateTime(value.CreateTime), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M4_UUID(value.UUID), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M9_PageIndex(value.PageIndex), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M16_LastModifiedTime(value.LastModifiedTime), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M14_CiphertextBlob(value.CiphertextBlob));
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
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member).ToArray());
    }
    public static AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric(software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetric value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetric concrete = (software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetric)value; AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric converted = new AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric(); converted.Version = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric__M7_Version(concrete._Version); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetric ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric(AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetric(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric__M7_Version(value.Version));
    }
    public static AWS.Cryptography.KeyStore.HierarchicalSymmetric FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric(software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalSymmetric value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.HierarchicalSymmetric concrete = (software.amazon.cryptography.keystore.internaldafny.types.HierarchicalSymmetric)value; AWS.Cryptography.KeyStore.HierarchicalSymmetric converted = new AWS.Cryptography.KeyStore.HierarchicalSymmetric(); converted.Version = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric__M7_Version(concrete._Version); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalSymmetric ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric(AWS.Cryptography.KeyStore.HierarchicalSymmetric value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.HierarchicalSymmetric(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric__M7_Version(value.Version));
    }
    public static AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_ActiveHierarchicalSymmetricBeacon(software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetricBeacon value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon concrete = (software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon)value; AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon converted = new AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IActiveHierarchicalSymmetricBeacon ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_ActiveHierarchicalSymmetricBeacon(AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.ActiveHierarchicalSymmetricBeacon();
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
      if (value is Com.Amazonaws.Dynamodb.DynamoDBv2Shim shim) { return shim._impl; }
      throw new System.ArgumentException("Custom implementations of Amazon.DynamoDBv2.IAmazonDynamoDBv2 are not supported yet");
    }
    public static software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_DdbClientReference(Amazon.DynamoDBv2.IAmazonDynamoDB value)
    {
      if (value is Amazon.DynamoDBv2.AmazonDynamoDBClient impl) { return new Com.Amazonaws.Dynamodb.DynamoDBv2Shim(impl); }
      throw new System.ArgumentException("Custom implementations of Amazon.DynamoDBv2.IAmazonDynamoDBv2 are not supported yet");
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      if (value is Com.Amazonaws.Kms.KeyManagementServiceShim shim) { return shim._impl; }
      throw new System.ArgumentException("Custom implementations of Amazon.KeyManagementService.IAmazonKeyManagementService are not supported yet");
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_KmsClientReference(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      if (value is Amazon.KeyManagementService.AmazonKeyManagementServiceClient impl) { return new Com.Amazonaws.Kms.KeyManagementServiceShim(impl); }
      throw new System.ArgumentException("Custom implementations of Amazon.KeyManagementService.IAmazonKeyManagementService are not supported yet");
    }
    public static string FromDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N3_kms__S9_KeyIdType(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static AWS.Cryptography.KeyStore.Discovery FromDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Discovery(software.amazon.cryptography.keystore.internaldafny.types._IDiscovery value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.Discovery concrete = (software.amazon.cryptography.keystore.internaldafny.types.Discovery)value; AWS.Cryptography.KeyStore.Discovery converted = new AWS.Cryptography.KeyStore.Discovery(); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDiscovery ToDafny_N3_aws__N12_cryptography__N8_keyStore__S9_Discovery(AWS.Cryptography.KeyStore.Discovery value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.Discovery();
    }
    public static AWS.Cryptography.KeyStore.MRDiscovery FromDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery(software.amazon.cryptography.keystore.internaldafny.types._IMRDiscovery value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery concrete = (software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery)value; AWS.Cryptography.KeyStore.MRDiscovery converted = new AWS.Cryptography.KeyStore.MRDiscovery(); converted.Region = (string)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery__M6_region(concrete._region); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMRDiscovery ToDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery(AWS.Cryptography.KeyStore.MRDiscovery value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.MRDiscovery(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery__M6_region(value.Region));
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
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys(Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys(System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys__M6_member).ToArray());
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
      if (value is NativeWrapper_KeyStorageInterface nativeWrapper) return nativeWrapper._impl;
      return new KeyStorageInterface(value);

    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_KeyStorageInterfaceReference(AWS.Cryptography.KeyStore.IKeyStorageInterface value)
    {
      switch (value)
      {
        case KeyStorageInterface valueWithImpl:
          return valueWithImpl._impl;
        case KeyStorageInterfaceBase nativeImpl:
          return new NativeWrapper_KeyStorageInterface(nativeImpl);
        default:
          throw new System.ArgumentException(
              "Custom implementations of KeyStorageInterface must extend KeyStorageInterfaceBase.");
      }
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.OverWriteEncryptedHierarchicalKey concrete = (software.amazon.cryptography.keystore.internaldafny.types.OverWriteEncryptedHierarchicalKey)value; AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey converted = new AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey(); converted.Item = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M4_Item(concrete._Item);
      converted.Old = (AWS.Cryptography.KeyStore.EncryptedHierarchicalKey)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M3_Old(concrete._Old); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.OverWriteEncryptedHierarchicalKey(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M4_Item(value.Item), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M3_Old(value.Old));
    }
    public static System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys(System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys__M6_member).ToArray());
    }
    public static AWS.Cryptography.KeyStore.OverWriteMutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteMutationIndex value)
    {
      software.amazon.cryptography.keystore.internaldafny.types.OverWriteMutationIndex concrete = (software.amazon.cryptography.keystore.internaldafny.types.OverWriteMutationIndex)value; AWS.Cryptography.KeyStore.OverWriteMutationIndex converted = new AWS.Cryptography.KeyStore.OverWriteMutationIndex(); converted.Index = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M5_Index(concrete._Index);
      converted.Old = (AWS.Cryptography.KeyStore.MutationIndex)FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M3_Old(concrete._Old); return converted;
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex(AWS.Cryptography.KeyStore.OverWriteMutationIndex value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystore.internaldafny.types.OverWriteMutationIndex(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M5_Index(value.Index), ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M3_Old(value.Old));
    }
    public static bool FromDafny_N6_smithy__N3_api__S7_Boolean(bool value)
    {
      return value;
    }
    public static bool ToDafny_N6_smithy__N3_api__S7_Boolean(bool value)
    {
      return value;
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
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M4_UUID(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M4_UUID(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Original(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Original(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Terminal(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M8_Terminal(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M5_Input(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M5_Input(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M14_CiphertextBlob(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S18_MutationCommitment__M14_CiphertextBlob(System.IO.MemoryStream value)
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
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.HierarchicalKeyType FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M4_Type(software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalKeyType value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IHierarchicalKeyType ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M4_Type(AWS.Cryptography.KeyStore.HierarchicalKeyType value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_HierarchicalKeyType(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M6_KmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M6_KmsArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M17_EncryptionContext(Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static Dafny.IMap<Dafny.ISequence<char>, Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M17_EncryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_EncryptionContextString(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M14_CiphertextBlob(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey__M14_CiphertextBlob(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_Identifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_Identifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_CreateTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M10_CreateTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M4_UUID(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M4_UUID(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M9_PageIndex(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M9_PageIndex(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M16_LastModifiedTime(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M16_LastModifiedTime(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M14_CiphertextBlob(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex__M14_CiphertextBlob(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GrantTokenList__M6_member(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric__M7_Version(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_ActiveHierarchicalSymmetric__M7_Version(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric__M7_Version(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_HierarchicalSymmetric__M7_Version(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
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
    public static string FromDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery__M6_region(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N8_keyStore__S11_MRDiscovery__M6_region(string value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys__M6_member(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_EncryptedHierarchicalKeys__M6_member(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
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
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M4_Item(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M4_Item(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.EncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M3_Old(software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey__M3_Old(AWS.Cryptography.KeyStore.EncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_EncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys__M6_member(software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IOverWriteEncryptedHierarchicalKey ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_OverWriteEncryptedHierarchicalKeys__M6_member(AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_OverWriteEncryptedHierarchicalKey(value);
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M5_Index(software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M5_Index(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static AWS.Cryptography.KeyStore.MutationIndex FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M3_Old(software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IMutationIndex ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_OverWriteMutationIndex__M3_Old(AWS.Cryptography.KeyStore.MutationIndex value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_MutationIndex(value);
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
    public static string FromDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_com__N9_amazonaws__N3_kms__S10_RegionType(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
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
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.keystore.internaldafny.types._IError value)
    {
      switch (value)
      {
        case software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsDynamodb dafnyVal:
          return Com.Amazonaws.Dynamodb.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsDynamodb
          );
        case software.amazon.cryptography.keystore.internaldafny.types.Error_ComAmazonawsKms dafnyVal:
          return Com.Amazonaws.Kms.TypeConversion.FromDafny_CommonError( // Manual edit KMS. -> Kms.
            dafnyVal._ComAmazonawsKms
          );
        case software.amazon.cryptography.keystore.internaldafny.types.Error_AlreadyExistsConditionFailed dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_BranchKeyCiphertextException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_KeyManagementException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStorageException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_KeyStoreException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_MutationCommitmentConditionFailed dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_NoLongerExistsConditionFailed dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_OldEncConditionFailed dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_VersionRaceException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException(dafnyVal);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
        case software.amazon.cryptography.keystore.internaldafny.types.Error_OpaqueWithText dafnyVal:
          return new OpaqueWithTextError(dafnyVal._obj, dafnyVal._obj.ToString());
        default:
          // The switch MUST be complete for _IError, so `value` MUST NOT be an _IError. (How did you get here?)
          return new OpaqueError();
      }
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IError ToDafny_CommonError(System.Exception value)
    {
      switch (value.GetType().Namespace)
      {
        case "Com.Amazonaws.KMS":
          return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsKms(
            Com.Amazonaws.Kms.TypeConversion.ToDafny_CommonError(value) // Manual edit KMS. -> Kms.
          );
        case "Com.Amazonaws.Dynamodb":
          return software.amazon.cryptography.keystore.internaldafny.types.Error.create_ComAmazonawsDynamodb(
            Com.Amazonaws.Dynamodb.TypeConversion.ToDafny_CommonError(value)
          );
      }
      switch (value)
      {
        case AWS.Cryptography.KeyStore.AlreadyExistsConditionFailed exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_AlreadyExistsConditionFailed(exception);
        case AWS.Cryptography.KeyStore.BranchKeyCiphertextException exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_BranchKeyCiphertextException(exception);
        case AWS.Cryptography.KeyStore.KeyManagementException exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_KeyManagementException(exception);
        case AWS.Cryptography.KeyStore.KeyStorageException exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_KeyStorageException(exception);
        case AWS.Cryptography.KeyStore.KeyStoreException exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_KeyStoreException(exception);
        case AWS.Cryptography.KeyStore.MutationCommitmentConditionFailed exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_MutationCommitmentConditionFailed(exception);
        case AWS.Cryptography.KeyStore.NoLongerExistsConditionFailed exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_NoLongerExistsConditionFailed(exception);
        case AWS.Cryptography.KeyStore.OldEncConditionFailed exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_OldEncConditionFailed(exception);
        case AWS.Cryptography.KeyStore.VersionRaceException exception:
          return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_VersionRaceException(exception);
        case CollectionOfErrors collectionOfErrors:
          return new software.amazon.cryptography.keystore.internaldafny.types.Error_CollectionOfErrors(
            Dafny.Sequence<software.amazon.cryptography.keystore.internaldafny.types._IError>
              .FromArray(
                collectionOfErrors.list.Select
                    (x => TypeConversion.ToDafny_CommonError(x))
                  .ToArray()),
            Dafny.Sequence<char>.FromString(collectionOfErrors.Message)
          );
        // OpaqueError is redundant, but listed for completeness.
        case OpaqueError exception:
          return new software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque(exception);
        case System.Exception exception:
          return new software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque(exception);
        default:
          // The switch MUST be complete for System.Exception, so `value` MUST NOT be an System.Exception. (How did you get here?)
          return new software.amazon.cryptography.keystore.internaldafny.types.Error_Opaque(value);
      }
    }
  }
}
