// Code generated by smithy-go-codegen DO NOT EDIT.

package awscryptographymaterialproviderssmithygeneratedtypes

import (
	"fmt"
)

type AwsCryptographicMaterialProvidersException struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e AwsCryptographicMaterialProvidersException) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidDecryptionMaterials struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidDecryptionMaterials) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidEncryptionMaterials struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidEncryptionMaterials) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidAlgorithmSuiteInfo struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidAlgorithmSuiteInfo) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidAlgorithmSuiteInfoOnDecrypt struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidAlgorithmSuiteInfoOnDecrypt) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidAlgorithmSuiteInfoOnEncrypt struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidAlgorithmSuiteInfoOnEncrypt) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidDecryptionMaterialsTransition struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidDecryptionMaterialsTransition) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type InvalidEncryptionMaterialsTransition struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e InvalidEncryptionMaterialsTransition) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type EntryAlreadyExists struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e EntryAlreadyExists) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}

type EntryDoesNotExist struct {
	AwsCryptographicMaterialProvidersBaseException
	Message           string
	ErrorCodeOverride *string
}

func (e EntryDoesNotExist) Error() string {
	return fmt.Sprintf("%s: %s", e.ErrorCodeOverride, e.Message)
}