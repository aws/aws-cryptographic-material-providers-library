import boto3
import _dafny

from botocore.config import Config
from boto3.session import Session

from smithy_dafny_standard_library.internaldafny.generated.Wrappers import Option_Some
from aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import DynamoDBClientShim
from aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb import *
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb


# Persist this across calls; this doesn't change
available_aws_regions: list[str] = None

def get_available_aws_regions():
    global available_aws_regions
    if available_aws_regions is not None:
        return available_aws_regions
    available_aws_regions = Session().get_available_regions("dynamodb")
    return available_aws_regions

class default__(aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__):
    @staticmethod
    def DynamoDBClient(boto_client = None, region = None):
        if boto_client is None:
            if region is not None and region in get_available_aws_regions():
                boto_config = Config(
                    region_name=region
                )
                boto_client = boto3.client("dynamodb", config=boto_config)
            else:
                # If no region is provided,
                # boto_client will use the default region provided by boto3
                boto_client = boto3.client("dynamodb")
                region = boto_client.meta.region_name
        wrapped_client = DynamoDBClientShim(boto_client, region)
        return Wrappers.Result_Success(wrapped_client)
    
    @staticmethod
    def DDBClientForRegion(region: _dafny.Seq):
        region_string = _dafny.string_of(region)
        return default__.DynamoDBClient(region=region_string)

    @staticmethod
    def RegionMatch(client, region):
        # We should never be passing anything other than Shim as the 'client'.
        # If this assertion fails, that indicates that there is something wrong with
        # our code generation.
        try:
            assert isinstance(client, DynamoDBClientShim)
        except AssertionError:
            raise TypeError("Client provided to RegionMatch is not a DynamoDBClientShim: " + client)

        # Since client is a DynamoDBClientShim, we can reach into its _impl, which is a boto3 client,
        # then into the client's .meta.region_name attribute
        client_region_name = client._impl.meta.region_name
        return Option_Some(region.VerbatimString(False) == client_region_name)

aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__ = default__
