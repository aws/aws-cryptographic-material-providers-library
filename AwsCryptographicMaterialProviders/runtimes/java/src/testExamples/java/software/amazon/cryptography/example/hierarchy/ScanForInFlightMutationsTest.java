package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.ScanForInFlightMutations.PageResult;

public class ScanForInFlightMutationsTest {

  @Test
  public void testScanForInFlightMutations() {
    ScanForInFlightMutations underTest = new ScanForInFlightMutations(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      null
    );
    PageResult actual = underTest.scanForMutationLock(null);
    assert actual.lastEvaluatedKey() != null;
    assert actual.inFlightMutations().isEmpty();
    while (actual.lastEvaluatedKey() != null) {
      actual = underTest.scanForMutationLock(actual.lastEvaluatedKey());
      if (!actual.inFlightMutations().isEmpty()) {
        System.out.println(actual.inFlightMutations());
      }
    }
  }
}
