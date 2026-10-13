# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Entry point: ``python -m mpl_test_server <port>`` starts the server.

The port is the first positional argument, defaulting to 8103.
"""

import sys

from .app import serve


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    serve(int(argv[0]) if argv else 8103)


if __name__ == "__main__":
    main()
