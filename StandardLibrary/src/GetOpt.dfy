// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

/*
Types :
    Options = (name : string, help : string, params : seq<Params>)
    datatype Param =
      Opt(name: string, short: Option<char>, argName: string, help: string) // takes an argument
      Flag(name: string, short: Option<char>, help: string) // does not take an argument
      Command(options: Options) // sub command
    Parsed = (command : string, params : seq<OneArg>, files : seq<string>, subcommand : Option<Parsed>)
    OneArg (name : string, value : Option<string>) // for Opt value.Some? for Flag value.None?


Main Entry Points :
  GetOptions(opts : Options, args : seq<string>) // Parse args based on Options, automatically includes --help
  GetHelp(opts : Options) : string // return help text for Options

Helpers for `Opt` args :
  OptValue(args : seq<OneArg>, arg : string) : Option<string> // return value for arg, if used
  OptMapLast(args : seq<OneArg>) : map<string, string> // return args as map, return last value used if multiple
  OptMapList(args : seq<OneArg>) : map<string, seq<string>> // return all values for each arg used
  OptMapCheck(args : seq<OneArg>) : Result<map<string, string>, string> // as OptMapLast, but return error if any are used more than once

Helpers for `Flag` args :
  FlagCount(args : seq<OneArg>, arg : string) : nat // how many times was arg used
  FlagsSet(args : seq<OneArg>) : set<string> // set of all Flags used at least once
  FlagMapCount(args : seq<OneArg>) : map<string, nat> // // for each Flag used, how many times was it used
  FlagSetCheck(args : seq<OneArg>) : Result<set<string>, string> // as FlagSet, but return error if any are used more than once

Helper for argument values :
  None yet, but should parse numbers, enums, timestamps, dates, boolean, tristate, duration, and lists of all of these

Command Line Interpretations :
  We attempt to mostly match the GNU/POSIX standard, such as it is

  If "cmd" has
    Opt("Apple", Some('a'))
    Opt("Banana", Some('b'))
    Flag("Cherry", Some('c'))
    Flag("Date", Some('d'))
  then these are all equivalent
    cmd --cherry --apple red --banana yellow --date
    cmd --cherry --apple=red --banana=yellow --date
    cmd -c -a red -b yellow -d
    cmd -ca red -byellow -d
    cmd -cared -byellow -d
  and these are all equivalent
    cmd --cherry --apple red --banana yellow --date file1 file2 file3 file4 file5
    cmd file1 --cherry file2 --apple red file3 --banana yellow file4 --date file5
    cmd file1 -c file2 -a red file3 -b yellow file4 -d file5
  
  Everything after "--" is a file name, so
    cmd --cherry --date
  has two parameters and no files, while
    cmd --cherry -- --date
  has one parameter and one file (file name is "--date")

  If cmd has a subcommand, then it can take no file parameters
  e.g. if cmd has a subcommand sub then
    cmd --cherry sub --whatever file1
  is fine, but
    cmd --cherry file1 sub --whatever 
  returns the error "subcommand 'file1' not recognized"
*/

include "../../libraries/src/Wrappers.dfy"
include "StandardLibrary.dfy"

module {:options "-functionSyntax:4"} GetOpt {
  import opened Wrappers
  import opened StandardLibrary

  // --key value file --key=value file -abckValue [--] file file file
  method Example(args : seq<string>) returns (output : Result<bool, string>)
    requires 0 < |args|
  {
    var MyOptions := [
      Param.Flag("foo", None, "Does foo things"),
      Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
      Param.Command(Options("command", "Does command stuff", [
        Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
        Param.Flag("foo", None, "Does foo things")
      ]))
    ];

    var x :- GetOptions(Options("myProg", "does prog stuff", MyOptions), args);
    // deal with x.params
    // deal with x.files
    // deal with x.subcommand
    return Success(true);
  }

  datatype Options = Options (
    name : string,
    help : string,
    params : seq<Param>
    // Maybe some optional stuff here, e.g.
    //   X is required
    //   exactly one of X, Y, Z is required
  )

  datatype Param =
    | Opt(
        name: string,
        short: Option<char> := None,
        argName: string,
        help: string
      )
    | Flag(
        name: string,
        short: Option<char> := None,
        help: string
      )
    | Command(
        options : Options
      )

  function GetHelp(opts : Options) : string
  {
    var longLen := GetLongLen(opts.params, 6);
    var commandLen := GetCommandLen(opts.params);
    if commandLen == 0 then
      "USAGE : " + opts.name + " [args...]\n" +
      opts.help + "\n" +
        GetHelp2(opts.params, longLen)
    else
      "USAGE : " + opts.name + " [args...] + command + [args...]\n" +
      opts.help + "\n" +
      "\nAvailable Commands:\n" +
        GetCmdHelp(opts.params, commandLen) +
      "\nAvailable Options:\n" +
        GetHelp2(opts.params, longLen)
  }

  datatype OneArg = OneArg (
    name : string,
    value : Option<string>
  )

  datatype Parsed = Parsed (
    command : string,
    params : seq<OneArg>,
    files : seq<string>,
    subcommand : Option<Parsed>
  )

  // get value of first occurrence of option with required argument.
  // Cannot distinguish "no value" from "argument not used"
  function OptValue(args : seq<OneArg>, arg : string) : Option<string>
  {
    if |args| == 0 then
      None
    else if args[0].name == arg then
      args[0].value
    else
      OptValue(args[1..], arg)
  }

  // return the number of times this option was specified
  // only useful if the option takes an argument
  function {:tailrecursion} FlagCount(args : seq<OneArg>, arg : string) : nat
  {
    if |args| == 0 then
      0
    else if args[0].name == arg then
      1 + FlagCount(args[1..], arg)
    else
      FlagCount(args[1..], arg)
  }

  function {:tailrecursion} OptMapLast(args : seq<OneArg>, theMap : map<string, string> := map[]) : map<string, string>
  {
    if |args| == 0 then
      theMap
    else if args[0].value.Some? then
      OptMapLast(args[1..], theMap[args[0].name := args[0].value.value])
    else
      OptMapLast(args[1..], theMap)
  }

  function {:tailrecursion} FlagsSet(args : seq<OneArg>, theSet : set<string> := {}) : set<string>
  {
    if |args| == 0 then
      theSet
    else if args[0].value.Some? then
      FlagsSet(args[1..], theSet)
    else
      FlagsSet(args[1..], theSet + {args[0].name})
  }

  function {:tailrecursion} OptMapList(args : seq<OneArg>, theMap : map<string, seq<string>> := map[]) : (ret : map<string, seq<string>>)
    requires forall k <- theMap :: 0 < |theMap[k]|
    ensures forall k <- ret :: 0 < |ret[k]|
  {
    if |args| == 0 then
      theMap
    else if args[0].value.Some? then
      if args[0].name in theMap then
        OptMapList(args[1..], theMap[args[0].name := theMap[args[0].name] + [args[0].value.value]])
      else
        OptMapList(args[1..], theMap[args[0].name := [args[0].value.value]])
    else
      OptMapList(args[1..], theMap)
  }

  function {:tailrecursion} FlagMapCount(args : seq<OneArg>, theMap : map<string, nat> := map[]) : (ret : map<string, nat>)
    requires forall k <- theMap :: 0 < theMap[k]
    ensures forall k <- ret :: 0 < ret[k]
  {
    if |args| == 0 then
      theMap
    else if args[0].value.Some? then
      FlagMapCount(args[1..], theMap)
    else
      if args[0].name in theMap then
        FlagMapCount(args[1..], theMap[args[0].name := theMap[args[0].name] + 1])
      else
        FlagMapCount(args[1..], theMap[args[0].name := 1])
  }


  function {:tailrecursion} FlagSetCheck(args : seq<OneArg>, theSet : set<string> := {}) : Result<set<string>, string>
  {
    if |args| == 0 then
      Success(theSet)
    else if args[0].value.Some? then
      if args[0].name in theSet then
        Failure("Duplicate arg : " + args[0].name)
      else
        FlagSetCheck(args[1..], theSet + {args[0].name})
    else
      FlagSetCheck(args[1..], theSet)
  }

  function {:tailrecursion} OptMapCheck(args : seq<OneArg>, theMap : map<string, string> := map[]) : Result<map<string, string>, string>
  {
    if |args| == 0 then
      Success(theMap)
    else if args[0].value.Some? then
      if args[0].name in theMap then
        Failure("Duplicate arg : " + args[0].name)
      else
        OptMapCheck(args[1..], theMap[args[0].name := args[0].value.value])
    else
      OptMapCheck(args[1..], theMap)
  }


  type CommandMap = x : map<string, Options> | forall k <- x :: x[k].name == k

  function OneHelp(opt : Param, longLen : nat) : string
  {
    if opt.Command? then
      ""
    else
      GetShortHelp(opt) + "  " + GetLongHelp(opt, longLen) + "  " + opt.help + "\n"
  }

  function GetCommandHelp(opt : Param, commandLen : nat) : string
    requires opt.Command?
  {
    var name :=
      if |opt.options.name| < commandLen then
        opt.options.name + seq(commandLen - |opt.options.name|, i => ' ')
      else
        opt.options.name;
    name + "  " + opt.options.help + "\n"
  }

  function GetShortHelp(opt : Param) : (output : string)
  {
    if opt.Opt? || opt.Flag? then
      if opt.short.Some? then
        "-" + [opt.short.value]
      else
        "  "
    else
      ""
  }

  function GetLongHelp(opt : Param, longLen : nat) : string
  {
    if opt.Opt? || opt.Flag? then
      var tmp :=
        "--" + opt.name +
        if opt.Opt? then
          "=" + opt.argName
        else
          "";
      if |tmp| < longLen then
        tmp + seq(longLen - |tmp|, i => ' ')
      else
        tmp
    else
      ""
  }

  function GetHelp2(opts : seq<Param>, longLen : nat) : string
  {
    if |opts| == 0 then
      OneHelp(Flag("help", None, "This help text."), longLen)
    else
      var x := OneHelp(opts[0], longLen);
      x + GetHelp2(opts[1..], longLen)
  }

  function GetCmdHelp(opts : seq<Param>, commandLen : nat) : string
  {
    if |opts| == 0 then
      ""
    else
      var x :=
        if opts[0].Command? then
          GetCommandHelp(opts[0], commandLen)
        else
          "";
      x + GetCmdHelp(opts[1..], commandLen)
  }

  function GetLongLen(opts : seq<Param>, max : nat := 0) : nat
  {
    if |opts| == 0 then
      max
    else
      var x := |GetLongHelp(opts[0], 0)|;
      var newMax := if x > max then x else max;
      GetLongLen(opts[1..], newMax)
  }

  function GetCommandLen(opts : seq<Param>, max : nat := 0) : nat
  {
    if |opts| == 0 then
      max
    else
      var x := if opts[0].Command? then |opts[0].options.name| else 0;
      var newMax := if x > max then x else max;
      GetCommandLen(opts[1..], newMax)
  }

  // convert opts to the various maps that make parsing possible 
  function {:tailrecursion} GetMaps(
    opts : seq<Param>,
    longMap : map<string, bool> := map[],
    shortMap : map<char, string> := map[],
    commandMap : CommandMap := map[])
    : (ret : Result<(map<string, bool>, map<char, string>, CommandMap), string>)
    requires forall x <- shortMap :: shortMap[x] in longMap
    ensures ret.Success? ==> (forall x <- ret.value.1 :: ret.value.1[x] in ret.value.0)
  {
    if |opts| == 0 then
      Success((longMap, shortMap, commandMap))
    else
      var opt := opts[0];
      if opt.Command? then
        :- Need(opt.options.name !in commandMap, "Duplicate command in options : " + opt.options.name);
        GetMaps(opts[1..], longMap, shortMap, commandMap[opt.options.name := opt.options])
      else
        :- Need(opt.name !in longMap, "Duplicate long name in options : " + opt.name);
        var longMap := longMap[opt.name := opt.Opt?];
        if opt.short.Some? then
          var short := opt.short.value;
          if short in shortMap then // can't be a `Need` because shortMap[short] required in message
            Failure("Duplicate short char in options : '" + [short] + "' for " + opt.name + " and " + shortMap[short])
          else
            GetMaps(opts[1..], longMap[opt.name := opt.Opt?], shortMap[short := opt.name], commandMap)
        else
          GetMaps(opts[1..], longMap[opt.name := opt.Opt?], shortMap, commandMap)
  }

 function Print<T>(x: T): Outcome<string> {
    Pass
  } by method {
    print x,"\n";
    return Pass;
  }

  function GetOptions(opts : Options, args : seq<string>) : Result<Parsed, string>
    requires 0 < |args|
    decreases args
  {
    var (longMap, shortMap, commandMap) :- GetMaps(opts.params, map["help" := false]);
    var context := Context(longMap, shortMap, commandMap, args[0]);
    GetOptions2(args[1..], context)
  }

  datatype Context = Context (
    longMap : map<string, bool>,
    shortMap : map<char, string>,
    commands : CommandMap,
    command : string
  )

  function /*{:tailrecursion}*/ GetOptions2(
    args : seq<string>,
    context : Context,
    parms : seq<OneArg> := [],
    files : seq<string> := [])
    : Result<Parsed, string>
    requires forall x <- context.shortMap :: context.shortMap[x] in context.longMap
    decreases args
  {
    if |args| == 0 then
      Success(Parsed(context.command, parms, files, None))
    else if args[0] in context.commands then
      var (longMap, shortMap, commandSet) :- GetMaps(context.commands[args[0]].params, map["help" := false]);
      var newContext := Context(longMap, shortMap, commandSet, args[0]);
      var result :- GetOptions2(args[1..], newContext); // this is why it can't be tail recursive
      Success(Parsed(context.command, parms, files, Some(result)))
    else if args[0] == "--" then
      Success(Parsed(context.command, parms, files + args[1..], None))
    else if "--" < args[0] then
      var longOpt := args[0][2..];
      if '=' in longOpt then
        var (opt,arg) := SplitOnce(longOpt, '=');
        if opt in context.longMap then
          if context.longMap[opt] then
            GetOptions2(args[1..], context, parms + [OneArg(opt, Some(arg))], files)
          else
            Failure("Option " + opt + " does not take an argument, but it got one.")
        else
          Failure("Option " + opt + " not recognized.")
      else
      if longOpt in context.longMap then
        if context.longMap[longOpt] then
          if |args| < 2 then
            Failure("Option " + longOpt + " requires an argument, but didn't get one.")
          else
            GetOptions2(args[2..], context, parms + [OneArg(longOpt, Some(args[1]))], files)
        else
          GetOptions2(args[1..], context, parms + [OneArg(longOpt, None)], files)
      else
        Failure("Option " + longOpt + " not recognized.")
    else if "-" == args[0] then
      GetOptions2(args[1..], context, parms, files + [args[0]])
    else if "-" < args[0] then
      var (newParms, nextParm) :- GetShort(args[0][1..], context.longMap, context.shortMap);
      if nextParm.None? then
        GetOptions2(args[1..], context, parms + newParms, files)
      else if |args| == 1 then
        Failure("Short option " + [nextParm.value] + " requires argument but didn't get one.")
      else
        GetOptions2(args[2..], context, parms + newParms + [OneArg(context.shortMap[nextParm.value], Some(args[1]))], files)
    else if |context.commands| == 0 then
      GetOptions2(args[1..], context, parms, files + [args[0]])
    else
      Failure("Unrecognized command " + args[0] + " for " + context.command + "\nRun '" + context.command + " --help' for usage.")
  }

  function GetShort(arg : string, longMap : map<string, bool>, shortMap : map<char, string>, parms : seq<OneArg> := [])
    : (res : Result<(seq<OneArg>, Option<char>), string>)
    requires forall x <- shortMap :: shortMap[x] in longMap
    ensures res.Success? && res.value.1.Some? ==> res.value.1.value in shortMap
  {
    if |arg| == 0 then
      Success((parms, None))
    else
      var ch := arg[0];
      if ch in shortMap then
        var opt := shortMap[ch];
        if longMap[opt] then
          if |arg| == 1 then
            Success((parms, Some(ch)))
          else
            Success((parms + [OneArg(opt, Some(arg[1..]))], None))
        else
          GetShort(arg[1..], longMap, shortMap, parms + [OneArg(opt, None)])
      else
        Failure("Short option '" + [ch] + "' not recognized.")
  }

  method {:test} TestEmpty() {
    var MyOptions := Options("MyProg", "does stuff",
    [
      Param.Flag("foo", None, ""),
      Param.Opt("bar", None, "argName", ""),
      Param.Opt("two", Some('t'), "argName", ""),
      Param.Flag("six", Some('s'), "")
    ]);
    var x :- expect GetOptions(MyOptions, ["cmd"]);
    expect x.params == [];
    expect x.files == [];
  }
  method {:test} TestShort() {
    var MyOptions := Options("MyProg", "does stuff",
    [
      Param.Flag("foo", None, ""),
      Param.Opt("bar", None, "argName", ""),
      Param.Opt("two", Some('t'), "argName", ""),
      Param.Flag("six", Some('s'), ""),
      Param.Flag("seven", Some('v'), "")
    ]);
    var x :- expect GetOptions(MyOptions, ["cmd", "-svsttt", "-t", "stuff", "-v"]);
    expect x.params == [OneArg("six", None), OneArg("seven", None), OneArg("six", None), OneArg("two", Some("tt")),
    OneArg("two", Some("stuff")), OneArg("seven", None)];
    expect x.files == [];
  }

  method {:test} TestLong() {
    var MyOptions := Options("MyProg", "does stuff",
    [
      Param.Flag("foo", None, ""),
      Param.Opt("bar", None, "argName", ""),
      Param.Opt("two", Some('t'), "argName", ""),
      Param.Flag("six", Some('s'), ""),
      Param.Flag("seven", Some('v'), "")
    ]);
    var x :- expect GetOptions(MyOptions, ["cmd", "--foo", "file1", "--bar", "bar1", "-", "--bar=bar2=bar3", "file3", "--", "--this", "-that"]);
    expect x.params == [OneArg("foo", None), OneArg("bar", Some("bar1")), OneArg("bar", Some("bar2=bar3"))];
    expect x.files == ["file1", "-", "file3", "--this", "-that"];
  }

  method {:test} TestHelp() {
    var MyOptions := Options("MyProg", "does stuff",
    [
      Param.Flag("foo", None, ""),
      Param.Opt("bar", None, "argName", ""),
      Param.Opt("two", Some('t'), "argName", ""),
      Param.Flag("six", Some('s'), ""),
      Param.Flag("seven", Some('v'), "")
    ]);
    print "\n", GetHelp(MyOptions);
  }

  method {:test} TestNested() {
    var MyOptions := Options("MyProg", "does stuff",
    [
      Param.Flag("foo", None, "Does foo things"),
      Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
      Param.Command(Options("command", "Does command stuff", [
        Param.Opt("five", Some('h'), "thingy", "Does five things to thingy"),
        Param.Flag("six", None, "Does six things")
      ])),
      Param.Command(Options("other", "Does other stuff", [
        Param.Opt("seven", Some('h'), "thingy", "Does seven things to thingy"),
        Param.Flag("eight", None, "Does eight things")
      ]))
    ]);
    var x :- expect GetOptions(MyOptions, ["cmd", "--foo", "other", "--seven=siete", "--eight"]);
    expect x.command == "cmd";
    expect x.params == [OneArg("foo", None)];
    expect x.files == [];
    expect x.subcommand.Some?;
    var sub := x.subcommand.value;
    expect sub.command == "other";
    expect sub.params == [OneArg("seven", Some("siete")), OneArg("eight", None)];
    expect sub.files == [];
    expect sub.subcommand.None?;
    print "\n", GetHelp(MyOptions);
  }

    method {:test} TestDdbec() {
    var MyOptions := Options("ddbec", "Test the ddbec",
    [
      // Param.Flag("foo", None, "Does foo things"),
      // Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
      Param.Command(Options("encrypt", "Encrypts record", [
        Param.Opt("output", Some('o'), "fileName", "Write encrypted records to fileName.")
      ])),
      Param.Command(Options("decrypt", "Decrypts Records", [
        Param.Opt("expected", Some('e'), "fileName", "fileName contains expected plaintext records")
      ]))
    ]);
  }

}
