import uuid

import Wrappers
import _dafny
from standard_library.internal_generated_dafny.UUID import *
import standard_library.internal_generated_dafny.UUID

class default__:
    @staticmethod
    def GenerateUUID():
        try:
            generated_uuid = uuid.uuid4()
            return Wrappers.Result_Success(_dafny.Seq(str(generated_uuid)))
        except Exception as e:
            return Wrappers.Result_Failure(_dafny.Seq("Could not generate a UUID: " + str(e)))

standard_library.internal_generated_dafny.UUID.default__ = default__