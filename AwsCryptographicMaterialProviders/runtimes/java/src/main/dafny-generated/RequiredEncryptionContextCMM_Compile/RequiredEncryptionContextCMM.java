// Class RequiredEncryptionContextCMM
// Dafny class RequiredEncryptionContextCMM compiled into Java
package RequiredEncryptionContextCMM_Compile;

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
import DefaultCMM_Compile.*;
import DefaultClientSupplier_Compile.*;
import Utils_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class RequiredEncryptionContextCMM implements CMM_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager {
  public RequiredEncryptionContextCMM() {
    this._underlyingCMM = null;
    this._requiredEncryptionContextKeys = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsManager.DecryptMaterials(this, input);
    return _out2;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_ICryptographicMaterialsManager.GetEncryptionMaterials(this, input);
    return _out2;
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager inputCMM, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> inputKeys)
  {
    dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_keySet;
    _0_keySet = inputKeys;
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_keySeq;
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _out0;
    _out0 = SortedSets.__default.<dafny.DafnySequence<? extends java.lang.Byte>>SetToSequence(UTF8.ValidUTF8Bytes._typeDescriptor(), _0_keySet);
    _1_keySeq = _out0;
    (this)._underlyingCMM = inputCMM;
    (this)._requiredEncryptionContextKeys = _1_keySeq;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetEncryptionMaterials_k(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput, Boolean>)(_1_input) -> dafny.Helpers.Quantifier(((this).requiredEncryptionContextKeys()).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
        dafny.DafnySequence<? extends java.lang.Byte> _forall_var_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_0_boxed0));
        dafny.DafnySequence<? extends java.lang.Byte> _2_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_0;
        if (UTF8.ValidUTF8Bytes._Is(_2_k)) {
          return !(((this).requiredEncryptionContextKeys()).contains(_2_k)) || (((_1_input).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_2_k));
        } else {
          return true;
        }
      }))).apply(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Encryption context does not contain required keys.")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput _pat_let_tv0 = input;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = ((this).underlyingCMM()).GetEncryptionMaterials(((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput, software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput>Let(input, boxed16 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput _pat_let8_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(boxed16));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput, software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput>Let(_pat_let8_0, boxed17 -> {
          software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput _4_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(boxed17));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>, software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput>Let(Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>concatenate(((_pat_let_tv0).dtor_requiredEncryptionContextKeys()).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(UTF8.ValidUTF8Bytes._typeDescriptor())), (this).requiredEncryptionContextKeys())), boxed18 -> {
            Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _pat_let9_0 = ((Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(java.lang.Object)(boxed18));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>, software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput>Let(_pat_let9_0, boxed19 -> {
              Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _5_dt__update_hrequiredEncryptionContextKeys_h0 = ((Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(java.lang.Object)(boxed19));
              return software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.create((_4_dt__update__tmp_h0).dtor_encryptionContext(), (_4_dt__update__tmp_h0).dtor_commitmentPolicy(), (_4_dt__update__tmp_h0).dtor_algorithmSuiteId(), (_4_dt__update__tmp_h0).dtor_maxPlaintextLength(), _5_dt__update_hrequiredEncryptionContextKeys_h0);
            }
            )));
          }
          )));
        }
        )));
      }
      ))));
      _3_valueOrError1 = _out0;
      if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput _6_result;
      _6_result = (_3_valueOrError1).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, Boolean>)(_8_result) -> dafny.Helpers.Quantifier(((this).requiredEncryptionContextKeys()).UniqueElements(), true, ((_forall_var_1_boxed0) -> {
        dafny.DafnySequence<? extends java.lang.Byte> _forall_var_1 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_1_boxed0));
        dafny.DafnySequence<? extends java.lang.Byte> _9_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_1;
        if (UTF8.ValidUTF8Bytes._Is(_9_k)) {
          return !(((this).requiredEncryptionContextKeys()).contains(_9_k)) || ((((_8_result).dtor_encryptionMaterials()).dtor_requiredEncryptionContextKeys()).contains(_9_k));
        } else {
          return true;
        }
      }))).apply(_6_result), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Expected encryption context keys do not exist in keys to only authenticate.")));
      if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _10_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.EncryptionMaterialsHasPlaintextDataKey((_6_result).dtor_encryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Could not retrieve materials required for encryption")));
      if ((_10_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _11_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), CMM_Compile.__default.RequiredEncryptionContextKeys_q((input).dtor_requiredEncryptionContextKeys(), (_6_result).dtor_encryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring returned an invalid response")));
      if ((_11_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_11_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor());
        return output;
      }
      output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _6_result);
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptMaterials_k(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((input).dtor_reproducedEncryptionContext()).is_Some(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("No reproduced encryption context on decrypt.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), CMM_Compile.__default.ReproducedEncryptionContext_q(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Encryption context does not match reproduced encryption context.")));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_1_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput, Boolean>)(_3_input) -> dafny.Helpers.Quantifier(((this).requiredEncryptionContextKeys()).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends java.lang.Byte> _forall_var_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends java.lang.Byte> _4_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_0;
      if (UTF8.ValidUTF8Bytes._Is(_4_k)) {
        return !(((this).requiredEncryptionContextKeys()).contains(_4_k)) || ((((_3_input).dtor_reproducedEncryptionContext()).dtor_value()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_4_k));
      } else {
        return true;
      }
    }))).apply(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Reproduced encryption context missing required keys.")));
    if ((_2_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = ((this).underlyingCMM()).DecryptMaterials(input);
    _5_valueOrError3 = _out0;
    if ((_5_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_5_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput _6_result;
    _6_result = (_5_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, Boolean>)(_8_result) -> dafny.Helpers.Quantifier(((this).requiredEncryptionContextKeys()).UniqueElements(), true, ((_forall_var_1_boxed0) -> {
      dafny.DafnySequence<? extends java.lang.Byte> _forall_var_1 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_forall_var_1_boxed0));
      dafny.DafnySequence<? extends java.lang.Byte> _9_k = (dafny.DafnySequence<? extends java.lang.Byte>)_forall_var_1;
      if (UTF8.ValidUTF8Bytes._Is(_9_k)) {
        return !(((this).requiredEncryptionContextKeys()).contains(_9_k)) || ((((_8_result).dtor_decryptionMaterials()).dtor_encryptionContext()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_9_k));
      } else {
        return true;
      }
    }))).apply(_6_result), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Final encryption context missing required keys.")));
    if ((_7_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_7_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _10_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), CMM_Compile.__default.EncryptionContextComplete(input, (_6_result).dtor_decryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Reproduced encryption context missing from encryption context.")));
    if ((_10_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_10_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _11_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithPlaintextDataKey((_6_result).dtor_decryptionMaterials()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring.OnDecrypt failed to decrypt the plaintext data key.")));
    if ((_11_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_11_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor());
      return output;
    }
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _6_result);
    return output;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager _underlyingCMM;
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager underlyingCMM()
  {
    return this._underlyingCMM;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _requiredEncryptionContextKeys;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> requiredEncryptionContextKeys()
  {
    return this._requiredEncryptionContextKeys;
  }
  private static final dafny.TypeDescriptor<RequiredEncryptionContextCMM> _TYPE = dafny.TypeDescriptor.<RequiredEncryptionContextCMM>referenceWithInitializer(RequiredEncryptionContextCMM.class, () -> (RequiredEncryptionContextCMM) null);
  public static dafny.TypeDescriptor<RequiredEncryptionContextCMM> _typeDescriptor() {
    return (dafny.TypeDescriptor<RequiredEncryptionContextCMM>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RequiredEncryptionContextCMM.RequiredEncryptionContextCMM";
  }
}
