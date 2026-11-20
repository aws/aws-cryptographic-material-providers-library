//! The two modeled TestServer errors and their rpcv2Cbor wire form.

/// A modeled TestServer error.
#[derive(Debug, Clone)]
pub enum ServerError {
    /// Framework-side failure (bad request, unknown operation, unknown ID, etc.).
    Generic(String),
    /// A failure forwarded from the underlying MPL, with the messages of the
    /// errors it collected (MPLClientError's `collectedErrors`, absent when
    /// it collected none).
    Mpl(String, Option<Vec<String>>),
}

const NS: &str = "aws.cryptography.mpl.testserver";

impl ServerError {
    pub fn generic(message: impl Into<String>) -> Self {
        Self::Generic(message.into())
    }

    pub fn mpl(message: impl Into<String>) -> Self {
        Self::Mpl(message.into(), None)
    }

    pub fn mpl_collected(message: impl Into<String>, collected_errors: Vec<String>) -> Self {
        let collected_errors = (!collected_errors.is_empty()).then_some(collected_errors);
        Self::Mpl(message.into(), collected_errors)
    }

    /// The `__type` shape id placed on the wire.
    pub fn type_id(&self) -> String {
        match self {
            Self::Generic(_) => format!("{NS}#GenericServerError"),
            Self::Mpl(..) => format!("{NS}#MPLClientError"),
        }
    }

    pub fn message(&self) -> &str {
        match self {
            Self::Generic(m) | Self::Mpl(m, _) => m,
        }
    }

    /// Serialize to the rpcv2Cbor error body: a CBOR map `{__type, message}`,
    /// plus `collectedErrors` when the MPL collected any.
    pub fn to_cbor(&self) -> Vec<u8> {
        use ciborium::value::Value;
        let mut entries = vec![
            (
                Value::Text("__type".to_owned()),
                Value::Text(self.type_id()),
            ),
            (
                Value::Text("message".to_owned()),
                Value::Text(self.message().to_owned()),
            ),
        ];
        if let Self::Mpl(_, Some(collected)) = self {
            entries.push((
                Value::Text("collectedErrors".to_owned()),
                Value::Array(collected.iter().cloned().map(Value::Text).collect()),
            ));
        }
        let map = Value::Map(entries);
        let mut buf = Vec::new();
        ciborium::into_writer(&map, &mut buf).expect("CBOR error encoding");
        buf
    }
}
