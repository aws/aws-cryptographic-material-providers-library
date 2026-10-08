// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// rpcv2Cbor wire codec for the Primitives TestServer shapes. A request decodes
// from a CBOR map keyed by Smithy member name: blobs are byte strings, enums
// are their value strings, integers are CBOR integers. Responses and modeled
// errors encode as CBOR maps.

using System.Formats.Cbor;

namespace PrimitivesTestServer;

internal static class Model
{
    // Decodes the request body into a member-name -> value map. Byte strings
    // yield byte[], text strings string, integers long, booleans bool.
    internal static Dictionary<string, object> ReadMap(byte[] body)
    {
        try
        {
            var reader = new CborReader(body, CborConformanceMode.Lax);
            if (reader.PeekState() != CborReaderState.StartMap)
            {
                throw new FormatException($"expected a CBOR map, got {reader.PeekState()}");
            }
            var map = new Dictionary<string, object>();
            reader.ReadStartMap();
            while (reader.PeekState() != CborReaderState.EndMap)
            {
                var key = reader.ReadTextString();
                map[key] = ReadValue(reader);
            }
            reader.ReadEndMap();
            return map;
        }
        catch (Exception e)
        {
            throw ServerErrorException.Generic($"failed to decode CBOR request: {e.Message}");
        }
    }

    private static object ReadValue(CborReader reader) => reader.PeekState() switch
    {
        CborReaderState.ByteString => reader.ReadByteString(),
        CborReaderState.TextString => reader.ReadTextString(),
        CborReaderState.UnsignedInteger or CborReaderState.NegativeInteger => reader.ReadInt64(),
        CborReaderState.Boolean => reader.ReadBoolean(),
        CborReaderState.Null => ReadNull(reader),
        _ => throw new FormatException($"unsupported CBOR value {reader.PeekState()}"),
    };

    private static object ReadNull(CborReader reader)
    {
        reader.ReadNull();
        return null;
    }

    internal static byte[] Bytes(Dictionary<string, object> map, string member) =>
        map.TryGetValue(member, out var value) && value is byte[] bytes
            ? bytes
            : throw ServerErrorException.Generic($"missing or invalid blob member '{member}'");

    internal static string Str(Dictionary<string, object> map, string member) =>
        map.TryGetValue(member, out var value) && value is string text
            ? text
            : throw ServerErrorException.Generic($"missing or invalid string member '{member}'");

    internal static int Int(Dictionary<string, object> map, string member) =>
        map.TryGetValue(member, out var value) && value is long number
            ? checked((int)number)
            : throw ServerErrorException.Generic($"missing or invalid integer member '{member}'");

    // Encodes a response whose members are all blobs, in the given order.
    internal static byte[] WriteBlobs(params (string Member, byte[] Value)[] fields)
    {
        var writer = new CborWriter();
        writer.WriteStartMap(fields.Length);
        foreach (var (member, value) in fields)
        {
            writer.WriteTextString(member);
            writer.WriteByteString(value);
        }
        writer.WriteEndMap();
        return writer.Encode();
    }

    internal static byte[] WriteBool(string member, bool value)
    {
        var writer = new CborWriter();
        writer.WriteStartMap(1);
        writer.WriteTextString(member);
        writer.WriteBoolean(value);
        writer.WriteEndMap();
        return writer.Encode();
    }

    internal static byte[] WriteError(string typeId, string message)
    {
        var writer = new CborWriter();
        writer.WriteStartMap(2);
        writer.WriteTextString("__type");
        writer.WriteTextString(typeId);
        writer.WriteTextString("message");
        writer.WriteTextString(message);
        writer.WriteEndMap();
        return writer.Encode();
    }
}
