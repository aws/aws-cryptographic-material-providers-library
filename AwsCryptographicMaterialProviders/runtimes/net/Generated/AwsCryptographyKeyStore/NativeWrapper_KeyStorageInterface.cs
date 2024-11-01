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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutation(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetMutationOutput nativeOutput = _impl.GetMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.GetMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IGetMutationInput input)
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteAtomicMutation(software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteAtomicMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteAtomicMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteAtomicMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteAtomicMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteAtomicMutationOutput nativeOutput = _impl.WriteAtomicMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteAtomicMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteAtomicMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteAtomicMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteAtomicMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteAtomicMutationInput input)
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteMutationIndex(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteMutationIndexOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteMutationIndex is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteMutationIndexInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteMutationIndexInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteMutationIndexOutput nativeOutput = _impl.WriteMutationIndex(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteMutationIndex returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteMutationIndexOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteMutationIndexOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteMutationIndex_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteMutationIndexInput input)
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DeleteMutation(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.DeleteMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._DeleteMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.DeleteMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S19_DeleteMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.DeleteMutationOutput nativeOutput = _impl.DeleteMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._DeleteMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.DeleteMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_DeleteMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DeleteMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IDeleteMutationInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
  }
}
