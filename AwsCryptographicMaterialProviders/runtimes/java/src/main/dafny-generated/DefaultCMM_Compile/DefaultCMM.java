// Class DefaultCMM
// Dafny class DefaultCMM compiled into Java
package DefaultCMM_Compile;

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
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;
import MrkAwareStrictMultiKeyring_Compile.*;
import LocalCMC_Compile.*;
import StormTracker_Compile.*;
import software.amazon.cryptography.internaldafny.StormTrackingCMC.*;
import CacheConstants_Compile.*;
import AwsKmsHierarchicalKeyring_Compile.*;
import AwsKmsRsaKeyring_Compile.*;
import EcdhEdkWrapping_Compile.*;
import RawECDHKeyring_Compile.*;
import AwsKmsEcdhKeyring_Compile.*;
import RawAESKeyring_Compile.*;
import RawRSAKeyring_Compile.*;
import CMM_Compile.*;
import Defaults_Compile.*;
import Commitment_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DefaultCMM implements CMM_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager {
  public DefaultCMM() {
    this._keyring = null;
    this._cryptoPrimitives = null;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsManager.DecryptMaterials(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsManager.GetEncryptionMaterials(this, input);
    return _out1;
  }
  public void OfKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring k, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient c)
  {
    (this)._keyring = k;
    (this)._cryptoPrimitives = c;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetEncryptionMaterials_k(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), !((input).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(Materials_Compile.__default.EC__PUBLIC__KEY__FIELD()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Reserved Field found in EncryptionContext keys.")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _1_algorithmId;
      if (((input).dtor_algorithmSuiteId()).is_Some()) {
        _1_algorithmId = ((input).dtor_algorithmSuiteId()).dtor_value();
      } else {
        _1_algorithmId = Defaults_Compile.__default.GetAlgorithmSuiteForCommitmentPolicy((input).dtor_commitmentPolicy());
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _2_valueOrError1 = Commitment_Compile.__default.ValidateCommitmentPolicyOnEncrypt(_1_algorithmId, (input).dtor_commitmentPolicy());
      if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _3_suite;
      _3_suite = AlgorithmSuites_Compile.__default.GetSuite(_1_algorithmId);
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _4_signingKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _5_verificationKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      if (((_3_suite).dtor_signature()).is_ECDSA()) {
        Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _6_maybeECDSAPair;
        Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
        _out0 = ((this).cryptoPrimitives()).GenerateECDSASignatureKey(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput.create((((_3_suite).dtor_signature()).dtor_ECDSA()).dtor_curve()));
        _6_maybeECDSAPair = _out0;
        Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.Default());
        _7_valueOrError2 = (_6_maybeECDSAPair).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_8_e_boxed0) -> {
          software.amazon.cryptography.primitives.internaldafny.types.Error _8_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_8_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_8_e);
        }));
        if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput _9_pair;
        _9_pair = (_7_valueOrError2).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _4_signingKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_9_pair).dtor_signingKey());
        _5_verificationKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_9_pair).dtor_verificationKey());
      } else {
        _4_signingKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        _5_verificationKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      }
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _10_valueOrError3 = Materials_Compile.__default.InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput.create(_1_algorithmId, (input).dtor_encryptionContext(), ((input).dtor_requiredEncryptionContextKeys()).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())), _4_signingKey, _5_verificationKey));
      if ((_10_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _11_materials;
      _11_materials = (_10_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = ((this).keyring()).OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(_11_materials));
      _12_valueOrError4 = _out1;
      if ((_12_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_12_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput _13_result;
      _13_result = (_12_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput _14_encryptionMaterialsOutput;
      _14_encryptionMaterialsOutput = software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput.create((_13_result).dtor_materials());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _15_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.EncryptionMaterialsHasPlaintextDataKey((_14_encryptionMaterialsOutput).dtor_encryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Could not retrieve materials required for encryption")));
      if ((_15_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_15_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _16_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.ValidEncryptionMaterialsTransition(_11_materials, (_14_encryptionMaterialsOutput).dtor_encryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring returned an invalid response")));
      if ((_16_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_16_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _14_encryptionMaterialsOutput);
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptMaterials_k(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Commitment_Compile.__default.ValidateCommitmentPolicyOnDecrypt((input).dtor_algorithmSuiteId(), (input).dtor_commitmentPolicy());
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_requiredEncryptionContextKeys;
    _1_requiredEncryptionContextKeys = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor());
    if (((input).dtor_reproducedEncryptionContext()).is_Some()) {
      dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_keysSet;
      _2_keysSet = (((input).dtor_reproducedEncryptionContext()).dtor_value()).keySet();
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_keysSeq;
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _out0;
      _out0 = SortedSets.__default.<dafny.DafnySequence<? extends java.lang.Byte>>SetToSequence(UTF8.ValidUTF8Bytes._typeDescriptor(), _2_keysSet);
      _3_keysSeq = _out0;
      java.math.BigInteger _4_i = java.math.BigInteger.ZERO;
      _4_i = java.math.BigInteger.ZERO;
      while ((_4_i).compareTo(java.math.BigInteger.valueOf((_3_keysSeq).length())) < 0) {
        dafny.DafnySequence<? extends java.lang.Byte> _5_key;
        _5_key = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_3_keysSeq).select(dafny.Helpers.toInt((_4_i)))));
        if (((input).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_5_key)) {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((((input).dtor_reproducedEncryptionContext()).dtor_value()).get(_5_key)))).equals(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((input).dtor_encryptionContext()).get(_5_key)))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Encryption context does not match reproduced encryption context.")));
          if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_6_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
            return output;
          }
        } else {
          _1_requiredEncryptionContextKeys = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>concatenate(_1_requiredEncryptionContextKeys, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(UTF8.ValidUTF8Bytes._typeDescriptor(), _5_key));
        }
        _4_i = (_4_i).add(java.math.BigInteger.ONE);
      }
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _7_valueOrError2 = Materials_Compile.__default.InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput.create((input).dtor_algorithmSuiteId(), dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>merge((input).dtor_encryptionContext(), ((input).dtor_reproducedEncryptionContext()).UnwrapOr(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnyMap.fromElements())), _1_requiredEncryptionContextKeys));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _8_materials;
    _8_materials = (_7_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = ((this).keyring()).OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput.create(_8_materials, (input).dtor_encryptedDataKeys()));
    _9_valueOrError3 = _out1;
    if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_9_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _10_result;
    _10_result = (_9_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _11_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsTransitionIsValid(_8_materials, (_10_result).dtor_materials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring.OnDecrypt failed to decrypt the plaintext data key.")));
    if ((_11_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_11_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput.create((_10_result).dtor_materials()));
    return output;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring _keyring;
  public software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring keyring()
  {
    return this._keyring;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  private static final dafny.TypeDescriptor<DefaultCMM> _TYPE = dafny.TypeDescriptor.<DefaultCMM>referenceWithInitializer(DefaultCMM.class, () -> (DefaultCMM) null);
  public static dafny.TypeDescriptor<DefaultCMM> _typeDescriptor() {
    return (dafny.TypeDescriptor<DefaultCMM>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "DefaultCMM.DefaultCMM";
  }
}
