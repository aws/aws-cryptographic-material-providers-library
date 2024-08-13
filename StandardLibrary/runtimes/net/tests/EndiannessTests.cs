using System;
using System.Numerics;
using System.Collections;

class TestEndianness {
    public static void Main(string[] args)
    {
        if (BitConverter.IsLittleEndian == false) {
            throw new SystemException("Not little endian"); 
        }
    }
}