from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.ciphers import Cipher
import Wrappers
import _dafny

class default__:

  @staticmethod
  def AesKdfCtrStream(nonce, key, length):
    cipher = Cipher(
        algorithms.AES(bytes(key)), modes.CTR(bytes(nonce)),
    )
    plaintext = bytearray(length)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return Wrappers.Result_Success(_dafny.Seq(ciphertext))