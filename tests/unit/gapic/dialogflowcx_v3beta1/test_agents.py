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

import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule

from google import auth
from google.api_core import client_options
from google.api_core import exceptions
from google.api_core import future
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation_async  # type: ignore
from google.api_core import operations_v1
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsAsyncClient
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.services.agents import pagers
from google.cloud.dialogflowcx_v3beta1.services.agents import transports
from google.cloud.dialogflowcx_v3beta1.types import agent
from google.cloud.dialogflowcx_v3beta1.types import agent as gcdc_agent
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import struct_pb2 as struct  # type: ignore


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert AgentsClient._get_default_mtls_endpoint(None) is None
    assert AgentsClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert (
        AgentsClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    )
    assert (
        AgentsClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        AgentsClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert AgentsClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class", [AgentsClient, AgentsAsyncClient])
def test_agents_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds

        assert client.transport._host == "dialogflow.googleapis.com:443"


def test_agents_client_get_transport_class():
    transport = AgentsClient.get_transport_class()
    assert transport == transports.AgentsGrpcTransport

    transport = AgentsClient.get_transport_class("grpc")
    assert transport == transports.AgentsGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AgentsClient, transports.AgentsGrpcTransport, "grpc"),
        (AgentsAsyncClient, transports.AgentsGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
@mock.patch.object(
    AgentsClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AgentsClient)
)
@mock.patch.object(
    AgentsAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AgentsAsyncClient)
)
def test_agents_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(AgentsClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(AgentsClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                ssl_channel_credentials=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                ssl_channel_credentials=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (AgentsClient, transports.AgentsGrpcTransport, "grpc", "true"),
        (
            AgentsAsyncClient,
            transports.AgentsGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (AgentsClient, transports.AgentsGrpcTransport, "grpc", "false"),
        (
            AgentsAsyncClient,
            transports.AgentsGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    AgentsClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AgentsClient)
)
@mock.patch.object(
    AgentsAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AgentsAsyncClient)
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_agents_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            ssl_channel_creds = mock.Mock()
            with mock.patch(
                "grpc.ssl_channel_credentials", return_value=ssl_channel_creds
            ):
                patched.return_value = None
                client = client_class(client_options=options)

                if use_client_cert_env == "false":
                    expected_ssl_channel_creds = None
                    expected_host = client.DEFAULT_ENDPOINT
                else:
                    expected_ssl_channel_creds = ssl_channel_creds
                    expected_host = client.DEFAULT_MTLS_ENDPOINT

                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=expected_host,
                    scopes=None,
                    ssl_channel_credentials=expected_ssl_channel_creds,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.grpc.SslCredentials.__init__", return_value=None
            ):
                with mock.patch(
                    "google.auth.transport.grpc.SslCredentials.is_mtls",
                    new_callable=mock.PropertyMock,
                ) as is_mtls_mock:
                    with mock.patch(
                        "google.auth.transport.grpc.SslCredentials.ssl_credentials",
                        new_callable=mock.PropertyMock,
                    ) as ssl_credentials_mock:
                        if use_client_cert_env == "false":
                            is_mtls_mock.return_value = False
                            ssl_credentials_mock.return_value = None
                            expected_host = client.DEFAULT_ENDPOINT
                            expected_ssl_channel_creds = None
                        else:
                            is_mtls_mock.return_value = True
                            ssl_credentials_mock.return_value = mock.Mock()
                            expected_host = client.DEFAULT_MTLS_ENDPOINT
                            expected_ssl_channel_creds = (
                                ssl_credentials_mock.return_value
                            )

                        patched.return_value = None
                        client = client_class()
                        patched.assert_called_once_with(
                            credentials=None,
                            credentials_file=None,
                            host=expected_host,
                            scopes=None,
                            ssl_channel_credentials=expected_ssl_channel_creds,
                            quota_project_id=None,
                            client_info=transports.base.DEFAULT_CLIENT_INFO,
                        )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.grpc.SslCredentials.__init__", return_value=None
            ):
                with mock.patch(
                    "google.auth.transport.grpc.SslCredentials.is_mtls",
                    new_callable=mock.PropertyMock,
                ) as is_mtls_mock:
                    is_mtls_mock.return_value = False
                    patched.return_value = None
                    client = client_class()
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=client.DEFAULT_ENDPOINT,
                        scopes=None,
                        ssl_channel_credentials=None,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                    )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AgentsClient, transports.AgentsGrpcTransport, "grpc"),
        (AgentsAsyncClient, transports.AgentsGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_agents_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AgentsClient, transports.AgentsGrpcTransport, "grpc"),
        (AgentsAsyncClient, transports.AgentsGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_agents_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_agents_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.dialogflowcx_v3beta1.services.agents.transports.AgentsGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = AgentsClient(client_options={"api_endpoint": "squid.clam.whelk"})
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_list_agents(transport: str = "grpc", request_type=agent.ListAgentsRequest):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.ListAgentsResponse(
            next_page_token="next_page_token_value",
        )

        response = client.list_agents(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.ListAgentsRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, pagers.ListAgentsPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_agents_from_dict():
    test_list_agents(request_type=dict)


@pytest.mark.asyncio
async def test_list_agents_async(
    transport: str = "grpc_asyncio", request_type=agent.ListAgentsRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            agent.ListAgentsResponse(next_page_token="next_page_token_value",)
        )

        response = await client.list_agents(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.ListAgentsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAgentsAsyncPager)

    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_list_agents_async_from_dict():
    await test_list_agents_async(request_type=dict)


def test_list_agents_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.ListAgentsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        call.return_value = agent.ListAgentsResponse()

        client.list_agents(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_agents_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.ListAgentsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            agent.ListAgentsResponse()
        )

        await client.list_agents(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_agents_flattened():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.ListAgentsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_agents(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


def test_list_agents_flattened_error():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_agents(
            agent.ListAgentsRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_agents_flattened_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.ListAgentsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            agent.ListAgentsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_agents(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


@pytest.mark.asyncio
async def test_list_agents_flattened_error_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_agents(
            agent.ListAgentsRequest(), parent="parent_value",
        )


def test_list_agents_pager():
    client = AgentsClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            agent.ListAgentsResponse(
                agents=[agent.Agent(), agent.Agent(), agent.Agent(),],
                next_page_token="abc",
            ),
            agent.ListAgentsResponse(agents=[], next_page_token="def",),
            agent.ListAgentsResponse(agents=[agent.Agent(),], next_page_token="ghi",),
            agent.ListAgentsResponse(agents=[agent.Agent(), agent.Agent(),],),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_agents(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, agent.Agent) for i in results)


def test_list_agents_pages():
    client = AgentsClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_agents), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            agent.ListAgentsResponse(
                agents=[agent.Agent(), agent.Agent(), agent.Agent(),],
                next_page_token="abc",
            ),
            agent.ListAgentsResponse(agents=[], next_page_token="def",),
            agent.ListAgentsResponse(agents=[agent.Agent(),], next_page_token="ghi",),
            agent.ListAgentsResponse(agents=[agent.Agent(), agent.Agent(),],),
            RuntimeError,
        )
        pages = list(client.list_agents(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_agents_async_pager():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_agents), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            agent.ListAgentsResponse(
                agents=[agent.Agent(), agent.Agent(), agent.Agent(),],
                next_page_token="abc",
            ),
            agent.ListAgentsResponse(agents=[], next_page_token="def",),
            agent.ListAgentsResponse(agents=[agent.Agent(),], next_page_token="ghi",),
            agent.ListAgentsResponse(agents=[agent.Agent(), agent.Agent(),],),
            RuntimeError,
        )
        async_pager = await client.list_agents(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, agent.Agent) for i in responses)


@pytest.mark.asyncio
async def test_list_agents_async_pages():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_agents), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            agent.ListAgentsResponse(
                agents=[agent.Agent(), agent.Agent(), agent.Agent(),],
                next_page_token="abc",
            ),
            agent.ListAgentsResponse(agents=[], next_page_token="def",),
            agent.ListAgentsResponse(agents=[agent.Agent(),], next_page_token="ghi",),
            agent.ListAgentsResponse(agents=[agent.Agent(), agent.Agent(),],),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_agents(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_agent(transport: str = "grpc", request_type=agent.GetAgentRequest):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.Agent(
            name="name_value",
            display_name="display_name_value",
            default_language_code="default_language_code_value",
            time_zone="time_zone_value",
            description="description_value",
            avatar_uri="avatar_uri_value",
            start_flow="start_flow_value",
            enable_stackdriver_logging=True,
            enable_spell_correction=True,
        )

        response = client.get_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.GetAgentRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


def test_get_agent_from_dict():
    test_get_agent(request_type=dict)


@pytest.mark.asyncio
async def test_get_agent_async(
    transport: str = "grpc_asyncio", request_type=agent.GetAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            agent.Agent(
                name="name_value",
                display_name="display_name_value",
                default_language_code="default_language_code_value",
                time_zone="time_zone_value",
                description="description_value",
                avatar_uri="avatar_uri_value",
                start_flow="start_flow_value",
                enable_stackdriver_logging=True,
                enable_spell_correction=True,
            )
        )

        response = await client.get_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.GetAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


@pytest.mark.asyncio
async def test_get_agent_async_from_dict():
    await test_get_agent_async(request_type=dict)


def test_get_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.GetAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        call.return_value = agent.Agent()

        client.get_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.GetAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(agent.Agent())

        await client.get_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_agent_flattened():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.Agent()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_agent(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_get_agent_flattened_error():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_agent(
            agent.GetAgentRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_agent_flattened_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = agent.Agent()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(agent.Agent())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_agent(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_agent_flattened_error_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_agent(
            agent.GetAgentRequest(), name="name_value",
        )


def test_create_agent(
    transport: str = "grpc", request_type=gcdc_agent.CreateAgentRequest
):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent(
            name="name_value",
            display_name="display_name_value",
            default_language_code="default_language_code_value",
            time_zone="time_zone_value",
            description="description_value",
            avatar_uri="avatar_uri_value",
            start_flow="start_flow_value",
            enable_stackdriver_logging=True,
            enable_spell_correction=True,
        )

        response = client.create_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == gcdc_agent.CreateAgentRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, gcdc_agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


def test_create_agent_from_dict():
    test_create_agent(request_type=dict)


@pytest.mark.asyncio
async def test_create_agent_async(
    transport: str = "grpc_asyncio", request_type=gcdc_agent.CreateAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcdc_agent.Agent(
                name="name_value",
                display_name="display_name_value",
                default_language_code="default_language_code_value",
                time_zone="time_zone_value",
                description="description_value",
                avatar_uri="avatar_uri_value",
                start_flow="start_flow_value",
                enable_stackdriver_logging=True,
                enable_spell_correction=True,
            )
        )

        response = await client.create_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == gcdc_agent.CreateAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcdc_agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


@pytest.mark.asyncio
async def test_create_agent_async_from_dict():
    await test_create_agent_async(request_type=dict)


def test_create_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcdc_agent.CreateAgentRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        call.return_value = gcdc_agent.Agent()

        client.create_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcdc_agent.CreateAgentRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcdc_agent.Agent())

        await client.create_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_agent_flattened():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_agent(
            parent="parent_value", agent=gcdc_agent.Agent(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].agent == gcdc_agent.Agent(name="name_value")


def test_create_agent_flattened_error():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_agent(
            gcdc_agent.CreateAgentRequest(),
            parent="parent_value",
            agent=gcdc_agent.Agent(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_agent_flattened_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcdc_agent.Agent())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_agent(
            parent="parent_value", agent=gcdc_agent.Agent(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].agent == gcdc_agent.Agent(name="name_value")


@pytest.mark.asyncio
async def test_create_agent_flattened_error_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_agent(
            gcdc_agent.CreateAgentRequest(),
            parent="parent_value",
            agent=gcdc_agent.Agent(name="name_value"),
        )


def test_update_agent(
    transport: str = "grpc", request_type=gcdc_agent.UpdateAgentRequest
):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent(
            name="name_value",
            display_name="display_name_value",
            default_language_code="default_language_code_value",
            time_zone="time_zone_value",
            description="description_value",
            avatar_uri="avatar_uri_value",
            start_flow="start_flow_value",
            enable_stackdriver_logging=True,
            enable_spell_correction=True,
        )

        response = client.update_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == gcdc_agent.UpdateAgentRequest()

    # Establish that the response is the type that we expect.

    assert isinstance(response, gcdc_agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


def test_update_agent_from_dict():
    test_update_agent(request_type=dict)


@pytest.mark.asyncio
async def test_update_agent_async(
    transport: str = "grpc_asyncio", request_type=gcdc_agent.UpdateAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcdc_agent.Agent(
                name="name_value",
                display_name="display_name_value",
                default_language_code="default_language_code_value",
                time_zone="time_zone_value",
                description="description_value",
                avatar_uri="avatar_uri_value",
                start_flow="start_flow_value",
                enable_stackdriver_logging=True,
                enable_spell_correction=True,
            )
        )

        response = await client.update_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == gcdc_agent.UpdateAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcdc_agent.Agent)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.default_language_code == "default_language_code_value"

    assert response.time_zone == "time_zone_value"

    assert response.description == "description_value"

    assert response.avatar_uri == "avatar_uri_value"

    assert response.start_flow == "start_flow_value"

    assert response.enable_stackdriver_logging is True

    assert response.enable_spell_correction is True


@pytest.mark.asyncio
async def test_update_agent_async_from_dict():
    await test_update_agent_async(request_type=dict)


def test_update_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcdc_agent.UpdateAgentRequest()
    request.agent.name = "agent.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        call.return_value = gcdc_agent.Agent()

        client.update_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "agent.name=agent.name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcdc_agent.UpdateAgentRequest()
    request.agent.name = "agent.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcdc_agent.Agent())

        await client.update_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "agent.name=agent.name/value",) in kw["metadata"]


def test_update_agent_flattened():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_agent(
            agent=gcdc_agent.Agent(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].agent == gcdc_agent.Agent(name="name_value")

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_agent_flattened_error():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_agent(
            gcdc_agent.UpdateAgentRequest(),
            agent=gcdc_agent.Agent(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_agent_flattened_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcdc_agent.Agent()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcdc_agent.Agent())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_agent(
            agent=gcdc_agent.Agent(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].agent == gcdc_agent.Agent(name="name_value")

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


@pytest.mark.asyncio
async def test_update_agent_flattened_error_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_agent(
            gcdc_agent.UpdateAgentRequest(),
            agent=gcdc_agent.Agent(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_delete_agent(transport: str = "grpc", request_type=agent.DeleteAgentRequest):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        response = client.delete_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.DeleteAgentRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_agent_from_dict():
    test_delete_agent(request_type=dict)


@pytest.mark.asyncio
async def test_delete_agent_async(
    transport: str = "grpc_asyncio", request_type=agent.DeleteAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)

        response = await client.delete_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.DeleteAgentRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_agent_async_from_dict():
    await test_delete_agent_async(request_type=dict)


def test_delete_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.DeleteAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        call.return_value = None

        client.delete_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.DeleteAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)

        await client.delete_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_agent_flattened():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_agent(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_delete_agent_flattened_error():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_agent(
            agent.DeleteAgentRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_agent_flattened_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_agent(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_delete_agent_flattened_error_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_agent(
            agent.DeleteAgentRequest(), name="name_value",
        )


def test_export_agent(transport: str = "grpc", request_type=agent.ExportAgentRequest):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.export_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.ExportAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_export_agent_from_dict():
    test_export_agent(request_type=dict)


@pytest.mark.asyncio
async def test_export_agent_async(
    transport: str = "grpc_asyncio", request_type=agent.ExportAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.export_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.ExportAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_export_agent_async_from_dict():
    await test_export_agent_async(request_type=dict)


def test_export_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.ExportAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export_agent), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.export_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_export_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.ExportAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.export_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_restore_agent(transport: str = "grpc", request_type=agent.RestoreAgentRequest):
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.restore_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.RestoreAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_restore_agent_from_dict():
    test_restore_agent(request_type=dict)


@pytest.mark.asyncio
async def test_restore_agent_async(
    transport: str = "grpc_asyncio", request_type=agent.RestoreAgentRequest
):
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_agent), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.restore_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == agent.RestoreAgentRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_restore_agent_async_from_dict():
    await test_restore_agent_async(request_type=dict)


def test_restore_agent_field_headers():
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.RestoreAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_agent), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.restore_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_restore_agent_field_headers_async():
    client = AgentsAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = agent.RestoreAgentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_agent), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.restore_agent(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.AgentsGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AgentsClient(
            credentials=credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.AgentsGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AgentsClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.AgentsGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AgentsClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.AgentsGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = AgentsClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.AgentsGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.AgentsGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [transports.AgentsGrpcTransport, transports.AgentsGrpcAsyncIOTransport],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = AgentsClient(credentials=credentials.AnonymousCredentials(),)
    assert isinstance(client.transport, transports.AgentsGrpcTransport,)


def test_agents_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.AgentsTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_agents_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.dialogflowcx_v3beta1.services.agents.transports.AgentsTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.AgentsTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_agents",
        "get_agent",
        "create_agent",
        "update_agent",
        "delete_agent",
        "export_agent",
        "restore_agent",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_agents_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        auth, "load_credentials_from_file"
    ) as load_creds, mock.patch(
        "google.cloud.dialogflowcx_v3beta1.services.agents.transports.AgentsTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.AgentsTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/dialogflow",
            ),
            quota_project_id="octopus",
        )


def test_agents_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(auth, "default") as adc, mock.patch(
        "google.cloud.dialogflowcx_v3beta1.services.agents.transports.AgentsTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.AgentsTransport()
        adc.assert_called_once()


def test_agents_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        AgentsClient()
        adc.assert_called_once_with(
            scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/dialogflow",
            ),
            quota_project_id=None,
        )


def test_agents_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.AgentsGrpcTransport(
            host="squid.clam.whelk", quota_project_id="octopus"
        )
        adc.assert_called_once_with(
            scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/dialogflow",
            ),
            quota_project_id="octopus",
        )


def test_agents_host_no_port():
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="dialogflow.googleapis.com"
        ),
    )
    assert client.transport._host == "dialogflow.googleapis.com:443"


def test_agents_host_with_port():
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="dialogflow.googleapis.com:8000"
        ),
    )
    assert client.transport._host == "dialogflow.googleapis.com:8000"


def test_agents_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")

    # Check that channel is used if provided.
    transport = transports.AgentsGrpcTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_agents_grpc_asyncio_transport_channel():
    channel = aio.insecure_channel("http://localhost/")

    # Check that channel is used if provided.
    transport = transports.AgentsGrpcAsyncIOTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


@pytest.mark.parametrize(
    "transport_class",
    [transports.AgentsGrpcTransport, transports.AgentsGrpcAsyncIOTransport],
)
def test_agents_transport_channel_mtls_with_client_cert_source(transport_class):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel", autospec=True
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=(
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/dialogflow",
                ),
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


@pytest.mark.parametrize(
    "transport_class",
    [transports.AgentsGrpcTransport, transports.AgentsGrpcAsyncIOTransport],
)
def test_agents_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel", autospec=True
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=(
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/dialogflow",
                ),
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_agents_grpc_lro_client():
    client = AgentsClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_agents_grpc_lro_async_client():
    client = AgentsAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsAsyncClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_agent_path():
    project = "squid"
    location = "clam"
    agent = "whelk"

    expected = "projects/{project}/locations/{location}/agents/{agent}".format(
        project=project, location=location, agent=agent,
    )
    actual = AgentsClient.agent_path(project, location, agent)
    assert expected == actual


def test_parse_agent_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "agent": "nudibranch",
    }
    path = AgentsClient.agent_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_agent_path(path)
    assert expected == actual


def test_flow_path():
    project = "cuttlefish"
    location = "mussel"
    agent = "winkle"
    flow = "nautilus"

    expected = "projects/{project}/locations/{location}/agents/{agent}/flows/{flow}".format(
        project=project, location=location, agent=agent, flow=flow,
    )
    actual = AgentsClient.flow_path(project, location, agent, flow)
    assert expected == actual


def test_parse_flow_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
        "agent": "squid",
        "flow": "clam",
    }
    path = AgentsClient.flow_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_flow_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "whelk"

    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = AgentsClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "octopus",
    }
    path = AgentsClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "oyster"

    expected = "folders/{folder}".format(folder=folder,)
    actual = AgentsClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nudibranch",
    }
    path = AgentsClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "cuttlefish"

    expected = "organizations/{organization}".format(organization=organization,)
    actual = AgentsClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "mussel",
    }
    path = AgentsClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "winkle"

    expected = "projects/{project}".format(project=project,)
    actual = AgentsClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nautilus",
    }
    path = AgentsClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "scallop"
    location = "abalone"

    expected = "projects/{project}/locations/{location}".format(
        project=project, location=location,
    )
    actual = AgentsClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "squid",
        "location": "clam",
    }
    path = AgentsClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = AgentsClient.parse_common_location_path(path)
    assert expected == actual


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.AgentsTransport, "_prep_wrapped_messages"
    ) as prep:
        client = AgentsClient(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.AgentsTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = AgentsClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
