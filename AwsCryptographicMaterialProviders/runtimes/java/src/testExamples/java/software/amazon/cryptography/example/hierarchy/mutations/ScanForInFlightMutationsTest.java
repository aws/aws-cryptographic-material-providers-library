package software.amazon.cryptography.example.hierarchy.mutations;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.mutations.ScanForInFlightMutations.PageResult;

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
    final short pageLimit = 5;
    short pageIndex = 0;
    while (actual.lastEvaluatedKey() != null && pageIndex < pageLimit) {
      actual = underTest.scanForMutationLock(actual.lastEvaluatedKey());
      if (!actual.inFlightMutations().isEmpty()) {
        System.out.println(actual.inFlightMutations());
      }
      pageIndex++;
    }
  }
}
