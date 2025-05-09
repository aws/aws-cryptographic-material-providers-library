// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System.Linq;
using System;
namespace AWS.Cryptography.MaterialProvidersTestVectorKeys
{
  public static class TypeConversion
  {
    private const string ISO8601DateFormat = "yyyy-MM-dd\\THH:mm:ss.fff\\Z";

    private const string ISO8601DateFormatNoMS = "yyyy-MM-dd\\THH:mm:ss\\Z";

    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_CmmOperation(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ICmmOperation value)
    {
      if (value.is_ENCRYPT) return AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation.ENCRYPT;
      if (value.is_DECRYPT) return AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation.DECRYPT;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation value");
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ICmmOperation ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_CmmOperation(AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation value)
    {
      if (AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation.ENCRYPT.Equals(value)) return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.CmmOperation.create_ENCRYPT();
      if (AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation.DECRYPT.Equals(value)) return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.CmmOperation.create_DECRYPT();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation value");
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput__M3_cmm(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput__M3_cmm(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionInput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IGetKeyDescriptionInput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionInput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionInput(); converted.Json = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput__M4_json(concrete._json); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IGetKeyDescriptionInput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput(AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionInput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput__M4_json(value.Json));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionOutput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IGetKeyDescriptionOutput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionOutput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionOutput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionOutput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionOutput(); converted.KeyDescription = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput__M14_keyDescription(concrete._keyDescription); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IGetKeyDescriptionOutput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput(AWS.Cryptography.MaterialProvidersTestVectorKeys.GetKeyDescriptionOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionOutput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput__M14_keyDescription(value.KeyDescription));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)value;
      var converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription(); if (value.is_Kms)
      {
        converted.Kms = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_Kms(concrete.dtor_Kms);
        return converted;
      }
      if (value.is_KmsMrk)
      {
        converted.KmsMrk = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsMrk(concrete.dtor_KmsMrk);
        return converted;
      }
      if (value.is_KmsMrkDiscovery)
      {
        converted.KmsMrkDiscovery = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M15_KmsMrkDiscovery(concrete.dtor_KmsMrkDiscovery);
        return converted;
      }
      if (value.is_RSA)
      {
        converted.RSA = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_RSA(concrete.dtor_RSA);
        return converted;
      }
      if (value.is_AES)
      {
        converted.AES = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_AES(concrete.dtor_AES);
        return converted;
      }
      if (value.is_ECDH)
      {
        converted.ECDH = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M4_ECDH(concrete.dtor_ECDH);
        return converted;
      }
      if (value.is_Static)
      {
        converted.Static = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_Static(concrete.dtor_Static);
        return converted;
      }
      if (value.is_KmsRsa)
      {
        converted.KmsRsa = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsRsa(concrete.dtor_KmsRsa);
        return converted;
      }
      if (value.is_KmsECDH)
      {
        converted.KmsECDH = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M7_KmsECDH(concrete.dtor_KmsECDH);
        return converted;
      }
      if (value.is_Hierarchy)
      {
        converted.Hierarchy = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M9_Hierarchy(concrete.dtor_Hierarchy);
        return converted;
      }
      if (value.is_Multi)
      {
        converted.Multi = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M5_Multi(concrete.dtor_Multi);
        return converted;
      }
      if (value.is_RequiredEncryptionContext)
      {
        converted.RequiredEncryptionContext = FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M25_RequiredEncryptionContext(concrete.dtor_RequiredEncryptionContext);
        return converted;
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription state");
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      value.Validate(); if (value.IsSetKms())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Kms(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_Kms(value.Kms));
      }
      if (value.IsSetKmsMrk())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsMrk(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsMrk(value.KmsMrk));
      }
      if (value.IsSetKmsMrkDiscovery())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsMrkDiscovery(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M15_KmsMrkDiscovery(value.KmsMrkDiscovery));
      }
      if (value.IsSetRSA())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RSA(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_RSA(value.RSA));
      }
      if (value.IsSetAES())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_AES(value.AES));
      }
      if (value.IsSetECDH())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_ECDH(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M4_ECDH(value.ECDH));
      }
      if (value.IsSetStatic())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Static(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_Static(value.Static));
      }
      if (value.IsSetKmsRsa())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsRsa(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsRsa(value.KmsRsa));
      }
      if (value.IsSetKmsECDH())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsECDH(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M7_KmsECDH(value.KmsECDH));
      }
      if (value.IsSetHierarchy())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Hierarchy(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M9_Hierarchy(value.Hierarchy));
      }
      if (value.IsSetMulti())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Multi(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M5_Multi(value.Multi));
      }
      if (value.IsSetRequiredEncryptionContext())
      {
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M25_RequiredEncryptionContext(value.RequiredEncryptionContext));
      }
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription state");
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorException FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException value)
    {
      return new AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorException(
      FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException__M7_message(value._message)
      );
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorException value)
    {

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(
      ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException__M7_message(value.getMessage())
      );
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorsConfig FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyVectorsConfig value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorsConfig converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorsConfig(); converted.KeyManifestPath = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig__M15_keyManifestPath(concrete._keyManifestPath); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyVectorsConfig ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorsConfig value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig__M15_keyManifestPath(value.KeyManifestPath));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionInput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ISerializeKeyDescriptionInput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionInput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionInput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionInput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionInput(); converted.KeyDescription = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput__M14_keyDescription(concrete._keyDescription); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ISerializeKeyDescriptionInput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput(AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionInput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput__M14_keyDescription(value.KeyDescription));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionOutput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ISerializeKeyDescriptionOutput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionOutput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionOutput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionOutput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionOutput(); converted.Json = (System.IO.MemoryStream)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput__M4_json(concrete._json); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ISerializeKeyDescriptionOutput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput(AWS.Cryptography.MaterialProvidersTestVectorKeys.SerializeKeyDescriptionOutput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.SerializeKeyDescriptionOutput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput__M4_json(value.Json));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorCmmInput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ITestVectorCmmInput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorCmmInput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorCmmInput(); converted.KeyDescription = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M14_keyDescription(concrete._keyDescription);
      converted.ForOperation = (AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M12_forOperation(concrete._forOperation); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ITestVectorCmmInput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput(AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorCmmInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorCmmInput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M14_keyDescription(value.KeyDescription), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M12_forOperation(value.ForOperation));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorKeyringInput FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ITestVectorKeyringInput value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorKeyringInput converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorKeyringInput(); converted.KeyDescription = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput__M14_keyDescription(concrete._keyDescription); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ITestVectorKeyringInput ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput(AWS.Cryptography.MaterialProvidersTestVectorKeys.TestVectorKeyringInput value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.TestVectorKeyringInput(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput__M14_keyDescription(value.KeyDescription));
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S19_CreateKeyringOutput__M7_keyring(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput__M3_cmm(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S32_CreateWrappedTestVectorCmmOutput__M3_cmm(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput__M4_json(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_GetKeyDescriptionInput__M4_json(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput__M14_keyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S23_GetKeyDescriptionOutput__M14_keyDescription(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKMSInfo value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKMSInfo ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_Kms(AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsMrk(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAware value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAware ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsMrk(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M15_KmsMrkDiscovery(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAwareDiscovery value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAwareDiscovery ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M15_KmsMrkDiscovery(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawRSA value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawRSA ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_RSA(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawAES value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawAES ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M3_AES(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M4_ECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawEcdh value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawEcdh ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M4_ECDH(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_Static(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IStaticKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IStaticKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_Static(AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsRsa(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsRsaKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsRsaKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M6_KmsRsa(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M7_KmsECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsEcdhKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsEcdhKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M7_KmsECDH(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M9_Hierarchy(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IHierarchyKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IHierarchyKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M9_Hierarchy(AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M5_Multi(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IMultiKeyring value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IMultiKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M5_Multi(AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M25_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRequiredEncryptionContextCMM value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRequiredEncryptionContextCMM ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription__M25_RequiredEncryptionContext(AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException__M7_message(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException__M7_message(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig__M15_keyManifestPath(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_KeyVectorsConfig__M15_keyManifestPath(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput__M14_keyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_SerializeKeyDescriptionInput__M14_keyDescription(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static System.IO.MemoryStream FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput__M4_json(Dafny.ISequence<byte> value)
    {
      return FromDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S29_SerializeKeyDescriptionOutput__M4_json(System.IO.MemoryStream value)
    {
      return ToDafny_N6_smithy__N3_api__S4_Blob(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M14_keyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M14_keyDescription(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M12_forOperation(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ICmmOperation value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_CmmOperation(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._ICmmOperation ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_TestVectorCmmInput__M12_forOperation(AWS.Cryptography.MaterialProvidersTestVectorKeys.CmmOperation value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_CmmOperation(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput__M14_keyDescription(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S22_TestVectorKeyringInput__M14_keyDescription(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static AWS.Cryptography.MaterialProviders.IKeyring FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(AWS.Cryptography.MaterialProviders.IKeyring value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S16_KeyringReference(value);
    }
    public static AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager value)
    {
      // This is converting a reference type in a dependant module.
      // Therefore it defers to the dependant module for conversion
      return AWS.Cryptography.MaterialProviders.TypeConversion.ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S38_CryptographicMaterialsManagerReference(value);
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
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKMSInfo value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo__M5_keyId(concrete._keyId); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKMSInfo ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo(AWS.Cryptography.MaterialProvidersTestVectorKeys.KMSInfo value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo__M5_keyId(value.KeyId));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAware value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware__M5_keyId(concrete._keyId); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAware ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAware value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware__M5_keyId(value.KeyId));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAwareDiscovery value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M5_keyId(concrete._keyId);
      converted.DefaultMrkRegion = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M16_defaultMrkRegion(concrete._defaultMrkRegion);
      if (concrete._awsKmsDiscoveryFilter.is_Some) converted.AwsKmsDiscoveryFilter = (AWS.Cryptography.MaterialProviders.DiscoveryFilter)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M21_awsKmsDiscoveryFilter(concrete._awsKmsDiscoveryFilter); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsMrkAwareDiscovery ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsMrkAwareDiscovery value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProviders.DiscoveryFilter var_awsKmsDiscoveryFilter = value.IsSetAwsKmsDiscoveryFilter() ? value.AwsKmsDiscoveryFilter : (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null;
      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M5_keyId(value.KeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M16_defaultMrkRegion(value.DefaultMrkRegion), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M21_awsKmsDiscoveryFilter(var_awsKmsDiscoveryFilter));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawRSA value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M5_keyId(concrete._keyId);
      converted.ProviderId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M10_providerId(concrete._providerId);
      converted.Padding = (AWS.Cryptography.MaterialProviders.PaddingScheme)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M7_padding(concrete._padding); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawRSA ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawRSA value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M5_keyId(value.KeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M10_providerId(value.ProviderId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M7_padding(value.Padding));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawAES value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M5_keyId(concrete._keyId);
      converted.ProviderId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M10_providerId(concrete._providerId); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawAES ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawAES value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M5_keyId(value.KeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M10_providerId(value.ProviderId));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawEcdh value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh(); converted.SenderKeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M11_senderKeyId(concrete._senderKeyId);
      converted.RecipientKeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M14_recipientKeyId(concrete._recipientKeyId);
      converted.SenderPublicKey = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M15_senderPublicKey(concrete._senderPublicKey);
      converted.RecipientPublicKey = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_recipientPublicKey(concrete._recipientPublicKey);
      converted.ProviderId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M10_providerId(concrete._providerId);
      converted.CurveSpec = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M9_curveSpec(concrete._curveSpec);
      converted.KeyAgreementScheme = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_keyAgreementScheme(concrete._keyAgreementScheme); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRawEcdh ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh(AWS.Cryptography.MaterialProvidersTestVectorKeys.RawEcdh value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M11_senderKeyId(value.SenderKeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M14_recipientKeyId(value.RecipientKeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M15_senderPublicKey(value.SenderPublicKey), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_recipientPublicKey(value.RecipientPublicKey), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M10_providerId(value.ProviderId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M9_curveSpec(value.CurveSpec), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_keyAgreementScheme(value.KeyAgreementScheme));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IStaticKeyring value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring__M5_keyId(concrete._keyId); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IStaticKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring(AWS.Cryptography.MaterialProvidersTestVectorKeys.StaticKeyring value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring__M5_keyId(value.KeyId));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsRsaKeyring value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M5_keyId(concrete._keyId);
      converted.EncryptionAlgorithm = (Amazon.KeyManagementService.EncryptionAlgorithmSpec)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M19_encryptionAlgorithm(concrete._encryptionAlgorithm); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsRsaKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsRsaKeyring value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M5_keyId(value.KeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M19_encryptionAlgorithm(value.EncryptionAlgorithm));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsEcdhKeyring value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring(); converted.SenderKeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M11_senderKeyId(concrete._senderKeyId);
      converted.RecipientKeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M14_recipientKeyId(concrete._recipientKeyId);
      converted.SenderPublicKey = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M15_senderPublicKey(concrete._senderPublicKey);
      converted.RecipientPublicKey = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_recipientPublicKey(concrete._recipientPublicKey);
      converted.CurveSpec = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M9_curveSpec(concrete._curveSpec);
      converted.KeyAgreementScheme = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_keyAgreementScheme(concrete._keyAgreementScheme); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKmsEcdhKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring(AWS.Cryptography.MaterialProvidersTestVectorKeys.KmsEcdhKeyring value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsEcdhKeyring(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M11_senderKeyId(value.SenderKeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M14_recipientKeyId(value.RecipientKeyId), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M15_senderPublicKey(value.SenderPublicKey), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_recipientPublicKey(value.RecipientPublicKey), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M9_curveSpec(value.CurveSpec), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_keyAgreementScheme(value.KeyAgreementScheme));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IHierarchyKeyring value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring(); converted.KeyId = (string)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring__M5_keyId(concrete._keyId); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IHierarchyKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring(AWS.Cryptography.MaterialProvidersTestVectorKeys.HierarchyKeyring value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.HierarchyKeyring(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring__M5_keyId(value.KeyId));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IMultiKeyring value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring(); if (concrete._generator.is_Some) converted.Generator = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M9_generator(concrete._generator);
      converted.ChildKeyrings = (System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription>)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M13_childKeyrings(concrete._childKeyrings); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IMultiKeyring ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring(AWS.Cryptography.MaterialProvidersTestVectorKeys.MultiKeyring value)
    {
      value.Validate();
      AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription var_generator = value.IsSetGenerator() ? value.Generator : (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)null;
      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M9_generator(var_generator), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M13_childKeyrings(value.ChildKeyrings));
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRequiredEncryptionContextCMM value)
    {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM concrete = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM)value; AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM converted = new AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM(); converted.Underlying = (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M10_underlying(concrete._underlying);
      converted.RequiredEncryptionContextKeys = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M29_requiredEncryptionContextKeys(concrete._requiredEncryptionContextKeys); return converted;
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IRequiredEncryptionContextCMM ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM(AWS.Cryptography.MaterialProvidersTestVectorKeys.RequiredEncryptionContextCMM value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M10_underlying(value.Underlying), ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M29_requiredEncryptionContextKeys(value.RequiredEncryptionContextKeys));
    }
    public static string FromDafny_N6_smithy__N3_api__S6_String(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N6_smithy__N3_api__S6_String(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_KMSInfo__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S11_KmsMrkAware__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M16_defaultMrkRegion(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M16_defaultMrkRegion(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M21_awsKmsDiscoveryFilter(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProviders.DiscoveryFilter)null : FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S20_KmsMrkAwareDiscovery__M21_awsKmsDiscoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter>.create_Some(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter((AWS.Cryptography.MaterialProviders.DiscoveryFilter)value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M10_providerId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M10_providerId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProviders.PaddingScheme FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M7_padding(software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(value);
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawRSA__M7_padding(AWS.Cryptography.MaterialProviders.PaddingScheme value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M10_providerId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S6_RawAES__M10_providerId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M11_senderKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M11_senderKeyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M14_recipientKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M14_recipientKeyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M15_senderPublicKey(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M15_senderPublicKey(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_recipientPublicKey(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_recipientPublicKey(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M10_providerId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M10_providerId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M9_curveSpec(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M9_curveSpec(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_keyAgreementScheme(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S7_RawEcdh__M18_keyAgreementScheme(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_StaticKeyring__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Amazon.KeyManagementService.EncryptionAlgorithmSpec FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M19_encryptionAlgorithm(software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec value)
    {
      return FromDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(value);
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S13_KmsRsaKeyring__M19_encryptionAlgorithm(Amazon.KeyManagementService.EncryptionAlgorithmSpec value)
    {
      return ToDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M11_senderKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M11_senderKeyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M14_recipientKeyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M14_recipientKeyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M15_senderPublicKey(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M15_senderPublicKey(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_recipientPublicKey(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_recipientPublicKey(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M9_curveSpec(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M9_curveSpec(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_keyAgreementScheme(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KmsEcdhKeyring__M18_keyAgreementScheme(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring__M5_keyId(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S16_HierarchyKeyring__M5_keyId(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M9_generator(Wrappers_Compile._IOption<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> value)
    {
      return value.is_None ? (AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)null : FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value.Extract());
    }
    public static Wrappers_Compile._IOption<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M9_generator(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return value == null ? Wrappers_Compile.Option<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription>.create_None() : Wrappers_Compile.Option<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription>.create_Some(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription((AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription)value));
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription> FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M13_childKeyrings(Dafny.ISequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList(value);
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S12_MultiKeyring__M13_childKeyrings(System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M10_underlying(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M10_underlying(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M29_requiredEncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S28_RequiredEncryptionContextCMM__M29_requiredEncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(value);
    }
    public static AWS.Cryptography.MaterialProviders.DiscoveryFilter FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter value)
    {
      software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter concrete = (software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter)value; AWS.Cryptography.MaterialProviders.DiscoveryFilter converted = new AWS.Cryptography.MaterialProviders.DiscoveryFilter(); converted.AccountIds = (System.Collections.Generic.List<string>)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(concrete._accountIds);
      converted.Partition = (string)FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(concrete._partition); return converted;
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IDiscoveryFilter ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter(AWS.Cryptography.MaterialProviders.DiscoveryFilter value)
    {
      value.Validate();

      return new software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(value.AccountIds), ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(value.Partition));
    }
    public static AWS.Cryptography.MaterialProviders.PaddingScheme FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme value)
    {
      if (value.is_PKCS1) return AWS.Cryptography.MaterialProviders.PaddingScheme.PKCS1;
      if (value.is_OAEP__SHA1__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA1_MGF1;
      if (value.is_OAEP__SHA256__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA256_MGF1;
      if (value.is_OAEP__SHA384__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA384_MGF1;
      if (value.is_OAEP__SHA512__MGF1) return AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA512_MGF1;
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.PaddingScheme value");
    }
    public static software.amazon.cryptography.materialproviders.internaldafny.types._IPaddingScheme ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_PaddingScheme(AWS.Cryptography.MaterialProviders.PaddingScheme value)
    {
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.PKCS1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_PKCS1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA1_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA1__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA256_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA256__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA384_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA384__MGF1();
      if (AWS.Cryptography.MaterialProviders.PaddingScheme.OAEP_SHA512_MGF1.Equals(value)) return software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.create_OAEP__SHA512__MGF1();
      throw new System.ArgumentException("Invalid AWS.Cryptography.MaterialProviders.PaddingScheme value");
    }
    public static Amazon.KeyManagementService.EncryptionAlgorithmSpec FromDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec value)
    {
      if (value.is_SYMMETRIC__DEFAULT) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT;
      if (value.is_RSAES__OAEP__SHA__1) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1;
      if (value.is_RSAES__OAEP__SHA__256) return Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256;
      throw new System.ArgumentException("Invalid Amazon.KeyManagementService.EncryptionAlgorithmSpec value");
    }
    public static software.amazon.cryptography.services.kms.internaldafny.types._IEncryptionAlgorithmSpec ToDafny_N3_com__N9_amazonaws__N3_kms__S23_EncryptionAlgorithmSpec(Amazon.KeyManagementService.EncryptionAlgorithmSpec value)
    {
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_SYMMETRIC__DEFAULT();
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__1();
      if (Amazon.KeyManagementService.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256.Equals(value)) return software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.create_RSAES__OAEP__SHA__256();
      throw new System.ArgumentException("Invalid Amazon.KeyManagementService.EncryptionAlgorithmSpec value");
    }
    public static System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription> FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList(Dafny.ISequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> value)
    {
      return new System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList__M6_member));
    }
    public static Dafny.ISequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription> ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList(System.Collections.Generic.List<AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription> value)
    {
      return Dafny.Sequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList__M6_member).ToArray());
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(Dafny.ISequence<Dafny.ISequence<byte>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<byte>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<byte>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member).ToArray());
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(value);
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M10_accountIds(System.Collections.Generic.List<string> value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(Dafny.ISequence<char> value)
    {
      return FromDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S15_DiscoveryFilter__M9_partition(string value)
    {
      return ToDafny_N6_smithy__N3_api__S6_String(value);
    }
    public static AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList__M6_member(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription value)
    {
      return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IKeyDescription ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyDescriptionList__M6_member(AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription value)
    {
      return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S14_KeyDescription(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member(Dafny.ISequence<byte> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S21_EncryptionContextKeys__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(value);
    }
    public static System.Collections.Generic.List<string> FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(Dafny.ISequence<Dafny.ISequence<char>> value)
    {
      return new System.Collections.Generic.List<string>(value.Elements.Select(FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member));
    }
    public static Dafny.ISequence<Dafny.ISequence<char>> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList(System.Collections.Generic.List<string> value)
    {
      return Dafny.Sequence<Dafny.ISequence<char>>.FromArray(value.Select(ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member).ToArray());
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(Dafny.ISequence<byte> value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return utf8.GetString(value.Elements);
    }
    public static Dafny.ISequence<byte> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_Utf8Bytes(string value)
    {
      System.Text.UTF8Encoding utf8 = new System.Text.UTF8Encoding(false, true);
      return Dafny.Sequence<byte>.FromArray(utf8.GetBytes(value));
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member(Dafny.ISequence<char> value)
    {
      return FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(value);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S13_AccountIdList__M6_member(string value)
    {
      return ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(value);
    }
    public static string FromDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(Dafny.ISequence<char> value)
    {
      return new string(value.Elements);
    }
    public static Dafny.ISequence<char> ToDafny_N3_aws__N12_cryptography__N17_materialProviders__S9_AccountId(string value)
    {
      return Dafny.Sequence<char>.FromString(value);
    }
    public static System.Exception FromDafny_CommonError(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IError value)
    {
      switch (value)
      {

        case software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException dafnyVal:
          return FromDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException(dafnyVal);
        case software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_CollectionOfErrors dafnyVal:
          return new CollectionOfErrors(
              new System.Collections.Generic.List<Exception>(dafnyVal.dtor_list.CloneAsArray()
                .Select(x => TypeConversion.FromDafny_CommonError(x))),
              new string(dafnyVal.dtor_message.Elements));
        case software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_Opaque dafnyVal:
          return new OpaqueError(dafnyVal._obj);
        case software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_OpaqueWithText dafnyVal:
          return new OpaqueWithTextError(dafnyVal._obj, dafnyVal._obj.ToString());
        default:
          // The switch MUST be complete for _IError, so `value` MUST NOT be an _IError. (How did you get here?)
          return new OpaqueError();
      }
    }
    public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IError ToDafny_CommonError(System.Exception value)
    {

      switch (value)
      {
        case AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyVectorException exception:
          return ToDafny_N3_aws__N12_cryptography__N31_materialProvidersTestVectorKeys__S18_KeyVectorException(exception);
        case CollectionOfErrors collectionOfErrors:
          return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_CollectionOfErrors(
            Dafny.Sequence<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types._IError>
              .FromArray(
                collectionOfErrors.list.Select
                    (x => TypeConversion.ToDafny_CommonError(x))
                  .ToArray()),
            Dafny.Sequence<char>.FromString(collectionOfErrors.Message)
          );
        // OpaqueError is redundant, but listed for completeness.
        case OpaqueError exception:
          return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_Opaque(exception);
        case System.Exception exception:
          return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_Opaque(exception);
        default:
          // The switch MUST be complete for System.Exception, so `value` MUST NOT be an System.Exception. (How did you get here?)
          return new software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_Opaque(value);
      }
    }
  }
}
