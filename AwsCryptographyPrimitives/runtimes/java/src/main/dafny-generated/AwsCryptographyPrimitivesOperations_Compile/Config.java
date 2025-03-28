// Class Config
// Dafny class Config compiled into Java
package AwsCryptographyPrimitivesOperations_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class Config {
  public Config () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Config o = (Config)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesOperations.Config.Config");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Config> _TYPE = dafny.TypeDescriptor.<Config>referenceWithInitializer(Config.class, () -> Config.Default());
  public static dafny.TypeDescriptor<Config> _typeDescriptor() {
    return (dafny.TypeDescriptor<Config>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Config theDefault = AwsCryptographyPrimitivesOperations_Compile.Config.create();
  public static Config Default() {
    return theDefault;
  }
  public static Config create() {
    return new Config();
  }
  public static Config create_Config() {
    return create();
  }
  public boolean is_Config() { return true; }
  public static java.util.ArrayList<Config> AllSingletonConstructors() {
    java.util.ArrayList<Config> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Config());
    return singleton_iterator;
  }
}
