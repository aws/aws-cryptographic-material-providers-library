#![allow(warnings, unconditional_panic)]
#![allow(nonstandard_style)]

pub mod aes_gcm;
pub mod aes_kdf_ctr;
pub mod digest;
pub mod ecdh;
pub mod ecdsa;
pub mod hmac;
pub mod random;
pub mod rsa;
pub mod _dafny_externs {
    pub use crate::aes_gcm::*;
    pub use crate::aes_kdf_ctr::*;
    pub use crate::digest::*;
    pub use crate::ecdh::*;
    pub use crate::ecdsa::*;
    pub use crate::hmac::*;
    pub use crate::random::*;
    pub use crate::rsa::*;
}
pub mod AESEncryption {
  pub struct _default {}

  impl _default {
    pub fn EncryptionOutputFromByteSeq(s: &::dafny_runtime::Sequence<u8>, encAlg: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM>) -> ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput> {
      let mut cipherText: ::dafny_runtime::Sequence<u8> = s.take(&(s.cardinality() - ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(encAlg.tagLength().clone())));
      let mut authTag: ::dafny_runtime::Sequence<u8> = s.drop(&(s.cardinality() - ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(encAlg.tagLength().clone())));
      ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput::AESEncryptOutput {
          cipherText: cipherText.clone(),
          authTag: authTag.clone()
        })
    }
    pub fn AESEncrypt(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(input.iv().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.encAlg().ivLength().clone()) && input.key().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.encAlg().keyLength().clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Request does not match algorithm.")
              })));
      if valueOrError0.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>>());
        return res.read();
      };
      let mut r#__let_tmp_rhs0: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput> = input.clone();
      let mut encAlg: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM> = r#__let_tmp_rhs0.encAlg().clone();
      let mut iv: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.iv().clone();
      let mut key: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.key().clone();
      let mut msg: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.msg().clone();
      let mut aad: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.aad().clone();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      let mut _out0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      _out0 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::AESEncryption::AES_GCM::AESEncryptExtern(&encAlg, &iv, &key, &msg, &aad));
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out0.read());
      if valueOrError1.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>>());
        return res.read();
      };
      let mut value: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput> = valueOrError1.read().Extract();
      let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError2 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(value.cipherText().cardinality() == msg.cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("AESEncrypt did not return cipherText of expected length")
              })));
      if valueOrError2.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError2.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>>());
        return res.read();
      };
      let mut valueOrError3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError3 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(value.authTag().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(encAlg.tagLength().clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("AESEncryption did not return valid tag")
              })));
      if valueOrError3.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError3.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>>());
        return res.read();
      };
      res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: value.clone()
            }));
      return res.read();
    }
    pub fn AESDecrypt(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(input.key().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.encAlg().keyLength().clone()) && input.iv().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.encAlg().ivLength().clone()) && input.authTag().cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.encAlg().tagLength().clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Request does not match algorithm.")
              })));
      if valueOrError0.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      let mut r#__let_tmp_rhs1: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput> = input.clone();
      let mut encAlg: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM> = r#__let_tmp_rhs1.encAlg().clone();
      let mut key: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.key().clone();
      let mut cipherTxt: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.cipherTxt().clone();
      let mut authTag: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.authTag().clone();
      let mut iv: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.iv().clone();
      let mut aad: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.aad().clone();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      let mut _out1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      _out1 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::AESEncryption::AES_GCM::AESDecryptExtern(&encAlg, &key, &cipherTxt, &authTag, &iv, &aad));
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out1.read());
      if valueOrError1.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      let mut value: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
      let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError2 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(cipherTxt.cardinality() == value.cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("AESDecrypt did not return plaintext of expected length")
              })));
      if valueOrError2.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError2.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: value.clone()
            }));
      return res.read();
    }
    pub fn CreateAESEncryptExternSuccess(output: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>::Success {
          value: output.clone()
        })
    }
    pub fn CreateAESEncryptExternFailure(error: &crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateAESDecryptExternSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateAESDecryptExternFailure(error: &crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>::Failure {
          error: error.clone()
        })
    }
  }
}
pub mod AesKdfCtr {
  pub struct _default {}

  impl _default {
    pub fn CreateStreamSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateStreamFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }
}
pub mod r#_Aws_Compile {
  pub mod r#_Cryptography_Compile {
    
  }
}
pub mod software {
  pub mod amazon {
    pub mod cryptography {
      pub mod primitives {
        pub mod internaldafny {
          pub use ::dafny_runtime::UpcastObject;
          pub use ::std::any::Any;
          pub use crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient;

          pub struct _default {}

          impl _default {
            pub fn DefaultCryptoConfig() -> ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CryptoConfig> {
              ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::CryptoConfig::CryptoConfig {})
            }
            pub fn AtomicPrimitives(config: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CryptoConfig>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut client = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>>::new();
              let mut _nw0: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient::_allocate_object();
              crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient::_ctor(&_nw0, &::std::rc::Rc::new(crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config::Config {}));
              client = ::dafny_runtime::MaybePlacebo::from(_nw0.clone());
              res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
                      value: client.read()
                    }));
              return res.read();
            }
            pub fn CreateSuccessOfClient(client: &::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
                  value: client.clone()
                })
            }
            pub fn CreateFailureOfError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
                  error: error.clone()
                })
            }
          }

          #[derive(Debug)]
          pub struct AtomicPrimitivesClient {
            pub r#__i_config: ::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>
          }

          impl AtomicPrimitivesClient {
            pub fn _allocate_object() -> ::dafny_runtime::Object<Self> {
              ::dafny_runtime::allocate_object::<Self>()
            }
            pub fn _ctor(this: &::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>) -> () {
              let mut _set__i_config: bool = false;
              ::dafny_runtime::update_field_uninit_object!(this.clone(), r#__i_config, _set__i_config, config.clone());
              return ();
            }
            pub fn config(&self) -> ::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config> {
              self.r#__i_config.clone()
            }
          }

          impl UpcastObject<dyn Any>
            for crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient {
            ::dafny_runtime::UpcastObjectFn!(dyn ::std::any::Any);
          }

          impl IAwsCryptographicPrimitivesClient
            for crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient {
            fn GenerateRandomBytes(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRandomBytesInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out2 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GenerateRandomBytes(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out2.read());
              return output.read();
            }
            fn Digest(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out3 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::Digest(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out3.read());
              return output.read();
            }
            fn HMac(&self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::HMac(&self.config().clone(), input)
            }
            fn HkdfExtract(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out4 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out4 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::HkdfExtract(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out4.read());
              return output.read();
            }
            fn HkdfExpand(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out5 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out5 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::HkdfExpand(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out5.read());
              return output.read();
            }
            fn Hkdf(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out6 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out6 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::Hkdf(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out6.read());
              return output.read();
            }
            fn KdfCounterMode(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out7 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out7 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::KdfCounterMode(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out7.read());
              return output.read();
            }
            fn AesKdfCounterMode(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AesKdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out8 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out8 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::AesKdfCounterMode(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out8.read());
              return output.read();
            }
            fn AESEncrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out9 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out9 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::AESEncrypt(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out9.read());
              return output.read();
            }
            fn AESDecrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out10 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out10 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::AESDecrypt(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out10.read());
              return output.read();
            }
            fn GenerateRSAKeyPair(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out11 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out11 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GenerateRSAKeyPair(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out11.read());
              return output.read();
            }
            fn GetRSAKeyModulusLength(&self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GetRSAKeyModulusLength(&self.config().clone(), input)
            }
            fn RSADecrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out12 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out12 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::RSADecrypt(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out12.read());
              return output.read();
            }
            fn RSAEncrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out13 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out13 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::RSAEncrypt(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out13.read());
              return output.read();
            }
            fn GenerateECDSASignatureKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out14 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out14 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GenerateECDSASignatureKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out14.read());
              return output.read();
            }
            fn ECDSASign(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out15 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out15 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::ECDSASign(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out15.read());
              return output.read();
            }
            fn ECDSAVerify(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSAVerifyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out16 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out16 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::ECDSAVerify(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out16.read());
              return output.read();
            }
            fn GenerateECCKeyPair(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out17 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out17 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GenerateECCKeyPair(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out17.read());
              return output.read();
            }
            fn GetPublicKeyFromPrivateKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out18 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out18 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::GetPublicKeyFromPrivateKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out18.read());
              return output.read();
            }
            fn ValidatePublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out19 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out19 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::ValidatePublicKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out19.read());
              return output.read();
            }
            fn DeriveSharedSecret(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out20 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out20 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::DeriveSharedSecret(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out20.read());
              return output.read();
            }
            fn CompressPublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out21 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out21 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::CompressPublicKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out21.read());
              return output.read();
            }
            fn DecompressPublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out22 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out22 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::DecompressPublicKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out22.read());
              return output.read();
            }
            fn ParsePublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
              let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              let mut _out23 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
              _out23 = ::dafny_runtime::MaybePlacebo::from(crate::r#_AwsCryptographyPrimitivesOperations_Compile::_default::ParsePublicKey(&self.config().clone(), input));
              output = ::dafny_runtime::MaybePlacebo::from(_out23.read());
              return output.read();
            }
          }

          impl UpcastObject<dyn IAwsCryptographicPrimitivesClient>
            for crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient {
            ::dafny_runtime::UpcastObjectFn!(dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient);
          }

          pub mod types {
            pub use ::std::fmt::Debug;
            pub use ::dafny_runtime::DafnyPrint;
            pub use ::std::cmp::Eq;
            pub use ::std::hash::Hash;
            pub use ::std::default::Default;
            pub use ::std::convert::AsRef;
            pub use ::dafny_runtime::UpcastObject;
            pub use ::std::any::Any;

            pub struct _default {}

            impl _default {
              pub fn IsValid_PositiveInteger(x: i32) -> bool {
                0 <= x
              }
              pub fn IsValid_RSAModulusLengthBits(x: i32) -> bool {
                81 <= x
              }
              pub fn IsValid_RSAModulusLengthBitsToGenerate(x: i32) -> bool {
                81 <= x && x <= 4096
              }
              pub fn IsValid_SymmetricKeyLength(x: i32) -> bool {
                1 <= x && x <= 32
              }
              pub fn IsValid_Uint8Bits(x: i32) -> bool {
                0 <= x && x <= 255
              }
              pub fn IsValid_Uint8Bytes(x: i32) -> bool {
                0 <= x && x <= 32
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DafnyCallEvent<I: ::dafny_runtime::DafnyType, O: ::dafny_runtime::DafnyType> {
              DafnyCallEvent {
                input: I,
                output: O
              }
            }

            impl<I: ::dafny_runtime::DafnyType, O: ::dafny_runtime::DafnyType> DafnyCallEvent<I, O> {
              pub fn input(&self) -> &I {
                match self {
                  DafnyCallEvent::DafnyCallEvent{input, output, } => input,
                }
              }
              pub fn output(&self) -> &O {
                match self {
                  DafnyCallEvent::DafnyCallEvent{input, output, } => output,
                }
              }
            }

            impl<I: ::dafny_runtime::DafnyType, O: ::dafny_runtime::DafnyType> Debug
              for DafnyCallEvent<I, O> {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl<I: ::dafny_runtime::DafnyType, O: ::dafny_runtime::DafnyType> DafnyPrint
              for DafnyCallEvent<I, O> {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DafnyCallEvent::DafnyCallEvent{input, output, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DafnyCallEvent.DafnyCallEvent(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(input, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(output, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl<I: ::dafny_runtime::DafnyType + Eq, O: ::dafny_runtime::DafnyType + Eq> Eq
              for DafnyCallEvent<I, O> {}

            impl<I: ::dafny_runtime::DafnyType + Hash, O: ::dafny_runtime::DafnyType + Hash> Hash
              for DafnyCallEvent<I, O> {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DafnyCallEvent::DafnyCallEvent{input, output, } => {
                    ::std::hash::Hash::hash(input, _state);
                    ::std::hash::Hash::hash(output, _state)
                  },
                }
              }
            }

            impl<I: ::dafny_runtime::DafnyType + Default, O: ::dafny_runtime::DafnyType + Default> Default
              for DafnyCallEvent<I, O> {
              fn default() -> DafnyCallEvent<I, O> {
                DafnyCallEvent::DafnyCallEvent {
                  input: ::std::default::Default::default(),
                  output: ::std::default::Default::default()
                }
              }
            }

            impl<I: ::dafny_runtime::DafnyType, O: ::dafny_runtime::DafnyType> AsRef<DafnyCallEvent<I, O>>
              for &DafnyCallEvent<I, O> {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AES_CTR {
              AES_CTR {
                keyLength: crate::software::amazon::cryptography::primitives::internaldafny::types::SymmetricKeyLength,
                nonceLength: crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bits
              }
            }

            impl AES_CTR {
              pub fn keyLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::SymmetricKeyLength {
                match self {
                  AES_CTR::AES_CTR{keyLength, nonceLength, } => keyLength,
                }
              }
              pub fn nonceLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bits {
                match self {
                  AES_CTR::AES_CTR{keyLength, nonceLength, } => nonceLength,
                }
              }
            }

            impl Debug
              for AES_CTR {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AES_CTR {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AES_CTR::AES_CTR{keyLength, nonceLength, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AES__CTR.AES__CTR(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(keyLength, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(nonceLength, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AES_CTR {}

            impl Hash
              for AES_CTR {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AES_CTR::AES_CTR{keyLength, nonceLength, } => {
                    ::std::hash::Hash::hash(keyLength, _state);
                    ::std::hash::Hash::hash(nonceLength, _state)
                  },
                }
              }
            }

            impl Default
              for AES_CTR {
              fn default() -> AES_CTR {
                AES_CTR::AES_CTR {
                  keyLength: ::std::default::Default::default(),
                  nonceLength: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AES_CTR>
              for &AES_CTR {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AES_GCM {
              AES_GCM {
                keyLength: crate::software::amazon::cryptography::primitives::internaldafny::types::SymmetricKeyLength,
                tagLength: crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bytes,
                ivLength: crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bits
              }
            }

            impl AES_GCM {
              pub fn keyLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::SymmetricKeyLength {
                match self {
                  AES_GCM::AES_GCM{keyLength, tagLength, ivLength, } => keyLength,
                }
              }
              pub fn tagLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bytes {
                match self {
                  AES_GCM::AES_GCM{keyLength, tagLength, ivLength, } => tagLength,
                }
              }
              pub fn ivLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::Uint8Bits {
                match self {
                  AES_GCM::AES_GCM{keyLength, tagLength, ivLength, } => ivLength,
                }
              }
            }

            impl Debug
              for AES_GCM {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AES_GCM {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AES_GCM::AES_GCM{keyLength, tagLength, ivLength, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.AES__GCM(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(keyLength, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(tagLength, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(ivLength, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AES_GCM {}

            impl Hash
              for AES_GCM {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AES_GCM::AES_GCM{keyLength, tagLength, ivLength, } => {
                    ::std::hash::Hash::hash(keyLength, _state);
                    ::std::hash::Hash::hash(tagLength, _state);
                    ::std::hash::Hash::hash(ivLength, _state)
                  },
                }
              }
            }

            impl Default
              for AES_GCM {
              fn default() -> AES_GCM {
                AES_GCM::AES_GCM {
                  keyLength: ::std::default::Default::default(),
                  tagLength: ::std::default::Default::default(),
                  ivLength: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AES_GCM>
              for &AES_GCM {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AESDecryptInput {
              AESDecryptInput {
                encAlg: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM>,
                key: ::dafny_runtime::Sequence<u8>,
                cipherTxt: ::dafny_runtime::Sequence<u8>,
                authTag: ::dafny_runtime::Sequence<u8>,
                iv: ::dafny_runtime::Sequence<u8>,
                aad: ::dafny_runtime::Sequence<u8>
              }
            }

            impl AESDecryptInput {
              pub fn encAlg(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => encAlg,
                }
              }
              pub fn key(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => key,
                }
              }
              pub fn cipherTxt(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => cipherTxt,
                }
              }
              pub fn authTag(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => authTag,
                }
              }
              pub fn iv(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => iv,
                }
              }
              pub fn aad(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => aad,
                }
              }
            }

            impl Debug
              for AESDecryptInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AESDecryptInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput.AESDecryptInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(encAlg, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(key, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(cipherTxt, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(authTag, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(iv, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(aad, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AESDecryptInput {}

            impl Hash
              for AESDecryptInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AESDecryptInput::AESDecryptInput{encAlg, key, cipherTxt, authTag, iv, aad, } => {
                    ::std::hash::Hash::hash(encAlg, _state);
                    ::std::hash::Hash::hash(key, _state);
                    ::std::hash::Hash::hash(cipherTxt, _state);
                    ::std::hash::Hash::hash(authTag, _state);
                    ::std::hash::Hash::hash(iv, _state);
                    ::std::hash::Hash::hash(aad, _state)
                  },
                }
              }
            }

            impl Default
              for AESDecryptInput {
              fn default() -> AESDecryptInput {
                AESDecryptInput::AESDecryptInput {
                  encAlg: ::std::default::Default::default(),
                  key: ::std::default::Default::default(),
                  cipherTxt: ::std::default::Default::default(),
                  authTag: ::std::default::Default::default(),
                  iv: ::std::default::Default::default(),
                  aad: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AESDecryptInput>
              for &AESDecryptInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AESEncryptInput {
              AESEncryptInput {
                encAlg: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM>,
                iv: ::dafny_runtime::Sequence<u8>,
                key: ::dafny_runtime::Sequence<u8>,
                msg: ::dafny_runtime::Sequence<u8>,
                aad: ::dafny_runtime::Sequence<u8>
              }
            }

            impl AESEncryptInput {
              pub fn encAlg(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM> {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => encAlg,
                }
              }
              pub fn iv(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => iv,
                }
              }
              pub fn key(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => key,
                }
              }
              pub fn msg(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => msg,
                }
              }
              pub fn aad(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => aad,
                }
              }
            }

            impl Debug
              for AESEncryptInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AESEncryptInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput.AESEncryptInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(encAlg, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(iv, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(key, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(msg, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(aad, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AESEncryptInput {}

            impl Hash
              for AESEncryptInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AESEncryptInput::AESEncryptInput{encAlg, iv, key, msg, aad, } => {
                    ::std::hash::Hash::hash(encAlg, _state);
                    ::std::hash::Hash::hash(iv, _state);
                    ::std::hash::Hash::hash(key, _state);
                    ::std::hash::Hash::hash(msg, _state);
                    ::std::hash::Hash::hash(aad, _state)
                  },
                }
              }
            }

            impl Default
              for AESEncryptInput {
              fn default() -> AESEncryptInput {
                AESEncryptInput::AESEncryptInput {
                  encAlg: ::std::default::Default::default(),
                  iv: ::std::default::Default::default(),
                  key: ::std::default::Default::default(),
                  msg: ::std::default::Default::default(),
                  aad: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AESEncryptInput>
              for &AESEncryptInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AESEncryptOutput {
              AESEncryptOutput {
                cipherText: ::dafny_runtime::Sequence<u8>,
                authTag: ::dafny_runtime::Sequence<u8>
              }
            }

            impl AESEncryptOutput {
              pub fn cipherText(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptOutput::AESEncryptOutput{cipherText, authTag, } => cipherText,
                }
              }
              pub fn authTag(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AESEncryptOutput::AESEncryptOutput{cipherText, authTag, } => authTag,
                }
              }
            }

            impl Debug
              for AESEncryptOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AESEncryptOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AESEncryptOutput::AESEncryptOutput{cipherText, authTag, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.AESEncryptOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(cipherText, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(authTag, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AESEncryptOutput {}

            impl Hash
              for AESEncryptOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AESEncryptOutput::AESEncryptOutput{cipherText, authTag, } => {
                    ::std::hash::Hash::hash(cipherText, _state);
                    ::std::hash::Hash::hash(authTag, _state)
                  },
                }
              }
            }

            impl Default
              for AESEncryptOutput {
              fn default() -> AESEncryptOutput {
                AESEncryptOutput::AESEncryptOutput {
                  cipherText: ::std::default::Default::default(),
                  authTag: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AESEncryptOutput>
              for &AESEncryptOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum AesKdfCtrInput {
              AesKdfCtrInput {
                ikm: ::dafny_runtime::Sequence<u8>,
                expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
                nonce: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>
              }
            }

            impl AesKdfCtrInput {
              pub fn ikm(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  AesKdfCtrInput::AesKdfCtrInput{ikm, expectedLength, nonce, } => ikm,
                }
              }
              pub fn expectedLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger {
                match self {
                  AesKdfCtrInput::AesKdfCtrInput{ikm, expectedLength, nonce, } => expectedLength,
                }
              }
              pub fn nonce(&self) -> &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> {
                match self {
                  AesKdfCtrInput::AesKdfCtrInput{ikm, expectedLength, nonce, } => nonce,
                }
              }
            }

            impl Debug
              for AesKdfCtrInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for AesKdfCtrInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  AesKdfCtrInput::AesKdfCtrInput{ikm, expectedLength, nonce, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.AesKdfCtrInput.AesKdfCtrInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(ikm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(expectedLength, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(nonce, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for AesKdfCtrInput {}

            impl Hash
              for AesKdfCtrInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  AesKdfCtrInput::AesKdfCtrInput{ikm, expectedLength, nonce, } => {
                    ::std::hash::Hash::hash(ikm, _state);
                    ::std::hash::Hash::hash(expectedLength, _state);
                    ::std::hash::Hash::hash(nonce, _state)
                  },
                }
              }
            }

            impl Default
              for AesKdfCtrInput {
              fn default() -> AesKdfCtrInput {
                AesKdfCtrInput::AesKdfCtrInput {
                  ikm: ::std::default::Default::default(),
                  expectedLength: ::std::default::Default::default(),
                  nonce: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<AesKdfCtrInput>
              for &AesKdfCtrInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            pub struct IAwsCryptographicPrimitivesClientCallHistory {}

            impl IAwsCryptographicPrimitivesClientCallHistory {
              pub fn _allocate_object() -> ::dafny_runtime::Object<Self> {
                ::dafny_runtime::allocate_object::<Self>()
              }
            }

            impl UpcastObject<dyn Any>
              for crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClientCallHistory {
              ::dafny_runtime::UpcastObjectFn!(dyn ::std::any::Any);
            }

            pub trait IAwsCryptographicPrimitivesClient: ::std::any::Any + ::dafny_runtime::UpcastObject<dyn ::std::any::Any> {
              fn GenerateRandomBytes(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRandomBytesInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn Digest(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn HMac(&self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn HkdfExtract(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn HkdfExpand(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn Hkdf(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn KdfCounterMode(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn AesKdfCounterMode(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AesKdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn AESEncrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn AESDecrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn GenerateRSAKeyPair(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn GetRSAKeyModulusLength(&self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn RSADecrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn RSAEncrypt(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn GenerateECDSASignatureKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn ECDSASign(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn ECDSAVerify(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSAVerifyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn GenerateECCKeyPair(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn GetPublicKeyFromPrivateKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn ValidatePublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn DeriveSharedSecret(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn CompressPublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn DecompressPublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
              fn ParsePublicKey(&mut self, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>;
            }

            #[derive(PartialEq, Clone)]
            pub enum CompressPublicKeyInput {
              CompressPublicKeyInput {
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey>,
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>
              }
            }

            impl CompressPublicKeyInput {
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> {
                match self {
                  CompressPublicKeyInput::CompressPublicKeyInput{publicKey, eccCurve, } => publicKey,
                }
              }
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  CompressPublicKeyInput::CompressPublicKeyInput{publicKey, eccCurve, } => eccCurve,
                }
              }
            }

            impl Debug
              for CompressPublicKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for CompressPublicKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  CompressPublicKeyInput::CompressPublicKeyInput{publicKey, eccCurve, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput.CompressPublicKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for CompressPublicKeyInput {}

            impl Hash
              for CompressPublicKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  CompressPublicKeyInput::CompressPublicKeyInput{publicKey, eccCurve, } => {
                    ::std::hash::Hash::hash(publicKey, _state);
                    ::std::hash::Hash::hash(eccCurve, _state)
                  },
                }
              }
            }

            impl Default
              for CompressPublicKeyInput {
              fn default() -> CompressPublicKeyInput {
                CompressPublicKeyInput::CompressPublicKeyInput {
                  publicKey: ::std::default::Default::default(),
                  eccCurve: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<CompressPublicKeyInput>
              for &CompressPublicKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum CompressPublicKeyOutput {
              CompressPublicKeyOutput {
                compressedPublicKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl CompressPublicKeyOutput {
              pub fn compressedPublicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  CompressPublicKeyOutput::CompressPublicKeyOutput{compressedPublicKey, } => compressedPublicKey,
                }
              }
            }

            impl Debug
              for CompressPublicKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for CompressPublicKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  CompressPublicKeyOutput::CompressPublicKeyOutput{compressedPublicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.CompressPublicKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(compressedPublicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for CompressPublicKeyOutput {}

            impl Hash
              for CompressPublicKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  CompressPublicKeyOutput::CompressPublicKeyOutput{compressedPublicKey, } => {
                    ::std::hash::Hash::hash(compressedPublicKey, _state)
                  },
                }
              }
            }

            impl Default
              for CompressPublicKeyOutput {
              fn default() -> CompressPublicKeyOutput {
                CompressPublicKeyOutput::CompressPublicKeyOutput {
                  compressedPublicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<CompressPublicKeyOutput>
              for &CompressPublicKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum CryptoConfig {
              CryptoConfig {}
            }

            impl CryptoConfig {}

            impl Debug
              for CryptoConfig {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for CryptoConfig {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  CryptoConfig::CryptoConfig{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.CryptoConfig.CryptoConfig")?;
                    Ok(())
                  },
                }
              }
            }

            impl CryptoConfig {
              pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<CryptoConfig>> {
                ::dafny_runtime::seq![::std::rc::Rc::new(CryptoConfig::CryptoConfig {})].iter()
              }
            }

            impl Eq
              for CryptoConfig {}

            impl Hash
              for CryptoConfig {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  CryptoConfig::CryptoConfig{} => {
                    
                  },
                }
              }
            }

            impl Default
              for CryptoConfig {
              fn default() -> CryptoConfig {
                CryptoConfig::CryptoConfig {}
              }
            }

            impl AsRef<CryptoConfig>
              for &CryptoConfig {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DecompressPublicKeyInput {
              DecompressPublicKeyInput {
                compressedPublicKey: ::dafny_runtime::Sequence<u8>,
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>
              }
            }

            impl DecompressPublicKeyInput {
              pub fn compressedPublicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  DecompressPublicKeyInput::DecompressPublicKeyInput{compressedPublicKey, eccCurve, } => compressedPublicKey,
                }
              }
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  DecompressPublicKeyInput::DecompressPublicKeyInput{compressedPublicKey, eccCurve, } => eccCurve,
                }
              }
            }

            impl Debug
              for DecompressPublicKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DecompressPublicKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DecompressPublicKeyInput::DecompressPublicKeyInput{compressedPublicKey, eccCurve, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput.DecompressPublicKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(compressedPublicKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for DecompressPublicKeyInput {}

            impl Hash
              for DecompressPublicKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DecompressPublicKeyInput::DecompressPublicKeyInput{compressedPublicKey, eccCurve, } => {
                    ::std::hash::Hash::hash(compressedPublicKey, _state);
                    ::std::hash::Hash::hash(eccCurve, _state)
                  },
                }
              }
            }

            impl Default
              for DecompressPublicKeyInput {
              fn default() -> DecompressPublicKeyInput {
                DecompressPublicKeyInput::DecompressPublicKeyInput {
                  compressedPublicKey: ::std::default::Default::default(),
                  eccCurve: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<DecompressPublicKeyInput>
              for &DecompressPublicKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DecompressPublicKeyOutput {
              DecompressPublicKeyOutput {
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey>
              }
            }

            impl DecompressPublicKeyOutput {
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> {
                match self {
                  DecompressPublicKeyOutput::DecompressPublicKeyOutput{publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for DecompressPublicKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DecompressPublicKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DecompressPublicKeyOutput::DecompressPublicKeyOutput{publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.DecompressPublicKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for DecompressPublicKeyOutput {}

            impl Hash
              for DecompressPublicKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DecompressPublicKeyOutput::DecompressPublicKeyOutput{publicKey, } => {
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for DecompressPublicKeyOutput {
              fn default() -> DecompressPublicKeyOutput {
                DecompressPublicKeyOutput::DecompressPublicKeyOutput {
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<DecompressPublicKeyOutput>
              for &DecompressPublicKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DeriveSharedSecretInput {
              DeriveSharedSecretInput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>,
                privateKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey>,
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey>
              }
            }

            impl DeriveSharedSecretInput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  DeriveSharedSecretInput::DeriveSharedSecretInput{eccCurve, privateKey, publicKey, } => eccCurve,
                }
              }
              pub fn privateKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey> {
                match self {
                  DeriveSharedSecretInput::DeriveSharedSecretInput{eccCurve, privateKey, publicKey, } => privateKey,
                }
              }
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> {
                match self {
                  DeriveSharedSecretInput::DeriveSharedSecretInput{eccCurve, privateKey, publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for DeriveSharedSecretInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DeriveSharedSecretInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DeriveSharedSecretInput::DeriveSharedSecretInput{eccCurve, privateKey, publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput.DeriveSharedSecretInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for DeriveSharedSecretInput {}

            impl Hash
              for DeriveSharedSecretInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DeriveSharedSecretInput::DeriveSharedSecretInput{eccCurve, privateKey, publicKey, } => {
                    ::std::hash::Hash::hash(eccCurve, _state);
                    ::std::hash::Hash::hash(privateKey, _state);
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for DeriveSharedSecretInput {
              fn default() -> DeriveSharedSecretInput {
                DeriveSharedSecretInput::DeriveSharedSecretInput {
                  eccCurve: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default(),
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<DeriveSharedSecretInput>
              for &DeriveSharedSecretInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DeriveSharedSecretOutput {
              DeriveSharedSecretOutput {
                sharedSecret: ::dafny_runtime::Sequence<u8>
              }
            }

            impl DeriveSharedSecretOutput {
              pub fn sharedSecret(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  DeriveSharedSecretOutput::DeriveSharedSecretOutput{sharedSecret, } => sharedSecret,
                }
              }
            }

            impl Debug
              for DeriveSharedSecretOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DeriveSharedSecretOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DeriveSharedSecretOutput::DeriveSharedSecretOutput{sharedSecret, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.DeriveSharedSecretOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(sharedSecret, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for DeriveSharedSecretOutput {}

            impl Hash
              for DeriveSharedSecretOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DeriveSharedSecretOutput::DeriveSharedSecretOutput{sharedSecret, } => {
                    ::std::hash::Hash::hash(sharedSecret, _state)
                  },
                }
              }
            }

            impl Default
              for DeriveSharedSecretOutput {
              fn default() -> DeriveSharedSecretOutput {
                DeriveSharedSecretOutput::DeriveSharedSecretOutput {
                  sharedSecret: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<DeriveSharedSecretOutput>
              for &DeriveSharedSecretOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DigestAlgorithm {
              SHA_512 {},
              SHA_384 {},
              SHA_256 {}
            }

            impl DigestAlgorithm {}

            impl Debug
              for DigestAlgorithm {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DigestAlgorithm {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DigestAlgorithm::SHA_512{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.SHA__512")?;
                    Ok(())
                  },
                  DigestAlgorithm::SHA_384{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.SHA__384")?;
                    Ok(())
                  },
                  DigestAlgorithm::SHA_256{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.SHA__256")?;
                    Ok(())
                  },
                }
              }
            }

            impl DigestAlgorithm {
              pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<DigestAlgorithm>> {
                ::dafny_runtime::seq![::std::rc::Rc::new(DigestAlgorithm::SHA_512 {}), ::std::rc::Rc::new(DigestAlgorithm::SHA_384 {}), ::std::rc::Rc::new(DigestAlgorithm::SHA_256 {})].iter()
              }
            }

            impl Eq
              for DigestAlgorithm {}

            impl Hash
              for DigestAlgorithm {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DigestAlgorithm::SHA_512{} => {
                    
                  },
                  DigestAlgorithm::SHA_384{} => {
                    
                  },
                  DigestAlgorithm::SHA_256{} => {
                    
                  },
                }
              }
            }

            impl Default
              for DigestAlgorithm {
              fn default() -> DigestAlgorithm {
                DigestAlgorithm::SHA_512 {}
              }
            }

            impl AsRef<DigestAlgorithm>
              for &DigestAlgorithm {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum DigestInput {
              DigestInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                message: ::dafny_runtime::Sequence<u8>
              }
            }

            impl DigestInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  DigestInput::DigestInput{digestAlgorithm, message, } => digestAlgorithm,
                }
              }
              pub fn message(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  DigestInput::DigestInput{digestAlgorithm, message, } => message,
                }
              }
            }

            impl Debug
              for DigestInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for DigestInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  DigestInput::DigestInput{digestAlgorithm, message, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.DigestInput.DigestInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for DigestInput {}

            impl Hash
              for DigestInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  DigestInput::DigestInput{digestAlgorithm, message, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(message, _state)
                  },
                }
              }
            }

            impl Default
              for DigestInput {
              fn default() -> DigestInput {
                DigestInput::DigestInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  message: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<DigestInput>
              for &DigestInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECCPrivateKey {
              ECCPrivateKey {
                pem: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ECCPrivateKey {
              pub fn pem(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECCPrivateKey::ECCPrivateKey{pem, } => pem,
                }
              }
            }

            impl Debug
              for ECCPrivateKey {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECCPrivateKey {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECCPrivateKey::ECCPrivateKey{pem, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.ECCPrivateKey(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(pem, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ECCPrivateKey {}

            impl Hash
              for ECCPrivateKey {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECCPrivateKey::ECCPrivateKey{pem, } => {
                    ::std::hash::Hash::hash(pem, _state)
                  },
                }
              }
            }

            impl Default
              for ECCPrivateKey {
              fn default() -> ECCPrivateKey {
                ECCPrivateKey::ECCPrivateKey {
                  pem: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ECCPrivateKey>
              for &ECCPrivateKey {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECCPublicKey {
              ECCPublicKey {
                der: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ECCPublicKey {
              pub fn der(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECCPublicKey::ECCPublicKey{der, } => der,
                }
              }
            }

            impl Debug
              for ECCPublicKey {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECCPublicKey {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECCPublicKey::ECCPublicKey{der, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.ECCPublicKey(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(der, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ECCPublicKey {}

            impl Hash
              for ECCPublicKey {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECCPublicKey::ECCPublicKey{der, } => {
                    ::std::hash::Hash::hash(der, _state)
                  },
                }
              }
            }

            impl Default
              for ECCPublicKey {
              fn default() -> ECCPublicKey {
                ECCPublicKey::ECCPublicKey {
                  der: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ECCPublicKey>
              for &ECCPublicKey {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECDHCurveSpec {
              ECC_NIST_P256 {},
              ECC_NIST_P384 {},
              ECC_NIST_P521 {},
              SM2 {}
            }

            impl ECDHCurveSpec {}

            impl Debug
              for ECDHCurveSpec {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECDHCurveSpec {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECDHCurveSpec::ECC_NIST_P256{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.ECC__NIST__P256")?;
                    Ok(())
                  },
                  ECDHCurveSpec::ECC_NIST_P384{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.ECC__NIST__P384")?;
                    Ok(())
                  },
                  ECDHCurveSpec::ECC_NIST_P521{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.ECC__NIST__P521")?;
                    Ok(())
                  },
                  ECDHCurveSpec::SM2{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.SM2")?;
                    Ok(())
                  },
                }
              }
            }

            impl ECDHCurveSpec {
              pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<ECDHCurveSpec>> {
                ::dafny_runtime::seq![::std::rc::Rc::new(ECDHCurveSpec::ECC_NIST_P256 {}), ::std::rc::Rc::new(ECDHCurveSpec::ECC_NIST_P384 {}), ::std::rc::Rc::new(ECDHCurveSpec::ECC_NIST_P521 {}), ::std::rc::Rc::new(ECDHCurveSpec::SM2 {})].iter()
              }
            }

            impl Eq
              for ECDHCurveSpec {}

            impl Hash
              for ECDHCurveSpec {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECDHCurveSpec::ECC_NIST_P256{} => {
                    
                  },
                  ECDHCurveSpec::ECC_NIST_P384{} => {
                    
                  },
                  ECDHCurveSpec::ECC_NIST_P521{} => {
                    
                  },
                  ECDHCurveSpec::SM2{} => {
                    
                  },
                }
              }
            }

            impl Default
              for ECDHCurveSpec {
              fn default() -> ECDHCurveSpec {
                ECDHCurveSpec::ECC_NIST_P256 {}
              }
            }

            impl AsRef<ECDHCurveSpec>
              for &ECDHCurveSpec {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECDSASignatureAlgorithm {
              ECDSA_P384 {},
              ECDSA_P256 {}
            }

            impl ECDSASignatureAlgorithm {}

            impl Debug
              for ECDSASignatureAlgorithm {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECDSASignatureAlgorithm {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECDSASignatureAlgorithm::ECDSA_P384{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.ECDSA__P384")?;
                    Ok(())
                  },
                  ECDSASignatureAlgorithm::ECDSA_P256{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.ECDSA__P256")?;
                    Ok(())
                  },
                }
              }
            }

            impl ECDSASignatureAlgorithm {
              pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<ECDSASignatureAlgorithm>> {
                ::dafny_runtime::seq![::std::rc::Rc::new(ECDSASignatureAlgorithm::ECDSA_P384 {}), ::std::rc::Rc::new(ECDSASignatureAlgorithm::ECDSA_P256 {})].iter()
              }
            }

            impl Eq
              for ECDSASignatureAlgorithm {}

            impl Hash
              for ECDSASignatureAlgorithm {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECDSASignatureAlgorithm::ECDSA_P384{} => {
                    
                  },
                  ECDSASignatureAlgorithm::ECDSA_P256{} => {
                    
                  },
                }
              }
            }

            impl Default
              for ECDSASignatureAlgorithm {
              fn default() -> ECDSASignatureAlgorithm {
                ECDSASignatureAlgorithm::ECDSA_P384 {}
              }
            }

            impl AsRef<ECDSASignatureAlgorithm>
              for &ECDSASignatureAlgorithm {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECDSASignInput {
              ECDSASignInput {
                signatureAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
                signingKey: ::dafny_runtime::Sequence<u8>,
                message: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ECDSASignInput {
              pub fn signatureAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> {
                match self {
                  ECDSASignInput::ECDSASignInput{signatureAlgorithm, signingKey, message, } => signatureAlgorithm,
                }
              }
              pub fn signingKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECDSASignInput::ECDSASignInput{signatureAlgorithm, signingKey, message, } => signingKey,
                }
              }
              pub fn message(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECDSASignInput::ECDSASignInput{signatureAlgorithm, signingKey, message, } => message,
                }
              }
            }

            impl Debug
              for ECDSASignInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECDSASignInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECDSASignInput::ECDSASignInput{signatureAlgorithm, signingKey, message, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDSASignInput.ECDSASignInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signatureAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signingKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ECDSASignInput {}

            impl Hash
              for ECDSASignInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECDSASignInput::ECDSASignInput{signatureAlgorithm, signingKey, message, } => {
                    ::std::hash::Hash::hash(signatureAlgorithm, _state);
                    ::std::hash::Hash::hash(signingKey, _state);
                    ::std::hash::Hash::hash(message, _state)
                  },
                }
              }
            }

            impl Default
              for ECDSASignInput {
              fn default() -> ECDSASignInput {
                ECDSASignInput::ECDSASignInput {
                  signatureAlgorithm: ::std::default::Default::default(),
                  signingKey: ::std::default::Default::default(),
                  message: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ECDSASignInput>
              for &ECDSASignInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ECDSAVerifyInput {
              ECDSAVerifyInput {
                signatureAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
                verificationKey: ::dafny_runtime::Sequence<u8>,
                message: ::dafny_runtime::Sequence<u8>,
                signature: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ECDSAVerifyInput {
              pub fn signatureAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => signatureAlgorithm,
                }
              }
              pub fn verificationKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => verificationKey,
                }
              }
              pub fn message(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => message,
                }
              }
              pub fn signature(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => signature,
                }
              }
            }

            impl Debug
              for ECDSAVerifyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ECDSAVerifyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ECDSAVerifyInput.ECDSAVerifyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signatureAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(verificationKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signature, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ECDSAVerifyInput {}

            impl Hash
              for ECDSAVerifyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ECDSAVerifyInput::ECDSAVerifyInput{signatureAlgorithm, verificationKey, message, signature, } => {
                    ::std::hash::Hash::hash(signatureAlgorithm, _state);
                    ::std::hash::Hash::hash(verificationKey, _state);
                    ::std::hash::Hash::hash(message, _state);
                    ::std::hash::Hash::hash(signature, _state)
                  },
                }
              }
            }

            impl Default
              for ECDSAVerifyInput {
              fn default() -> ECDSAVerifyInput {
                ECDSAVerifyInput::ECDSAVerifyInput {
                  signatureAlgorithm: ::std::default::Default::default(),
                  verificationKey: ::std::default::Default::default(),
                  message: ::std::default::Default::default(),
                  signature: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ECDSAVerifyInput>
              for &ECDSAVerifyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateECCKeyPairInput {
              GenerateECCKeyPairInput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>
              }
            }

            impl GenerateECCKeyPairInput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  GenerateECCKeyPairInput::GenerateECCKeyPairInput{eccCurve, } => eccCurve,
                }
              }
            }

            impl Debug
              for GenerateECCKeyPairInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateECCKeyPairInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateECCKeyPairInput::GenerateECCKeyPairInput{eccCurve, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput.GenerateECCKeyPairInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateECCKeyPairInput {}

            impl Hash
              for GenerateECCKeyPairInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateECCKeyPairInput::GenerateECCKeyPairInput{eccCurve, } => {
                    ::std::hash::Hash::hash(eccCurve, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateECCKeyPairInput {
              fn default() -> GenerateECCKeyPairInput {
                GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateECCKeyPairInput>
              for &GenerateECCKeyPairInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateECCKeyPairOutput {
              GenerateECCKeyPairOutput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>,
                privateKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey>,
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey>
              }
            }

            impl GenerateECCKeyPairOutput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  GenerateECCKeyPairOutput::GenerateECCKeyPairOutput{eccCurve, privateKey, publicKey, } => eccCurve,
                }
              }
              pub fn privateKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey> {
                match self {
                  GenerateECCKeyPairOutput::GenerateECCKeyPairOutput{eccCurve, privateKey, publicKey, } => privateKey,
                }
              }
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> {
                match self {
                  GenerateECCKeyPairOutput::GenerateECCKeyPairOutput{eccCurve, privateKey, publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for GenerateECCKeyPairOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateECCKeyPairOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateECCKeyPairOutput::GenerateECCKeyPairOutput{eccCurve, privateKey, publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.GenerateECCKeyPairOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateECCKeyPairOutput {}

            impl Hash
              for GenerateECCKeyPairOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateECCKeyPairOutput::GenerateECCKeyPairOutput{eccCurve, privateKey, publicKey, } => {
                    ::std::hash::Hash::hash(eccCurve, _state);
                    ::std::hash::Hash::hash(privateKey, _state);
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateECCKeyPairOutput {
              fn default() -> GenerateECCKeyPairOutput {
                GenerateECCKeyPairOutput::GenerateECCKeyPairOutput {
                  eccCurve: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default(),
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateECCKeyPairOutput>
              for &GenerateECCKeyPairOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateECDSASignatureKeyInput {
              GenerateECDSASignatureKeyInput {
                signatureAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>
              }
            }

            impl GenerateECDSASignatureKeyInput {
              pub fn signatureAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> {
                match self {
                  GenerateECDSASignatureKeyInput::GenerateECDSASignatureKeyInput{signatureAlgorithm, } => signatureAlgorithm,
                }
              }
            }

            impl Debug
              for GenerateECDSASignatureKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateECDSASignatureKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateECDSASignatureKeyInput::GenerateECDSASignatureKeyInput{signatureAlgorithm, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput.GenerateECDSASignatureKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signatureAlgorithm, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateECDSASignatureKeyInput {}

            impl Hash
              for GenerateECDSASignatureKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateECDSASignatureKeyInput::GenerateECDSASignatureKeyInput{signatureAlgorithm, } => {
                    ::std::hash::Hash::hash(signatureAlgorithm, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateECDSASignatureKeyInput {
              fn default() -> GenerateECDSASignatureKeyInput {
                GenerateECDSASignatureKeyInput::GenerateECDSASignatureKeyInput {
                  signatureAlgorithm: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateECDSASignatureKeyInput>
              for &GenerateECDSASignatureKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateECDSASignatureKeyOutput {
              GenerateECDSASignatureKeyOutput {
                signatureAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
                verificationKey: ::dafny_runtime::Sequence<u8>,
                signingKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl GenerateECDSASignatureKeyOutput {
              pub fn signatureAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> {
                match self {
                  GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput{signatureAlgorithm, verificationKey, signingKey, } => signatureAlgorithm,
                }
              }
              pub fn verificationKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput{signatureAlgorithm, verificationKey, signingKey, } => verificationKey,
                }
              }
              pub fn signingKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput{signatureAlgorithm, verificationKey, signingKey, } => signingKey,
                }
              }
            }

            impl Debug
              for GenerateECDSASignatureKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateECDSASignatureKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput{signatureAlgorithm, verificationKey, signingKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.GenerateECDSASignatureKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signatureAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(verificationKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(signingKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateECDSASignatureKeyOutput {}

            impl Hash
              for GenerateECDSASignatureKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput{signatureAlgorithm, verificationKey, signingKey, } => {
                    ::std::hash::Hash::hash(signatureAlgorithm, _state);
                    ::std::hash::Hash::hash(verificationKey, _state);
                    ::std::hash::Hash::hash(signingKey, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateECDSASignatureKeyOutput {
              fn default() -> GenerateECDSASignatureKeyOutput {
                GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput {
                  signatureAlgorithm: ::std::default::Default::default(),
                  verificationKey: ::std::default::Default::default(),
                  signingKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateECDSASignatureKeyOutput>
              for &GenerateECDSASignatureKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateRandomBytesInput {
              GenerateRandomBytesInput {
                length: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
              }
            }

            impl GenerateRandomBytesInput {
              pub fn length(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger {
                match self {
                  GenerateRandomBytesInput::GenerateRandomBytesInput{length, } => length,
                }
              }
            }

            impl Debug
              for GenerateRandomBytesInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateRandomBytesInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateRandomBytesInput::GenerateRandomBytesInput{length, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput.GenerateRandomBytesInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(length, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateRandomBytesInput {}

            impl Hash
              for GenerateRandomBytesInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateRandomBytesInput::GenerateRandomBytesInput{length, } => {
                    ::std::hash::Hash::hash(length, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateRandomBytesInput {
              fn default() -> GenerateRandomBytesInput {
                GenerateRandomBytesInput::GenerateRandomBytesInput {
                  length: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateRandomBytesInput>
              for &GenerateRandomBytesInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateRSAKeyPairInput {
              GenerateRSAKeyPairInput {
                lengthBits: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBitsToGenerate
              }
            }

            impl GenerateRSAKeyPairInput {
              pub fn lengthBits(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBitsToGenerate {
                match self {
                  GenerateRSAKeyPairInput::GenerateRSAKeyPairInput{lengthBits, } => lengthBits,
                }
              }
            }

            impl Debug
              for GenerateRSAKeyPairInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateRSAKeyPairInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateRSAKeyPairInput::GenerateRSAKeyPairInput{lengthBits, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairInput.GenerateRSAKeyPairInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(lengthBits, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateRSAKeyPairInput {}

            impl Hash
              for GenerateRSAKeyPairInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateRSAKeyPairInput::GenerateRSAKeyPairInput{lengthBits, } => {
                    ::std::hash::Hash::hash(lengthBits, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateRSAKeyPairInput {
              fn default() -> GenerateRSAKeyPairInput {
                GenerateRSAKeyPairInput::GenerateRSAKeyPairInput {
                  lengthBits: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateRSAKeyPairInput>
              for &GenerateRSAKeyPairInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GenerateRSAKeyPairOutput {
              GenerateRSAKeyPairOutput {
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey>,
                privateKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey>
              }
            }

            impl GenerateRSAKeyPairOutput {
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey> {
                match self {
                  GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput{publicKey, privateKey, } => publicKey,
                }
              }
              pub fn privateKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey> {
                match self {
                  GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput{publicKey, privateKey, } => privateKey,
                }
              }
            }

            impl Debug
              for GenerateRSAKeyPairOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GenerateRSAKeyPairOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput{publicKey, privateKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GenerateRSAKeyPairOutput.GenerateRSAKeyPairOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GenerateRSAKeyPairOutput {}

            impl Hash
              for GenerateRSAKeyPairOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput{publicKey, privateKey, } => {
                    ::std::hash::Hash::hash(publicKey, _state);
                    ::std::hash::Hash::hash(privateKey, _state)
                  },
                }
              }
            }

            impl Default
              for GenerateRSAKeyPairOutput {
              fn default() -> GenerateRSAKeyPairOutput {
                GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput {
                  publicKey: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GenerateRSAKeyPairOutput>
              for &GenerateRSAKeyPairOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GetPublicKeyFromPrivateKeyInput {
              GetPublicKeyFromPrivateKeyInput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>,
                privateKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey>
              }
            }

            impl GetPublicKeyFromPrivateKeyInput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput{eccCurve, privateKey, } => eccCurve,
                }
              }
              pub fn privateKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey> {
                match self {
                  GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput{eccCurve, privateKey, } => privateKey,
                }
              }
            }

            impl Debug
              for GetPublicKeyFromPrivateKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GetPublicKeyFromPrivateKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput{eccCurve, privateKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput.GetPublicKeyFromPrivateKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GetPublicKeyFromPrivateKeyInput {}

            impl Hash
              for GetPublicKeyFromPrivateKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput{eccCurve, privateKey, } => {
                    ::std::hash::Hash::hash(eccCurve, _state);
                    ::std::hash::Hash::hash(privateKey, _state)
                  },
                }
              }
            }

            impl Default
              for GetPublicKeyFromPrivateKeyInput {
              fn default() -> GetPublicKeyFromPrivateKeyInput {
                GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput {
                  eccCurve: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GetPublicKeyFromPrivateKeyInput>
              for &GetPublicKeyFromPrivateKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GetPublicKeyFromPrivateKeyOutput {
              GetPublicKeyFromPrivateKeyOutput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>,
                privateKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey>,
                publicKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl GetPublicKeyFromPrivateKeyOutput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput{eccCurve, privateKey, publicKey, } => eccCurve,
                }
              }
              pub fn privateKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey> {
                match self {
                  GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput{eccCurve, privateKey, publicKey, } => privateKey,
                }
              }
              pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput{eccCurve, privateKey, publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for GetPublicKeyFromPrivateKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GetPublicKeyFromPrivateKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput{eccCurve, privateKey, publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.GetPublicKeyFromPrivateKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GetPublicKeyFromPrivateKeyOutput {}

            impl Hash
              for GetPublicKeyFromPrivateKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput{eccCurve, privateKey, publicKey, } => {
                    ::std::hash::Hash::hash(eccCurve, _state);
                    ::std::hash::Hash::hash(privateKey, _state);
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for GetPublicKeyFromPrivateKeyOutput {
              fn default() -> GetPublicKeyFromPrivateKeyOutput {
                GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput {
                  eccCurve: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default(),
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GetPublicKeyFromPrivateKeyOutput>
              for &GetPublicKeyFromPrivateKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GetRSAKeyModulusLengthInput {
              GetRSAKeyModulusLengthInput {
                publicKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl GetRSAKeyModulusLengthInput {
              pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput{publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for GetRSAKeyModulusLengthInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GetRSAKeyModulusLengthInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput{publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthInput.GetRSAKeyModulusLengthInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GetRSAKeyModulusLengthInput {}

            impl Hash
              for GetRSAKeyModulusLengthInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput{publicKey, } => {
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for GetRSAKeyModulusLengthInput {
              fn default() -> GetRSAKeyModulusLengthInput {
                GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput {
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GetRSAKeyModulusLengthInput>
              for &GetRSAKeyModulusLengthInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum GetRSAKeyModulusLengthOutput {
              GetRSAKeyModulusLengthOutput {
                length: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits
              }
            }

            impl GetRSAKeyModulusLengthOutput {
              pub fn length(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits {
                match self {
                  GetRSAKeyModulusLengthOutput::GetRSAKeyModulusLengthOutput{length, } => length,
                }
              }
            }

            impl Debug
              for GetRSAKeyModulusLengthOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for GetRSAKeyModulusLengthOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  GetRSAKeyModulusLengthOutput::GetRSAKeyModulusLengthOutput{length, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput.GetRSAKeyModulusLengthOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(length, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for GetRSAKeyModulusLengthOutput {}

            impl Hash
              for GetRSAKeyModulusLengthOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  GetRSAKeyModulusLengthOutput::GetRSAKeyModulusLengthOutput{length, } => {
                    ::std::hash::Hash::hash(length, _state)
                  },
                }
              }
            }

            impl Default
              for GetRSAKeyModulusLengthOutput {
              fn default() -> GetRSAKeyModulusLengthOutput {
                GetRSAKeyModulusLengthOutput::GetRSAKeyModulusLengthOutput {
                  length: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<GetRSAKeyModulusLengthOutput>
              for &GetRSAKeyModulusLengthOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum HkdfExpandInput {
              HkdfExpandInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                prk: ::dafny_runtime::Sequence<u8>,
                info: ::dafny_runtime::Sequence<u8>,
                expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
              }
            }

            impl HkdfExpandInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => digestAlgorithm,
                }
              }
              pub fn prk(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => prk,
                }
              }
              pub fn info(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => info,
                }
              }
              pub fn expectedLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => expectedLength,
                }
              }
            }

            impl Debug
              for HkdfExpandInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for HkdfExpandInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput.HkdfExpandInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(prk, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(info, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(expectedLength, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for HkdfExpandInput {}

            impl Hash
              for HkdfExpandInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  HkdfExpandInput::HkdfExpandInput{digestAlgorithm, prk, info, expectedLength, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(prk, _state);
                    ::std::hash::Hash::hash(info, _state);
                    ::std::hash::Hash::hash(expectedLength, _state)
                  },
                }
              }
            }

            impl Default
              for HkdfExpandInput {
              fn default() -> HkdfExpandInput {
                HkdfExpandInput::HkdfExpandInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  prk: ::std::default::Default::default(),
                  info: ::std::default::Default::default(),
                  expectedLength: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<HkdfExpandInput>
              for &HkdfExpandInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum HkdfExtractInput {
              HkdfExtractInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                salt: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>,
                ikm: ::dafny_runtime::Sequence<u8>
              }
            }

            impl HkdfExtractInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  HkdfExtractInput::HkdfExtractInput{digestAlgorithm, salt, ikm, } => digestAlgorithm,
                }
              }
              pub fn salt(&self) -> &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> {
                match self {
                  HkdfExtractInput::HkdfExtractInput{digestAlgorithm, salt, ikm, } => salt,
                }
              }
              pub fn ikm(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HkdfExtractInput::HkdfExtractInput{digestAlgorithm, salt, ikm, } => ikm,
                }
              }
            }

            impl Debug
              for HkdfExtractInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for HkdfExtractInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  HkdfExtractInput::HkdfExtractInput{digestAlgorithm, salt, ikm, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput.HkdfExtractInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(salt, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(ikm, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for HkdfExtractInput {}

            impl Hash
              for HkdfExtractInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  HkdfExtractInput::HkdfExtractInput{digestAlgorithm, salt, ikm, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(salt, _state);
                    ::std::hash::Hash::hash(ikm, _state)
                  },
                }
              }
            }

            impl Default
              for HkdfExtractInput {
              fn default() -> HkdfExtractInput {
                HkdfExtractInput::HkdfExtractInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  salt: ::std::default::Default::default(),
                  ikm: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<HkdfExtractInput>
              for &HkdfExtractInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum HkdfInput {
              HkdfInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                salt: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>,
                ikm: ::dafny_runtime::Sequence<u8>,
                info: ::dafny_runtime::Sequence<u8>,
                expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
              }
            }

            impl HkdfInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => digestAlgorithm,
                }
              }
              pub fn salt(&self) -> &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => salt,
                }
              }
              pub fn ikm(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => ikm,
                }
              }
              pub fn info(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => info,
                }
              }
              pub fn expectedLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => expectedLength,
                }
              }
            }

            impl Debug
              for HkdfInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for HkdfInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.HkdfInput.HkdfInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(salt, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(ikm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(info, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(expectedLength, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for HkdfInput {}

            impl Hash
              for HkdfInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  HkdfInput::HkdfInput{digestAlgorithm, salt, ikm, info, expectedLength, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(salt, _state);
                    ::std::hash::Hash::hash(ikm, _state);
                    ::std::hash::Hash::hash(info, _state);
                    ::std::hash::Hash::hash(expectedLength, _state)
                  },
                }
              }
            }

            impl Default
              for HkdfInput {
              fn default() -> HkdfInput {
                HkdfInput::HkdfInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  salt: ::std::default::Default::default(),
                  ikm: ::std::default::Default::default(),
                  info: ::std::default::Default::default(),
                  expectedLength: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<HkdfInput>
              for &HkdfInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum HMacInput {
              HMacInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                key: ::dafny_runtime::Sequence<u8>,
                message: ::dafny_runtime::Sequence<u8>
              }
            }

            impl HMacInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  HMacInput::HMacInput{digestAlgorithm, key, message, } => digestAlgorithm,
                }
              }
              pub fn key(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HMacInput::HMacInput{digestAlgorithm, key, message, } => key,
                }
              }
              pub fn message(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  HMacInput::HMacInput{digestAlgorithm, key, message, } => message,
                }
              }
            }

            impl Debug
              for HMacInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for HMacInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  HMacInput::HMacInput{digestAlgorithm, key, message, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.HMacInput.HMacInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(key, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for HMacInput {}

            impl Hash
              for HMacInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  HMacInput::HMacInput{digestAlgorithm, key, message, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(key, _state);
                    ::std::hash::Hash::hash(message, _state)
                  },
                }
              }
            }

            impl Default
              for HMacInput {
              fn default() -> HMacInput {
                HMacInput::HMacInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  key: ::std::default::Default::default(),
                  message: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<HMacInput>
              for &HMacInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum KdfCtrInput {
              KdfCtrInput {
                digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
                ikm: ::dafny_runtime::Sequence<u8>,
                expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
                purpose: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>,
                nonce: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>
              }
            }

            impl KdfCtrInput {
              pub fn digestAlgorithm(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => digestAlgorithm,
                }
              }
              pub fn ikm(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => ikm,
                }
              }
              pub fn expectedLength(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => expectedLength,
                }
              }
              pub fn purpose(&self) -> &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => purpose,
                }
              }
              pub fn nonce(&self) -> &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => nonce,
                }
              }
            }

            impl Debug
              for KdfCtrInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for KdfCtrInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput.KdfCtrInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(digestAlgorithm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(ikm, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(expectedLength, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(purpose, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(nonce, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for KdfCtrInput {}

            impl Hash
              for KdfCtrInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  KdfCtrInput::KdfCtrInput{digestAlgorithm, ikm, expectedLength, purpose, nonce, } => {
                    ::std::hash::Hash::hash(digestAlgorithm, _state);
                    ::std::hash::Hash::hash(ikm, _state);
                    ::std::hash::Hash::hash(expectedLength, _state);
                    ::std::hash::Hash::hash(purpose, _state);
                    ::std::hash::Hash::hash(nonce, _state)
                  },
                }
              }
            }

            impl Default
              for KdfCtrInput {
              fn default() -> KdfCtrInput {
                KdfCtrInput::KdfCtrInput {
                  digestAlgorithm: ::std::default::Default::default(),
                  ikm: ::std::default::Default::default(),
                  expectedLength: ::std::default::Default::default(),
                  purpose: ::std::default::Default::default(),
                  nonce: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<KdfCtrInput>
              for &KdfCtrInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ParsePublicKeyInput {
              ParsePublicKeyInput {
                publicKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ParsePublicKeyInput {
              pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ParsePublicKeyInput::ParsePublicKeyInput{publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for ParsePublicKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ParsePublicKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ParsePublicKeyInput::ParsePublicKeyInput{publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyInput.ParsePublicKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ParsePublicKeyInput {}

            impl Hash
              for ParsePublicKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ParsePublicKeyInput::ParsePublicKeyInput{publicKey, } => {
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for ParsePublicKeyInput {
              fn default() -> ParsePublicKeyInput {
                ParsePublicKeyInput::ParsePublicKeyInput {
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ParsePublicKeyInput>
              for &ParsePublicKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ParsePublicKeyOutput {
              ParsePublicKeyOutput {
                publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey>
              }
            }

            impl ParsePublicKeyOutput {
              pub fn publicKey(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> {
                match self {
                  ParsePublicKeyOutput::ParsePublicKeyOutput{publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for ParsePublicKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ParsePublicKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ParsePublicKeyOutput::ParsePublicKeyOutput{publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput.ParsePublicKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ParsePublicKeyOutput {}

            impl Hash
              for ParsePublicKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ParsePublicKeyOutput::ParsePublicKeyOutput{publicKey, } => {
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for ParsePublicKeyOutput {
              fn default() -> ParsePublicKeyOutput {
                ParsePublicKeyOutput::ParsePublicKeyOutput {
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ParsePublicKeyOutput>
              for &ParsePublicKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            pub type PositiveInteger = i32;

            #[derive(PartialEq, Clone)]
            pub enum RSADecryptInput {
              RSADecryptInput {
                padding: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>,
                privateKey: ::dafny_runtime::Sequence<u8>,
                cipherText: ::dafny_runtime::Sequence<u8>
              }
            }

            impl RSADecryptInput {
              pub fn padding(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode> {
                match self {
                  RSADecryptInput::RSADecryptInput{padding, privateKey, cipherText, } => padding,
                }
              }
              pub fn privateKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSADecryptInput::RSADecryptInput{padding, privateKey, cipherText, } => privateKey,
                }
              }
              pub fn cipherText(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSADecryptInput::RSADecryptInput{padding, privateKey, cipherText, } => cipherText,
                }
              }
            }

            impl Debug
              for RSADecryptInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for RSADecryptInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  RSADecryptInput::RSADecryptInput{padding, privateKey, cipherText, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput.RSADecryptInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(padding, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(cipherText, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for RSADecryptInput {}

            impl Hash
              for RSADecryptInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  RSADecryptInput::RSADecryptInput{padding, privateKey, cipherText, } => {
                    ::std::hash::Hash::hash(padding, _state);
                    ::std::hash::Hash::hash(privateKey, _state);
                    ::std::hash::Hash::hash(cipherText, _state)
                  },
                }
              }
            }

            impl Default
              for RSADecryptInput {
              fn default() -> RSADecryptInput {
                RSADecryptInput::RSADecryptInput {
                  padding: ::std::default::Default::default(),
                  privateKey: ::std::default::Default::default(),
                  cipherText: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<RSADecryptInput>
              for &RSADecryptInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum RSAEncryptInput {
              RSAEncryptInput {
                padding: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>,
                publicKey: ::dafny_runtime::Sequence<u8>,
                plaintext: ::dafny_runtime::Sequence<u8>
              }
            }

            impl RSAEncryptInput {
              pub fn padding(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode> {
                match self {
                  RSAEncryptInput::RSAEncryptInput{padding, publicKey, plaintext, } => padding,
                }
              }
              pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSAEncryptInput::RSAEncryptInput{padding, publicKey, plaintext, } => publicKey,
                }
              }
              pub fn plaintext(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSAEncryptInput::RSAEncryptInput{padding, publicKey, plaintext, } => plaintext,
                }
              }
            }

            impl Debug
              for RSAEncryptInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for RSAEncryptInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  RSAEncryptInput::RSAEncryptInput{padding, publicKey, plaintext, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput.RSAEncryptInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(padding, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(plaintext, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for RSAEncryptInput {}

            impl Hash
              for RSAEncryptInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  RSAEncryptInput::RSAEncryptInput{padding, publicKey, plaintext, } => {
                    ::std::hash::Hash::hash(padding, _state);
                    ::std::hash::Hash::hash(publicKey, _state);
                    ::std::hash::Hash::hash(plaintext, _state)
                  },
                }
              }
            }

            impl Default
              for RSAEncryptInput {
              fn default() -> RSAEncryptInput {
                RSAEncryptInput::RSAEncryptInput {
                  padding: ::std::default::Default::default(),
                  publicKey: ::std::default::Default::default(),
                  plaintext: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<RSAEncryptInput>
              for &RSAEncryptInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            pub type RSAModulusLengthBits = i32;

            pub type RSAModulusLengthBitsToGenerate = i32;

            #[derive(PartialEq, Clone)]
            pub enum RSAPaddingMode {
              PKCS1 {},
              OAEP_SHA1 {},
              OAEP_SHA256 {},
              OAEP_SHA384 {},
              OAEP_SHA512 {}
            }

            impl RSAPaddingMode {}

            impl Debug
              for RSAPaddingMode {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for RSAPaddingMode {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  RSAPaddingMode::PKCS1{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.PKCS1")?;
                    Ok(())
                  },
                  RSAPaddingMode::OAEP_SHA1{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.OAEP__SHA1")?;
                    Ok(())
                  },
                  RSAPaddingMode::OAEP_SHA256{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.OAEP__SHA256")?;
                    Ok(())
                  },
                  RSAPaddingMode::OAEP_SHA384{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.OAEP__SHA384")?;
                    Ok(())
                  },
                  RSAPaddingMode::OAEP_SHA512{} => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.OAEP__SHA512")?;
                    Ok(())
                  },
                }
              }
            }

            impl RSAPaddingMode {
              pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<RSAPaddingMode>> {
                ::dafny_runtime::seq![::std::rc::Rc::new(RSAPaddingMode::PKCS1 {}), ::std::rc::Rc::new(RSAPaddingMode::OAEP_SHA1 {}), ::std::rc::Rc::new(RSAPaddingMode::OAEP_SHA256 {}), ::std::rc::Rc::new(RSAPaddingMode::OAEP_SHA384 {}), ::std::rc::Rc::new(RSAPaddingMode::OAEP_SHA512 {})].iter()
              }
            }

            impl Eq
              for RSAPaddingMode {}

            impl Hash
              for RSAPaddingMode {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  RSAPaddingMode::PKCS1{} => {
                    
                  },
                  RSAPaddingMode::OAEP_SHA1{} => {
                    
                  },
                  RSAPaddingMode::OAEP_SHA256{} => {
                    
                  },
                  RSAPaddingMode::OAEP_SHA384{} => {
                    
                  },
                  RSAPaddingMode::OAEP_SHA512{} => {
                    
                  },
                }
              }
            }

            impl Default
              for RSAPaddingMode {
              fn default() -> RSAPaddingMode {
                RSAPaddingMode::PKCS1 {}
              }
            }

            impl AsRef<RSAPaddingMode>
              for &RSAPaddingMode {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum RSAPrivateKey {
              RSAPrivateKey {
                lengthBits: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits,
                pem: ::dafny_runtime::Sequence<u8>
              }
            }

            impl RSAPrivateKey {
              pub fn lengthBits(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits {
                match self {
                  RSAPrivateKey::RSAPrivateKey{lengthBits, pem, } => lengthBits,
                }
              }
              pub fn pem(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSAPrivateKey::RSAPrivateKey{lengthBits, pem, } => pem,
                }
              }
            }

            impl Debug
              for RSAPrivateKey {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for RSAPrivateKey {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  RSAPrivateKey::RSAPrivateKey{lengthBits, pem, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey.RSAPrivateKey(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(lengthBits, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(pem, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for RSAPrivateKey {}

            impl Hash
              for RSAPrivateKey {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  RSAPrivateKey::RSAPrivateKey{lengthBits, pem, } => {
                    ::std::hash::Hash::hash(lengthBits, _state);
                    ::std::hash::Hash::hash(pem, _state)
                  },
                }
              }
            }

            impl Default
              for RSAPrivateKey {
              fn default() -> RSAPrivateKey {
                RSAPrivateKey::RSAPrivateKey {
                  lengthBits: ::std::default::Default::default(),
                  pem: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<RSAPrivateKey>
              for &RSAPrivateKey {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum RSAPublicKey {
              RSAPublicKey {
                lengthBits: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits,
                pem: ::dafny_runtime::Sequence<u8>
              }
            }

            impl RSAPublicKey {
              pub fn lengthBits(&self) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits {
                match self {
                  RSAPublicKey::RSAPublicKey{lengthBits, pem, } => lengthBits,
                }
              }
              pub fn pem(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  RSAPublicKey::RSAPublicKey{lengthBits, pem, } => pem,
                }
              }
            }

            impl Debug
              for RSAPublicKey {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for RSAPublicKey {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  RSAPublicKey::RSAPublicKey{lengthBits, pem, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey.RSAPublicKey(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(lengthBits, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(pem, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for RSAPublicKey {}

            impl Hash
              for RSAPublicKey {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  RSAPublicKey::RSAPublicKey{lengthBits, pem, } => {
                    ::std::hash::Hash::hash(lengthBits, _state);
                    ::std::hash::Hash::hash(pem, _state)
                  },
                }
              }
            }

            impl Default
              for RSAPublicKey {
              fn default() -> RSAPublicKey {
                RSAPublicKey::RSAPublicKey {
                  lengthBits: ::std::default::Default::default(),
                  pem: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<RSAPublicKey>
              for &RSAPublicKey {
              fn as_ref(&self) -> Self {
                self
              }
            }

            pub type SymmetricKeyLength = i32;

            pub type Uint8Bits = i32;

            pub type Uint8Bytes = i32;

            #[derive(PartialEq, Clone)]
            pub enum ValidatePublicKeyInput {
              ValidatePublicKeyInput {
                eccCurve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>,
                publicKey: ::dafny_runtime::Sequence<u8>
              }
            }

            impl ValidatePublicKeyInput {
              pub fn eccCurve(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> {
                match self {
                  ValidatePublicKeyInput::ValidatePublicKeyInput{eccCurve, publicKey, } => eccCurve,
                }
              }
              pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
                match self {
                  ValidatePublicKeyInput::ValidatePublicKeyInput{eccCurve, publicKey, } => publicKey,
                }
              }
            }

            impl Debug
              for ValidatePublicKeyInput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ValidatePublicKeyInput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ValidatePublicKeyInput::ValidatePublicKeyInput{eccCurve, publicKey, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput.ValidatePublicKeyInput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(eccCurve, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ValidatePublicKeyInput {}

            impl Hash
              for ValidatePublicKeyInput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ValidatePublicKeyInput::ValidatePublicKeyInput{eccCurve, publicKey, } => {
                    ::std::hash::Hash::hash(eccCurve, _state);
                    ::std::hash::Hash::hash(publicKey, _state)
                  },
                }
              }
            }

            impl Default
              for ValidatePublicKeyInput {
              fn default() -> ValidatePublicKeyInput {
                ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: ::std::default::Default::default(),
                  publicKey: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ValidatePublicKeyInput>
              for &ValidatePublicKeyInput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum ValidatePublicKeyOutput {
              ValidatePublicKeyOutput {
                success: bool
              }
            }

            impl ValidatePublicKeyOutput {
              pub fn success(&self) -> &bool {
                match self {
                  ValidatePublicKeyOutput::ValidatePublicKeyOutput{success, } => success,
                }
              }
            }

            impl Debug
              for ValidatePublicKeyOutput {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for ValidatePublicKeyOutput {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  ValidatePublicKeyOutput::ValidatePublicKeyOutput{success, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.ValidatePublicKeyOutput(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(success, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for ValidatePublicKeyOutput {}

            impl Hash
              for ValidatePublicKeyOutput {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  ValidatePublicKeyOutput::ValidatePublicKeyOutput{success, } => {
                    ::std::hash::Hash::hash(success, _state)
                  },
                }
              }
            }

            impl Default
              for ValidatePublicKeyOutput {
              fn default() -> ValidatePublicKeyOutput {
                ValidatePublicKeyOutput::ValidatePublicKeyOutput {
                  success: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<ValidatePublicKeyOutput>
              for &ValidatePublicKeyOutput {
              fn as_ref(&self) -> Self {
                self
              }
            }

            #[derive(PartialEq, Clone)]
            pub enum Error {
              AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>
              },
              CollectionOfErrors {
                list: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>,
                message: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>
              },
              Opaque {
                obj: ::dafny_runtime::Object<dyn ::std::any::Any>
              }
            }

            impl Error {
              pub fn message(&self) -> &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
                match self {
                  Error::AwsCryptographicPrimitivesError{message, } => message,
                  Error::CollectionOfErrors{list, message, } => message,
                  Error::Opaque{obj, } => panic!("field does not exist on this variant"),
                }
              }
              pub fn list(&self) -> &::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>> {
                match self {
                  Error::AwsCryptographicPrimitivesError{message, } => panic!("field does not exist on this variant"),
                  Error::CollectionOfErrors{list, message, } => list,
                  Error::Opaque{obj, } => panic!("field does not exist on this variant"),
                }
              }
              pub fn obj(&self) -> &::dafny_runtime::Object<dyn ::std::any::Any> {
                match self {
                  Error::AwsCryptographicPrimitivesError{message, } => panic!("field does not exist on this variant"),
                  Error::CollectionOfErrors{list, message, } => panic!("field does not exist on this variant"),
                  Error::Opaque{obj, } => obj,
                }
              }
            }

            impl Debug
              for Error {
              fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
                ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
              }
            }

            impl DafnyPrint
              for Error {
              fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
                match self {
                  Error::AwsCryptographicPrimitivesError{message, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.Error.AwsCryptographicPrimitivesError(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                  Error::CollectionOfErrors{list, message, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.Error.CollectionOfErrors(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(list, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(message, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                  Error::Opaque{obj, } => {
                    write!(_formatter, "software.amazon.cryptography.primitives.internaldafny.types.Error.Opaque(")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(obj, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                  },
                }
              }
            }

            impl Eq
              for Error {}

            impl Hash
              for Error {
              fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
                match self {
                  Error::AwsCryptographicPrimitivesError{message, } => {
                    ::std::hash::Hash::hash(message, _state)
                  },
                  Error::CollectionOfErrors{list, message, } => {
                    ::std::hash::Hash::hash(list, _state);
                    ::std::hash::Hash::hash(message, _state)
                  },
                  Error::Opaque{obj, } => {
                    ::std::hash::Hash::hash(obj, _state)
                  },
                }
              }
            }

            impl Default
              for Error {
              fn default() -> Error {
                Error::AwsCryptographicPrimitivesError {
                  message: ::std::default::Default::default()
                }
              }
            }

            impl AsRef<Error>
              for &Error {
              fn as_ref(&self) -> Self {
                self
              }
            }

            pub type OpaqueError = ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>;
          }
        }
      }
    }
  }
}
pub mod r#_AwsCryptographyPrimitivesOperations_Compile {
  pub use ::std::fmt::Debug;
  pub use ::dafny_runtime::DafnyPrint;
  pub use ::std::cmp::Eq;
  pub use ::std::hash::Hash;
  pub use ::std::default::Default;
  pub use ::std::convert::AsRef;

  pub struct _default {}

  impl _default {
    pub fn GenerateRandomBytes(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRandomBytesInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out24 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out24 = ::dafny_runtime::MaybePlacebo::from(crate::r#_Random_Compile::_default::GenerateBytes(input.length().clone()));
      output = ::dafny_runtime::MaybePlacebo::from(_out24.read());
      return output.read();
    }
    pub fn Digest(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out25 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out25 = ::dafny_runtime::MaybePlacebo::from(crate::r#_Digest_Compile::_default::Digest(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out25.read());
      return output.read();
    }
    pub fn HMac(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      crate::r#_WrappedHMAC_Compile::_default::Digest(input)
    }
    pub fn HkdfExtract(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out26 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out26 = ::dafny_runtime::MaybePlacebo::from(crate::r#_WrappedHKDF_Compile::_default::Extract(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out26.read());
      return output.read();
    }
    pub fn HkdfExpand(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out27 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out27 = ::dafny_runtime::MaybePlacebo::from(crate::r#_WrappedHKDF_Compile::_default::Expand(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out27.read());
      return output.read();
    }
    pub fn Hkdf(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out28 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out28 = ::dafny_runtime::MaybePlacebo::from(crate::r#_WrappedHKDF_Compile::_default::Hkdf(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out28.read());
      return output.read();
    }
    pub fn KdfCounterMode(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out29 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out29 = ::dafny_runtime::MaybePlacebo::from(crate::r#_KdfCtr_Compile::_default::KdfCounterMode(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out29.read());
      return output.read();
    }
    pub fn AesKdfCounterMode(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AesKdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
              error: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                    message: ::dafny_runtime::string_utf16_of("Implement")
                  })
            }));
      return output.read();
    }
    pub fn AESEncrypt(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out30 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out30 = ::dafny_runtime::MaybePlacebo::from(crate::AESEncryption::_default::AESEncrypt(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out30.read());
      return output.read();
    }
    pub fn AESDecrypt(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out31 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out31 = ::dafny_runtime::MaybePlacebo::from(crate::AESEncryption::_default::AESDecrypt(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out31.read());
      return output.read();
    }
    pub fn GenerateRSAKeyPair(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut publicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey>>::new();
      let mut privateKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey>>::new();
      let mut _out32 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey>>::new();
      let mut _out33 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey>>::new();
      let _x = crate::RSAEncryption::_default::GenerateKeyPair(input.lengthBits().clone());
      _out32 = ::dafny_runtime::MaybePlacebo::from(_x.0);
      _out33 = ::dafny_runtime::MaybePlacebo::from(_x.1);
      publicKey = ::dafny_runtime::MaybePlacebo::from(_out32.read());
      privateKey = ::dafny_runtime::MaybePlacebo::from(_out33.read());
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput {
                    publicKey: publicKey.read(),
                    privateKey: privateKey.read()
                  })
            }));
      return output.read();
    }
    pub fn GetRSAKeyModulusLength(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut valueOrError0: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::RSAEncryption::_default::GetRSAKeyModulusLength(input.publicKey());
      if valueOrError0.IsFailure() {
        valueOrError0.PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>>()
      } else {
        let mut length: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits = valueOrError0.Extract();
        ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
            value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput::GetRSAKeyModulusLengthOutput {
                  length: length
                })
          })
      }
    }
    pub fn RSADecrypt(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out34 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out34 = ::dafny_runtime::MaybePlacebo::from(crate::RSAEncryption::_default::Decrypt(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out34.read());
      return output.read();
    }
    pub fn RSAEncrypt(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out35 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out35 = ::dafny_runtime::MaybePlacebo::from(crate::RSAEncryption::_default::Encrypt(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out35.read());
      return output.read();
    }
    pub fn GenerateECDSASignatureKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out36 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out36 = ::dafny_runtime::MaybePlacebo::from(crate::Signature::_default::KeyGen(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out36.read());
      return output.read();
    }
    pub fn ECDSASign(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out37 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out37 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::Signature::ECDSA::Sign(input.signatureAlgorithm(), input.signingKey(), input.message()));
      output = ::dafny_runtime::MaybePlacebo::from(_out37.read());
      return output.read();
    }
    pub fn ECDSAVerify(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSAVerifyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      output = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::Signature::ECDSA::Verify(input.signatureAlgorithm(), input.verificationKey(), input.message(), input.signature()));
      return output.read();
    }
    pub fn GenerateECCKeyPair(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out38 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out38 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out38.read());
      return output.read();
    }
    pub fn GetPublicKeyFromPrivateKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out39 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out39 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GetPublicKeyFromPrivate(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out39.read());
      return output.read();
    }
    pub fn ValidatePublicKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out40 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out40 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out40.read());
      return output.read();
    }
    pub fn DeriveSharedSecret(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out41 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out41 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DeriveSharedSecret(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out41.read());
      return output.read();
    }
    pub fn CompressPublicKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out42 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out42 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::CompressPublicKey(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out42.read());
      return output.read();
    }
    pub fn DecompressPublicKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out43 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out43 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DecompressPublicKey(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out43.read());
      return output.read();
    }
    pub fn ParsePublicKey(config: &::std::rc::Rc<crate::r#_AwsCryptographyPrimitivesOperations_Compile::Config>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out44 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out44 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ParsePublicKey(input));
      output = ::dafny_runtime::MaybePlacebo::from(_out44.read());
      return output.read();
    }
  }

  #[derive(PartialEq, Clone)]
  pub enum Config {
    Config {}
  }

  impl Config {}

  impl Debug
    for Config {
    fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
      ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
    }
  }

  impl DafnyPrint
    for Config {
    fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
      match self {
        Config::Config{} => {
          write!(_formatter, "AwsCryptographyPrimitivesOperations_Compile.Config.Config")?;
          Ok(())
        },
      }
    }
  }

  impl Config {
    pub fn _AllSingletonConstructors() -> ::dafny_runtime::SequenceIter<::std::rc::Rc<Config>> {
      ::dafny_runtime::seq![::std::rc::Rc::new(Config::Config {})].iter()
    }
  }

  impl Eq
    for Config {}

  impl Hash
    for Config {
    fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
      match self {
        Config::Config{} => {
          
        },
      }
    }
  }

  impl Default
    for Config {
    fn default() -> Config {
      Config::Config {}
    }
  }

  impl AsRef<Config>
    for &Config {
    fn as_ref(&self) -> Self {
      self
    }
  }
}
pub mod r#_Digest_Compile {
  pub struct _default {}

  impl _default {
    pub fn Length(digestAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>) -> ::dafny_runtime::_System::nat {
      let mut _source0: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = digestAlgorithm.clone();
      if matches!((&_source0).as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_512{ .. }) {
        ::dafny_runtime::int!(64)
      } else {
        if matches!((&_source0).as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384{ .. }) {
          ::dafny_runtime::int!(48)
        } else {
          ::dafny_runtime::int!(32)
        }
      }
    }
    pub fn Digest(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut r#__let_tmp_rhs2: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput> = input.clone();
      let mut digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs2.digestAlgorithm().clone();
      let mut message: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs2.message().clone();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out45 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out45 = ::dafny_runtime::MaybePlacebo::from(crate::ExternDigest::_default::Digest(&digestAlgorithm, &message));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out45.read());
      if valueOrError0.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      let mut value: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(value.cardinality() == crate::r#_Digest_Compile::_default::Length(&digestAlgorithm), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Incorrect length digest from ExternDigest.")
              })));
      if valueOrError1.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: value.clone()
            }));
      return res.read();
    }
  }
}
pub mod ECDH {
  pub use ::std::fmt::Debug;
  pub use ::dafny_runtime::DafnyPrint;
  pub use ::std::cmp::Eq;
  pub use ::std::hash::Hash;
  pub use ::std::default::Default;
  pub use ::std::convert::AsRef;

  pub struct _default {}

  impl _default {
    pub fn GenerateEccKeyPair(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out46 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out46 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::KeyGeneration::GenerateKeyPair(input.eccCurve()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out46.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>>());
        return output.read();
      };
      let mut keyPair: ::std::rc::Rc<crate::ECDH::EccKeyPair> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput::GenerateECCKeyPairOutput {
                    eccCurve: input.eccCurve().clone(),
                    privateKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey::ECCPrivateKey {
                          pem: keyPair.privateKey().clone()
                        }),
                    publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey::ECCPublicKey {
                          der: keyPair.publicKey().clone()
                        })
                  })
            }));
      return output.read();
    }
    pub fn GetPublicKeyFromPrivate(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out47 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out47 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::ECCUtils::GetPublicKey(input.eccCurve(), input.privateKey()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out47.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>>());
        return output.read();
      };
      let mut publicKey: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput::GetPublicKeyFromPrivateKeyOutput {
                    eccCurve: input.eccCurve().clone(),
                    privateKey: input.privateKey().clone(),
                    publicKey: publicKey.clone()
                  })
            }));
      return output.read();
    }
    pub fn ValidatePublicKey(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out48 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out48 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::ECCUtils::ValidatePublicKey(input.eccCurve(), input.publicKey()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out48.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>>());
        return output.read();
      };
      let mut result: bool = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput::ValidatePublicKeyOutput {
                    success: result
                  })
            }));
      return output.read();
    }
    pub fn DeriveSharedSecret(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out49 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out49 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::DeriveSharedSecret::CalculateSharedSecret(input.eccCurve(), input.privateKey(), input.publicKey()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out49.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>>());
        return output.read();
      };
      let mut derivedSharedSecret: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput::DeriveSharedSecretOutput {
                    sharedSecret: derivedSharedSecret.clone()
                  })
            }));
      return output.read();
    }
    pub fn CompressPublicKey(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out50 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out50 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::ECCUtils::CompressPublicKey(input.publicKey().der(), input.eccCurve()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out50.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>>());
        return output.read();
      };
      let mut compressedPublicKey: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput::CompressPublicKeyOutput {
                    compressedPublicKey: compressedPublicKey.clone()
                  })
            }));
      return output.read();
    }
    pub fn DecompressPublicKey(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out51 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out51 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::ECCUtils::DecompressPublicKey(input.compressedPublicKey(), input.eccCurve()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out51.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>>());
        return output.read();
      };
      let mut decompressedPublicKey: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput::DecompressPublicKeyOutput {
                    publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey::ECCPublicKey {
                          der: decompressedPublicKey.clone()
                        })
                  })
            }));
      return output.read();
    }
    pub fn ParsePublicKey(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out52 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out52 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::ECDH::ECCUtils::ParsePublicKey(input.publicKey()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out52.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>>());
        return output.read();
      };
      let mut derPublicKey: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput::ParsePublicKeyOutput {
                    publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey::ECCPublicKey {
                          der: derPublicKey.clone()
                        })
                  })
            }));
      return output.read();
    }
    pub fn CreateExternEccKeyGenSuccess(output: &::std::rc::Rc<crate::ECDH::EccKeyPair>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternEccKeyGenFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::ECDH::EccKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternGetPublicKeyFromPrivateSuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternGetPublicKeyFromPrivateError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternValidatePublicKeySuccess(output: bool) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output
        })
    }
    pub fn CreateExternValidatePublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternDerivesharedSecretSuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternDerivesharedSecretError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternCompressPublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternCompressPublicKeySuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternDecompressPublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternDecompressPublicKeySuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternParsePublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateExternParsePublicKeySuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateGetInfinityPublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateGetInfinityPublicKeySuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateGetOutOfBoundsPublicKeyError(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateGetOutOfBoundsPublicKeySuccess(output: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
  }

  #[derive(PartialEq, Clone)]
  pub enum EccKeyPair {
    EccKeyPair {
      privateKey: ::dafny_runtime::Sequence<u8>,
      publicKey: ::dafny_runtime::Sequence<u8>
    }
  }

  impl EccKeyPair {
    pub fn privateKey(&self) -> &::dafny_runtime::Sequence<u8> {
      match self {
        EccKeyPair::EccKeyPair{privateKey, publicKey, } => privateKey,
      }
    }
    pub fn publicKey(&self) -> &::dafny_runtime::Sequence<u8> {
      match self {
        EccKeyPair::EccKeyPair{privateKey, publicKey, } => publicKey,
      }
    }
  }

  impl Debug
    for EccKeyPair {
    fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
      ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
    }
  }

  impl DafnyPrint
    for EccKeyPair {
    fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
      match self {
        EccKeyPair::EccKeyPair{privateKey, publicKey, } => {
          write!(_formatter, "ECDH.EccKeyPair.EccKeyPair(")?;
          ::dafny_runtime::DafnyPrint::fmt_print(privateKey, _formatter, false)?;
          write!(_formatter, ", ")?;
          ::dafny_runtime::DafnyPrint::fmt_print(publicKey, _formatter, false)?;
          write!(_formatter, ")")?;
          Ok(())
        },
      }
    }
  }

  impl Eq
    for EccKeyPair {}

  impl Hash
    for EccKeyPair {
    fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
      match self {
        EccKeyPair::EccKeyPair{privateKey, publicKey, } => {
          ::std::hash::Hash::hash(privateKey, _state);
          ::std::hash::Hash::hash(publicKey, _state)
        },
      }
    }
  }

  impl Default
    for EccKeyPair {
    fn default() -> EccKeyPair {
      EccKeyPair::EccKeyPair {
        privateKey: ::std::default::Default::default(),
        publicKey: ::std::default::Default::default()
      }
    }
  }

  impl AsRef<EccKeyPair>
    for &EccKeyPair {
    fn as_ref(&self) -> Self {
      self
    }
  }
}
pub mod ExternDigest {
  pub struct _default {}

  impl _default {
    pub fn CreateDigestSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateDigestFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }
}
pub mod ExternRandom {
  pub struct _default {}

  impl _default {
    pub fn CreateGenerateBytesSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateGenerateBytesFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }
}
pub mod r#_HKDF_Compile {
  pub struct _default {}

  impl _default {
    pub fn Extract(hmac: &::dafny_runtime::Object<crate::HMAC::HMac>, salt: &::dafny_runtime::Sequence<u8>, ikm: &::dafny_runtime::Sequence<u8>) -> ::dafny_runtime::Sequence<u8> {
      let mut prk = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      ::dafny_runtime::md!(hmac).Init(salt);
      ::dafny_runtime::md!(hmac).BlockUpdate(ikm);
      let mut _out53 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out53 = ::dafny_runtime::MaybePlacebo::from(::dafny_runtime::md!(hmac).GetResult());
      prk = ::dafny_runtime::MaybePlacebo::from(_out53.read());
      prk = ::dafny_runtime::MaybePlacebo::from(prk.read());
      return prk.read();
    }
    pub fn Expand(hmac: &::dafny_runtime::Object<crate::HMAC::HMac>, prk: &::dafny_runtime::Sequence<u8>, info: &::dafny_runtime::Sequence<u8>, expectedLength: &::dafny_runtime::DafnyInt, digest: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>) -> ::dafny_runtime::Sequence<u8> {
      let mut okm = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut hashLength: ::dafny_runtime::DafnyInt = crate::r#_Digest_Compile::_default::Length(digest);
      let mut n: ::dafny_runtime::DafnyInt = (::dafny_runtime::euclidian_division)(hashLength.clone() + expectedLength.clone() - ::dafny_runtime::int!(1), hashLength.clone());
      ::dafny_runtime::md!(hmac).Init(prk);
      let mut t_prev: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>;
      let mut t_n: ::dafny_runtime::Sequence<u8> = t_prev.clone();
      let mut i: ::dafny_runtime::DafnyInt = ::dafny_runtime::int!(1);
      while i.clone() <= n.clone() {
        ::dafny_runtime::md!(hmac).BlockUpdate(&t_prev);
        ::dafny_runtime::md!(hmac).BlockUpdate(info);
        ::dafny_runtime::md!(hmac).BlockUpdate(&::dafny_runtime::seq![::dafny_runtime::truncate!(i.clone(), u8)]);
        let mut _out54 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
        _out54 = ::dafny_runtime::MaybePlacebo::from(::dafny_runtime::md!(hmac).GetResult());
        t_prev = _out54.read();
        t_n = t_n.concat(&t_prev);
        i = i.clone() + ::dafny_runtime::int!(1);
      };
      okm = ::dafny_runtime::MaybePlacebo::from(t_n.clone());
      if expectedLength.clone() < okm.read().cardinality() {
        okm = ::dafny_runtime::MaybePlacebo::from(okm.read().take(expectedLength));
      };
      return okm.read();
    }
    pub fn Hkdf(digest: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>, salt: &::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>>, ikm: &::dafny_runtime::Sequence<u8>, info: &::dafny_runtime::Sequence<u8>, L: &::dafny_runtime::DafnyInt) -> ::dafny_runtime::Sequence<u8> {
      let mut okm = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      if L.clone() == ::dafny_runtime::int!(0) {
        okm = ::dafny_runtime::MaybePlacebo::from(::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>);
        return okm.read();
      };
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out55 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out55 = ::dafny_runtime::MaybePlacebo::from(crate::HMAC::HMac::Build(digest));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out55.read());
      if !(!valueOrError0.read().IsFailure()) {
        panic!("Halt")
      };
      let mut hmac: ::dafny_runtime::Object<crate::HMAC::HMac> = valueOrError0.read().Extract();
      let mut hashLength: ::dafny_runtime::_System::nat = crate::r#_Digest_Compile::_default::Length(digest);
      let mut nonEmptySalt = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _source1: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> = salt.clone();
      if matches!((&_source1).as_ref(), mpl_standard_library::_Wrappers_Compile::Option::None{ .. }) {
        nonEmptySalt = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_StandardLibrary_Compile::_default::Fill::<u8>(&0, &hashLength));
      } else {
        let mut r#___mcc_h0: ::dafny_runtime::Sequence<u8> = _source1.value().clone();
        let mut s: ::dafny_runtime::Sequence<u8> = r#___mcc_h0.clone();
        nonEmptySalt = ::dafny_runtime::MaybePlacebo::from(s.clone());
      };
      let mut prk = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out56 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out56 = ::dafny_runtime::MaybePlacebo::from(crate::r#_HKDF_Compile::_default::Extract(&hmac, &nonEmptySalt.read(), ikm));
      prk = ::dafny_runtime::MaybePlacebo::from(_out56.read());
      let mut _out57 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out57 = ::dafny_runtime::MaybePlacebo::from(crate::r#_HKDF_Compile::_default::Expand(&hmac, &prk.read(), info, L, digest));
      okm = ::dafny_runtime::MaybePlacebo::from(_out57.read());
      return okm.read();
    }
  }
}
pub mod HMAC {
  pub use ::dafny_runtime::UpcastObject;
  pub use ::std::any::Any;
  pub use crate::_dafny_externs::HMAC::*;

  pub struct _default {}

  impl _default {
    pub fn CreateDigestSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateDigestFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }

  impl HMac {
    pub fn CreateHMacSuccess(hmac: &::dafny_runtime::Object<crate::HMAC::HMac>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: hmac.clone()
        })
    }
    pub fn CreateHMacFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }

  impl UpcastObject<dyn Any>
    for HMac {
    ::dafny_runtime::UpcastObjectFn!(dyn ::std::any::Any);
  }
}
pub mod r#_KdfCtr_Compile {
  pub struct _default {}

  impl _default {
    pub fn KdfCounterMode(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>((input.digestAlgorithm().clone() == ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}) || input.digestAlgorithm().clone() == ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {})) && (input.ikm().cardinality() == ::dafny_runtime::int!(32) || input.ikm().cardinality() == ::dafny_runtime::int!(48) || input.ikm().cardinality() == ::dafny_runtime::int!(66)) && matches!(input.nonce().as_ref(), mpl_standard_library::_Wrappers_Compile::Option::Some{ .. }) && (input.nonce().value().cardinality() == ::dafny_runtime::int!(16) || input.nonce().value().cardinality() == ::dafny_runtime::int!(32)) && (input.expectedLength().clone() == 32 || input.expectedLength().clone() == 64) && (::dafny_runtime::int!(0) < ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) * ::dafny_runtime::int!(8) && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) * ::dafny_runtime::int!(8) < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Kdf in Counter Mode input is invalid.")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut ikm: ::dafny_runtime::Sequence<u8> = input.ikm().clone();
      let mut label_: ::dafny_runtime::Sequence<u8> = input.purpose().UnwrapOr(&(::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>));
      let mut info: ::dafny_runtime::Sequence<u8> = input.nonce().UnwrapOr(&(::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>));
      let mut okm: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>;
      let mut internalLength: u32 = ::dafny_runtime::truncate!(::dafny_runtime::int!(4) + crate::r#_KdfCtr_Compile::_default::SEPARATION_INDICATOR().cardinality() + ::dafny_runtime::int!(4), u32);
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(true && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(internalLength) + label_.cardinality() + info.cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Input Length exceeds INT32_MAX_LIMIT")
              })));
      if valueOrError1.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut lengthBits: ::dafny_runtime::Sequence<u8> = mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::UInt32ToSeq((input.expectedLength().clone() * 8) as u32);
      let mut explicitInfo: ::dafny_runtime::Sequence<u8> = label_.concat(&crate::r#_KdfCtr_Compile::_default::SEPARATION_INDICATOR()).concat(&info).concat(&lengthBits);
      let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError2 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(4) + explicitInfo.cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("PRF input length exceeds INT32_MAX_LIMIT.")
              })));
      if valueOrError2.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError2.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut valueOrError3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out58 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out58 = ::dafny_runtime::MaybePlacebo::from(crate::r#_KdfCtr_Compile::_default::RawDerive(&ikm, &explicitInfo, input.expectedLength().clone(), 0, input.digestAlgorithm()));
      valueOrError3 = ::dafny_runtime::MaybePlacebo::from(_out58.read());
      if valueOrError3.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError3.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      okm = valueOrError3.read().Extract();
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: okm.clone()
            }));
      return output.read();
    }
    pub fn RawDerive(ikm: &::dafny_runtime::Sequence<u8>, explicitInfo: &::dafny_runtime::Sequence<u8>, length: i32, offset: i32, digestAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out59 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out59 = ::dafny_runtime::MaybePlacebo::from(crate::HMAC::HMac::Build(digestAlgorithm));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out59.read());
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut hmac: ::dafny_runtime::Object<crate::HMAC::HMac> = valueOrError0.read().Extract();
      ::dafny_runtime::md!(hmac).Init(ikm);
      let mut macLengthBytes: i32 = ::dafny_runtime::truncate!(crate::r#_Digest_Compile::_default::Length(digestAlgorithm), i32);
      let mut iterations: i32 = (::dafny_runtime::euclidian_division)(length + macLengthBytes - 1, macLengthBytes);
      let mut buffer: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>;
      let mut i: ::dafny_runtime::Sequence<u8> = mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::UInt32ToSeq(crate::r#_KdfCtr_Compile::_default::COUNTER_START_VALUE());
      let mut _hi0: i32 = iterations + 1;
      for iteration in ::dafny_runtime::integer_range(1, _hi0).map(::std::convert::Into::<i32>::into) {
        ::dafny_runtime::md!(hmac).BlockUpdate(&i);
        ::dafny_runtime::md!(hmac).BlockUpdate(explicitInfo);
        let mut tmp = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
        let mut _out60 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
        _out60 = ::dafny_runtime::MaybePlacebo::from(::dafny_runtime::md!(hmac).GetResult());
        tmp = ::dafny_runtime::MaybePlacebo::from(_out60.read());
        buffer = buffer.concat(&tmp.read());
        let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
        valueOrError1 = ::dafny_runtime::MaybePlacebo::from(crate::r#_KdfCtr_Compile::_default::Increment(&i));
        if valueOrError1.read().IsFailure() {
          output = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
          return output.read();
        };
        i = valueOrError1.read().Extract();
      }
      let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError2 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(buffer.cardinality() >= ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(length), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Failed to derive key of requested length")
              })));
      if valueOrError2.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError2.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: buffer.take(&::std::convert::Into::<::dafny_runtime::DafnyInt>::into(length))
            }));
      return output.read();
    }
    pub fn Increment(x: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      if x.get(&::dafny_runtime::int!(3)) < 255 {
        ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
            value: ::dafny_runtime::seq![x.get(&::dafny_runtime::int!(0)), x.get(&::dafny_runtime::int!(1)), x.get(&::dafny_runtime::int!(2)), x.get(&::dafny_runtime::int!(3)) + 1]
          })
      } else {
        if x.get(&::dafny_runtime::int!(2)) < 255 {
          ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::dafny_runtime::seq![x.get(&::dafny_runtime::int!(0)), x.get(&::dafny_runtime::int!(1)), x.get(&::dafny_runtime::int!(2)) + 1, 0]
            })
        } else {
          if x.get(&::dafny_runtime::int!(1)) < 255 {
            ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
                value: ::dafny_runtime::seq![x.get(&::dafny_runtime::int!(0)), x.get(&::dafny_runtime::int!(1)) + 1, 0, 0]
              })
          } else {
            if x.get(&::dafny_runtime::int!(0)) < 255 {
              ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
                  value: ::dafny_runtime::seq![x.get(&::dafny_runtime::int!(0)) + 1, 0, 0, 0]
                })
            } else {
              ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
                  error: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                        message: ::dafny_runtime::string_utf16_of("Unable to derive key material; may have exceeded limit.")
                      })
                })
            }
          }
        }
      }
    }
    pub fn SEPARATION_INDICATOR() -> ::dafny_runtime::Sequence<u8> {
      ::dafny_runtime::seq![0]
    }
    pub fn COUNTER_START_VALUE() -> u32 {
      1
    }
  }
}
pub mod RSAEncryption {
  pub struct _default {}

  impl _default {
    pub fn GenerateKeyPair(lengthBits: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBitsToGenerate) -> (::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey>) {
      let mut publicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey>>::new();
      let mut privateKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey>>::new();
      let mut pemPublic = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut pemPrivate = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out61 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out62 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let _x = crate::_dafny_externs::RSAEncryption::RSA::GenerateKeyPairExtern(lengthBits);
      _out61 = ::dafny_runtime::MaybePlacebo::from(_x.0);
      _out62 = ::dafny_runtime::MaybePlacebo::from(_x.1);
      pemPublic = ::dafny_runtime::MaybePlacebo::from(_out61.read());
      pemPrivate = ::dafny_runtime::MaybePlacebo::from(_out62.read());
      privateKey = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey::RSAPrivateKey {
              lengthBits: lengthBits,
              pem: pemPrivate.read()
            }));
      publicKey = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey::RSAPublicKey {
              lengthBits: lengthBits,
              pem: pemPublic.read()
            }));
      return (
          publicKey.read(),
          privateKey.read()
        );
    }
    pub fn GetRSAKeyModulusLength(publicKey: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut valueOrError0: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<u32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::_dafny_externs::RSAEncryption::RSA::GetRSAKeyModulusLengthExtern(publicKey);
      if valueOrError0.IsFailure() {
        valueOrError0.PropagateFailure::<i32>()
      } else {
        let mut length: u32 = valueOrError0.Extract();
        let mut valueOrError1: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(81) <= ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(length) && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(length) < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Unsupported length for RSA modulus.")
              }));
        if valueOrError1.IsFailure() {
          valueOrError1.PropagateFailure::<i32>()
        } else {
          ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<i32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: length as i32
            })
        }
      }
    }
    pub fn Decrypt(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(0) < input.privateKey().cardinality() && ::dafny_runtime::int!(0) < input.cipherText().cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut _out63 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out63 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::RSAEncryption::RSA::DecryptExtern(input.padding(), input.privateKey(), input.cipherText()));
      output = ::dafny_runtime::MaybePlacebo::from(_out63.read());
      return output.read();
    }
    pub fn Encrypt(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(0) < input.publicKey().cardinality() && ::dafny_runtime::int!(0) < input.plaintext().cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut _out64 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out64 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::RSAEncryption::RSA::EncryptExtern(input.padding(), input.publicKey(), input.plaintext()));
      output = ::dafny_runtime::MaybePlacebo::from(_out64.read());
      return output.read();
    }
    pub fn CreateGetRSAKeyModulusLengthExternSuccess(output: u32) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<u32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<u32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output
        })
    }
    pub fn CreateGetRSAKeyModulusLengthExternFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<u32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<u32, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateBytesSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateBytesFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }
}
pub mod r#_Random_Compile {
  pub struct _default {}

  impl _default {
    pub fn GenerateBytes(i: i32) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      let mut _out65 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
      _out65 = ::dafny_runtime::MaybePlacebo::from(crate::ExternRandom::_default::GenerateBytes(i));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out65.read());
      if valueOrError0.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      let mut value: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(value.cardinality() == ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(i), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Incorrect length from ExternRandom.")
              })));
      if valueOrError1.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return res.read();
      };
      res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: value.clone()
            }));
      return res.read();
    }
  }
}
pub mod Signature {
  pub use ::std::fmt::Debug;
  pub use ::dafny_runtime::DafnyPrint;
  pub use ::std::cmp::Eq;
  pub use ::std::hash::Hash;
  pub use ::std::default::Default;
  pub use ::std::convert::AsRef;

  pub struct _default {}

  impl _default {
    pub fn SignatureLength(signatureAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>) -> u16 {
      let mut _source2: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> = signatureAlgorithm.clone();
      if matches!((&_source2).as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm::ECDSA_P384{ .. }) {
        103
      } else {
        71
      }
    }
    pub fn FieldSize(signatureAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>) -> ::dafny_runtime::_System::nat {
      let mut _source3: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm> = signatureAlgorithm.clone();
      if matches!((&_source3).as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm::ECDSA_P384{ .. }) {
        ::dafny_runtime::int!(49)
      } else {
        ::dafny_runtime::int!(33)
      }
    }
    pub fn KeyGen(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut res = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out66 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out66 = ::dafny_runtime::MaybePlacebo::from(crate::_dafny_externs::Signature::ECDSA::ExternKeyGen(input.signatureAlgorithm()));
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out66.read());
      if valueOrError0.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>>());
        return res.read();
      };
      let mut sigKeyPair: ::std::rc::Rc<crate::Signature::SignatureKeyPair> = valueOrError0.read().Extract();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(sigKeyPair.verificationKey().cardinality() == crate::Signature::_default::FieldSize(input.signatureAlgorithm()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Incorrect verification-key length from ExternKeyGen.")
              })));
      if valueOrError1.read().IsFailure() {
        res = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>>());
        return res.read();
      };
      res = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyOutput::GenerateECDSASignatureKeyOutput {
                    signatureAlgorithm: input.signatureAlgorithm().clone(),
                    verificationKey: sigKeyPair.verificationKey().clone(),
                    signingKey: sigKeyPair.signingKey().clone()
                  })
            }));
      return res.read();
    }
    pub fn CreateExternKeyGenSuccess(output: &::std::rc::Rc<crate::Signature::SignatureKeyPair>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: output.clone()
        })
    }
    pub fn CreateExternKeyGenFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateSignSuccess(bytes: &::dafny_runtime::Sequence<u8>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: bytes.clone()
        })
    }
    pub fn CreateSignFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
    pub fn CreateVerifySuccess(b: bool) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
          value: b
        })
    }
    pub fn CreateVerifyFailure(error: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Failure {
          error: error.clone()
        })
    }
  }

  #[derive(PartialEq, Clone)]
  pub enum SignatureKeyPair {
    SignatureKeyPair {
      verificationKey: ::dafny_runtime::Sequence<u8>,
      signingKey: ::dafny_runtime::Sequence<u8>
    }
  }

  impl SignatureKeyPair {
    pub fn verificationKey(&self) -> &::dafny_runtime::Sequence<u8> {
      match self {
        SignatureKeyPair::SignatureKeyPair{verificationKey, signingKey, } => verificationKey,
      }
    }
    pub fn signingKey(&self) -> &::dafny_runtime::Sequence<u8> {
      match self {
        SignatureKeyPair::SignatureKeyPair{verificationKey, signingKey, } => signingKey,
      }
    }
  }

  impl Debug
    for SignatureKeyPair {
    fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
      ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
    }
  }

  impl DafnyPrint
    for SignatureKeyPair {
    fn fmt_print(&self, _formatter: &mut ::std::fmt::Formatter, _in_seq: bool) -> std::fmt::Result {
      match self {
        SignatureKeyPair::SignatureKeyPair{verificationKey, signingKey, } => {
          write!(_formatter, "Signature.SignatureKeyPair.SignatureKeyPair(")?;
          ::dafny_runtime::DafnyPrint::fmt_print(verificationKey, _formatter, false)?;
          write!(_formatter, ", ")?;
          ::dafny_runtime::DafnyPrint::fmt_print(signingKey, _formatter, false)?;
          write!(_formatter, ")")?;
          Ok(())
        },
      }
    }
  }

  impl Eq
    for SignatureKeyPair {}

  impl Hash
    for SignatureKeyPair {
    fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
      match self {
        SignatureKeyPair::SignatureKeyPair{verificationKey, signingKey, } => {
          ::std::hash::Hash::hash(verificationKey, _state);
          ::std::hash::Hash::hash(signingKey, _state)
        },
      }
    }
  }

  impl Default
    for SignatureKeyPair {
    fn default() -> SignatureKeyPair {
      SignatureKeyPair::SignatureKeyPair {
        verificationKey: ::std::default::Default::default(),
        signingKey: ::std::default::Default::default()
      }
    }
  }

  impl AsRef<SignatureKeyPair>
    for &SignatureKeyPair {
    fn as_ref(&self) -> Self {
      self
    }
  }
}
pub mod r#_WrappedHKDF_Compile {
  pub struct _default {}

  impl _default {
    pub fn Extract(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>((matches!(input.salt().as_ref(), mpl_standard_library::_Wrappers_Compile::Option::None{ .. }) || input.salt().value().cardinality() != ::dafny_runtime::int!(0)) && input.ikm().cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("HKDF Extract needs a salt and reasonable ikm.")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut r#__let_tmp_rhs3: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput> = input.clone();
      let mut digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs3.digestAlgorithm().clone();
      let mut salt: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> = r#__let_tmp_rhs3.salt().clone();
      let mut ikm: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs3.ikm().clone();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out67 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out67 = ::dafny_runtime::MaybePlacebo::from(crate::HMAC::HMac::Build(&digestAlgorithm));
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out67.read());
      if valueOrError1.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut hmac: ::dafny_runtime::Object<crate::HMAC::HMac> = valueOrError1.read().Extract();
      let mut prk = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out68 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out68 = ::dafny_runtime::MaybePlacebo::from(crate::r#_HKDF_Compile::_default::Extract(&hmac, &salt.UnwrapOr(&mpl_standard_library::_StandardLibrary_Compile::_default::Fill::<u8>(&0, &crate::r#_Digest_Compile::_default::Length(&digestAlgorithm))), &ikm));
      prk = ::dafny_runtime::MaybePlacebo::from(_out68.read());
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: prk.read()
            }));
      return output.read();
    }
    pub fn Expand(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(1) <= ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) <= (::dafny_runtime::int!(255) * crate::r#_Digest_Compile::_default::Length(input.digestAlgorithm())) && input.info().cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT() && crate::r#_Digest_Compile::_default::Length(input.digestAlgorithm()) == input.prk().cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("HKDF Expand needs valid input.")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut r#__let_tmp_rhs4: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput> = input.clone();
      let mut digestAlgorithm: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs4.digestAlgorithm().clone();
      let mut prk: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs4.prk().clone();
      let mut info: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs4.info().clone();
      let mut expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger = r#__let_tmp_rhs4.expectedLength().clone();
      let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut _out69 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::HMAC::HMac>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      _out69 = ::dafny_runtime::MaybePlacebo::from(crate::HMAC::HMac::Build(&digestAlgorithm));
      valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out69.read());
      if valueOrError1.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError1.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut hmac: ::dafny_runtime::Object<crate::HMAC::HMac> = valueOrError1.read().Extract();
      let mut omk = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out70 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out70 = ::dafny_runtime::MaybePlacebo::from(crate::r#_HKDF_Compile::_default::Expand(&hmac, &prk, &info, &::std::convert::Into::<::dafny_runtime::DafnyInt>::into(expectedLength), &digestAlgorithm));
      omk = ::dafny_runtime::MaybePlacebo::from(_out70.read());
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: omk.read()
            }));
      return output.read();
    }
    pub fn Hkdf(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
      valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(1) <= ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(input.expectedLength().clone()) <= (::dafny_runtime::int!(255) * crate::r#_Digest_Compile::_default::Length(input.digestAlgorithm())) && (matches!(input.salt().as_ref(), mpl_standard_library::_Wrappers_Compile::Option::None{ .. }) || input.salt().value().cardinality() != ::dafny_runtime::int!(0)) && input.info().cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT() && input.ikm().cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Wrapped Hkdf input is invalid.")
              })));
      if valueOrError0.read().IsFailure() {
        output = ::dafny_runtime::MaybePlacebo::from(valueOrError0.read().PropagateFailure::<::dafny_runtime::Sequence<u8>>());
        return output.read();
      };
      let mut r#__let_tmp_rhs5: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput> = input.clone();
      let mut digest: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs5.digestAlgorithm().clone();
      let mut salt: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Option<::dafny_runtime::Sequence<u8>>> = r#__let_tmp_rhs5.salt().clone();
      let mut ikm: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs5.ikm().clone();
      let mut info: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs5.info().clone();
      let mut expectedLength: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger = r#__let_tmp_rhs5.expectedLength().clone();
      let mut okm = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      let mut _out71 = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
      _out71 = ::dafny_runtime::MaybePlacebo::from(crate::r#_HKDF_Compile::_default::Hkdf(&digest, &salt, &ikm, &info, &::std::convert::Into::<::dafny_runtime::DafnyInt>::into(expectedLength)));
      okm = ::dafny_runtime::MaybePlacebo::from(_out71.read());
      output = ::dafny_runtime::MaybePlacebo::from(::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
              value: okm.read()
            }));
      return output.read();
    }
  }
}
pub mod r#_WrappedHMAC_Compile {
  pub struct _default {}

  impl _default {
    pub fn Digest(input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>) -> ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> {
      let mut valueOrError0: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(::dafny_runtime::int!(0) < input.key().cardinality(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
              message: ::dafny_runtime::string_utf16_of("Key MUST NOT be 0 bytes.")
            }));
      if valueOrError0.IsFailure() {
        valueOrError0.PropagateFailure::<::dafny_runtime::Sequence<u8>>()
      } else {
        let mut valueOrError1: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(input.message().cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
                message: ::dafny_runtime::string_utf16_of("Message over INT32_MAX_LIMIT")
              }));
        if valueOrError1.IsFailure() {
          valueOrError1.PropagateFailure::<::dafny_runtime::Sequence<u8>>()
        } else {
          let mut valueOrError2: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::HMAC::_default::Digest(input);
          if valueOrError2.IsFailure() {
            valueOrError2.PropagateFailure::<::dafny_runtime::Sequence<u8>>()
          } else {
            let mut value: ::dafny_runtime::Sequence<u8> = valueOrError2.Extract();
            ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
                value: value.clone()
              })
          }
        }
      }
    }
  }
}
pub mod _module {
    pub struct _default {}

    impl _default {
        pub fn _Test__Main_() -> () {
            let mut success: bool = true;
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestSignature.YCompression384: "#
                ))
            );
            crate::r#_TestSignature_Compile::_default::YCompression384();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestSignature.YCompression256: "#
                ))
            );
            crate::r#_TestSignature_Compile::_default::YCompression256();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestSignature.VerifyMessage384: "#
                ))
            );
            crate::r#_TestSignature_Compile::_default::VerifyMessage384();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestSignature.VerifyMessage256: "#
                ))
            );
            crate::r#_TestSignature_Compile::_default::VerifyMessage256();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesHKDF.TestCase1: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::TestCase1();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesGenerateRandomBytes.BasicGenerateRandomBytes: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesGenerateRandomBytes_Compile::_default::BasicGenerateRandomBytes();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"ConstantTimeTest.ConstantTimeTest: "#
                ))
            );
            crate::r#_ConstantTimeTest_Compile::_default::ConstantTimeTest();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestHKDF_Rfc5869TestVectors.ExpectRFCTestVectors: "#
                ))
            );
            crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::ExpectRFCTestVectors();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestKDFK_TestVectors.ExpectInternalTestVectors: "#
                ))
            );
            crate::r#_TestKDFK__TestVectors_Compile::_default::ExpectInternalTestVectors();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesRSA.RSAEncryptTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::RSAEncryptTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesRSA.GetRSAKeyModulusLength: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::GetRSAKeyModulusLength();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesAES.AESDecryptTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesAES_Compile::_default::AESDecryptTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesAES.AESEncryptTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesAES_Compile::_default::AESEncryptTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesHMAC.HMACTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesHMAC_Compile::_default::HMACTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesDigest.DigestTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesDigest_Compile::_default::DigestTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesHMacDigest.DigestTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::DigestTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestKeyGen: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestKeyGen();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestGetPublicKeyFromPrivatePem: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestGetPublicKeyFromPrivatePem();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestGetPublicKeyFromPrivateIncorrectCruve: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestGetPublicKeyFromPrivateIncorrectCruve();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeySuccess: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeySuccess();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeyFailure: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeyFailure();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeyFailurePointAtINFFailOnLoad: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeyFailurePointAtINFFailOnLoad(
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeyFailurePointAtINF: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeyFailurePointAtINF();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestValidatePublicKeyFailurePointGreaterThanP: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestValidatePublicKeyFailurePointGreaterThanP();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestGenerateSharedSecret: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestGenerateSharedSecret();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestCompressDecompressPublicKey: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestCompressDecompressPublicKey();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestCompressDecompressConstantPublicKeys: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestCompressDecompressConstantPublicKeys();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestPublicKeyValidationTestVectorsInfinity: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestPublicKeyValidationTestVectorsInfinity();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestECDH.TestPublicKeyValidationTestVectorsOutOfBounds: "#
                ))
            );
            crate::r#_TestECDH_Compile::_default::TestPublicKeyValidationTestVectorsOutOfBounds();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"TestAwsCryptographyPrimitivesAesKdfCtr.AesKdfCtrTests: "#
                ))
            );
            crate::r#_TestAwsCryptographyPrimitivesAesKdfCtr_Compile::_default::AesKdfCtrTests();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                    r#"PASSED
"#
                ))
            );
            if !success {
                panic!("Halt")
            };
            return ();
        }
    }
}
pub mod r#_ConstantTime_Compile {
    pub struct _default {}

    impl _default {
        pub fn Compare(
            a: &::dafny_runtime::Sequence<u8>,
            b: &::dafny_runtime::Sequence<u8>,
            acc: u8,
        ) -> u8 {
            let mut _r0 = a.clone();
            let mut _r1 = b.clone();
            let mut _r2 = acc;
            'TAIL_CALL_START: loop {
                let a = _r0;
                let b = _r1;
                let acc = _r2;
                if a.cardinality() == ::dafny_runtime::int!(0) {
                    return acc;
                } else {
                    let mut x: u8 = a.get(&::dafny_runtime::int!(0)) as u8
                        ^ b.get(&::dafny_runtime::int!(0)) as u8;
                    let mut _in0: ::dafny_runtime::Sequence<u8> = a.drop(&::dafny_runtime::int!(1));
                    let mut _in1: ::dafny_runtime::Sequence<u8> = b.drop(&::dafny_runtime::int!(1));
                    let mut _in2: u8 = x | acc;
                    _r0 = _in0.clone();
                    _r1 = _in1.clone();
                    _r2 = _in2;
                    continue 'TAIL_CALL_START;
                }
            }
        }
        pub fn Equals(
            a: &::dafny_runtime::Sequence<u8>,
            b: &::dafny_runtime::Sequence<u8>,
        ) -> bool {
            crate::r#_ConstantTime_Compile::_default::Compare(a, b, (0) as u8) == (0) as u8
        }
    }
}
pub mod r#_ConstantTimeTest_Compile {
    pub struct _default {}

    impl _default {
        pub fn ConstantTimeTest() -> () {
            if !crate::r#_ConstantTime_Compile::_default::Equals(
                &(::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>),
                &(::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>),
            ) {
                panic!("Halt")
            };
            if !crate::r#_ConstantTime_Compile::_default::Equals(
                &::dafny_runtime::seq![1],
                &::dafny_runtime::seq![1],
            ) {
                panic!("Halt")
            };
            if !(!crate::r#_ConstantTime_Compile::_default::Equals(
                &::dafny_runtime::seq![1],
                &::dafny_runtime::seq![2],
            )) {
                panic!("Halt")
            };
            if !crate::r#_ConstantTime_Compile::_default::Equals(
                &::dafny_runtime::seq![1, 2, 3],
                &::dafny_runtime::seq![1, 2, 3],
            ) {
                panic!("Halt")
            };
            if !(!crate::r#_ConstantTime_Compile::_default::Equals(
                &::dafny_runtime::seq![2, 2, 3],
                &::dafny_runtime::seq![1, 2, 3],
            )) {
                panic!("Halt")
            };
            if !(!crate::r#_ConstantTime_Compile::_default::Equals(
                &::dafny_runtime::seq![1, 2, 3],
                &::dafny_runtime::seq![1, 2, 4],
            )) {
                panic!("Halt")
            };
            return ();
        }
    }

    #[test]
    pub fn ConstantTimeTest() {
        _default::ConstantTimeTest()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesAES_Compile {
    pub struct _default {}

    impl _default {
        pub fn AESDecryptTests() -> () {
            crate::r#_TestAwsCryptographyPrimitivesAES_Compile::_default::BasicAESDecryptTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput::AESDecryptInput {
            encAlg: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM::AES_GCM {
                  keyLength: 32,
                  tagLength: 16,
                  ivLength: 12
                }),
            key: ::dafny_runtime::seq![1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            cipherTxt: ::dafny_runtime::seq![102, 165, 173, 47],
            authTag: ::dafny_runtime::seq![54, 200, 18, 56, 172, 194, 174, 23, 239, 151, 47, 180, 143, 232, 142, 184],
            iv: ::dafny_runtime::seq![2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            aad: ::dafny_runtime::seq![3, 3, 3, 3]
          }), &::dafny_runtime::seq![97, 115, 100, 102]);
            return ();
        }
        pub fn AESEncryptTests() -> () {
            crate::r#_TestAwsCryptographyPrimitivesAES_Compile::_default::BasicAESEncryptTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput::AESEncryptInput {
            encAlg: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AES_GCM::AES_GCM {
                  keyLength: 32,
                  tagLength: 16,
                  ivLength: 12
                }),
            iv: ::dafny_runtime::seq![2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            key: ::dafny_runtime::seq![1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            msg: ::dafny_runtime::seq![97, 115, 100, 102],
            aad: ::dafny_runtime::seq![3, 3, 3, 3]
          }));
            return ();
        }
        pub fn BasicAESDecryptTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput>,
            expectedOutput: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out0 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out0.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out1 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::AESDecrypt(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out1.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e00: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e10: ::dafny_runtime::Sequence<u8> = expectedOutput.clone();
            if !(_e00.clone() == _e10.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e00));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e10));
                panic!("Halt")
            };
            return ();
        }
        pub fn BasicAESEncryptTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptInput>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out2 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out2.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out3 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::AESEncrypt(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out3.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESEncryptOutput> = valueOrError1.read().Extract();
            let mut decryptInput: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::AESDecryptInput::AESDecryptInput {
            encAlg: input.encAlg().clone(),
            key: input.key().clone(),
            cipherTxt: output.cipherText().clone(),
            authTag: output.authTag().clone(),
            iv: input.iv().clone(),
            aad: input.aad().clone()
          });
            crate::r#_TestAwsCryptographyPrimitivesAES_Compile::_default::BasicAESDecryptTest(
                &decryptInput,
                input.msg(),
            );
            return ();
        }
    }

    #[test]
    pub fn AESDecryptTests() {
        _default::AESDecryptTests()
    }

    #[test]
    pub fn AESEncryptTests() {
        _default::AESEncryptTests()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesAesKdfCtr_Compile {
    pub struct _default {}

    impl _default {
        pub fn AesKdfCtrTests() -> () {
            let mut key: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                138, 39, 30, 72, 206, 182, 214, 144, 245, 34, 28, 219, 204, 175, 198, 23, 132, 234,
                125, 246, 130, 54, 251, 60, 137, 120, 166, 245, 0, 150, 79, 107
            ];
            let mut nonce: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                66, 32, 73, 11, 207, 79, 97, 80, 11, 22, 236, 247, 42, 6, 222, 165
            ];
            let mut goal: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                143, 128, 174, 191, 9, 171, 140, 22, 40, 143, 11, 239, 249, 101, 61, 120, 176, 23,
                233, 210, 125, 72, 114, 70, 209, 170, 206, 96, 24, 112, 215, 169, 100, 136, 162,
                231, 208, 24, 135, 121, 223, 13, 239, 180
            ];
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(
                crate::AesKdfCtr::_default::AesKdfCtrStream(&nonce, &key, 44),
            );
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut result: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
            let mut _e01: ::dafny_runtime::DafnyInt = result.cardinality();
            let mut _e11: ::dafny_runtime::DafnyInt = ::dafny_runtime::int!(44);
            if !(_e01.clone() == _e11.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e01));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e11));
                panic!("Halt")
            };
            let mut _e02: ::dafny_runtime::Sequence<u8> = goal.clone();
            let mut _e12: ::dafny_runtime::Sequence<u8> = result.clone();
            if !(_e02.clone() == _e12.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e02));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e12));
                panic!("Halt")
            };
            key = ::dafny_runtime::seq![
                212, 191, 10, 32, 13, 55, 22, 101, 189, 182, 186, 119, 202, 16, 175, 49, 103, 82,
                87, 190, 13, 142, 103, 201, 98, 84, 228, 47, 142, 96, 61, 167
            ];
            nonce = ::dafny_runtime::seq![
                135, 1, 132, 66, 198, 216, 26, 105, 47, 97, 246, 192, 186, 187, 54, 129
            ];
            goal = ::dafny_runtime::seq![
                11, 154, 37, 42, 116, 143, 238, 68, 62, 135, 225, 71, 98, 224, 135, 18
            ];
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(
                crate::AesKdfCtr::_default::AesKdfCtrStream(&nonce, &key, 16),
            );
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            result = valueOrError1.read().Extract();
            let mut _e03: ::dafny_runtime::DafnyInt = result.cardinality();
            let mut _e13: ::dafny_runtime::DafnyInt = ::dafny_runtime::int!(16);
            if !(_e03.clone() == _e13.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e03));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e13));
                panic!("Halt")
            };
            let mut _e04: ::dafny_runtime::Sequence<u8> = goal.clone();
            let mut _e14: ::dafny_runtime::Sequence<u8> = result.clone();
            if !(_e04.clone() == _e14.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e04));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e14));
                panic!("Halt")
            };
            key = ::dafny_runtime::seq![
                106, 72, 42, 47, 58, 213, 111, 196, 126, 37, 46, 203, 150, 153, 188, 53, 32, 194,
                159, 196, 221, 90, 124, 70, 45, 252, 99, 98, 42, 68, 94, 19
            ];
            nonce = ::dafny_runtime::seq![
                13, 247, 32, 159, 220, 254, 69, 218, 42, 110, 159, 42, 209, 244, 79, 232
            ];
            goal = ::dafny_runtime::seq![
                150, 218, 139, 126, 166, 233, 178, 123, 229, 210, 40, 218, 141, 26, 127, 208, 124,
                197, 212, 69, 251, 71, 73, 90, 47, 134, 46, 7, 215, 208, 194, 180, 174, 110, 1, 57,
                16, 37, 16, 235, 93, 138, 25, 180, 85, 16, 229, 165, 238, 36, 56, 131, 247, 31, 64,
                23, 249, 67, 153, 94, 23, 243, 69, 11
            ];
            let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, crate::software::amazon::cryptography::primitives::internaldafny::types::OpaqueError>>>::new();
            valueOrError2 = ::dafny_runtime::MaybePlacebo::from(
                crate::AesKdfCtr::_default::AesKdfCtrStream(&nonce, &key, 64),
            );
            if !(!valueOrError2.read().IsFailure()) {
                panic!("Halt")
            };
            result = valueOrError2.read().Extract();
            let mut _e05: ::dafny_runtime::DafnyInt = result.cardinality();
            let mut _e15: ::dafny_runtime::DafnyInt = ::dafny_runtime::int!(64);
            if !(_e05.clone() == _e15.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e05));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e15));
                panic!("Halt")
            };
            let mut _e06: ::dafny_runtime::Sequence<u8> = goal.clone();
            let mut _e16: ::dafny_runtime::Sequence<u8> = result.clone();
            if !(_e06.clone() == _e16.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e06));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e16));
                panic!("Halt")
            };
            return ();
        }
    }

    #[test]
    pub fn AesKdfCtrTests() {
        _default::AesKdfCtrTests()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesDigest_Compile {
    pub struct _default {}

    impl _default {
        pub fn DigestTests() -> () {
            crate::r#_TestAwsCryptographyPrimitivesDigest_Compile::_default::BasicDigestTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}), &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![240, 228, 194, 247, 108, 88, 145, 110, 194, 88, 242, 70, 133, 27, 234, 9, 29, 20, 212, 36, 122, 47, 195, 225, 134, 148, 70, 27, 24, 22, 225, 59]);
            crate::r#_TestAwsCryptographyPrimitivesDigest_Compile::_default::BasicDigestTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}), &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![166, 158, 125, 243, 11, 36, 192, 66, 236, 84, 12, 203, 189, 191, 177, 86, 44, 133, 120, 112, 56, 200, 133, 116, 156, 30, 64, 142, 45, 98, 250, 54, 100, 44, 208, 7, 95, 163, 81, 232, 34, 226, 184, 165, 145, 57, 205, 157]);
            crate::r#_TestAwsCryptographyPrimitivesDigest_Compile::_default::BasicDigestTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_512 {}), &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![64, 27, 9, 234, 179, 192, 19, 212, 202, 84, 146, 43, 184, 2, 190, 200, 253, 83, 24, 25, 43, 10, 117, 242, 1, 216, 179, 114, 116, 41, 8, 15, 179, 55, 89, 26, 189, 62, 68, 69, 59, 149, 69, 85, 183, 160, 129, 46, 16, 129, 195, 155, 116, 2, 147, 247, 101, 234, 231, 49, 245, 166, 94, 209]);
            return ();
        }
        pub fn BasicDigestTest(
            digestAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
            message: &::dafny_runtime::Sequence<u8>,
            expectedDigest: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out4 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out4 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out4.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut input: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestInput::DigestInput {
            digestAlgorithm: digestAlgorithm.clone(),
            message: message.clone()
          });
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out5 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out5 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::Digest(::dafny_runtime::md!(client.clone()), &input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out5.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e07: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e17: ::dafny_runtime::_System::nat =
                crate::r#_Digest_Compile::_default::Length(digestAlgorithm);
            if !(_e07.clone() == _e17.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e07));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e17));
                panic!("Halt")
            };
            let mut _e08: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e18: ::dafny_runtime::Sequence<u8> = expectedDigest.clone();
            if !(_e08.clone() == _e18.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e08));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e18));
                panic!("Halt")
            };
            return ();
        }
    }

  //   #[test]
  //   pub fn DigestTests() {
  //     println!("Skipping 2");
  // // _default::DigestTests()
  //   }
}
pub mod r#_TestAwsCryptographyPrimitivesGenerateRandomBytes_Compile {
    pub struct _default {}

    impl _default {
        pub fn BasicGenerateRandomBytes() -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out6 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out6 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out6.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut length: i32 = 5;
            let mut input: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRandomBytesInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRandomBytesInput::GenerateRandomBytesInput {
            length: length
          });
            let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out7 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out7 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::GenerateRandomBytes(::dafny_runtime::md!(client.clone()), &input));
            output = ::dafny_runtime::MaybePlacebo::from(_out7.read());
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(output.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut value: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e09: ::dafny_runtime::DafnyInt = value.cardinality();
            let mut _e19: ::dafny_runtime::DafnyInt =
                ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(length);
            if !(_e09.clone() == _e19.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e09));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e19));
                panic!("Halt")
            };
            return ();
        }
    }

    #[test]
    pub fn BasicGenerateRandomBytes() {
        _default::BasicGenerateRandomBytes()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesHKDF_Compile {
    pub struct _default {}

    impl _default {
        pub fn TestCase1() -> () {
            let mut _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {});
            let mut IKM: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
                11
            ];
            let mut salt: ::dafny_runtime::Sequence<u8> =
                ::dafny_runtime::seq![0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
            let mut info: ::dafny_runtime::Sequence<u8> =
                ::dafny_runtime::seq![240, 241, 242, 243, 244, 245, 246, 247, 248, 249];
            let mut L: i32 = 42;
            let mut PRK: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199,
                59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229
            ];
            let mut OKM: ::dafny_runtime::Sequence<u8> = ::dafny_runtime::seq![
                60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10,
                144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184,
                135, 24, 88, 101
            ];
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicExtractTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput::HkdfExtractInput {
            digestAlgorithm: _hash.clone(),
            salt: ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                  value: salt.clone()
                }),
            ikm: IKM.clone()
          }), &PRK);
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicExpandTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput::HkdfExpandInput {
            digestAlgorithm: _hash.clone(),
            prk: PRK.clone(),
            info: info.clone(),
            expectedLength: L
          }), &OKM);
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicHkdfTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput::HkdfInput {
            digestAlgorithm: _hash.clone(),
            salt: ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                  value: salt.clone()
                }),
            ikm: IKM.clone(),
            info: info.clone(),
            expectedLength: L
          }), &OKM);
            return ();
        }
        pub fn BasicExtractTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput>,
            expectedPRK: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out8 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out8 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out8.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out9 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out9 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::HkdfExtract(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out9.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e010: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e110: ::dafny_runtime::_System::nat =
                crate::r#_Digest_Compile::_default::Length(input.digestAlgorithm());
            if !(_e010.clone() == _e110.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e010));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e110));
                panic!("Halt")
            };
            let mut _e011: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e111: ::dafny_runtime::Sequence<u8> = expectedPRK.clone();
            if !(_e011.clone() == _e111.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e011));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e111));
                panic!("Halt")
            };
            return ();
        }
        pub fn BasicExpandTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput>,
            expectedOKM: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out10 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out10 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out10.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out11 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out11 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::HkdfExpand(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out11.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e012: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e112: ::dafny_runtime::_System::nat =
                ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(
                    input.expectedLength().clone(),
                );
            if !(_e012.clone() == _e112.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e012));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e112));
                panic!("Halt")
            };
            let mut _e013: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e113: ::dafny_runtime::Sequence<u8> = expectedOKM.clone();
            if !(_e013.clone() == _e113.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e013));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e113));
                panic!("Halt")
            };
            return ();
        }
        pub fn BasicHkdfTest(
            input: &::std::rc::Rc<
                crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput,
            >,
            expectedOKM: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out12 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out12 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out12.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out13 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out13 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::Hkdf(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out13.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e014: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e114: ::dafny_runtime::_System::nat =
                ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(
                    input.expectedLength().clone(),
                );
            if !(_e014.clone() == _e114.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e014));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e114));
                panic!("Halt")
            };
            let mut _e015: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e115: ::dafny_runtime::Sequence<u8> = expectedOKM.clone();
            if !(_e015.clone() == _e115.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e015));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e115));
                panic!("Halt")
            };
            return ();
        }
    }

    #[test]
    pub fn TestCase1() {
        _default::TestCase1()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesHMAC_Compile {
    pub struct _default {}

    impl _default {
        pub fn HMACTests() -> () {
            crate::r#_TestAwsCryptographyPrimitivesHMAC_Compile::_default::BasicHMACTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}), &::dafny_runtime::seq![1, 2, 3, 4], &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![55, 107, 186, 241, 51, 255, 154, 169, 106, 133, 2, 248, 54, 230, 193, 147, 212, 179, 154, 66, 43, 52, 108, 181, 144, 152, 19, 101, 117, 99, 204, 134]);
            crate::r#_TestAwsCryptographyPrimitivesHMAC_Compile::_default::BasicHMACTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}), &::dafny_runtime::seq![1, 2, 3, 4], &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![90, 206, 234, 81, 173, 76, 235, 148, 203, 139, 195, 46, 251, 14, 97, 110, 146, 49, 147, 24, 240, 1, 17, 231, 58, 104, 146, 53, 144, 167, 11, 112, 7, 39, 122, 15, 58, 53, 144, 91, 16, 223, 51, 98, 30, 88, 23, 166]);
            crate::r#_TestAwsCryptographyPrimitivesHMAC_Compile::_default::BasicHMACTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_512 {}), &::dafny_runtime::seq![1, 2, 3, 4], &::dafny_runtime::seq![97, 115, 100, 102], &::dafny_runtime::seq![100, 23, 173, 215, 39, 67, 51, 165, 149, 53, 87, 84, 145, 58, 221, 155, 239, 182, 249, 134, 147, 191, 143, 224, 140, 165, 190, 221, 183, 15, 6, 102, 203, 77, 238, 64, 10, 138, 61, 64, 219, 79, 248, 249, 90, 102, 217, 188, 13, 2, 101, 96, 217, 242, 73, 254, 190, 217, 134, 33, 163, 137, 151, 183]);
            return ();
        }
        pub fn BasicHMACTest(
            digestAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
            key: &::dafny_runtime::Sequence<u8>,
            message: &::dafny_runtime::Sequence<u8>,
            expectedDigest: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out14 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out14 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out14.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut input: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput::HMacInput {
            digestAlgorithm: digestAlgorithm.clone(),
            key: key.clone(),
            message: message.clone()
          });
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::HMac(::dafny_runtime::rd!(client.clone()), &input));
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e016: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e116: ::dafny_runtime::_System::nat =
                crate::r#_Digest_Compile::_default::Length(digestAlgorithm);
            if !(_e016.clone() == _e116.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e016));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e116));
                panic!("Halt")
            };
            let mut _e017: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e117: ::dafny_runtime::Sequence<u8> = expectedDigest.clone();
            if !(_e017.clone() == _e117.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e017));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e117));
                panic!("Halt")
            };
            return ();
        }
    }

    #[test]
    pub fn HMACTests() {
        _default::HMACTests()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesHMacDigest_Compile {
    pub struct _default {}

    impl _default {
        pub fn DigestTests() -> () {
          let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out15 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out15 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            println!("B");
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out15.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            println!("Client : {:p}", client.as_ref());
            let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
            println!("Ca {}", scnt);
            println!("Client Ptr {:p} {:p}", &client, client.0.as_ref().unwrap().as_ref().get() as *const crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient as *const _);
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::HmacSHA_256(&::dafny_runtime::upcast_object::<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient, dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>()(client.clone()));
            let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
            println!("Cb {}", scnt);
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::HmacSHA_256(&::dafny_runtime::upcast_object::<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient, dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>()(client.clone()));
            let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
            println!("Cc {}", scnt);
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::HmacSHA_256(&::dafny_runtime::upcast_object::<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient, dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>()(client.clone()));
            let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
            println!("Cd {}", scnt);
            println!("D");
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::HmacSHA_384(&::dafny_runtime::upcast_object::<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient, dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>()(client.clone()));
            println!("E");
            crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::HmacSHA_512(&::dafny_runtime::upcast_object::<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient, dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>()(client.clone()));
            println!("F");
            return ();
        }
        pub fn HmacSHA_256(
            client: &::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>,
        ) -> () {
          let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
          println!("HmacSHA_256-a {}", scnt);

          // let _foo = crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::BasicHMacTest(client, &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput::HMacInput {
          //     digestAlgorithm: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          //     key: ::dafny_runtime::seq![1, 1, 1, 1],
          //     message: ::dafny_runtime::seq![97, 115, 100, 102]
          //   }), &::dafny_runtime::seq![93, 12, 86, 145, 123, 239, 169, 72, 195, 226, 204, 179, 103, 94, 195, 83, 134, 128, 226, 185, 184, 203, 98, 100, 115, 32, 7, 44, 172, 11, 81, 16]);
            // let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<(), ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            // valueOrError0 = ::dafny_runtime::MaybePlacebo::from(crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::BasicHMacTest(client, &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput::HMacInput {
            //     digestAlgorithm: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
            //     key: ::dafny_runtime::seq![1, 1, 1, 1],
            //     message: ::dafny_runtime::seq![97, 115, 100, 102]
            //   }), &::dafny_runtime::seq![93, 12, 86, 145, 123, 239, 169, 72, 195, 226, 204, 179, 103, 94, 195, 83, 134, 128, 226, 185, 184, 203, 98, 100, 115, 32, 7, 44, 172, 11, 81, 16]));
          // if !(!valueOrError0.read().IsFailure()) {
            //     panic!("Halt")
            // };
            // let mut _v0: () = valueOrError0.read().Extract();
            let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
            println!("HmacSHA_256-b {}", scnt);
              return ();
        }
        pub fn HmacSHA_384(
            client: &::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<(), ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::BasicHMacTest(client, &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput::HMacInput {
                digestAlgorithm: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
                key: ::dafny_runtime::seq![1, 1, 1, 1],
                message: ::dafny_runtime::seq![97, 115, 100, 102]
              }), &::dafny_runtime::seq![219, 44, 51, 60, 217, 57, 186, 208, 8, 69, 115, 185, 190, 136, 136, 1, 69, 143, 151, 148, 7, 66, 149, 193, 16, 225, 51, 85, 92, 176, 139, 249, 56, 93, 189, 11, 150, 21, 135, 54, 153, 37, 76, 68, 70, 77, 154, 124]));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut _v1: () = valueOrError0.read().Extract();
            return ();
        }
        pub fn HmacSHA_512(
            client: &::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<(), ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(crate::r#_TestAwsCryptographyPrimitivesHMacDigest_Compile::_default::BasicHMacTest(client, &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput::HMacInput {
                digestAlgorithm: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_512 {}),
                key: ::dafny_runtime::seq![1, 1, 1, 1],
                message: ::dafny_runtime::seq![97, 115, 100, 102]
              }), &::dafny_runtime::seq![49, 213, 21, 219, 23, 169, 195, 39, 177, 1, 15, 162, 233, 182, 208, 84, 226, 3, 27, 120, 75, 78, 85, 46, 220, 5, 166, 206, 79, 47, 25, 94, 88, 119, 211, 192, 148, 23, 252, 155, 98, 218, 97, 225, 38, 93, 83, 113, 139, 95, 101, 222, 154, 98, 244, 206, 88, 229, 6, 115, 226, 188, 152, 173]));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut _v2: () = valueOrError0.read().Extract();
            return ();
        }
        fn FakeHMac(thing : &dyn crate::software::amazon::cryptography::primitives::internaldafny::IAwsCryptographicPrimitivesClient, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>)
        {

        }
        fn FakeHMac2(thing : &dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::IAwsCryptographicPrimitivesClient>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>)
        {

        }
        fn FakeHMac3(thing : dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::IAwsCryptographicPrimitivesClient>, input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput>)
        {

        }
        pub fn BasicHMacTest(
            client: &::dafny_runtime::Object<dyn crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient>,
            input: &::std::rc::Rc<
                crate::software::amazon::cryptography::primitives::internaldafny::types::HMacInput,
            >,
            expectedDigest: &::dafny_runtime::Sequence<u8>,
        ) -> ::std::rc::Rc<
            mpl_standard_library::_Wrappers_Compile::Result<
                (),
                ::std::rc::Rc<
                    crate::software::amazon::cryptography::primitives::internaldafny::types::Error,
                >,
            >,
        > {
          let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
          println!("BasicHMacTest A, {}, {:?}", scnt, client);
          // let mut valueOrError0: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::HMac(::dafny_runtime::rd!(client.clone()), input);
          // Self::FakeHMac(::dafny_runtime::rd!(client.clone()), input);
          Self::FakeHMac3(client.clone(), input);
          let scnt = std::rc::Rc::strong_count(&client.0.as_ref().unwrap());
          println!("BasicHMacTest B, {}, {:?}", scnt, client);
          return Default::default();
            // if valueOrError0.IsFailure() {
            //     valueOrError0.PropagateFailure::<()>()
            // } else {
            //     let mut output: ::dafny_runtime::Sequence<u8> = valueOrError0.Extract();
            //     let mut valueOrError1: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(output.cardinality() == crate::r#_Digest_Compile::_default::Length(input.digestAlgorithm()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
            //     message: ::dafny_runtime::string_utf16_of("Error")
            //   }));
            //     if valueOrError1.IsFailure() {
            //         valueOrError1.PropagateFailure::<()>()
            //     } else {
            //         let mut valueOrError2: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Outcome<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = mpl_standard_library::_Wrappers_Compile::_default::Need::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>(output.clone() == expectedDigest.clone(), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError {
            //       message: ::dafny_runtime::string_utf16_of("Error")
            //     }));
            //         if valueOrError2.IsFailure() {
            //             valueOrError2.PropagateFailure::<()>()
            //         } else {
            //             ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Result::<(), ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>::Success {
            //     value: ()
            //   })
            //         }
            //     }
            // }
        }
    }

    #[test]
    pub fn DigestTests() {
        _default::DigestTests()
    }
}
pub mod r#_TestAwsCryptographyPrimitivesRSA_Compile {
    pub struct _default {}

    impl _default {
        pub fn RSAEncryptTests() -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out16 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out16 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out16.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut keys = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out17 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out17 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::GenerateRSAKeyPair(::dafny_runtime::md!(client.clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairInput::GenerateRSAKeyPairInput {
                lengthBits: 2048
              })));
            keys = ::dafny_runtime::MaybePlacebo::from(_out17.read());
            if !matches!(
                (&keys.read()).as_ref(),
                mpl_standard_library::_Wrappers_Compile::Result::Success { .. }
            ) {
                panic!("Halt")
            };
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::BasicRSAEncryptTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput::RSAEncryptInput {
            padding: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode::OAEP_SHA256 {}),
            publicKey: keys.read().value().publicKey().pem().clone(),
            plaintext: ::dafny_runtime::seq![97, 115, 100, 102]
          }), keys.read().value());
            return ();
        }
        pub fn GetRSAKeyModulusLength() -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out18 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out18 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out18.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                &crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::RSA_PUBLIC_2048(),
            ));
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut publicKey2048: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError1.read().Extract();
            let mut valueOrError2: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::GetRSAKeyModulusLength(::dafny_runtime::rd!(client.clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput {
              publicKey: publicKey2048.clone()
            }));
            if !(!valueOrError2.IsFailure()) {
                panic!("Halt")
            };
            let mut length2048: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput> = valueOrError2.Extract();
            let mut _e018: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits = length2048.length().clone();
            let mut _e118: i32 = 2048;
            if !(_e018 == _e118) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e018));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e118));
                panic!("Halt")
            };
            let mut valueOrError3 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError3 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                &crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::RSA_PUBLIC_3072(),
            ));
            if !(!valueOrError3.read().IsFailure()) {
                panic!("Halt")
            };
            let mut publicKey3072: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError3.read().Extract();
            let mut valueOrError4: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::GetRSAKeyModulusLength(::dafny_runtime::rd!(client.clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput {
              publicKey: publicKey3072.clone()
            }));
            if !(!valueOrError4.IsFailure()) {
                panic!("Halt")
            };
            let mut length3072: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput> = valueOrError4.Extract();
            let mut _e019: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits = length3072.length().clone();
            let mut _e119: i32 = 3072;
            if !(_e019 == _e119) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e019));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e119));
                panic!("Halt")
            };
            let mut valueOrError5 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError5 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                &crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::RSA_PUBLIC_4096(),
            ));
            if !(!valueOrError5.read().IsFailure()) {
                panic!("Halt")
            };
            let mut publicKey4096: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError5.read().Extract();
            let mut valueOrError6: ::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>> = crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::GetRSAKeyModulusLength(::dafny_runtime::rd!(client.clone()), &::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthInput::GetRSAKeyModulusLengthInput {
              publicKey: publicKey4096.clone()
            }));
            if !(!valueOrError6.IsFailure()) {
                panic!("Halt")
            };
            let mut length4096: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetRSAKeyModulusLengthOutput> = valueOrError6.Extract();
            let mut _e020: crate::software::amazon::cryptography::primitives::internaldafny::types::RSAModulusLengthBits = length4096.length().clone();
            let mut _e120: i32 = 4096;
            if !(_e020 == _e120) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e020));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e120));
                panic!("Halt")
            };
            return ();
        }
        pub fn BasicRSADecryptTests(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput>,
            expectedOutput: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out19 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out19 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out19.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out20 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out20 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::RSADecrypt(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out20.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e021: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e121: ::dafny_runtime::Sequence<u8> = expectedOutput.clone();
            if !(_e021.clone() == _e121.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e021));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e121));
                panic!("Halt")
            };
            return ();
        }
        pub fn BasicRSAEncryptTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput>,
            keypair: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out21 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out21 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out21.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out22 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out22 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::RSAEncrypt(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out22.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut decryptInput: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSADecryptInput::RSADecryptInput {
            padding: input.padding().clone(),
            privateKey: keypair.privateKey().pem().clone(),
            cipherText: output.clone()
          });
            crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::BasicRSADecryptTests(
                &decryptInput,
                input.plaintext(),
            );
            return ();
        }
        pub fn TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM() -> () {
            let mut allPadding: ::dafny_runtime::Set<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>> = (&({
          ::std::rc::Rc::new(move || -> ::dafny_runtime::Set<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>{
              let mut _coll0: ::dafny_runtime::SetBuilder<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>> = ::dafny_runtime::SetBuilder::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>::new();
              for r#__compr_0 in crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode::_AllSingletonConstructors() {
                let mut p: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode> = r#__compr_0.clone();
                _coll0.add(&p)
              }
              _coll0.build()
            })
        }))();
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(&crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::StaticPublicKeyFromGenerateRSAKeyPair()));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut PublicKeyFromGenerateRSAKeyPairPemBytes: mpl_standard_library::UTF8::ValidUTF8Bytes =
                valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(&crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::StaticPrivateKeyFromGenerateRSAKeyPair()));
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut PrivateKeyFromGenerateRSAKeyPairPemBytes: mpl_standard_library::UTF8::ValidUTF8Bytes =
                valueOrError1.read().Extract();
            let mut KeyFromGenerateRSAKeyPair: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput {
            publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey::RSAPublicKey {
                  lengthBits: 2048,
                  pem: PublicKeyFromGenerateRSAKeyPairPemBytes.clone()
                }),
            privateKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey::RSAPrivateKey {
                  lengthBits: 2048,
                  pem: PrivateKeyFromGenerateRSAKeyPairPemBytes.clone()
                })
          });
            while allPadding.clone() != ::dafny_runtime::set! {} {
                let mut padding = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>::new();
                'label_goto__ASSIGN_SUCH_THAT_0: loop {
                    for r#__assign_such_that_0 in (&allPadding).iter().cloned() {
                        padding =
                            ::dafny_runtime::MaybePlacebo::from(r#__assign_such_that_0.clone());
                        if allPadding.contains(&padding.read()) {
                            break 'label_goto__ASSIGN_SUCH_THAT_0;
                        }
                    }
                    panic!("Halt");
                    break;
                }
                crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::BasicRSAEncryptTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput::RSAEncryptInput {
              padding: padding.read(),
              publicKey: KeyFromGenerateRSAKeyPair.publicKey().pem().clone(),
              plaintext: ::dafny_runtime::seq![97, 115, 100, 102]
            }), &KeyFromGenerateRSAKeyPair);
                allPadding = allPadding.subtract(&::dafny_runtime::set! {padding.read()});
            }
            return ();
        }
        pub fn TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM() -> () {
            let mut allPadding: ::dafny_runtime::Set<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>> = (&({
          ::std::rc::Rc::new(move || -> ::dafny_runtime::Set<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>{
              let mut _coll1: ::dafny_runtime::SetBuilder<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>> = ::dafny_runtime::SetBuilder::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>::new();
              for r#__compr_1 in crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode::_AllSingletonConstructors() {
                let mut p: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode> = r#__compr_1.clone();
                _coll1.add(&p)
              }
              _coll1.build()
            })
        }))();
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(&crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::StaticPublicKeyFromTestVectors()));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut PublicKeyFromTestVectorsPemBytes: mpl_standard_library::UTF8::ValidUTF8Bytes =
                valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(&crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::StaticPrivateKeyFromTestVectors()));
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut PrivateKeyFromTestVectorsPemBytes: mpl_standard_library::UTF8::ValidUTF8Bytes =
                valueOrError1.read().Extract();
            let mut KeyFromTestVectorsPair: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateRSAKeyPairOutput::GenerateRSAKeyPairOutput {
            publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPublicKey::RSAPublicKey {
                  lengthBits: 4096,
                  pem: PublicKeyFromTestVectorsPemBytes.clone()
                }),
            privateKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPrivateKey::RSAPrivateKey {
                  lengthBits: 4096,
                  pem: PrivateKeyFromTestVectorsPemBytes.clone()
                })
          });
            while allPadding.clone() != ::dafny_runtime::set! {} {
                let mut padding = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::RSAPaddingMode>>::new();
                'label_goto__ASSIGN_SUCH_THAT_1: loop {
                    for r#__assign_such_that_1 in (&allPadding).iter().cloned() {
                        padding =
                            ::dafny_runtime::MaybePlacebo::from(r#__assign_such_that_1.clone());
                        if allPadding.contains(&padding.read()) {
                            break 'label_goto__ASSIGN_SUCH_THAT_1;
                        }
                    }
                    panic!("Halt");
                    break;
                }
                crate::r#_TestAwsCryptographyPrimitivesRSA_Compile::_default::BasicRSAEncryptTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::RSAEncryptInput::RSAEncryptInput {
              padding: padding.read(),
              publicKey: KeyFromTestVectorsPair.publicKey().pem().clone(),
              plaintext: ::dafny_runtime::seq![97, 115, 100, 102]
            }), &KeyFromTestVectorsPair);
                allPadding = allPadding.subtract(&::dafny_runtime::set! {padding.read()});
            }
            return ();
        }
        pub fn StaticPublicKeyFromGenerateRSAKeyPair(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PUBLIC KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0RbkftAm30eFm+o6JraW\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "AbWR+2grPfQk3i3w4eCsZHDQib6iUwX0MVADd2DjTnlkYa1DytDHRKfWHjtTniQ/\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "EdKbENIFC5mLgh1Max7n9nQ6bmo4EvH2s4pUr3YBSys/dXpRDUCD/Mt4G+qDE8DT\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "NSe8dqX5U44HwImQmKzvLYvD5gUY7eM5co4ZpfYrlRRVNkpv5qVNK7bz9KvQmKfP\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "bQfzyvOZgSqQyHKfxbCM6ByE8Dd0NoI1ALwBY8wCXn/+6q4xLWTywu4nGIXs5Vt7\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "vrMqwHSvYaNQKjUyPjsG3xPMwKruh30mGzc2KlKLZ+MiV+SNAiooqVkL6CxH4yJc\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of("NwIDAQAB\n"))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PUBLIC KEY-----\n",
                ))
        }
        pub fn StaticPrivateKeyFromGenerateRSAKeyPair(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PRIVATE KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRFuR+0CbfR4Wb\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "6jomtpYBtZH7aCs99CTeLfDh4KxkcNCJvqJTBfQxUAN3YONOeWRhrUPK0MdEp9Ye\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "O1OeJD8R0psQ0gULmYuCHUxrHuf2dDpuajgS8fazilSvdgFLKz91elENQIP8y3gb\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "6oMTwNM1J7x2pflTjgfAiZCYrO8ti8PmBRjt4zlyjhml9iuVFFU2Sm/mpU0rtvP0\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "q9CYp89tB/PK85mBKpDIcp/FsIzoHITwN3Q2gjUAvAFjzAJef/7qrjEtZPLC7icY\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "hezlW3u+syrAdK9ho1AqNTI+OwbfE8zAqu6HfSYbNzYqUotn4yJX5I0CKiipWQvo\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "LEfjIlw3AgMBAAECggEAWe7DTCpCtgHg3X2jEnixT73lsuGMy+KBoxDWjYkiDTea\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "8sxMrHIgpL86JnRFgMDk5MBuKsOfGhAooCs7XYdQm11fNh5nbiRWZZotftu1wQMg\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "CNLmGHv7dSD4KNoUV10cN+7rAsyvmKF5oWQ+idYD4labkNr1wTMTcYSZ7ZlgbNFr\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "ZFwsZizD4RrpwwyrpZ25f/H95p9fQrZXrB3Wt5aNn0uhTcQL0KfnvMamZNPfxj9b\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "j6CWpyXtFOMc8nuT4fKOh7q4A87UsduBBhdAk4m4m98WvlIZIUW89w3kzIfr9zCT\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "VxflBzeEDSM8+Sy1TJNRBBwhRnQ/gNLLD+e6/O/MTQKBgQD/vRxZvyJkWaRYkGeS\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "VVAZQJOSQUPpVC5U3y2ghV8Dm30BfMEtySdD9hXd635X7e0dvIqwxJAwFgJ+SYT2\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "NNE8wiIKolQH1h01cYK+kwAohB6vQPLymYwzc9HNcevCDFkt7VVRgnwUHk6BXz4T\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "LsF/jYTUdzCyFfjYWGTOEh7PkwKBgQDRTZSe2Tqua2Groi75tmXMAzI6jQsiBqTn\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Jv0es+IMWZyh2yMy9x6numM7IBBamgt+6hNEKaUmQxoEFbo0dUsEx35RH2Pdkr8X\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "IuXuh3IdRgRCV9WxnecBD32Cci9qLN1aaVJHfdA2dW4LAb7m4/GeuiS/8ZatXEm2\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Kf0YZAx/TQKBgEpbQtX5U9eXlMhHXEXY1kwxUXbx0PwThNEaftqwTJrw55y6GDTm\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "yqrg7ySyJu8L96hwvGZ/EGlazOjJGYa4fqnKzDkJT6NjpuR2F4yvkxk0qPNN0BWn\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "fXMsVrEEUYb/LiLDYc4sQUVcNnk5JwRO0OX0UM2xxg/RgaPtt4mPDTRPAoGBAJsY\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "1izv5CAjyniY8h5xHvYS2EGzCrDoI4J2zdLWkYd9UChQbsDxhnHcGHRTykqZJDOj\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "2SsFgS/dQYYNY7JDyJd+DQioLiSe/aNzZNdg3xr6K2XOGLhJvkh25han7qLLJCw/\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "J416mbQBSM43OPN3rjBk1560s2c7oBOxAa/1U51xAoGBAOYFMvdk6H359yaJGmsN\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "kY7lS6heh4cHfSM7Hw02lh/ovasdQm+afcnDWEW0XQYM6KQCcJiwbIK/kPkVsvJe\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "o6gynyWoHrrQuRdmffPvzT50paccJuupeHAtfOAue5y57FQUc4Xm4Qj3P7cQJr9z\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "UMCUAooEJcdmAUyVUy5BQc7P\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PRIVATE KEY-----\n",
                ))
        }
        pub fn StaticPublicKeyFromTestVectors(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PUBLIC KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs7RoNYEPAIws89VV+kra\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "rVv/4wbdmUAaAKWgWuxZi5na9GJSmnhCkqyLRm7wPbQY4LCoa5/IMUxkHLsYDPdu\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "udY0Qm0GcoxOlvJKHYo4RjF7HyiS34D6dvyO4Gd3aq0mZHoxSGCxW/7hf03wEMzc\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "iVJXWHXhaI0lD6nrzIEgLrE4L+3V2LeAQjvZsTKd+bYMqeZOL2syiVVIAU8POwAG\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "GVBroJoveFm/SUp6lCiN0M2kTeyQA2ax3QTtZSAa8nwrI7U52XOzVmdMicJsy2Pg\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "uW98te3MuODdK24yNkHIkYameP/Umf/SJshUJQd5a/TUp3XE+HhOWAumx22tIDlC\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "vZS11cuk2fp0WeHUnXaC19N5qWKfvHEKSugzty/z3lGP7ItFhrF2X1qJHeAAsL11\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "kjo6Lc48KsE1vKvbnW4VLyB3wdNiVvmUNO29tPXwaR0Q5Gbr3jk3nUzdkEHouHWQ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "41lubOHCCBN3V13mh/MgtNhESHjfmmOnh54ErD9saA1d7CjTf8g2wqmjEqvGSW6N\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "q7zhcWR2tp1olflS7oHzul4/I3hnkfL6Kb2xAWWaQKvg3mtsY2OPlzFEP0tR5UcH\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Pfp5CeS1Xzg7hN6vRICW6m4l3u2HJFld2akDMm1vnSz8RCbPW7jp7YBxUkWJmypM\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "tG7Yv2aGZXGbUtM8o1cZarECAwEAAQ==\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PUBLIC KEY-----",
                ))
        }
        pub fn StaticPrivateKeyFromTestVectors(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PRIVATE KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCztGg1gQ8AjCzz\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "1VX6StqtW//jBt2ZQBoApaBa7FmLmdr0YlKaeEKSrItGbvA9tBjgsKhrn8gxTGQc\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "uxgM92651jRCbQZyjE6W8kodijhGMXsfKJLfgPp2/I7gZ3dqrSZkejFIYLFb/uF/\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "TfAQzNyJUldYdeFojSUPqevMgSAusTgv7dXYt4BCO9mxMp35tgyp5k4vazKJVUgB\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Tw87AAYZUGugmi94Wb9JSnqUKI3QzaRN7JADZrHdBO1lIBryfCsjtTnZc7NWZ0yJ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "wmzLY+C5b3y17cy44N0rbjI2QciRhqZ4/9SZ/9ImyFQlB3lr9NSndcT4eE5YC6bH\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "ba0gOUK9lLXVy6TZ+nRZ4dSddoLX03mpYp+8cQpK6DO3L/PeUY/si0WGsXZfWokd\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "4ACwvXWSOjotzjwqwTW8q9udbhUvIHfB02JW+ZQ07b209fBpHRDkZuveOTedTN2Q\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Qei4dZDjWW5s4cIIE3dXXeaH8yC02ERIeN+aY6eHngSsP2xoDV3sKNN/yDbCqaMS\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "q8ZJbo2rvOFxZHa2nWiV+VLugfO6Xj8jeGeR8vopvbEBZZpAq+Dea2xjY4+XMUQ/\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "S1HlRwc9+nkJ5LVfODuE3q9EgJbqbiXe7YckWV3ZqQMybW+dLPxEJs9buOntgHFS\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "RYmbKky0bti/ZoZlcZtS0zyjVxlqsQIDAQABAoICAEr3m/GWIXgNAkPGX9PGnmtr\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "0dgX6SIhh7d1YOwNZV3DlYAV9HfUa5Fcwc1kQny7QRWbHOepBI7sW2dQ9buTDXIh\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "VjPP37yxo6d89EZWfxtpUP+yoXL0D4jL257qCvtJuJZ6E00qaVMDhXbiQKABlo8C\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "9sVEiABhwXBDZsctpwtTiykTgv6hrrPy2+H8R8MAm0/VcBCAG9kG5r8FCEmIvQKa\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "dgvNxrfiWNZuZ6yfLmpJH54SbhG9Kb4WbCKfvh4ihqyi0btRdSM6fMeLgG9o/zrc\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "s54B0kHeLOYNVo0j7FQpZBFeSIbmHfln4RKBh7ntrTke/Ejbh3NbiPvxWSP0P067\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "SYWPkQpip2q0ION81wSQZ1haP2GewFFu4IEjG3DlqqpKKGLqXrmjMufnildVFpBx\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "ir+MgvgQfEBoGEx0aElyO7QuRYaEiXeb/BhMZeC5O65YhJrWSuTVizh3xgJWjgfV\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "aYwYgxN8SBXBhXLIVvnPhadTqsW1C/aevLOk110eSFWcHf+FCK781ykIzcpXoRGX\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "OwWcZzC/fmSABS0yH56ow+I0tjdLIEEMhoa4/kkamioHOJ4yyB+W1DO6/DnMyQlx\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "g7y2WsAaIEBoWUARy776k70xPPMtYAxzFXI9KhqRVrPfeaRZ+ojeyLyr3GQGyyoo\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "cuGRdMUblsmODv4ixmOxAoIBAQDvkznvVYNdP3Eg5vQeLm/qsP6dLejLijBLeq9i\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "7DZH2gRpKcflXZxCkRjsKDDE+fgDcBYEp2zYfRIVvgrxlTQZdaSG+GoDcbjbNQn3\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "djCCtOOACioN/vg2zFlX4Bs6Q+NaV7g5qP5SUaxUBjuHLe7Nc+ZkyheMHuNYVLvk\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "HL/IoWyANpZYjMUU3xMbL/J29Gz7CPGr8Si28TihAHGfcNgn8S04OQZhTX+bU805\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "/+7B4XW47Mthg/u7hlqFl+YIAaSJYvWkEaVP1A9I7Ve0aMDSMWwzTg9cle2uVaL3\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "+PTzWY5coBlHKjqAg9ufhYSDhAqBd/JOSlv8RwcA3PDXJ6C/AoIBAQDABmXXYQky\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "7phExXBvkLtJt2TBGjjwulf4R8TC6W5F51jJuoqY/mTqYcLcOn2nYGVwoFvPsy/Q\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "CTjfODwJBXzbloXtYFR3PWAeL1Y6+7Cm+koMWIPJyVbD5Fzm+gZStM0GwP8FhDt2\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Wt8fWEyXmoLdAy6RAwiEmCagEh8o+13oBfwnBllbz7TxaErsUuR+XVgl/iHwztdv\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "cdJKyRgaFfWSh9aiO7EMV2rBGWsoX09SRvprPFAGx8Ffm7YcqIk34QXsQyc45Dyn\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "CwkvypxHoaB3ot/48FeFm9IubApb/ctv+EgkBfL4S4bdwRXS1rt+0+QihBoFyP2o\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "J91cdm4hEWCPAoIBAQC6l11hFaYZo0bWDGsHcr2B+dZkzxPoKznQH76n+jeQoLIc\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "wgjJkK4afm39yJOrZtEOxGaxu0CgIFFMk9ZsL/wC9EhvQt02z4TdXiLkFK5VrtMd\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "r0zv16y06VWQhqBOMf/KJlX6uq9RqADi9HO6pkC+zc0cpPXQEWKaMmygju+kMG2U\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Mm/IieMZjWCRJTfgBCE5J88qTsqaKagkZXcZakdAXKwOhQN+F2EStiM6UCZB5PrO\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "S8dfrO8ML+ki8Zqck8L1qhiNb5zkXtKExy4u+gNr8khGcT6vqqoSxOoH3mPRgOfL\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Jnppne8wlwIf7Vq3H8ka6zPSXEHma999gZcmy9t7AoIBAGbQhiLl79j3a0wXMvZp\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Vf5IVYgXFDnAbG2hb7a06bhAAIgyexcjzsC4C2+DWdgOgwHkuoPg+062QV8zauGh\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "sJKaa6cHlvIpSJeg3NjD/nfJN3CYzCd0yCIm2Z9Ka6xI5iYhm+pGPNhIG4Na8deS\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "gVL46yv1pc/o73VxfoGg5UzgN3xlp97Cva0sHEGguHr4W8Qr59xZw3wGQ4SLW35M\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "F6qXVNKUh12GSMCPbZK2RXBWVKqqJmca+WzJoJ6DlsT2lQdFhXCus9L007xlDXxF\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "C/hCmw1dEl+VaNo2Ou26W/zdwTKYhNlxBwsg4SB8nPNxXIsmlBBY54froFhriNfn\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "x/0CggEAUzz+VMtjoEWw2HSHLOXrO4EmwJniNgiiwfX3DfZE4tMNZgqZwLkq67ns\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "T0n3b0XfAOOkLgMZrUoOxPHkxFeyLLf7pAEJe7QNB+Qilw8e2zVqtiJrRk6uDIGJ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Sv+yM52zkImZAe2jOdU3KeUZxSMmb5vIoiPBm+tb2WupAg3YdpKn1/jWTpVmV/+G\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "UtTLVE6YpAyFp1gMxhutE9vfIS94ek+vt03AoEOlltt6hqZfv3xmY8vGuAjlnj12\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "zHaq+fhCRPsbsZkzJ9nIVdXYnNIEGtMGNnxax7tYRej/UXqyazbxHiJ0iPF4PeDn\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "dzxtGxpeTBi+KhKlca8SlCdCqYwG6Q==\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PRIVATE KEY-----",
                ))
        }
        pub fn RSA_PUBLIC_2048() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PUBLIC KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqBvECLsPdF1J5DOkaA1n\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "UrGwNT9ard3KSMaPypla/5Jhz0veCz1OSjnx35+FE3q7omHQBmKRs6XDkj4tJ5vh\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "1baw2yzgIAqW9lOXK64GiYy0maH2NfRxGbj5LhVq5T4YOkKh9D3GFbfT9/NpcsOZ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "M2HDX8Z+M0HM3XymtcfpHk5o6QF1lbBW+rDJEcYhPN0obBufCXaasgsBRP5Ei2b5\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "18xpy9M19By1yuC9mlNcpE5v5A8fq/qLLT4s34/6dnVxKX6gIoWDzDrUNrnPe0p5\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "pqZ1SHalrELMf/liXPrf94+0cF8g1fYVGGo+MZsG5/HRngLiskP25w5smMT51U1y\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of("gQIDAQAB\n"))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PUBLIC KEY-----",
                ))
        }
        pub fn RSA_PUBLIC_3072() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PUBLIC KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAnrUonUAKKpZE+LbQfq6I\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "gAR//GNnT7L6P3LCboXu44StJtvVyAmHZXPgdkxxT1EKLFx+Tys3B7jhgno9cs67\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Scf0pLjJAmXOVHa6881oxi5zeP0e6+KzOPugg3C+EknS2PSHTLsdTrkgZU+oUjde\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "AgRSgmWrp8aMM1WpoLmNcWC/Pi0mSziVnIzE3WhkZ2Ccetz/viRL60VHlTwNQPVa\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "7fqbcSqBxm/VjDzYvDwzmU+4GNEs5hrA2IFDxxsYZAU8HdASQM18A8W7n0Okaa4e\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "c4svyKVFkncbNCqetynLU0A5ny7I5WVXV7DNi2VMjD/mZsEt8IrwfuWSMKuIPxs/\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "Nb/4Psr7ZvbKSlaMwEpyReHvYYqM7dd6A4Y9FirnrpAPaqlfm8UFtHKQvUckxRoR\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "05kzNN2jIRJtMwGpn+40tiei7eBGMmIn41/dnkM7GOJau4BarSJMiREK1yH9hh1C\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "GbrQu6i0F9G0uBDITen9/uPX9cxK5pNHAxeWzr2UP1UzAgMBAAE=\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PUBLIC KEY-----",
                ))
        }
        pub fn RSA_PUBLIC_4096() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PUBLIC KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs86OIUN9RbdEdyQb2tGQ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "miDmmeJaYKanLB0lfWiuO85kJK8edZyLkHIzps81qwgVSzbMCBB7QGcMyPbb3wbE\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "B4EJ32v3cuMVUs6sOvOYV4g1c1Hi1WVqnCeH+3RSFBfb7RL7SvSUmilX2tNV6uZy\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "BmMSGBJ/IMzxoHjKSFn6r1ttwov8X5DmNTyIp4qG3qyL1qhpla1bUE5Nb6uMHI2v\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "qMM+8zSPcRN40CfaQATxevNs/69++XJ+5L1nKU9fMwust1GEbtJ6cIBwAuqlyMm9\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "CnZ+tn56FEVPrUrsQX35QRNjbi0jjKI8ItkdyJ5fLixCjJ20tCo5jeL5KJ32Rjuw\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "BlB2KQrgdw5VEMrMlTJz9oozUv8GFzjtS4kx+tAsWhji5s0jry4QFYG01Q4ezVPb\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "TYdxg1Yz265EyLmF0+/ZQtO1kQc7tXHD5Gzzwyqot/UdJwlXStUGB2yEe62HQ2LT\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "9Ly3V7rUDJzO44zuFVjqchRPYWNdiYl8BVP/ak2bMtcowk06T9bo1tRf4HJWfpIM\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "GF27MXqykKHxcmOb0UfGIfI0eUtkid4gJdCxhidiILj6SHpEr+oa/Oogz01rVCdm\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "mbWmgFxmiKse8NXNQR+7qhMYX5GgdeSbp/Lg24HF9mvnd0S2wHkC86lGyQtvzrsd\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "DdUJZ2jqiKvMLdMKNFHFGGUCAwEAAQ==\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PUBLIC KEY-----",
                ))
        }
    }

    #[test]
    pub fn RSAEncryptTests() {
        _default::RSAEncryptTests()
    }

    #[test]
    pub fn GetRSAKeyModulusLength() {
        _default::GetRSAKeyModulusLength()
    }

    #[test]
    pub fn TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM() {
        _default::TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM()
    }

    #[test]
    pub fn TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM() {
        _default::TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM()
    }
}
pub mod r#_TestECDH_Compile {
    pub struct _default {}

    impl _default {
        pub fn TestKeyGen() -> () {
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi0: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi0.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out23 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out23 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out23.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypair: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError0.read().Extract();
            }
            return ();
        }
        pub fn TestGetPublicKeyFromPrivatePem() -> () {
            let mut pemPrivateKeys: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PRIVATE(),
                crate::r#_TestECDH_Compile::_default::ECC_P384_PRIVATE(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PRIVATE()
            ];
            let mut derPublicKeys: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC(),
                crate::r#_TestECDH_Compile::_default::ECC_384_PUBLIC(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PUBLIC()
            ];
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi1: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi1.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<
                    ::std::rc::Rc<
                        mpl_standard_library::_Wrappers_Compile::Result<
                            mpl_standard_library::UTF8::ValidUTF8Bytes,
                            ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                        >,
                    >,
                >::new();
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                    &pemPrivateKeys.get(&i),
                ));
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut privateKey: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError0.read().Extract();
                let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out24 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out24 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &derPublicKeys.get(&i),
                    ),
                );
                looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out24.read());
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(
                        &looseHexPublicKey.read(),
                    );
                let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out25 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out25 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ParsePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput::ParsePublicKeyInput {
                  publicKey: publicKeyBytes.clone()
                })));
                valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out25.read());
                if !(!valueOrError1.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut expectedPublicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput> = valueOrError1.read().Extract();
                let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out26 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out26 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GetPublicKeyFromPrivate(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput {
                  eccCurve: curve.clone(),
                  privateKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey::ECCPrivateKey {
                        pem: privateKey.clone()
                      })
                })));
                valueOrError2 = ::dafny_runtime::MaybePlacebo::from(_out26.read());
                if !(!valueOrError2.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut publicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput> = valueOrError2.read().Extract();
                let mut _e022: ::dafny_runtime::Sequence<u8> = publicKey.publicKey().clone();
                let mut _e122: ::dafny_runtime::Sequence<u8> =
                    expectedPublicKey.publicKey().der().clone();
                if !(_e022.clone() == _e122.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e022));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e122));
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestGetPublicKeyFromPrivateIncorrectCruve() -> () {
            let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = crate::r#_TestECDH_Compile::_default::P384();
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                &crate::r#_TestECDH_Compile::_default::ECC_P256_PRIVATE(),
            ));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut privateKey: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError0.read().Extract();
            let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            >::new();
            let mut _out27 = ::dafny_runtime::MaybePlacebo::<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            >::new();
            _out27 = ::dafny_runtime::MaybePlacebo::from(
                crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                    &crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC(),
                ),
            );
            looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out27.read());
            let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                mpl_standard_library::_HexStrings_Compile::_default::FromHexString(&looseHexPublicKey.read());
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out28 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out28 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ParsePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyInput::ParsePublicKeyInput {
                publicKey: publicKeyBytes.clone()
              })));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out28.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut expectedPublicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ParsePublicKeyOutput> = valueOrError1.read().Extract();
            let mut publicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out29 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out29 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GetPublicKeyFromPrivate(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GetPublicKeyFromPrivateKeyInput::GetPublicKeyFromPrivateKeyInput {
                eccCurve: curve.clone(),
                privateKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPrivateKey::ECCPrivateKey {
                      pem: privateKey.clone()
                    })
              })));
            publicKey = ::dafny_runtime::MaybePlacebo::from(_out29.read());
            if !matches!(
                (&publicKey.read()).as_ref(),
                mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
            ) {
                panic!("Halt")
            };
            return ();
        }
        pub fn expectLooseHexString(
            s: &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            let mut s2 = ::dafny_runtime::MaybePlacebo::<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            >::new();
            if !mpl_standard_library::_HexStrings_Compile::_default::IsLooseHexString(s) {
                panic!("Halt")
            };
            s2 = ::dafny_runtime::MaybePlacebo::from(s.clone());
            return s2.read();
        }
        pub fn TestValidatePublicKeySuccess() -> () {
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi2: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi2.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out30 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out30 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out30.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypairA: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError0.read().Extract();
                let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out31 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out31 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out31.read());
                if !(!valueOrError1.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypairB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError1.read().Extract();
                let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out32 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out32 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: curve.clone(),
                  publicKey: keypairB.publicKey().der().clone()
                })));
                valueOrError2 = ::dafny_runtime::MaybePlacebo::from(_out32.read());
                if !(!valueOrError2.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut validPublicKeyB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput> = valueOrError2.read().Extract();
            }
            return ();
        }
        pub fn TestValidatePublicKeyFailure() -> () {
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi3: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi3.clone()) {
                let mut _hi4: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
                for j in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi4.clone()) {
                    let mut curve_i: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                    let mut curve_j: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&j);
                    let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    let mut _out33 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    _out33 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                    eccCurve: curve_i.clone()
                  })));
                    valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out33.read());
                    if !(!valueOrError0.read().IsFailure()) {
                        panic!("Halt")
                    };
                    let mut keypairA: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError0.read().Extract();
                    let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    let mut _out34 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    _out34 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                    eccCurve: curve_j.clone()
                  })));
                    valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out34.read());
                    if !(!valueOrError1.read().IsFailure()) {
                        panic!("Halt")
                    };
                    let mut keypairB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError1.read().Extract();
                    let mut validPublicKeyB = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    let mut _out35 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                    _out35 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                    eccCurve: curve_i.clone(),
                    publicKey: keypairB.publicKey().der().clone()
                  })));
                    validPublicKeyB = ::dafny_runtime::MaybePlacebo::from(_out35.read());
                    if curve_i.clone() != curve_j.clone() {
                        if !matches!(
                            (&validPublicKeyB.read()).as_ref(),
                            mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                        ) {
                            panic!("Halt")
                        }
                    } else {
                        if !matches!(
                            (&validPublicKeyB.read()).as_ref(),
                            mpl_standard_library::_Wrappers_Compile::Result::Success { .. }
                        ) {
                            panic!("Halt")
                        }
                    }
                }
            }
            return ();
        }
        pub fn TestValidatePublicKeyFailurePointAtINFFailOnLoad() -> () {
            let mut publicKeysWithPointsAtINF: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_256_PUBLIC_INF_FAIL_ON_LOAD(),
                crate::r#_TestECDH_Compile::_default::ECC_384_PUBLIC_INF_FAIL_ON_LOAD(),
                crate::r#_TestECDH_Compile::_default::ECC_521_PUBLIC_INF_FAIL_ON_LOAD()
            ];
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi5: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi5.clone()) {
                let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out36 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out36 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &publicKeysWithPointsAtINF.get(&i),
                    ),
                );
                looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out36.read());
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(
                        &looseHexPublicKey.read(),
                    );
                let mut validPublicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out37 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out37 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: supportedCurves.get(&i),
                  publicKey: publicKeyBytes.clone()
                })));
                validPublicKey = ::dafny_runtime::MaybePlacebo::from(_out37.read());
                if !matches!(
                    (&validPublicKey.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                };
                if !matches!(validPublicKey.read().error().as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError{ .. }) {
          panic!("Halt")
        };
                let mut errMsg: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                    validPublicKey.read().error().message().clone();
                if !(errMsg.clone()
                    == crate::r#_TestECDH_Compile::_default::BAD_X509_KEY_ERR_MSG_RUST()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_JAVA()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_NET6()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_NET48())
                {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestValidatePublicKeyFailurePointAtINF() -> () {
            let mut publicKeysWithPointsAtINF: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_256_PUBLIC_INF(),
                crate::r#_TestECDH_Compile::_default::ECC_384_PUBLIC_INF(),
                crate::r#_TestECDH_Compile::_default::ECC_521_PUBLIC_INF()
            ];
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi6: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi6.clone()) {
                let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out38 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out38 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &publicKeysWithPointsAtINF.get(&i),
                    ),
                );
                looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out38.read());
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(
                        &looseHexPublicKey.read(),
                    );
                let mut validPublicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out39 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out39 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: supportedCurves.get(&i),
                  publicKey: publicKeyBytes.clone()
                })));
                validPublicKey = ::dafny_runtime::MaybePlacebo::from(_out39.read());
                if !matches!(
                    (&validPublicKey.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad() -> () {
            let mut publicKeysWithPointsGreaterThanP: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC_GP_FAIL_ON_LOAD(),
                crate::r#_TestECDH_Compile::_default::ECC_P384_PUBLIC_GP_FAIL_ON_LOAD(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PUBLIC_GP_FAIL_ON_LOAD()
            ];
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi7: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi7.clone()) {
                let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out40 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out40 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &publicKeysWithPointsGreaterThanP.get(&i),
                    ),
                );
                looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out40.read());
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(
                        &looseHexPublicKey.read(),
                    );
                let mut validPublicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out41 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out41 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: supportedCurves.get(&i),
                  publicKey: publicKeyBytes.clone()
                })));
                validPublicKey = ::dafny_runtime::MaybePlacebo::from(_out41.read());
                if !matches!(
                    (&validPublicKey.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                };
                if !matches!(validPublicKey.read().error().as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError{ .. }) {
          panic!("Halt")
        };
                let mut errMsg: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                    validPublicKey.read().error().message().clone();
                if !(crate::r#_TestECDH_Compile::_default::seq_contains::<
                    ::dafny_runtime::DafnyCharUTF16,
                >(
                    &errMsg,
                    &crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_JAVA(),
                ) || errMsg.clone()
                    == crate::r#_TestECDH_Compile::_default::BAD_X509_KEY_ERR_MSG_RUST()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_NET6()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_NE48())
                {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestValidatePublicKeyFailurePointGreaterThanP() -> () {
            let mut publicKeysWithPointsGreaterThanP: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC_GP(),
                crate::r#_TestECDH_Compile::_default::ECC_P384_PUBLIC_GP(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PUBLIC_GP()
            ];
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi8: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi8.clone()) {
                let mut looseHexPublicKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out42 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out42 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &publicKeysWithPointsGreaterThanP.get(&i),
                    ),
                );
                looseHexPublicKey = ::dafny_runtime::MaybePlacebo::from(_out42.read());
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(
                        &looseHexPublicKey.read(),
                    );
                let mut validPublicKey = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out43 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out43 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: supportedCurves.get(&i),
                  publicKey: publicKeyBytes.clone()
                })));
                validPublicKey = ::dafny_runtime::MaybePlacebo::from(_out43.read());
                if !matches!(
                    (&validPublicKey.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestGenerateSharedSecret() -> () {
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi9: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi9.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out44 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out44 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out44.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypairA: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError0.read().Extract();
                let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out45 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out45 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out45.read());
                if !(!valueOrError1.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypairB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError1.read().Extract();
                if !(keypairA.privateKey().clone() != keypairB.privateKey().clone()
                    && keypairA.publicKey().clone() != keypairB.publicKey().clone())
                {
                    panic!("Halt")
                };
                let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out46 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out46 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: curve.clone(),
                  publicKey: keypairB.publicKey().der().clone()
                })));
                valueOrError2 = ::dafny_runtime::MaybePlacebo::from(_out46.read());
                if !(!valueOrError2.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut validPublicKeyB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput> = valueOrError2.read().Extract();
                let mut valueOrError3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out47 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out47 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DeriveSharedSecret(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput::DeriveSharedSecretInput {
                  eccCurve: curve.clone(),
                  privateKey: keypairA.privateKey().clone(),
                  publicKey: keypairB.publicKey().clone()
                })));
                valueOrError3 = ::dafny_runtime::MaybePlacebo::from(_out47.read());
                if !(!valueOrError3.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut sharedSecretA: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput> = valueOrError3.read().Extract();
                let mut valueOrError4 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out48 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out48 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DeriveSharedSecret(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretInput::DeriveSharedSecretInput {
                  eccCurve: curve.clone(),
                  privateKey: keypairB.privateKey().clone(),
                  publicKey: keypairA.publicKey().clone()
                })));
                valueOrError4 = ::dafny_runtime::MaybePlacebo::from(_out48.read());
                if !(!valueOrError4.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut sharedSecretB: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput> = valueOrError4.read().Extract();
                let mut _e023: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput> = sharedSecretA.clone();
                let mut _e123: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DeriveSharedSecretOutput> = sharedSecretB.clone();
                if !(_e023.clone() == _e123.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e023));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e123));
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestCompressDecompressPublicKey() -> () {
            let mut supportedCurves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi10: ::dafny_runtime::DafnyInt = supportedCurves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi10.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = supportedCurves.get(&i);
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out49 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out49 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::GenerateEccKeyPair(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairInput::GenerateECCKeyPairInput {
                  eccCurve: curve.clone()
                })));
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out49.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut keypair: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECCKeyPairOutput> = valueOrError0.read().Extract();
                let mut originalPublicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> = keypair.publicKey().clone();
                let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out50 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out50 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::CompressPublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput::CompressPublicKeyInput {
                  publicKey: originalPublicKey.clone(),
                  eccCurve: curve.clone()
                })));
                valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out50.read());
                if !(!valueOrError1.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut compressedPublicKeyResult: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput> = valueOrError1.read().Extract();
                if !(compressedPublicKeyResult.compressedPublicKey().clone()
                    != originalPublicKey.der().clone())
                {
                    panic!("Halt")
                };
                let mut compressedPublicKey: ::dafny_runtime::Sequence<u8> =
                    compressedPublicKeyResult.compressedPublicKey().clone();
                let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out51 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out51 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DecompressPublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput::DecompressPublicKeyInput {
                  compressedPublicKey: compressedPublicKey.clone(),
                  eccCurve: curve.clone()
                })));
                valueOrError2 = ::dafny_runtime::MaybePlacebo::from(_out51.read());
                if !(!valueOrError2.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut decompressedPublicKeyResult: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput> = valueOrError2.read().Extract();
                let mut decompressedPublicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> = decompressedPublicKeyResult.publicKey().clone();
                let mut _e024: ::dafny_runtime::Sequence<u8> = originalPublicKey.der().clone();
                let mut _e124: ::dafny_runtime::Sequence<u8> = decompressedPublicKey.der().clone();
                if !(_e024.clone() == _e124.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e024));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e124));
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestCompressDecompressConstantPublicKeys() -> () {
            let mut derX509PublicKeys: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC(),
                crate::r#_TestECDH_Compile::_default::ECC_384_PUBLIC(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PUBLIC()
            ];
            let mut compressedKeys: ::dafny_runtime::Sequence<
                ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
            > = ::dafny_runtime::seq![
                crate::r#_TestECDH_Compile::_default::ECC_P256_PUBLIC_COMPRESSED(),
                crate::r#_TestECDH_Compile::_default::ECC_384_PUBLIC_COMPRESSED(),
                crate::r#_TestECDH_Compile::_default::ECC_P521_PUBLIC_COMPRESSED()
            ];
            let mut curves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi11: ::dafny_runtime::DafnyInt = curves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi11.clone()) {
                let mut curve: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec> = curves.get(&i);
                let mut originalPublicKey: ::dafny_runtime::Sequence<
                    ::dafny_runtime::DafnyCharUTF16,
                > = derX509PublicKeys.get(&i);
                let mut publicKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(&originalPublicKey);
                let mut compressedKey = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                let mut _out52 = ::dafny_runtime::MaybePlacebo::<
                    ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                >::new();
                _out52 = ::dafny_runtime::MaybePlacebo::from(
                    crate::r#_TestECDH_Compile::_default::expectLooseHexString(
                        &compressedKeys.get(&i),
                    ),
                );
                compressedKey = ::dafny_runtime::MaybePlacebo::from(_out52.read());
                let mut compressedKeyBytes: ::dafny_runtime::Sequence<u8> =
                    mpl_standard_library::_HexStrings_Compile::_default::FromHexString(&compressedKey.read());
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out53 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out53 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::CompressPublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyInput::CompressPublicKeyInput {
                  publicKey: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey::ECCPublicKey {
                        der: publicKeyBytes.clone()
                      }),
                  eccCurve: curve.clone()
                })));
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out53.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut compressedPublicKeyResult: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::CompressPublicKeyOutput> = valueOrError0.read().Extract();
                let mut _e025: ::dafny_runtime::Sequence<u8> =
                    compressedPublicKeyResult.compressedPublicKey().clone();
                let mut _e125: ::dafny_runtime::Sequence<u8> = compressedKeyBytes.clone();
                if !(_e025.clone() == _e125.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e025));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e125));
                    panic!("Halt")
                };
                let mut compressedPublicKey: ::dafny_runtime::Sequence<u8> =
                    compressedPublicKeyResult.compressedPublicKey().clone();
                let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out54 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out54 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::DecompressPublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyInput::DecompressPublicKeyInput {
                  compressedPublicKey: compressedPublicKey.clone(),
                  eccCurve: curve.clone()
                })));
                valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out54.read());
                if !(!valueOrError1.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut decompressedPublicKeyResult: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DecompressPublicKeyOutput> = valueOrError1.read().Extract();
                let mut decompressedPublicKey: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECCPublicKey> = decompressedPublicKeyResult.publicKey().clone();
                let mut _e026: ::dafny_runtime::Sequence<u8> = publicKeyBytes.clone();
                let mut _e126: ::dafny_runtime::Sequence<u8> = decompressedPublicKey.der().clone();
                if !(_e026.clone() == _e126.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e026));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e126));
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestPublicKeyValidationTestVectorsInfinity() -> () {
            let mut curves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi12: ::dafny_runtime::DafnyInt = curves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi12.clone()) {
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out55 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out55 = ::dafny_runtime::MaybePlacebo::from(
                    crate::_dafny_externs::ECDH::ECCUtils::GetInfinityPublicKey(&curves.get(&i)),
                );
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out55.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut der_ecc_inf: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
                let mut validPublicKeyB = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out56 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out56 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: curves.get(&i),
                  publicKey: der_ecc_inf.clone()
                })));
                validPublicKeyB = ::dafny_runtime::MaybePlacebo::from(_out56.read());
                if !matches!(
                    (&validPublicKeyB.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                };
                if !matches!(validPublicKeyB.read().error().as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError{ .. }) {
          panic!("Halt")
        };
                let mut errMsg: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                    validPublicKeyB.read().error().message().clone();
                if !(errMsg.clone()
                    == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_JAVA()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::BAD_X509_KEY_ERR_MSG_RUST()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_NET6()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::INFINITY_POINT_ERR_MSG_NET48())
                {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn TestPublicKeyValidationTestVectorsOutOfBounds() -> () {
            let mut curves: ::dafny_runtime::Sequence<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec>> = ::dafny_runtime::seq![crate::r#_TestECDH_Compile::_default::P256(), crate::r#_TestECDH_Compile::_default::P384(), crate::r#_TestECDH_Compile::_default::P521()];
            let mut _hi13: ::dafny_runtime::DafnyInt = curves.cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi13.clone()) {
                let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out57 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out57 = ::dafny_runtime::MaybePlacebo::from(
                    crate::_dafny_externs::ECDH::ECCUtils::GetOutOfBoundsPublicKey(&curves.get(&i)),
                );
                valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out57.read());
                if !(!valueOrError0.read().IsFailure()) {
                    panic!("Halt")
                };
                let mut der_ecc_inf: ::dafny_runtime::Sequence<u8> = valueOrError0.read().Extract();
                let mut validPublicKeyB = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                let mut _out58 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyOutput>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
                _out58 = ::dafny_runtime::MaybePlacebo::from(crate::ECDH::_default::ValidatePublicKey(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ValidatePublicKeyInput::ValidatePublicKeyInput {
                  eccCurve: curves.get(&i),
                  publicKey: der_ecc_inf.clone()
                })));
                validPublicKeyB = ::dafny_runtime::MaybePlacebo::from(_out58.read());
                if !matches!(
                    (&validPublicKeyB.read()).as_ref(),
                    mpl_standard_library::_Wrappers_Compile::Result::Failure { .. }
                ) {
                    panic!("Halt")
                };
                if !matches!(validPublicKeyB.read().error().as_ref(), crate::software::amazon::cryptography::primitives::internaldafny::types::Error::AwsCryptographicPrimitivesError{ .. }) {
          panic!("Halt")
        };
                let mut errMsg: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                    validPublicKeyB.read().error().message().clone();
                if !(crate::r#_TestECDH_Compile::_default::seq_contains::<
                    ::dafny_runtime::DafnyCharUTF16,
                >(
                    &errMsg,
                    &crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_JAVA(),
                ) || errMsg.clone()
                    == crate::r#_TestECDH_Compile::_default::BAD_X509_KEY_ERR_MSG_RUST()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_NET6()
                    || errMsg.clone()
                        == crate::r#_TestECDH_Compile::_default::OUT_OF_BOUNDS_ERR_MSG_NE48())
                {
                    panic!("Halt")
                }
            }
            return ();
        }
        pub fn seq_contains<_T: ::dafny_runtime::DafnyTypeEq>(
            haystack: &::dafny_runtime::Sequence<_T>,
            needle: &::dafny_runtime::Sequence<_T>,
        ) -> bool {
            let mut _r0 = haystack.clone();
            let mut _r1 = needle.clone();
            'TAIL_CALL_START: loop {
                let haystack = _r0;
                let needle = _r1;
                if needle.cardinality() == ::dafny_runtime::int!(0) {
                    return true;
                } else {
                    if haystack.cardinality() == ::dafny_runtime::int!(0) {
                        return false;
                    } else {
                        if haystack.cardinality() < needle.cardinality() {
                            return false;
                        } else {
                            if needle.get(&::dafny_runtime::int!(0))
                                == haystack.get(&::dafny_runtime::int!(0))
                                && needle.drop(&::dafny_runtime::int!(1))
                                    <= haystack.drop(&::dafny_runtime::int!(1))
                            {
                                return true;
                            } else {
                                let mut _in3: ::dafny_runtime::Sequence<_T> =
                                    haystack.drop(&::dafny_runtime::int!(1));
                                let mut _in4: ::dafny_runtime::Sequence<_T> = needle.clone();
                                _r0 = _in3.clone();
                                _r1 = _in4.clone();
                                continue 'TAIL_CALL_START;
                            }
                        }
                    }
                }
            }
        }
        pub fn P256() -> ::std::rc::Rc<
            crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec,
        > {
            ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec::ECC_NIST_P256 {})
        }
        pub fn P384() -> ::std::rc::Rc<
            crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec,
        > {
            ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec::ECC_NIST_P384 {})
        }
        pub fn P521() -> ::std::rc::Rc<
            crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec,
        > {
            ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECDHCurveSpec::ECC_NIST_P521 {})
        }
        pub fn ECC_P256_PRIVATE() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PRIVATE KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PRIVATE KEY-----",
                ))
        }
        pub fn ECC_P384_PRIVATE() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PRIVATE KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PRIVATE KEY-----",
                ))
        }
        pub fn ECC_P521_PRIVATE() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("-----BEGIN PRIVATE KEY-----\n")
                .concat(&::dafny_runtime::string_utf16_of(
                    "MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of(
                    "C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n",
                ))
                .concat(&::dafny_runtime::string_utf16_of("Qg==\n"))
                .concat(&::dafny_runtime::string_utf16_of(
                    "-----END PRIVATE KEY-----",
                ))
        }
        pub fn ECC_P256_PUBLIC() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3059301306072a8648ce3d020106082a8648ce3d03010703420004a7520c7b4ab9478",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "4f227dcc7197dcddc108b3cf9715fec9be172e575c1610b199f008eec272a313489",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "e944c126391d8cd6085efbdc5bc96961981981a149b6bc",
            ))
        }
        pub fn ECC_384_PUBLIC() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3076301006072a8648ce3d020106052b81040022036200041ac8f5ba07769518a58505",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "905998c89f20e4daea5e6f54e2bcfd1461acbe7484bc32b04533ba0b06c248ab11a2",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "450d443c522904bbf89a6b5e3a66b9aadf",
            ))
        }
        pub fn ECC_P521_PUBLIC() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "30819b301006072a8648ce3d020106052b81040023038186000401de32732469d8769e",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb2",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "1d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39017df878ad9db941c8bd6e",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "dcdea45a151f0b7babcb5d53f1d90d5be2db564997f01dfeb3a55a11058a6be49805",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "e98f574e5a261534c5a685fcc86c2c6c0a2e93e942",
            ))
        }
        pub fn ECC_256_PUBLIC_INF_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3019301306072a8648ce3d020106082a8648ce3d03010703020000",
            )
        }
        pub fn ECC_384_PUBLIC_INF_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("3016301006072a8648ce3d020106052b8104002203020000")
        }
        pub fn ECC_521_PUBLIC_INF_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("3016301006072a8648ce3d020106052b8104002303020000")
        }
        pub fn BAD_X509_KEY_ERR_MSG_RUST(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("Invalid X509 Public Key.")
        }
        pub fn INFINITY_POINT_ERR_MSG_JAVA(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("encoded key spec not recognized: Point at infinity")
        }
        pub fn INFINITY_POINT_ERR_MSG_NET6(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("Point at infinity (Parameter 'q')")
        }
        pub fn INFINITY_POINT_ERR_MSG_NET48(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("Point at infinity\r\nParameter name: q")
        }
        pub fn ECC_256_PUBLIC_INF() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3059301306072a864886f70d0106082a864886f70d03010703420004000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000",
            ))
        }
        pub fn ECC_384_PUBLIC_INF() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3076301006072a864886f70d0106052b810400220362000400000000000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of("00000000000000"))
        }
        pub fn ECC_521_PUBLIC_INF() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3081ee3010060772a8648ce3d02106052b81040023038186000400000000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "0000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000",
            ))
        }
        pub fn ECC_P256_PUBLIC_GP_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3059301306072a8648ce3d020106082a8648ce3d03010703420004fffffffffffffffff",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffff",
            ))
        }
        pub fn ECC_P384_PUBLIC_GP_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3076301006072a8648ce3d020106052b8104002203620004fffffffffffffffffffffff",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "fffffffffffffffffffffffffffff",
            ))
        }
        pub fn ECC_P521_PUBLIC_GP_FAIL_ON_LOAD(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "30819b301006072a8648ce3d020106052b810400230381860004ffffffffffffffffffff",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "ffffffffffffffffffffffffffffffffff",
            ))
        }
        pub fn OUT_OF_BOUNDS_ERR_MSG_JAVA(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("encoded key spec not recognized: x value invalid for")
        }
        pub fn OUT_OF_BOUNDS_ERR_MSG_NET6(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("value invalid for Fp field element (Parameter 'x')")
        }
        pub fn OUT_OF_BOUNDS_ERR_MSG_NE48(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "value invalid for Fp field element\r\nParameter name: x",
            )
        }
        pub fn ECC_P256_PUBLIC_GP() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3059301306072a864886f70d0106082a864886f70d03010703420004000000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of("000000001"))
        }
        pub fn ECC_P384_PUBLIC_GP() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3076301006072a864886f70d0106052b810400220362000400000000000000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "0000000000000000000000000000001",
            ))
        }
        pub fn ECC_P521_PUBLIC_GP() -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "3081ee3010060772a8648ce3d02106052b8104002303818600040000000000000000000",
            )
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000000000000000000000000000000000000000000",
            ))
            .concat(&::dafny_runtime::string_utf16_of(
                "00000000000000000000000000000000001",
            ))
        }
        pub fn ECC_P256_PUBLIC_COMPRESSED(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of(
                "02a7520c7b4ab94784f227dcc7197dcddc108b3cf9715fec9be172e575c1610b19",
            )
        }
        pub fn ECC_384_PUBLIC_COMPRESSED(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("031ac8f5ba07769518a58505b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c905998")
        }
        pub fn ECC_P521_PUBLIC_COMPRESSED(
        ) -> ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            ::dafny_runtime::string_utf16_of("0201de32732469d8769e47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb21d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39")
        }
    }

    #[test]
    pub fn TestKeyGen() {
        _default::TestKeyGen()
    }

    #[test]
    pub fn TestGetPublicKeyFromPrivatePem() {
        _default::TestGetPublicKeyFromPrivatePem()
    }

    #[test]
    pub fn TestGetPublicKeyFromPrivateIncorrectCruve() {
        _default::TestGetPublicKeyFromPrivateIncorrectCruve()
    }

    #[test]
    pub fn TestValidatePublicKeySuccess() {
        _default::TestValidatePublicKeySuccess()
    }

    #[test]
    pub fn TestValidatePublicKeyFailure() {
        _default::TestValidatePublicKeyFailure()
    }

    #[test]
    pub fn TestValidatePublicKeyFailurePointAtINFFailOnLoad() {
        _default::TestValidatePublicKeyFailurePointAtINFFailOnLoad()
    }

    #[test]
    pub fn TestValidatePublicKeyFailurePointAtINF() {
        _default::TestValidatePublicKeyFailurePointAtINF()
    }

    #[test]
    pub fn TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad() {
        _default::TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad()
    }

    #[test]
    pub fn TestValidatePublicKeyFailurePointGreaterThanP() {
        _default::TestValidatePublicKeyFailurePointGreaterThanP()
    }

    #[test]
    pub fn TestGenerateSharedSecret() {
        _default::TestGenerateSharedSecret()
    }

    #[test]
    pub fn TestCompressDecompressPublicKey() {
        _default::TestCompressDecompressPublicKey()
    }

    #[test]
    pub fn TestCompressDecompressConstantPublicKeys() {
        _default::TestCompressDecompressConstantPublicKeys()
    }

    #[test]
    pub fn TestPublicKeyValidationTestVectorsInfinity() {
        _default::TestPublicKeyValidationTestVectorsInfinity()
    }

    #[test]
    pub fn TestPublicKeyValidationTestVectorsOutOfBounds() {
        _default::TestPublicKeyValidationTestVectorsOutOfBounds()
    }
}
pub mod r#_TestHKDF__Rfc5869TestVectors_Compile {
    pub use dafny_runtime::DafnyPrint;
    pub use std::cmp::Eq;
    pub use std::convert::AsRef;
    pub use std::default::Default;
    pub use std::fmt::Debug;
    pub use std::hash::Hash;

    pub struct _default {}

    impl _default {
        pub fn ExpectRFCTestVectors() -> () {
            let mut _hi14: ::dafny_runtime::DafnyInt =
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::testVectors()
                    .cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi14.clone()) {
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::ExpectTestVector(
                    &crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::testVectors()
                        .get(&i),
                )
            }
            return ();
        }
        pub fn ExpectTestVector(
            vector: &::std::rc::Rc<crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector>,
        ) -> () {
            let mut r#__let_tmp_rhs0: ::std::rc::Rc<
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector,
            > = vector.clone();
            let mut name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                r#__let_tmp_rhs0.name().clone();
            let mut _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs0._hash().clone();
            let mut IKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.IKM().clone();
            let mut salt: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.salt().clone();
            let mut info: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.info().clone();
            let mut L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger = r#__let_tmp_rhs0.L().clone();
            let mut PRK: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.PRK().clone();
            let mut OKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs0.OKM().clone();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(
                    &name.concat(&::dafny_runtime::string_utf16_of("\n"))
                )
            );
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicExtractTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExtractInput::HkdfExtractInput {
            digestAlgorithm: _hash.clone(),
            salt: if ::dafny_runtime::int!(0) < salt.cardinality() {
                ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                    value: salt.clone()
                  })
              } else {
                ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::None {})
              },
            ikm: IKM.clone()
          }), &PRK);
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicExpandTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfExpandInput::HkdfExpandInput {
            digestAlgorithm: _hash.clone(),
            prk: PRK.clone(),
            info: info.clone(),
            expectedLength: L
          }), &OKM);
            crate::r#_TestAwsCryptographyPrimitivesHKDF_Compile::_default::BasicHkdfTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::HkdfInput::HkdfInput {
            digestAlgorithm: _hash.clone(),
            salt: if ::dafny_runtime::int!(0) < salt.cardinality() {
                ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                    value: salt.clone()
                  })
              } else {
                ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::None {})
              },
            ikm: IKM.clone(),
            info: info.clone(),
            expectedLength: L
          }), &OKM);
            return ();
        }
        pub fn a1() -> ::std::rc::Rc<crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector>
        {
            ::std::rc::Rc::new(crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector::RFCTestVector {
          name: ::dafny_runtime::string_utf16_of("A.1.  Test Case 1"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
          salt: ::dafny_runtime::seq![0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
          info: ::dafny_runtime::seq![240, 241, 242, 243, 244, 245, 246, 247, 248, 249],
          L: 42,
          PRK: ::dafny_runtime::seq![7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229],
          OKM: ::dafny_runtime::seq![60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101]
        })
        }
        pub fn a2() -> ::std::rc::Rc<crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector>
        {
            ::std::rc::Rc::new(crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector::RFCTestVector {
          name: ::dafny_runtime::string_utf16_of("A.2.  Test Case 2"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
          salt: ::dafny_runtime::seq![96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175],
          info: ::dafny_runtime::seq![176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
          L: 82,
          PRK: ::dafny_runtime::seq![6, 166, 184, 140, 88, 83, 54, 26, 6, 16, 76, 156, 235, 53, 180, 92, 239, 118, 0, 20, 144, 70, 113, 1, 74, 25, 63, 64, 193, 95, 194, 68],
          OKM: ::dafny_runtime::seq![177, 30, 57, 141, 200, 3, 39, 161, 200, 231, 247, 140, 89, 106, 73, 52, 79, 1, 46, 218, 45, 78, 250, 216, 160, 80, 204, 76, 25, 175, 169, 124, 89, 4, 90, 153, 202, 199, 130, 114, 113, 203, 65, 198, 94, 89, 14, 9, 218, 50, 117, 96, 12, 47, 9, 184, 54, 119, 147, 169, 172, 163, 219, 113, 204, 48, 197, 129, 121, 236, 62, 135, 193, 76, 1, 213, 193, 243, 67, 79, 29, 135]
        })
        }
        pub fn a3() -> ::std::rc::Rc<crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector>
        {
            ::std::rc::Rc::new(crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector::RFCTestVector {
          name: ::dafny_runtime::string_utf16_of("A.3.  Test Case 3"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
          salt: ::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>,
          info: ::dafny_runtime::seq![] as ::dafny_runtime::Sequence<u8>,
          L: 42,
          PRK: ::dafny_runtime::seq![25, 239, 36, 163, 44, 113, 123, 22, 127, 51, 169, 29, 111, 100, 139, 223, 150, 89, 103, 118, 175, 219, 99, 119, 172, 67, 76, 28, 41, 60, 203, 4],
          OKM: ::dafny_runtime::seq![141, 164, 231, 117, 165, 99, 193, 143, 113, 95, 128, 42, 6, 60, 90, 49, 184, 161, 31, 92, 94, 225, 135, 158, 195, 69, 78, 95, 60, 115, 141, 45, 157, 32, 19, 149, 250, 164, 182, 26, 150, 200]
        })
        }
        pub fn testVectors() -> ::dafny_runtime::Sequence<
            ::std::rc::Rc<crate::r#_TestHKDF__Rfc5869TestVectors_Compile::RFCTestVector>,
        > {
            ::dafny_runtime::seq![
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::a1(),
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::a2(),
                crate::r#_TestHKDF__Rfc5869TestVectors_Compile::_default::a3()
            ]
        }
    }

    #[test]
    pub fn ExpectRFCTestVectors() {
        _default::ExpectRFCTestVectors()
    }

    #[derive(PartialEq, Clone)]
    pub enum RFCTestVector {
        RFCTestVector {
      name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
      _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
      IKM: ::dafny_runtime::Sequence<u8>,
      salt: ::dafny_runtime::Sequence<u8>,
      info: ::dafny_runtime::Sequence<u8>,
      L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
      PRK: ::dafny_runtime::Sequence<u8>,
      OKM: ::dafny_runtime::Sequence<u8>
    }
  }

    impl RFCTestVector {
        pub fn name(&self) -> &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => name,
            }
        }
        pub fn _hash(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>{
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => _hash,
            }
        }
        pub fn IKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => IKM,
            }
        }
        pub fn salt(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => salt,
            }
        }
        pub fn info(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => info,
            }
        }
        pub fn L(
            &self,
        ) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
        {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => L,
            }
        }
        pub fn PRK(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => PRK,
            }
        }
        pub fn OKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => OKM,
            }
        }
    }

    impl Debug for RFCTestVector {
        fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
            ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
        }
    }

    impl DafnyPrint for RFCTestVector {
        fn fmt_print(
            &self,
            _formatter: &mut ::std::fmt::Formatter,
            _in_seq: bool,
        ) -> std::fmt::Result {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => {
                    write!(
                        _formatter,
                        "TestHKDF__Rfc5869TestVectors_Compile.RFCTestVector.RFCTestVector("
                    )?;
                    ::dafny_runtime::DafnyPrint::fmt_print(name, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(_hash, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(IKM, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(salt, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(info, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(L, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(PRK, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(OKM, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                }
            }
        }
    }

    impl Eq for RFCTestVector {}

    impl Hash for RFCTestVector {
        fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
            match self {
                RFCTestVector::RFCTestVector {
                    name,
                    _hash,
                    IKM,
                    salt,
                    info,
                    L,
                    PRK,
                    OKM,
                } => {
                    ::std::hash::Hash::hash(name, _state);
                    ::std::hash::Hash::hash(_hash, _state);
                    ::std::hash::Hash::hash(IKM, _state);
                    ::std::hash::Hash::hash(salt, _state);
                    ::std::hash::Hash::hash(info, _state);
                    ::std::hash::Hash::hash(L, _state);
                    ::std::hash::Hash::hash(PRK, _state);
                    ::std::hash::Hash::hash(OKM, _state)
                }
            }
        }
    }

    impl Default for RFCTestVector {
        fn default() -> RFCTestVector {
            RFCTestVector::RFCTestVector {
                name: ::std::default::Default::default(),
                _hash: ::std::default::Default::default(),
                IKM: ::std::default::Default::default(),
                salt: ::std::default::Default::default(),
                info: ::std::default::Default::default(),
                L: ::std::default::Default::default(),
                PRK: ::std::default::Default::default(),
                OKM: ::std::default::Default::default(),
            }
        }
    }

    impl AsRef<RFCTestVector> for &RFCTestVector {
        fn as_ref(&self) -> Self {
            self
        }
    }
}
pub mod r#_TestKDF_Compile {
    pub struct _default {}

    impl _default {
        pub fn KdfRawDeriveTest(
            ikm: &::dafny_runtime::Sequence<u8>,
            info: &::dafny_runtime::Sequence<u8>,
            L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
            expectedOKM: &::dafny_runtime::Sequence<u8>,
            digestAlgorithm: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
        ) -> () {
            let mut output = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out59 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out59 = ::dafny_runtime::MaybePlacebo::from(
                crate::r#_KdfCtr_Compile::_default::RawDerive(ikm, info, L, 0, digestAlgorithm),
            );
            output = ::dafny_runtime::MaybePlacebo::from(_out59.read());
            if matches!(
                (&output.read()).as_ref(),
                mpl_standard_library::_Wrappers_Compile::Result::Success { .. }
            ) {
                let mut _e027: ::dafny_runtime::DafnyInt = output.read().value().cardinality();
                let mut _e127: ::dafny_runtime::_System::nat =
                    ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(L);
                if !(_e027.clone() == _e127.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e027));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e127));
                    panic!("Halt")
                };
                let mut _e028: ::dafny_runtime::Sequence<u8> = output.read().value().clone();
                let mut _e128: ::dafny_runtime::Sequence<u8> = expectedOKM.clone();
                if !(_e028.clone() == _e128.clone()) {
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Left:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e028));
                    print!(
                        "{}",
                        ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                            "Right:\n"
                        ))
                    );
                    print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e128));
                    panic!("Halt")
                }
            };
            return ();
        }
        pub fn KdfTest(
            input: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput>,
            expectedOKM: &::dafny_runtime::Sequence<u8>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out60 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out60 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::_default::AtomicPrimitives(&crate::software::amazon::cryptography::primitives::internaldafny::_default::DefaultCryptoConfig()));
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out60.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut client: ::dafny_runtime::Object<crate::software::amazon::cryptography::primitives::internaldafny::AtomicPrimitivesClient> = valueOrError0.read().Extract();
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out61 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out61 = ::dafny_runtime::MaybePlacebo::from(crate::software::amazon::cryptography::primitives::internaldafny::types::IAwsCryptographicPrimitivesClient::KdfCounterMode(::dafny_runtime::md!(client.clone()), input));
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out61.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut output: ::dafny_runtime::Sequence<u8> = valueOrError1.read().Extract();
            let mut _e029: ::dafny_runtime::DafnyInt = output.cardinality();
            let mut _e129: ::dafny_runtime::_System::nat =
                ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(
                    input.expectedLength().clone(),
                );
            if !(_e029.clone() == _e129.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e029));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e129));
                panic!("Halt")
            };
            let mut _e030: ::dafny_runtime::Sequence<u8> = output.clone();
            let mut _e130: ::dafny_runtime::Sequence<u8> = expectedOKM.clone();
            if !(_e030.clone() == _e130.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e030));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e130));
                panic!("Halt")
            };
            return ();
        }
    }
}
pub mod r#_TestKDFK__TestVectors_Compile {
    pub use dafny_runtime::DafnyPrint;
    pub use std::cmp::Eq;
    pub use std::convert::AsRef;
    pub use std::default::Default;
    pub use std::fmt::Debug;
    pub use std::hash::Hash;

    pub struct _default {}

    impl _default {
        pub fn ExpectInternalTestVectors() -> () {
            let mut _hi15: ::dafny_runtime::DafnyInt =
                crate::r#_TestKDFK__TestVectors_Compile::_default::rawTestVectors().cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi15.clone()) {
                crate::r#_TestKDFK__TestVectors_Compile::_default::ExpectRawDeriveTestVector(
                    &crate::r#_TestKDFK__TestVectors_Compile::_default::rawTestVectors().get(&i),
                )
            }
            let mut _hi16: ::dafny_runtime::DafnyInt =
                crate::r#_TestKDFK__TestVectors_Compile::_default::testVectors().cardinality();
            for i in ::dafny_runtime::integer_range(::dafny_runtime::int!(0), _hi16.clone()) {
                crate::r#_TestKDFK__TestVectors_Compile::_default::ExpectTestVector(
                    &crate::r#_TestKDFK__TestVectors_Compile::_default::testVectors().get(&i),
                )
            }
            return ();
        }
        pub fn ExpectRawDeriveTestVector(
            vector: &::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector>,
        ) -> () {
            let mut r#__let_tmp_rhs1: ::std::rc::Rc<
                crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector,
            > = vector.clone();
            let mut name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                r#__let_tmp_rhs1.name().clone();
            let mut _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs1._hash().clone();
            let mut IKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.IKM().clone();
            let mut info: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.info().clone();
            let mut L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger = r#__let_tmp_rhs1.L().clone();
            let mut OKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs1.OKM().clone();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(
                    &name.concat(&::dafny_runtime::string_utf16_of("\n"))
                )
            );
            if !((IKM.cardinality() == ::dafny_runtime::int!(32) || IKM.cardinality() == ::dafny_runtime::int!(48)) && 0 < L && ::dafny_runtime::int!(4) + info.cardinality() < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT() && (_hash.clone() == ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}) || _hash.clone() == ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}))) {
        panic!("Halt")
      };
            if !(::std::convert::Into::<::dafny_runtime::DafnyInt>::into(L) + crate::r#_Digest_Compile::_default::Length(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {})) < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT() - ::dafny_runtime::int!(1) && ::std::convert::Into::<::dafny_runtime::DafnyInt>::into(L) + crate::r#_Digest_Compile::_default::Length(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {})) < mpl_standard_library::_StandardLibrary_Compile::r#_UInt_Compile::_default::INT32_MAX_LIMIT() - ::dafny_runtime::int!(1)) {
        panic!("Halt")
      };
            crate::r#_TestKDF_Compile::_default::KdfRawDeriveTest(&IKM, &info, L, &OKM, &_hash);
            return ();
        }
        pub fn ExpectTestVector(
            vector: &::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector>,
        ) -> () {
            let mut r#__let_tmp_rhs2: ::std::rc::Rc<
                crate::r#_TestKDFK__TestVectors_Compile::TestVector,
            > = vector.clone();
            let mut name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> =
                r#__let_tmp_rhs2.name().clone();
            let mut _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm> = r#__let_tmp_rhs2._hash().clone();
            let mut IKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs2.IKM().clone();
            let mut info: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs2.info().clone();
            let mut purpose: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs2.purpose().clone();
            let mut L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger = r#__let_tmp_rhs2.L().clone();
            let mut OKM: ::dafny_runtime::Sequence<u8> = r#__let_tmp_rhs2.OKM().clone();
            print!(
                "{}",
                ::dafny_runtime::DafnyPrintWrapper(
                    &name.concat(&::dafny_runtime::string_utf16_of("\n"))
                )
            );
            crate::r#_TestKDF_Compile::_default::KdfTest(&::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::KdfCtrInput::KdfCtrInput {
            digestAlgorithm: _hash.clone(),
            ikm: IKM.clone(),
            expectedLength: L,
            purpose: ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                  value: purpose.clone()
                }),
            nonce: ::std::rc::Rc::new(mpl_standard_library::_Wrappers_Compile::Option::<::dafny_runtime::Sequence<u8>>::Some {
                  value: info.clone()
                })
          }), &OKM);
            return ();
        }
        pub fn b1() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.1  Test Case 1"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![226, 4, 214, 212, 102, 170, 213, 7, 255, 175, 109, 109, 171, 10, 91, 38, 21, 44, 158, 33, 231, 100, 55, 4, 100, 227, 96, 200, 251, 199, 101, 198],
          info: ::dafny_runtime::seq![123, 3, 185, 141, 159, 148, 184, 153, 229, 145, 243, 239, 38, 75, 113, 177, 147, 251, 167, 4, 60, 126, 149, 60, 222, 35, 188, 83, 132, 188, 26, 98, 147, 88, 1, 21, 250, 227, 73, 95, 216, 69, 218, 219, 208, 43, 214, 69, 92, 244, 141, 15, 98, 179, 62, 98, 54, 74, 58, 128],
          L: 32,
          OKM: ::dafny_runtime::seq![119, 13, 250, 182, 166, 164, 164, 190, 224, 37, 127, 243, 53, 33, 63, 120, 216, 40, 123, 79, 213, 55, 213, 193, 255, 250, 149, 105, 16, 231, 199, 121]
        })
        }
        pub fn b2() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.2  Test Case 2"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![174, 238, 202, 96, 246, 137, 164, 65, 177, 59, 12, 188, 212, 65, 216, 45, 240, 207, 135, 218, 194, 54, 41, 13, 236, 232, 147, 29, 248, 215, 3, 23],
          info: ::dafny_runtime::seq![88, 142, 192, 65, 229, 115, 59, 112, 49, 33, 44, 85, 56, 239, 228, 246, 170, 250, 76, 218, 139, 146, 93, 38, 31, 90, 38, 136, 240, 7, 179, 172, 36, 14, 225, 41, 145, 231, 123, 140, 184, 83, 134, 120, 97, 89, 102, 22, 74, 129, 135, 43, 209, 207, 203, 251, 57, 164, 244, 80],
          L: 32,
          OKM: ::dafny_runtime::seq![62, 129, 214, 17, 60, 238, 60, 82, 158, 206, 223, 248, 154, 105, 153, 206, 37, 182, 24, 193, 94, 225, 209, 157, 69, 203, 55, 106, 28, 142, 35, 116]
        })
        }
        pub fn b3() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.3  Test Case 3"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![149, 200, 247, 110, 17, 54, 126, 181, 85, 38, 162, 179, 147, 174, 144, 101, 131, 209, 203, 221, 71, 150, 33, 70, 245, 6, 204, 124, 172, 18, 244, 100],
          info: ::dafny_runtime::seq![202, 214, 14, 144, 75, 158, 156, 139, 254, 180, 168, 26, 127, 103, 211, 189, 220, 192, 94, 100, 37, 88, 112, 64, 55, 112, 243, 83, 58, 230, 221, 99, 76, 234, 165, 108, 83, 230, 136, 189, 19, 122, 230, 1, 137, 53, 243, 75, 159, 176, 132, 234, 72, 228, 198, 136, 246, 187, 179, 136],
          L: 32,
          OKM: ::dafny_runtime::seq![202, 250, 92, 160, 63, 95, 190, 42, 36, 32, 4, 171, 203, 211, 222, 16, 89, 199, 64, 123, 30, 229, 121, 37, 81, 36, 175, 24, 155, 224, 181, 86]
        })
        }
        pub fn b4() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.4  Test Case 4"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![77, 5, 57, 31, 214, 251, 30, 41, 46, 120, 171, 150, 25, 177, 183, 42, 125, 99, 238, 89, 215, 67, 93, 215, 24, 151, 185, 255, 126, 231, 174, 112],
          info: ::dafny_runtime::seq![240, 120, 230, 249, 183, 248, 45, 100, 85, 79, 166, 182, 4, 200, 8, 241, 155, 31, 106, 214, 114, 125, 183, 170, 111, 28, 134, 105, 78, 16, 75, 82, 86, 200, 180, 3, 153, 25, 100, 100, 129, 215, 234, 36, 82, 199, 44, 23, 163, 232, 215, 211, 145, 98, 133, 70, 10, 165, 235, 129],
          L: 32,
          OKM: ::dafny_runtime::seq![107, 22, 232, 245, 59, 131, 26, 165, 232, 107, 249, 122, 92, 79, 163, 125, 8, 155, 193, 114, 218, 90, 30, 127, 102, 45, 212, 165, 149, 51, 154, 183]
        })
        }
        pub fn b5() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.5  Test Case 5"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![15, 104, 168, 47, 241, 103, 22, 52, 204, 145, 54, 197, 100, 169, 224, 42, 118, 118, 33, 221, 116, 161, 191, 92, 36, 18, 155, 128, 130, 20, 183, 82],
          info: ::dafny_runtime::seq![100, 133, 153, 128, 156, 44, 78, 124, 106, 94, 108, 68, 159, 0, 49, 235, 245, 92, 54, 97, 168, 149, 180, 77, 176, 87, 46, 232, 128, 131, 177, 244, 177, 38, 2, 170, 85, 252, 29, 241, 80, 166, 90, 109, 110, 237, 160, 170, 121, 164, 52, 161, 3, 155, 145, 181, 165, 143, 199, 241],
          L: 32,
          OKM: ::dafny_runtime::seq![226, 151, 100, 15, 119, 104, 72, 93, 74, 110, 124, 254, 36, 95, 139, 250, 132, 112, 13, 153, 118, 38, 146, 234, 26, 66, 92, 204, 2, 117, 232, 245]
        })
        }
        pub fn b6() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.6 Test Case 6"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
          IKM: ::dafny_runtime::seq![130, 44, 118, 74, 27, 17, 112, 133, 193, 15, 14, 104, 152, 20, 210, 191, 189, 155, 67, 40, 127, 26, 140, 117, 215, 149, 169, 131, 26, 40, 97, 132, 200, 88, 111, 53, 119, 182, 229, 187, 206, 22, 55, 146, 94, 4, 252, 71],
          info: ::dafny_runtime::seq![175, 52, 97, 16, 185, 65, 177, 29, 33, 137, 49, 108, 159, 194, 185, 244, 33, 55, 117, 165, 215, 54, 141, 53, 65, 38, 120, 162, 143, 205, 3, 176, 127, 5, 73, 102, 110, 253, 243, 12, 128, 240, 171, 85, 99, 114, 10, 86, 239, 97, 106, 19, 187, 143, 119, 128, 3, 111, 192, 142],
          L: 32,
          OKM: ::dafny_runtime::seq![224, 174, 35, 92, 184, 35, 128, 82, 123, 231, 105, 52, 166, 150, 34, 57, 109, 144, 231, 191, 167, 226, 210, 149, 228, 55, 91, 206, 224, 209, 177, 1]
        })
        }
        pub fn b7() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.7 Test Case 7"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
          IKM: ::dafny_runtime::seq![52, 14, 33, 45, 117, 142, 131, 204, 91, 137, 228, 181, 106, 134, 238, 140, 150, 49, 174, 78, 75, 186, 236, 21, 172, 9, 94, 164, 64, 123, 199, 182, 52, 173, 99, 13, 208, 190, 133, 169, 28, 8, 168, 199, 225, 225, 3, 11],
          info: ::dafny_runtime::seq![60, 213, 86, 26, 209, 47, 173, 252, 228, 8, 224, 65, 128, 175, 206, 227, 139, 131, 21, 107, 158, 75, 224, 119, 156, 79, 13, 185, 226, 107, 254, 92, 205, 67, 225, 89, 33, 151, 124, 210, 107, 29, 184, 40, 139, 128, 8, 158, 183, 209, 187, 215, 245, 158, 16, 17, 179, 225, 139, 81],
          L: 32,
          OKM: ::dafny_runtime::seq![5, 250, 87, 123, 112, 129, 33, 14, 124, 157, 230, 157, 176, 61, 124, 32, 38, 207, 68, 105, 169, 11, 250, 41, 241, 194, 193, 8, 24, 212, 99, 224]
        })
        }
        pub fn b8() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.8 Test Case 8"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
          IKM: ::dafny_runtime::seq![0, 161, 45, 60, 228, 255, 117, 166, 227, 15, 65, 243, 85, 124, 130, 106, 241, 50, 107, 99, 2, 244, 206, 136, 123, 173, 61, 51, 23, 165, 72, 200, 192, 58, 5, 114, 132, 220, 195, 141, 139, 198, 144, 189, 74, 86, 95, 71],
          info: ::dafny_runtime::seq![36, 197, 192, 178, 200, 16, 223, 160, 142, 53, 215, 254, 235, 184, 199, 142, 12, 215, 38, 201, 46, 205, 66, 217, 23, 16, 19, 115, 140, 162, 83, 26, 148, 127, 82, 60, 55, 246, 76, 219, 4, 48, 91, 217, 105, 209, 214, 249, 236, 212, 100, 5, 210, 130, 128, 249, 104, 80, 11, 167],
          L: 32,
          OKM: ::dafny_runtime::seq![174, 243, 213, 124, 141, 167, 217, 88, 44, 93, 28, 98, 214, 182, 72, 150, 218, 155, 27, 14, 64, 18, 164, 76, 220, 61, 207, 75, 112, 173, 108, 102]
        })
        }
        pub fn b9() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.9 Test Case 9"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
          IKM: ::dafny_runtime::seq![0, 0, 217, 183, 236, 111, 190, 253, 242, 86, 253, 104, 34, 11, 82, 5, 172, 101, 162, 0, 17, 69, 17, 140, 80, 186, 107, 101, 112, 50, 25, 139, 139, 124, 227, 178, 247, 6, 138, 120, 13, 193, 124, 34, 69, 154, 242, 183],
          info: ::dafny_runtime::seq![216, 87, 84, 28, 98, 184, 87, 86, 220, 115, 222, 125, 194, 216, 111, 93, 94, 139, 40, 51, 139, 176, 169, 69, 181, 196, 253, 124, 129, 247, 25, 97, 185, 112, 93, 61, 21, 59, 25, 25, 93, 0, 59, 116, 33, 32, 104, 237, 16, 249, 108, 83, 67, 134, 83, 8, 122, 1, 82, 207],
          L: 20,
          OKM: ::dafny_runtime::seq![121, 62, 241, 19, 249, 99, 151, 171, 0, 49, 234, 160, 250, 167, 119, 193, 7, 231, 208, 60]
        })
        }
        pub fn b10() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector::InternalTestVector {
          name: ::dafny_runtime::string_utf16_of("B.10 Test Case 10"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_384 {}),
          IKM: ::dafny_runtime::seq![79, 61, 116, 77, 62, 68, 158, 6, 39, 191, 68, 152, 116, 56, 40, 248, 110, 99, 143, 96, 98, 10, 126, 212, 167, 201, 181, 176, 115, 105, 28, 158, 201, 71, 40, 197, 136, 34, 232, 39, 240, 246, 204, 248, 109, 188, 28, 174],
          info: ::dafny_runtime::seq![48, 31, 238, 178, 94, 108, 168, 80, 62, 205, 130, 31, 29, 55, 135, 174, 191, 179, 208, 236, 81, 139, 179, 17, 116, 245, 32, 155, 42, 193, 242, 142, 211, 230, 152, 115, 107, 173, 16, 161, 142, 60, 189, 181, 220, 39, 187, 209, 45, 5, 139, 54, 219, 8, 146, 249, 207, 208, 131, 0],
          L: 20,
          OKM: ::dafny_runtime::seq![133, 239, 149, 5, 178, 48, 86, 94, 204, 242, 166, 74, 179, 222, 83, 229, 169, 28, 123, 81]
        })
        }
        pub fn rawTestVectors() -> ::dafny_runtime::Sequence<
            ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::InternalTestVector>,
        > {
            ::dafny_runtime::seq![
                crate::r#_TestKDFK__TestVectors_Compile::_default::b1(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b2(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b3(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b4(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b5(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b6(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b7(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b8(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b9(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::b10()
            ]
        }
        pub fn PURPOSE() -> mpl_standard_library::UTF8::ValidUTF8Bytes {
            mpl_standard_library::UTF8::_default::EncodeAscii(&::dafny_runtime::string_utf16_of(
                "aws-kms-hierarchy",
            ))
        }
        pub fn c1() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::TestVector::TestVector {
          name: ::dafny_runtime::string_utf16_of("C.1 Test Case 1"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![125, 201, 189, 252, 37, 52, 4, 124, 254, 99, 233, 235, 41, 123, 119, 82, 81, 73, 237, 125, 74, 252, 233, 198, 68, 15, 53, 14, 97, 239, 62, 208],
          info: ::dafny_runtime::seq![119, 218, 233, 62, 104, 155, 88, 29, 62, 6, 235, 1, 200, 211, 186, 2],
          purpose: crate::r#_TestKDFK__TestVectors_Compile::_default::PURPOSE(),
          L: 32,
          OKM: ::dafny_runtime::seq![188, 232, 152, 114, 85, 137, 174, 192, 143, 152, 52, 179, 184, 15, 220, 63, 241, 115, 144, 126, 85, 116, 231, 41, 253, 206, 18, 124, 247, 109, 183, 204]
        })
        }
        pub fn c2() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::TestVector::TestVector {
          name: ::dafny_runtime::string_utf16_of("C.2 Test Case 2"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![80, 22, 113, 23, 118, 68, 10, 32, 75, 169, 199, 192, 255, 220, 214, 60, 182, 1, 126, 147, 171, 233, 110, 177, 35, 145, 217, 129, 30, 9, 80, 159],
          info: ::dafny_runtime::seq![210, 241, 192, 158, 103, 66, 27, 35, 143, 66, 168, 189, 82, 171, 211, 252],
          purpose: crate::r#_TestKDFK__TestVectors_Compile::_default::PURPOSE(),
          L: 32,
          OKM: ::dafny_runtime::seq![54, 206, 174, 72, 237, 133, 85, 156, 93, 53, 120, 152, 118, 82, 89, 33, 114, 98, 204, 236, 138, 57, 162, 118, 85, 92, 199, 232, 240, 252, 92, 97]
        })
        }
        pub fn c3() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::TestVector::TestVector {
          name: ::dafny_runtime::string_utf16_of("C.3 Test Case 3"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![57, 90, 16, 46, 83, 54, 189, 241, 27, 242, 237, 236, 246, 66, 54, 226, 74, 112, 79, 156, 208, 13, 148, 71, 117, 211, 139, 57, 73, 69, 122, 236],
          info: ::dafny_runtime::seq![51, 15, 183, 124, 82, 229, 249, 86, 117, 148, 237, 162, 27, 243, 173, 108],
          purpose: crate::r#_TestKDFK__TestVectors_Compile::_default::PURPOSE(),
          L: 32,
          OKM: ::dafny_runtime::seq![22, 55, 236, 141, 159, 163, 250, 236, 86, 47, 225, 103, 156, 225, 228, 146, 166, 45, 244, 39, 136, 163, 205, 200, 116, 193, 20, 147, 112, 254, 210, 194]
        })
        }
        pub fn c4() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::TestVector::TestVector {
          name: ::dafny_runtime::string_utf16_of("C.4 Test Case 4"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![152, 192, 25, 223, 239, 154, 175, 67, 237, 250, 184, 146, 228, 243, 227, 1, 128, 247, 228, 152, 142, 131, 149, 41, 60, 70, 244, 58, 166, 234, 86, 189],
          info: ::dafny_runtime::seq![243, 160, 102, 127, 219, 137, 115, 38, 187, 216, 48, 80, 151, 168, 148, 71],
          purpose: crate::r#_TestKDFK__TestVectors_Compile::_default::PURPOSE(),
          L: 32,
          OKM: ::dafny_runtime::seq![191, 112, 86, 234, 220, 233, 122, 154, 100, 188, 230, 238, 239, 155, 54, 32, 97, 35, 51, 160, 121, 235, 42, 64, 145, 105, 15, 153, 162, 89, 9, 156]
        })
        }
        pub fn c5() -> ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector> {
            ::std::rc::Rc::new(crate::r#_TestKDFK__TestVectors_Compile::TestVector::TestVector {
          name: ::dafny_runtime::string_utf16_of("C.5 Test Case 5"),
          _hash: ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm::SHA_256 {}),
          IKM: ::dafny_runtime::seq![166, 236, 116, 51, 140, 189, 192, 175, 42, 154, 51, 26, 208, 149, 76, 159, 174, 162, 207, 4, 108, 232, 196, 240, 12, 57, 228, 155, 97, 75, 42, 66],
          info: ::dafny_runtime::seq![236, 169, 233, 45, 43, 25, 122, 243, 152, 191, 154, 55, 45, 134, 159, 220],
          purpose: crate::r#_TestKDFK__TestVectors_Compile::_default::PURPOSE(),
          L: 32,
          OKM: ::dafny_runtime::seq![156, 11, 20, 251, 100, 227, 163, 161, 30, 45, 242, 2, 248, 246, 44, 11, 88, 132, 189, 175, 95, 96, 61, 44, 98, 160, 212, 136, 140, 222, 57, 151]
        })
        }
        pub fn testVectors() -> ::dafny_runtime::Sequence<
            ::std::rc::Rc<crate::r#_TestKDFK__TestVectors_Compile::TestVector>,
        > {
            ::dafny_runtime::seq![
                crate::r#_TestKDFK__TestVectors_Compile::_default::c1(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::c2(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::c3(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::c4(),
                crate::r#_TestKDFK__TestVectors_Compile::_default::c5()
            ]
        }
    }

    #[test]
    pub fn ExpectInternalTestVectors() {
        _default::ExpectInternalTestVectors()
    }

    #[derive(PartialEq, Clone)]
    pub enum InternalTestVector {
        InternalTestVector {
      name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
      _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
      IKM: ::dafny_runtime::Sequence<u8>,
      info: ::dafny_runtime::Sequence<u8>,
      L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
      OKM: ::dafny_runtime::Sequence<u8>
    }
  }

    impl InternalTestVector {
        pub fn name(&self) -> &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => name,
            }
        }
        pub fn _hash(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>{
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => _hash,
            }
        }
        pub fn IKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => IKM,
            }
        }
        pub fn info(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => info,
            }
        }
        pub fn L(
            &self,
        ) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
        {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => L,
            }
        }
        pub fn OKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => OKM,
            }
        }
    }

    impl Debug for InternalTestVector {
        fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
            ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
        }
    }

    impl DafnyPrint for InternalTestVector {
        fn fmt_print(
            &self,
            _formatter: &mut ::std::fmt::Formatter,
            _in_seq: bool,
        ) -> std::fmt::Result {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => {
                    write!(
                        _formatter,
                        "TestKDFK__TestVectors_Compile.InternalTestVector.InternalTestVector("
                    )?;
                    ::dafny_runtime::DafnyPrint::fmt_print(name, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(_hash, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(IKM, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(info, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(L, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(OKM, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                }
            }
        }
    }

    impl Eq for InternalTestVector {}

    impl Hash for InternalTestVector {
        fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
            match self {
                InternalTestVector::InternalTestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    L,
                    OKM,
                } => {
                    ::std::hash::Hash::hash(name, _state);
                    ::std::hash::Hash::hash(_hash, _state);
                    ::std::hash::Hash::hash(IKM, _state);
                    ::std::hash::Hash::hash(info, _state);
                    ::std::hash::Hash::hash(L, _state);
                    ::std::hash::Hash::hash(OKM, _state)
                }
            }
        }
    }

    impl Default for InternalTestVector {
        fn default() -> InternalTestVector {
            InternalTestVector::InternalTestVector {
                name: ::std::default::Default::default(),
                _hash: ::std::default::Default::default(),
                IKM: ::std::default::Default::default(),
                info: ::std::default::Default::default(),
                L: ::std::default::Default::default(),
                OKM: ::std::default::Default::default(),
            }
        }
    }

    impl AsRef<InternalTestVector> for &InternalTestVector {
        fn as_ref(&self) -> Self {
            self
        }
    }

    #[derive(PartialEq, Clone)]
    pub enum TestVector {
        TestVector {
      name: ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
      _hash: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>,
      IKM: ::dafny_runtime::Sequence<u8>,
      info: ::dafny_runtime::Sequence<u8>,
      purpose: ::dafny_runtime::Sequence<u8>,
      L: crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger,
      OKM: ::dafny_runtime::Sequence<u8>
    }
  }

    impl TestVector {
        pub fn name(&self) -> &::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16> {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => name,
            }
        }
        pub fn _hash(&self) -> &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::DigestAlgorithm>{
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => _hash,
            }
        }
        pub fn IKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => IKM,
            }
        }
        pub fn info(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => info,
            }
        }
        pub fn purpose(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => purpose,
            }
        }
        pub fn L(
            &self,
        ) -> &crate::software::amazon::cryptography::primitives::internaldafny::types::PositiveInteger
        {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => L,
            }
        }
        pub fn OKM(&self) -> &::dafny_runtime::Sequence<u8> {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => OKM,
            }
        }
    }

    impl Debug for TestVector {
        fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
            ::dafny_runtime::DafnyPrint::fmt_print(self, f, true)
        }
    }

    impl DafnyPrint for TestVector {
        fn fmt_print(
            &self,
            _formatter: &mut ::std::fmt::Formatter,
            _in_seq: bool,
        ) -> std::fmt::Result {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => {
                    write!(
                        _formatter,
                        "TestKDFK__TestVectors_Compile.TestVector.TestVector("
                    )?;
                    ::dafny_runtime::DafnyPrint::fmt_print(name, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(_hash, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(IKM, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(info, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(purpose, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(L, _formatter, false)?;
                    write!(_formatter, ", ")?;
                    ::dafny_runtime::DafnyPrint::fmt_print(OKM, _formatter, false)?;
                    write!(_formatter, ")")?;
                    Ok(())
                }
            }
        }
    }

    impl Eq for TestVector {}

    impl Hash for TestVector {
        fn hash<_H: ::std::hash::Hasher>(&self, _state: &mut _H) {
            match self {
                TestVector::TestVector {
                    name,
                    _hash,
                    IKM,
                    info,
                    purpose,
                    L,
                    OKM,
                } => {
                    ::std::hash::Hash::hash(name, _state);
                    ::std::hash::Hash::hash(_hash, _state);
                    ::std::hash::Hash::hash(IKM, _state);
                    ::std::hash::Hash::hash(info, _state);
                    ::std::hash::Hash::hash(purpose, _state);
                    ::std::hash::Hash::hash(L, _state);
                    ::std::hash::Hash::hash(OKM, _state)
                }
            }
        }
    }

    impl Default for TestVector {
        fn default() -> TestVector {
            TestVector::TestVector {
                name: ::std::default::Default::default(),
                _hash: ::std::default::Default::default(),
                IKM: ::std::default::Default::default(),
                info: ::std::default::Default::default(),
                purpose: ::std::default::Default::default(),
                L: ::std::default::Default::default(),
                OKM: ::std::default::Default::default(),
            }
        }
    }

    impl AsRef<TestVector> for &TestVector {
        fn as_ref(&self) -> Self {
            self
        }
    }
}
pub mod r#_TestSignature_Compile {
    pub struct _default {}

    impl _default {
        pub fn RequireGoodKeyLengths(
            alg: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
            sigKeyPair: &::std::rc::Rc<crate::Signature::SignatureKeyPair>,
        ) -> () {
            let mut _e031: ::dafny_runtime::DafnyInt = sigKeyPair.verificationKey().cardinality();
            let mut _e131: ::dafny_runtime::_System::nat =
                crate::Signature::_default::FieldSize(alg);
            if !(_e031.clone() == _e131.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e031));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e131));
                panic!("Halt")
            };
            return ();
        }
        pub fn YCompression(
            alg: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
            fieldSize: &::dafny_runtime::_System::nat,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out62 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out62 = ::dafny_runtime::MaybePlacebo::from(
                crate::_dafny_externs::Signature::ECDSA::ExternKeyGen(alg),
            );
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(_out62.read());
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut res: ::std::rc::Rc<crate::Signature::SignatureKeyPair> =
                valueOrError0.read().Extract();
            crate::r#_TestSignature_Compile::_default::RequireGoodKeyLengths(alg, &res);
            let mut public = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
            let mut secret = ::dafny_runtime::MaybePlacebo::<::dafny_runtime::Sequence<u8>>::new();
            let mut _rhs0: ::dafny_runtime::Sequence<u8> = res.verificationKey().clone();
            let mut _rhs1: ::dafny_runtime::Sequence<u8> = res.signingKey().clone();
            public = ::dafny_runtime::MaybePlacebo::from(_rhs0.clone());
            secret = ::dafny_runtime::MaybePlacebo::from(_rhs1.clone());
            if !(::dafny_runtime::int!(0) < secret.read().cardinality()) {
                panic!("Halt")
            };
            let mut _e032: ::dafny_runtime::DafnyInt = public.read().cardinality();
            let mut _e132: ::dafny_runtime::DafnyInt = ::dafny_runtime::int!(1)
                + (::dafny_runtime::euclidian_division)(
                    fieldSize.clone() + ::dafny_runtime::int!(7),
                    ::dafny_runtime::int!(8),
                );
            if !(_e032.clone() == _e132.clone()) {
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Left:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e032));
                print!(
                    "{}",
                    ::dafny_runtime::DafnyPrintWrapper(&::dafny_runtime::string_utf16_of(
                        "Right:\n"
                    ))
                );
                print!("{}", ::dafny_runtime::DafnyPrintWrapper(&_e132));
                panic!("Halt")
            };
            if !(public.read().get(&::dafny_runtime::int!(0)) == 2
                || public.read().get(&::dafny_runtime::int!(0)) == 3)
            {
                panic!("Halt")
            };
            return ();
        }
        pub fn VerifyMessage(
            alg: &::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>,
        ) -> () {
            let mut valueOrError0 = ::dafny_runtime::MaybePlacebo::<
                ::std::rc::Rc<
                    mpl_standard_library::_Wrappers_Compile::Result<
                        mpl_standard_library::UTF8::ValidUTF8Bytes,
                        ::dafny_runtime::Sequence<::dafny_runtime::DafnyCharUTF16>,
                    >,
                >,
            >::new();
            valueOrError0 = ::dafny_runtime::MaybePlacebo::from(mpl_standard_library::UTF8::_default::Encode(
                &::dafny_runtime::string_utf16_of("Hello, World!"),
            ));
            if !(!valueOrError0.read().IsFailure()) {
                panic!("Halt")
            };
            let mut message: mpl_standard_library::UTF8::ValidUTF8Bytes = valueOrError0.read().Extract();
            let mut genInput: ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput> = ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::GenerateECDSASignatureKeyInput::GenerateECDSASignatureKeyInput {
            signatureAlgorithm: alg.clone()
          });
            let mut valueOrError1 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out63 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::std::rc::Rc<crate::Signature::SignatureKeyPair>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out63 = ::dafny_runtime::MaybePlacebo::from(
                crate::_dafny_externs::Signature::ECDSA::ExternKeyGen(alg),
            );
            valueOrError1 = ::dafny_runtime::MaybePlacebo::from(_out63.read());
            if !(!valueOrError1.read().IsFailure()) {
                panic!("Halt")
            };
            let mut keys: ::std::rc::Rc<crate::Signature::SignatureKeyPair> =
                valueOrError1.read().Extract();
            crate::r#_TestSignature_Compile::_default::RequireGoodKeyLengths(alg, &keys);
            let mut valueOrError2 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            let mut _out64 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<::dafny_runtime::Sequence<u8>, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            _out64 = ::dafny_runtime::MaybePlacebo::from(
                crate::_dafny_externs::Signature::ECDSA::Sign(alg, keys.signingKey(), &message),
            );
            valueOrError2 = ::dafny_runtime::MaybePlacebo::from(_out64.read());
            if !(!valueOrError2.read().IsFailure()) {
                panic!("Halt")
            };
            let mut signature: ::dafny_runtime::Sequence<u8> = valueOrError2.read().Extract();
            let mut valueOrError3 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError3 = ::dafny_runtime::MaybePlacebo::from(
                crate::_dafny_externs::Signature::ECDSA::Verify(
                    alg,
                    keys.verificationKey(),
                    &message,
                    &signature,
                ),
            );
            if !(!valueOrError3.read().IsFailure()) {
                panic!("Halt")
            };
            let mut shouldBeTrue: bool = valueOrError3.read().Extract();
            if !shouldBeTrue {
                panic!("Halt")
            };
            let mut valueOrError4 = ::dafny_runtime::MaybePlacebo::<::std::rc::Rc<mpl_standard_library::_Wrappers_Compile::Result<bool, ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::Error>>>>::new();
            valueOrError4 = ::dafny_runtime::MaybePlacebo::from(
                crate::_dafny_externs::Signature::ECDSA::Verify(
                    alg,
                    keys.verificationKey(),
                    &message.concat(&::dafny_runtime::seq![1]),
                    &signature,
                ),
            );
            if !(!valueOrError4.read().IsFailure()) {
                panic!("Halt")
            };
            let mut shouldBeFalse: bool = valueOrError4.read().Extract();
            if !(!shouldBeFalse) {
                panic!("Halt")
            };
            return ();
        }
        pub fn YCompression384() -> () {
            crate::r#_TestSignature_Compile::_default::YCompression(
                &crate::r#_TestSignature_Compile::_default::P384(),
                &::dafny_runtime::int!(384),
            );
            return ();
        }
        pub fn YCompression256() -> () {
            crate::r#_TestSignature_Compile::_default::YCompression(
                &crate::r#_TestSignature_Compile::_default::P256(),
                &::dafny_runtime::int!(256),
            );
            return ();
        }
        pub fn VerifyMessage384() -> () {
            crate::r#_TestSignature_Compile::_default::VerifyMessage(
                &crate::r#_TestSignature_Compile::_default::P384(),
            );
            return ();
        }
        pub fn VerifyMessage256() -> () {
            crate::r#_TestSignature_Compile::_default::VerifyMessage(
                &crate::r#_TestSignature_Compile::_default::P256(),
            );
            return ();
        }
        pub fn P384() -> ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>{
            ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm::ECDSA_P384 {})
        }
        pub fn P256() -> ::std::rc::Rc<crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm>{
            ::std::rc::Rc::new(crate::software::amazon::cryptography::primitives::internaldafny::types::ECDSASignatureAlgorithm::ECDSA_P256 {})
        }
    }

    #[test]
    pub fn YCompression384() {
        _default::YCompression384()
    }

    #[test]
    pub fn YCompression256() {
        _default::YCompression256()
    }

    #[test]
    pub fn VerifyMessage384() {
        _default::VerifyMessage384()
    }

    #[test]
    pub fn VerifyMessage256() {
        _default::VerifyMessage256()
    }
}
