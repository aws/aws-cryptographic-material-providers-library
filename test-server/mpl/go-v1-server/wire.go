// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// rpcv2Cbor HTTP wire layer: routes POST /service/{Service}/operation/{Operation},
// validates the protocol headers, decodes the CBOR request body, dispatches to
// a handler, and encodes the CBOR response or a modeled error.

package main

import (
	"errors"
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"

	keystoretypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographykeystoresmithygeneratedtypes"
	mpltypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl/awscryptographymaterialproviderssmithygeneratedtypes"
	"github.com/aws/smithy-go/encoding/cbor"
)

const (
	serviceName      = "MPLTestServer"
	errorNamespace   = "aws.cryptography.mpl.testserver"
	genericErrorType = errorNamespace + "#GenericServerError"
	mplErrorType     = errorNamespace + "#MPLClientError"
	smithyProtocol   = "rpc-v2-cbor"
	cborContentType  = "application/cbor"
)

// serverError is one of the two modeled TestServer errors. collectedErrors is
// MPLClientError's collectedErrors, or nil when the error collected none.
type serverError struct {
	typeID          string
	message         string
	collectedErrors []string
}

// generic builds a GenericServerError: a failure originating in the TestServer
// framework itself (bad headers, unknown operation, malformed request, bad
// handle).
func generic(format string, args ...any) *serverError {
	return &serverError{typeID: genericErrorType, message: fmt.Sprintf(format, args...)}
}

// mplError builds an MPLClientError: a failure raised by the Material
// Providers Library, carrying the library error's message.
func mplError(message string) *serverError {
	return &serverError{typeID: mplErrorType, message: message}
}

// mplFailure builds the MPLClientError for an error the MPL returned. A Dafny
// CollectionOfErrors, from the MPL or its key store, also carries the message
// of each error it collected.
func mplFailure(err error) *serverError {
	var collected []error
	var mplErrors mpltypes.CollectionOfErrors
	var keyStoreErrors keystoretypes.CollectionOfErrors
	switch {
	case errors.As(err, &mplErrors):
		collected = mplErrors.ListOfErrors
	case errors.As(err, &keyStoreErrors):
		collected = keyStoreErrors.ListOfErrors
	}
	out := mplError(err.Error())
	for _, e := range collected {
		out.collectedErrors = append(out.collectedErrors, e.Error())
	}
	return out
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
// outcome is a modeled success response, a GenericServerError, or an
// MPLClientError; a panic from the generated bindings becomes a
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
	case "CreateRawAesKeyring":
		out, serr = state.createRawAesKeyring(ctx, req)
	case "CreateStaticKeyring":
		out, serr = state.createStaticKeyring(ctx, req)
	case "CreateDefaultCmm":
		out, serr = state.createDefaultCmm(ctx, req)
	case "CreateKeyStoreClient":
		out, serr = state.createKeyStoreClient(ctx, req)
	case "CreateCryptographicMaterialsCache":
		out, serr = state.createCryptographicMaterialsCache(ctx, req)
	case "CreateAwsKmsHierarchicalKeyring":
		out, serr = state.createAwsKmsHierarchicalKeyring(ctx, req)
	case "CreateAwsKmsKeyring":
		out, serr = state.createAwsKmsKeyring(ctx, req)
	case "InitializeEncryptionMaterials":
		out, serr = state.initializeEncryptionMaterials(ctx, req)
	case "InitializeDecryptionMaterials":
		out, serr = state.initializeDecryptionMaterials(ctx, req)
	case "OnEncrypt":
		out, serr = state.onEncrypt(req)
	case "OnDecrypt":
		out, serr = state.onDecrypt(req)
	case "GetEncryptionMaterials":
		out, serr = state.getEncryptionMaterials(req)
	case "DecryptMaterials":
		out, serr = state.decryptMaterials(req)
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
	body := cbor.Map{
		"__type":  cbor.String(e.typeID),
		"message": cbor.String(e.message),
	}
	if len(e.collectedErrors) > 0 {
		collected := cbor.List{}
		for _, message := range e.collectedErrors {
			collected = append(collected, cbor.String(message))
		}
		body["collectedErrors"] = collected
	}
	return http.StatusBadRequest, cbor.Encode(body)
}
