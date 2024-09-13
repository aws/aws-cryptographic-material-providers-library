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
  internal class NativeWrapper_EncryptedKeyStore : software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore
  {
    internal readonly EncryptedKeyStoreBase _impl;
    public NativeWrapper_EncryptedKeyStore(EncryptedKeyStoreBase nativeImpl)
    {
      _impl = nativeImpl;
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetBeacon(software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetBeaconOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetBeacon is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetBeaconInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GetBeaconInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetBeaconOutput nativeOutput = _impl.GetBeacon(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetBeacon returned null, should be {typeof(AWS.Cryptography.KeyStore.GetBeaconOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetBeaconOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetBeacon_k(software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetActiveOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetActive(software.amazon.cryptography.keystore.internaldafny.types._IGetActiveInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetActiveOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetActive is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetActiveInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GetActiveInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetActiveOutput nativeOutput = _impl.GetActive(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetActive returned null, should be {typeof(AWS.Cryptography.KeyStore.GetActiveOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetActiveOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetActiveOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetActiveOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetActiveOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetActive_k(software.amazon.cryptography.keystore.internaldafny.types._IGetActiveInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetVersion(software.amazon.cryptography.keystore.internaldafny.types._IGetVersionInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.GetVersionOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._GetVersion is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.GetVersionInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetVersionInput(input);
      try
      {
        AWS.Cryptography.KeyStore.GetVersionOutput nativeOutput = _impl.GetVersion(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._GetVersion returned null, should be {typeof(AWS.Cryptography.KeyStore.GetVersionOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetVersionOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IGetVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> GetVersion_k(software.amazon.cryptography.keystore.internaldafny.types._IGetVersionInput input)
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteCompleteMutation(software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteCompleteMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteCompleteMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteCompleteMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteCompleteMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteCompleteMutationOutput nativeOutput = _impl.WriteCompleteMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteCompleteMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteCompleteMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S27_WriteCompleteMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteCompleteMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteItemsForInitializeMutation(software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteItemsForInitializeMutation is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S36_WriteItemsForInitializeMutationInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput nativeOutput = _impl.WriteItemsForInitializeMutation(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteItemsForInitializeMutation returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S37_WriteItemsForInitializeMutationOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteItemsForInitializeMutation_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DescribeEncryptedKeyStore(software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._DescribeEncryptedKeyStore is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S30_DescribeEncryptedKeyStoreInput(input);
      try
      {
        AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput nativeOutput = _impl.DescribeEncryptedKeyStore(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._DescribeEncryptedKeyStore returned null, should be {typeof(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S31_DescribeEncryptedKeyStoreOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> DescribeEncryptedKeyStore_k(software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreInput input)
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
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewKey(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteNewKeyOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteNewKey is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteNewKeyInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_WriteNewKeyInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteNewKeyOutput nativeOutput = _impl.WriteNewKey(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteNewKey returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteNewKeyOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_WriteNewKeyOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewKey_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewVersion(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionInput input)
    {
      void validateOutput(AWS.Cryptography.KeyStore.WriteNewVersionOutput nativeOutput)
      {
        try { nativeOutput.Validate(); }
        catch (ArgumentException e)
        {
          var message = $"Output of {_impl}._WriteNewVersion is invalid. {e.Message}";
          throw new KeyStoreException(message);
        }
      }
      AWS.Cryptography.KeyStore.WriteNewVersionInput nativeInput = TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S20_WriteNewVersionInput(input);
      try
      {
        AWS.Cryptography.KeyStore.WriteNewVersionOutput nativeOutput = _impl.WriteNewVersion(nativeInput);
        _ = nativeOutput ?? throw new KeyStoreException($"{_impl}._WriteNewVersion returned null, should be {typeof(AWS.Cryptography.KeyStore.WriteNewVersionOutput)}");
        validateOutput(nativeOutput);
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Success(TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_WriteNewVersionOutput(nativeOutput));
      }
      catch (Exception e)
      {
        return Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError>.create_Failure(TypeConversion.ToDafny_CommonError(e));
      }
    }
    public Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> WriteNewVersion_k(software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionInput input)
    {
      throw new KeyStoreException("Not supported at this time.");
    }
  }
}
