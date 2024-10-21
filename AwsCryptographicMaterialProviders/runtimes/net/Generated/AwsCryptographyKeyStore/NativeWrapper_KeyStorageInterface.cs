// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
// ReSharper disable RedundantUsingDirective
// ReSharper disable RedundantNameQualifier
// ReSharper disable SuggestVarOrType_SimpleTypes
using System;
using _System;
using Wrappers_Compile;

namespace AWS.Cryptography.KeyStore
{
  internal class NativeWrapper_KeyStorageInterface : software.amazon.cryptography.keystore.internaldafny.types.IKeyStorageInterface
  {
    internal readonly KeyStorageInterfaceBase _impl;
    public NativeWrapper_KeyStorageInterface(KeyStorageInterfaceBase nativeImpl)
    {
      _impl = nativeImpl;
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewEncryptedBranchKey(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteNewEncryptedBranchKey is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_WriteNewEncryptedBranchKeyInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput nativeOutput = _impl.WriteNewEncryptedBranchKey(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteNewEncryptedBranchKey returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_WriteNewEncryptedBranchKeyOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewEncryptedBranchKey_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetItemsForInitializeMutation(software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetItemsForInitializeMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput nativeOutput = _impl.GetItemsForInitializeMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetItemsForInitializeMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetItemsForInitializeMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutationLock(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetMutationLockOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetMutationLock is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetMutationLockInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_GetMutationLockInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetMutationLockOutput nativeOutput = _impl.GetMutationLock(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetMutationLock returned null, should be {typeof(AWS.Cryptography.KeyStore.GetMutationLockOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_GetMutationLockOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutationLock_k(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetKeyStorageInfo(software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetKeyStorageInfo is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetKeyStorageInfoInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_GetKeyStorageInfoInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput nativeOutput = _impl.GetKeyStorageInfo(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetKeyStorageInfo returned null, should be {typeof(AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_GetKeyStorageInfoOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetKeyStorageInfo_k(software.amazon.cryptography.keystore.internaldafny.types._IGetKeyStorageInfoInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetEncryptedBranchKeyVersion is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput nativeOutput = _impl.GetEncryptedBranchKeyVersion(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetEncryptedBranchKeyVersion returned null, should be {typeof(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedBranchKeyVersion_k(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DeleteMutationLockAndIndex(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.DeleteMutationLockAndIndexOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._DeleteMutationLockAndIndex is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.DeleteMutationLockAndIndexInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_DeleteMutationLockAndIndexInput(input);
      try
      {
        AWS.Cryptography.KeyStore.DeleteMutationLockAndIndexOutput nativeOutput = _impl.DeleteMutationLockAndIndex(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._DeleteMutationLockAndIndex returned null, should be {typeof(AWS.Cryptography.KeyStore.DeleteMutationLockAndIndexOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_DeleteMutationLockAndIndexOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DeleteMutationLockAndIndex_k(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationLockAndIndexInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedBeaconKey(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetEncryptedBeaconKey is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput nativeOutput = _impl.GetEncryptedBeaconKey(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetEncryptedBeaconKey returned null, should be {typeof(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedBeaconKey_k(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedActiveBranchKey(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetEncryptedActiveBranchKey is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput nativeOutput = _impl.GetEncryptedActiveBranchKey(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetEncryptedActiveBranchKey returned null, should be {typeof(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetEncryptedActiveBranchKey_k(software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteMutatedVersions(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteMutatedVersions is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteMutatedVersionsInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput nativeOutput = _impl.WriteMutatedVersions(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteMutatedVersions returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteMutatedVersionsOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteMutatedVersions_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteInitializeMutation(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteInitializeMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteInitializeMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteInitializeMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_WriteInitializeMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteInitializeMutationOutput nativeOutput = _impl.WriteInitializeMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteInitializeMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteInitializeMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_WriteInitializeMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteInitializeMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteInitializeMutationInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewEncryptedBranchKeyVersion(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteNewEncryptedBranchKeyVersion is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S38_WriteNewEncryptedBranchKeyVersionInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput nativeOutput = _impl.WriteNewEncryptedBranchKeyVersion(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteNewEncryptedBranchKeyVersion returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S39_WriteNewEncryptedBranchKeyVersionOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewEncryptedBranchKeyVersion_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewEncryptedBranchKeyVersionInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutationLockAndIndex(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetMutationLockAndIndexOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetMutationLockAndIndex is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetMutationLockAndIndexInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S28_GetMutationLockAndIndexInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetMutationLockAndIndexOutput nativeOutput = _impl.GetMutationLockAndIndex(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetMutationLockAndIndex returned null, should be {typeof(AWS.Cryptography.KeyStore.GetMutationLockAndIndexOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S29_GetMutationLockAndIndexOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutationLockAndIndex_k(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationLockAndIndexInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> QueryForVersions(software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.QueryForVersionsOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._QueryForVersions is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.QueryForVersionsInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput(input);
      try
      {
        AWS.Cryptography.KeyStore.QueryForVersionsOutput nativeOutput = _impl.QueryForVersions(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._QueryForVersions returned null, should be {typeof(AWS.Cryptography.KeyStore.QueryForVersionsOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> QueryForVersions_k(software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> UpdateMutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.UpdateMutationIndexOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._UpdateMutationIndex is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.UpdateMutationIndexInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_UpdateMutationIndexInput(input);
      try
      {
        AWS.Cryptography.KeyStore.UpdateMutationIndexOutput nativeOutput = _impl.UpdateMutationIndex(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._UpdateMutationIndex returned null, should be {typeof(AWS.Cryptography.KeyStore.UpdateMutationIndexOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_UpdateMutationIndexOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> UpdateMutationIndex_k(software.amazon.cryptography.keystore.internaldafny.types._IUpdateMutationIndexInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
  }
}
