// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// rpcv2Cbor HTTP wire layer: routes POST /service/{Service}/operation/{Operation},
// validates the protocol headers, decodes the CBOR request body, dispatches to
// a handler, and encodes the CBOR response or a modeled error.

package main

import (
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"

	"github.com/aws/smithy-go/encoding/cbor"
)

const (
	serviceName         = "PrimitivesTestServer"
	errorNamespace      = "aws.cryptography.primitives.testserver"
	genericErrorType    = errorNamespace + "#GenericServerError"
	primitivesErrorType = errorNamespace + "#PrimitivesError"
	smithyProtocol      = "rpc-v2-cbor"
	cborContentType     = "application/cbor"
)

// serverError is one of the two modeled TestServer errors.
type serverError struct {
	typeID  string
	message string
}

// generic builds a GenericServerError: a failure originating in the TestServer
// framework itself (bad headers, unknown operation, malformed request).
func generic(format string, args ...any) *serverError {
	return &serverError{typeID: genericErrorType, message: fmt.Sprintf(format, args...)}
}

// primitivesError builds a PrimitivesError: a failure forwarded from the
// AtomicPrimitives client, carrying the library error's message.
func primitivesError(message string) *serverError {
	return &serverError{typeID: primitivesErrorType, message: message}
}

// newHandler builds the HTTP handler. Shared with tests so they drive the real
// wire path.
func newHandler(state *appState) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		status, body := dispatch(state, r)
		w.Header().Set("smithy-protocol", smithyProtocol)
		w.Header().Set("Content-Type", cborContentType)
		// An explicit Content-Length keeps every response eligible for
		// HTTP/1.1 keep-alive (the generated Test_Client pools connections).
		w.Header().Set("Content-Length", strconv.Itoa(len(body)))
		w.WriteHeader(status)
		_, _ = w.Write(body)
	})
}

// dispatch runs one operation and returns the HTTP status and CBOR body. Every
// outcome is a modeled success response, a GenericServerError, or a
// PrimitivesError; a panic from the generated bindings becomes a
// GenericServerError.
func dispatch(state *appState, r *http.Request) (status int, body []byte) {
	defer func() {
		if p := recover(); p != nil {
			status, body = errorResponse(generic("unexpected server error: %v", p))
		}
	}()

	if r.Method != http.MethodPost {
		return errorResponse(generic("unsupported method %s; expected POST", r.Method))
	}
	service, operation, ok := parsePath(r.URL.Path)
	if !ok {
		return errorResponse(generic("unknown operation: %s", r.URL.Path))
	}
	if service != serviceName {
		return errorResponse(generic("unknown service: %s; expected %s", service, serviceName))
	}
	if r.Header.Get("smithy-protocol") != smithyProtocol {
		return errorResponse(generic("missing or invalid smithy-protocol header; expected %s", smithyProtocol))
	}
	if r.Header.Get("Content-Type") != cborContentType {
		return errorResponse(generic("missing or invalid content-type; expected %s", cborContentType))
	}
	payload, err := io.ReadAll(r.Body)
	if err != nil {
		return errorResponse(generic("failed to read request body: %v", err))
	}
	req, err := decodeBody(payload)
	if err != nil {
		return errorResponse(generic("failed to decode CBOR request: %v", err))
	}

	ctx := r.Context()
	var out cbor.Value
	var serr *serverError
	switch operation {
	case "AesEncrypt":
		out, serr = state.aesEncrypt(ctx, req)
	case "AesDecrypt":
		out, serr = state.aesDecrypt(ctx, req)
	case "GenerateRandomBytes":
		out, serr = state.generateRandomBytes(ctx, req)
	case "Digest":
		out, serr = state.digest(ctx, req)
	case "Hmac":
		out, serr = state.hmac(ctx, req)
	case "Hkdf":
		out, serr = state.hkdf(ctx, req)
	case "KbkdfCtrHmac":
		serr = generic("KbkdfCtrHmac is not supported by the go language server")
	case "EcdsaGenerateKeyPair":
		out, serr = state.ecdsaGenerateKeyPair(ctx, req)
	case "EcdsaSign":
		out, serr = state.ecdsaSign(ctx, req)
	case "EcdsaVerify":
		out, serr = state.ecdsaVerify(ctx, req)
	default:
		serr = generic("unknown operation: %s", operation)
	}
	if serr != nil {
		return errorResponse(serr)
	}
	return http.StatusOK, cbor.Encode(out)
}

// parsePath extracts the service and operation from /service/{s}/operation/{o}.
func parsePath(path string) (service, operation string, ok bool) {
	parts := strings.Split(strings.Trim(path, "/"), "/")
	if len(parts) != 4 || parts[0] != "service" || parts[2] != "operation" {
		return "", "", false
	}
	return parts[1], parts[3], true
}

// errorResponse serializes a modeled error to its rpcv2Cbor wire form: HTTP 400
// (both errors carry @error("client")) with a CBOR map carrying the __type
// discriminator so the generated Test_Client maps it back to the modeled type.
func errorResponse(e *serverError) (int, []byte) {
	return http.StatusBadRequest, cbor.Encode(cbor.Map{
		"__type":  cbor.String(e.typeID),
		"message": cbor.String(e.message),
	})
}
