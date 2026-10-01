// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// CBOR value tree for the rpcv2Cbor wire: maps decode to
// Dictionary<string, object>, arrays to List<object>, blobs to byte[], text to
// string, integers to long. Accessors raise GenericServerError on a missing or
// mistyped required member, since that is the harness's fault.

using System.Formats.Cbor;

namespace MplTestServer;

internal static class Model
{
    internal static Dictionary<string, object> ReadMap(byte[] body)
    {
        try
        {
            var reader = new CborReader(body, CborConformanceMode.Lax);
            if (ReadValue(reader) is Dictionary<string, object> map)
            {
                return map;
            }
            throw new FormatException("request body is not a CBOR map");
        }
        catch (ServerErrorException)
        {
            throw;
        }
        catch (Exception e)
        {
            throw ServerErrorException.Generic($"failed to decode CBOR request: {e.Message}");
        }
    }

    private static object ReadValue(CborReader reader)
    {
        switch (reader.PeekState())
        {
            case CborReaderState.StartMap:
                var map = new Dictionary<string, object>();
                reader.ReadStartMap();
                while (reader.PeekState() != CborReaderState.EndMap)
                {
                    var key = reader.ReadTextString();
                    map[key] = ReadValue(reader);
                }
                reader.ReadEndMap();
                return map;
            case CborReaderState.StartArray:
                var list = new List<object>();
                reader.ReadStartArray();
                while (reader.PeekState() != CborReaderState.EndArray)
                {
                    list.Add(ReadValue(reader));
                }
                reader.ReadEndArray();
                return list;
            case CborReaderState.ByteString:
                return reader.ReadByteString();
            case CborReaderState.TextString:
                return reader.ReadTextString();
            case CborReaderState.UnsignedInteger:
            case CborReaderState.NegativeInteger:
                return reader.ReadInt64();
            case CborReaderState.Boolean:
                return reader.ReadBoolean();
            case CborReaderState.Null:
                reader.ReadNull();
                return null;
            default:
                throw new FormatException($"unsupported CBOR value {reader.PeekState()}");
        }
    }

    internal static bool Present(Dictionary<string, object> map, string member) =>
        map.TryGetValue(member, out var value) && value != null;

    internal static T Member<T>(Dictionary<string, object> map, string member, string kind) =>
        map.TryGetValue(member, out var value) && value is T typed
            ? typed
            : throw ServerErrorException.Generic($"missing or non-{kind} member '{member}'");

    internal static byte[] Bytes(Dictionary<string, object> map, string member) =>
        Member<byte[]>(map, member, "blob");

    internal static MemoryStream OptionalBlob(Dictionary<string, object> map, string member) =>
        Present(map, member) ? new MemoryStream(Bytes(map, member)) : null;

    internal static string Str(Dictionary<string, object> map, string member) =>
        Member<string>(map, member, "string");

    internal static long Long(Dictionary<string, object> map, string member) =>
        Member<long>(map, member, "integer");

    internal static Dictionary<string, object> Map(Dictionary<string, object> map, string member) =>
        Member<Dictionary<string, object>>(map, member, "structure");

    internal static List<object> List(Dictionary<string, object> map, string member) =>
        Member<List<object>>(map, member, "list");

    /// A string-to-string map member; absent means empty.
    internal static Dictionary<string, string> StringMap(Dictionary<string, object> map, string member)
    {
        var result = new Dictionary<string, string>();
        if (!Present(map, member))
        {
            return result;
        }
        foreach (var (key, value) in Map(map, member))
        {
            result[key] = value as string
                ?? throw ServerErrorException.Generic($"map value is not a string: {member}.{key}");
        }
        return result;
    }

    /// A list-of-strings member; absent means empty.
    internal static List<string> StringList(Dictionary<string, object> map, string member)
    {
        var result = new List<string>();
        if (!Present(map, member))
        {
            return result;
        }
        foreach (var element in List(map, member))
        {
            result.Add(element as string
                ?? throw ServerErrorException.Generic($"list element is not a string: {member}"));
        }
        return result;
    }

    /// A list-of-blobs member, or null when absent.
    internal static List<MemoryStream> OptionalBlobList(Dictionary<string, object> map, string member)
    {
        if (!Present(map, member))
        {
            return null;
        }
        var result = new List<MemoryStream>();
        foreach (var element in List(map, member))
        {
            result.Add(new MemoryStream(element as byte[]
                ?? throw ServerErrorException.Generic($"list element is not a blob: {member}")));
        }
        return result;
    }

    internal static byte[] Write(Dictionary<string, object> map)
    {
        var writer = new CborWriter();
        WriteValue(writer, map);
        return writer.Encode();
    }

    private static void WriteValue(CborWriter writer, object value)
    {
        switch (value)
        {
            case null:
                writer.WriteNull();
                break;
            case Dictionary<string, object> map:
                // Absent optional members are omitted rather than sent as null.
                var present = map.Where(entry => entry.Value != null).ToList();
                writer.WriteStartMap(present.Count);
                foreach (var (key, entry) in present)
                {
                    writer.WriteTextString(key);
                    WriteValue(writer, entry);
                }
                writer.WriteEndMap();
                break;
            case Dictionary<string, string> strings:
                writer.WriteStartMap(strings.Count);
                foreach (var (key, entry) in strings)
                {
                    writer.WriteTextString(key);
                    writer.WriteTextString(entry);
                }
                writer.WriteEndMap();
                break;
            case IEnumerable<object> list when value is not string:
                var items = list.ToList();
                writer.WriteStartArray(items.Count);
                foreach (var item in items)
                {
                    WriteValue(writer, item);
                }
                writer.WriteEndArray();
                break;
            case byte[] bytes:
                writer.WriteByteString(bytes);
                break;
            case MemoryStream stream:
                writer.WriteByteString(stream.ToArray());
                break;
            case string text:
                writer.WriteTextString(text);
                break;
            case long number:
                writer.WriteInt64(number);
                break;
            default:
                throw new InvalidOperationException($"cannot encode {value.GetType()}");
        }
    }

    internal static byte[] WriteError(string typeId, string message) =>
        Write(new Dictionary<string, object> { ["__type"] = typeId, ["message"] = message ?? "" });
}
