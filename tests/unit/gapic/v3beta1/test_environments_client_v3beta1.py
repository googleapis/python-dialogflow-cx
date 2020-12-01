# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.rpc import status_pb2

from google.cloud import dialogflowcx_v3beta1
from google.cloud.dialogflowcx_v3beta1.proto import environment_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestEnvironmentsClient(object):
    def test_list_environments(self):
        # Setup Expected Response
        next_page_token = ""
        environments_element = {}
        environments = [environments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "environments": environments,
        }
        expected_response = environment_pb2.ListEnvironmentsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_environments(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.environments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = environment_pb2.ListEnvironmentsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_environments_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_environments(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_environment(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "description": description,
        }
        expected_response = environment_pb2.Environment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        response = client.get_environment(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = environment_pb2.GetEnvironmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_environment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        with pytest.raises(CustomException):
            client.get_environment(name)

    def test_create_environment(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = environment_pb2.Environment(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_create_environment", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        environment = {}

        response = client.create_environment(parent, environment)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = environment_pb2.CreateEnvironmentRequest(
            parent=parent, environment=environment
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_environment_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_create_environment_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        environment = {}

        response = client.create_environment(parent, environment)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_update_environment(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = environment_pb2.Environment(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_update_environment", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        environment = {}
        update_mask = {}

        response = client.update_environment(environment, update_mask)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = environment_pb2.UpdateEnvironmentRequest(
            environment=environment, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_environment_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_update_environment_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        environment = {}
        update_mask = {}

        response = client.update_environment(environment, update_mask)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_delete_environment(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        client.delete_environment(name)

        assert len(channel.requests) == 1
        expected_request = environment_pb2.DeleteEnvironmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_environment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        with pytest.raises(CustomException):
            client.delete_environment(name)

    def test_lookup_environment_history(self):
        # Setup Expected Response
        next_page_token = ""
        environments_element = {}
        environments = [environments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "environments": environments,
        }
        expected_response = environment_pb2.LookupEnvironmentHistoryResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup Request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        paged_list_response = client.lookup_environment_history(name)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.environments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = environment_pb2.LookupEnvironmentHistoryRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_lookup_environment_history_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EnvironmentsClient()

        # Setup request
        name = client.environment_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"
        )

        paged_list_response = client.lookup_environment_history(name)
        with pytest.raises(CustomException):
            list(paged_list_response)
