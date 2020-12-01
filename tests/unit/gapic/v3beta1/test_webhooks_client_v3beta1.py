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
from google.cloud.dialogflowcx_v3beta1.proto import webhook_pb2
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


class TestWebhooksClient(object):
    def test_list_webhooks(self):
        # Setup Expected Response
        next_page_token = ""
        webhooks_element = {}
        webhooks = [webhooks_element]
        expected_response = {"next_page_token": next_page_token, "webhooks": webhooks}
        expected_response = webhook_pb2.ListWebhooksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_webhooks(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.webhooks[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = webhook_pb2.ListWebhooksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_webhooks_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_webhooks(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_webhook(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        disabled = True
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "disabled": disabled,
        }
        expected_response = webhook_pb2.Webhook(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup Request
        name = client.webhook_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[WEBHOOK]")

        response = client.get_webhook(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = webhook_pb2.GetWebhookRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_webhook_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup request
        name = client.webhook_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[WEBHOOK]")

        with pytest.raises(CustomException):
            client.get_webhook(name)

    def test_create_webhook(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        disabled = True
        expected_response = {
            "name": name,
            "display_name": display_name,
            "disabled": disabled,
        }
        expected_response = webhook_pb2.Webhook(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        webhook = {}

        response = client.create_webhook(parent, webhook)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = webhook_pb2.CreateWebhookRequest(
            parent=parent, webhook=webhook
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_webhook_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        webhook = {}

        with pytest.raises(CustomException):
            client.create_webhook(parent, webhook)

    def test_update_webhook(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        disabled = True
        expected_response = {
            "name": name,
            "display_name": display_name,
            "disabled": disabled,
        }
        expected_response = webhook_pb2.Webhook(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup Request
        webhook = {}

        response = client.update_webhook(webhook)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = webhook_pb2.UpdateWebhookRequest(webhook=webhook)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_webhook_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup request
        webhook = {}

        with pytest.raises(CustomException):
            client.update_webhook(webhook)

    def test_delete_webhook(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup Request
        name = client.webhook_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[WEBHOOK]")

        client.delete_webhook(name)

        assert len(channel.requests) == 1
        expected_request = webhook_pb2.DeleteWebhookRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_webhook_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.WebhooksClient()

        # Setup request
        name = client.webhook_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[WEBHOOK]")

        with pytest.raises(CustomException):
            client.delete_webhook(name)
