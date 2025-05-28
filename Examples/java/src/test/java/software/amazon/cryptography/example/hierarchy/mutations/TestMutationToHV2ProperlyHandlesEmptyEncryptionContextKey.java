package software.amazon.cryptography.example.hierarchy.mutations;

import org.testng.annotations.BeforeSuite;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class TestMutationToHV2ProperlyHandlesEmptyEncryptionContextKey {

  static final String testPrefix = "mutation-to-hv-2-properly-handles-empty-encryption-context-key-java-test-";
  private String testBranchKeyId;
  private static final Map<String, String> encryptionContext;
  static {
    // Initial Capacity of 8 b/c we have 8 key-pairs
    // LoadFactor greater than 1 should ensure that we never re-size the hash map
    Map<String, String> _encryptionContext = new HashMap<>(8, 2);
    _encryptionContext.put("\n", "newline");
    _encryptionContext.put("\t", "tab");
    _encryptionContext.put("\r", "carriage-return");
    _encryptionContext.put(" ", "space");
    _encryptionContext.put("", "empty");
    _encryptionContext.put("NormalKey", "Value with\nspecial\rchars\t");
    _encryptionContext.put("\u0007", "bell-unicode");
    _encryptionContext.put("\u0001", "unicode");
    encryptionContext = Collections.unmodifiableMap(_encryptionContext);
  }

  @BeforeSuite
  public void createHV1WithAnEmptyEncryptionContextKey() {
    testBranchKeyId = testPrefix + UUID.randomUUID().toString();

  }

}
