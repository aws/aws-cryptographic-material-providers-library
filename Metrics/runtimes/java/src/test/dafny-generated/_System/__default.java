// Class __default
// Dafny class __default compiled into Java
package _System;

import TestMetricsAgentText_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static void __Test____Main__(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> __noArgsParameter)
  {
    boolean _0_success;
    _0_success = true;
    System.out.print((dafny.DafnySequence.asString("TestMetricsAgentText.TestCreateTextMetricsAgent: ")).verbatimString());
    try {
      {
        TestMetricsAgentText_Compile.__default.TestCreateTextMetricsAgent();
        {
          System.out.print((dafny.DafnySequence.asString("PASSED\n")).verbatimString());
        }
      }
    }
    catch (dafny.DafnyHaltException e) {
      dafny.DafnySequence<Character> _1_haltMessage = dafny.DafnySequence.asString(e.getMessage());
      {
        System.out.print((dafny.DafnySequence.asString("FAILED\n	")).verbatimString());
        System.out.print((_1_haltMessage).verbatimString());
        System.out.print((dafny.DafnySequence.asString("\n")).verbatimString());
        _0_success = false;
      }
    }
    if (!(_0_success)) {
      throw new dafny.DafnyHaltException("<stdin>(1,0): " + (dafny.DafnySequence.asString("Test failures occurred: see above.\n")).verbatimString());
    }
  }
  public static void __Main(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> args) {
    __default.__Test____Main__(args);
  }
  @Override
  public java.lang.String toString() {
    return "_module._default";
  }
}
