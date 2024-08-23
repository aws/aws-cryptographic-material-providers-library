// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public static class TypeConversion
  {
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyInput(); if (concrete._branchKeyIdentifier.is_Some) converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier);
      if (concrete._encryptionContext.is_Some) converted.EncryptionContext = (System.Collections.Generic.Dictionary<string, string>)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_encryptionContext(concrete._encryptionContext);
      converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_kmsArn(concrete._kmsArn);
      converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M9_kmsClient(concrete._kmsClient); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput(AWS.Cryptography.KeyStoreAdmin.CreateKeyInput value)
    {
      value.Validate();
      string var_branchKeyIdentifier = value.IsSetBranchKeyIdentifier() ? value.BranchKeyIdentifier : (string)null;
      System.Collections.Generic.Dictionary<string, string> var_encryptionContext = value.IsSetEncryptionContext() ? value.EncryptionContext : (System.Collections.Generic.Dictionary<string, string>)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M19_branchKeyIdentifier(var_branchKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_encryptionContext(var_encryptionContext), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_kmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M9_kmsClient(value.KmsClient));
    }
    public static AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput)value; AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput converted = new AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._ICreateKeyOutput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput(AWS.Cryptography.KeyStoreAdmin.CreateKeyOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.CreateKeyOutput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M19_branchKeyIdentifier(value.BranchKeyIdentifier));
    }
    public static AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig)value; AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig converted = new AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig(); converted.LogicalKeyStoreName = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(concrete._logicalKeyStoreName);
      if (concrete._storage.is_Some) converted.Storage = (AWS.Cryptography.KeyStore.Storage)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(concrete._storage); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IKeyStoreAdminConfig ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig(AWS.Cryptography.KeyStoreAdmin.KeyStoreAdminConfig value)
    {
      value.Validate();
      AWS.Cryptography.KeyStore.Storage var_storage = value.IsSetStorage() ? value.Storage : (AWS.Cryptography.KeyStore.Storage)null;
      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.KeyStoreAdminConfig(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(value.LogicalKeyStoreName), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(var_storage));
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
    public static AWS.Cryptography.KeyStoreAdmin.VersionKeyInput FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput value)
    {
      software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput concrete = (software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput)value; AWS.Cryptography.KeyStoreAdmin.VersionKeyInput converted = new AWS.Cryptography.KeyStoreAdmin.VersionKeyInput(); converted.BranchKeyIdentifier = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M19_branchKeyIdentifier(concrete._branchKeyIdentifier);
      converted.KmsArn = (string)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_kmsArn(concrete._kmsArn);
      converted.KmsClient = (Amazon.KeyManagementService.IAmazonKeyManagementService)FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M9_kmsClient(concrete._kmsClient); return converted;
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types._IVersionKeyInput ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput(AWS.Cryptography.KeyStoreAdmin.VersionKeyInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.VersionKeyInput(ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M19_branchKeyIdentifier(value.BranchKeyIdentifier), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_kmsArn(value.KmsArn), ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M9_kmsClient(value.KmsClient));
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
    public static AWS.Cryptography.KeyStoreAdmin.VersionRaceException FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException(software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException value)
    {
      return new AWS.Cryptography.KeyStoreAdmin.VersionRaceException(
      FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException(AWS.Cryptography.KeyStoreAdmin.VersionRaceException value)
    {

      return new software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException(
      ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException__M7_message(value.Message)
      );
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M19_branchKeyIdentifier(Wrappers_Compile._IOption<Dafny.ISequence<char>> value)
    {
      return value.is_None ? (string)null : FromDafny_N6_smithy__N3_api__S6_String(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M19_branchKeyIdentifier(string value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.ISequence<char>>.create_None() : Wrappers_Compile.Option<Dafny.ISequence<char>>.create_Some(ToDafny_N6_smithy__N3_api__S6_String((string)value));
    }
    public static System.Collections.Generic.Dictionary<string, string> FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_encryptionContext(Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> value)
    {
      return value.is_None ? (System.Collections.Generic.Dictionary<string, string>)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext(value.Extract());
    }
    public static Wrappers_Compile._IOption<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M17_encryptionContext(System.Collections.Generic.Dictionary<string, string> value)
    {
      return value == null ? Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_None() : Wrappers_Compile.Option<Dafny.IMap<Dafny.ISequence<byte>, Dafny.ISequence<byte>>>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S17_EncryptionContext((System.Collections.Generic.Dictionary<string, string>)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_kmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M6_kmsArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S14_CreateKeyInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_CreateKeyOutput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M19_logicalKeyStoreName(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.KeyStore.Storage FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IStorage> value)
    {
      return value.is_None ? (AWS.Cryptography.KeyStore.Storage)null : FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.keystore.internaldafny.types._IStorage> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S19_KeyStoreAdminConfig__M7_storage(AWS.Cryptography.KeyStore.Storage value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IStorage>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.keystore.internaldafny.types._IStorage>.create_Some(ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage((AWS.Cryptography.KeyStore.Storage)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M19_branchKeyIdentifier(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M19_branchKeyIdentifier(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_kmsArn(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M6_kmsArn(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M9_kmsClient(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S15_VersionKeyInput__M9_kmsClient(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
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
    public static Amazon.KeyManagementService.IAmazonKeyManagementService FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient value)
    {
      if (value is Com.Amazonaws.Kms.KeyManagementServiceShim shim) { return shim._impl; }
      throw new System.ArgumentException("Custom implementations of Amazon.KeyManagementService.IAmazonKeyManagementService are not supported yet");
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S18_KmsClientReference(Amazon.KeyManagementService.IAmazonKeyManagementService value)
    {
      if (value is Amazon.KeyManagementService.AmazonKeyManagementServiceClient impl) { return new Com.Amazonaws.Kms.KeyManagementServiceShim(impl); }
      throw new System.ArgumentException("Custom implementations of Amazon.KeyManagementService.IAmazonKeyManagementService are not supported yet");
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
    public static AWS.Cryptography.KeyStore.DynamoDBTable FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types._IDynamoDBTable ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M3_ddb(AWS.Cryptography.KeyStore.DynamoDBTable value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S13_DynamoDBTable(value);
    }
    public static AWS.Cryptography.KeyStore.IEncryptedKeyStore FromDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore value)
    {
      return FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore ToDafny_N3_aws__N12_cryptography__N8_keyStore__S7_Storage__M6_custom(AWS.Cryptography.KeyStore.IEncryptedKeyStore value)
    {
      return ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(value);
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
    public static AWS.Cryptography.KeyStore.IEncryptedKeyStore FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(value);
    }
    public static software.amazon.cryptography.keystore.internaldafny.types.IEncryptedKeyStore ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(AWS.Cryptography.KeyStore.IEncryptedKeyStore value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.KeyStore.TypeConversion.ToDafny_N3_aws__N12_cryptography__N8_keyStore__S26_EncryptedKeyStoreReference(value);
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
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.keystoreadmin.internaldafny.types._IError value)
    {
      switch (value)
      {
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_AwsCryptographyKeyStore dafnyVal:
          return AWS.Cryptography.KeyStore.TypeConversion.FromDafny_CommonError(
            dafnyVal._AwsCryptographyKeyStore
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsDynamodb dafnyVal:
          return Com.Amazonaws.Dynamodb.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsDynamodb
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_ComAmazonawsKms dafnyVal:
          return Com.Amazonaws.KMS.TypeConversion.FromDafny_CommonError(
            dafnyVal._ComAmazonawsKms
          );
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_KeyStoreAdminException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S22_KeyStoreAdminException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_VersionRaceException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException(dafnyVal);
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.keystoreadmin.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
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
        case AWS.Cryptography.KeyStoreAdmin.VersionRaceException exception:
          return ToDafny_N3_aws__N12_cryptography__N13_keyStoreAdmin__S20_VersionRaceException(exception);
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
