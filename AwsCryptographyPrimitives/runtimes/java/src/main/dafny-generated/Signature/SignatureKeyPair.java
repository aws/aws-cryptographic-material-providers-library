// Class SignatureKeyPair
// Dafny class SignatureKeyPair compiled into Java
package Signature;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class SignatureKeyPair {
  public dafny.DafnySequence<? extends java.lang.Byte> _verificationKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _signingKey;
  public SignatureKeyPair (dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    this._verificationKey = verificationKey;
    this._signingKey = signingKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SignatureKeyPair o = (SignatureKeyPair)other;
    return true && java.util.Objects.equals(this._verificationKey, o._verificationKey) && java.util.Objects.equals(this._signingKey, o._signingKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._verificationKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signingKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Signature.SignatureKeyPair.SignatureKeyPair");
    s.append("(");
    s.append(dafny.Helpers.toString(this._verificationKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._signingKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SignatureKeyPair> _TYPE = dafny.TypeDescriptor.<SignatureKeyPair>referenceWithInitializer(SignatureKeyPair.class, () -> SignatureKeyPair.Default());
  public static dafny.TypeDescriptor<SignatureKeyPair> _typeDescriptor() {
    return (dafny.TypeDescriptor<SignatureKeyPair>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SignatureKeyPair theDefault = Signature.SignatureKeyPair.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static SignatureKeyPair Default() {
    return theDefault;
  }
  public static SignatureKeyPair create(dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    return new SignatureKeyPair(verificationKey, signingKey);
  }
  public static SignatureKeyPair create_SignatureKeyPair(dafny.DafnySequence<? extends java.lang.Byte> verificationKey, dafny.DafnySequence<? extends java.lang.Byte> signingKey) {
    return create(verificationKey, signingKey);
  }
  public boolean is_SignatureKeyPair() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_verificationKey() {
    return this._verificationKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_signingKey() {
    return this._signingKey;
  }
}
