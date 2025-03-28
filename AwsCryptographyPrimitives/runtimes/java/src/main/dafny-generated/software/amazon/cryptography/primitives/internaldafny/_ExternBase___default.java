// Class _ExternBase___default
// Dafny class __default compiled into Java
package software.amazon.cryptography.primitives.internaldafny;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;
import Digest_Compile.*;
import HMAC.*;
import WrappedHMAC_Compile.*;
import HKDF_Compile.*;
import WrappedHKDF_Compile.*;
import Signature.*;
import KdfCtr_Compile.*;
import RSAEncryption.*;
import ECDH.*;
import AwsCryptographyPrimitivesOperations_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.CryptoConfig DefaultCryptoConfig() {
    return software.amazon.cryptography.primitives.internaldafny.types.CryptoConfig.create();
  }
  public static Wrappers_Compile.Result<AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> AtomicPrimitives(software.amazon.cryptography.primitives.internaldafny.types.CryptoConfig config)
  {
    Wrappers_Compile.Result<AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> res = (Wrappers_Compile.Result<AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    AtomicPrimitivesClient _0_client;
    AtomicPrimitivesClient _nw0 = new AtomicPrimitivesClient();
    _nw0.__ctor(AwsCryptographyPrimitivesOperations_Compile.Config.create());
    _0_client = _nw0;
    res = Wrappers_Compile.Result.<AtomicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AtomicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(AtomicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _0_client);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateSuccessOfClient(software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient client) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), client);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateFailureOfError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "AtomicPrimitives._default";
  }
}
