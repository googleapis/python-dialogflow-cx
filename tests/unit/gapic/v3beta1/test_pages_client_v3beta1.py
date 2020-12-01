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
from google.cloud.dialogflowcx_v3beta1.proto import page_pb2
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


class TestPagesClient(object):
    def test_list_pages(self):
        # Setup Expected Response
        next_page_token = ""
        pages_element = {}
        pages = [pages_element]
        expected_response = {"next_page_token": next_page_token, "pages": pages}
        expected_response = page_pb2.ListPagesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_pages(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.pages[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = page_pb2.ListPagesRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_pages_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        paged_list_response = client.list_pages(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_page(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        expected_response = {"name": name_2, "display_name": display_name}
        expected_response = page_pb2.Page(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup Request
        name = client.page_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[PAGE]"
        )

        response = client.get_page(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = page_pb2.GetPageRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_page_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup request
        name = client.page_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[PAGE]"
        )

        with pytest.raises(CustomException):
            client.get_page(name)

    def test_create_page(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        expected_response = {"name": name, "display_name": display_name}
        expected_response = page_pb2.Page(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup Request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        page = {}

        response = client.create_page(parent, page)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = page_pb2.CreatePageRequest(parent=parent, page=page)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_page_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup request
        parent = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")
        page = {}

        with pytest.raises(CustomException):
            client.create_page(parent, page)

    def test_update_page(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        expected_response = {"name": name, "display_name": display_name}
        expected_response = page_pb2.Page(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup Request
        page = {}

        response = client.update_page(page)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = page_pb2.UpdatePageRequest(page=page)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_page_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup request
        page = {}

        with pytest.raises(CustomException):
            client.update_page(page)

    def test_delete_page(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup Request
        name = client.page_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[PAGE]"
        )

        client.delete_page(name)

        assert len(channel.requests) == 1
        expected_request = page_pb2.DeletePageRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_page_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.PagesClient()

        # Setup request
        name = client.page_path(
            "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[PAGE]"
        )

        with pytest.raises(CustomException):
            client.delete_page(name)
