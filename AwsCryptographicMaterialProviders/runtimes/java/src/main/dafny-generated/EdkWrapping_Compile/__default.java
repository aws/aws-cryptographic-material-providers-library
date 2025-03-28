// Class __default
// Dafny class __default compiled into Java
package EdkWrapping_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T> Wrappers_Compile.Result<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> WrapEdkMaterial(dafny.TypeDescriptor<__T> _td___T, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials encryptionMaterials, MaterialWrapping_Compile.WrapMaterial<__T> wrap, MaterialWrapping_Compile.GenerateAndWrapMaterial<__T> generateAndWrap)
  {
    Wrappers_Compile.Result<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ret = (Wrappers_Compile.Result<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.ValidEncryptionMaterials(encryptionMaterials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid materials for encryption.")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        ret = (_0_valueOrError0).<WrapEdkMaterialOutput<__T>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
        return ret;
      }
      if ((((encryptionMaterials).dtor_plaintextDataKey()).is_Some()) && ((((encryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING())) {
        Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = (Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = (wrap).Invoke(MaterialWrapping_Compile.WrapInput.create(((encryptionMaterials).dtor_plaintextDataKey()).dtor_value(), (encryptionMaterials).dtor_algorithmSuite(), (encryptionMaterials).dtor_encryptionContext()));
        _1_valueOrError1 = _out0;
        if ((_1_valueOrError1).IsFailure(MaterialWrapping_Compile.WrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_1_valueOrError1).<WrapEdkMaterialOutput<__T>>PropagateFailure(MaterialWrapping_Compile.WrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        MaterialWrapping_Compile.WrapOutput<__T> _2_directOutput;
        _2_directOutput = (_1_valueOrError1).Extract(MaterialWrapping_Compile.WrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<__T>create_WrapOnlyEdkMaterialOutput(_td___T, (_2_directOutput).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_2_directOutput).dtor_wrapInfo()));
        return ret;
      } else if ((((encryptionMaterials).dtor_plaintextDataKey()).is_Some()) && ((((encryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_IntermediateKeyWrapping())) {
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError2 = (Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = IntermediateKeyWrapping_Compile.__default.<__T>IntermediateWrap(_td___T, generateAndWrap, ((encryptionMaterials).dtor_plaintextDataKey()).dtor_value(), (encryptionMaterials).dtor_algorithmSuite(), (encryptionMaterials).dtor_encryptionContext());
        _3_valueOrError2 = _out1;
        if ((_3_valueOrError2).IsFailure(IntermediateKeyWrapping_Compile.IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_3_valueOrError2).<WrapEdkMaterialOutput<__T>>PropagateFailure(IntermediateKeyWrapping_Compile.IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        IntermediateKeyWrapping_Compile.IntermediateWrapOutput<__T> _4_intermediateOutput;
        _4_intermediateOutput = (_3_valueOrError2).Extract(IntermediateKeyWrapping_Compile.IntermediateWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<__T>create_WrapOnlyEdkMaterialOutput(_td___T, (_4_intermediateOutput).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_4_intermediateOutput).dtor_symmetricSigningKey()), (_4_intermediateOutput).dtor_wrapInfo()));
        return ret;
      } else if ((((encryptionMaterials).dtor_plaintextDataKey()).is_None()) && ((((encryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING())) {
        Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError3 = (Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
        _out2 = (generateAndWrap).Invoke(MaterialWrapping_Compile.GenerateAndWrapInput.create((encryptionMaterials).dtor_algorithmSuite(), (encryptionMaterials).dtor_encryptionContext()));
        _5_valueOrError3 = _out2;
        if ((_5_valueOrError3).IsFailure(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_5_valueOrError3).<WrapEdkMaterialOutput<__T>>PropagateFailure(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        MaterialWrapping_Compile.GenerateAndWrapOutput<__T> _6_directOutput;
        _6_directOutput = (_5_valueOrError3).Extract(MaterialWrapping_Compile.GenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<__T>create_GenerateAndWrapEdkMaterialOutput(_td___T, (_6_directOutput).dtor_plaintextMaterial(), (_6_directOutput).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_6_directOutput).dtor_wrapInfo()));
        return ret;
      } else if ((((encryptionMaterials).dtor_plaintextDataKey()).is_None()) && ((((encryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_IntermediateKeyWrapping())) {
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _7_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((encryptionMaterials).dtor_algorithmSuite()).dtor_commitment()).is_HKDF(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid algorithm suite: suites with intermediate key wrapping must use key commitment.")));
        if ((_7_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_7_valueOrError4).<WrapEdkMaterialOutput<__T>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError5 = (Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
        _out3 = IntermediateKeyWrapping_Compile.__default.<__T>IntermediateGenerateAndWrap(_td___T, generateAndWrap, (encryptionMaterials).dtor_algorithmSuite(), (encryptionMaterials).dtor_encryptionContext());
        _8_valueOrError5 = _out3;
        if ((_8_valueOrError5).IsFailure(IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_8_valueOrError5).<WrapEdkMaterialOutput<__T>>PropagateFailure(IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput<__T> _9_intermediateOutput;
        _9_intermediateOutput = (_8_valueOrError5).Extract(IntermediateKeyWrapping_Compile.IntermediateGenerateAndWrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<WrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(WrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<__T>create_GenerateAndWrapEdkMaterialOutput(_td___T, (_9_intermediateOutput).dtor_plaintextDataKey(), (_9_intermediateOutput).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_9_intermediateOutput).dtor_symmetricSigningKey()), (_9_intermediateOutput).dtor_wrapInfo()));
        return ret;
      } else {
      }
    }
    return ret;
  }
  public static <__T> Wrappers_Compile.Result<UnwrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> UnwrapEdkMaterial(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends java.lang.Byte> wrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials decryptionMaterials, MaterialWrapping_Compile.UnwrapMaterial<__T> unwrap)
  {
    Wrappers_Compile.Result<UnwrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ret = (Wrappers_Compile.Result<UnwrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.ValidDecryptionMaterials(decryptionMaterials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid materials for decryption.")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        ret = (_0_valueOrError0).<UnwrapEdkMaterialOutput<__T>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
        return ret;
      }
      if ((((decryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING()) {
        Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = (Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = (unwrap).Invoke(MaterialWrapping_Compile.UnwrapInput.create(wrappedMaterial, (decryptionMaterials).dtor_algorithmSuite(), (decryptionMaterials).dtor_encryptionContext()));
        _1_valueOrError1 = _out0;
        if ((_1_valueOrError1).IsFailure(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_1_valueOrError1).<UnwrapEdkMaterialOutput<__T>>PropagateFailure(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        MaterialWrapping_Compile.UnwrapOutput<__T> _2_directOutput;
        _2_directOutput = (_1_valueOrError1).Extract(MaterialWrapping_Compile.UnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<UnwrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<__T>create(_td___T, (_2_directOutput).dtor_unwrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), (_2_directOutput).dtor_unwrapInfo()));
        return ret;
      } else if ((((decryptionMaterials).dtor_algorithmSuite()).dtor_edkWrapping()).is_IntermediateKeyWrapping()) {
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _3_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((wrappedMaterial).length())).compareTo(java.math.BigInteger.valueOf((int) ((((((decryptionMaterials).dtor_algorithmSuite()).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) + (((((decryptionMaterials).dtor_algorithmSuite()).dtor_encrypt()).dtor_AES__GCM()).dtor_tagLength())))) >= 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid material for Intermediate Unwrapping")));
        if ((_3_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_3_valueOrError2).<UnwrapEdkMaterialOutput<__T>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError3 = (Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = IntermediateKeyWrapping_Compile.__default.<__T>IntermediateUnwrap(_td___T, unwrap, wrappedMaterial, (decryptionMaterials).dtor_algorithmSuite(), (decryptionMaterials).dtor_encryptionContext());
        _4_valueOrError3 = _out1;
        if ((_4_valueOrError3).IsFailure(IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          ret = (_4_valueOrError3).<UnwrapEdkMaterialOutput<__T>>PropagateFailure(IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T));
          return ret;
        }
        IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput<__T> _5_intermediateOutput;
        _5_intermediateOutput = (_4_valueOrError3).Extract(IntermediateKeyWrapping_Compile.IntermediateUnwrapOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        ret = Wrappers_Compile.Result.<UnwrapEdkMaterialOutput<__T>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(UnwrapEdkMaterialOutput.<__T>_typeDescriptor(_td___T), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<__T>create(_td___T, (_5_intermediateOutput).dtor_plaintextDataKey(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_5_intermediateOutput).dtor_symmetricSigningKey()), (_5_intermediateOutput).dtor_unwrapInfo()));
        return ret;
      } else {
      }
    }
    return ret;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetProviderWrappedMaterial(dafny.DafnySequence<? extends java.lang.Byte> material, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo algSuite)
  {
    if (((algSuite).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING()) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), material);
    } else {
      Wrappers_Compile.Result<IntermediateKeyWrapping_Compile.DeserializedIntermediateWrappedMaterial, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_deserializedWrappedRes = IntermediateKeyWrapping_Compile.__default.DeserializeIntermediateWrappedMaterial(material, algSuite);
      if ((_0_deserializedWrappedRes).is_Failure()) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unable to deserialize Intermediate Key Wrapped material.")));
      } else {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_0_deserializedWrappedRes).dtor_value()).dtor_providerWrappedIkm());
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "EdkWrapping._default";
  }
}
