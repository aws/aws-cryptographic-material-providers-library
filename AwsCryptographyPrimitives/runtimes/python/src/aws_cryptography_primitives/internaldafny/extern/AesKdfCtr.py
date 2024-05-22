from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.exceptions import AlreadyFinalized
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import Error_AwsCryptographicPrimitivesError
import standard_library.internaldafny.generated.Wrappers as Wrappers
import _dafny
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr

# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.AesKdfCtr.default__):

  @staticmethod
  def AesKdfCtrStream(nonce, key, length):
    cipher = Cipher(
        algorithms.AES(bytes(key)), modes.CTR(bytes(nonce)),
    )
    plaintext = bytearray(length)
    encryptor = cipher.encryptor()
    try:
      ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    except ValueError:
      return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
        message="Cannot finalize an encryptor when the plaintext data is not a multiple of the algorithm block size"
      ))
    except AlreadyFinalized:
      return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
        message="Cannot update or finalize an encryptor which was already finalized"
      ))
    return Wrappers.Result_Success(_dafny.Seq(ciphertext))
  
# Export extern-extended class into generated class
aws_cryptography_primitives.internaldafny.generated.AesKdfCtr.default__ = default__