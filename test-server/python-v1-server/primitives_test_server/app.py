# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Hand-implemented rpcv2Cbor HTTP server for the Python Primitives Language_Server.

Routes ``POST /service/PrimitivesTestServer/operation/<Op>``, decodes the CBOR
request body, dispatches to the operation handler, and encodes the CBOR response.
Each outcome is a modeled success response, a ``GenericServerError``, or a
``PrimitivesError``; the two errors serialize as a CBOR map carrying the
``__type`` discriminator (the error's absolute shape id) so the generated Java
Test_Client maps them back to the modeled type.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cbor2

from .primitives_bridge import OPERATIONS, PrimitivesError, ServerError

_NAMESPACE = "aws.cryptography.primitives.testserver"
_GENERIC_SERVER_ERROR = _NAMESPACE + "#GenericServerError"
_PRIMITIVES_ERROR = _NAMESPACE + "#PrimitivesError"
_SERVICE = "PrimitivesTestServer"
_SMITHY_PROTOCOL = "rpc-v2-cbor"
_CBOR_CONTENT_TYPE = "application/cbor"


def _route(path):
    """Return (service, operation) for /service/<S>/operation/<O>, else (None, None)."""
    parts = path.strip("/").split("/")
    if len(parts) == 4 and parts[0] == "service" and parts[2] == "operation":
        return parts[1], parts[3]
    return None, None


def _make_handler():
    class RpcV2CborHandler(BaseHTTPRequestHandler):
        # HTTP/1.1 with a Content-Length on every response keeps the smithy-java
        # client's pooled connections valid across the many requests the Tests make.
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def _send_cbor(self, status, payload):
            body = cbor2.dumps(payload)
            self.send_response(status)
            self.send_header("smithy-protocol", _SMITHY_PROTOCOL)
            self.send_header("Content-Type", _CBOR_CONTENT_TYPE)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _send_error(self, type_id, message):
            self._send_cbor(400, {"__type": type_id, "message": message})

        def do_POST(self):  # noqa: N802
            service, operation = _route(self.path)
            if service != _SERVICE:
                self._send_error(
                    _GENERIC_SERVER_ERROR, f"unknown service: {self.path}"
                )
                return
            if self.headers.get("smithy-protocol") != _SMITHY_PROTOCOL:
                self._send_error(
                    _GENERIC_SERVER_ERROR,
                    "missing or invalid smithy-protocol header; expected rpc-v2-cbor",
                )
                return
            handler = OPERATIONS.get(operation)
            if handler is None:
                self._send_error(
                    _GENERIC_SERVER_ERROR, f"unknown operation: {operation}"
                )
                return
            try:
                length = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(length) if length else b""
                request = cbor2.loads(raw) if raw else {}
                response = handler(request)
                self._send_cbor(200, response)
            except ServerError as exc:
                self._send_error(_GENERIC_SERVER_ERROR, str(exc))
            except PrimitivesError as exc:
                self._send_error(_PRIMITIVES_ERROR, str(exc))
            except Exception as exc:  # noqa: BLE001
                self._send_error(
                    _GENERIC_SERVER_ERROR, f"unexpected server error: {exc}"
                )

    return RpcV2CborHandler


class _PrimitivesThreadingHTTPServer(ThreadingHTTPServer):
    request_queue_size = 128
    daemon_threads = True
    allow_reuse_address = True


def serve(port, host="127.0.0.1"):
    """Start the Python Primitives Language_Server on host:port until stopped."""
    server = _PrimitivesThreadingHTTPServer((host, port), _make_handler())
    print(
        f"primitives-test-server (python) listening at http://{host}:{port}",
        flush=True,
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
