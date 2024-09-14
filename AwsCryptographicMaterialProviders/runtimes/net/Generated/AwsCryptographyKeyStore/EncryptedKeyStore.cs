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
  internal class EncryptedKeyStore : EncryptedKeyStoreBase
  {
    internal readonly software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore _impl;
    internal EncryptedKeyStore(software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore impl) { this._impl = impl; }
    protected override AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput _WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S25_WriteMutatedVersionsInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteMutatedVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteMutatedVersions(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteMutatedVersionsOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetBeaconOutput _GetBeacon(AWS.Cryptography.KeyStore.GetBeaconInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GetBeaconInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetBeaconOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetBeacon(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetBeaconOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetActiveOutput _GetActive(AWS.Cryptography.KeyStore.GetActiveInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetActiveInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S14_GetActiveInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetActiveOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetActive(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetActiveOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetVersionOutput _GetVersion(AWS.Cryptography.KeyStore.GetVersionInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetVersionInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S15_GetVersionInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetVersion(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S16_GetVersionOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput _GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetItemsForInitializeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetItemsForInitializeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S35_GetItemsForInitializeMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteCompleteMutationOutput _WriteCompleteMutation(AWS.Cryptography.KeyStore.WriteCompleteMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_WriteCompleteMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteCompleteMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteCompleteMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_WriteCompleteMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput _WriteItemsForInitializeMutation(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S36_WriteItemsForInitializeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteItemsForInitializeMutationOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteItemsForInitializeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S37_WriteItemsForInitializeMutationOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput _DescribeEncryptedKeyStore(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S30_DescribeEncryptedKeyStoreInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IDescribeEncryptedKeyStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.DescribeEncryptedKeyStore(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S31_DescribeEncryptedKeyStoreOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.QueryForVersionsOutput _QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S21_QueryForVersionsInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IQueryForVersionsOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.QueryForVersions(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S22_QueryForVersionsOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteNewKeyOutput _WriteNewKey(AWS.Cryptography.KeyStore.WriteNewKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S16_WriteNewKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_WriteNewKeyOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteNewVersionOutput _WriteNewVersion(AWS.Cryptography.KeyStore.WriteNewVersionInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S20_WriteNewVersionInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewVersion(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S21_WriteNewVersionOutput(result.dtor_value);
    }
  }
}
