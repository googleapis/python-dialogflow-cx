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
from collections import OrderedDict
from distutils import util
import os
import re
from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dialogflowcx_v3.services.test_cases import pagers
from google.cloud.dialogflowcx_v3.types import test_case
from google.cloud.dialogflowcx_v3.types import test_case as gcdc_test_case
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import TestCasesTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import TestCasesGrpcTransport
from .transports.grpc_asyncio import TestCasesGrpcAsyncIOTransport


class TestCasesClientMeta(type):
    """Metaclass for the TestCases client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[TestCasesTransport]]
    _transport_registry["grpc"] = TestCasesGrpcTransport
    _transport_registry["grpc_asyncio"] = TestCasesGrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[TestCasesTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class TestCasesClient(metaclass=TestCasesClientMeta):
    """Service for managing [Test
    Cases][google.cloud.dialogflow.cx.v3.TestCase] and [Test Case
    Results][google.cloud.dialogflow.cx.v3.TestCaseResult].
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "dialogflow.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TestCasesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TestCasesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> TestCasesTransport:
        """Returns the transport used by the client instance.

        Returns:
            TestCasesTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def agent_path(project: str, location: str, agent: str,) -> str:
        """Returns a fully-qualified agent string."""
        return "projects/{project}/locations/{location}/agents/{agent}".format(
            project=project, location=location, agent=agent,
        )

    @staticmethod
    def parse_agent_path(path: str) -> Dict[str, str]:
        """Parses a agent path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def entity_type_path(
        project: str, location: str, agent: str, entity_type: str,
    ) -> str:
        """Returns a fully-qualified entity_type string."""
        return "projects/{project}/locations/{location}/agents/{agent}/entityTypes/{entity_type}".format(
            project=project, location=location, agent=agent, entity_type=entity_type,
        )

    @staticmethod
    def parse_entity_type_path(path: str) -> Dict[str, str]:
        """Parses a entity_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/entityTypes/(?P<entity_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def environment_path(
        project: str, location: str, agent: str, environment: str,
    ) -> str:
        """Returns a fully-qualified environment string."""
        return "projects/{project}/locations/{location}/agents/{agent}/environments/{environment}".format(
            project=project, location=location, agent=agent, environment=environment,
        )

    @staticmethod
    def parse_environment_path(path: str) -> Dict[str, str]:
        """Parses a environment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/environments/(?P<environment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def flow_path(project: str, location: str, agent: str, flow: str,) -> str:
        """Returns a fully-qualified flow string."""
        return "projects/{project}/locations/{location}/agents/{agent}/flows/{flow}".format(
            project=project, location=location, agent=agent, flow=flow,
        )

    @staticmethod
    def parse_flow_path(path: str) -> Dict[str, str]:
        """Parses a flow path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/flows/(?P<flow>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def intent_path(project: str, location: str, agent: str, intent: str,) -> str:
        """Returns a fully-qualified intent string."""
        return "projects/{project}/locations/{location}/agents/{agent}/intents/{intent}".format(
            project=project, location=location, agent=agent, intent=intent,
        )

    @staticmethod
    def parse_intent_path(path: str) -> Dict[str, str]:
        """Parses a intent path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/intents/(?P<intent>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def page_path(
        project: str, location: str, agent: str, flow: str, page: str,
    ) -> str:
        """Returns a fully-qualified page string."""
        return "projects/{project}/locations/{location}/agents/{agent}/flows/{flow}/pages/{page}".format(
            project=project, location=location, agent=agent, flow=flow, page=page,
        )

    @staticmethod
    def parse_page_path(path: str) -> Dict[str, str]:
        """Parses a page path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/flows/(?P<flow>.+?)/pages/(?P<page>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def test_case_path(project: str, location: str, agent: str, test_case: str,) -> str:
        """Returns a fully-qualified test_case string."""
        return "projects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}".format(
            project=project, location=location, agent=agent, test_case=test_case,
        )

    @staticmethod
    def parse_test_case_path(path: str) -> Dict[str, str]:
        """Parses a test_case path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/testCases/(?P<test_case>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def test_case_result_path(
        project: str, location: str, agent: str, test_case: str, result: str,
    ) -> str:
        """Returns a fully-qualified test_case_result string."""
        return "projects/{project}/locations/{location}/agents/{agent}/testCases/{test_case}/results/{result}".format(
            project=project,
            location=location,
            agent=agent,
            test_case=test_case,
            result=result,
        )

    @staticmethod
    def parse_test_case_result_path(path: str) -> Dict[str, str]:
        """Parses a test_case_result path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/testCases/(?P<test_case>.+?)/results/(?P<result>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def transition_route_group_path(
        project: str, location: str, agent: str, flow: str, transition_route_group: str,
    ) -> str:
        """Returns a fully-qualified transition_route_group string."""
        return "projects/{project}/locations/{location}/agents/{agent}/flows/{flow}/transitionRouteGroups/{transition_route_group}".format(
            project=project,
            location=location,
            agent=agent,
            flow=flow,
            transition_route_group=transition_route_group,
        )

    @staticmethod
    def parse_transition_route_group_path(path: str) -> Dict[str, str]:
        """Parses a transition_route_group path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/flows/(?P<flow>.+?)/transitionRouteGroups/(?P<transition_route_group>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def webhook_path(project: str, location: str, agent: str, webhook: str,) -> str:
        """Returns a fully-qualified webhook string."""
        return "projects/{project}/locations/{location}/agents/{agent}/webhooks/{webhook}".format(
            project=project, location=location, agent=agent, webhook=webhook,
        )

    @staticmethod
    def parse_webhook_path(path: str) -> Dict[str, str]:
        """Parses a webhook path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/agents/(?P<agent>.+?)/webhooks/(?P<webhook>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, TestCasesTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the test cases client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, TestCasesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
        )

        client_cert_source_func = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                is_mtls = True
                client_cert_source_func = client_options.client_cert_source
            else:
                is_mtls = mtls.has_default_client_cert_source()
                if is_mtls:
                    client_cert_source_func = mtls.default_client_cert_source()
                else:
                    client_cert_source_func = None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                if is_mtls:
                    api_endpoint = self.DEFAULT_MTLS_ENDPOINT
                else:
                    api_endpoint = self.DEFAULT_ENDPOINT
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted "
                    "values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, TestCasesTransport):
            # transport is a TestCasesTransport instance.
            if credentials or client_options.credentials_file:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
            )

    def list_test_cases(
        self,
        request: test_case.ListTestCasesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTestCasesPager:
        r"""Fetches a list of test cases for a given agent.

        Args:
            request (google.cloud.dialogflowcx_v3.types.ListTestCasesRequest):
                The request object. The request message for
                [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3.TestCases.ListTestCases].
            parent (str):
                Required. The agent to list all pages for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.services.test_cases.pagers.ListTestCasesPager:
                The response message for
                [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3.TestCases.ListTestCases].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.ListTestCasesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.ListTestCasesRequest):
            request = test_case.ListTestCasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_test_cases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTestCasesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_delete_test_cases(
        self,
        request: test_case.BatchDeleteTestCasesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Batch deletes test cases.

        Args:
            request (google.cloud.dialogflowcx_v3.types.BatchDeleteTestCasesRequest):
                The request object. The request message for
                [TestCases.BatchDeleteTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchDeleteTestCases].
            parent (str):
                Required. The agent to delete test cases from. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.BatchDeleteTestCasesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.BatchDeleteTestCasesRequest):
            request = test_case.BatchDeleteTestCasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_test_cases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def get_test_case(
        self,
        request: test_case.GetTestCaseRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> test_case.TestCase:
        r"""Gets a test case.

        Args:
            request (google.cloud.dialogflowcx_v3.types.GetTestCaseRequest):
                The request object. The request message for
                [TestCases.GetTestCase][google.cloud.dialogflow.cx.v3.TestCases.GetTestCase].
            name (str):
                Required. The name of the testcase. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.types.TestCase:
                Represents a test case.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.GetTestCaseRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.GetTestCaseRequest):
            request = test_case.GetTestCaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_test_case]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_test_case(
        self,
        request: gcdc_test_case.CreateTestCaseRequest = None,
        *,
        parent: str = None,
        test_case: gcdc_test_case.TestCase = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_test_case.TestCase:
        r"""Creates a test case for the given agent.

        Args:
            request (google.cloud.dialogflowcx_v3.types.CreateTestCaseRequest):
                The request object. The request message for
                [TestCases.CreateTestCase][google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase].
            parent (str):
                Required. The agent to create the test case for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            test_case (google.cloud.dialogflowcx_v3.types.TestCase):
                Required. The test case to create.
                This corresponds to the ``test_case`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.types.TestCase:
                Represents a test case.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, test_case])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcdc_test_case.CreateTestCaseRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcdc_test_case.CreateTestCaseRequest):
            request = gcdc_test_case.CreateTestCaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if test_case is not None:
                request.test_case = test_case

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_test_case]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_test_case(
        self,
        request: gcdc_test_case.UpdateTestCaseRequest = None,
        *,
        test_case: gcdc_test_case.TestCase = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_test_case.TestCase:
        r"""Updates the specified test case.

        Args:
            request (google.cloud.dialogflowcx_v3.types.UpdateTestCaseRequest):
                The request object. The request message for
                [TestCases.UpdateTestCase][google.cloud.dialogflow.cx.v3.TestCases.UpdateTestCase].
            test_case (google.cloud.dialogflowcx_v3.types.TestCase):
                Required. The test case to update.
                This corresponds to the ``test_case`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The mask to specify which fields should be
                updated. The
                [``creationTime``][google.cloud.dialogflow.cx.v3.TestCase.creation_time]
                and
                [``lastTestResult``][google.cloud.dialogflow.cx.v3.TestCase.last_test_result]
                cannot be updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.types.TestCase:
                Represents a test case.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([test_case, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcdc_test_case.UpdateTestCaseRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcdc_test_case.UpdateTestCaseRequest):
            request = gcdc_test_case.UpdateTestCaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if test_case is not None:
                request.test_case = test_case
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_test_case]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("test_case.name", request.test_case.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def run_test_case(
        self,
        request: test_case.RunTestCaseRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Kicks off a test case run.

        Args:
            request (google.cloud.dialogflowcx_v3.types.RunTestCaseRequest):
                The request object. The request message for
                [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3.TestCases.RunTestCase].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflowcx_v3.types.RunTestCaseResponse`
                The response message for
                [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3.TestCases.RunTestCase].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.RunTestCaseRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.RunTestCaseRequest):
            request = test_case.RunTestCaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.run_test_case]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            test_case.RunTestCaseResponse,
            metadata_type=test_case.RunTestCaseMetadata,
        )

        # Done; return the response.
        return response

    def batch_run_test_cases(
        self,
        request: test_case.BatchRunTestCasesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Kicks off a batch run of test cases.

        Args:
            request (google.cloud.dialogflowcx_v3.types.BatchRunTestCasesRequest):
                The request object. The request message for
                [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflowcx_v3.types.BatchRunTestCasesResponse`
                The response message for
                [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.BatchRunTestCasesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.BatchRunTestCasesRequest):
            request = test_case.BatchRunTestCasesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_run_test_cases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            test_case.BatchRunTestCasesResponse,
            metadata_type=test_case.BatchRunTestCasesMetadata,
        )

        # Done; return the response.
        return response

    def calculate_coverage(
        self,
        request: test_case.CalculateCoverageRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> test_case.CalculateCoverageResponse:
        r"""Calculates the test coverage for an agent.

        Args:
            request (google.cloud.dialogflowcx_v3.types.CalculateCoverageRequest):
                The request object. The request message for
                [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.types.CalculateCoverageResponse:
                The response message for
                [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.CalculateCoverageRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.CalculateCoverageRequest):
            request = test_case.CalculateCoverageRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.calculate_coverage]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("agent", request.agent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def import_test_cases(
        self,
        request: test_case.ImportTestCasesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Imports the test cases from a Cloud Storage bucket or
        a local file. It always creates new test cases and won't
        overwite any existing ones. The provided ID in the
        imported test case is neglected.

        Args:
            request (google.cloud.dialogflowcx_v3.types.ImportTestCasesRequest):
                The request object. The request message for
                [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflowcx_v3.types.ImportTestCasesResponse`
                The response message for
                [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.ImportTestCasesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.ImportTestCasesRequest):
            request = test_case.ImportTestCasesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_test_cases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            test_case.ImportTestCasesResponse,
            metadata_type=test_case.ImportTestCasesMetadata,
        )

        # Done; return the response.
        return response

    def export_test_cases(
        self,
        request: test_case.ExportTestCasesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Exports the test cases under the agent to a Cloud
        Storage bucket or a local file. Filter can be applied to
        export a subset of test cases.

        Args:
            request (google.cloud.dialogflowcx_v3.types.ExportTestCasesRequest):
                The request object. The request message for
                [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ExportTestCases].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflowcx_v3.types.ExportTestCasesResponse`
                The response message for
                [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ExportTestCases].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.ExportTestCasesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.ExportTestCasesRequest):
            request = test_case.ExportTestCasesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export_test_cases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            test_case.ExportTestCasesResponse,
            metadata_type=test_case.ExportTestCasesMetadata,
        )

        # Done; return the response.
        return response

    def list_test_case_results(
        self,
        request: test_case.ListTestCaseResultsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTestCaseResultsPager:
        r"""Fetches a list of results for a given test case.

        Args:
            request (google.cloud.dialogflowcx_v3.types.ListTestCaseResultsRequest):
                The request object. The request message for
                [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults].
            parent (str):
                Required. The test case to list results for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/ testCases/<TestCase ID>``.
                Specify a ``-`` as a wildcard for TestCase ID to list
                results across multiple test cases.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.services.test_cases.pagers.ListTestCaseResultsPager:
                The response message for
                [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.ListTestCaseResultsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.ListTestCaseResultsRequest):
            request = test_case.ListTestCaseResultsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_test_case_results]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTestCaseResultsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_test_case_result(
        self,
        request: test_case.GetTestCaseResultRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> test_case.TestCaseResult:
        r"""Gets a test case result.

        Args:
            request (google.cloud.dialogflowcx_v3.types.GetTestCaseResultRequest):
                The request object. The request message for
                [TestCases.GetTestCaseResult][google.cloud.dialogflow.cx.v3.TestCases.GetTestCaseResult].
            name (str):
                Required. The name of the testcase. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>/results/<TestCaseResult ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3.types.TestCaseResult:
                Represents a result from running a
                test case in an agent environment.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a test_case.GetTestCaseResultRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, test_case.GetTestCaseResultRequest):
            request = test_case.GetTestCaseResultRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_test_case_result]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflowcx",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("TestCasesClient",)
