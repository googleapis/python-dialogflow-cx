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
from google.cloud.dialogflowcx_v3beta1.proto import flow_pb2
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


class TestFlowsClient(object):
    def test_create_flow(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = flow_pb2.Flow(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        flow = {}

        response = client.create_flow(parent, flow)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = flow_pb2.CreateFlowRequest(parent=parent, flow=flow)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_flow_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")
        flow = {}

        with pytest.raises(CustomException):
            client.create_flow(parent, flow)

    def test_delete_flow(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        client.delete_flow(name)

        assert len(channel.requests) == 1
        expected_request = flow_pb2.DeleteFlowRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_flow_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        with pytest.raises(CustomException):
            client.delete_flow(name)

    def test_list_flows(self):
        # Setup Expected Response
        next_page_token = ""
        flows_element = {}
        flows = [flows_element]
        expected_response = {"next_page_token": next_page_token, "flows": flows}
        expected_response = flow_pb2.ListFlowsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_flows(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.flows[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = flow_pb2.ListFlowsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_flows_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup request
        parent = client.agent_path("[PROJECT]", "[LOCATION]", "[AGENT]")

        paged_list_response = client.list_flows(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_flow(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "description": description,
        }
        expected_response = flow_pb2.Flow(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        response = client.get_flow(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = flow_pb2.GetFlowRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_flow_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        with pytest.raises(CustomException):
            client.get_flow(name)

    def test_update_flow(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
        }
        expected_response = flow_pb2.Flow(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        flow = {}
        update_mask = {}

        response = client.update_flow(flow, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = flow_pb2.UpdateFlowRequest(
            flow=flow, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_flow_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup request
        flow = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_flow(flow, update_mask)

    def test_train_flow(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_train_flow", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        response = client.train_flow(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = flow_pb2.TrainFlowRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_train_flow_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_train_flow_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = dialogflowcx_v3beta1.FlowsClient()

        # Setup Request
        name = client.flow_path("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]")

        response = client.train_flow(name)
        exception = response.exception()
        assert exception.errors[0] == error
