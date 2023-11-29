import uuid

import Wrappers
import _dafny
from standard_library.internaldafny.generated.UUID import *
import standard_library.internaldafny.generated.UUID

class default__:
    @staticmethod
    def ToByteArray(dafny_str):
        try:
            print(f"{dafny_str.Elements=}")
            uuid_from_str = uuid.UUID(''.join(dafny_str.Elements))
            print(f"{uuid_from_str=}")
            return Wrappers.Result_Success(_dafny.Seq(uuid_from_str.bytes))
        except Exception as e:
            return Wrappers.Result_Failure(_dafny.string_of(
                "Could not convert UUID to byte array: " + str(e)
            ))
        
    @staticmethod
    def FromByteArray(dafny_b):
        pass

    @staticmethod
    def GenerateUUID():
        try:
            generated_uuid = uuid.uuid4()
            return Wrappers.Result_Success(_dafny.Seq(str(generated_uuid)))
        except Exception as e:
            return Wrappers.Result_Failure(_dafny.Seq("Could not generate a UUID: " + str(e)))

standard_library.internaldafny.generated.UUID.default__ = default__