// Class _ExternBase___default
// Dafny class __default compiled into Java
package OsLang;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static dafny.DafnySequence<? extends Character> GetPlatformShort() {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(__default.GetLanguageShort(), dafny.DafnySequence.asString(" ")), __default.GetOsShort());
  }
  public static dafny.DafnySequence<? extends Character> GetPlatformLong() {
    return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(__default.GetLanguageLong(), dafny.DafnySequence.asString(" ")), __default.GetOsLong());
  }
  @Override
  public java.lang.String toString() {
    return "OsLang._default";
  }
}
