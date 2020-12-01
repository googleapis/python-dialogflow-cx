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
from google.cloud.dialogflowcx_v3beta1.proto import agent_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2


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


class TestAgentsClient(object):
    def test_list_agents(self):
        # Setup Expected Response
        next_page_token = ""
        agents_element = {}
        agents = [agents_element]
        expected_response = {"next_page_token": next_page_token, "agents": agents}
        expected_response = agent_pb2.ListAgentsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_agents(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.agents[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = agent_pb2.ListAgentsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_agents_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_agents(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_agent(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        default_language_code = "defaultLanguageCode856575222"
        time_zone = "timeZone36848094"
        description = "description-1724546052"
        avatar_uri = "avatarUri-402824826"
        start_flow = "startFlow-1573559573"
        enable_stackdriver_logging = True
        enable_spell_correction = False
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "default_language_code": default_language_code,
            "time_zone": time_zone,
            "description": description,
            "avatar_uri": avatar_uri,
            "start_flow": start_flow,
            "enable_stackdriver_logging": enable_stackdriver_logging,
            "enable_spell_correction": enable_spell_correction,
        }
        expected_response = agent_pb2.Agent(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        response = client.get_agent(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = agent_pb2.GetAgentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_agent_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        with pytest.raises(CustomException):
            client.get_agent(name)

    def test_create_agent(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        default_language_code = "defaultLanguageCode856575222"
        time_zone = "timeZone36848094"
        description = "description-1724546052"
        avatar_uri = "avatarUri-402824826"
        start_flow = "startFlow-1573559573"
        enable_stackdriver_logging = True
        enable_spell_correction = False
        expected_response = {
            "name": name,
            "display_name": display_name,
            "default_language_code": default_language_code,
            "time_zone": time_zone,
            "description": description,
            "avatar_uri": avatar_uri,
            "start_flow": start_flow,
            "enable_stackdriver_logging": enable_stackdriver_logging,
            "enable_spell_correction": enable_spell_correction,
        }
        expected_response = agent_pb2.Agent(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")
        agent = {}

        response = client.create_agent(parent, agent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = agent_pb2.CreateAgentRequest(parent=parent, agent=agent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_agent_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")
        agent = {}

        with pytest.raises(CustomException):
            client.create_agent(parent, agent)

    def test_update_agent(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        default_language_code = "defaultLanguageCode856575222"
        time_zone = "timeZone36848094"
        description = "description-1724546052"
        avatar_uri = "avatarUri-402824826"
        start_flow = "startFlow-1573559573"
        enable_stackdriver_logging = True
        enable_spell_correction = False
        expected_response = {
            "name": name,
            "display_name": display_name,
            "default_language_code": default_language_code,
            "time_zone": time_zone,
            "description": description,
            "avatar_uri": avatar_uri,
            "start_flow": start_flow,
            "enable_stackdriver_logging": enable_stackdriver_logging,
            "enable_spell_correction": enable_spell_correction,
        }
        expected_response = agent_pb2.Agent(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        agent = {}

        response = client.update_agent(agent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = agent_pb2.UpdateAgentRequest(agent=agent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_agent_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup request
        agent = {}

        with pytest.raises(CustomException):
            client.update_agent(agent)

    def test_delete_agent(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        client.delete_agent(name)

        assert len(channel.requests) == 1
        expected_request = agent_pb2.DeleteAgentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_agent_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        with pytest.raises(CustomException):
            client.delete_agent(name)

    def test_export_agent(self):
        # Setup Expected Response
        agent_uri = "agentUri-1700713166"
        expected_response = {"agent_uri": agent_uri}
        expected_response = agent_pb2.ExportAgentResponse(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_export_agent", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        response = client.export_agent(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = agent_pb2.ExportAgentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_export_agent_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_export_agent_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        response = client.export_agent(name)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_restore_agent(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_restore_agent", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        response = client.restore_agent(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = agent_pb2.RestoreAgentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_restore_agent_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_restore_agent_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.AgentsClient()

        # Setup Request
        name = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        response = client.restore_agent(name)
        exception = response.exception()
        assert exception.errors[0] == error
