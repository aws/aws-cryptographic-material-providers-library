import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_internal_kms.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries

# Module: ComAmazonawsKmsTypes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsValid__AliasNameType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__ArnType(x):
        return ((20) <= (len(x))) and ((len(x)) <= (2048))

    @staticmethod
    def IsValid__AttestationDocumentType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (262144))

    @staticmethod
    def IsValid__CiphertextType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (6144))

    @staticmethod
    def IsValid__CloudHsmClusterIdType(x):
        return ((19) <= (len(x))) and ((len(x)) <= (24))

    @staticmethod
    def IsValid__CustomKeyStoreIdType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (64))

    @staticmethod
    def IsValid__CustomKeyStoreNameType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__DescriptionType(x):
        return ((0) <= (len(x))) and ((len(x)) <= (8192))

    @staticmethod
    def IsValid__GrantIdType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__GrantNameType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__GrantTokenList(x):
        return ((0) <= (len(x))) and ((len(x)) <= (10))

    @staticmethod
    def IsValid__GrantTokenType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (8192))

    @staticmethod
    def IsValid__KeyIdType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (2048))

    @staticmethod
    def IsValid__KeyStorePasswordType(x):
        return ((7) <= (len(x))) and ((len(x)) <= (32))

    @staticmethod
    def IsValid__LimitType(x):
        return ((1) <= (x)) and ((x) <= (1000))

    @staticmethod
    def IsValid__MarkerType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (1024))

    @staticmethod
    def IsValid__NumberOfBytesType(x):
        return ((1) <= (x)) and ((x) <= (1024))

    @staticmethod
    def IsValid__PendingWindowInDaysType(x):
        return ((1) <= (x)) and ((x) <= (365))

    @staticmethod
    def IsValid__PlaintextType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (4096))

    @staticmethod
    def IsValid__PolicyNameType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__PolicyType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (131072))

    @staticmethod
    def IsValid__PrincipalIdType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__PublicKeyType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (8192))

    @staticmethod
    def IsValid__RegionType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (32))

    @staticmethod
    def IsValid__RotationPeriodInDaysType(x):
        return ((90) <= (x)) and ((x) <= (2560))

    @staticmethod
    def IsValid__TagKeyType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__TagValueType(x):
        return ((0) <= (len(x))) and ((len(x)) <= (256))

    @staticmethod
    def IsValid__TrustAnchorCertificateType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (5000))

    @staticmethod
    def IsValid__XksKeyIdType(x):
        return ((1) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__XksProxyAuthenticationAccessKeyIdType(x):
        return ((20) <= (len(x))) and ((len(x)) <= (30))

    @staticmethod
    def IsValid__XksProxyAuthenticationRawSecretAccessKeyType(x):
        return ((43) <= (len(x))) and ((len(x)) <= (64))

    @staticmethod
    def IsValid__XksProxyUriEndpointType(x):
        return ((10) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__XksProxyUriPathType(x):
        return ((10) <= (len(x))) and ((len(x)) <= (128))

    @staticmethod
    def IsValid__XksProxyVpcEndpointServiceNameType(x):
        return ((20) <= (len(x))) and ((len(x)) <= (64))


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class AlgorithmSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AlgorithmSpec_RSAES__PKCS1__V1__5(), AlgorithmSpec_RSAES__OAEP__SHA__1(), AlgorithmSpec_RSAES__OAEP__SHA__256(), AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1(), AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256(), AlgorithmSpec_SM2PKE()]
    @classmethod
    def default(cls, ):
        return lambda: AlgorithmSpec_RSAES__PKCS1__V1__5()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSAES__PKCS1__V1__5(self) -> bool:
        return isinstance(self, AlgorithmSpec_RSAES__PKCS1__V1__5)
    @property
    def is_RSAES__OAEP__SHA__1(self) -> bool:
        return isinstance(self, AlgorithmSpec_RSAES__OAEP__SHA__1)
    @property
    def is_RSAES__OAEP__SHA__256(self) -> bool:
        return isinstance(self, AlgorithmSpec_RSAES__OAEP__SHA__256)
    @property
    def is_RSA__AES__KEY__WRAP__SHA__1(self) -> bool:
        return isinstance(self, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1)
    @property
    def is_RSA__AES__KEY__WRAP__SHA__256(self) -> bool:
        return isinstance(self, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256)
    @property
    def is_SM2PKE(self) -> bool:
        return isinstance(self, AlgorithmSpec_SM2PKE)

class AlgorithmSpec_RSAES__PKCS1__V1__5(AlgorithmSpec, NamedTuple('RSAES__PKCS1__V1__5', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.RSAES_PKCS1_V1_5'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_RSAES__PKCS1__V1__5)
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSpec_RSAES__OAEP__SHA__1(AlgorithmSpec, NamedTuple('RSAES__OAEP__SHA__1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.RSAES_OAEP_SHA_1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_RSAES__OAEP__SHA__1)
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSpec_RSAES__OAEP__SHA__256(AlgorithmSpec, NamedTuple('RSAES__OAEP__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.RSAES_OAEP_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_RSAES__OAEP__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1(AlgorithmSpec, NamedTuple('RSA__AES__KEY__WRAP__SHA__1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.RSA_AES_KEY_WRAP_SHA_1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1)
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256(AlgorithmSpec, NamedTuple('RSA__AES__KEY__WRAP__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.RSA_AES_KEY_WRAP_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSpec_SM2PKE(AlgorithmSpec, NamedTuple('SM2PKE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AlgorithmSpec.SM2PKE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AlgorithmSpec_SM2PKE)
    def __hash__(self) -> int:
        return super().__hash__()


class AliasListEntry:
    @classmethod
    def default(cls, ):
        return lambda: AliasListEntry_AliasListEntry(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AliasListEntry(self) -> bool:
        return isinstance(self, AliasListEntry_AliasListEntry)

class AliasListEntry_AliasListEntry(AliasListEntry, NamedTuple('AliasListEntry', [('AliasName', Any), ('AliasArn', Any), ('TargetKeyId', Any), ('CreationDate', Any), ('LastUpdatedDate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.AliasListEntry.AliasListEntry({_dafny.string_of(self.AliasName)}, {_dafny.string_of(self.AliasArn)}, {_dafny.string_of(self.TargetKeyId)}, {_dafny.string_of(self.CreationDate)}, {_dafny.string_of(self.LastUpdatedDate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AliasListEntry_AliasListEntry) and self.AliasName == __o.AliasName and self.AliasArn == __o.AliasArn and self.TargetKeyId == __o.TargetKeyId and self.CreationDate == __o.CreationDate and self.LastUpdatedDate == __o.LastUpdatedDate
    def __hash__(self) -> int:
        return super().__hash__()


class AliasNameType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_0_x_: _dafny.Seq = source__
        return default__.IsValid__AliasNameType(d_0_x_)

class ArnType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_x_: _dafny.Seq = source__
        return default__.IsValid__ArnType(d_1_x_)

class AttestationDocumentType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_2_x_: _dafny.Seq = source__
        return default__.IsValid__AttestationDocumentType(d_2_x_)

class CancelKeyDeletionRequest:
    @classmethod
    def default(cls, ):
        return lambda: CancelKeyDeletionRequest_CancelKeyDeletionRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CancelKeyDeletionRequest(self) -> bool:
        return isinstance(self, CancelKeyDeletionRequest_CancelKeyDeletionRequest)

class CancelKeyDeletionRequest_CancelKeyDeletionRequest(CancelKeyDeletionRequest, NamedTuple('CancelKeyDeletionRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CancelKeyDeletionRequest.CancelKeyDeletionRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CancelKeyDeletionRequest_CancelKeyDeletionRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class CancelKeyDeletionResponse:
    @classmethod
    def default(cls, ):
        return lambda: CancelKeyDeletionResponse_CancelKeyDeletionResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CancelKeyDeletionResponse(self) -> bool:
        return isinstance(self, CancelKeyDeletionResponse_CancelKeyDeletionResponse)

class CancelKeyDeletionResponse_CancelKeyDeletionResponse(CancelKeyDeletionResponse, NamedTuple('CancelKeyDeletionResponse', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CancelKeyDeletionResponse.CancelKeyDeletionResponse({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CancelKeyDeletionResponse_CancelKeyDeletionResponse) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class CiphertextType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_3_x_: _dafny.Seq = source__
        return default__.IsValid__CiphertextType(d_3_x_)

class CloudHsmClusterIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_4_x_: _dafny.Seq = source__
        return default__.IsValid__CloudHsmClusterIdType(d_4_x_)

class ConnectCustomKeyStoreRequest:
    @classmethod
    def default(cls, ):
        return lambda: ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ConnectCustomKeyStoreRequest(self) -> bool:
        return isinstance(self, ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest)

class ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest(ConnectCustomKeyStoreRequest, NamedTuple('ConnectCustomKeyStoreRequest', [('CustomKeyStoreId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectCustomKeyStoreRequest.ConnectCustomKeyStoreRequest({_dafny.string_of(self.CustomKeyStoreId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest) and self.CustomKeyStoreId == __o.CustomKeyStoreId
    def __hash__(self) -> int:
        return super().__hash__()


class ConnectCustomKeyStoreResponse:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse()]
    @classmethod
    def default(cls, ):
        return lambda: ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ConnectCustomKeyStoreResponse(self) -> bool:
        return isinstance(self, ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse)

class ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse(ConnectCustomKeyStoreResponse, NamedTuple('ConnectCustomKeyStoreResponse', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectCustomKeyStoreResponse.ConnectCustomKeyStoreResponse'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse)
    def __hash__(self) -> int:
        return super().__hash__()


class ConnectionErrorCodeType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConnectionErrorCodeType_INVALID__CREDENTIALS(), ConnectionErrorCodeType_CLUSTER__NOT__FOUND(), ConnectionErrorCodeType_NETWORK__ERRORS(), ConnectionErrorCodeType_INTERNAL__ERROR(), ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS(), ConnectionErrorCodeType_USER__LOCKED__OUT(), ConnectionErrorCodeType_USER__NOT__FOUND(), ConnectionErrorCodeType_USER__LOGGED__IN(), ConnectionErrorCodeType_SUBNET__NOT__FOUND(), ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET(), ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED(), ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE(), ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND(), ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE(), ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION(), ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION(), ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT(), ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION()]
    @classmethod
    def default(cls, ):
        return lambda: ConnectionErrorCodeType_INVALID__CREDENTIALS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_INVALID__CREDENTIALS(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_INVALID__CREDENTIALS)
    @property
    def is_CLUSTER__NOT__FOUND(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_CLUSTER__NOT__FOUND)
    @property
    def is_NETWORK__ERRORS(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_NETWORK__ERRORS)
    @property
    def is_INTERNAL__ERROR(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_INTERNAL__ERROR)
    @property
    def is_INSUFFICIENT__CLOUDHSM__HSMS(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS)
    @property
    def is_USER__LOCKED__OUT(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_USER__LOCKED__OUT)
    @property
    def is_USER__NOT__FOUND(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_USER__NOT__FOUND)
    @property
    def is_USER__LOGGED__IN(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_USER__LOGGED__IN)
    @property
    def is_SUBNET__NOT__FOUND(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_SUBNET__NOT__FOUND)
    @property
    def is_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET)
    @property
    def is_XKS__PROXY__ACCESS__DENIED(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED)
    @property
    def is_XKS__PROXY__NOT__REACHABLE(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE)
    @property
    def is_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND)
    @property
    def is_XKS__PROXY__INVALID__RESPONSE(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE)
    @property
    def is_XKS__PROXY__INVALID__CONFIGURATION(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION)
    @property
    def is_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION)
    @property
    def is_XKS__PROXY__TIMED__OUT(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT)
    @property
    def is_XKS__PROXY__INVALID__TLS__CONFIGURATION(self) -> bool:
        return isinstance(self, ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION)

class ConnectionErrorCodeType_INVALID__CREDENTIALS(ConnectionErrorCodeType, NamedTuple('INVALID__CREDENTIALS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.INVALID_CREDENTIALS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_INVALID__CREDENTIALS)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_CLUSTER__NOT__FOUND(ConnectionErrorCodeType, NamedTuple('CLUSTER__NOT__FOUND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.CLUSTER_NOT_FOUND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_CLUSTER__NOT__FOUND)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_NETWORK__ERRORS(ConnectionErrorCodeType, NamedTuple('NETWORK__ERRORS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.NETWORK_ERRORS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_NETWORK__ERRORS)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_INTERNAL__ERROR(ConnectionErrorCodeType, NamedTuple('INTERNAL__ERROR', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.INTERNAL_ERROR'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_INTERNAL__ERROR)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS(ConnectionErrorCodeType, NamedTuple('INSUFFICIENT__CLOUDHSM__HSMS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.INSUFFICIENT_CLOUDHSM_HSMS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_USER__LOCKED__OUT(ConnectionErrorCodeType, NamedTuple('USER__LOCKED__OUT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.USER_LOCKED_OUT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_USER__LOCKED__OUT)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_USER__NOT__FOUND(ConnectionErrorCodeType, NamedTuple('USER__NOT__FOUND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.USER_NOT_FOUND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_USER__NOT__FOUND)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_USER__LOGGED__IN(ConnectionErrorCodeType, NamedTuple('USER__LOGGED__IN', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.USER_LOGGED_IN'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_USER__LOGGED__IN)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_SUBNET__NOT__FOUND(ConnectionErrorCodeType, NamedTuple('SUBNET__NOT__FOUND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.SUBNET_NOT_FOUND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_SUBNET__NOT__FOUND)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET(ConnectionErrorCodeType, NamedTuple('INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__ACCESS__DENIED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_ACCESS_DENIED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__NOT__REACHABLE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_NOT_REACHABLE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND(ConnectionErrorCodeType, NamedTuple('XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__INVALID__RESPONSE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_INVALID_RESPONSE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__INVALID__CONFIGURATION', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_INVALID_CONFIGURATION'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION(ConnectionErrorCodeType, NamedTuple('XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__TIMED__OUT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_TIMED_OUT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION(ConnectionErrorCodeType, NamedTuple('XKS__PROXY__INVALID__TLS__CONFIGURATION', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_INVALID_TLS_CONFIGURATION'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION)
    def __hash__(self) -> int:
        return super().__hash__()


class ConnectionStateType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConnectionStateType_CONNECTED(), ConnectionStateType_CONNECTING(), ConnectionStateType_FAILED(), ConnectionStateType_DISCONNECTED(), ConnectionStateType_DISCONNECTING()]
    @classmethod
    def default(cls, ):
        return lambda: ConnectionStateType_CONNECTED()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CONNECTED(self) -> bool:
        return isinstance(self, ConnectionStateType_CONNECTED)
    @property
    def is_CONNECTING(self) -> bool:
        return isinstance(self, ConnectionStateType_CONNECTING)
    @property
    def is_FAILED(self) -> bool:
        return isinstance(self, ConnectionStateType_FAILED)
    @property
    def is_DISCONNECTED(self) -> bool:
        return isinstance(self, ConnectionStateType_DISCONNECTED)
    @property
    def is_DISCONNECTING(self) -> bool:
        return isinstance(self, ConnectionStateType_DISCONNECTING)

class ConnectionStateType_CONNECTED(ConnectionStateType, NamedTuple('CONNECTED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionStateType.CONNECTED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionStateType_CONNECTED)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionStateType_CONNECTING(ConnectionStateType, NamedTuple('CONNECTING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionStateType.CONNECTING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionStateType_CONNECTING)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionStateType_FAILED(ConnectionStateType, NamedTuple('FAILED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionStateType.FAILED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionStateType_FAILED)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionStateType_DISCONNECTED(ConnectionStateType, NamedTuple('DISCONNECTED', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionStateType.DISCONNECTED'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionStateType_DISCONNECTED)
    def __hash__(self) -> int:
        return super().__hash__()

class ConnectionStateType_DISCONNECTING(ConnectionStateType, NamedTuple('DISCONNECTING', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ConnectionStateType.DISCONNECTING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConnectionStateType_DISCONNECTING)
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAliasRequest:
    @classmethod
    def default(cls, ):
        return lambda: CreateAliasRequest_CreateAliasRequest(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAliasRequest(self) -> bool:
        return isinstance(self, CreateAliasRequest_CreateAliasRequest)

class CreateAliasRequest_CreateAliasRequest(CreateAliasRequest, NamedTuple('CreateAliasRequest', [('AliasName', Any), ('TargetKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateAliasRequest.CreateAliasRequest({_dafny.string_of(self.AliasName)}, {_dafny.string_of(self.TargetKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateAliasRequest_CreateAliasRequest) and self.AliasName == __o.AliasName and self.TargetKeyId == __o.TargetKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class CreateCustomKeyStoreRequest:
    @classmethod
    def default(cls, ):
        return lambda: CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateCustomKeyStoreRequest(self) -> bool:
        return isinstance(self, CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest)

class CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest(CreateCustomKeyStoreRequest, NamedTuple('CreateCustomKeyStoreRequest', [('CustomKeyStoreName', Any), ('CloudHsmClusterId', Any), ('TrustAnchorCertificate', Any), ('KeyStorePassword', Any), ('CustomKeyStoreType', Any), ('XksProxyUriEndpoint', Any), ('XksProxyUriPath', Any), ('XksProxyVpcEndpointServiceName', Any), ('XksProxyAuthenticationCredential', Any), ('XksProxyConnectivity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateCustomKeyStoreRequest.CreateCustomKeyStoreRequest({_dafny.string_of(self.CustomKeyStoreName)}, {_dafny.string_of(self.CloudHsmClusterId)}, {_dafny.string_of(self.TrustAnchorCertificate)}, {_dafny.string_of(self.KeyStorePassword)}, {_dafny.string_of(self.CustomKeyStoreType)}, {_dafny.string_of(self.XksProxyUriEndpoint)}, {_dafny.string_of(self.XksProxyUriPath)}, {_dafny.string_of(self.XksProxyVpcEndpointServiceName)}, {_dafny.string_of(self.XksProxyAuthenticationCredential)}, {_dafny.string_of(self.XksProxyConnectivity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest) and self.CustomKeyStoreName == __o.CustomKeyStoreName and self.CloudHsmClusterId == __o.CloudHsmClusterId and self.TrustAnchorCertificate == __o.TrustAnchorCertificate and self.KeyStorePassword == __o.KeyStorePassword and self.CustomKeyStoreType == __o.CustomKeyStoreType and self.XksProxyUriEndpoint == __o.XksProxyUriEndpoint and self.XksProxyUriPath == __o.XksProxyUriPath and self.XksProxyVpcEndpointServiceName == __o.XksProxyVpcEndpointServiceName and self.XksProxyAuthenticationCredential == __o.XksProxyAuthenticationCredential and self.XksProxyConnectivity == __o.XksProxyConnectivity
    def __hash__(self) -> int:
        return super().__hash__()


class CreateCustomKeyStoreResponse:
    @classmethod
    def default(cls, ):
        return lambda: CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateCustomKeyStoreResponse(self) -> bool:
        return isinstance(self, CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse)

class CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse(CreateCustomKeyStoreResponse, NamedTuple('CreateCustomKeyStoreResponse', [('CustomKeyStoreId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateCustomKeyStoreResponse.CreateCustomKeyStoreResponse({_dafny.string_of(self.CustomKeyStoreId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse) and self.CustomKeyStoreId == __o.CustomKeyStoreId
    def __hash__(self) -> int:
        return super().__hash__()


class CreateGrantRequest:
    @classmethod
    def default(cls, ):
        return lambda: CreateGrantRequest_CreateGrantRequest(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateGrantRequest(self) -> bool:
        return isinstance(self, CreateGrantRequest_CreateGrantRequest)

class CreateGrantRequest_CreateGrantRequest(CreateGrantRequest, NamedTuple('CreateGrantRequest', [('KeyId', Any), ('GranteePrincipal', Any), ('RetiringPrincipal', Any), ('Operations', Any), ('Constraints', Any), ('GrantTokens', Any), ('Name', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateGrantRequest.CreateGrantRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GranteePrincipal)}, {_dafny.string_of(self.RetiringPrincipal)}, {_dafny.string_of(self.Operations)}, {_dafny.string_of(self.Constraints)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.Name)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateGrantRequest_CreateGrantRequest) and self.KeyId == __o.KeyId and self.GranteePrincipal == __o.GranteePrincipal and self.RetiringPrincipal == __o.RetiringPrincipal and self.Operations == __o.Operations and self.Constraints == __o.Constraints and self.GrantTokens == __o.GrantTokens and self.Name == __o.Name and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class CreateGrantResponse:
    @classmethod
    def default(cls, ):
        return lambda: CreateGrantResponse_CreateGrantResponse(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateGrantResponse(self) -> bool:
        return isinstance(self, CreateGrantResponse_CreateGrantResponse)

class CreateGrantResponse_CreateGrantResponse(CreateGrantResponse, NamedTuple('CreateGrantResponse', [('GrantToken', Any), ('GrantId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateGrantResponse.CreateGrantResponse({_dafny.string_of(self.GrantToken)}, {_dafny.string_of(self.GrantId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateGrantResponse_CreateGrantResponse) and self.GrantToken == __o.GrantToken and self.GrantId == __o.GrantId
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyRequest_CreateKeyRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyRequest(self) -> bool:
        return isinstance(self, CreateKeyRequest_CreateKeyRequest)

class CreateKeyRequest_CreateKeyRequest(CreateKeyRequest, NamedTuple('CreateKeyRequest', [('Policy', Any), ('Description', Any), ('KeyUsage', Any), ('CustomerMasterKeySpec', Any), ('KeySpec', Any), ('Origin', Any), ('CustomKeyStoreId', Any), ('BypassPolicyLockoutSafetyCheck', Any), ('Tags', Any), ('MultiRegion', Any), ('XksKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateKeyRequest.CreateKeyRequest({_dafny.string_of(self.Policy)}, {_dafny.string_of(self.Description)}, {_dafny.string_of(self.KeyUsage)}, {_dafny.string_of(self.CustomerMasterKeySpec)}, {_dafny.string_of(self.KeySpec)}, {_dafny.string_of(self.Origin)}, {_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.BypassPolicyLockoutSafetyCheck)}, {_dafny.string_of(self.Tags)}, {_dafny.string_of(self.MultiRegion)}, {_dafny.string_of(self.XksKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyRequest_CreateKeyRequest) and self.Policy == __o.Policy and self.Description == __o.Description and self.KeyUsage == __o.KeyUsage and self.CustomerMasterKeySpec == __o.CustomerMasterKeySpec and self.KeySpec == __o.KeySpec and self.Origin == __o.Origin and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.BypassPolicyLockoutSafetyCheck == __o.BypassPolicyLockoutSafetyCheck and self.Tags == __o.Tags and self.MultiRegion == __o.MultiRegion and self.XksKeyId == __o.XksKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class CreateKeyResponse:
    @classmethod
    def default(cls, ):
        return lambda: CreateKeyResponse_CreateKeyResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateKeyResponse(self) -> bool:
        return isinstance(self, CreateKeyResponse_CreateKeyResponse)

class CreateKeyResponse_CreateKeyResponse(CreateKeyResponse, NamedTuple('CreateKeyResponse', [('KeyMetadata', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CreateKeyResponse.CreateKeyResponse({_dafny.string_of(self.KeyMetadata)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CreateKeyResponse_CreateKeyResponse) and self.KeyMetadata == __o.KeyMetadata
    def __hash__(self) -> int:
        return super().__hash__()


class CustomerMasterKeySpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CustomerMasterKeySpec_RSA__2048(), CustomerMasterKeySpec_RSA__3072(), CustomerMasterKeySpec_RSA__4096(), CustomerMasterKeySpec_ECC__NIST__P256(), CustomerMasterKeySpec_ECC__NIST__P384(), CustomerMasterKeySpec_ECC__NIST__P521(), CustomerMasterKeySpec_ECC__SECG__P256K1(), CustomerMasterKeySpec_SYMMETRIC__DEFAULT(), CustomerMasterKeySpec_HMAC__224(), CustomerMasterKeySpec_HMAC__256(), CustomerMasterKeySpec_HMAC__384(), CustomerMasterKeySpec_HMAC__512(), CustomerMasterKeySpec_SM2()]
    @classmethod
    def default(cls, ):
        return lambda: CustomerMasterKeySpec_RSA__2048()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSA__2048(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_RSA__2048)
    @property
    def is_RSA__3072(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_RSA__3072)
    @property
    def is_RSA__4096(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_RSA__4096)
    @property
    def is_ECC__NIST__P256(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_ECC__NIST__P256)
    @property
    def is_ECC__NIST__P384(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_ECC__NIST__P384)
    @property
    def is_ECC__NIST__P521(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_ECC__NIST__P521)
    @property
    def is_ECC__SECG__P256K1(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_ECC__SECG__P256K1)
    @property
    def is_SYMMETRIC__DEFAULT(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_SYMMETRIC__DEFAULT)
    @property
    def is_HMAC__224(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_HMAC__224)
    @property
    def is_HMAC__256(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_HMAC__256)
    @property
    def is_HMAC__384(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_HMAC__384)
    @property
    def is_HMAC__512(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_HMAC__512)
    @property
    def is_SM2(self) -> bool:
        return isinstance(self, CustomerMasterKeySpec_SM2)

class CustomerMasterKeySpec_RSA__2048(CustomerMasterKeySpec, NamedTuple('RSA__2048', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.RSA_2048'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_RSA__2048)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_RSA__3072(CustomerMasterKeySpec, NamedTuple('RSA__3072', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.RSA_3072'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_RSA__3072)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_RSA__4096(CustomerMasterKeySpec, NamedTuple('RSA__4096', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.RSA_4096'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_RSA__4096)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_ECC__NIST__P256(CustomerMasterKeySpec, NamedTuple('ECC__NIST__P256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.ECC_NIST_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_ECC__NIST__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_ECC__NIST__P384(CustomerMasterKeySpec, NamedTuple('ECC__NIST__P384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.ECC_NIST_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_ECC__NIST__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_ECC__NIST__P521(CustomerMasterKeySpec, NamedTuple('ECC__NIST__P521', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.ECC_NIST_P521'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_ECC__NIST__P521)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_ECC__SECG__P256K1(CustomerMasterKeySpec, NamedTuple('ECC__SECG__P256K1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.ECC_SECG_P256K1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_ECC__SECG__P256K1)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_SYMMETRIC__DEFAULT(CustomerMasterKeySpec, NamedTuple('SYMMETRIC__DEFAULT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.SYMMETRIC_DEFAULT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_SYMMETRIC__DEFAULT)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_HMAC__224(CustomerMasterKeySpec, NamedTuple('HMAC__224', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_224'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_HMAC__224)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_HMAC__256(CustomerMasterKeySpec, NamedTuple('HMAC__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_HMAC__256)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_HMAC__384(CustomerMasterKeySpec, NamedTuple('HMAC__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_HMAC__384)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_HMAC__512(CustomerMasterKeySpec, NamedTuple('HMAC__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_HMAC__512)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomerMasterKeySpec_SM2(CustomerMasterKeySpec, NamedTuple('SM2', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomerMasterKeySpec.SM2'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomerMasterKeySpec_SM2)
    def __hash__(self) -> int:
        return super().__hash__()


class CustomKeyStoreIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_5_x_: _dafny.Seq = source__
        return default__.IsValid__CustomKeyStoreIdType(d_5_x_)

class CustomKeyStoreNameType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_6_x_: _dafny.Seq = source__
        return default__.IsValid__CustomKeyStoreNameType(d_6_x_)

class CustomKeyStoresListEntry:
    @classmethod
    def default(cls, ):
        return lambda: CustomKeyStoresListEntry_CustomKeyStoresListEntry(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CustomKeyStoresListEntry(self) -> bool:
        return isinstance(self, CustomKeyStoresListEntry_CustomKeyStoresListEntry)

class CustomKeyStoresListEntry_CustomKeyStoresListEntry(CustomKeyStoresListEntry, NamedTuple('CustomKeyStoresListEntry', [('CustomKeyStoreId', Any), ('CustomKeyStoreName', Any), ('CloudHsmClusterId', Any), ('TrustAnchorCertificate', Any), ('ConnectionState', Any), ('ConnectionErrorCode', Any), ('CreationDate', Any), ('CustomKeyStoreType', Any), ('XksProxyConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomKeyStoresListEntry.CustomKeyStoresListEntry({_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.CustomKeyStoreName)}, {_dafny.string_of(self.CloudHsmClusterId)}, {_dafny.string_of(self.TrustAnchorCertificate)}, {_dafny.string_of(self.ConnectionState)}, {_dafny.string_of(self.ConnectionErrorCode)}, {_dafny.string_of(self.CreationDate)}, {_dafny.string_of(self.CustomKeyStoreType)}, {_dafny.string_of(self.XksProxyConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomKeyStoresListEntry_CustomKeyStoresListEntry) and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.CustomKeyStoreName == __o.CustomKeyStoreName and self.CloudHsmClusterId == __o.CloudHsmClusterId and self.TrustAnchorCertificate == __o.TrustAnchorCertificate and self.ConnectionState == __o.ConnectionState and self.ConnectionErrorCode == __o.ConnectionErrorCode and self.CreationDate == __o.CreationDate and self.CustomKeyStoreType == __o.CustomKeyStoreType and self.XksProxyConfiguration == __o.XksProxyConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class CustomKeyStoreType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CustomKeyStoreType_AWS__CLOUDHSM(), CustomKeyStoreType_EXTERNAL__KEY__STORE()]
    @classmethod
    def default(cls, ):
        return lambda: CustomKeyStoreType_AWS__CLOUDHSM()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AWS__CLOUDHSM(self) -> bool:
        return isinstance(self, CustomKeyStoreType_AWS__CLOUDHSM)
    @property
    def is_EXTERNAL__KEY__STORE(self) -> bool:
        return isinstance(self, CustomKeyStoreType_EXTERNAL__KEY__STORE)

class CustomKeyStoreType_AWS__CLOUDHSM(CustomKeyStoreType, NamedTuple('AWS__CLOUDHSM', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomKeyStoreType.AWS_CLOUDHSM'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomKeyStoreType_AWS__CLOUDHSM)
    def __hash__(self) -> int:
        return super().__hash__()

class CustomKeyStoreType_EXTERNAL__KEY__STORE(CustomKeyStoreType, NamedTuple('EXTERNAL__KEY__STORE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.CustomKeyStoreType.EXTERNAL_KEY_STORE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CustomKeyStoreType_EXTERNAL__KEY__STORE)
    def __hash__(self) -> int:
        return super().__hash__()


class DataKeyPairSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DataKeyPairSpec_RSA__2048(), DataKeyPairSpec_RSA__3072(), DataKeyPairSpec_RSA__4096(), DataKeyPairSpec_ECC__NIST__P256(), DataKeyPairSpec_ECC__NIST__P384(), DataKeyPairSpec_ECC__NIST__P521(), DataKeyPairSpec_ECC__SECG__P256K1(), DataKeyPairSpec_SM2()]
    @classmethod
    def default(cls, ):
        return lambda: DataKeyPairSpec_RSA__2048()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSA__2048(self) -> bool:
        return isinstance(self, DataKeyPairSpec_RSA__2048)
    @property
    def is_RSA__3072(self) -> bool:
        return isinstance(self, DataKeyPairSpec_RSA__3072)
    @property
    def is_RSA__4096(self) -> bool:
        return isinstance(self, DataKeyPairSpec_RSA__4096)
    @property
    def is_ECC__NIST__P256(self) -> bool:
        return isinstance(self, DataKeyPairSpec_ECC__NIST__P256)
    @property
    def is_ECC__NIST__P384(self) -> bool:
        return isinstance(self, DataKeyPairSpec_ECC__NIST__P384)
    @property
    def is_ECC__NIST__P521(self) -> bool:
        return isinstance(self, DataKeyPairSpec_ECC__NIST__P521)
    @property
    def is_ECC__SECG__P256K1(self) -> bool:
        return isinstance(self, DataKeyPairSpec_ECC__SECG__P256K1)
    @property
    def is_SM2(self) -> bool:
        return isinstance(self, DataKeyPairSpec_SM2)

class DataKeyPairSpec_RSA__2048(DataKeyPairSpec, NamedTuple('RSA__2048', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.RSA_2048'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_RSA__2048)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_RSA__3072(DataKeyPairSpec, NamedTuple('RSA__3072', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.RSA_3072'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_RSA__3072)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_RSA__4096(DataKeyPairSpec, NamedTuple('RSA__4096', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.RSA_4096'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_RSA__4096)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_ECC__NIST__P256(DataKeyPairSpec, NamedTuple('ECC__NIST__P256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_NIST_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_ECC__NIST__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_ECC__NIST__P384(DataKeyPairSpec, NamedTuple('ECC__NIST__P384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_NIST_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_ECC__NIST__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_ECC__NIST__P521(DataKeyPairSpec, NamedTuple('ECC__NIST__P521', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_NIST_P521'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_ECC__NIST__P521)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_ECC__SECG__P256K1(DataKeyPairSpec, NamedTuple('ECC__SECG__P256K1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_SECG_P256K1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_ECC__SECG__P256K1)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeyPairSpec_SM2(DataKeyPairSpec, NamedTuple('SM2', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeyPairSpec.SM2'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeyPairSpec_SM2)
    def __hash__(self) -> int:
        return super().__hash__()


class DataKeySpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DataKeySpec_AES__256(), DataKeySpec_AES__128()]
    @classmethod
    def default(cls, ):
        return lambda: DataKeySpec_AES__256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES__256(self) -> bool:
        return isinstance(self, DataKeySpec_AES__256)
    @property
    def is_AES__128(self) -> bool:
        return isinstance(self, DataKeySpec_AES__128)

class DataKeySpec_AES__256(DataKeySpec, NamedTuple('AES__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeySpec.AES_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeySpec_AES__256)
    def __hash__(self) -> int:
        return super().__hash__()

class DataKeySpec_AES__128(DataKeySpec, NamedTuple('AES__128', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DataKeySpec.AES_128'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DataKeySpec_AES__128)
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptRequest:
    @classmethod
    def default(cls, ):
        return lambda: DecryptRequest_DecryptRequest(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptRequest(self) -> bool:
        return isinstance(self, DecryptRequest_DecryptRequest)

class DecryptRequest_DecryptRequest(DecryptRequest, NamedTuple('DecryptRequest', [('CiphertextBlob', Any), ('EncryptionContext', Any), ('GrantTokens', Any), ('KeyId', Any), ('EncryptionAlgorithm', Any), ('Recipient', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DecryptRequest.DecryptRequest({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.EncryptionAlgorithm)}, {_dafny.string_of(self.Recipient)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptRequest_DecryptRequest) and self.CiphertextBlob == __o.CiphertextBlob and self.EncryptionContext == __o.EncryptionContext and self.GrantTokens == __o.GrantTokens and self.KeyId == __o.KeyId and self.EncryptionAlgorithm == __o.EncryptionAlgorithm and self.Recipient == __o.Recipient and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptResponse:
    @classmethod
    def default(cls, ):
        return lambda: DecryptResponse_DecryptResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptResponse(self) -> bool:
        return isinstance(self, DecryptResponse_DecryptResponse)

class DecryptResponse_DecryptResponse(DecryptResponse, NamedTuple('DecryptResponse', [('KeyId', Any), ('Plaintext', Any), ('EncryptionAlgorithm', Any), ('CiphertextForRecipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DecryptResponse.DecryptResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Plaintext)}, {_dafny.string_of(self.EncryptionAlgorithm)}, {_dafny.string_of(self.CiphertextForRecipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DecryptResponse_DecryptResponse) and self.KeyId == __o.KeyId and self.Plaintext == __o.Plaintext and self.EncryptionAlgorithm == __o.EncryptionAlgorithm and self.CiphertextForRecipient == __o.CiphertextForRecipient
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteAliasRequest:
    @classmethod
    def default(cls, ):
        return lambda: DeleteAliasRequest_DeleteAliasRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteAliasRequest(self) -> bool:
        return isinstance(self, DeleteAliasRequest_DeleteAliasRequest)

class DeleteAliasRequest_DeleteAliasRequest(DeleteAliasRequest, NamedTuple('DeleteAliasRequest', [('AliasName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeleteAliasRequest.DeleteAliasRequest({_dafny.string_of(self.AliasName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteAliasRequest_DeleteAliasRequest) and self.AliasName == __o.AliasName
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteCustomKeyStoreRequest:
    @classmethod
    def default(cls, ):
        return lambda: DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteCustomKeyStoreRequest(self) -> bool:
        return isinstance(self, DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest)

class DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest(DeleteCustomKeyStoreRequest, NamedTuple('DeleteCustomKeyStoreRequest', [('CustomKeyStoreId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeleteCustomKeyStoreRequest.DeleteCustomKeyStoreRequest({_dafny.string_of(self.CustomKeyStoreId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest) and self.CustomKeyStoreId == __o.CustomKeyStoreId
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteCustomKeyStoreResponse:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse()]
    @classmethod
    def default(cls, ):
        return lambda: DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteCustomKeyStoreResponse(self) -> bool:
        return isinstance(self, DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse)

class DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse(DeleteCustomKeyStoreResponse, NamedTuple('DeleteCustomKeyStoreResponse', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeleteCustomKeyStoreResponse.DeleteCustomKeyStoreResponse'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse)
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteImportedKeyMaterialRequest:
    @classmethod
    def default(cls, ):
        return lambda: DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteImportedKeyMaterialRequest(self) -> bool:
        return isinstance(self, DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest)

class DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest(DeleteImportedKeyMaterialRequest, NamedTuple('DeleteImportedKeyMaterialRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeleteImportedKeyMaterialRequest.DeleteImportedKeyMaterialRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class DeriveSharedSecretRequest:
    @classmethod
    def default(cls, ):
        return lambda: DeriveSharedSecretRequest_DeriveSharedSecretRequest(_dafny.Seq(""), KeyAgreementAlgorithmSpec.default()(), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeriveSharedSecretRequest(self) -> bool:
        return isinstance(self, DeriveSharedSecretRequest_DeriveSharedSecretRequest)

class DeriveSharedSecretRequest_DeriveSharedSecretRequest(DeriveSharedSecretRequest, NamedTuple('DeriveSharedSecretRequest', [('KeyId', Any), ('KeyAgreementAlgorithm', Any), ('PublicKey', Any), ('GrantTokens', Any), ('DryRun', Any), ('Recipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeriveSharedSecretRequest.DeriveSharedSecretRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyAgreementAlgorithm)}, {_dafny.string_of(self.PublicKey)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)}, {_dafny.string_of(self.Recipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeriveSharedSecretRequest_DeriveSharedSecretRequest) and self.KeyId == __o.KeyId and self.KeyAgreementAlgorithm == __o.KeyAgreementAlgorithm and self.PublicKey == __o.PublicKey and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun and self.Recipient == __o.Recipient
    def __hash__(self) -> int:
        return super().__hash__()


class DeriveSharedSecretResponse:
    @classmethod
    def default(cls, ):
        return lambda: DeriveSharedSecretResponse_DeriveSharedSecretResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeriveSharedSecretResponse(self) -> bool:
        return isinstance(self, DeriveSharedSecretResponse_DeriveSharedSecretResponse)

class DeriveSharedSecretResponse_DeriveSharedSecretResponse(DeriveSharedSecretResponse, NamedTuple('DeriveSharedSecretResponse', [('KeyId', Any), ('SharedSecret', Any), ('CiphertextForRecipient', Any), ('KeyAgreementAlgorithm', Any), ('KeyOrigin', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DeriveSharedSecretResponse.DeriveSharedSecretResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.SharedSecret)}, {_dafny.string_of(self.CiphertextForRecipient)}, {_dafny.string_of(self.KeyAgreementAlgorithm)}, {_dafny.string_of(self.KeyOrigin)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeriveSharedSecretResponse_DeriveSharedSecretResponse) and self.KeyId == __o.KeyId and self.SharedSecret == __o.SharedSecret and self.CiphertextForRecipient == __o.CiphertextForRecipient and self.KeyAgreementAlgorithm == __o.KeyAgreementAlgorithm and self.KeyOrigin == __o.KeyOrigin
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeCustomKeyStoresRequest:
    @classmethod
    def default(cls, ):
        return lambda: DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeCustomKeyStoresRequest(self) -> bool:
        return isinstance(self, DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest)

class DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest(DescribeCustomKeyStoresRequest, NamedTuple('DescribeCustomKeyStoresRequest', [('CustomKeyStoreId', Any), ('CustomKeyStoreName', Any), ('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DescribeCustomKeyStoresRequest.DescribeCustomKeyStoresRequest({_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.CustomKeyStoreName)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest) and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.CustomKeyStoreName == __o.CustomKeyStoreName and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeCustomKeyStoresResponse:
    @classmethod
    def default(cls, ):
        return lambda: DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeCustomKeyStoresResponse(self) -> bool:
        return isinstance(self, DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse)

class DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse(DescribeCustomKeyStoresResponse, NamedTuple('DescribeCustomKeyStoresResponse', [('CustomKeyStores', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DescribeCustomKeyStoresResponse.DescribeCustomKeyStoresResponse({_dafny.string_of(self.CustomKeyStores)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse) and self.CustomKeyStores == __o.CustomKeyStores and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: DescribeKeyRequest_DescribeKeyRequest(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeKeyRequest(self) -> bool:
        return isinstance(self, DescribeKeyRequest_DescribeKeyRequest)

class DescribeKeyRequest_DescribeKeyRequest(DescribeKeyRequest, NamedTuple('DescribeKeyRequest', [('KeyId', Any), ('GrantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DescribeKeyRequest.DescribeKeyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeKeyRequest_DescribeKeyRequest) and self.KeyId == __o.KeyId and self.GrantTokens == __o.GrantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class DescribeKeyResponse:
    @classmethod
    def default(cls, ):
        return lambda: DescribeKeyResponse_DescribeKeyResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DescribeKeyResponse(self) -> bool:
        return isinstance(self, DescribeKeyResponse_DescribeKeyResponse)

class DescribeKeyResponse_DescribeKeyResponse(DescribeKeyResponse, NamedTuple('DescribeKeyResponse', [('KeyMetadata', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DescribeKeyResponse.DescribeKeyResponse({_dafny.string_of(self.KeyMetadata)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DescribeKeyResponse_DescribeKeyResponse) and self.KeyMetadata == __o.KeyMetadata
    def __hash__(self) -> int:
        return super().__hash__()


class DescriptionType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_7_x_: _dafny.Seq = source__
        return default__.IsValid__DescriptionType(d_7_x_)

class DisableKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: DisableKeyRequest_DisableKeyRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisableKeyRequest(self) -> bool:
        return isinstance(self, DisableKeyRequest_DisableKeyRequest)

class DisableKeyRequest_DisableKeyRequest(DisableKeyRequest, NamedTuple('DisableKeyRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DisableKeyRequest.DisableKeyRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisableKeyRequest_DisableKeyRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class DisableKeyRotationRequest:
    @classmethod
    def default(cls, ):
        return lambda: DisableKeyRotationRequest_DisableKeyRotationRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisableKeyRotationRequest(self) -> bool:
        return isinstance(self, DisableKeyRotationRequest_DisableKeyRotationRequest)

class DisableKeyRotationRequest_DisableKeyRotationRequest(DisableKeyRotationRequest, NamedTuple('DisableKeyRotationRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DisableKeyRotationRequest.DisableKeyRotationRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisableKeyRotationRequest_DisableKeyRotationRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class DisconnectCustomKeyStoreRequest:
    @classmethod
    def default(cls, ):
        return lambda: DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisconnectCustomKeyStoreRequest(self) -> bool:
        return isinstance(self, DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest)

class DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest(DisconnectCustomKeyStoreRequest, NamedTuple('DisconnectCustomKeyStoreRequest', [('CustomKeyStoreId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DisconnectCustomKeyStoreRequest.DisconnectCustomKeyStoreRequest({_dafny.string_of(self.CustomKeyStoreId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest) and self.CustomKeyStoreId == __o.CustomKeyStoreId
    def __hash__(self) -> int:
        return super().__hash__()


class DisconnectCustomKeyStoreResponse:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse()]
    @classmethod
    def default(cls, ):
        return lambda: DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DisconnectCustomKeyStoreResponse(self) -> bool:
        return isinstance(self, DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse)

class DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse(DisconnectCustomKeyStoreResponse, NamedTuple('DisconnectCustomKeyStoreResponse', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.DisconnectCustomKeyStoreResponse.DisconnectCustomKeyStoreResponse'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse)
    def __hash__(self) -> int:
        return super().__hash__()


class EnableKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: EnableKeyRequest_EnableKeyRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EnableKeyRequest(self) -> bool:
        return isinstance(self, EnableKeyRequest_EnableKeyRequest)

class EnableKeyRequest_EnableKeyRequest(EnableKeyRequest, NamedTuple('EnableKeyRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EnableKeyRequest.EnableKeyRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EnableKeyRequest_EnableKeyRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class EnableKeyRotationRequest:
    @classmethod
    def default(cls, ):
        return lambda: EnableKeyRotationRequest_EnableKeyRotationRequest(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EnableKeyRotationRequest(self) -> bool:
        return isinstance(self, EnableKeyRotationRequest_EnableKeyRotationRequest)

class EnableKeyRotationRequest_EnableKeyRotationRequest(EnableKeyRotationRequest, NamedTuple('EnableKeyRotationRequest', [('KeyId', Any), ('RotationPeriodInDays', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EnableKeyRotationRequest.EnableKeyRotationRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.RotationPeriodInDays)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EnableKeyRotationRequest_EnableKeyRotationRequest) and self.KeyId == __o.KeyId and self.RotationPeriodInDays == __o.RotationPeriodInDays
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptionAlgorithmSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT(), EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256()]
    @classmethod
    def default(cls, ):
        return lambda: EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SYMMETRIC__DEFAULT(self) -> bool:
        return isinstance(self, EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT)
    @property
    def is_RSAES__OAEP__SHA__1(self) -> bool:
        return isinstance(self, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1)
    @property
    def is_RSAES__OAEP__SHA__256(self) -> bool:
        return isinstance(self, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256)

class EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT(EncryptionAlgorithmSpec, NamedTuple('SYMMETRIC__DEFAULT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(EncryptionAlgorithmSpec, NamedTuple('RSAES__OAEP__SHA__1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256(EncryptionAlgorithmSpec, NamedTuple('RSAES__OAEP__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptRequest:
    @classmethod
    def default(cls, ):
        return lambda: EncryptRequest_EncryptRequest(_dafny.Seq(""), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptRequest(self) -> bool:
        return isinstance(self, EncryptRequest_EncryptRequest)

class EncryptRequest_EncryptRequest(EncryptRequest, NamedTuple('EncryptRequest', [('KeyId', Any), ('Plaintext', Any), ('EncryptionContext', Any), ('GrantTokens', Any), ('EncryptionAlgorithm', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EncryptRequest.EncryptRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Plaintext)}, {_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.EncryptionAlgorithm)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptRequest_EncryptRequest) and self.KeyId == __o.KeyId and self.Plaintext == __o.Plaintext and self.EncryptionContext == __o.EncryptionContext and self.GrantTokens == __o.GrantTokens and self.EncryptionAlgorithm == __o.EncryptionAlgorithm and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptResponse:
    @classmethod
    def default(cls, ):
        return lambda: EncryptResponse_EncryptResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptResponse(self) -> bool:
        return isinstance(self, EncryptResponse_EncryptResponse)

class EncryptResponse_EncryptResponse(EncryptResponse, NamedTuple('EncryptResponse', [('CiphertextBlob', Any), ('KeyId', Any), ('EncryptionAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.EncryptResponse.EncryptResponse({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.EncryptionAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptResponse_EncryptResponse) and self.CiphertextBlob == __o.CiphertextBlob and self.KeyId == __o.KeyId and self.EncryptionAlgorithm == __o.EncryptionAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class ExpirationModelType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ExpirationModelType_KEY__MATERIAL__EXPIRES(), ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE()]
    @classmethod
    def default(cls, ):
        return lambda: ExpirationModelType_KEY__MATERIAL__EXPIRES()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KEY__MATERIAL__EXPIRES(self) -> bool:
        return isinstance(self, ExpirationModelType_KEY__MATERIAL__EXPIRES)
    @property
    def is_KEY__MATERIAL__DOES__NOT__EXPIRE(self) -> bool:
        return isinstance(self, ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE)

class ExpirationModelType_KEY__MATERIAL__EXPIRES(ExpirationModelType, NamedTuple('KEY__MATERIAL__EXPIRES', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ExpirationModelType.KEY_MATERIAL_EXPIRES'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExpirationModelType_KEY__MATERIAL__EXPIRES)
    def __hash__(self) -> int:
        return super().__hash__()

class ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE(ExpirationModelType, NamedTuple('KEY__MATERIAL__DOES__NOT__EXPIRE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ExpirationModelType.KEY_MATERIAL_DOES_NOT_EXPIRE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE)
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyPairRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyPairRequest_GenerateDataKeyPairRequest(Wrappers.Option.default()(), _dafny.Seq(""), DataKeyPairSpec.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyPairRequest(self) -> bool:
        return isinstance(self, GenerateDataKeyPairRequest_GenerateDataKeyPairRequest)

class GenerateDataKeyPairRequest_GenerateDataKeyPairRequest(GenerateDataKeyPairRequest, NamedTuple('GenerateDataKeyPairRequest', [('EncryptionContext', Any), ('KeyId', Any), ('KeyPairSpec', Any), ('GrantTokens', Any), ('Recipient', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyPairRequest.GenerateDataKeyPairRequest({_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyPairSpec)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.Recipient)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyPairRequest_GenerateDataKeyPairRequest) and self.EncryptionContext == __o.EncryptionContext and self.KeyId == __o.KeyId and self.KeyPairSpec == __o.KeyPairSpec and self.GrantTokens == __o.GrantTokens and self.Recipient == __o.Recipient and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyPairResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyPairResponse_GenerateDataKeyPairResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyPairResponse(self) -> bool:
        return isinstance(self, GenerateDataKeyPairResponse_GenerateDataKeyPairResponse)

class GenerateDataKeyPairResponse_GenerateDataKeyPairResponse(GenerateDataKeyPairResponse, NamedTuple('GenerateDataKeyPairResponse', [('PrivateKeyCiphertextBlob', Any), ('PrivateKeyPlaintext', Any), ('PublicKey', Any), ('KeyId', Any), ('KeyPairSpec', Any), ('CiphertextForRecipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyPairResponse.GenerateDataKeyPairResponse({_dafny.string_of(self.PrivateKeyCiphertextBlob)}, {_dafny.string_of(self.PrivateKeyPlaintext)}, {_dafny.string_of(self.PublicKey)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyPairSpec)}, {_dafny.string_of(self.CiphertextForRecipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyPairResponse_GenerateDataKeyPairResponse) and self.PrivateKeyCiphertextBlob == __o.PrivateKeyCiphertextBlob and self.PrivateKeyPlaintext == __o.PrivateKeyPlaintext and self.PublicKey == __o.PublicKey and self.KeyId == __o.KeyId and self.KeyPairSpec == __o.KeyPairSpec and self.CiphertextForRecipient == __o.CiphertextForRecipient
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyPairWithoutPlaintextRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest(Wrappers.Option.default()(), _dafny.Seq(""), DataKeyPairSpec.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyPairWithoutPlaintextRequest(self) -> bool:
        return isinstance(self, GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest)

class GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest(GenerateDataKeyPairWithoutPlaintextRequest, NamedTuple('GenerateDataKeyPairWithoutPlaintextRequest', [('EncryptionContext', Any), ('KeyId', Any), ('KeyPairSpec', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyPairWithoutPlaintextRequest.GenerateDataKeyPairWithoutPlaintextRequest({_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyPairSpec)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest) and self.EncryptionContext == __o.EncryptionContext and self.KeyId == __o.KeyId and self.KeyPairSpec == __o.KeyPairSpec and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyPairWithoutPlaintextResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyPairWithoutPlaintextResponse(self) -> bool:
        return isinstance(self, GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse)

class GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse(GenerateDataKeyPairWithoutPlaintextResponse, NamedTuple('GenerateDataKeyPairWithoutPlaintextResponse', [('PrivateKeyCiphertextBlob', Any), ('PublicKey', Any), ('KeyId', Any), ('KeyPairSpec', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyPairWithoutPlaintextResponse.GenerateDataKeyPairWithoutPlaintextResponse({_dafny.string_of(self.PrivateKeyCiphertextBlob)}, {_dafny.string_of(self.PublicKey)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyPairSpec)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse) and self.PrivateKeyCiphertextBlob == __o.PrivateKeyCiphertextBlob and self.PublicKey == __o.PublicKey and self.KeyId == __o.KeyId and self.KeyPairSpec == __o.KeyPairSpec
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyRequest_GenerateDataKeyRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyRequest(self) -> bool:
        return isinstance(self, GenerateDataKeyRequest_GenerateDataKeyRequest)

class GenerateDataKeyRequest_GenerateDataKeyRequest(GenerateDataKeyRequest, NamedTuple('GenerateDataKeyRequest', [('KeyId', Any), ('EncryptionContext', Any), ('NumberOfBytes', Any), ('KeySpec', Any), ('GrantTokens', Any), ('Recipient', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyRequest.GenerateDataKeyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.NumberOfBytes)}, {_dafny.string_of(self.KeySpec)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.Recipient)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyRequest_GenerateDataKeyRequest) and self.KeyId == __o.KeyId and self.EncryptionContext == __o.EncryptionContext and self.NumberOfBytes == __o.NumberOfBytes and self.KeySpec == __o.KeySpec and self.GrantTokens == __o.GrantTokens and self.Recipient == __o.Recipient and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyResponse_GenerateDataKeyResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyResponse(self) -> bool:
        return isinstance(self, GenerateDataKeyResponse_GenerateDataKeyResponse)

class GenerateDataKeyResponse_GenerateDataKeyResponse(GenerateDataKeyResponse, NamedTuple('GenerateDataKeyResponse', [('CiphertextBlob', Any), ('Plaintext', Any), ('KeyId', Any), ('CiphertextForRecipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyResponse.GenerateDataKeyResponse({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.Plaintext)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.CiphertextForRecipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyResponse_GenerateDataKeyResponse) and self.CiphertextBlob == __o.CiphertextBlob and self.Plaintext == __o.Plaintext and self.KeyId == __o.KeyId and self.CiphertextForRecipient == __o.CiphertextForRecipient
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyWithoutPlaintextRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyWithoutPlaintextRequest(self) -> bool:
        return isinstance(self, GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest)

class GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest(GenerateDataKeyWithoutPlaintextRequest, NamedTuple('GenerateDataKeyWithoutPlaintextRequest', [('KeyId', Any), ('EncryptionContext', Any), ('KeySpec', Any), ('NumberOfBytes', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextRequest.GenerateDataKeyWithoutPlaintextRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.EncryptionContext)}, {_dafny.string_of(self.KeySpec)}, {_dafny.string_of(self.NumberOfBytes)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest) and self.KeyId == __o.KeyId and self.EncryptionContext == __o.EncryptionContext and self.KeySpec == __o.KeySpec and self.NumberOfBytes == __o.NumberOfBytes and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateDataKeyWithoutPlaintextResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateDataKeyWithoutPlaintextResponse(self) -> bool:
        return isinstance(self, GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse)

class GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse(GenerateDataKeyWithoutPlaintextResponse, NamedTuple('GenerateDataKeyWithoutPlaintextResponse', [('CiphertextBlob', Any), ('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateDataKeyWithoutPlaintextResponse.GenerateDataKeyWithoutPlaintextResponse({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse) and self.CiphertextBlob == __o.CiphertextBlob and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateMacRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateMacRequest_GenerateMacRequest(_dafny.Seq({}), _dafny.Seq(""), MacAlgorithmSpec.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateMacRequest(self) -> bool:
        return isinstance(self, GenerateMacRequest_GenerateMacRequest)

class GenerateMacRequest_GenerateMacRequest(GenerateMacRequest, NamedTuple('GenerateMacRequest', [('Message', Any), ('KeyId', Any), ('MacAlgorithm', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateMacRequest.GenerateMacRequest({_dafny.string_of(self.Message)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.MacAlgorithm)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateMacRequest_GenerateMacRequest) and self.Message == __o.Message and self.KeyId == __o.KeyId and self.MacAlgorithm == __o.MacAlgorithm and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateMacResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateMacResponse_GenerateMacResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateMacResponse(self) -> bool:
        return isinstance(self, GenerateMacResponse_GenerateMacResponse)

class GenerateMacResponse_GenerateMacResponse(GenerateMacResponse, NamedTuple('GenerateMacResponse', [('Mac', Any), ('MacAlgorithm', Any), ('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateMacResponse.GenerateMacResponse({_dafny.string_of(self.Mac)}, {_dafny.string_of(self.MacAlgorithm)}, {_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateMacResponse_GenerateMacResponse) and self.Mac == __o.Mac and self.MacAlgorithm == __o.MacAlgorithm and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateRandomRequest:
    @classmethod
    def default(cls, ):
        return lambda: GenerateRandomRequest_GenerateRandomRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateRandomRequest(self) -> bool:
        return isinstance(self, GenerateRandomRequest_GenerateRandomRequest)

class GenerateRandomRequest_GenerateRandomRequest(GenerateRandomRequest, NamedTuple('GenerateRandomRequest', [('NumberOfBytes', Any), ('CustomKeyStoreId', Any), ('Recipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateRandomRequest.GenerateRandomRequest({_dafny.string_of(self.NumberOfBytes)}, {_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.Recipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateRandomRequest_GenerateRandomRequest) and self.NumberOfBytes == __o.NumberOfBytes and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.Recipient == __o.Recipient
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateRandomResponse:
    @classmethod
    def default(cls, ):
        return lambda: GenerateRandomResponse_GenerateRandomResponse(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateRandomResponse(self) -> bool:
        return isinstance(self, GenerateRandomResponse_GenerateRandomResponse)

class GenerateRandomResponse_GenerateRandomResponse(GenerateRandomResponse, NamedTuple('GenerateRandomResponse', [('Plaintext', Any), ('CiphertextForRecipient', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GenerateRandomResponse.GenerateRandomResponse({_dafny.string_of(self.Plaintext)}, {_dafny.string_of(self.CiphertextForRecipient)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateRandomResponse_GenerateRandomResponse) and self.Plaintext == __o.Plaintext and self.CiphertextForRecipient == __o.CiphertextForRecipient
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyPolicyRequest:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyPolicyRequest_GetKeyPolicyRequest(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyPolicyRequest(self) -> bool:
        return isinstance(self, GetKeyPolicyRequest_GetKeyPolicyRequest)

class GetKeyPolicyRequest_GetKeyPolicyRequest(GetKeyPolicyRequest, NamedTuple('GetKeyPolicyRequest', [('KeyId', Any), ('PolicyName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetKeyPolicyRequest.GetKeyPolicyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.PolicyName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyPolicyRequest_GetKeyPolicyRequest) and self.KeyId == __o.KeyId and self.PolicyName == __o.PolicyName
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyPolicyResponse:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyPolicyResponse_GetKeyPolicyResponse(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyPolicyResponse(self) -> bool:
        return isinstance(self, GetKeyPolicyResponse_GetKeyPolicyResponse)

class GetKeyPolicyResponse_GetKeyPolicyResponse(GetKeyPolicyResponse, NamedTuple('GetKeyPolicyResponse', [('Policy', Any), ('PolicyName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetKeyPolicyResponse.GetKeyPolicyResponse({_dafny.string_of(self.Policy)}, {_dafny.string_of(self.PolicyName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyPolicyResponse_GetKeyPolicyResponse) and self.Policy == __o.Policy and self.PolicyName == __o.PolicyName
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyRotationStatusRequest:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyRotationStatusRequest_GetKeyRotationStatusRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyRotationStatusRequest(self) -> bool:
        return isinstance(self, GetKeyRotationStatusRequest_GetKeyRotationStatusRequest)

class GetKeyRotationStatusRequest_GetKeyRotationStatusRequest(GetKeyRotationStatusRequest, NamedTuple('GetKeyRotationStatusRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetKeyRotationStatusRequest.GetKeyRotationStatusRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyRotationStatusRequest_GetKeyRotationStatusRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class GetKeyRotationStatusResponse:
    @classmethod
    def default(cls, ):
        return lambda: GetKeyRotationStatusResponse_GetKeyRotationStatusResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetKeyRotationStatusResponse(self) -> bool:
        return isinstance(self, GetKeyRotationStatusResponse_GetKeyRotationStatusResponse)

class GetKeyRotationStatusResponse_GetKeyRotationStatusResponse(GetKeyRotationStatusResponse, NamedTuple('GetKeyRotationStatusResponse', [('KeyRotationEnabled', Any), ('KeyId', Any), ('RotationPeriodInDays', Any), ('NextRotationDate', Any), ('OnDemandRotationStartDate', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetKeyRotationStatusResponse.GetKeyRotationStatusResponse({_dafny.string_of(self.KeyRotationEnabled)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.RotationPeriodInDays)}, {_dafny.string_of(self.NextRotationDate)}, {_dafny.string_of(self.OnDemandRotationStartDate)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetKeyRotationStatusResponse_GetKeyRotationStatusResponse) and self.KeyRotationEnabled == __o.KeyRotationEnabled and self.KeyId == __o.KeyId and self.RotationPeriodInDays == __o.RotationPeriodInDays and self.NextRotationDate == __o.NextRotationDate and self.OnDemandRotationStartDate == __o.OnDemandRotationStartDate
    def __hash__(self) -> int:
        return super().__hash__()


class GetParametersForImportRequest:
    @classmethod
    def default(cls, ):
        return lambda: GetParametersForImportRequest_GetParametersForImportRequest(_dafny.Seq(""), AlgorithmSpec.default()(), WrappingKeySpec.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetParametersForImportRequest(self) -> bool:
        return isinstance(self, GetParametersForImportRequest_GetParametersForImportRequest)

class GetParametersForImportRequest_GetParametersForImportRequest(GetParametersForImportRequest, NamedTuple('GetParametersForImportRequest', [('KeyId', Any), ('WrappingAlgorithm', Any), ('WrappingKeySpec', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetParametersForImportRequest.GetParametersForImportRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.WrappingAlgorithm)}, {_dafny.string_of(self.WrappingKeySpec)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetParametersForImportRequest_GetParametersForImportRequest) and self.KeyId == __o.KeyId and self.WrappingAlgorithm == __o.WrappingAlgorithm and self.WrappingKeySpec == __o.WrappingKeySpec
    def __hash__(self) -> int:
        return super().__hash__()


class GetParametersForImportResponse:
    @classmethod
    def default(cls, ):
        return lambda: GetParametersForImportResponse_GetParametersForImportResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetParametersForImportResponse(self) -> bool:
        return isinstance(self, GetParametersForImportResponse_GetParametersForImportResponse)

class GetParametersForImportResponse_GetParametersForImportResponse(GetParametersForImportResponse, NamedTuple('GetParametersForImportResponse', [('KeyId', Any), ('ImportToken', Any), ('PublicKey', Any), ('ParametersValidTo', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetParametersForImportResponse.GetParametersForImportResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.ImportToken)}, {_dafny.string_of(self.PublicKey)}, {_dafny.string_of(self.ParametersValidTo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetParametersForImportResponse_GetParametersForImportResponse) and self.KeyId == __o.KeyId and self.ImportToken == __o.ImportToken and self.PublicKey == __o.PublicKey and self.ParametersValidTo == __o.ParametersValidTo
    def __hash__(self) -> int:
        return super().__hash__()


class GetPublicKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: GetPublicKeyRequest_GetPublicKeyRequest(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetPublicKeyRequest(self) -> bool:
        return isinstance(self, GetPublicKeyRequest_GetPublicKeyRequest)

class GetPublicKeyRequest_GetPublicKeyRequest(GetPublicKeyRequest, NamedTuple('GetPublicKeyRequest', [('KeyId', Any), ('GrantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetPublicKeyRequest.GetPublicKeyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetPublicKeyRequest_GetPublicKeyRequest) and self.KeyId == __o.KeyId and self.GrantTokens == __o.GrantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class GetPublicKeyResponse:
    @classmethod
    def default(cls, ):
        return lambda: GetPublicKeyResponse_GetPublicKeyResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetPublicKeyResponse(self) -> bool:
        return isinstance(self, GetPublicKeyResponse_GetPublicKeyResponse)

class GetPublicKeyResponse_GetPublicKeyResponse(GetPublicKeyResponse, NamedTuple('GetPublicKeyResponse', [('KeyId', Any), ('PublicKey', Any), ('CustomerMasterKeySpec', Any), ('KeySpec', Any), ('KeyUsage', Any), ('EncryptionAlgorithms', Any), ('SigningAlgorithms', Any), ('KeyAgreementAlgorithms', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GetPublicKeyResponse.GetPublicKeyResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.PublicKey)}, {_dafny.string_of(self.CustomerMasterKeySpec)}, {_dafny.string_of(self.KeySpec)}, {_dafny.string_of(self.KeyUsage)}, {_dafny.string_of(self.EncryptionAlgorithms)}, {_dafny.string_of(self.SigningAlgorithms)}, {_dafny.string_of(self.KeyAgreementAlgorithms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GetPublicKeyResponse_GetPublicKeyResponse) and self.KeyId == __o.KeyId and self.PublicKey == __o.PublicKey and self.CustomerMasterKeySpec == __o.CustomerMasterKeySpec and self.KeySpec == __o.KeySpec and self.KeyUsage == __o.KeyUsage and self.EncryptionAlgorithms == __o.EncryptionAlgorithms and self.SigningAlgorithms == __o.SigningAlgorithms and self.KeyAgreementAlgorithms == __o.KeyAgreementAlgorithms
    def __hash__(self) -> int:
        return super().__hash__()


class GrantConstraints:
    @classmethod
    def default(cls, ):
        return lambda: GrantConstraints_GrantConstraints(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GrantConstraints(self) -> bool:
        return isinstance(self, GrantConstraints_GrantConstraints)

class GrantConstraints_GrantConstraints(GrantConstraints, NamedTuple('GrantConstraints', [('EncryptionContextSubset', Any), ('EncryptionContextEquals', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantConstraints.GrantConstraints({_dafny.string_of(self.EncryptionContextSubset)}, {_dafny.string_of(self.EncryptionContextEquals)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantConstraints_GrantConstraints) and self.EncryptionContextSubset == __o.EncryptionContextSubset and self.EncryptionContextEquals == __o.EncryptionContextEquals
    def __hash__(self) -> int:
        return super().__hash__()


class GrantIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_8_x_: _dafny.Seq = source__
        return default__.IsValid__GrantIdType(d_8_x_)

class GrantListEntry:
    @classmethod
    def default(cls, ):
        return lambda: GrantListEntry_GrantListEntry(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GrantListEntry(self) -> bool:
        return isinstance(self, GrantListEntry_GrantListEntry)

class GrantListEntry_GrantListEntry(GrantListEntry, NamedTuple('GrantListEntry', [('KeyId', Any), ('GrantId', Any), ('Name', Any), ('CreationDate', Any), ('GranteePrincipal', Any), ('RetiringPrincipal', Any), ('IssuingAccount', Any), ('Operations', Any), ('Constraints', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantListEntry.GrantListEntry({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantId)}, {_dafny.string_of(self.Name)}, {_dafny.string_of(self.CreationDate)}, {_dafny.string_of(self.GranteePrincipal)}, {_dafny.string_of(self.RetiringPrincipal)}, {_dafny.string_of(self.IssuingAccount)}, {_dafny.string_of(self.Operations)}, {_dafny.string_of(self.Constraints)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantListEntry_GrantListEntry) and self.KeyId == __o.KeyId and self.GrantId == __o.GrantId and self.Name == __o.Name and self.CreationDate == __o.CreationDate and self.GranteePrincipal == __o.GranteePrincipal and self.RetiringPrincipal == __o.RetiringPrincipal and self.IssuingAccount == __o.IssuingAccount and self.Operations == __o.Operations and self.Constraints == __o.Constraints
    def __hash__(self) -> int:
        return super().__hash__()


class GrantNameType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_9_x_: _dafny.Seq = source__
        return default__.IsValid__GrantNameType(d_9_x_)

class GrantOperation:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [GrantOperation_Decrypt(), GrantOperation_Encrypt(), GrantOperation_GenerateDataKey(), GrantOperation_GenerateDataKeyWithoutPlaintext(), GrantOperation_ReEncryptFrom(), GrantOperation_ReEncryptTo(), GrantOperation_Sign(), GrantOperation_Verify(), GrantOperation_GetPublicKey(), GrantOperation_CreateGrant(), GrantOperation_RetireGrant(), GrantOperation_DescribeKey(), GrantOperation_GenerateDataKeyPair(), GrantOperation_GenerateDataKeyPairWithoutPlaintext(), GrantOperation_GenerateMac(), GrantOperation_VerifyMac(), GrantOperation_DeriveSharedSecret()]
    @classmethod
    def default(cls, ):
        return lambda: GrantOperation_Decrypt()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Decrypt(self) -> bool:
        return isinstance(self, GrantOperation_Decrypt)
    @property
    def is_Encrypt(self) -> bool:
        return isinstance(self, GrantOperation_Encrypt)
    @property
    def is_GenerateDataKey(self) -> bool:
        return isinstance(self, GrantOperation_GenerateDataKey)
    @property
    def is_GenerateDataKeyWithoutPlaintext(self) -> bool:
        return isinstance(self, GrantOperation_GenerateDataKeyWithoutPlaintext)
    @property
    def is_ReEncryptFrom(self) -> bool:
        return isinstance(self, GrantOperation_ReEncryptFrom)
    @property
    def is_ReEncryptTo(self) -> bool:
        return isinstance(self, GrantOperation_ReEncryptTo)
    @property
    def is_Sign(self) -> bool:
        return isinstance(self, GrantOperation_Sign)
    @property
    def is_Verify(self) -> bool:
        return isinstance(self, GrantOperation_Verify)
    @property
    def is_GetPublicKey(self) -> bool:
        return isinstance(self, GrantOperation_GetPublicKey)
    @property
    def is_CreateGrant(self) -> bool:
        return isinstance(self, GrantOperation_CreateGrant)
    @property
    def is_RetireGrant(self) -> bool:
        return isinstance(self, GrantOperation_RetireGrant)
    @property
    def is_DescribeKey(self) -> bool:
        return isinstance(self, GrantOperation_DescribeKey)
    @property
    def is_GenerateDataKeyPair(self) -> bool:
        return isinstance(self, GrantOperation_GenerateDataKeyPair)
    @property
    def is_GenerateDataKeyPairWithoutPlaintext(self) -> bool:
        return isinstance(self, GrantOperation_GenerateDataKeyPairWithoutPlaintext)
    @property
    def is_GenerateMac(self) -> bool:
        return isinstance(self, GrantOperation_GenerateMac)
    @property
    def is_VerifyMac(self) -> bool:
        return isinstance(self, GrantOperation_VerifyMac)
    @property
    def is_DeriveSharedSecret(self) -> bool:
        return isinstance(self, GrantOperation_DeriveSharedSecret)

class GrantOperation_Decrypt(GrantOperation, NamedTuple('Decrypt', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.Decrypt'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_Decrypt)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_Encrypt(GrantOperation, NamedTuple('Encrypt', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.Encrypt'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_Encrypt)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GenerateDataKey(GrantOperation, NamedTuple('GenerateDataKey', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GenerateDataKey'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GenerateDataKey)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GenerateDataKeyWithoutPlaintext(GrantOperation, NamedTuple('GenerateDataKeyWithoutPlaintext', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GenerateDataKeyWithoutPlaintext'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GenerateDataKeyWithoutPlaintext)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_ReEncryptFrom(GrantOperation, NamedTuple('ReEncryptFrom', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.ReEncryptFrom'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_ReEncryptFrom)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_ReEncryptTo(GrantOperation, NamedTuple('ReEncryptTo', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.ReEncryptTo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_ReEncryptTo)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_Sign(GrantOperation, NamedTuple('Sign', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.Sign'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_Sign)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_Verify(GrantOperation, NamedTuple('Verify', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.Verify'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_Verify)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GetPublicKey(GrantOperation, NamedTuple('GetPublicKey', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GetPublicKey'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GetPublicKey)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_CreateGrant(GrantOperation, NamedTuple('CreateGrant', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.CreateGrant'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_CreateGrant)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_RetireGrant(GrantOperation, NamedTuple('RetireGrant', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.RetireGrant'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_RetireGrant)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_DescribeKey(GrantOperation, NamedTuple('DescribeKey', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.DescribeKey'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_DescribeKey)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GenerateDataKeyPair(GrantOperation, NamedTuple('GenerateDataKeyPair', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GenerateDataKeyPair'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GenerateDataKeyPair)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GenerateDataKeyPairWithoutPlaintext(GrantOperation, NamedTuple('GenerateDataKeyPairWithoutPlaintext', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GenerateDataKeyPairWithoutPlaintext'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GenerateDataKeyPairWithoutPlaintext)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_GenerateMac(GrantOperation, NamedTuple('GenerateMac', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.GenerateMac'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_GenerateMac)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_VerifyMac(GrantOperation, NamedTuple('VerifyMac', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.VerifyMac'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_VerifyMac)
    def __hash__(self) -> int:
        return super().__hash__()

class GrantOperation_DeriveSharedSecret(GrantOperation, NamedTuple('DeriveSharedSecret', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.GrantOperation.DeriveSharedSecret'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GrantOperation_DeriveSharedSecret)
    def __hash__(self) -> int:
        return super().__hash__()


class GrantTokenList:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_10_x_: _dafny.Seq = source__
        return default__.IsValid__GrantTokenList(d_10_x_)

class GrantTokenType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_11_x_: _dafny.Seq = source__
        return default__.IsValid__GrantTokenType(d_11_x_)

class ImportKeyMaterialRequest:
    @classmethod
    def default(cls, ):
        return lambda: ImportKeyMaterialRequest_ImportKeyMaterialRequest(_dafny.Seq(""), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportKeyMaterialRequest(self) -> bool:
        return isinstance(self, ImportKeyMaterialRequest_ImportKeyMaterialRequest)

class ImportKeyMaterialRequest_ImportKeyMaterialRequest(ImportKeyMaterialRequest, NamedTuple('ImportKeyMaterialRequest', [('KeyId', Any), ('ImportToken', Any), ('EncryptedKeyMaterial', Any), ('ValidTo', Any), ('ExpirationModel', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ImportKeyMaterialRequest.ImportKeyMaterialRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.ImportToken)}, {_dafny.string_of(self.EncryptedKeyMaterial)}, {_dafny.string_of(self.ValidTo)}, {_dafny.string_of(self.ExpirationModel)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportKeyMaterialRequest_ImportKeyMaterialRequest) and self.KeyId == __o.KeyId and self.ImportToken == __o.ImportToken and self.EncryptedKeyMaterial == __o.EncryptedKeyMaterial and self.ValidTo == __o.ValidTo and self.ExpirationModel == __o.ExpirationModel
    def __hash__(self) -> int:
        return super().__hash__()


class ImportKeyMaterialResponse:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ImportKeyMaterialResponse_ImportKeyMaterialResponse()]
    @classmethod
    def default(cls, ):
        return lambda: ImportKeyMaterialResponse_ImportKeyMaterialResponse()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ImportKeyMaterialResponse(self) -> bool:
        return isinstance(self, ImportKeyMaterialResponse_ImportKeyMaterialResponse)

class ImportKeyMaterialResponse_ImportKeyMaterialResponse(ImportKeyMaterialResponse, NamedTuple('ImportKeyMaterialResponse', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ImportKeyMaterialResponse.ImportKeyMaterialResponse'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ImportKeyMaterialResponse_ImportKeyMaterialResponse)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyAgreementAlgorithmSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyAgreementAlgorithmSpec_ECDH()]
    @classmethod
    def default(cls, ):
        return lambda: KeyAgreementAlgorithmSpec_ECDH()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDH(self) -> bool:
        return isinstance(self, KeyAgreementAlgorithmSpec_ECDH)

class KeyAgreementAlgorithmSpec_ECDH(KeyAgreementAlgorithmSpec, NamedTuple('ECDH', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec.ECDH'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyAgreementAlgorithmSpec_ECDH)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyEncryptionMechanism:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyEncryptionMechanism_RSAES__OAEP__SHA__256()]
    @classmethod
    def default(cls, ):
        return lambda: KeyEncryptionMechanism_RSAES__OAEP__SHA__256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSAES__OAEP__SHA__256(self) -> bool:
        return isinstance(self, KeyEncryptionMechanism_RSAES__OAEP__SHA__256)

class KeyEncryptionMechanism_RSAES__OAEP__SHA__256(KeyEncryptionMechanism, NamedTuple('RSAES__OAEP__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyEncryptionMechanism.RSAES_OAEP_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyEncryptionMechanism_RSAES__OAEP__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_12_x_: _dafny.Seq = source__
        return default__.IsValid__KeyIdType(d_12_x_)

class KeyListEntry:
    @classmethod
    def default(cls, ):
        return lambda: KeyListEntry_KeyListEntry(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyListEntry(self) -> bool:
        return isinstance(self, KeyListEntry_KeyListEntry)

class KeyListEntry_KeyListEntry(KeyListEntry, NamedTuple('KeyListEntry', [('KeyId', Any), ('KeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyListEntry.KeyListEntry({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.KeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyListEntry_KeyListEntry) and self.KeyId == __o.KeyId and self.KeyArn == __o.KeyArn
    def __hash__(self) -> int:
        return super().__hash__()


class KeyManagerType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyManagerType_AWS(), KeyManagerType_CUSTOMER()]
    @classmethod
    def default(cls, ):
        return lambda: KeyManagerType_AWS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AWS(self) -> bool:
        return isinstance(self, KeyManagerType_AWS)
    @property
    def is_CUSTOMER(self) -> bool:
        return isinstance(self, KeyManagerType_CUSTOMER)

class KeyManagerType_AWS(KeyManagerType, NamedTuple('AWS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyManagerType.AWS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyManagerType_AWS)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyManagerType_CUSTOMER(KeyManagerType, NamedTuple('CUSTOMER', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyManagerType.CUSTOMER'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyManagerType_CUSTOMER)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyMetadata:
    @classmethod
    def default(cls, ):
        return lambda: KeyMetadata_KeyMetadata(Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyMetadata(self) -> bool:
        return isinstance(self, KeyMetadata_KeyMetadata)

class KeyMetadata_KeyMetadata(KeyMetadata, NamedTuple('KeyMetadata', [('AWSAccountId', Any), ('KeyId', Any), ('Arn', Any), ('CreationDate', Any), ('Enabled', Any), ('Description', Any), ('KeyUsage', Any), ('KeyState', Any), ('DeletionDate', Any), ('ValidTo', Any), ('Origin', Any), ('CustomKeyStoreId', Any), ('CloudHsmClusterId', Any), ('ExpirationModel', Any), ('KeyManager', Any), ('CustomerMasterKeySpec', Any), ('KeySpec', Any), ('EncryptionAlgorithms', Any), ('SigningAlgorithms', Any), ('KeyAgreementAlgorithms', Any), ('MultiRegion', Any), ('MultiRegionConfiguration', Any), ('PendingDeletionWindowInDays', Any), ('MacAlgorithms', Any), ('XksKeyConfiguration', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyMetadata.KeyMetadata({_dafny.string_of(self.AWSAccountId)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Arn)}, {_dafny.string_of(self.CreationDate)}, {_dafny.string_of(self.Enabled)}, {_dafny.string_of(self.Description)}, {_dafny.string_of(self.KeyUsage)}, {_dafny.string_of(self.KeyState)}, {_dafny.string_of(self.DeletionDate)}, {_dafny.string_of(self.ValidTo)}, {_dafny.string_of(self.Origin)}, {_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.CloudHsmClusterId)}, {_dafny.string_of(self.ExpirationModel)}, {_dafny.string_of(self.KeyManager)}, {_dafny.string_of(self.CustomerMasterKeySpec)}, {_dafny.string_of(self.KeySpec)}, {_dafny.string_of(self.EncryptionAlgorithms)}, {_dafny.string_of(self.SigningAlgorithms)}, {_dafny.string_of(self.KeyAgreementAlgorithms)}, {_dafny.string_of(self.MultiRegion)}, {_dafny.string_of(self.MultiRegionConfiguration)}, {_dafny.string_of(self.PendingDeletionWindowInDays)}, {_dafny.string_of(self.MacAlgorithms)}, {_dafny.string_of(self.XksKeyConfiguration)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMetadata_KeyMetadata) and self.AWSAccountId == __o.AWSAccountId and self.KeyId == __o.KeyId and self.Arn == __o.Arn and self.CreationDate == __o.CreationDate and self.Enabled == __o.Enabled and self.Description == __o.Description and self.KeyUsage == __o.KeyUsage and self.KeyState == __o.KeyState and self.DeletionDate == __o.DeletionDate and self.ValidTo == __o.ValidTo and self.Origin == __o.Origin and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.CloudHsmClusterId == __o.CloudHsmClusterId and self.ExpirationModel == __o.ExpirationModel and self.KeyManager == __o.KeyManager and self.CustomerMasterKeySpec == __o.CustomerMasterKeySpec and self.KeySpec == __o.KeySpec and self.EncryptionAlgorithms == __o.EncryptionAlgorithms and self.SigningAlgorithms == __o.SigningAlgorithms and self.KeyAgreementAlgorithms == __o.KeyAgreementAlgorithms and self.MultiRegion == __o.MultiRegion and self.MultiRegionConfiguration == __o.MultiRegionConfiguration and self.PendingDeletionWindowInDays == __o.PendingDeletionWindowInDays and self.MacAlgorithms == __o.MacAlgorithms and self.XksKeyConfiguration == __o.XksKeyConfiguration
    def __hash__(self) -> int:
        return super().__hash__()


class KeySpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeySpec_RSA__2048(), KeySpec_RSA__3072(), KeySpec_RSA__4096(), KeySpec_ECC__NIST__P256(), KeySpec_ECC__NIST__P384(), KeySpec_ECC__NIST__P521(), KeySpec_ECC__SECG__P256K1(), KeySpec_SYMMETRIC__DEFAULT(), KeySpec_HMAC__224(), KeySpec_HMAC__256(), KeySpec_HMAC__384(), KeySpec_HMAC__512(), KeySpec_SM2()]
    @classmethod
    def default(cls, ):
        return lambda: KeySpec_RSA__2048()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSA__2048(self) -> bool:
        return isinstance(self, KeySpec_RSA__2048)
    @property
    def is_RSA__3072(self) -> bool:
        return isinstance(self, KeySpec_RSA__3072)
    @property
    def is_RSA__4096(self) -> bool:
        return isinstance(self, KeySpec_RSA__4096)
    @property
    def is_ECC__NIST__P256(self) -> bool:
        return isinstance(self, KeySpec_ECC__NIST__P256)
    @property
    def is_ECC__NIST__P384(self) -> bool:
        return isinstance(self, KeySpec_ECC__NIST__P384)
    @property
    def is_ECC__NIST__P521(self) -> bool:
        return isinstance(self, KeySpec_ECC__NIST__P521)
    @property
    def is_ECC__SECG__P256K1(self) -> bool:
        return isinstance(self, KeySpec_ECC__SECG__P256K1)
    @property
    def is_SYMMETRIC__DEFAULT(self) -> bool:
        return isinstance(self, KeySpec_SYMMETRIC__DEFAULT)
    @property
    def is_HMAC__224(self) -> bool:
        return isinstance(self, KeySpec_HMAC__224)
    @property
    def is_HMAC__256(self) -> bool:
        return isinstance(self, KeySpec_HMAC__256)
    @property
    def is_HMAC__384(self) -> bool:
        return isinstance(self, KeySpec_HMAC__384)
    @property
    def is_HMAC__512(self) -> bool:
        return isinstance(self, KeySpec_HMAC__512)
    @property
    def is_SM2(self) -> bool:
        return isinstance(self, KeySpec_SM2)

class KeySpec_RSA__2048(KeySpec, NamedTuple('RSA__2048', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.RSA_2048'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_RSA__2048)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_RSA__3072(KeySpec, NamedTuple('RSA__3072', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.RSA_3072'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_RSA__3072)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_RSA__4096(KeySpec, NamedTuple('RSA__4096', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.RSA_4096'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_RSA__4096)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_ECC__NIST__P256(KeySpec, NamedTuple('ECC__NIST__P256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.ECC_NIST_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_ECC__NIST__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_ECC__NIST__P384(KeySpec, NamedTuple('ECC__NIST__P384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.ECC_NIST_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_ECC__NIST__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_ECC__NIST__P521(KeySpec, NamedTuple('ECC__NIST__P521', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.ECC_NIST_P521'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_ECC__NIST__P521)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_ECC__SECG__P256K1(KeySpec, NamedTuple('ECC__SECG__P256K1', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.ECC_SECG_P256K1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_ECC__SECG__P256K1)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_SYMMETRIC__DEFAULT(KeySpec, NamedTuple('SYMMETRIC__DEFAULT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.SYMMETRIC_DEFAULT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_SYMMETRIC__DEFAULT)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_HMAC__224(KeySpec, NamedTuple('HMAC__224', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.HMAC_224'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_HMAC__224)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_HMAC__256(KeySpec, NamedTuple('HMAC__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.HMAC_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_HMAC__256)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_HMAC__384(KeySpec, NamedTuple('HMAC__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.HMAC_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_HMAC__384)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_HMAC__512(KeySpec, NamedTuple('HMAC__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.HMAC_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_HMAC__512)
    def __hash__(self) -> int:
        return super().__hash__()

class KeySpec_SM2(KeySpec, NamedTuple('SM2', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeySpec.SM2'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeySpec_SM2)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyState:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyState_Creating(), KeyState_Enabled(), KeyState_Disabled(), KeyState_PendingDeletion(), KeyState_PendingImport(), KeyState_PendingReplicaDeletion(), KeyState_Unavailable(), KeyState_Updating()]
    @classmethod
    def default(cls, ):
        return lambda: KeyState_Creating()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Creating(self) -> bool:
        return isinstance(self, KeyState_Creating)
    @property
    def is_Enabled(self) -> bool:
        return isinstance(self, KeyState_Enabled)
    @property
    def is_Disabled(self) -> bool:
        return isinstance(self, KeyState_Disabled)
    @property
    def is_PendingDeletion(self) -> bool:
        return isinstance(self, KeyState_PendingDeletion)
    @property
    def is_PendingImport(self) -> bool:
        return isinstance(self, KeyState_PendingImport)
    @property
    def is_PendingReplicaDeletion(self) -> bool:
        return isinstance(self, KeyState_PendingReplicaDeletion)
    @property
    def is_Unavailable(self) -> bool:
        return isinstance(self, KeyState_Unavailable)
    @property
    def is_Updating(self) -> bool:
        return isinstance(self, KeyState_Updating)

class KeyState_Creating(KeyState, NamedTuple('Creating', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.Creating'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_Creating)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_Enabled(KeyState, NamedTuple('Enabled', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.Enabled'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_Enabled)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_Disabled(KeyState, NamedTuple('Disabled', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.Disabled'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_Disabled)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_PendingDeletion(KeyState, NamedTuple('PendingDeletion', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.PendingDeletion'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_PendingDeletion)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_PendingImport(KeyState, NamedTuple('PendingImport', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.PendingImport'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_PendingImport)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_PendingReplicaDeletion(KeyState, NamedTuple('PendingReplicaDeletion', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.PendingReplicaDeletion'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_PendingReplicaDeletion)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_Unavailable(KeyState, NamedTuple('Unavailable', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.Unavailable'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_Unavailable)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyState_Updating(KeyState, NamedTuple('Updating', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyState.Updating'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyState_Updating)
    def __hash__(self) -> int:
        return super().__hash__()


class KeyStorePasswordType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_13_x_: _dafny.Seq = source__
        return default__.IsValid__KeyStorePasswordType(d_13_x_)

class KeyUsageType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KeyUsageType_SIGN__VERIFY(), KeyUsageType_ENCRYPT__DECRYPT(), KeyUsageType_GENERATE__VERIFY__MAC(), KeyUsageType_KEY__AGREEMENT()]
    @classmethod
    def default(cls, ):
        return lambda: KeyUsageType_SIGN__VERIFY()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SIGN__VERIFY(self) -> bool:
        return isinstance(self, KeyUsageType_SIGN__VERIFY)
    @property
    def is_ENCRYPT__DECRYPT(self) -> bool:
        return isinstance(self, KeyUsageType_ENCRYPT__DECRYPT)
    @property
    def is_GENERATE__VERIFY__MAC(self) -> bool:
        return isinstance(self, KeyUsageType_GENERATE__VERIFY__MAC)
    @property
    def is_KEY__AGREEMENT(self) -> bool:
        return isinstance(self, KeyUsageType_KEY__AGREEMENT)

class KeyUsageType_SIGN__VERIFY(KeyUsageType, NamedTuple('SIGN__VERIFY', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyUsageType.SIGN_VERIFY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyUsageType_SIGN__VERIFY)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyUsageType_ENCRYPT__DECRYPT(KeyUsageType, NamedTuple('ENCRYPT__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyUsageType.ENCRYPT_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyUsageType_ENCRYPT__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyUsageType_GENERATE__VERIFY__MAC(KeyUsageType, NamedTuple('GENERATE__VERIFY__MAC', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyUsageType.GENERATE_VERIFY_MAC'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyUsageType_GENERATE__VERIFY__MAC)
    def __hash__(self) -> int:
        return super().__hash__()

class KeyUsageType_KEY__AGREEMENT(KeyUsageType, NamedTuple('KEY__AGREEMENT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.KeyUsageType.KEY_AGREEMENT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyUsageType_KEY__AGREEMENT)
    def __hash__(self) -> int:
        return super().__hash__()


class LimitType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_14_x_: int = source__
        if True:
            return default__.IsValid__LimitType(d_14_x_)
        return False

class ListAliasesRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListAliasesRequest_ListAliasesRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListAliasesRequest(self) -> bool:
        return isinstance(self, ListAliasesRequest_ListAliasesRequest)

class ListAliasesRequest_ListAliasesRequest(ListAliasesRequest, NamedTuple('ListAliasesRequest', [('KeyId', Any), ('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListAliasesRequest.ListAliasesRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListAliasesRequest_ListAliasesRequest) and self.KeyId == __o.KeyId and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class ListAliasesResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListAliasesResponse_ListAliasesResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListAliasesResponse(self) -> bool:
        return isinstance(self, ListAliasesResponse_ListAliasesResponse)

class ListAliasesResponse_ListAliasesResponse(ListAliasesResponse, NamedTuple('ListAliasesResponse', [('Aliases', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListAliasesResponse.ListAliasesResponse({_dafny.string_of(self.Aliases)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListAliasesResponse_ListAliasesResponse) and self.Aliases == __o.Aliases and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class ListGrantsRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListGrantsRequest_ListGrantsRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListGrantsRequest(self) -> bool:
        return isinstance(self, ListGrantsRequest_ListGrantsRequest)

class ListGrantsRequest_ListGrantsRequest(ListGrantsRequest, NamedTuple('ListGrantsRequest', [('Limit', Any), ('Marker', Any), ('KeyId', Any), ('GrantId', Any), ('GranteePrincipal', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListGrantsRequest.ListGrantsRequest({_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantId)}, {_dafny.string_of(self.GranteePrincipal)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListGrantsRequest_ListGrantsRequest) and self.Limit == __o.Limit and self.Marker == __o.Marker and self.KeyId == __o.KeyId and self.GrantId == __o.GrantId and self.GranteePrincipal == __o.GranteePrincipal
    def __hash__(self) -> int:
        return super().__hash__()


class ListGrantsResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListGrantsResponse_ListGrantsResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListGrantsResponse(self) -> bool:
        return isinstance(self, ListGrantsResponse_ListGrantsResponse)

class ListGrantsResponse_ListGrantsResponse(ListGrantsResponse, NamedTuple('ListGrantsResponse', [('Grants', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListGrantsResponse.ListGrantsResponse({_dafny.string_of(self.Grants)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListGrantsResponse_ListGrantsResponse) and self.Grants == __o.Grants and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeyPoliciesRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListKeyPoliciesRequest_ListKeyPoliciesRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeyPoliciesRequest(self) -> bool:
        return isinstance(self, ListKeyPoliciesRequest_ListKeyPoliciesRequest)

class ListKeyPoliciesRequest_ListKeyPoliciesRequest(ListKeyPoliciesRequest, NamedTuple('ListKeyPoliciesRequest', [('KeyId', Any), ('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeyPoliciesRequest.ListKeyPoliciesRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeyPoliciesRequest_ListKeyPoliciesRequest) and self.KeyId == __o.KeyId and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeyPoliciesResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListKeyPoliciesResponse_ListKeyPoliciesResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeyPoliciesResponse(self) -> bool:
        return isinstance(self, ListKeyPoliciesResponse_ListKeyPoliciesResponse)

class ListKeyPoliciesResponse_ListKeyPoliciesResponse(ListKeyPoliciesResponse, NamedTuple('ListKeyPoliciesResponse', [('PolicyNames', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeyPoliciesResponse.ListKeyPoliciesResponse({_dafny.string_of(self.PolicyNames)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeyPoliciesResponse_ListKeyPoliciesResponse) and self.PolicyNames == __o.PolicyNames and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeyRotationsRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListKeyRotationsRequest_ListKeyRotationsRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeyRotationsRequest(self) -> bool:
        return isinstance(self, ListKeyRotationsRequest_ListKeyRotationsRequest)

class ListKeyRotationsRequest_ListKeyRotationsRequest(ListKeyRotationsRequest, NamedTuple('ListKeyRotationsRequest', [('KeyId', Any), ('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeyRotationsRequest.ListKeyRotationsRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeyRotationsRequest_ListKeyRotationsRequest) and self.KeyId == __o.KeyId and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeyRotationsResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListKeyRotationsResponse_ListKeyRotationsResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeyRotationsResponse(self) -> bool:
        return isinstance(self, ListKeyRotationsResponse_ListKeyRotationsResponse)

class ListKeyRotationsResponse_ListKeyRotationsResponse(ListKeyRotationsResponse, NamedTuple('ListKeyRotationsResponse', [('Rotations', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeyRotationsResponse.ListKeyRotationsResponse({_dafny.string_of(self.Rotations)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeyRotationsResponse_ListKeyRotationsResponse) and self.Rotations == __o.Rotations and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeysRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListKeysRequest_ListKeysRequest(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeysRequest(self) -> bool:
        return isinstance(self, ListKeysRequest_ListKeysRequest)

class ListKeysRequest_ListKeysRequest(ListKeysRequest, NamedTuple('ListKeysRequest', [('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeysRequest.ListKeysRequest({_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeysRequest_ListKeysRequest) and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class ListKeysResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListKeysResponse_ListKeysResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListKeysResponse(self) -> bool:
        return isinstance(self, ListKeysResponse_ListKeysResponse)

class ListKeysResponse_ListKeysResponse(ListKeysResponse, NamedTuple('ListKeysResponse', [('Keys', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListKeysResponse.ListKeysResponse({_dafny.string_of(self.Keys)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListKeysResponse_ListKeysResponse) and self.Keys == __o.Keys and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class ListResourceTagsRequest:
    @classmethod
    def default(cls, ):
        return lambda: ListResourceTagsRequest_ListResourceTagsRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListResourceTagsRequest(self) -> bool:
        return isinstance(self, ListResourceTagsRequest_ListResourceTagsRequest)

class ListResourceTagsRequest_ListResourceTagsRequest(ListResourceTagsRequest, NamedTuple('ListResourceTagsRequest', [('KeyId', Any), ('Limit', Any), ('Marker', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListResourceTagsRequest.ListResourceTagsRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Limit)}, {_dafny.string_of(self.Marker)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListResourceTagsRequest_ListResourceTagsRequest) and self.KeyId == __o.KeyId and self.Limit == __o.Limit and self.Marker == __o.Marker
    def __hash__(self) -> int:
        return super().__hash__()


class ListResourceTagsResponse:
    @classmethod
    def default(cls, ):
        return lambda: ListResourceTagsResponse_ListResourceTagsResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ListResourceTagsResponse(self) -> bool:
        return isinstance(self, ListResourceTagsResponse_ListResourceTagsResponse)

class ListResourceTagsResponse_ListResourceTagsResponse(ListResourceTagsResponse, NamedTuple('ListResourceTagsResponse', [('Tags', Any), ('NextMarker', Any), ('Truncated', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ListResourceTagsResponse.ListResourceTagsResponse({_dafny.string_of(self.Tags)}, {_dafny.string_of(self.NextMarker)}, {_dafny.string_of(self.Truncated)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ListResourceTagsResponse_ListResourceTagsResponse) and self.Tags == __o.Tags and self.NextMarker == __o.NextMarker and self.Truncated == __o.Truncated
    def __hash__(self) -> int:
        return super().__hash__()


class MacAlgorithmSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [MacAlgorithmSpec_HMAC__SHA__224(), MacAlgorithmSpec_HMAC__SHA__256(), MacAlgorithmSpec_HMAC__SHA__384(), MacAlgorithmSpec_HMAC__SHA__512()]
    @classmethod
    def default(cls, ):
        return lambda: MacAlgorithmSpec_HMAC__SHA__224()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HMAC__SHA__224(self) -> bool:
        return isinstance(self, MacAlgorithmSpec_HMAC__SHA__224)
    @property
    def is_HMAC__SHA__256(self) -> bool:
        return isinstance(self, MacAlgorithmSpec_HMAC__SHA__256)
    @property
    def is_HMAC__SHA__384(self) -> bool:
        return isinstance(self, MacAlgorithmSpec_HMAC__SHA__384)
    @property
    def is_HMAC__SHA__512(self) -> bool:
        return isinstance(self, MacAlgorithmSpec_HMAC__SHA__512)

class MacAlgorithmSpec_HMAC__SHA__224(MacAlgorithmSpec, NamedTuple('HMAC__SHA__224', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_224'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MacAlgorithmSpec_HMAC__SHA__224)
    def __hash__(self) -> int:
        return super().__hash__()

class MacAlgorithmSpec_HMAC__SHA__256(MacAlgorithmSpec, NamedTuple('HMAC__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MacAlgorithmSpec_HMAC__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class MacAlgorithmSpec_HMAC__SHA__384(MacAlgorithmSpec, NamedTuple('HMAC__SHA__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MacAlgorithmSpec_HMAC__SHA__384)
    def __hash__(self) -> int:
        return super().__hash__()

class MacAlgorithmSpec_HMAC__SHA__512(MacAlgorithmSpec, NamedTuple('HMAC__SHA__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MacAlgorithmSpec_HMAC__SHA__512)
    def __hash__(self) -> int:
        return super().__hash__()


class MarkerType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_15_x_: _dafny.Seq = source__
        return default__.IsValid__MarkerType(d_15_x_)

class MessageType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [MessageType_RAW(), MessageType_DIGEST()]
    @classmethod
    def default(cls, ):
        return lambda: MessageType_RAW()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RAW(self) -> bool:
        return isinstance(self, MessageType_RAW)
    @property
    def is_DIGEST(self) -> bool:
        return isinstance(self, MessageType_DIGEST)

class MessageType_RAW(MessageType, NamedTuple('RAW', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MessageType.RAW'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MessageType_RAW)
    def __hash__(self) -> int:
        return super().__hash__()

class MessageType_DIGEST(MessageType, NamedTuple('DIGEST', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MessageType.DIGEST'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MessageType_DIGEST)
    def __hash__(self) -> int:
        return super().__hash__()


class MultiRegionConfiguration:
    @classmethod
    def default(cls, ):
        return lambda: MultiRegionConfiguration_MultiRegionConfiguration(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiRegionConfiguration(self) -> bool:
        return isinstance(self, MultiRegionConfiguration_MultiRegionConfiguration)

class MultiRegionConfiguration_MultiRegionConfiguration(MultiRegionConfiguration, NamedTuple('MultiRegionConfiguration', [('MultiRegionKeyType', Any), ('PrimaryKey', Any), ('ReplicaKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MultiRegionConfiguration.MultiRegionConfiguration({_dafny.string_of(self.MultiRegionKeyType)}, {_dafny.string_of(self.PrimaryKey)}, {_dafny.string_of(self.ReplicaKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiRegionConfiguration_MultiRegionConfiguration) and self.MultiRegionKeyType == __o.MultiRegionKeyType and self.PrimaryKey == __o.PrimaryKey and self.ReplicaKeys == __o.ReplicaKeys
    def __hash__(self) -> int:
        return super().__hash__()


class MultiRegionKey:
    @classmethod
    def default(cls, ):
        return lambda: MultiRegionKey_MultiRegionKey(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiRegionKey(self) -> bool:
        return isinstance(self, MultiRegionKey_MultiRegionKey)

class MultiRegionKey_MultiRegionKey(MultiRegionKey, NamedTuple('MultiRegionKey', [('Arn', Any), ('Region', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MultiRegionKey.MultiRegionKey({_dafny.string_of(self.Arn)}, {_dafny.string_of(self.Region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiRegionKey_MultiRegionKey) and self.Arn == __o.Arn and self.Region == __o.Region
    def __hash__(self) -> int:
        return super().__hash__()


class MultiRegionKeyType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [MultiRegionKeyType_PRIMARY(), MultiRegionKeyType_REPLICA()]
    @classmethod
    def default(cls, ):
        return lambda: MultiRegionKeyType_PRIMARY()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PRIMARY(self) -> bool:
        return isinstance(self, MultiRegionKeyType_PRIMARY)
    @property
    def is_REPLICA(self) -> bool:
        return isinstance(self, MultiRegionKeyType_REPLICA)

class MultiRegionKeyType_PRIMARY(MultiRegionKeyType, NamedTuple('PRIMARY', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MultiRegionKeyType.PRIMARY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiRegionKeyType_PRIMARY)
    def __hash__(self) -> int:
        return super().__hash__()

class MultiRegionKeyType_REPLICA(MultiRegionKeyType, NamedTuple('REPLICA', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.MultiRegionKeyType.REPLICA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MultiRegionKeyType_REPLICA)
    def __hash__(self) -> int:
        return super().__hash__()


class NumberOfBytesType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_16_x_: int = source__
        if True:
            return default__.IsValid__NumberOfBytesType(d_16_x_)
        return False

class OriginType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [OriginType_AWS__KMS(), OriginType_EXTERNAL(), OriginType_AWS__CLOUDHSM(), OriginType_EXTERNAL__KEY__STORE()]
    @classmethod
    def default(cls, ):
        return lambda: OriginType_AWS__KMS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AWS__KMS(self) -> bool:
        return isinstance(self, OriginType_AWS__KMS)
    @property
    def is_EXTERNAL(self) -> bool:
        return isinstance(self, OriginType_EXTERNAL)
    @property
    def is_AWS__CLOUDHSM(self) -> bool:
        return isinstance(self, OriginType_AWS__CLOUDHSM)
    @property
    def is_EXTERNAL__KEY__STORE(self) -> bool:
        return isinstance(self, OriginType_EXTERNAL__KEY__STORE)

class OriginType_AWS__KMS(OriginType, NamedTuple('AWS__KMS', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.OriginType.AWS_KMS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OriginType_AWS__KMS)
    def __hash__(self) -> int:
        return super().__hash__()

class OriginType_EXTERNAL(OriginType, NamedTuple('EXTERNAL', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.OriginType.EXTERNAL'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OriginType_EXTERNAL)
    def __hash__(self) -> int:
        return super().__hash__()

class OriginType_AWS__CLOUDHSM(OriginType, NamedTuple('AWS__CLOUDHSM', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.OriginType.AWS_CLOUDHSM'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OriginType_AWS__CLOUDHSM)
    def __hash__(self) -> int:
        return super().__hash__()

class OriginType_EXTERNAL__KEY__STORE(OriginType, NamedTuple('EXTERNAL__KEY__STORE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.OriginType.EXTERNAL_KEY_STORE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, OriginType_EXTERNAL__KEY__STORE)
    def __hash__(self) -> int:
        return super().__hash__()


class PendingWindowInDaysType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_17_x_: int = source__
        if True:
            return default__.IsValid__PendingWindowInDaysType(d_17_x_)
        return False

class PlaintextType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_18_x_: _dafny.Seq = source__
        return default__.IsValid__PlaintextType(d_18_x_)

class PolicyNameType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_19_x_: _dafny.Seq = source__
        return default__.IsValid__PolicyNameType(d_19_x_)

class PolicyType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_20_x_: _dafny.Seq = source__
        return default__.IsValid__PolicyType(d_20_x_)

class PrincipalIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_21_x_: _dafny.Seq = source__
        return default__.IsValid__PrincipalIdType(d_21_x_)

class PublicKeyType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_22_x_: _dafny.Seq = source__
        return default__.IsValid__PublicKeyType(d_22_x_)

class PutKeyPolicyRequest:
    @classmethod
    def default(cls, ):
        return lambda: PutKeyPolicyRequest_PutKeyPolicyRequest(_dafny.Seq(""), Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutKeyPolicyRequest(self) -> bool:
        return isinstance(self, PutKeyPolicyRequest_PutKeyPolicyRequest)

class PutKeyPolicyRequest_PutKeyPolicyRequest(PutKeyPolicyRequest, NamedTuple('PutKeyPolicyRequest', [('KeyId', Any), ('PolicyName', Any), ('Policy', Any), ('BypassPolicyLockoutSafetyCheck', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.PutKeyPolicyRequest.PutKeyPolicyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.PolicyName)}, {_dafny.string_of(self.Policy)}, {_dafny.string_of(self.BypassPolicyLockoutSafetyCheck)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PutKeyPolicyRequest_PutKeyPolicyRequest) and self.KeyId == __o.KeyId and self.PolicyName == __o.PolicyName and self.Policy == __o.Policy and self.BypassPolicyLockoutSafetyCheck == __o.BypassPolicyLockoutSafetyCheck
    def __hash__(self) -> int:
        return super().__hash__()


class RecipientInfo:
    @classmethod
    def default(cls, ):
        return lambda: RecipientInfo_RecipientInfo(Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RecipientInfo(self) -> bool:
        return isinstance(self, RecipientInfo_RecipientInfo)

class RecipientInfo_RecipientInfo(RecipientInfo, NamedTuple('RecipientInfo', [('KeyEncryptionAlgorithm', Any), ('AttestationDocument', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RecipientInfo.RecipientInfo({_dafny.string_of(self.KeyEncryptionAlgorithm)}, {_dafny.string_of(self.AttestationDocument)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RecipientInfo_RecipientInfo) and self.KeyEncryptionAlgorithm == __o.KeyEncryptionAlgorithm and self.AttestationDocument == __o.AttestationDocument
    def __hash__(self) -> int:
        return super().__hash__()


class ReEncryptRequest:
    @classmethod
    def default(cls, ):
        return lambda: ReEncryptRequest_ReEncryptRequest(_dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReEncryptRequest(self) -> bool:
        return isinstance(self, ReEncryptRequest_ReEncryptRequest)

class ReEncryptRequest_ReEncryptRequest(ReEncryptRequest, NamedTuple('ReEncryptRequest', [('CiphertextBlob', Any), ('SourceEncryptionContext', Any), ('SourceKeyId', Any), ('DestinationKeyId', Any), ('DestinationEncryptionContext', Any), ('SourceEncryptionAlgorithm', Any), ('DestinationEncryptionAlgorithm', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ReEncryptRequest.ReEncryptRequest({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.SourceEncryptionContext)}, {_dafny.string_of(self.SourceKeyId)}, {_dafny.string_of(self.DestinationKeyId)}, {_dafny.string_of(self.DestinationEncryptionContext)}, {_dafny.string_of(self.SourceEncryptionAlgorithm)}, {_dafny.string_of(self.DestinationEncryptionAlgorithm)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReEncryptRequest_ReEncryptRequest) and self.CiphertextBlob == __o.CiphertextBlob and self.SourceEncryptionContext == __o.SourceEncryptionContext and self.SourceKeyId == __o.SourceKeyId and self.DestinationKeyId == __o.DestinationKeyId and self.DestinationEncryptionContext == __o.DestinationEncryptionContext and self.SourceEncryptionAlgorithm == __o.SourceEncryptionAlgorithm and self.DestinationEncryptionAlgorithm == __o.DestinationEncryptionAlgorithm and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class ReEncryptResponse:
    @classmethod
    def default(cls, ):
        return lambda: ReEncryptResponse_ReEncryptResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReEncryptResponse(self) -> bool:
        return isinstance(self, ReEncryptResponse_ReEncryptResponse)

class ReEncryptResponse_ReEncryptResponse(ReEncryptResponse, NamedTuple('ReEncryptResponse', [('CiphertextBlob', Any), ('SourceKeyId', Any), ('KeyId', Any), ('SourceEncryptionAlgorithm', Any), ('DestinationEncryptionAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ReEncryptResponse.ReEncryptResponse({_dafny.string_of(self.CiphertextBlob)}, {_dafny.string_of(self.SourceKeyId)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.SourceEncryptionAlgorithm)}, {_dafny.string_of(self.DestinationEncryptionAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReEncryptResponse_ReEncryptResponse) and self.CiphertextBlob == __o.CiphertextBlob and self.SourceKeyId == __o.SourceKeyId and self.KeyId == __o.KeyId and self.SourceEncryptionAlgorithm == __o.SourceEncryptionAlgorithm and self.DestinationEncryptionAlgorithm == __o.DestinationEncryptionAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class RegionType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_23_x_: _dafny.Seq = source__
        return default__.IsValid__RegionType(d_23_x_)

class ReplicateKeyRequest:
    @classmethod
    def default(cls, ):
        return lambda: ReplicateKeyRequest_ReplicateKeyRequest(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicateKeyRequest(self) -> bool:
        return isinstance(self, ReplicateKeyRequest_ReplicateKeyRequest)

class ReplicateKeyRequest_ReplicateKeyRequest(ReplicateKeyRequest, NamedTuple('ReplicateKeyRequest', [('KeyId', Any), ('ReplicaRegion', Any), ('Policy', Any), ('BypassPolicyLockoutSafetyCheck', Any), ('Description', Any), ('Tags', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ReplicateKeyRequest.ReplicateKeyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.ReplicaRegion)}, {_dafny.string_of(self.Policy)}, {_dafny.string_of(self.BypassPolicyLockoutSafetyCheck)}, {_dafny.string_of(self.Description)}, {_dafny.string_of(self.Tags)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicateKeyRequest_ReplicateKeyRequest) and self.KeyId == __o.KeyId and self.ReplicaRegion == __o.ReplicaRegion and self.Policy == __o.Policy and self.BypassPolicyLockoutSafetyCheck == __o.BypassPolicyLockoutSafetyCheck and self.Description == __o.Description and self.Tags == __o.Tags
    def __hash__(self) -> int:
        return super().__hash__()


class ReplicateKeyResponse:
    @classmethod
    def default(cls, ):
        return lambda: ReplicateKeyResponse_ReplicateKeyResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ReplicateKeyResponse(self) -> bool:
        return isinstance(self, ReplicateKeyResponse_ReplicateKeyResponse)

class ReplicateKeyResponse_ReplicateKeyResponse(ReplicateKeyResponse, NamedTuple('ReplicateKeyResponse', [('ReplicaKeyMetadata', Any), ('ReplicaPolicy', Any), ('ReplicaTags', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ReplicateKeyResponse.ReplicateKeyResponse({_dafny.string_of(self.ReplicaKeyMetadata)}, {_dafny.string_of(self.ReplicaPolicy)}, {_dafny.string_of(self.ReplicaTags)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ReplicateKeyResponse_ReplicateKeyResponse) and self.ReplicaKeyMetadata == __o.ReplicaKeyMetadata and self.ReplicaPolicy == __o.ReplicaPolicy and self.ReplicaTags == __o.ReplicaTags
    def __hash__(self) -> int:
        return super().__hash__()


class RetireGrantRequest:
    @classmethod
    def default(cls, ):
        return lambda: RetireGrantRequest_RetireGrantRequest(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RetireGrantRequest(self) -> bool:
        return isinstance(self, RetireGrantRequest_RetireGrantRequest)

class RetireGrantRequest_RetireGrantRequest(RetireGrantRequest, NamedTuple('RetireGrantRequest', [('GrantToken', Any), ('KeyId', Any), ('GrantId', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RetireGrantRequest.RetireGrantRequest({_dafny.string_of(self.GrantToken)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantId)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RetireGrantRequest_RetireGrantRequest) and self.GrantToken == __o.GrantToken and self.KeyId == __o.KeyId and self.GrantId == __o.GrantId and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class RevokeGrantRequest:
    @classmethod
    def default(cls, ):
        return lambda: RevokeGrantRequest_RevokeGrantRequest(_dafny.Seq(""), _dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RevokeGrantRequest(self) -> bool:
        return isinstance(self, RevokeGrantRequest_RevokeGrantRequest)

class RevokeGrantRequest_RevokeGrantRequest(RevokeGrantRequest, NamedTuple('RevokeGrantRequest', [('KeyId', Any), ('GrantId', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RevokeGrantRequest.RevokeGrantRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.GrantId)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RevokeGrantRequest_RevokeGrantRequest) and self.KeyId == __o.KeyId and self.GrantId == __o.GrantId and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class RotateKeyOnDemandRequest:
    @classmethod
    def default(cls, ):
        return lambda: RotateKeyOnDemandRequest_RotateKeyOnDemandRequest(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RotateKeyOnDemandRequest(self) -> bool:
        return isinstance(self, RotateKeyOnDemandRequest_RotateKeyOnDemandRequest)

class RotateKeyOnDemandRequest_RotateKeyOnDemandRequest(RotateKeyOnDemandRequest, NamedTuple('RotateKeyOnDemandRequest', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RotateKeyOnDemandRequest.RotateKeyOnDemandRequest({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RotateKeyOnDemandRequest_RotateKeyOnDemandRequest) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class RotateKeyOnDemandResponse:
    @classmethod
    def default(cls, ):
        return lambda: RotateKeyOnDemandResponse_RotateKeyOnDemandResponse(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RotateKeyOnDemandResponse(self) -> bool:
        return isinstance(self, RotateKeyOnDemandResponse_RotateKeyOnDemandResponse)

class RotateKeyOnDemandResponse_RotateKeyOnDemandResponse(RotateKeyOnDemandResponse, NamedTuple('RotateKeyOnDemandResponse', [('KeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RotateKeyOnDemandResponse.RotateKeyOnDemandResponse({_dafny.string_of(self.KeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RotateKeyOnDemandResponse_RotateKeyOnDemandResponse) and self.KeyId == __o.KeyId
    def __hash__(self) -> int:
        return super().__hash__()


class RotationPeriodInDaysType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_24_x_: int = source__
        if True:
            return default__.IsValid__RotationPeriodInDaysType(d_24_x_)
        return False

class RotationsListEntry:
    @classmethod
    def default(cls, ):
        return lambda: RotationsListEntry_RotationsListEntry(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RotationsListEntry(self) -> bool:
        return isinstance(self, RotationsListEntry_RotationsListEntry)

class RotationsListEntry_RotationsListEntry(RotationsListEntry, NamedTuple('RotationsListEntry', [('KeyId', Any), ('RotationDate', Any), ('RotationType', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RotationsListEntry.RotationsListEntry({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.RotationDate)}, {_dafny.string_of(self.RotationType)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RotationsListEntry_RotationsListEntry) and self.KeyId == __o.KeyId and self.RotationDate == __o.RotationDate and self.RotationType == __o.RotationType
    def __hash__(self) -> int:
        return super().__hash__()


class RotationType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [RotationType_AUTOMATIC(), RotationType_ON__DEMAND()]
    @classmethod
    def default(cls, ):
        return lambda: RotationType_AUTOMATIC()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AUTOMATIC(self) -> bool:
        return isinstance(self, RotationType_AUTOMATIC)
    @property
    def is_ON__DEMAND(self) -> bool:
        return isinstance(self, RotationType_ON__DEMAND)

class RotationType_AUTOMATIC(RotationType, NamedTuple('AUTOMATIC', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RotationType.AUTOMATIC'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RotationType_AUTOMATIC)
    def __hash__(self) -> int:
        return super().__hash__()

class RotationType_ON__DEMAND(RotationType, NamedTuple('ON__DEMAND', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.RotationType.ON_DEMAND'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RotationType_ON__DEMAND)
    def __hash__(self) -> int:
        return super().__hash__()


class ScheduleKeyDeletionRequest:
    @classmethod
    def default(cls, ):
        return lambda: ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ScheduleKeyDeletionRequest(self) -> bool:
        return isinstance(self, ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest)

class ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest(ScheduleKeyDeletionRequest, NamedTuple('ScheduleKeyDeletionRequest', [('KeyId', Any), ('PendingWindowInDays', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ScheduleKeyDeletionRequest.ScheduleKeyDeletionRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.PendingWindowInDays)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest) and self.KeyId == __o.KeyId and self.PendingWindowInDays == __o.PendingWindowInDays
    def __hash__(self) -> int:
        return super().__hash__()


class ScheduleKeyDeletionResponse:
    @classmethod
    def default(cls, ):
        return lambda: ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ScheduleKeyDeletionResponse(self) -> bool:
        return isinstance(self, ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse)

class ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse(ScheduleKeyDeletionResponse, NamedTuple('ScheduleKeyDeletionResponse', [('KeyId', Any), ('DeletionDate', Any), ('KeyState', Any), ('PendingWindowInDays', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.ScheduleKeyDeletionResponse.ScheduleKeyDeletionResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.DeletionDate)}, {_dafny.string_of(self.KeyState)}, {_dafny.string_of(self.PendingWindowInDays)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse) and self.KeyId == __o.KeyId and self.DeletionDate == __o.DeletionDate and self.KeyState == __o.KeyState and self.PendingWindowInDays == __o.PendingWindowInDays
    def __hash__(self) -> int:
        return super().__hash__()


class SigningAlgorithmSpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [SigningAlgorithmSpec_RSASSA__PSS__SHA__256(), SigningAlgorithmSpec_RSASSA__PSS__SHA__384(), SigningAlgorithmSpec_RSASSA__PSS__SHA__512(), SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256(), SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384(), SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512(), SigningAlgorithmSpec_ECDSA__SHA__256(), SigningAlgorithmSpec_ECDSA__SHA__384(), SigningAlgorithmSpec_ECDSA__SHA__512(), SigningAlgorithmSpec_SM2DSA()]
    @classmethod
    def default(cls, ):
        return lambda: SigningAlgorithmSpec_RSASSA__PSS__SHA__256()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSASSA__PSS__SHA__256(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PSS__SHA__256)
    @property
    def is_RSASSA__PSS__SHA__384(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PSS__SHA__384)
    @property
    def is_RSASSA__PSS__SHA__512(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PSS__SHA__512)
    @property
    def is_RSASSA__PKCS1__V1__5__SHA__256(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256)
    @property
    def is_RSASSA__PKCS1__V1__5__SHA__384(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384)
    @property
    def is_RSASSA__PKCS1__V1__5__SHA__512(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512)
    @property
    def is_ECDSA__SHA__256(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_ECDSA__SHA__256)
    @property
    def is_ECDSA__SHA__384(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_ECDSA__SHA__384)
    @property
    def is_ECDSA__SHA__512(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_ECDSA__SHA__512)
    @property
    def is_SM2DSA(self) -> bool:
        return isinstance(self, SigningAlgorithmSpec_SM2DSA)

class SigningAlgorithmSpec_RSASSA__PSS__SHA__256(SigningAlgorithmSpec, NamedTuple('RSASSA__PSS__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PSS_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PSS__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_RSASSA__PSS__SHA__384(SigningAlgorithmSpec, NamedTuple('RSASSA__PSS__SHA__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PSS_SHA_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PSS__SHA__384)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_RSASSA__PSS__SHA__512(SigningAlgorithmSpec, NamedTuple('RSASSA__PSS__SHA__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PSS_SHA_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PSS__SHA__512)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256(SigningAlgorithmSpec, NamedTuple('RSASSA__PKCS1__V1__5__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PKCS1_V1_5_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384(SigningAlgorithmSpec, NamedTuple('RSASSA__PKCS1__V1__5__SHA__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PKCS1_V1_5_SHA_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512(SigningAlgorithmSpec, NamedTuple('RSASSA__PKCS1__V1__5__SHA__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PKCS1_V1_5_SHA_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_ECDSA__SHA__256(SigningAlgorithmSpec, NamedTuple('ECDSA__SHA__256', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.ECDSA_SHA_256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_ECDSA__SHA__256)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_ECDSA__SHA__384(SigningAlgorithmSpec, NamedTuple('ECDSA__SHA__384', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.ECDSA_SHA_384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_ECDSA__SHA__384)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_ECDSA__SHA__512(SigningAlgorithmSpec, NamedTuple('ECDSA__SHA__512', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.ECDSA_SHA_512'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_ECDSA__SHA__512)
    def __hash__(self) -> int:
        return super().__hash__()

class SigningAlgorithmSpec_SM2DSA(SigningAlgorithmSpec, NamedTuple('SM2DSA', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SigningAlgorithmSpec.SM2DSA'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SigningAlgorithmSpec_SM2DSA)
    def __hash__(self) -> int:
        return super().__hash__()


class SignRequest:
    @classmethod
    def default(cls, ):
        return lambda: SignRequest_SignRequest(_dafny.Seq(""), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()(), SigningAlgorithmSpec.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SignRequest(self) -> bool:
        return isinstance(self, SignRequest_SignRequest)

class SignRequest_SignRequest(SignRequest, NamedTuple('SignRequest', [('KeyId', Any), ('Message', Any), ('MessageType', Any), ('GrantTokens', Any), ('SigningAlgorithm', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SignRequest.SignRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Message)}, {_dafny.string_of(self.MessageType)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.SigningAlgorithm)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignRequest_SignRequest) and self.KeyId == __o.KeyId and self.Message == __o.Message and self.MessageType == __o.MessageType and self.GrantTokens == __o.GrantTokens and self.SigningAlgorithm == __o.SigningAlgorithm and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class SignResponse:
    @classmethod
    def default(cls, ):
        return lambda: SignResponse_SignResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SignResponse(self) -> bool:
        return isinstance(self, SignResponse_SignResponse)

class SignResponse_SignResponse(SignResponse, NamedTuple('SignResponse', [('KeyId', Any), ('Signature', Any), ('SigningAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.SignResponse.SignResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Signature)}, {_dafny.string_of(self.SigningAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignResponse_SignResponse) and self.KeyId == __o.KeyId and self.Signature == __o.Signature and self.SigningAlgorithm == __o.SigningAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class Tag:
    @classmethod
    def default(cls, ):
        return lambda: Tag_Tag(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Tag(self) -> bool:
        return isinstance(self, Tag_Tag)

class Tag_Tag(Tag, NamedTuple('Tag', [('TagKey', Any), ('TagValue', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Tag.Tag({_dafny.string_of(self.TagKey)}, {_dafny.string_of(self.TagValue)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tag_Tag) and self.TagKey == __o.TagKey and self.TagValue == __o.TagValue
    def __hash__(self) -> int:
        return super().__hash__()


class TagKeyType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_25_x_: _dafny.Seq = source__
        return default__.IsValid__TagKeyType(d_25_x_)

class TagResourceRequest:
    @classmethod
    def default(cls, ):
        return lambda: TagResourceRequest_TagResourceRequest(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TagResourceRequest(self) -> bool:
        return isinstance(self, TagResourceRequest_TagResourceRequest)

class TagResourceRequest_TagResourceRequest(TagResourceRequest, NamedTuple('TagResourceRequest', [('KeyId', Any), ('Tags', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.TagResourceRequest.TagResourceRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Tags)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TagResourceRequest_TagResourceRequest) and self.KeyId == __o.KeyId and self.Tags == __o.Tags
    def __hash__(self) -> int:
        return super().__hash__()


class TagValueType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_26_x_: _dafny.Seq = source__
        return default__.IsValid__TagValueType(d_26_x_)

class IKMSClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "ComAmazonawsKmsTypes.IKMSClientCallHistory"

class IKMSClient:
    pass
    def CancelKeyDeletion(self, input):
        pass

    def ConnectCustomKeyStore(self, input):
        pass

    def CreateAlias(self, input):
        pass

    def CreateCustomKeyStore(self, input):
        pass

    def CreateGrant(self, input):
        pass

    def CreateKey(self, input):
        pass

    def Decrypt(self, input):
        pass

    def DeleteAlias(self, input):
        pass

    def DeleteCustomKeyStore(self, input):
        pass

    def DeleteImportedKeyMaterial(self, input):
        pass

    def DeriveSharedSecret(self, input):
        pass

    def DescribeCustomKeyStores(self, input):
        pass

    def DescribeKey(self, input):
        pass

    def DisableKey(self, input):
        pass

    def DisableKeyRotation(self, input):
        pass

    def DisconnectCustomKeyStore(self, input):
        pass

    def EnableKey(self, input):
        pass

    def EnableKeyRotation(self, input):
        pass

    def Encrypt(self, input):
        pass

    def GenerateDataKey(self, input):
        pass

    def GenerateDataKeyPair(self, input):
        pass

    def GenerateDataKeyPairWithoutPlaintext(self, input):
        pass

    def GenerateDataKeyWithoutPlaintext(self, input):
        pass

    def GenerateMac(self, input):
        pass

    def GenerateRandom(self, input):
        pass

    def GetKeyPolicy(self, input):
        pass

    def GetKeyRotationStatus(self, input):
        pass

    def GetParametersForImport(self, input):
        pass

    def GetPublicKey(self, input):
        pass

    def ImportKeyMaterial(self, input):
        pass

    def ListAliases(self, input):
        pass

    def ListGrants(self, input):
        pass

    def ListKeyPolicies(self, input):
        pass

    def ListKeyRotations(self, input):
        pass

    def ListKeys(self, input):
        pass

    def ListResourceTags(self, input):
        pass

    def PutKeyPolicy(self, input):
        pass

    def ReEncrypt(self, input):
        pass

    def ReplicateKey(self, input):
        pass

    def RetireGrant(self, input):
        pass

    def RevokeGrant(self, input):
        pass

    def RotateKeyOnDemand(self, input):
        pass

    def ScheduleKeyDeletion(self, input):
        pass

    def Sign(self, input):
        pass

    def TagResource(self, input):
        pass

    def UntagResource(self, input):
        pass

    def UpdateAlias(self, input):
        pass

    def UpdateCustomKeyStore(self, input):
        pass

    def UpdateKeyDescription(self, input):
        pass

    def UpdatePrimaryRegion(self, input):
        pass

    def Verify(self, input):
        pass

    def VerifyMac(self, input):
        pass


class TrustAnchorCertificateType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_0_x_: _dafny.Seq = source__
        return default__.IsValid__TrustAnchorCertificateType(d_0_x_)

class UntagResourceRequest:
    @classmethod
    def default(cls, ):
        return lambda: UntagResourceRequest_UntagResourceRequest(_dafny.Seq(""), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UntagResourceRequest(self) -> bool:
        return isinstance(self, UntagResourceRequest_UntagResourceRequest)

class UntagResourceRequest_UntagResourceRequest(UntagResourceRequest, NamedTuple('UntagResourceRequest', [('KeyId', Any), ('TagKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UntagResourceRequest.UntagResourceRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.TagKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UntagResourceRequest_UntagResourceRequest) and self.KeyId == __o.KeyId and self.TagKeys == __o.TagKeys
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateAliasRequest:
    @classmethod
    def default(cls, ):
        return lambda: UpdateAliasRequest_UpdateAliasRequest(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateAliasRequest(self) -> bool:
        return isinstance(self, UpdateAliasRequest_UpdateAliasRequest)

class UpdateAliasRequest_UpdateAliasRequest(UpdateAliasRequest, NamedTuple('UpdateAliasRequest', [('AliasName', Any), ('TargetKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UpdateAliasRequest.UpdateAliasRequest({_dafny.string_of(self.AliasName)}, {_dafny.string_of(self.TargetKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateAliasRequest_UpdateAliasRequest) and self.AliasName == __o.AliasName and self.TargetKeyId == __o.TargetKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateCustomKeyStoreRequest:
    @classmethod
    def default(cls, ):
        return lambda: UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest(_dafny.Seq(""), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateCustomKeyStoreRequest(self) -> bool:
        return isinstance(self, UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest)

class UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest(UpdateCustomKeyStoreRequest, NamedTuple('UpdateCustomKeyStoreRequest', [('CustomKeyStoreId', Any), ('NewCustomKeyStoreName', Any), ('KeyStorePassword', Any), ('CloudHsmClusterId', Any), ('XksProxyUriEndpoint', Any), ('XksProxyUriPath', Any), ('XksProxyVpcEndpointServiceName', Any), ('XksProxyAuthenticationCredential', Any), ('XksProxyConnectivity', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UpdateCustomKeyStoreRequest.UpdateCustomKeyStoreRequest({_dafny.string_of(self.CustomKeyStoreId)}, {_dafny.string_of(self.NewCustomKeyStoreName)}, {_dafny.string_of(self.KeyStorePassword)}, {_dafny.string_of(self.CloudHsmClusterId)}, {_dafny.string_of(self.XksProxyUriEndpoint)}, {_dafny.string_of(self.XksProxyUriPath)}, {_dafny.string_of(self.XksProxyVpcEndpointServiceName)}, {_dafny.string_of(self.XksProxyAuthenticationCredential)}, {_dafny.string_of(self.XksProxyConnectivity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest) and self.CustomKeyStoreId == __o.CustomKeyStoreId and self.NewCustomKeyStoreName == __o.NewCustomKeyStoreName and self.KeyStorePassword == __o.KeyStorePassword and self.CloudHsmClusterId == __o.CloudHsmClusterId and self.XksProxyUriEndpoint == __o.XksProxyUriEndpoint and self.XksProxyUriPath == __o.XksProxyUriPath and self.XksProxyVpcEndpointServiceName == __o.XksProxyVpcEndpointServiceName and self.XksProxyAuthenticationCredential == __o.XksProxyAuthenticationCredential and self.XksProxyConnectivity == __o.XksProxyConnectivity
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateCustomKeyStoreResponse:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse()]
    @classmethod
    def default(cls, ):
        return lambda: UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateCustomKeyStoreResponse(self) -> bool:
        return isinstance(self, UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse)

class UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse(UpdateCustomKeyStoreResponse, NamedTuple('UpdateCustomKeyStoreResponse', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UpdateCustomKeyStoreResponse.UpdateCustomKeyStoreResponse'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse)
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateKeyDescriptionRequest:
    @classmethod
    def default(cls, ):
        return lambda: UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateKeyDescriptionRequest(self) -> bool:
        return isinstance(self, UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest)

class UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest(UpdateKeyDescriptionRequest, NamedTuple('UpdateKeyDescriptionRequest', [('KeyId', Any), ('Description', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UpdateKeyDescriptionRequest.UpdateKeyDescriptionRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Description)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest) and self.KeyId == __o.KeyId and self.Description == __o.Description
    def __hash__(self) -> int:
        return super().__hash__()


class UpdatePrimaryRegionRequest:
    @classmethod
    def default(cls, ):
        return lambda: UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdatePrimaryRegionRequest(self) -> bool:
        return isinstance(self, UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest)

class UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest(UpdatePrimaryRegionRequest, NamedTuple('UpdatePrimaryRegionRequest', [('KeyId', Any), ('PrimaryRegion', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.UpdatePrimaryRegionRequest.UpdatePrimaryRegionRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.PrimaryRegion)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest) and self.KeyId == __o.KeyId and self.PrimaryRegion == __o.PrimaryRegion
    def __hash__(self) -> int:
        return super().__hash__()


class VerifyMacRequest:
    @classmethod
    def default(cls, ):
        return lambda: VerifyMacRequest_VerifyMacRequest(_dafny.Seq({}), _dafny.Seq(""), MacAlgorithmSpec.default()(), _dafny.Seq({}), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VerifyMacRequest(self) -> bool:
        return isinstance(self, VerifyMacRequest_VerifyMacRequest)

class VerifyMacRequest_VerifyMacRequest(VerifyMacRequest, NamedTuple('VerifyMacRequest', [('Message', Any), ('KeyId', Any), ('MacAlgorithm', Any), ('Mac', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.VerifyMacRequest.VerifyMacRequest({_dafny.string_of(self.Message)}, {_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.MacAlgorithm)}, {_dafny.string_of(self.Mac)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VerifyMacRequest_VerifyMacRequest) and self.Message == __o.Message and self.KeyId == __o.KeyId and self.MacAlgorithm == __o.MacAlgorithm and self.Mac == __o.Mac and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class VerifyMacResponse:
    @classmethod
    def default(cls, ):
        return lambda: VerifyMacResponse_VerifyMacResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VerifyMacResponse(self) -> bool:
        return isinstance(self, VerifyMacResponse_VerifyMacResponse)

class VerifyMacResponse_VerifyMacResponse(VerifyMacResponse, NamedTuple('VerifyMacResponse', [('KeyId', Any), ('MacValid', Any), ('MacAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.VerifyMacResponse.VerifyMacResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.MacValid)}, {_dafny.string_of(self.MacAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VerifyMacResponse_VerifyMacResponse) and self.KeyId == __o.KeyId and self.MacValid == __o.MacValid and self.MacAlgorithm == __o.MacAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class VerifyRequest:
    @classmethod
    def default(cls, ):
        return lambda: VerifyRequest_VerifyRequest(_dafny.Seq(""), _dafny.Seq({}), Wrappers.Option.default()(), _dafny.Seq({}), SigningAlgorithmSpec.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VerifyRequest(self) -> bool:
        return isinstance(self, VerifyRequest_VerifyRequest)

class VerifyRequest_VerifyRequest(VerifyRequest, NamedTuple('VerifyRequest', [('KeyId', Any), ('Message', Any), ('MessageType', Any), ('Signature', Any), ('SigningAlgorithm', Any), ('GrantTokens', Any), ('DryRun', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.VerifyRequest.VerifyRequest({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.Message)}, {_dafny.string_of(self.MessageType)}, {_dafny.string_of(self.Signature)}, {_dafny.string_of(self.SigningAlgorithm)}, {_dafny.string_of(self.GrantTokens)}, {_dafny.string_of(self.DryRun)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VerifyRequest_VerifyRequest) and self.KeyId == __o.KeyId and self.Message == __o.Message and self.MessageType == __o.MessageType and self.Signature == __o.Signature and self.SigningAlgorithm == __o.SigningAlgorithm and self.GrantTokens == __o.GrantTokens and self.DryRun == __o.DryRun
    def __hash__(self) -> int:
        return super().__hash__()


class VerifyResponse:
    @classmethod
    def default(cls, ):
        return lambda: VerifyResponse_VerifyResponse(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_VerifyResponse(self) -> bool:
        return isinstance(self, VerifyResponse_VerifyResponse)

class VerifyResponse_VerifyResponse(VerifyResponse, NamedTuple('VerifyResponse', [('KeyId', Any), ('SignatureValid', Any), ('SigningAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.VerifyResponse.VerifyResponse({_dafny.string_of(self.KeyId)}, {_dafny.string_of(self.SignatureValid)}, {_dafny.string_of(self.SigningAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VerifyResponse_VerifyResponse) and self.KeyId == __o.KeyId and self.SignatureValid == __o.SignatureValid and self.SigningAlgorithm == __o.SigningAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class WrappingKeySpec:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [WrappingKeySpec_RSA__2048(), WrappingKeySpec_RSA__3072(), WrappingKeySpec_RSA__4096(), WrappingKeySpec_SM2()]
    @classmethod
    def default(cls, ):
        return lambda: WrappingKeySpec_RSA__2048()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RSA__2048(self) -> bool:
        return isinstance(self, WrappingKeySpec_RSA__2048)
    @property
    def is_RSA__3072(self) -> bool:
        return isinstance(self, WrappingKeySpec_RSA__3072)
    @property
    def is_RSA__4096(self) -> bool:
        return isinstance(self, WrappingKeySpec_RSA__4096)
    @property
    def is_SM2(self) -> bool:
        return isinstance(self, WrappingKeySpec_SM2)

class WrappingKeySpec_RSA__2048(WrappingKeySpec, NamedTuple('RSA__2048', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.WrappingKeySpec.RSA_2048'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrappingKeySpec_RSA__2048)
    def __hash__(self) -> int:
        return super().__hash__()

class WrappingKeySpec_RSA__3072(WrappingKeySpec, NamedTuple('RSA__3072', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.WrappingKeySpec.RSA_3072'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrappingKeySpec_RSA__3072)
    def __hash__(self) -> int:
        return super().__hash__()

class WrappingKeySpec_RSA__4096(WrappingKeySpec, NamedTuple('RSA__4096', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.WrappingKeySpec.RSA_4096'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrappingKeySpec_RSA__4096)
    def __hash__(self) -> int:
        return super().__hash__()

class WrappingKeySpec_SM2(WrappingKeySpec, NamedTuple('SM2', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.WrappingKeySpec.SM2'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrappingKeySpec_SM2)
    def __hash__(self) -> int:
        return super().__hash__()


class XksKeyConfigurationType:
    @classmethod
    def default(cls, ):
        return lambda: XksKeyConfigurationType_XksKeyConfigurationType(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_XksKeyConfigurationType(self) -> bool:
        return isinstance(self, XksKeyConfigurationType_XksKeyConfigurationType)

class XksKeyConfigurationType_XksKeyConfigurationType(XksKeyConfigurationType, NamedTuple('XksKeyConfigurationType', [('Id', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.XksKeyConfigurationType.XksKeyConfigurationType({_dafny.string_of(self.Id)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, XksKeyConfigurationType_XksKeyConfigurationType) and self.Id == __o.Id
    def __hash__(self) -> int:
        return super().__hash__()


class XksKeyIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_x_: _dafny.Seq = source__
        return default__.IsValid__XksKeyIdType(d_1_x_)

class XksProxyAuthenticationAccessKeyIdType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_2_x_: _dafny.Seq = source__
        return default__.IsValid__XksProxyAuthenticationAccessKeyIdType(d_2_x_)

class XksProxyAuthenticationCredentialType:
    @classmethod
    def default(cls, ):
        return lambda: XksProxyAuthenticationCredentialType_XksProxyAuthenticationCredentialType(_dafny.Seq(""), _dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_XksProxyAuthenticationCredentialType(self) -> bool:
        return isinstance(self, XksProxyAuthenticationCredentialType_XksProxyAuthenticationCredentialType)

class XksProxyAuthenticationCredentialType_XksProxyAuthenticationCredentialType(XksProxyAuthenticationCredentialType, NamedTuple('XksProxyAuthenticationCredentialType', [('AccessKeyId', Any), ('RawSecretAccessKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.XksProxyAuthenticationCredentialType.XksProxyAuthenticationCredentialType({_dafny.string_of(self.AccessKeyId)}, {_dafny.string_of(self.RawSecretAccessKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, XksProxyAuthenticationCredentialType_XksProxyAuthenticationCredentialType) and self.AccessKeyId == __o.AccessKeyId and self.RawSecretAccessKey == __o.RawSecretAccessKey
    def __hash__(self) -> int:
        return super().__hash__()


class XksProxyAuthenticationRawSecretAccessKeyType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_3_x_: _dafny.Seq = source__
        return default__.IsValid__XksProxyAuthenticationRawSecretAccessKeyType(d_3_x_)

class XksProxyConfigurationType:
    @classmethod
    def default(cls, ):
        return lambda: XksProxyConfigurationType_XksProxyConfigurationType(Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_XksProxyConfigurationType(self) -> bool:
        return isinstance(self, XksProxyConfigurationType_XksProxyConfigurationType)

class XksProxyConfigurationType_XksProxyConfigurationType(XksProxyConfigurationType, NamedTuple('XksProxyConfigurationType', [('Connectivity', Any), ('AccessKeyId', Any), ('UriEndpoint', Any), ('UriPath', Any), ('VpcEndpointServiceName', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.XksProxyConfigurationType.XksProxyConfigurationType({_dafny.string_of(self.Connectivity)}, {_dafny.string_of(self.AccessKeyId)}, {_dafny.string_of(self.UriEndpoint)}, {_dafny.string_of(self.UriPath)}, {_dafny.string_of(self.VpcEndpointServiceName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, XksProxyConfigurationType_XksProxyConfigurationType) and self.Connectivity == __o.Connectivity and self.AccessKeyId == __o.AccessKeyId and self.UriEndpoint == __o.UriEndpoint and self.UriPath == __o.UriPath and self.VpcEndpointServiceName == __o.VpcEndpointServiceName
    def __hash__(self) -> int:
        return super().__hash__()


class XksProxyConnectivityType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [XksProxyConnectivityType_PUBLIC__ENDPOINT(), XksProxyConnectivityType_VPC__ENDPOINT__SERVICE()]
    @classmethod
    def default(cls, ):
        return lambda: XksProxyConnectivityType_PUBLIC__ENDPOINT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PUBLIC__ENDPOINT(self) -> bool:
        return isinstance(self, XksProxyConnectivityType_PUBLIC__ENDPOINT)
    @property
    def is_VPC__ENDPOINT__SERVICE(self) -> bool:
        return isinstance(self, XksProxyConnectivityType_VPC__ENDPOINT__SERVICE)

class XksProxyConnectivityType_PUBLIC__ENDPOINT(XksProxyConnectivityType, NamedTuple('PUBLIC__ENDPOINT', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.XksProxyConnectivityType.PUBLIC_ENDPOINT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, XksProxyConnectivityType_PUBLIC__ENDPOINT)
    def __hash__(self) -> int:
        return super().__hash__()

class XksProxyConnectivityType_VPC__ENDPOINT__SERVICE(XksProxyConnectivityType, NamedTuple('VPC__ENDPOINT__SERVICE', [])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.XksProxyConnectivityType.VPC_ENDPOINT_SERVICE'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, XksProxyConnectivityType_VPC__ENDPOINT__SERVICE)
    def __hash__(self) -> int:
        return super().__hash__()


class XksProxyUriEndpointType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_4_x_: _dafny.Seq = source__
        return default__.IsValid__XksProxyUriEndpointType(d_4_x_)

class XksProxyUriPathType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_5_x_: _dafny.Seq = source__
        return default__.IsValid__XksProxyUriPathType(d_5_x_)

class XksProxyVpcEndpointServiceNameType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_6_x_: _dafny.Seq = source__
        return default__.IsValid__XksProxyVpcEndpointServiceNameType(d_6_x_)

class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_AlreadyExistsException(Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AlreadyExistsException(self) -> bool:
        return isinstance(self, Error_AlreadyExistsException)
    @property
    def is_CloudHsmClusterInUseException(self) -> bool:
        return isinstance(self, Error_CloudHsmClusterInUseException)
    @property
    def is_CloudHsmClusterInvalidConfigurationException(self) -> bool:
        return isinstance(self, Error_CloudHsmClusterInvalidConfigurationException)
    @property
    def is_CloudHsmClusterNotActiveException(self) -> bool:
        return isinstance(self, Error_CloudHsmClusterNotActiveException)
    @property
    def is_CloudHsmClusterNotFoundException(self) -> bool:
        return isinstance(self, Error_CloudHsmClusterNotFoundException)
    @property
    def is_CloudHsmClusterNotRelatedException(self) -> bool:
        return isinstance(self, Error_CloudHsmClusterNotRelatedException)
    @property
    def is_ConflictException(self) -> bool:
        return isinstance(self, Error_ConflictException)
    @property
    def is_CustomKeyStoreHasCMKsException(self) -> bool:
        return isinstance(self, Error_CustomKeyStoreHasCMKsException)
    @property
    def is_CustomKeyStoreInvalidStateException(self) -> bool:
        return isinstance(self, Error_CustomKeyStoreInvalidStateException)
    @property
    def is_CustomKeyStoreNameInUseException(self) -> bool:
        return isinstance(self, Error_CustomKeyStoreNameInUseException)
    @property
    def is_CustomKeyStoreNotFoundException(self) -> bool:
        return isinstance(self, Error_CustomKeyStoreNotFoundException)
    @property
    def is_DependencyTimeoutException(self) -> bool:
        return isinstance(self, Error_DependencyTimeoutException)
    @property
    def is_DisabledException(self) -> bool:
        return isinstance(self, Error_DisabledException)
    @property
    def is_DryRunOperationException(self) -> bool:
        return isinstance(self, Error_DryRunOperationException)
    @property
    def is_ExpiredImportTokenException(self) -> bool:
        return isinstance(self, Error_ExpiredImportTokenException)
    @property
    def is_IncorrectKeyException(self) -> bool:
        return isinstance(self, Error_IncorrectKeyException)
    @property
    def is_IncorrectKeyMaterialException(self) -> bool:
        return isinstance(self, Error_IncorrectKeyMaterialException)
    @property
    def is_IncorrectTrustAnchorException(self) -> bool:
        return isinstance(self, Error_IncorrectTrustAnchorException)
    @property
    def is_InvalidAliasNameException(self) -> bool:
        return isinstance(self, Error_InvalidAliasNameException)
    @property
    def is_InvalidArnException(self) -> bool:
        return isinstance(self, Error_InvalidArnException)
    @property
    def is_InvalidCiphertextException(self) -> bool:
        return isinstance(self, Error_InvalidCiphertextException)
    @property
    def is_InvalidGrantIdException(self) -> bool:
        return isinstance(self, Error_InvalidGrantIdException)
    @property
    def is_InvalidGrantTokenException(self) -> bool:
        return isinstance(self, Error_InvalidGrantTokenException)
    @property
    def is_InvalidImportTokenException(self) -> bool:
        return isinstance(self, Error_InvalidImportTokenException)
    @property
    def is_InvalidKeyUsageException(self) -> bool:
        return isinstance(self, Error_InvalidKeyUsageException)
    @property
    def is_InvalidMarkerException(self) -> bool:
        return isinstance(self, Error_InvalidMarkerException)
    @property
    def is_KeyUnavailableException(self) -> bool:
        return isinstance(self, Error_KeyUnavailableException)
    @property
    def is_KMSInternalException(self) -> bool:
        return isinstance(self, Error_KMSInternalException)
    @property
    def is_KMSInvalidMacException(self) -> bool:
        return isinstance(self, Error_KMSInvalidMacException)
    @property
    def is_KMSInvalidSignatureException(self) -> bool:
        return isinstance(self, Error_KMSInvalidSignatureException)
    @property
    def is_KMSInvalidStateException(self) -> bool:
        return isinstance(self, Error_KMSInvalidStateException)
    @property
    def is_LimitExceededException(self) -> bool:
        return isinstance(self, Error_LimitExceededException)
    @property
    def is_MalformedPolicyDocumentException(self) -> bool:
        return isinstance(self, Error_MalformedPolicyDocumentException)
    @property
    def is_NotFoundException(self) -> bool:
        return isinstance(self, Error_NotFoundException)
    @property
    def is_TagException(self) -> bool:
        return isinstance(self, Error_TagException)
    @property
    def is_UnsupportedOperationException(self) -> bool:
        return isinstance(self, Error_UnsupportedOperationException)
    @property
    def is_XksKeyAlreadyInUseException(self) -> bool:
        return isinstance(self, Error_XksKeyAlreadyInUseException)
    @property
    def is_XksKeyInvalidConfigurationException(self) -> bool:
        return isinstance(self, Error_XksKeyInvalidConfigurationException)
    @property
    def is_XksKeyNotFoundException(self) -> bool:
        return isinstance(self, Error_XksKeyNotFoundException)
    @property
    def is_XksProxyIncorrectAuthenticationCredentialException(self) -> bool:
        return isinstance(self, Error_XksProxyIncorrectAuthenticationCredentialException)
    @property
    def is_XksProxyInvalidConfigurationException(self) -> bool:
        return isinstance(self, Error_XksProxyInvalidConfigurationException)
    @property
    def is_XksProxyInvalidResponseException(self) -> bool:
        return isinstance(self, Error_XksProxyInvalidResponseException)
    @property
    def is_XksProxyUriEndpointInUseException(self) -> bool:
        return isinstance(self, Error_XksProxyUriEndpointInUseException)
    @property
    def is_XksProxyUriInUseException(self) -> bool:
        return isinstance(self, Error_XksProxyUriInUseException)
    @property
    def is_XksProxyUriUnreachableException(self) -> bool:
        return isinstance(self, Error_XksProxyUriUnreachableException)
    @property
    def is_XksProxyVpcEndpointServiceInUseException(self) -> bool:
        return isinstance(self, Error_XksProxyVpcEndpointServiceInUseException)
    @property
    def is_XksProxyVpcEndpointServiceInvalidConfigurationException(self) -> bool:
        return isinstance(self, Error_XksProxyVpcEndpointServiceInvalidConfigurationException)
    @property
    def is_XksProxyVpcEndpointServiceNotFoundException(self) -> bool:
        return isinstance(self, Error_XksProxyVpcEndpointServiceNotFoundException)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, Error_Opaque)

class Error_AlreadyExistsException(Error, NamedTuple('AlreadyExistsException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.AlreadyExistsException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_AlreadyExistsException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CloudHsmClusterInUseException(Error, NamedTuple('CloudHsmClusterInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CloudHsmClusterInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CloudHsmClusterInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CloudHsmClusterInvalidConfigurationException(Error, NamedTuple('CloudHsmClusterInvalidConfigurationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CloudHsmClusterInvalidConfigurationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CloudHsmClusterInvalidConfigurationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CloudHsmClusterNotActiveException(Error, NamedTuple('CloudHsmClusterNotActiveException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CloudHsmClusterNotActiveException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CloudHsmClusterNotActiveException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CloudHsmClusterNotFoundException(Error, NamedTuple('CloudHsmClusterNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CloudHsmClusterNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CloudHsmClusterNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CloudHsmClusterNotRelatedException(Error, NamedTuple('CloudHsmClusterNotRelatedException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CloudHsmClusterNotRelatedException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CloudHsmClusterNotRelatedException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ConflictException(Error, NamedTuple('ConflictException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.ConflictException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ConflictException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CustomKeyStoreHasCMKsException(Error, NamedTuple('CustomKeyStoreHasCMKsException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CustomKeyStoreHasCMKsException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CustomKeyStoreHasCMKsException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CustomKeyStoreInvalidStateException(Error, NamedTuple('CustomKeyStoreInvalidStateException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CustomKeyStoreInvalidStateException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CustomKeyStoreInvalidStateException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CustomKeyStoreNameInUseException(Error, NamedTuple('CustomKeyStoreNameInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CustomKeyStoreNameInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CustomKeyStoreNameInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CustomKeyStoreNotFoundException(Error, NamedTuple('CustomKeyStoreNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.CustomKeyStoreNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_CustomKeyStoreNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_DependencyTimeoutException(Error, NamedTuple('DependencyTimeoutException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.DependencyTimeoutException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_DependencyTimeoutException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_DisabledException(Error, NamedTuple('DisabledException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.DisabledException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_DisabledException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_DryRunOperationException(Error, NamedTuple('DryRunOperationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.DryRunOperationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_DryRunOperationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ExpiredImportTokenException(Error, NamedTuple('ExpiredImportTokenException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.ExpiredImportTokenException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_ExpiredImportTokenException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_IncorrectKeyException(Error, NamedTuple('IncorrectKeyException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.IncorrectKeyException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_IncorrectKeyException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_IncorrectKeyMaterialException(Error, NamedTuple('IncorrectKeyMaterialException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.IncorrectKeyMaterialException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_IncorrectKeyMaterialException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_IncorrectTrustAnchorException(Error, NamedTuple('IncorrectTrustAnchorException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.IncorrectTrustAnchorException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_IncorrectTrustAnchorException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAliasNameException(Error, NamedTuple('InvalidAliasNameException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidAliasNameException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidAliasNameException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidArnException(Error, NamedTuple('InvalidArnException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidArnException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidArnException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidCiphertextException(Error, NamedTuple('InvalidCiphertextException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidCiphertextException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidCiphertextException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidGrantIdException(Error, NamedTuple('InvalidGrantIdException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidGrantIdException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidGrantIdException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidGrantTokenException(Error, NamedTuple('InvalidGrantTokenException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidGrantTokenException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidGrantTokenException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidImportTokenException(Error, NamedTuple('InvalidImportTokenException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidImportTokenException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidImportTokenException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidKeyUsageException(Error, NamedTuple('InvalidKeyUsageException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidKeyUsageException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidKeyUsageException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidMarkerException(Error, NamedTuple('InvalidMarkerException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.InvalidMarkerException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_InvalidMarkerException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_KeyUnavailableException(Error, NamedTuple('KeyUnavailableException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.KeyUnavailableException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KeyUnavailableException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_KMSInternalException(Error, NamedTuple('KMSInternalException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.KMSInternalException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KMSInternalException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_KMSInvalidMacException(Error, NamedTuple('KMSInvalidMacException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.KMSInvalidMacException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KMSInvalidMacException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_KMSInvalidSignatureException(Error, NamedTuple('KMSInvalidSignatureException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.KMSInvalidSignatureException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KMSInvalidSignatureException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_KMSInvalidStateException(Error, NamedTuple('KMSInvalidStateException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.KMSInvalidStateException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_KMSInvalidStateException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_LimitExceededException(Error, NamedTuple('LimitExceededException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.LimitExceededException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_LimitExceededException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_MalformedPolicyDocumentException(Error, NamedTuple('MalformedPolicyDocumentException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.MalformedPolicyDocumentException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_MalformedPolicyDocumentException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_NotFoundException(Error, NamedTuple('NotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.NotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_NotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_TagException(Error, NamedTuple('TagException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.TagException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_TagException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_UnsupportedOperationException(Error, NamedTuple('UnsupportedOperationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.UnsupportedOperationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_UnsupportedOperationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksKeyAlreadyInUseException(Error, NamedTuple('XksKeyAlreadyInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksKeyAlreadyInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksKeyAlreadyInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksKeyInvalidConfigurationException(Error, NamedTuple('XksKeyInvalidConfigurationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksKeyInvalidConfigurationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksKeyInvalidConfigurationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksKeyNotFoundException(Error, NamedTuple('XksKeyNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksKeyNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksKeyNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyIncorrectAuthenticationCredentialException(Error, NamedTuple('XksProxyIncorrectAuthenticationCredentialException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyIncorrectAuthenticationCredentialException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyIncorrectAuthenticationCredentialException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyInvalidConfigurationException(Error, NamedTuple('XksProxyInvalidConfigurationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyInvalidConfigurationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyInvalidConfigurationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyInvalidResponseException(Error, NamedTuple('XksProxyInvalidResponseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyInvalidResponseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyInvalidResponseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyUriEndpointInUseException(Error, NamedTuple('XksProxyUriEndpointInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyUriEndpointInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyUriEndpointInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyUriInUseException(Error, NamedTuple('XksProxyUriInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyUriInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyUriInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyUriUnreachableException(Error, NamedTuple('XksProxyUriUnreachableException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyUriUnreachableException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyUriUnreachableException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyVpcEndpointServiceInUseException(Error, NamedTuple('XksProxyVpcEndpointServiceInUseException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyVpcEndpointServiceInUseException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyVpcEndpointServiceInUseException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyVpcEndpointServiceInvalidConfigurationException(Error, NamedTuple('XksProxyVpcEndpointServiceInvalidConfigurationException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyVpcEndpointServiceInvalidConfigurationException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyVpcEndpointServiceInvalidConfigurationException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_XksProxyVpcEndpointServiceNotFoundException(Error, NamedTuple('XksProxyVpcEndpointServiceNotFoundException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.XksProxyVpcEndpointServiceNotFoundException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_XksProxyVpcEndpointServiceNotFoundException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any), ('alt__text', Any)])):
    def __dafnystr__(self) -> str:
        return f'ComAmazonawsKmsTypes.Error.Opaque({_dafny.string_of(self.obj)}, {_dafny.string_of(self.alt__text)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Error_Opaque) and self.obj == __o.obj and self.alt__text == __o.alt__text
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Error.default()()
    def _Is(source__):
        d_7_e_: Error = source__
        return (d_7_e_).is_Opaque
