include "../../libraries/src/MutableMap/MutableMap.dfy"
include "../../StandardLibrary/src/Index.dfy"

module TestMutableMap {
  import opened DafnyLibraries
  import opened StandardLibrary.UInt
  import Time

  method {:test} TestPerformanceScaling()
  {
    var sizes := [1, 10, 10000, 100000, 1000000, 1000000000, 100000000000000000];
    var i := 0;
    while i < |sizes| {
        TestForEachSize(sizes[i]);
        i := i + 1;
    }
  }

  method TestForEachSize(size: int)
    requires size > 0
  {
    var time1 := Time.GetAbsoluteTime();
    TestMapOperations(size);
    print "Time taken for " , size , " items \n";
    Time.PrintTimeSince(time1);
  }

  method TestMapOperations(size: int)
  requires size > 0
{
  // Explicitly parametrize with <seq<uint8>, int>
  var testMap := new MutableMap((k: seq<uint8>, v: int) => true, true);
  var i := 0;
  while i < size {
    // Convert int -> seq<uint8> (just an example: single-byte sequence)
    var key := IntToBytes(i); 
    testMap.Put(key, i);
    i := i + 1;
  }
  expect testMap.Size() == size;
  // Reset loop
  i := 0;
  while i < size {
    var key := IntToBytes(i);
    var tempI := testMap.Select(key);
    expect i == tempI;
    i := i + 1;
  }
  i := 0;
  while i < size {
    var key := IntToBytes(i);
    testMap.Remove(key);
    expect !testMap.HasKey(key);
    i := i + 1;
  }
}
method IntToBytes(x: int) returns (bytes: seq<uint8>)
  requires x >= 0
  ensures |bytes| > 0
{
  var result := [];
  var n := x;
  while n > 0
    decreases n
  {
    result := [(n % 256) as uint8] + result;
    n := n / 256;
  }
  if |result| == 0 {
    result := [(0) as uint8];
  }
  bytes := result;
}
}
