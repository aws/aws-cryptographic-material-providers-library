// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using System.IO;
using System.Collections.Generic;
using AWS.Cryptography.KeyStoreAdmin;
using software.amazon.cryptography.keystoreadmin.internaldafny.types;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KeyStoreAdmin
  {
    private readonly software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient _impl;
    public KeyStoreAdmin(software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient impl)
    {
      this._impl = impl;
    }
    public software.amazon.cryptography.keystoreadmin.internaldafny.types.IKeyStoreAdminClient impl()
    {
      return this._impl;
    }
    public KeyStoreAdmin(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(input);
      var result = software.amazon.cryptography.keystoreadmin.internaldafny.__default.KeyStoreAdmin(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      this._impl = result.dtor_value;
    }
    public AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput CreateKey(AWS.Cryptography.KeyStoreAdmin.CreateKeyInput input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput, software.amazon.cryptography.keystoreadmin.internaldafny.types._IError> result = _impl.CreateKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(result.dtor_value);
    }
    public AWS.Cryptography.KeyStoreAdmin.VersionKeyOutput VersionKey(AWS.Cryptography.KeyStoreAdmin.VersionKeyInput input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyOutput, software.amazon.cryptography.keystoreadmin.internaldafny.types._IError> result = _impl.VersionKey(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S16_VersionKeyOutput(result.dtor_value);
    }
    public AWS.Cryptography.KeyStoreAdmin.InitializeMutationOutput InitializeMutation(AWS.Cryptography.KeyStoreAdmin.InitializeMutationInput input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S23_InitializeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystoreadmin.internaldafny.types._IInitializeMutationOutput, software.amazon.cryptography.keystoreadmin.internaldafny.types._IError> result = _impl.InitializeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S24_InitializeMutationOutput(result.dtor_value);
    }
    public AWS.Cryptography.KeyStoreAdmin.ApplyMutationOutput ApplyMutation(AWS.Cryptography.KeyStoreAdmin.ApplyMutationInput input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_ApplyMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystoreadmin.internaldafny.types._IApplyMutationOutput, software.amazon.cryptography.keystoreadmin.internaldafny.types._IError> result = _impl.ApplyMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_ApplyMutationOutput(result.dtor_value);
    }
    public AWS.Cryptography.KeyStoreAdmin.DescribeMutationOutput DescribeMutation(AWS.Cryptography.KeyStoreAdmin.DescribeMutationInput input)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationInput internalInput = TypeConversion.ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S21_DescribeMutationInput(input);
      Wrappers_Compile._IResult<software.amazon.cryptography.keystoreadmin.internaldafny.types._IDescribeMutationOutput, software.amazon.cryptography.keystoreadmin.internaldafny.types._IError> result = _impl.DescribeMutation(internalInput);
      if (result.is_Failure) throw TypeConversion.FromDafny_CommonError(result.dtor_error);
      return TypeConversion.FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_DescribeMutationOutput(result.dtor_value);
    }
  }
}
