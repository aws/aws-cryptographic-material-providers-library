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
    protected override AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreOutput _WriteNewBranchKeyVersionToKeystore(AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewBranchKeyVersionToKeystoreInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S39_WriteNewBranchKeyVersionToKeystoreInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewBranchKeyVersionToKeystoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewBranchKeyVersionToKeystore(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S40_WriteNewBranchKeyVersionToKeystoreOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput _GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S32_GetEncryptedActiveBranchKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedActiveBranchKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedActiveBranchKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedActiveBranchKeyOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetTableNameOutput _GetTableName(AWS.Cryptography.KeyStore.GetTableNameInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetTableNameInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_GetTableNameInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetTableNameOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetTableName(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S18_GetTableNameOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.WriteNewKeyToStoreOutput _WriteNewKeyToStore(AWS.Cryptography.KeyStore.WriteNewKeyToStoreInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyToStoreInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S23_WriteNewKeyToStoreInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IWriteNewKeyToStoreOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.WriteNewKeyToStore(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S24_WriteNewKeyToStoreOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput _GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S33_GetEncryptedBranchKeyVersionInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBranchKeyVersionOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedBranchKeyVersion(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S34_GetEncryptedBranchKeyVersionOutput(result.dtor_value);
    }
    protected override AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput _GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input)
    {
      software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_GetEncryptedBeaconKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystore.internaldafny.types._IGetEncryptedBeaconKeyOutput, software.amazon.cryptography.keystore.internaldafny.types._IError> result = this._impl.GetEncryptedBeaconKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S27_GetEncryptedBeaconKeyOutput(result.dtor_value);
    }
  }
}
