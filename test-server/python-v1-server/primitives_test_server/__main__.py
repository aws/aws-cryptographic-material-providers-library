# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Entry point: ``python -m primitives_test_server <port>`` starts the server.

The port is the first positional argument, defaulting to the
PRIMITIVES_TESTSERVER_PORT env var, then 8091.
"""

import os
import sys

from .app import serve


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv:
        port = int(argv[0])
    else:
        port = int(os.environ.get("PRIMITIVES_TESTSERVER_PORT", "8091"))
    serve(port)


if __name__ == "__main__":
    main()
