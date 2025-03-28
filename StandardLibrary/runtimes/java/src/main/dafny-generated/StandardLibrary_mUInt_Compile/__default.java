// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_mUInt_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;
import Utf16EncodingForm_Compile.*;
import UnicodeStrings_Compile.*;
import FileIO_Compile.*;
import MulInternals_Compile.*;
import ModInternals_Compile.*;
import DivInternals_Compile.*;
import Power_Compile.*;
import Logarithm_Compile.*;
import StandardLibraryInterop_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean UInt8Less(byte a, byte b)
  {
    return java.lang.Integer.compareUnsigned(a, b) < 0;
  }
  public static <__T> boolean HasUint16Len(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s)
  {
    return (java.math.BigInteger.valueOf((s).length())).compareTo(__default.UINT16__LIMIT()) < 0;
  }
  public static <__T> boolean HasUint32Len(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s)
  {
    return (java.math.BigInteger.valueOf((s).length())).compareTo(__default.UINT32__LIMIT()) < 0;
  }
  public static <__T> boolean HasUint64Len(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s)
  {
    return (java.math.BigInteger.valueOf((s).length())).compareTo(__default.UINT64__LIMIT()) < 0;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> UInt16ToSeq(short x) {
    byte _0_b0 = ((byte) (dafny.Helpers.divideUnsignedShort(x, (short) 256)));
    byte _1_b1 = ((byte) (dafny.Helpers.remainderUnsignedShort(x, (short) 256)));
    return dafny.DafnySequence.<java.lang.Byte> of(_0_b0, _1_b1);
  }
  public static short SeqToUInt16(dafny.DafnySequence<? extends java.lang.Byte> s) {
    short _0_x0 = (short) (short) ((short)(((short) java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * ((short) 256)));
    return (short) (short) ((short)((_0_x0) + ((short) java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> UInt32ToSeq(int x) {
    byte _0_b0 = ((byte) (java.lang.Integer.divideUnsigned(x, 16777216)));
    int _1_x0 = (int) ((x) - ((int) ((java.lang.Byte.toUnsignedInt(_0_b0)) * (16777216))));
    byte _2_b1 = ((byte) (java.lang.Integer.divideUnsigned(_1_x0, 65536)));
    int _3_x1 = (int) ((_1_x0) - ((int) ((java.lang.Byte.toUnsignedInt(_2_b1)) * (65536))));
    byte _4_b2 = ((byte) (java.lang.Integer.divideUnsigned(_3_x1, 256)));
    byte _5_b3 = ((byte) (java.lang.Integer.remainderUnsigned(_3_x1, 256)));
    return dafny.DafnySequence.<java.lang.Byte> of(_0_b0, _2_b1, _4_b2, _5_b3);
  }
  public static int SeqToUInt32(dafny.DafnySequence<? extends java.lang.Byte> s) {
    int _0_x0 = (int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * (16777216));
    int _1_x1 = (int) ((_0_x0) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))))) * (65536))));
    int _2_x2 = (int) ((_1_x1) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))))) * (256))));
    return (int) ((_2_x2) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> UInt64ToSeq(long x) {
    byte _0_b0 = ((byte) ((long) java.lang.Long.divideUnsigned(x, (long) 72057594037927936L)));
    long _1_x0 = (long) (long) ((x) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_0_b0)) * ((long) 72057594037927936L))));
    byte _2_b1 = ((byte) ((long) java.lang.Long.divideUnsigned(_1_x0, (long) 281474976710656L)));
    long _3_x1 = (long) (long) ((_1_x0) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_2_b1)) * ((long) 281474976710656L))));
    byte _4_b2 = ((byte) ((long) java.lang.Long.divideUnsigned(_3_x1, (long) 1099511627776L)));
    long _5_x2 = (long) (long) ((_3_x1) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_4_b2)) * ((long) 1099511627776L))));
    byte _6_b3 = ((byte) ((long) java.lang.Long.divideUnsigned(_5_x2, (long) 4294967296L)));
    long _7_x3 = (long) (long) ((_5_x2) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_6_b3)) * ((long) 4294967296L))));
    byte _8_b4 = ((byte) ((long) java.lang.Long.divideUnsigned(_7_x3, (long) 16777216L)));
    long _9_x4 = (long) (long) ((_7_x3) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_8_b4)) * ((long) 16777216L))));
    byte _10_b5 = ((byte) ((long) java.lang.Long.divideUnsigned(_9_x4, (long) 65536L)));
    long _11_x5 = (long) (long) ((_9_x4) - ((long) (long) (((long) java.lang.Byte.toUnsignedLong(_10_b5)) * ((long) 65536L))));
    byte _12_b6 = ((byte) ((long) java.lang.Long.divideUnsigned(_11_x5, (long) 256L)));
    byte _13_b7 = ((byte) ((long) java.lang.Long.remainderUnsigned(_11_x5, (long) 256L)));
    return dafny.DafnySequence.<java.lang.Byte> of(_0_b0, _2_b1, _4_b2, _6_b3, _8_b4, _10_b5, _12_b6, _13_b7);
  }
  public static long SeqToUInt64(dafny.DafnySequence<? extends java.lang.Byte> s) {
    long _0_x0 = (long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * ((long) 72057594037927936L));
    long _1_x1 = (long) (long) ((_0_x0) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))))) * ((long) 281474976710656L))));
    long _2_x2 = (long) (long) ((_1_x1) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))))) * ((long) 1099511627776L))));
    long _3_x3 = (long) (long) ((_2_x2) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))))) * ((long) 4294967296L))));
    long _4_x4 = (long) (long) ((_3_x3) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(4L)))))))) * ((long) 16777216L))));
    long _5_x5 = (long) (long) ((_4_x4) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(5L)))))))) * ((long) 65536L))));
    long _6_x6 = (long) (long) ((_5_x5) + ((long) (long) (((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(6L)))))))) * ((long) 256L))));
    long _7_x = (long) (long) ((_6_x6) + ((long) java.lang.Byte.toUnsignedLong(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(7L)))))))));
    return _7_x;
  }
  public static java.math.BigInteger UINT16__LIMIT()
  {
    return (dafny.Helpers.unsignedToBigInteger(BoundedInts_Compile.__default.UINT16__MAX())).add(java.math.BigInteger.ONE);
  }
  public static java.math.BigInteger UINT32__LIMIT()
  {
    return (dafny.Helpers.unsignedToBigInteger(BoundedInts_Compile.__default.UINT32__MAX())).add(java.math.BigInteger.ONE);
  }
  public static java.math.BigInteger UINT64__LIMIT()
  {
    return (dafny.Helpers.unsignedToBigInteger(BoundedInts_Compile.__default.UINT64__MAX())).add(java.math.BigInteger.ONE);
  }
  public static java.math.BigInteger INT32__MAX__LIMIT()
  {
    return java.math.BigInteger.valueOf(BoundedInts_Compile.__default.INT32__MAX());
  }
  public static java.math.BigInteger INT64__MAX__LIMIT()
  {
    return java.math.BigInteger.valueOf(BoundedInts_Compile.__default.INT64__MAX());
  }
  public static java.math.BigInteger UINT64__MAX__LIMIT()
  {
    return dafny.Helpers.unsignedToBigInteger(BoundedInts_Compile.__default.UINT64__MAX());
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.UInt._default";
  }
}
