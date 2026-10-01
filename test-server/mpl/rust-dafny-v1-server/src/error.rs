//! The two modeled TestServer errors and their rpcv2Cbor wire form.

/// A modeled TestServer error.
#[derive(Debug, Clone)]
pub enum ServerError {
    /// Framework-side failure (bad request, unknown operation, unknown ID, etc.).
    Generic(String),
    /// A failure forwarded from the underlying MPL.
    Mpl(String),
}

const NS: &str = "aws.cryptography.mpl.testserver";

impl ServerError {
    pub fn generic(message: impl Into<String>) -> Self {
        Self::Generic(message.into())
    }

    pub fn mpl(message: impl Into<String>) -> Self {
        Self::Mpl(message.into())
    }

    /// The `__type` shape id placed on the wire.
    pub fn type_id(&self) -> String {
        match self {
            Self::Generic(_) => format!("{NS}#GenericServerError"),
            Self::Mpl(_) => format!("{NS}#MPLClientError"),
        }
    }

    pub fn message(&self) -> &str {
        match self {
            Self::Generic(m) | Self::Mpl(m) => m,
        }
    }

    /// Serialize to the rpcv2Cbor error body: a CBOR map `{__type, message}`.
    pub fn to_cbor(&self) -> Vec<u8> {
        let map = ciborium::value::Value::Map(vec![
            (
                ciborium::value::Value::Text("__type".to_owned()),
                ciborium::value::Value::Text(self.type_id()),
            ),
            (
                ciborium::value::Value::Text("message".to_owned()),
                ciborium::value::Value::Text(self.message().to_owned()),
            ),
        ]);
        let mut buf = Vec::new();
        ciborium::into_writer(&map, &mut buf).expect("CBOR error encoding");
        buf
    }
}
