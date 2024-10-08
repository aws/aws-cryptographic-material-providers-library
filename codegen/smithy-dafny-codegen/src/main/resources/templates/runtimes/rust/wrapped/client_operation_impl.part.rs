    fn $operationName:L(
        &mut self,
        input: &$operationInputDafnyType:L,
    ) -> std::rc::Rc<
        crate::r#_Wrappers_Compile::Result<
            $operationOutputDafnyType:L,
            std::rc::Rc<crate::r#$dafnyTypesModuleName:L::Error>,
        >,
    >{
        let inner_input = $inputFromDafny:L;
        let result = tokio::task::block_in_place(|| {
            dafny_tokio_runtime.block_on(crate::operation::$snakeCaseOperationName:L::$pascalCaseOperationName:L::send(&self.wrapped, inner_input))
        });
        match result {
            Err(error) => ::std::rc::Rc::new(
                crate::_Wrappers_Compile::Result::Failure {
                    error: crate::conversions::error::to_dafny(error),
                },
            ),
            Ok(inner_result) => ::std::rc::Rc::new(
                crate::_Wrappers_Compile::Result::Success {
                    value: $outputToDafny:L,
                },
            ),
        }
    }