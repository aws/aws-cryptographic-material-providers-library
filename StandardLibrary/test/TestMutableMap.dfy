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
    var testMap := new MutableMap();
    
    var i := 0;
    while i < size {
      testMap.Put(i, i);
      i := i + 1;
    }
    
    expect testMap.Size() == size;
    
    var tempI;
    while i < size {
      tempI := testMap.Select(i);
      expect i == tempI;
      i := i + 1;
    }

    while i < size {
      testMap.Remove(i);
      expect !testMap.HasKey(i);
    }
  }
}
