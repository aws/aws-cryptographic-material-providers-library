// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.primitives;

public class TestUtils {

  /** Convert a String of Hex to a Byte Array. */
  // See https://tiny.amazon.com/bhksn4so
  public static byte[] fromHex(String data) {
    byte[] result = new byte[data.length() / 2];
    for (int x = 0; x < result.length; x++) {
      result[x] = (byte) Integer.parseInt(data.substring(2 * x, 2 * x + 2), 16);
    }
    return result;
  }
}
