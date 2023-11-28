// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../../submodules/MaterialProviders/libraries/src/Wrappers.dfy"
include "../../../../submodules/MaterialProviders/StandardLibrary/src/StandardLibrary.dfy"

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
      Param.Command("Does command stuff", Options("command", [
        Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
        Param.Flag("foo", None, "Does foo things")
      ]))
    ];

    var x :- GetOptions(Options("myProg", MyOptions), args);
    // deal with x.params
    // deal with x.files
    return Success(true);
  }

  datatype Options = Options (
    name : string,
    params : seq<Param>
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
        help: string,
        options: Options
      )

  function GetHelp(opts : Options) : string
  {
    var longLen := GetLongLen(opts.params, 6);
    var commandLen := GetCommandLen(opts.params);
    if commandLen == 0 then
      "USAGE : " + opts.name + " [args...]\n" +
        GetHelp2(opts.params, longLen)
    else
      "USAGE : " + opts.name + " [args...] + command + [args...]\n" +
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
  function GetValue(args : seq<OneArg>, arg : string) : Option<string>
  {
    if |args| == 0 then
      None
    else if args[0].name == arg then
      args[0].value
    else
      GetValue(args[1..], arg)
  }

  // return the number of times this option was specified
  // only useful if the option takes an argument
  function CountArgs(args : seq<OneArg>, arg : string) : nat
  {
    if |args| == 0 then
      0
    else if args[0].name == arg then
      1 + CountArgs(args[1..], arg)
    else
      CountArgs(args[1..], arg)
  }

  // return the number of times this option was specified
  // only useful if the option takes an argument
  function {:tailrecursion} AsMapLast(args : seq<OneArg>, arg : string, theMap : map<string, string> := map[]) : map<string, string>
  {
    if |args| == 0 then
      theMap
    else if args[0].name == arg && args[0].value.Some? then
      AsMapLast(args[1..], arg, theMap[args[0].name := args[0].value.value])
    else
      AsMapLast(args[1..], arg, theMap)
  }

  // return the number of times this option was specified
  // only useful if the option takes an argument
  function {:tailrecursion} AsMapList(args : seq<OneArg>, arg : string, theMap : map<string, seq<string>> := map[]) : map<string, seq<string>>
  {
    if |args| == 0 then
      theMap
    else if args[0].name == arg && args[0].value.Some? then
      if args[0].name in theMap then
        AsMapList(args[1..], arg, theMap[args[0].name := theMap[args[0].name] + [args[0].value.value]])
      else
        AsMapList(args[1..], arg, theMap[args[0].name := [args[0].value.value]])
    else
      AsMapList(args[1..], arg, theMap)
  }

  // return the number of times this option was specified
  // only useful if the option takes an argument
  function {:tailrecursion} AsMapCheck(args : seq<OneArg>, arg : string, theMap : map<string, string> := map[]) : Result<map<string, string>, string>
  {
    if |args| == 0 then
      Success(theMap)
    else if args[0].name == arg && args[0].value.Some? then
      if args[0].name in theMap then
        Failure("Duplicate arg : " + args[0].name)
      else
        AsMapCheck(args[1..], arg, theMap[args[0].name := args[0].value.value])
    else
      AsMapCheck(args[1..], arg, theMap)
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
    name + "  " + opt.help + "\n"
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

  function printFromFunction<T>(x: T): () {
    ()
  } by method {
    print x,"\n";
    return ();
  }

  function GetOptions(opts : Options, args : seq<string>)
    : Result<Parsed, string>
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
      var result :- GetOptions2(args[1..], newContext);
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
      var newParms :- GetShort(args[0][1..], context.longMap, context.shortMap);
      GetOptions2(args[1..], context, parms + newParms, files)
    else
      GetOptions2(args[1..], context, parms, files + [args[0]])
  }

  function GetShort(arg : string, longMap : map<string, bool>, shortMap : map<char, string>, parms : seq<OneArg> := [])
    : Result<seq<OneArg>, string>
    requires forall x <- shortMap :: shortMap[x] in longMap
  {
    if |arg| == 0 then
      Success(parms)
    else
      var ch := arg[0];
      if ch in shortMap then
        var opt := shortMap[ch];
        if longMap[opt] then
          Success(parms + [OneArg(opt, Some(arg[1..]))])
        else
          GetShort(arg[1..], longMap, shortMap, parms + [OneArg(opt, None)])
      else
        Failure("Short option '" + [ch] + "' not recognized.")
  }

  method {:test} TestEmpty() {
    var MyOptions := Options("MyProg",
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
    var MyOptions := Options("MyProg",
    [
      Param.Flag("foo", None, ""),
      Param.Opt("bar", None, "argName", ""),
      Param.Opt("two", Some('t'), "argName", ""),
      Param.Flag("six", Some('s'), ""),
      Param.Flag("seven", Some('v'), "")
    ]);
    var x :- expect GetOptions(MyOptions, ["cmd", "-svsttt"]);
    expect x.params == [OneArg("six", None), OneArg("seven", None), OneArg("six", None), OneArg("two", Some("tt"))];
    expect x.files == [];
  }

  method {:test} TestLong() {
    var MyOptions := Options("MyProg",
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
    var MyOptions := Options("MyProg",
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
    var MyOptions := Options("MyProg",
    [
      Param.Flag("foo", None, "Does foo things"),
      Param.Opt("two", Some('t'), "thingy", "Does bar things to thingy"),
      Param.Command("Does command stuff", Options("command", [
        Param.Opt("five", Some('h'), "thingy", "Does five things to thingy"),
        Param.Flag("six", None, "Does six things")
      ])),
      Param.Command("Does other stuff", Options("other", [
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
}