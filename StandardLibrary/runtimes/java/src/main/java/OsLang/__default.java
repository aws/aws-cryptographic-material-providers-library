package OsLang;

import dafny.DafnySequence;

public class __default extends OsLang._ExternBase___default {

  public static DafnySequence<? extends Character> GetOsShort() {
    String s = System.getProperty("os.name");
    if (s.startsWith("Mac OS")) {
      s = "MacOS";
    }
    return software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
      s
    );
  }

  public static DafnySequence<? extends Character> GetOsLong() {
    return software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
      System.getProperty("os.name") +
      " " +
      System.getProperty("os.arch") +
      " " +
      System.getProperty("os.version")
    );
  }

  public static DafnySequence<? extends Character> GetLanguageShort() {
    return software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
      "Java"
    );
  }

  public static DafnySequence<? extends Character> GetLanguageLong() {
    return software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
      "Java " + System.getProperty("java.version")
    );
  }
}
