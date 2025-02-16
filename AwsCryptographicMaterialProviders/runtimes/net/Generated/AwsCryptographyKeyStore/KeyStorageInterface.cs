// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using System.IO;
using System.Collections.Generic;
using AWS.Cryptography.KeyStore;
using software.amazon.cryptography.keystore.internaldafny.types;
namespace AWS.Cryptography.KeyStore
{
  internal class KeyStorageInterface : KeyStorageInterfaceBase
  {
    internal readonly software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface _impl;
    internal KeyStorageInterface(software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface impl) { this._impl = impl; }
    protected override AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput _WriteNewEncryptedBranchKey(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewEncryptedBranchKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_WriteNewEncryptedBranchKeyOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetMutationOutput _GetMutation(AWS.Cryptography.KeyStore.GetMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput _GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetItemsForInitializeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput _GetKeyStorageInfo(AWS.Cryptography.KeyStore.GetKeyStorageInfoInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_GetKeyStorageInfoInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetKeyStorageInfo(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput _GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedBranchKeyVersion(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteAtomicMutationOutput _WriteAtomicMutation(AWS.Cryptography.KeyStore.WriteAtomicMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteAtomicMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteAtomicMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput _GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedBeaconKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput _GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedActiveBranchKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput _WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteMutatedVersions(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteMutatedVersionsOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteInitializeMutationOutput _WriteInitializeMutation(AWS.Cryptography.KeyStore.WriteInitializeMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteInitializeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S29_WriteInitializeMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput _WriteNewEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewEncryptedBranchKeyVersion(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S39_WriteNewEncryptedBranchKeyVersionOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteMutationIndexOutput _WriteMutationIndex(AWS.Cryptography.KeyStore.WriteMutationIndexInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteMutationIndex(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteMutationIndexOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.QueryForVersionsOutput _QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.QueryForVersions(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.DeleteMutationOutput _DeleteMutation(AWS.Cryptography.KeyStore.DeleteMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.DeleteMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_DeleteMutationOutput(result.dtor_value);
    }
  }
}
