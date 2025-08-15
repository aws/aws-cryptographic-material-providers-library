include "../../libraries/src/MutableMap/MutableMap.dfy"
include "../../StandardLibrary/src/Index.dfy"

module TestMutableMap {
  import opened DafnyLibraries
  import opened StandardLibrary.UInt

  method {:test} TestPerformanceBaseline()
  {
    var testMap := new MutableMap();
    var iterations := 100;
    
    var i := 0;
    while i < iterations {
      testMap.Put(i, i);
      i := i + 1;
    }
    
    expect testMap.Size() == iterations;
    
    i := 0;
    while i < iterations {
      expect testMap.HasKey(i);
      i := i + 1;
    }
    
    i := 0;
    while i < iterations {
      expect testMap.HasKey(i);
      expect testMap.Select(i) == i;
      i := i + 1;
    }
    
    i := 0;
    while i < iterations {
      testMap.Remove(i);
      i := i + 1;
    }
    
    expect testMap.Size() == 0;
  }

  method {:test} TestPerformanceScaling()
  {
    TestMapOperations(10);
    TestMapOperations(100);
    TestMapOperations(1000);
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
