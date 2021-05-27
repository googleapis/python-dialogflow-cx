# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.dialogflowcx_v3.types import environment
from google.cloud.dialogflowcx_v3.types import environment as gcdc_environment
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import EnvironmentsTransport, DEFAULT_CLIENT_INFO
from .grpc import EnvironmentsGrpcTransport


class EnvironmentsGrpcAsyncIOTransport(EnvironmentsTransport):
    """gRPC AsyncIO backend transport for Environments.

    Service for managing
    [Environments][google.cloud.dialogflow.cx.v3.Environment].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "dialogflow.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        self_signed_jwt_kwargs = cls._get_self_signed_jwt_kwargs(host, scopes)

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            **self_signed_jwt_kwargs,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_environments(
        self,
    ) -> Callable[
        [environment.ListEnvironmentsRequest],
        Awaitable[environment.ListEnvironmentsResponse],
    ]:
        r"""Return a callable for the list environments method over gRPC.

        Returns the list of all environments in the specified
        [Agent][google.cloud.dialogflow.cx.v3.Agent].

        Returns:
            Callable[[~.ListEnvironmentsRequest],
                    Awaitable[~.ListEnvironmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_environments" not in self._stubs:
            self._stubs["list_environments"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/ListEnvironments",
                request_serializer=environment.ListEnvironmentsRequest.serialize,
                response_deserializer=environment.ListEnvironmentsResponse.deserialize,
            )
        return self._stubs["list_environments"]

    @property
    def get_environment(
        self,
    ) -> Callable[
        [environment.GetEnvironmentRequest], Awaitable[environment.Environment]
    ]:
        r"""Return a callable for the get environment method over gRPC.

        Retrieves the specified
        [Environment][google.cloud.dialogflow.cx.v3.Environment].

        Returns:
            Callable[[~.GetEnvironmentRequest],
                    Awaitable[~.Environment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_environment" not in self._stubs:
            self._stubs["get_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/GetEnvironment",
                request_serializer=environment.GetEnvironmentRequest.serialize,
                response_deserializer=environment.Environment.deserialize,
            )
        return self._stubs["get_environment"]

    @property
    def create_environment(
        self,
    ) -> Callable[
        [gcdc_environment.CreateEnvironmentRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create environment method over gRPC.

        Creates an
        [Environment][google.cloud.dialogflow.cx.v3.Environment] in the
        specified [Agent][google.cloud.dialogflow.cx.v3.Agent].

        Returns:
            Callable[[~.CreateEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_environment" not in self._stubs:
            self._stubs["create_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/CreateEnvironment",
                request_serializer=gcdc_environment.CreateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_environment"]

    @property
    def update_environment(
        self,
    ) -> Callable[
        [gcdc_environment.UpdateEnvironmentRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update environment method over gRPC.

        Updates the specified
        [Environment][google.cloud.dialogflow.cx.v3.Environment].

        Returns:
            Callable[[~.UpdateEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_environment" not in self._stubs:
            self._stubs["update_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/UpdateEnvironment",
                request_serializer=gcdc_environment.UpdateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_environment"]

    @property
    def delete_environment(
        self,
    ) -> Callable[[environment.DeleteEnvironmentRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete environment method over gRPC.

        Deletes the specified
        [Environment][google.cloud.dialogflow.cx.v3.Environment].

        Returns:
            Callable[[~.DeleteEnvironmentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_environment" not in self._stubs:
            self._stubs["delete_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/DeleteEnvironment",
                request_serializer=environment.DeleteEnvironmentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_environment"]

    @property
    def lookup_environment_history(
        self,
    ) -> Callable[
        [environment.LookupEnvironmentHistoryRequest],
        Awaitable[environment.LookupEnvironmentHistoryResponse],
    ]:
        r"""Return a callable for the lookup environment history method over gRPC.

        Looks up the history of the specified
        [Environment][google.cloud.dialogflow.cx.v3.Environment].

        Returns:
            Callable[[~.LookupEnvironmentHistoryRequest],
                    Awaitable[~.LookupEnvironmentHistoryResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_environment_history" not in self._stubs:
            self._stubs["lookup_environment_history"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/LookupEnvironmentHistory",
                request_serializer=environment.LookupEnvironmentHistoryRequest.serialize,
                response_deserializer=environment.LookupEnvironmentHistoryResponse.deserialize,
            )
        return self._stubs["lookup_environment_history"]

    @property
    def run_continuous_test(
        self,
    ) -> Callable[
        [environment.RunContinuousTestRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the run continuous test method over gRPC.

        Kicks off a continuous test under the specified
        [Environment][google.cloud.dialogflow.cx.v3.Environment].

        Returns:
            Callable[[~.RunContinuousTestRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_continuous_test" not in self._stubs:
            self._stubs["run_continuous_test"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/RunContinuousTest",
                request_serializer=environment.RunContinuousTestRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["run_continuous_test"]

    @property
    def list_continuous_test_results(
        self,
    ) -> Callable[
        [environment.ListContinuousTestResultsRequest],
        Awaitable[environment.ListContinuousTestResultsResponse],
    ]:
        r"""Return a callable for the list continuous test results method over gRPC.

        Fetches a list of continuous test results for a given
        environment.

        Returns:
            Callable[[~.ListContinuousTestResultsRequest],
                    Awaitable[~.ListContinuousTestResultsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_continuous_test_results" not in self._stubs:
            self._stubs["list_continuous_test_results"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.cx.v3.Environments/ListContinuousTestResults",
                request_serializer=environment.ListContinuousTestResultsRequest.serialize,
                response_deserializer=environment.ListContinuousTestResultsResponse.deserialize,
            )
        return self._stubs["list_continuous_test_results"]


__all__ = ("EnvironmentsGrpcAsyncIOTransport",)
