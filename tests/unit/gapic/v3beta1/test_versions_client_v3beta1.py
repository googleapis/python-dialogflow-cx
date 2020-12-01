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
from google.cloud.dialogflowcx_v3beta1.proto import version_pb2
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


class TestVersionsClient(object):
    def test_list_versions(self):
        # Setup Expected Response
        next_page_token = ""
        versions_element = {}
        versions = [versions_element]
        expected_response = {"next_page_token": next_page_token, "versions": versions}
        expected_response = version_pb2.ListVersionsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_versions(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.versions[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = version_pb2.ListVersionsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_versions_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_versions(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_version(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "description": description,
        }
        expected_response = version_pb2.Version(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        response = client.get_version(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = version_pb2.GetVersionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_version_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        with pytest.raises(CustomException):
            client.get_version(name)

    def test_create_version(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = version_pb2.Version(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_create_version", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        version = {}

        response = client.create_version(parent, version)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = version_pb2.CreateVersionRequest(
            parent=parent, version=version
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_version_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_create_version_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        version = {}

        response = client.create_version(parent, version)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_update_version(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = version_pb2.Version(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        version = {}
        update_mask = {}

        response = client.update_version(version, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = version_pb2.UpdateVersionRequest(
            version=version, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_version_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup request
        version = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_version(version, update_mask)

    def test_delete_version(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        client.delete_version(name)

        assert len(channel.requests) == 1
        expected_request = version_pb2.DeleteVersionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_version_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        with pytest.raises(CustomException):
            client.delete_version(name)

    def test_load_version(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_load_version", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        response = client.load_version(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = version_pb2.LoadVersionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_load_version_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_load_version_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.VersionsClient()

        # Setup Request
        name = client.version_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]"
        )

        response = client.load_version(name)
        exception = response.exception()
        assert exception.errors[0] == error
