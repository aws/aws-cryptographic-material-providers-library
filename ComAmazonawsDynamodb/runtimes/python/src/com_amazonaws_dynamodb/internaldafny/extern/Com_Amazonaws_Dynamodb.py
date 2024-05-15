import module_
from standard_library.internaldafny.generated.Wrappers import Option_None, Option_Some
from com_amazonaws_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import DynamoDBClientShim
from com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb import *
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb
import _dafny

import boto3
from botocore.config import Config

def get_available_aws_regions():
    from boto3.session import Session
    s = Session()
    return s.get_available_regions("dynamodb")

class default__(com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__):
    @staticmethod
    def DynamoDBClient(boto_client = None, region = None):
        if boto_client is None:
            if region is not None and region in get_available_aws_regions():
                boto_config = Config(
                    region_name=region
                )
                boto_client = boto3.client("dynamodb", config=boto_config)
            else:
                boto_client = boto3.client("dynamodb")
                region = boto3.session.Session().region_name
        wrapped_client = DynamoDBClientShim(boto_client, region)
        return Wrappers.Result_Success(wrapped_client)
    
    @staticmethod
    def DDBClientForRegion(region: _dafny.Seq):
        return default__.DynamoDBClient(region = _dafny.string_of(region))

    @staticmethod
    def RegionMatch(client, region):
        # We should never be passing anything other than Shim as the 'client'.
        # If this assertion fails, that indicates that there is something wrong with
        # our code generation.
        try:
            assert isinstance(client, DynamoDBClientShim)
        except AssertionError:
            raise TypeError("Client provided to RegionMatch is not a DynamoDBClientShim: " + client)

        # Since client is a DynamoDBClientShim, we can reach into its _impl, which is a boto3 client
        client_region_name = client._impl.meta.region_name
        return Option_Some(region.VerbatimString(False) == client_region_name)

com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__ = default__
com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.DynamoDBClient = default__.DynamoDBClient
com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.DDBClientForRegion = default__.DDBClientForRegion