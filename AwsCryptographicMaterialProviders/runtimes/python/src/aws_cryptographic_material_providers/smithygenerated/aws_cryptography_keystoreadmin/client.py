# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    IKeyStoreAdminClient,
)
from typing import Callable, TypeVar, cast

from .config import Config, KeyStoreAdminConfig
from .dafny_protocol import DafnyRequest, DafnyResponse
from .plugin import set_config_impl
from smithy_python.exceptions import SmithyRetryException
from smithy_python.interfaces.interceptor import Interceptor, InterceptorContext
from smithy_python.interfaces.retries import RetryErrorInfo, RetryErrorType

from .config import Plugin
from .deserialize import (
    _deserialize_apply_mutation,
    _deserialize_create_key,
    _deserialize_describe_mutation,
    _deserialize_initialize_mutation,
    _deserialize_version_key,
)
from .errors import ServiceError
from .models import (
    ApplyMutationInput,
    ApplyMutationOutput,
    CreateKeyInput,
    CreateKeyOutput,
    DescribeMutationInput,
    DescribeMutationOutput,
    InitializeMutationInput,
    InitializeMutationOutput,
    VersionKeyInput,
    VersionKeyOutput,
)
from .serialize import (
    _serialize_apply_mutation,
    _serialize_create_key,
    _serialize_describe_mutation,
    _serialize_initialize_mutation,
    _serialize_version_key,
)


Input = TypeVar("Input")
Output = TypeVar("Output")


class KeyStoreAdmin:
    """Client for KeyStoreAdmin.

    :param config: Configuration for the client.
    """

    def __init__(
        self,
        config: KeyStoreAdminConfig | None = None,
        dafny_client: IKeyStoreAdminClient | None = None,
    ):
        if config is None:
            self._config = Config()
        else:
            self._config = config

        client_plugins: list[Plugin] = [
            set_config_impl,
        ]

        for plugin in client_plugins:
            plugin(self._config)

        if dafny_client is not None:
            self._config.dafnyImplInterface.impl = dafny_client

    def create_key(self, input: CreateKeyInput) -> CreateKeyOutput:
        """Create a new Branch Key in the Branch Key Store.
        This creates 3 items: the ACTIVE branch key item, the DECRYPT_ONLY for the ACTIVE branch key item, and the beacon key.
        In DynamoDB, the sort-key for the ACTIVE branch key is 'branch:ACTIVE`;
        the sort-key for the decrypt_only is 'branch:version:<uuid>';
        the sort-key for the beacon key is `beacon:ACTIVE'.
        The active branch key and the decrypt_only items have the same plain-text data key.
        The beacon key plain-text data key is unqiue.
        KMS calls are determined by the 'hierarchy-version' and 'KeyManagementStrategy'.
        All three items are written to DDB by a TransactionWriteItems, conditioned on the absence of a conflicting Branch Key ID.
        See Branch Key Store Developer Guide's 'Create Branch Keys': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-branch-keys.html

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_key,
            deserialize=_deserialize_create_key,
            config=self._config,
            operation_name="CreateKey",
        )

    def version_key(self, input: VersionKeyInput) -> VersionKeyOutput:
        """Rotates the Branch Key by creating a new ACTIVE version of an existing Branch Key,
        along with a complementing Version (DECRYPT_ONLY) in the Key Store.
        This generates a fresh AES-256 key which all future encrypts will use
        for the Key Derivation Function,
        until VersionKey is executed again.
        Rotation is accomplished by first authenticating the ACTIVE branch key item,
        followed by generation of a new ACTIVE and matching DECRYPT_ONLY.
        KMS calls are determined by the 'hierarchy-version' and 'KeyManagementStrategy'.
        These two items are then writen to the Branch Key Store via a TransactionWriteItems;
        this only overwrites the ACTIVE item, the DECRYPT_ONLY is a new item.
        This leaves all the previous DECRYPT_ONLY items avabile to service decryption of previous rotations.
        This operation can race against other Version Key requests or Initialize Mutation requests for the same Branch Key.
        Should that occur, all but one of the requests will fail.
        Race errors are either 'Version Race Exceptions' or 'Key Storage Exceptions'.
        See Branch Key Store Developer Guide's 'Rotate your active branch key': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_version_key,
            deserialize=_deserialize_version_key,
            config=self._config,
            operation_name="VersionKey",
        )

    def initialize_mutation(
        self, input: InitializeMutationInput
    ) -> InitializeMutationOutput:
        """Starts a Mutation to all Items of a Branch Key ID. Mutates the
        Beacon Key. Either Mutates the Active & its version (decrypt only), or
        versions the Branch Key, depending on the 'Do Not Version' argument.
        Regardless, if operation is successful, the Beacon, Active, & the
        Active's version are in the terminal state. Establishes the Mutation
        Commitment; simultaneous conflicting Mutations are prevented by the
        Mutation Commitment. A Mutation changes the Encryption Context and/or
        KMS Key associated with a Branch Key. As such, a Mutation can cause
        actors to loose access to a Branch Key, if the actor's access was
        predicated on particular Encryption Context value or KMS Key. Mutations
        MUST be completed via subsequent invocations of the Apply Mutation
        Operation, first invoked with the Mutation Token returned in
        'Initialize Mutation Output'. If access to a KMS Key is revoked while a
        Mutation is in-flight, the Branch Key will be stuck in a mixed state.
        This is not ideal, but once access to the KMS Key is restored, the
        Mutation can be continued by calling 'Describe Mutation' and then
        calling 'Apply Mutation' as normal. With respect to the output's
        Mutation Token, this operation is idempotent; if invoked with the same
        request as an in-flight Mutation, the operation will return successful
        with the same Mutation Token as earlier requests. The 'Initialize
        Mutation Flag' of the output indicates if the request was for a novel
        Mutation or one already in-flight. 'MutationConflictException' is
        thrown if a different Mutation/change is already in-flight. This
        operation can race against other Initialize Mutation requests or
        Version Key requests for the same Branch Key. Should that occur, all
        but one of the requests will fail. Race errors are either
        'VersionRaceException' or 'KeyStorageException'.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_initialize_mutation,
            deserialize=_deserialize_initialize_mutation,
            config=self._config,
            operation_name="InitializeMutation",
        )

    def apply_mutation(self, input: ApplyMutationInput) -> ApplyMutationOutput:
        """Applies the Mutation to a page of Branch Key Items. If all Items
        have been mutated, removes the Mutation Commitment and Index. This
        operation can race other Apply Mutation requests for the same Branch
        Key. Should that occur, all but one of the requests will fail with a
        'Key Storage Exception'. Note that the Mutation Token only contains
        serializable members; the 'System Key' and 'Strategy' settings are
        separate parameters. In particular, the 'System Key' setting MUST be
        consistent across the Initialize Mutation and all the Apply Mutation
        calls of a Mutation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_apply_mutation,
            deserialize=_deserialize_apply_mutation,
            config=self._config,
            operation_name="ApplyMutation",
        )

    def describe_mutation(self, input: DescribeMutationInput) -> DescribeMutationOutput:
        """Check for an in-flight Mutation on a Branch Key ID. If one exists,
        return a description of the mutation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_describe_mutation,
            deserialize=_deserialize_describe_mutation,
            config=self._config,
            operation_name="DescribeMutation",
        )

    def _execute_operation(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], DafnyRequest],
        deserialize: Callable[[DafnyResponse, Config], Output],
        config: Config,
        operation_name: str,
    ) -> Output:
        try:
            return self._handle_execution(
                input, plugins, serialize, deserialize, config, operation_name
            )
        except Exception as e:
            # Make sure every exception that we throw is an instance of ServiceError so
            # customers can reliably catch everything we throw.
            if not isinstance(e, ServiceError):
                raise ServiceError(e) from e
            raise e

    def _handle_execution(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], DafnyRequest],
        deserialize: Callable[[DafnyResponse, Config], Output],
        config: Config,
        operation_name: str,
    ) -> Output:
        context: InterceptorContext[Input, None, None, None] = InterceptorContext(
            request=input,
            response=None,
            transport_request=None,
            transport_response=None,
        )
        _client_interceptors = config.interceptors
        client_interceptors = cast(
            list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
            _client_interceptors,
        )
        interceptors = client_interceptors

        try:
            # Step 1a: Invoke read_before_execution on client-level interceptors
            for interceptor in client_interceptors:
                interceptor.read_before_execution(context)

            # Step 1b: Run operation-level plugins
            for plugin in plugins:
                plugin(config)

            _client_interceptors = config.interceptors
            interceptors = cast(
                list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
                _client_interceptors,
            )

            # Step 1c: Invoke the read_before_execution hooks on newly added
            # interceptors.
            for interceptor in interceptors:
                if interceptor not in client_interceptors:
                    interceptor.read_before_execution(context)

            # Step 2: Invoke the modify_before_serialization hooks
            for interceptor in interceptors:
                context._request = interceptor.modify_before_serialization(context)

            # Step 3: Invoke the read_before_serialization hooks
            for interceptor in interceptors:
                interceptor.read_before_serialization(context)

            # Step 4: Serialize the request
            context_with_transport_request = cast(
                InterceptorContext[Input, None, DafnyRequest, None], context
            )
            context_with_transport_request._transport_request = serialize(
                context_with_transport_request.request, config
            )

            # Step 5: Invoke read_after_serialization
            for interceptor in interceptors:
                interceptor.read_after_serialization(context_with_transport_request)

            # Step 6: Invoke modify_before_retry_loop
            for interceptor in interceptors:
                context_with_transport_request._transport_request = (
                    interceptor.modify_before_retry_loop(context_with_transport_request)
                )

            # Step 7: Acquire the retry token.
            retry_strategy = config.retry_strategy
            retry_token = retry_strategy.acquire_initial_retry_token()

            while True:
                # Make an attempt, creating a copy of the context so we don't pass
                # around old data.
                context_with_response = self._handle_attempt(
                    deserialize,
                    interceptors,
                    context_with_transport_request.copy(),
                    config,
                    operation_name,
                )

                # We perform this type-ignored re-assignment because `context` needs
                # to point at the latest context so it can be generically handled
                # later on. This is only an issue here because we've created a copy,
                # so we're no longer simply pointing at the same object in memory
                # with different names and type hints. It is possible to address this
                # without having to fall back to the type ignore, but it would impose
                # unnecessary runtime costs.
                context = context_with_response  # type: ignore

                if isinstance(context_with_response.response, Exception):
                    # Step 7u: Reacquire retry token if the attempt failed
                    try:
                        retry_token = retry_strategy.refresh_retry_token_for_retry(
                            token_to_renew=retry_token,
                            error_info=RetryErrorInfo(
                                # TODO: Determine the error type.
                                error_type=RetryErrorType.CLIENT_ERROR,
                            ),
                        )
                    except SmithyRetryException:
                        raise context_with_response.response
                else:
                    # Step 8: Invoke record_success
                    retry_strategy.record_success(token=retry_token)
                    break
        except Exception as e:
            context._response = e

        # At this point, the context's request will have been definitively set, and
        # The response will be set either with the modeled output or an exception. The
        # transport_request and transport_response may be set or None.
        execution_context = cast(
            InterceptorContext[
                Input, Output, DafnyRequest | None, DafnyResponse | None
            ],
            context,
        )
        return self._finalize_execution(interceptors, execution_context)

    def _handle_attempt(
        self,
        deserialize: Callable[[DafnyResponse, Config], Output],
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, None, DafnyRequest, None],
        config: Config,
        operation_name: str,
    ) -> InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None]:
        try:
            # Step 7a: Invoke read_before_attempt
            for interceptor in interceptors:
                interceptor.read_before_attempt(context)

            # Step 7m: Involve client Dafny impl
            if config.dafnyImplInterface.impl is None:
                raise Exception("No impl found on the operation config.")

            context_with_response = cast(
                InterceptorContext[Input, None, DafnyRequest, DafnyResponse], context
            )

            context_with_response._transport_response = (
                config.dafnyImplInterface.handle_request(
                    input=context_with_response.transport_request
                )
            )

            # Step 7n: Invoke read_after_transmit
            for interceptor in interceptors:
                interceptor.read_after_transmit(context_with_response)

            # Step 7o: Invoke modify_before_deserialization
            for interceptor in interceptors:
                context_with_response._transport_response = (
                    interceptor.modify_before_deserialization(context_with_response)
                )

            # Step 7p: Invoke read_before_deserialization
            for interceptor in interceptors:
                interceptor.read_before_deserialization(context_with_response)

            # Step 7q: deserialize
            context_with_output = cast(
                InterceptorContext[Input, Output, DafnyRequest, DafnyResponse],
                context_with_response,
            )
            context_with_output._response = deserialize(
                context_with_output._transport_response, config
            )

            # Step 7r: Invoke read_after_deserialization
            for interceptor in interceptors:
                interceptor.read_after_deserialization(context_with_output)
        except Exception as e:
            context._response = e

        # At this point, the context's request and transport_request have definitively been set,
        # the response is either set or an exception, and the transport_resposne is either set or
        # None. This will also be true after _finalize_attempt because there is no opportunity
        # there to set the transport_response.
        attempt_context = cast(
            InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None],
            context,
        )
        return self._finalize_attempt(interceptors, attempt_context)

    def _finalize_attempt(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None],
    ) -> InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None]:
        # Step 7s: Invoke modify_before_attempt_completion
        try:
            for interceptor in interceptors:
                context._response = interceptor.modify_before_attempt_completion(
                    context
                )
        except Exception as e:
            context._response = e

        # Step 7t: Invoke read_after_attempt
        for interceptor in interceptors:
            try:
                interceptor.read_after_attempt(context)
            except Exception as e:
                context._response = e

        return context

    def _finalize_execution(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[
            Input, Output, DafnyRequest | None, DafnyResponse | None
        ],
    ) -> Output:
        try:
            # Step 9: Invoke modify_before_completion
            for interceptor in interceptors:
                context._response = interceptor.modify_before_completion(context)

        except Exception as e:
            context._response = e

        # Step 11: Invoke read_after_execution
        for interceptor in interceptors:
            try:
                interceptor.read_after_execution(context)
            except Exception as e:
                context._response = e

        # Step 12: Return / throw
        if isinstance(context.response, Exception):
            raise context.response

        # We may want to add some aspects of this context to the output types so we can
        # return it to the end-users.
        return context.response
