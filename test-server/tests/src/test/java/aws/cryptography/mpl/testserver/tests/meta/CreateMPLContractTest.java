package aws.cryptography.mpl.testserver.tests.meta;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.CreateMPLInput;
import aws.cryptography.mpl.testserver.client.model.CreateMPLOutput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersConfig;
import aws.cryptography.mpl.testserver.tests.LanguageServerRegistry;
import aws.cryptography.mpl.testserver.tests.TestServerClients;
import java.util.UUID;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * The {@code CreateMPL} + handle contract, over the real wire.
 *
 * <p>Handles are the mechanism that makes the whole TestServer possible -- the MPL's
 * constructors return polymorph references that cannot be serialized -- so their
 * behavior is verified directly rather than inferred from a round-trip.
 *
 * <p>Note the accessor style: smithy-java generates JavaBean getters
 * ({@code getMplId()}) for reading a shape but member-named setters
 * ({@code .mplId(...)}) on its builder. This holds in both client and server mode.
 */
class CreateMPLContractTest {

    private static MPLTestServerClient client;

    @BeforeAll
    static void resolveTarget() {
        client = TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
    }

    private static CreateMPLOutput createMpl() {
        return client.createMPL(CreateMPLInput.builder()
            .config(MaterialProvidersConfig.builder().build())
            .build());
    }

    @Test
    @DisplayName("CreateMPL returns exactly one non-empty handle")
    void createMplReturnsNonEmptyHandle() {
        CreateMPLOutput output = createMpl();

        assertNotNull(output.getMplId(), "CreateMPL must return an mplId");
        assertFalse(output.getMplId().isEmpty(), "the returned mplId must be non-empty");
        // A UUID is not part of the wire contract, but it is what the registry promises.
        // A non-UUID would mean the registry stopped minting its own ids -- better caught
        // here than as a mystery collision later.
        UUID.fromString(output.getMplId());
    }

    @Test
    @DisplayName("Each CreateMPL yields a distinct handle, so instances are independent")
    void handlesAreDistinct() {
        String first = createMpl().getMplId();
        String second = createMpl().getMplId();

        // Distinctness is what lets a test hold two differently configured
        // MaterialProviders instances at once and know which one it is using.
        assertNotEquals(first, second, "two CreateMPL calls must return different handles");
    }
}
