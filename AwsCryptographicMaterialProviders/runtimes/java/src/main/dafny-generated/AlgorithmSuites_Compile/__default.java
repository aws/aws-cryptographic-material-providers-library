// Class __default
// Dafny class __default compiled into Java
package AlgorithmSuites_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean SupportedESDKEncrypt_q(software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt e) {
    return (((true) && ((((((e).dtor_AES__GCM()).dtor_keyLength()) == (32)) || ((((e).dtor_AES__GCM()).dtor_keyLength()) == (24))) || ((((e).dtor_AES__GCM()).dtor_keyLength()) == (16)))) && ((((e).dtor_AES__GCM()).dtor_tagLength()) == (16))) && ((((e).dtor_AES__GCM()).dtor_ivLength()) == (12));
  }
  public static boolean SupportedDBEEncrypt_q(software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt e) {
    return (((true) && ((((e).dtor_AES__GCM()).dtor_keyLength()) == (32))) && ((((e).dtor_AES__GCM()).dtor_tagLength()) == (16))) && ((((e).dtor_AES__GCM()).dtor_ivLength()) == (12));
  }
  public static boolean SupportedDBEEDKWrapping_q(software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm p) {
    return (((((((p).is_IntermediateKeyWrapping()) && (true)) && ((((((p).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && ((((((p).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_tagLength()) == (16))) && ((((((p).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_ivLength()) == (12))) && ((((p).dtor_IntermediateKeyWrapping()).dtor_macKeyKdf()).is_HKDF())) && ((((p).dtor_IntermediateKeyWrapping()).dtor_keyEncryptionKeyKdf()).is_HKDF());
  }
  public static boolean KeyDerivationAlgorithm_q(software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm kdf) {
    return (!((true) && ((kdf).is_HKDF())) || (((((kdf).dtor_HKDF()).dtor_inputKeyLength()) == (((kdf).dtor_HKDF()).dtor_outputKeyLength())) && (!(java.util.Objects.equals(((kdf).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512())) || ((((kdf).dtor_HKDF()).dtor_inputKeyLength()) == (32))))) && (!((kdf).is_None()));
  }
  public static boolean CommitmentDerivationAlgorithm_q(software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm kdf) {
    return (!((true) && ((kdf).is_HKDF())) || (((((((kdf).dtor_HKDF()).dtor_hmac()).is_SHA__512()) && ((((kdf).dtor_HKDF()).dtor_saltLength()) == (32))) && ((((kdf).dtor_HKDF()).dtor_inputKeyLength()) == (32))) && ((((kdf).dtor_HKDF()).dtor_outputKeyLength()) == (32)))) && (!((kdf).is_IDENTITY()));
  }
  public static boolean EdkWrappingAlgorithm_q(software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm alg) {
    return ((((((alg).is_IntermediateKeyWrapping()) && ((((alg).dtor_IntermediateKeyWrapping()).dtor_keyEncryptionKeyKdf()).is_HKDF())) && ((((alg).dtor_IntermediateKeyWrapping()).dtor_macKeyKdf()).is_HKDF())) && (true)) && ((((((alg).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_keyLength()) == (32))) || ((alg).is_DIRECT__KEY__WRAPPING());
  }
  public static boolean AlgorithmSuiteInfo_q(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    return ((((((((__default.KeyDerivationAlgorithm_q((a).dtor_kdf())) && (__default.CommitmentDerivationAlgorithm_q((a).dtor_commitment()))) && (__default.EdkWrappingAlgorithm_q((a).dtor_edkWrapping()))) && (!(((a).dtor_kdf()).is_HKDF()) || ((true) && (((((a).dtor_kdf()).dtor_HKDF()).dtor_outputKeyLength()) == ((((a).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()))))) && (!(((a).dtor_signature()).is_ECDSA()) || (((a).dtor_kdf()).is_HKDF()))) && (!(((a).dtor_commitment()).is_HKDF()) || ((((((a).dtor_commitment()).dtor_HKDF()).dtor_saltLength()) == (32)) && (java.util.Objects.equals((a).dtor_commitment(), (a).dtor_kdf()))))) && (!(((a).dtor_edkWrapping()).is_IntermediateKeyWrapping()) || (((((a).dtor_kdf()).is_HKDF()) && (java.util.Objects.equals((((a).dtor_edkWrapping()).dtor_IntermediateKeyWrapping()).dtor_keyEncryptionKeyKdf(), (a).dtor_kdf()))) && (java.util.Objects.equals((((a).dtor_edkWrapping()).dtor_IntermediateKeyWrapping()).dtor_macKeyKdf(), (a).dtor_kdf()))))) && (!((((a).dtor_kdf()).is_HKDF()) && (((a).dtor_commitment()).is_None())) || (java.lang.Integer.signum(((((a).dtor_kdf()).dtor_HKDF()).dtor_saltLength())) == 0))) && (!(!(((a).dtor_symmetricSignature()).is_None())) || ((true) && (((a).dtor_edkWrapping()).is_IntermediateKeyWrapping())));
  }
  public static boolean ESDKAlgorithmSuite_q(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv0 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv1 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv2 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv3 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv4 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv5 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv6 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv7 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv8 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv9 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv10 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv11 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv12 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv13 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv14 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv15 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv16 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv17 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv18 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv19 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv20 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv21 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv22 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv23 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv24 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv25 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv26 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv27 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv28 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv29 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv30 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv31 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv32 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv33 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv34 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv35 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv36 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv37 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv38 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv39 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv40 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv41 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv42 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv43 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv44 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv45 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv46 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv47 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv48 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv49 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv50 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv51 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv52 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv53 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv54 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv55 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv56 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv57 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv58 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv59 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv60 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv61 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv62 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv63 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv64 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv65 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv66 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv67 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv68 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv69 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv70 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv71 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv72 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv73 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv74 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv75 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv76 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv77 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv78 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv79 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv80 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv81 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv82 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv83 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv84 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv85 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv86 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv87 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv88 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv89 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv90 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv91 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv92 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv93 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv94 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv95 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv96 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv97 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv98 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv99 = a;
    return ((__default.AlgorithmSuiteInfo_q(a)) && (__default.SupportedESDKEncrypt_q((a).dtor_encrypt()))) && (((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId, Boolean>)(_source0_boxed0) -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _source0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId)(java.lang.Object)(_source0_boxed0));
      if (_source0.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()) {
        return ((((((((((_pat_let_tv0).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 20))) && (((_pat_let_tv1).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv2).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (16))) && (((_pat_let_tv3).dtor_kdf()).is_IDENTITY())) && (((_pat_let_tv4).dtor_signature()).is_None())) && (((_pat_let_tv5).dtor_commitment()).is_None())) && (((_pat_let_tv6).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv7).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()) {
        return ((((((((((_pat_let_tv8).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 70))) && (((_pat_let_tv9).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv10).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (24))) && (((_pat_let_tv11).dtor_kdf()).is_IDENTITY())) && (((_pat_let_tv12).dtor_signature()).is_None())) && (((_pat_let_tv13).dtor_commitment()).is_None())) && (((_pat_let_tv14).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv15).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()) {
        return ((((((((((_pat_let_tv16).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 120))) && (((_pat_let_tv17).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv18).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv19).dtor_kdf()).is_IDENTITY())) && (((_pat_let_tv20).dtor_signature()).is_None())) && (((_pat_let_tv21).dtor_commitment()).is_None())) && (((_pat_let_tv22).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv23).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()) {
        return (((((((((((_pat_let_tv24).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 20))) && (((_pat_let_tv25).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv26).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (16))) && (((_pat_let_tv27).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv28).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256()))) && (((_pat_let_tv29).dtor_signature()).is_None())) && (((_pat_let_tv30).dtor_commitment()).is_None())) && (((_pat_let_tv31).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv32).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()) {
        return (((((((((((_pat_let_tv33).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 70))) && (((_pat_let_tv34).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv35).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (24))) && (((_pat_let_tv36).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv37).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256()))) && (((_pat_let_tv38).dtor_signature()).is_None())) && (((_pat_let_tv39).dtor_commitment()).is_None())) && (((_pat_let_tv40).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv41).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()) {
        return (((((((((((_pat_let_tv42).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 120))) && (((_pat_let_tv43).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv44).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv45).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv46).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256()))) && (((_pat_let_tv47).dtor_signature()).is_None())) && (((_pat_let_tv48).dtor_commitment()).is_None())) && (((_pat_let_tv49).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv50).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()) {
        return ((((((((((((_pat_let_tv51).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 2, (byte) 20))) && (((_pat_let_tv52).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv53).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (16))) && (((_pat_let_tv54).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv55).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256()))) && (((_pat_let_tv56).dtor_signature()).is_ECDSA())) && (java.util.Objects.equals((((_pat_let_tv57).dtor_signature()).dtor_ECDSA()).dtor_curve(), software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P256()))) && (((_pat_let_tv58).dtor_commitment()).is_None())) && (((_pat_let_tv59).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv60).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()) {
        return ((((((((((((_pat_let_tv61).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 70))) && (((_pat_let_tv62).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv63).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (24))) && (((_pat_let_tv64).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv65).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((_pat_let_tv66).dtor_signature()).is_ECDSA())) && (java.util.Objects.equals((((_pat_let_tv67).dtor_signature()).dtor_ECDSA()).dtor_curve(), software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384()))) && (((_pat_let_tv68).dtor_commitment()).is_None())) && (((_pat_let_tv69).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv70).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()) {
        return ((((((((((((_pat_let_tv71).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 120))) && (((_pat_let_tv72).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv73).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv74).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv75).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((_pat_let_tv76).dtor_signature()).is_ECDSA())) && (java.util.Objects.equals((((_pat_let_tv77).dtor_signature()).dtor_ECDSA()).dtor_curve(), software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384()))) && (((_pat_let_tv78).dtor_commitment()).is_None())) && (((_pat_let_tv79).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv80).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else if (_source0.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()) {
        return (((((((((((_pat_let_tv81).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 4, (byte) 120))) && (((_pat_let_tv82).dtor_messageVersion()) == (2))) && (true)) && (((((_pat_let_tv83).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv84).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv85).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512()))) && (((_pat_let_tv86).dtor_signature()).is_None())) && (((_pat_let_tv87).dtor_commitment()).is_HKDF())) && (((_pat_let_tv88).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv89).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      } else {
        return ((((((((((((_pat_let_tv90).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 5, (byte) 120))) && (((_pat_let_tv91).dtor_messageVersion()) == (2))) && (true)) && (((((_pat_let_tv92).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv93).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv94).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512()))) && (((_pat_let_tv95).dtor_signature()).is_ECDSA())) && (java.util.Objects.equals((((_pat_let_tv96).dtor_signature()).dtor_ECDSA()).dtor_curve(), software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384()))) && (((_pat_let_tv97).dtor_commitment()).is_HKDF())) && (((_pat_let_tv98).dtor_symmetricSignature()).is_None())) && (((_pat_let_tv99).dtor_edkWrapping()).is_DIRECT__KEY__WRAPPING());
      }
    }).apply(((a).dtor_id()).dtor_ESDK()));
  }
  public static boolean DBEAlgorithmSuite_q(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv0 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv1 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv2 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv3 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv4 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv5 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv6 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv7 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv8 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv9 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv10 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv11 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv12 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv13 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv14 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv15 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv16 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv17 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv18 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv19 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv20 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv21 = a;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _pat_let_tv22 = a;
    return (((__default.AlgorithmSuiteInfo_q(a)) && (__default.SupportedDBEEncrypt_q((a).dtor_encrypt()))) && (__default.SupportedDBEEDKWrapping_q((a).dtor_edkWrapping()))) && (((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId, Boolean>)(_source0_boxed0) -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _source0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId)(java.lang.Object)(_source0_boxed0));
      if (_source0.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()) {
        return ((((((((((((((_pat_let_tv0).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 0))) && (((_pat_let_tv1).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv2).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv3).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv4).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512()))) && (((_pat_let_tv5).dtor_signature()).is_None())) && (((_pat_let_tv6).dtor_commitment()).is_HKDF())) && (((_pat_let_tv7).dtor_symmetricSignature()).is_HMAC())) && (java.util.Objects.equals(((_pat_let_tv8).dtor_symmetricSignature()).dtor_HMAC(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((_pat_let_tv9).dtor_edkWrapping()).is_IntermediateKeyWrapping())) && (true)) && (((((((_pat_let_tv10).dtor_edkWrapping()).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_keyLength()) == (32));
      } else {
        return (((((((((((((((_pat_let_tv11).dtor_binaryId()).equals(dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 1))) && (((_pat_let_tv12).dtor_messageVersion()) == (1))) && (true)) && (((((_pat_let_tv13).dtor_encrypt()).dtor_AES__GCM()).dtor_keyLength()) == (32))) && (((_pat_let_tv14).dtor_kdf()).is_HKDF())) && (java.util.Objects.equals((((_pat_let_tv15).dtor_kdf()).dtor_HKDF()).dtor_hmac(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512()))) && (((_pat_let_tv16).dtor_signature()).is_ECDSA())) && (java.util.Objects.equals((((_pat_let_tv17).dtor_signature()).dtor_ECDSA()).dtor_curve(), software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384()))) && (((_pat_let_tv18).dtor_commitment()).is_HKDF())) && (((_pat_let_tv19).dtor_symmetricSignature()).is_HMAC())) && (java.util.Objects.equals(((_pat_let_tv20).dtor_symmetricSignature()).dtor_HMAC(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((_pat_let_tv21).dtor_edkWrapping()).is_IntermediateKeyWrapping())) && (true)) && (((((((_pat_let_tv22).dtor_edkWrapping()).dtor_IntermediateKeyWrapping()).dtor_pdkEncryptAlgorithm()).dtor_AES__GCM()).dtor_keyLength()) == (32));
      }
    }).apply(((a).dtor_id()).dtor_DBE()));
  }
  public static boolean AlgorithmSuite_q(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _source0 = (a).dtor_id();
    if (_source0.is_ESDK()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_ESDK)_source0)._ESDK;
      return __default.ESDKAlgorithmSuite_q(a);
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _1___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_DBE)_source0)._DBE;
      return __default.DBEAlgorithmSuite_q(a);
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm HKDF__SHA__256(int keyLength) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_HKDF(software.amazon.cryptography.materialproviders.internaldafny.types.HKDF.create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256(), 0, keyLength, keyLength));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm HKDF__SHA__384(int keyLength) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_HKDF(software.amazon.cryptography.materialproviders.internaldafny.types.HKDF.create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384(), 0, keyLength, keyLength));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm HKDF__SHA__512(int keyLength) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_HKDF(software.amazon.cryptography.materialproviders.internaldafny.types.HKDF.create(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__512(), 32, keyLength, keyLength));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo GetSuite(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId id) {
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId _source0 = id;
    if (_source0.is_ESDK()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_ESDK)_source0)._ESDK;
      software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId _1_e = _0___mcc_h0;
      return __default.GetESDKSuite(_1_e);
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _2___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId_DBE)_source0)._DBE;
      software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId _3_e = _2___mcc_h1;
      return __default.GetDBESuite(_3_e);
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo GetDBESuite(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId id) {
    return ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)((__default.SupportedDBEAlgorithmSuites()).get(id)));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo GetESDKSuite(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId id) {
    return ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)((__default.SupportedESDKAlgorithmSuites()).get(id)));
  }
  public static int GetEncryptKeyLength(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt _source0 = (a).dtor_encrypt();
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt)_source0)._AES__GCM;
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_e = _0___mcc_h0;
    return (_1_e).dtor_keyLength();
  }
  public static int GetEncryptTagLength(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt _source0 = (a).dtor_encrypt();
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt)_source0)._AES__GCM;
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_e = _0___mcc_h0;
    return (_1_e).dtor_tagLength();
  }
  public static int GetEncryptIvLength(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo a) {
    software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt _source0 = (a).dtor_encrypt();
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt)_source0)._AES__GCM;
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_e = _0___mcc_h0;
    return (_1_e).dtor_ivLength();
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetAlgorithmSuiteInfo(dafny.DafnySequence<? extends java.lang.Byte> binaryId_q) {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (__default.AlgorithmSuiteInfoByBinaryId()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(binaryId_q), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid BinaryId")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AlgorithmSuite._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(AlgorithmSuite._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)((__default.AlgorithmSuiteInfoByBinaryId()).get(binaryId_q))));
    }
  }
  public static int Bits128()
  {
    return 16;
  }
  public static int TagLen()
  {
    return 16;
  }
  public static int IvLen()
  {
    return 12;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt AES__128__GCM__IV12__TAG16()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt.create(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(__default.Bits128(), __default.TagLen(), __default.IvLen()));
  }
  public static int Bits192()
  {
    return 24;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt AES__192__GCM__IV12__TAG16()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt.create(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(__default.Bits192(), __default.TagLen(), __default.IvLen()));
  }
  public static int Bits256()
  {
    return 32;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt AES__256__GCM__IV12__TAG16()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Encrypt.create(software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(__default.Bits256(), __default.TagLen(), __default.IvLen()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_IntermediateKeyWrapping(software.amazon.cryptography.materialproviders.internaldafny.types.IntermediateKeyWrapping.create(__default.HKDF__SHA__512(__default.Bits256()), __default.HKDF__SHA__512(__default.Bits256()), __default.AES__256__GCM__IV12__TAG16()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 0), 1, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__512(__default.Bits256()), __default.HKDF__SHA__512(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_HMAC(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()), __default.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512());
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_DBE(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()), dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 1), 1, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__512(__default.Bits256()), __default.HKDF__SHA__512(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384())), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_HMAC(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()), __default.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512());
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 20), 1, __default.AES__128__GCM__IV12__TAG16(), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_IDENTITY(software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY.create()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 70), 1, __default.AES__192__GCM__IV12__TAG16(), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_IDENTITY(software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY.create()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 120), 1, __default.AES__256__GCM__IV12__TAG16(), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_IDENTITY(software.amazon.cryptography.materialproviders.internaldafny.types.IDENTITY.create()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 20), 1, __default.AES__128__GCM__IV12__TAG16(), __default.HKDF__SHA__256(__default.Bits128()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 70), 1, __default.AES__192__GCM__IV12__TAG16(), __default.HKDF__SHA__256(__default.Bits192()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 120), 1, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__256(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), dafny.DafnySequence.<java.lang.Byte> of((byte) 2, (byte) 20), 1, __default.AES__128__GCM__IV12__TAG16(), __default.HKDF__SHA__256(__default.Bits128()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P256())), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 70), 1, __default.AES__192__GCM__IV12__TAG16(), __default.HKDF__SHA__384(__default.Bits192()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384())), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 120), 1, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__384(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.DerivationAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384())), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), dafny.DafnySequence.<java.lang.Byte> of((byte) 4, (byte) 120), 2, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__512(__default.Bits256()), __default.HKDF__SHA__512(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo.create(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteId.create_ESDK(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), dafny.DafnySequence.<java.lang.Byte> of((byte) 5, (byte) 120), 2, __default.AES__256__GCM__IV12__TAG16(), __default.HKDF__SHA__512(__default.Bits256()), __default.HKDF__SHA__512(__default.Bits256()), software.amazon.cryptography.materialproviders.internaldafny.types.SignatureAlgorithm.create_ECDSA(software.amazon.cryptography.materialproviders.internaldafny.types.ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.create_ECDSA__P384())), software.amazon.cryptography.materialproviders.internaldafny.types.SymmetricSignatureAlgorithm.create_None(software.amazon.cryptography.materialproviders.internaldafny.types.None.create()), software.amazon.cryptography.materialproviders.internaldafny.types.EdkWrappingAlgorithm.create_DIRECT__KEY__WRAPPING(software.amazon.cryptography.materialproviders.internaldafny.types.DIRECT__KEY__WRAPPING.create()));
  }
  public static dafny.DafnyMap<? extends software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId, ? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> SupportedESDKAlgorithmSuites()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(), __default.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(), __default.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()));
  }
  public static dafny.DafnyMap<? extends software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId, ? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> SupportedDBEAlgorithmSuites()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(), __default.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), new dafny.Tuple2(software.amazon.cryptography.materialproviders.internaldafny.types.DBEAlgorithmSuiteId.create_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(), __default.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> AlgorithmSuiteInfoByBinaryId()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 20), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 70), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 0, (byte) 120), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 20), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 70), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 1, (byte) 120), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 2, (byte) 20), __default.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 70), __default.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 3, (byte) 120), __default.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 4, (byte) 120), __default.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 5, (byte) 120), __default.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 0), __default.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), new dafny.Tuple2(dafny.DafnySequence.<java.lang.Byte> of((byte) 103, (byte) 1), __default.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()));
  }
  @Override
  public java.lang.String toString() {
    return "AlgorithmSuites._default";
  }
}
