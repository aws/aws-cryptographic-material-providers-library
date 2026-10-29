// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Runnable entry point for the Go MPL Language_Server: binds an rpcv2Cbor
// HTTP endpoint on the port given as the first CLI argument (default 8104).

package main

import (
	"fmt"
	"net"
	"net/http"
	"os"
	"strconv"
)

func main() {
	port := 8104
	if len(os.Args) > 1 {
		if parsed, err := strconv.Atoi(os.Args[1]); err == nil && parsed > 0 && parsed <= 65535 {
			port = parsed
		}
	}

	state, err := newAppState()
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to construct the MaterialProviders client: %v\n", err)
		os.Exit(1)
	}

	addr := fmt.Sprintf("127.0.0.1:%d", port)
	listener, err := net.Listen("tcp", addr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to bind %s: %v\n", addr, err)
		os.Exit(1)
	}
	fmt.Fprintf(os.Stderr, "listening at http://%s\n", addr)
	server := &http.Server{Handler: newHandler(state)}
	if err := server.Serve(listener); err != nil {
		fmt.Fprintf(os.Stderr, "server error: %v\n", err)
		os.Exit(1)
	}
}
