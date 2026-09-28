// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// rpcv2Cbor HTTP wire layer: routes POST
// /service/MPLTestServer/operation/{Operation}, validates the protocol
// headers, decodes the CBOR request body, dispatches to a handler, and encodes
// the CBOR response or a modeled error. Any exception escaping a handler
// becomes a modeled error so the server never leaks a bare HTTP error.

using System.Net;

namespace MplTestServer;

// One of the two modeled TestServer errors: GenericServerError for framework
// failures (bad headers, unknown operation, malformed input, bad handle),
// MPLClientError for a failure raised by the Material Providers Library.
internal sealed class ServerErrorException : Exception
{
    internal const string GenericType = "aws.cryptography.mpl.testserver#GenericServerError";
    internal const string MplType = "aws.cryptography.mpl.testserver#MPLClientError";

    internal string TypeId { get; }

    private ServerErrorException(string typeId, string message) : base(message)
    {
        TypeId = typeId;
    }

    internal static ServerErrorException Generic(string message) => new(GenericType, message);

    internal static ServerErrorException Mpl(string message) => new(MplType, message);
}

internal sealed class WireServer : IDisposable
{
    private const string SmithyProtocol = "rpc-v2-cbor";
    private const string CborContentType = "application/cbor";
    private const string ServiceName = "MPLTestServer";

    private readonly HttpListener _listener = new();
    private readonly Handlers _handlers;
    private Task _acceptLoop = Task.CompletedTask;

    internal WireServer(int port, Handlers handlers)
    {
        _handlers = handlers;
        _listener.Prefixes.Add($"http://127.0.0.1:{port}/");
    }

    // Completes when the listener stops.
    internal Task AcceptLoop => _acceptLoop;

    internal void Start()
    {
        _listener.Start();
        _acceptLoop = Task.Run(AcceptLoopAsync);
    }

    public void Dispose() => _listener.Close();

    private async Task AcceptLoopAsync()
    {
        while (_listener.IsListening)
        {
            HttpListenerContext context;
            try
            {
                context = await _listener.GetContextAsync();
            }
            catch (HttpListenerException)
            {
                break;
            }
            catch (ObjectDisposedException)
            {
                break;
            }
            // Each request runs on a worker so parallel clients aren't serialized.
            _ = Task.Run(() => Handle(context));
        }
    }

    private void Handle(HttpListenerContext context)
    {
        var (status, body) = Dispatch(context.Request);
        var response = context.Response;
        try
        {
            response.KeepAlive = true;
            response.StatusCode = status;
            response.Headers["smithy-protocol"] = SmithyProtocol;
            response.ContentType = CborContentType;
            // An explicit Content-Length keeps every response eligible for
            // HTTP/1.1 keep-alive (the generated Test_Client pools connections).
            response.ContentLength64 = body.Length;
            response.OutputStream.Write(body, 0, body.Length);
            response.Close();
        }
        catch (Exception)
        {
            response.Abort();
        }
    }

    // Runs one operation and returns the HTTP status and CBOR body. Every
    // outcome is a modeled success response, a GenericServerError, or an
    // MPLClientError.
    private (int Status, byte[] Body) Dispatch(HttpListenerRequest request)
    {
        try
        {
            return (200, DispatchOperation(request));
        }
        catch (ServerErrorException e)
        {
            return (400, Model.WriteError(e.TypeId, e.Message));
        }
        catch (Exception e)
        {
            return (400, Model.WriteError(ServerErrorException.GenericType, $"unexpected server error: {e.Message}"));
        }
    }

    private byte[] DispatchOperation(HttpListenerRequest request)
    {
        if (request.HttpMethod != "POST")
        {
            throw ServerErrorException.Generic($"unsupported method {request.HttpMethod}; expected POST");
        }
        var path = request.Url?.AbsolutePath ?? "";
        var parts = path.Trim('/').Split('/');
        if (parts.Length != 4 || parts[0] != "service" || parts[2] != "operation")
        {
            throw ServerErrorException.Generic($"unknown operation: {path}");
        }
        if (parts[1] != ServiceName)
        {
            throw ServerErrorException.Generic($"unknown service: {parts[1]}; expected {ServiceName}");
        }
        if (request.Headers["smithy-protocol"] != SmithyProtocol)
        {
            throw ServerErrorException.Generic($"missing or invalid smithy-protocol header; expected {SmithyProtocol}");
        }
        if (request.Headers["Content-Type"] != CborContentType)
        {
            throw ServerErrorException.Generic($"missing or invalid content-type; expected {CborContentType}");
        }
        using var buffer = new MemoryStream();
        request.InputStream.CopyTo(buffer);
        var payload = buffer.ToArray();

        return _handlers.Dispatch(parts[3], Model.ReadMap(payload));
    }
}
