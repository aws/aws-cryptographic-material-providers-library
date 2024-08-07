// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/Time.dfy"

module {:options "/functionSyntax:4" } TestTime {
  import Time

  method {:test} TestNonDecreasing() {
    var t1 := Time.GetCurrent();
    var t2 := Time.GetCurrent();
    expect t2 >= t1;
  }

  method {:test} TestPositiveValues() {
    var t1 := Time.GetCurrent();
    var t2 := Time.GetCurrent();
    expect t2 - t1 >= 0;
  }

  method {:test} TestGetCurrentTimeStamp()
  {
    var CurrentTime :- expect Time.GetCurrentTimeStamp();
    expect ISO8601?(CurrentTime);
  }

  lemma ISO8601Test()
  {
    assert ISO8601?("YYYY-MM-DDTHH:mm:ss.ssssssZ");
    assert ISO8601?("2024-08-06T17:23:25.000874Z");
  }

  predicate ISO8601?(
    CreateTime: string
  )
  {
    // “YYYY-MM-DDTHH:mm:ss.ssssssZ“
    && |CreateTime| == 27
    && CreateTime[4] == '-'
    && CreateTime[7] == '-'
    && CreateTime[10] == 'T'
    && CreateTime[13] == ':'
    && CreateTime[16] == ':'
    && CreateTime[19] == '.'
    && CreateTime[26] == 'Z'
  }

}
