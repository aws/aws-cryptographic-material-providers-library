// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../TestUtils.dfy"

module  {:options "/functionSyntax:4"} TestStormTracker {
  import opened AwsCryptographyMaterialProvidersTypes
  import opened UInt = StandardLibrary.UInt
  import opened Wrappers
  import opened StormTracker
  import opened AwsCryptographyKeyStoreTypes
  import UTF8

  function MakeMat(data : Utf8Bytes) : Materials
  {
    BranchKey(BranchKey := BranchKeyMaterials (
                branchKeyIdentifier := "spoo",
                branchKeyVersion := data,
                branchKey := data,
                encryptionContext := map[],
                kmsArn := "KeyId",
                createTime := "CreateTime",
                hierarchyVersion := HierarchyVersion.v1
              ))
  }

  function MakeGet(data : Utf8Bytes) : GetCacheEntryInput
  {
    GetCacheEntryInput (
      identifier := data,
      bytesUsed := Option.None
    )
  }
  function MakeDel(data : Utf8Bytes) : DeleteCacheEntryInput
  {
    DeleteCacheEntryInput (
      identifier := data
    )
  }
  function MakePut(data : Utf8Bytes, expiryTime : PositiveLong) : PutCacheEntryInput
  {
    PutCacheEntryInput (
      identifier := data,
      materials := MakeMat(data),
      creationTime := 123456789,
      // The expiryTime is in seconds
      expiryTime := expiryTime / 1000,
      messagesUsed := Option.None,
      bytesUsed := Option.None
    )
  }
  function MakeGetOutput(data : Utf8Bytes, expiryTime : PositiveLong): GetCacheEntryOutput
  {
    GetCacheEntryOutput(
      materials := MakeMat(data),
      creationTime := 123456789,
      // The expiryTime is in seconds
      expiryTime := expiryTime / 1000,
      messagesUsed := 1,
      bytesUsed := 0
    )
  }

  const abc : UTF8.ValidUTF8Bytes :=
    var s := [0x61, 0x62, 0x63];
    assert s == UTF8.EncodeAscii("abc");
    s

  const cde : UTF8.ValidUTF8Bytes :=
    var s := [0x63, 0x64, 0x65];
    assert s == UTF8.EncodeAscii("cde");
    s

  const one : UTF8.ValidUTF8Bytes :=
    var s := [0x6f, 0x6e, 0x65];
    assert s == UTF8.EncodeAscii("one");
    s

  const two : UTF8.ValidUTF8Bytes :=
    var s := [0x74, 0x77, 0x6f];
    assert s == UTF8.EncodeAscii("two");
    s

  const three : UTF8.ValidUTF8Bytes :=
    var s := [0x74, 0x68, 0x72, 0x65, 0x65];
    assert s == UTF8.EncodeAscii("three");
    s

  const four : UTF8.ValidUTF8Bytes :=
    var s := [0x66, 0x6f, 0x75, 0x72];
    assert s == UTF8.EncodeAscii("four");
    s


  method {:test} StormTrackerBasics() {
    var st := new StormTracker(DefaultStorm());

    var res :- expect st.GetFromCacheWithTime(MakeGet(abc), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(abc), 10000);
    expect res.EmptyWait?;
    var res2 :- expect st.PutCacheEntry(MakePut(abc, 10000));
    res2 :- expect st.PutCacheEntry(MakePut(cde, 10000));
    // The Storm tracker now deals in milliseconds,
    // so 11000 is 1 second later
    // The expiry time is in seconds, is in seconds.
    // The cache is willing to return a record
    // anytime within the expiry second.
    res :- expect st.GetFromCacheWithTime(MakeGet(abc), 11000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(abc), 11000);
    expect res.EmptyWait?;

    // the following are to test the Dafny header, to see that it allows for multiple calls
    var res3 := st.GetCacheEntry(MakeGet(abc));
    res3 := st.GetCacheEntry(MakeGet(abc));
    var res4 := st.GetFromCache(MakeGet(abc));
    res4 := st.GetFromCache(MakeGet(abc));
    var res5 := st.DeleteCacheEntry(MakeDel(abc));
    res5 := st.DeleteCacheEntry(MakeDel(abc));
  }

  method {:test} StormTrackerFanOut()
  {
    var st := new StormTracker(DefaultStorm().(fanOut := 3));
    var res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(two), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(three), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(four), 10000);
    expect res.EmptyWait?;
  }

  method {:test} StormTrackerPruneTTL()
  {
    var st := new StormTracker(DefaultStorm().(graceInterval := 3, fanOut := 3, inFlightTTL := 5));
    var res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(two), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(three), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(four), 10000);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(four), 10001);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(four), 10003);
    expect res.EmptyWait?;
    // Because the fanOut has been reached,
    // and nothing has been put into the cache
    // we need to let prune happen
    res :- expect st.GetFromCacheWithTime(MakeGet(four), 11000);
    expect res.EmptyFetch?;
  }

  method {:test} StormTrackerGraceInterval()
  {
    var st := new StormTracker(DefaultStorm().(graceInterval := 3));
    var res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10001);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10002);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10003);
    expect res.EmptyFetch?;
  }

  method {:test} FullStormTrackerGraceInterval()
  {
    // The cache is full, we wait for the graceInterval
    // regardless of the inFlightTTL

    var st := new StormTracker(DefaultStorm().(graceInterval := 2, inFlightTTL := 3, gracePeriod := 5));
    // This entry will be in the cache until ms:   11000
    var _ :- expect st.PutCacheEntry(MakePut(one, 10000));

    var res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 5);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 5);
    expect res.Full?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 4);
    expect res.Full?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 3);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 2);
    expect res.Full?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 1);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 1);
    expect res.Full?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 - 0);
    // This is because it went inflight
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 11000 + 1);
    // Now, graceInterval is smaller, so it calls for fetch
    expect res.EmptyFetch?;
  }

  method {:test} StormTrackerGracePeriod()
  {
    var config := DefaultStorm();
    var expiryTime := 100100;
    // expiryTime stored in the LocalCMC is in seconds
    // This means that if you only subtract 1,
    // you will not be before the grace period.
    // You need to subtract a seconds worth of milliseconds.
    var beforeGracePeriod := expiryTime - config.gracePeriod as Types.PositiveLong - 1000;
    var insideGracePeriod := expiryTime - config.gracePeriod as Types.PositiveLong + 1;
    var st := new StormTracker(config);

    var res2 :- expect st.PutCacheEntry(MakePut(one, expiryTime));

    var res :- expect st.GetFromCacheWithTime(MakeGet(one), beforeGracePeriod);
    expect res.Full?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), insideGracePeriod);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), insideGracePeriod);
    expect res.Full?;
  }

  method {:test} EmptyStormTrackerTLLAndInterval()
  {
    // The cache is empty, we wait for the least
    // duration between graceInterval and inFlightTTL
    // for empty identifiers

    var st := new StormTracker(DefaultStorm().(graceInterval := 2, inFlightTTL := 3));

    var res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10000);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10001);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10002);
    expect res.EmptyFetch?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10002);
    expect res.EmptyWait?;
    res :- expect st.GetFromCacheWithTime(MakeGet(one), 10003);
    expect res.EmptyWait?;
  }

}
