// Class SmallEncryptionContextVariation_AB
// Dafny class SmallEncryptionContextVariation_AB compiled into Java
package TestUtils_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SmallEncryptionContextVariation_AB extends SmallEncryptionContextVariation {
  public SmallEncryptionContextVariation_AB () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SmallEncryptionContextVariation_AB o = (SmallEncryptionContextVariation_AB)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestUtils.SmallEncryptionContextVariation.AB");
    return s.toString();
  }
}
