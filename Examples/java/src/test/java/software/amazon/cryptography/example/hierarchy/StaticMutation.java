package software.amazon.cryptography.example.hierarchy;

import java.util.Collections;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.mutations.DescribeMutationExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

public class StaticMutation {

  public void createStaticMutationSystemKey() {
    final String bkid = "STATIC-PRE-HV-2-MUTATION-WITH-SYSTEM-KEY";
    //noinspection unchecked
    SystemKey systemKey = MutationsProvider.KmsSystemKey(
      Fixtures.KSA_SYSTEM_KEY,
      Fixtures.kmsClientWest2,
      Collections.EMPTY_LIST
    );
    DescribeMutationExample.CompleteExample(
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v1,
      bkid,
      systemKey,
      null,
      null
    );
    logIt(bkid);
  }

  public void createStaticMutationTrustStorage() {
    final String bkid = "STATIC-PRE-HV-2-MUTATION-WITH-TRUST-STORAGE";
    SystemKey systemKey = MutationsProvider.TrustStorage();
    DescribeMutationExample.CompleteExample(
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v1,
      bkid,
      systemKey,
      null,
      null
    );
    logIt(bkid);
  }

  private static void logIt(String bkid) {
    System.out.println(
      "Created Branch Key and started a Mutation for it." +
      " Started but did not complete a Mutation for it (it is in-flight)." +
      " The COMMITMENT will not have `hierarchy-version`." +
      " This allows us to write tests for reading pre-HV-2 MUTATIONs." +
      " Branch Key ID: " +
      bkid
    );
  }
  // Uncomment to re-create static test resources.
  // @Test
  // public void testStaticMutation() {
  //   createStaticMutationSystemKey();
  //   createStaticMutationTrustStorage();
  // }
}
