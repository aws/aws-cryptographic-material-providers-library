# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import sys

"""
MPL's Dafny code parses the TestVectors JSON recursively.
i.e. GetTests(Json) = (Json[0], GetTests(Json[1:]))
The MPL Test Vectors generates more than the default recursion of 1000.
MPL test vectors exceeds Python's recursion limit when parsing the JSON, which needs >1 call per test vector.
(Other Crypto Tools languages are limited by memory; Python's explicit limit on function calls is unique.)
"""
sys.setrecursionlimit(100000) #previous recursion limit 10,000

# Initialize generated Dafny
from .internaldafny.generated import module_

# Initialize externs
from .internaldafny import extern
