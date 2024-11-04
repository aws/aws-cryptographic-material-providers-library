// Code generated by software.amazon.smithy.rust.codegen.smithy-rs. DO NOT EDIT.
impl super::Client {
    /// Constructs a fluent builder for the [`GetRuntimeInformation`](crate::operation::get_runtime_information::builders::GetRuntimeInformationFluentBuilder) operation.
    ///
    /// - On success, responds with [`GetRuntimeInformationOutput`](crate::operation::get_runtime_information::GetRuntimeInformationOutput) with field(s):
    ///   - [`language(String)`](crate::operation::get_runtime_information::GetRuntimeInformationOutput::language): (undocumented)
    ///   - [`runtime(String)`](crate::operation::get_runtime_information::GetRuntimeInformationOutput::runtime): (undocumented)
    /// - On failure, responds with [`SdkError<GetRuntimeInformationError>`](crate::operation::get_runtime_information::GetRuntimeInformationError)
    pub fn get_runtime_information(&self) -> crate::operation::get_runtime_information::builders::GetRuntimeInformationFluentBuilder {
        crate::operation::get_runtime_information::builders::GetRuntimeInformationFluentBuilder::new(self.clone())
    }
}