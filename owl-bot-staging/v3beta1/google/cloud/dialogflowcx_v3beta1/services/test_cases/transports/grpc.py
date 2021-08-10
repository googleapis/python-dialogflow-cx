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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers   # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.api_core import gapic_v1       # type: ignore
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import test_case
from google.cloud.dialogflowcx_v3beta1.types import test_case as gcdc_test_case
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import TestCasesTransport, DEFAULT_CLIENT_INFO


class TestCasesGrpcTransport(TestCasesTransport):
    """gRPC backend transport for TestCases.

    Service for managing [Test
    Cases][google.cloud.dialogflow.cx.v3beta1.TestCase] and [Test Case
    Results][google.cloud.dialogflow.cx.v3beta1.TestCaseResult].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'dialogflow.googleapis.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
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
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
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
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
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
            always_use_jwt_access=always_use_jwt_access,
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

    @classmethod
    def create_channel(cls,
                       host: str = 'dialogflow.googleapis.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_test_cases(self) -> Callable[
            [test_case.ListTestCasesRequest],
            test_case.ListTestCasesResponse]:
        r"""Return a callable for the list test cases method over gRPC.

        Fetches a list of test cases for a given agent.

        Returns:
            Callable[[~.ListTestCasesRequest],
                    ~.ListTestCasesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_test_cases' not in self._stubs:
            self._stubs['list_test_cases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/ListTestCases',
                request_serializer=test_case.ListTestCasesRequest.serialize,
                response_deserializer=test_case.ListTestCasesResponse.deserialize,
            )
        return self._stubs['list_test_cases']

    @property
    def batch_delete_test_cases(self) -> Callable[
            [test_case.BatchDeleteTestCasesRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the batch delete test cases method over gRPC.

        Batch deletes test cases.

        Returns:
            Callable[[~.BatchDeleteTestCasesRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'batch_delete_test_cases' not in self._stubs:
            self._stubs['batch_delete_test_cases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/BatchDeleteTestCases',
                request_serializer=test_case.BatchDeleteTestCasesRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['batch_delete_test_cases']

    @property
    def get_test_case(self) -> Callable[
            [test_case.GetTestCaseRequest],
            test_case.TestCase]:
        r"""Return a callable for the get test case method over gRPC.

        Gets a test case.

        Returns:
            Callable[[~.GetTestCaseRequest],
                    ~.TestCase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_test_case' not in self._stubs:
            self._stubs['get_test_case'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/GetTestCase',
                request_serializer=test_case.GetTestCaseRequest.serialize,
                response_deserializer=test_case.TestCase.deserialize,
            )
        return self._stubs['get_test_case']

    @property
    def create_test_case(self) -> Callable[
            [gcdc_test_case.CreateTestCaseRequest],
            gcdc_test_case.TestCase]:
        r"""Return a callable for the create test case method over gRPC.

        Creates a test case for the given agent.

        Returns:
            Callable[[~.CreateTestCaseRequest],
                    ~.TestCase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_test_case' not in self._stubs:
            self._stubs['create_test_case'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/CreateTestCase',
                request_serializer=gcdc_test_case.CreateTestCaseRequest.serialize,
                response_deserializer=gcdc_test_case.TestCase.deserialize,
            )
        return self._stubs['create_test_case']

    @property
    def update_test_case(self) -> Callable[
            [gcdc_test_case.UpdateTestCaseRequest],
            gcdc_test_case.TestCase]:
        r"""Return a callable for the update test case method over gRPC.

        Updates the specified test case.

        Returns:
            Callable[[~.UpdateTestCaseRequest],
                    ~.TestCase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_test_case' not in self._stubs:
            self._stubs['update_test_case'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/UpdateTestCase',
                request_serializer=gcdc_test_case.UpdateTestCaseRequest.serialize,
                response_deserializer=gcdc_test_case.TestCase.deserialize,
            )
        return self._stubs['update_test_case']

    @property
    def run_test_case(self) -> Callable[
            [test_case.RunTestCaseRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the run test case method over gRPC.

        Kicks off a test case run.

        Returns:
            Callable[[~.RunTestCaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'run_test_case' not in self._stubs:
            self._stubs['run_test_case'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/RunTestCase',
                request_serializer=test_case.RunTestCaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['run_test_case']

    @property
    def batch_run_test_cases(self) -> Callable[
            [test_case.BatchRunTestCasesRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the batch run test cases method over gRPC.

        Kicks off a batch run of test cases.

        Returns:
            Callable[[~.BatchRunTestCasesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'batch_run_test_cases' not in self._stubs:
            self._stubs['batch_run_test_cases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/BatchRunTestCases',
                request_serializer=test_case.BatchRunTestCasesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['batch_run_test_cases']

    @property
    def calculate_coverage(self) -> Callable[
            [test_case.CalculateCoverageRequest],
            test_case.CalculateCoverageResponse]:
        r"""Return a callable for the calculate coverage method over gRPC.

        Calculates the test coverage for an agent.

        Returns:
            Callable[[~.CalculateCoverageRequest],
                    ~.CalculateCoverageResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'calculate_coverage' not in self._stubs:
            self._stubs['calculate_coverage'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/CalculateCoverage',
                request_serializer=test_case.CalculateCoverageRequest.serialize,
                response_deserializer=test_case.CalculateCoverageResponse.deserialize,
            )
        return self._stubs['calculate_coverage']

    @property
    def import_test_cases(self) -> Callable[
            [test_case.ImportTestCasesRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the import test cases method over gRPC.

        Imports the test cases from a Cloud Storage bucket or
        a local file. It always creates new test cases and won't
        overwite any existing ones. The provided ID in the
        imported test case is neglected.

        Returns:
            Callable[[~.ImportTestCasesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'import_test_cases' not in self._stubs:
            self._stubs['import_test_cases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/ImportTestCases',
                request_serializer=test_case.ImportTestCasesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['import_test_cases']

    @property
    def export_test_cases(self) -> Callable[
            [test_case.ExportTestCasesRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the export test cases method over gRPC.

        Exports the test cases under the agent to a Cloud
        Storage bucket or a local file. Filter can be applied to
        export a subset of test cases.

        Returns:
            Callable[[~.ExportTestCasesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'export_test_cases' not in self._stubs:
            self._stubs['export_test_cases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/ExportTestCases',
                request_serializer=test_case.ExportTestCasesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['export_test_cases']

    @property
    def list_test_case_results(self) -> Callable[
            [test_case.ListTestCaseResultsRequest],
            test_case.ListTestCaseResultsResponse]:
        r"""Return a callable for the list test case results method over gRPC.

        Fetches a list of results for a given test case.

        Returns:
            Callable[[~.ListTestCaseResultsRequest],
                    ~.ListTestCaseResultsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_test_case_results' not in self._stubs:
            self._stubs['list_test_case_results'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/ListTestCaseResults',
                request_serializer=test_case.ListTestCaseResultsRequest.serialize,
                response_deserializer=test_case.ListTestCaseResultsResponse.deserialize,
            )
        return self._stubs['list_test_case_results']

    @property
    def get_test_case_result(self) -> Callable[
            [test_case.GetTestCaseResultRequest],
            test_case.TestCaseResult]:
        r"""Return a callable for the get test case result method over gRPC.

        Gets a test case result.

        Returns:
            Callable[[~.GetTestCaseResultRequest],
                    ~.TestCaseResult]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_test_case_result' not in self._stubs:
            self._stubs['get_test_case_result'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.cx.v3beta1.TestCases/GetTestCaseResult',
                request_serializer=test_case.GetTestCaseResultRequest.serialize,
                response_deserializer=test_case.TestCaseResult.deserialize,
            )
        return self._stubs['get_test_case_result']


__all__ = (
    'TestCasesGrpcTransport',
)