package software.amazon.cryptography.example.hierarchy;

import java.util.Collections;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;

public class BranchKeyReadTest {

  @Test
  public void test() {
    //noinspection unchecked
    BranchKeyReadExample.BranchKey(
      Fixtures.BRANCH_KEY_ID_WITH_UN_MODELED_EC,
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Collections.EMPTY_LIST,
      Fixtures.kmsClientWest2,
      Fixtures.ddbClientWest2
    );
  }
}
