package aws.cryptography.mpl.testserver.tests;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import java.net.URI;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import software.amazon.smithy.java.client.http.JavaHttpClientTransport;

/**
 * Supplies the ONE generated Java Test_Client, pointed at a target's endpoint
 * (Requirement 1.5). The only per-target input is the URL.
 *
 * <p>Clients are <strong>cached per endpoint and reused</strong> (Requirement 9.3). A
 * smithy-java client is thread-safe and meant to be shared; its JDK {@code HttpClient}
 * holds a connection pool. Building one per operation opens an equal number of
 * short-lived pools and subjects the server to connection churn, which shows up under
 * parameterized load as intermittent {@code TransportException: ... received no bytes}
 * -- a reused-but-closed connection, or an overflowed listen backlog. One stable client
 * per endpoint keeps the pool warm and removes that failure mode.
 */
public final class TestServerClients {

    private static final Map<URI, MPLTestServerClient> CLIENTS = new ConcurrentHashMap<>();

    private TestServerClients() {
    }

    /** @return a shared, reused Test_Client for a target. */
    public static MPLTestServerClient forTarget(LanguageServerTarget target) {
        return forEndpoint(target.endpoint());
    }

    /** @return a shared, reused Test_Client for an endpoint. */
    public static MPLTestServerClient forEndpoint(URI endpoint) {
        return CLIENTS.computeIfAbsent(endpoint, TestServerClients::build);
    }

    private static MPLTestServerClient build(URI endpoint) {
        return MPLTestServerClient.builder()
            .endpoint(endpoint.toString())
            .transport(new JavaHttpClientTransport())
            .build();
    }
}
