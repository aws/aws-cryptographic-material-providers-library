// Class __default
// Dafny class __default compiled into Java
package EncryptionContextUtils_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> normal()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 110, (byte) 111, (byte) 114, (byte) 109, (byte) 97, (byte) 108, (byte) 237, (byte) 128, (byte) 128);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> psi()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 144, (byte) 128, (byte) 130);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextWithPsiMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.normal(), __default.normal()), new dafny.Tuple2(__default.psi(), __default.psi()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextWitPsi()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextWithPsiMap());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> replacementChar()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 239, (byte) 191, (byte) 189);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextWithReplacementMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.normal(), __default.normal()), new dafny.Tuple2(__default.replacementChar(), __default.replacementChar()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextWitReplacementChar()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextWithReplacementMap());
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextControlMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.normal(), __default.normal()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextControl()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextControlMap());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> a()
  {
    return (UTF8.__default.Encode(dafny.DafnySequence.asString("a"))).dtor_value();
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextBasicMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.a(), __default.a()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextBasic()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextBasicMap());
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextEmptyMap()
  {
    return dafny.DafnyMap.fromElements();
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextEmpty()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextEmptyMap());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ascii1()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 49);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ascii2()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 194, (byte) 160);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ascii3()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 85);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextAsciiMapMultipleKeyValues()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.ascii1(), __default.ascii1()), new dafny.Tuple2(__default.ascii2(), __default.ascii2()), new dafny.Tuple2(__default.ascii3(), __default.ascii3()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ascii4()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 194, (byte) 182);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextAsciiMapSingleKeyValue()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.ascii4(), __default.ascii4()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextAscii()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextAsciiMapSingleKeyValue());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__2__1()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 196, (byte) 128);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__2__2()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 212, (byte) 152);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__2__3()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 212, (byte) 136);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF82MapMultipleKeyValues()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__2__1(), __default.utf8__2__1()), new dafny.Tuple2(__default.utf8__2__2(), __default.utf8__2__2()), new dafny.Tuple2(__default.utf8__2__3(), __default.utf8__2__3()));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF82MapSingleKeyValue()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__2__3(), __default.utf8__2__3()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextUTF82()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextUTF82MapSingleKeyValue());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__3__1()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 224, (byte) 160, (byte) 128);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__3__2()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 224, (byte) 183, (byte) 180);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__3__3()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 226, (byte) 136, (byte) 176);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF83MapMultipleKeyValues()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__3__1(), __default.utf8__3__1()), new dafny.Tuple2(__default.utf8__3__2(), __default.utf8__3__2()), new dafny.Tuple2(__default.utf8__3__3(), __default.utf8__3__3()));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF83MapSingleKeyValue()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__3__3(), __default.utf8__3__3()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextUTF83()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextUTF83MapSingleKeyValue());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__4__1()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 146, (byte) 128, (byte) 128);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__4__2()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 147, (byte) 128, (byte) 163);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__4__3()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 147, (byte) 137, (byte) 169);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF84MapMultipleKeyValues()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__4__1(), __default.utf8__4__1()), new dafny.Tuple2(__default.utf8__4__2(), __default.utf8__4__2()), new dafny.Tuple2(__default.utf8__4__3(), __default.utf8__4__3()));
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> encryptionContextUTF84MapSingleKeyValue()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.utf8__4__1(), __default.utf8__4__1()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextUTF84()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextUTF84MapSingleKeyValue());
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> variedUTF8EncryptionContext()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> empty(), __default.encryptionContextAscii()), __default.encryptionContextUTF82()), __default.encryptionContextUTF83()), __default.encryptionContextUTF84()), __default.encryptionContextWitReplacementChar());
  }
  public static dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> representativeEncryptionContextUtf8Values()
  {
    return dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>> of(__default.ascii4(), __default.utf8__2__3(), __default.utf8__3__3(), __default.utf8__4__3());
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> multipleEntriesUTF8EncryptionContext()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.encryptionContextAsciiMapMultipleKeyValues(), __default.encryptionContextUTF82MapMultipleKeyValues(), __default.encryptionContextUTF83MapMultipleKeyValues(), __default.encryptionContextUTF84MapMultipleKeyValues());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ascii5()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 195, (byte) 191);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__2__4()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 223, (byte) 159);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__2__5()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 223, (byte) 159);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__3__4()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 239, (byte) 163, (byte) 191);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__3__5()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 239, (byte) 191, (byte) 191);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__4__4()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 157, (byte) 132, (byte) 162);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> utf8__4__5()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 159, (byte) 167, (byte) 191);
  }
  @Override
  public java.lang.String toString() {
    return "EncryptionContextUtils._default";
  }
}
