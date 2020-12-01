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

from google.cloud import dialogflowcx_v3beta1
from google.cloud.dialogflowcx_v3beta1.proto import transition_route_group_pb2
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


class TestTransitionRouteGroupsClient(object):
    def test_list_transition_route_groups(self):
        # Setup Expected Response
        next_page_token = ""
        transition_route_groups_element = {}
        transition_route_groups = [transition_route_groups_element]
        expected_response = {
            "next_page_token": next_page_token,
            "transition_route_groups": transition_route_groups,
        }
        expected_response = transition_route_group_pb2.ListTransitionRouteGroupsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_transition_route_groups(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.transition_route_groups[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = transition_route_group_pb2.ListTransitionRouteGroupsRequest(
            parent=parent
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_transition_route_groups_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_transition_route_groups(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_transition_route_group(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        expected_response = {"name": name_2, "display_name": display_name}
        expected_response = transition_route_group_pb2.TransitionRouteGroup(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup Request
        name = client.transition_route_group_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]"
        )

        response = client.get_transition_route_group(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = transition_route_group_pb2.GetTransitionRouteGroupRequest(
            name=name
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_transition_route_group_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup request
        name = client.transition_route_group_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]"
        )

        with pytest.raises(CustomException):
            client.get_transition_route_group(name)

    def test_create_transition_route_group(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        expected_response = {"name": name, "display_name": display_name}
        expected_response = transition_route_group_pb2.TransitionRouteGroup(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        transition_route_group = {}

        response = client.create_transition_route_group(parent, transition_route_group)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = transition_route_group_pb2.CreateTransitionRouteGroupRequest(
            parent=parent, transition_route_group=transition_route_group
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_transition_route_group_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        transition_route_group = {}

        with pytest.raises(CustomException):
            client.create_transition_route_group(parent, transition_route_group)

    def test_update_transition_route_group(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        expected_response = {"name": name, "display_name": display_name}
        expected_response = transition_route_group_pb2.TransitionRouteGroup(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup Request
        transition_route_group = {}

        response = client.update_transition_route_group(transition_route_group)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = transition_route_group_pb2.UpdateTransitionRouteGroupRequest(
            transition_route_group=transition_route_group
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_transition_route_group_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup request
        transition_route_group = {}

        with pytest.raises(CustomException):
            client.update_transition_route_group(transition_route_group)

    def test_delete_transition_route_group(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup Request
        name = client.transition_route_group_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]"
        )

        client.delete_transition_route_group(name)

        assert len(channel.requests) == 1
        expected_request = transition_route_group_pb2.DeleteTransitionRouteGroupRequest(
            name=name
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_transition_route_group_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.TransitionRouteGroupsClient()

        # Setup request
        name = client.transition_route_group_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]"
        )

        with pytest.raises(CustomException):
            client.delete_transition_route_group(name)
