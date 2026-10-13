// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Runnable entry point for the .NET MPL Language_Server: binds an rpcv2Cbor
// HTTP endpoint on the port given as the first CLI argument (default 8102).

using MplTestServer;

var port = 8102;
if (args.Length > 0 && int.TryParse(args[0], out var parsed) && parsed is > 0 and <= 65535)
{
    port = parsed;
}

var server = new WireServer(port, new Handlers());
server.Start();
Console.Error.WriteLine($"listening at http://127.0.0.1:{port}");
await server.AcceptLoop;
