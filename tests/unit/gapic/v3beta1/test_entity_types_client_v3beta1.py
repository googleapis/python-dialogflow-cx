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
from google.cloud.dialogflowcx_v3beta1.proto import entity_type_pb2
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


class TestEntityTypesClient(object):
    def test_list_entity_types(self):
        # Setup Expected Response
        next_page_token = ""
        entity_types_element = {}
        entity_types = [entity_types_element]
        expected_response = {
            "next_page_token": next_page_token,
            "entity_types": entity_types,
        }
        expected_response = entity_type_pb2.ListEntityTypesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_entity_types(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.entity_types[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = entity_type_pb2.ListEntityTypesRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_entity_types_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_entity_types(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_entity_type(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        enable_fuzzy_extraction = True
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "enable_fuzzy_extraction": enable_fuzzy_extraction,
        }
        expected_response = entity_type_pb2.EntityType(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup Request
        name = client.entity_type_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"
        )

        response = client.get_entity_type(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = entity_type_pb2.GetEntityTypeRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_entity_type_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup request
        name = client.entity_type_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"
        )

        with pytest.raises(CustomException):
            client.get_entity_type(name)

    def test_create_entity_type(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        enable_fuzzy_extraction = True
        expected_response = {
            "name": name,
            "display_name": display_name,
            "enable_fuzzy_extraction": enable_fuzzy_extraction,
        }
        expected_response = entity_type_pb2.EntityType(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        entity_type = {}

        response = client.create_entity_type(parent, entity_type)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = entity_type_pb2.CreateEntityTypeRequest(
            parent=parent, entity_type=entity_type
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_entity_type_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        entity_type = {}

        with pytest.raises(CustomException):
            client.create_entity_type(parent, entity_type)

    def test_update_entity_type(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        enable_fuzzy_extraction = True
        expected_response = {
            "name": name,
            "display_name": display_name,
            "enable_fuzzy_extraction": enable_fuzzy_extraction,
        }
        expected_response = entity_type_pb2.EntityType(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup Request
        entity_type = {}

        response = client.update_entity_type(entity_type)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = entity_type_pb2.UpdateEntityTypeRequest(
            entity_type=entity_type
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_entity_type_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup request
        entity_type = {}

        with pytest.raises(CustomException):
            client.update_entity_type(entity_type)

    def test_delete_entity_type(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup Request
        name = client.entity_type_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"
        )

        client.delete_entity_type(name)

        assert len(channel.requests) == 1
        expected_request = entity_type_pb2.DeleteEntityTypeRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_entity_type_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.EntityTypesClient()

        # Setup request
        name = client.entity_type_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"
        )

        with pytest.raises(CustomException):
            client.delete_entity_type(name)
