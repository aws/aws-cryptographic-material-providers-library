package aws.cryptography.primitives.testserver.server;

import com.fasterxml.jackson.databind.node.ObjectNode;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.concurrent.Executors;
import software.amazon.cryptography.primitives.AtomicPrimitives;
import software.amazon.cryptography.primitives.model.CryptoConfig;

/** rpcv2Cbor HTTP Language_Server for the Primitives TestServer. */
public final class ServerMain {

    private static final String SERVICE = "PrimitivesTestServer";
    private static final String PROTOCOL = "rpc-v2-cbor";
    private static final String CONTENT_TYPE = "application/cbor";
    private static final int DEFAULT_PORT = 8110;

    private final Operations operations;

    private ServerMain(Operations operations) {
        this.operations = operations;
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        int port = args.length > 0 ? Integer.parseInt(args[0]) : DEFAULT_PORT;
        AtomicPrimitives primitives = AtomicPrimitives.builder()
            .CryptoConfig(CryptoConfig.builder().build())
            .build();
        ServerMain server = new ServerMain(new Operations(primitives));

        HttpServer http = HttpServer.create(new InetSocketAddress("127.0.0.1", port), 0);
        http.createContext("/", server::handle);
        http.setExecutor(Executors.newFixedThreadPool(4));
        http.start();
        System.out.println("Primitives TestServer (java) listening on http://127.0.0.1:" + port);
        Thread.currentThread().join();
    }

    private void handle(HttpExchange exchange) throws IOException {
        try {
            byte[] body = exchange.getRequestBody().readAllBytes();
            try {
                String operation = route(exchange.getRequestURI().getPath());
                requireProtocol(exchange);
                ObjectNode response = operations.dispatch(operation, Cbor.decode(body));
                write(exchange, 200, Cbor.encode(response));
            } catch (ModeledError e) {
                writeError(exchange, e);
            } catch (RuntimeException e) {
                writeError(exchange, ModeledError.primitives(messageOf(e)));
            }
        } finally {
            exchange.close();
        }
    }

    private static String route(String path) {
        String[] parts = path.split("/");
        if (parts.length != 5 || !"service".equals(parts[1]) || !"operation".equals(parts[3])) {
            throw ModeledError.generic("unexpected path: " + path);
        }
        if (!SERVICE.equals(parts[2])) {
            throw ModeledError.generic("unknown service: " + parts[2] + "; expected " + SERVICE);
        }
        return parts[4];
    }

    private static void requireProtocol(HttpExchange exchange) {
        String protocol = exchange.getRequestHeaders().getFirst("smithy-protocol");
        if (!PROTOCOL.equals(protocol)) {
            throw ModeledError.generic(
                "missing or invalid smithy-protocol header; expected " + PROTOCOL);
        }
    }

    private static void write(HttpExchange exchange, int status, byte[] body) throws IOException {
        exchange.getResponseHeaders().set("smithy-protocol", PROTOCOL);
        exchange.getResponseHeaders().set("Content-Type", CONTENT_TYPE);
        exchange.sendResponseHeaders(status, body.length);
        try (OutputStream out = exchange.getResponseBody()) {
            out.write(body);
        }
    }

    private static void writeError(HttpExchange exchange, ModeledError error) throws IOException {
        ObjectNode body = Cbor.object();
        body.put("__type", error.typeId());
        body.put("message", error.getMessage() == null ? "" : error.getMessage());
        write(exchange, 400, Cbor.encode(body));
    }

    private static String messageOf(RuntimeException e) {
        return e.getMessage() == null ? e.toString() : e.getMessage();
    }
}
