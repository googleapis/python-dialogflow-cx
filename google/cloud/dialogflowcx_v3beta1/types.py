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


from __future__ import absolute_import
import sys

from google.api_core.protobuf_helpers import get_messages

from google.cloud.dialogflowcx_v3beta1.proto import agent_pb2
from google.cloud.dialogflowcx_v3beta1.proto import audio_config_pb2
from google.cloud.dialogflowcx_v3beta1.proto import entity_type_pb2
from google.cloud.dialogflowcx_v3beta1.proto import environment_pb2
from google.cloud.dialogflowcx_v3beta1.proto import flow_pb2
from google.cloud.dialogflowcx_v3beta1.proto import fulfillment_pb2
from google.cloud.dialogflowcx_v3beta1.proto import intent_pb2
from google.cloud.dialogflowcx_v3beta1.proto import page_pb2
from google.cloud.dialogflowcx_v3beta1.proto import response_message_pb2
from google.cloud.dialogflowcx_v3beta1.proto import session_entity_type_pb2
from google.cloud.dialogflowcx_v3beta1.proto import session_pb2
from google.cloud.dialogflowcx_v3beta1.proto import transition_route_group_pb2
from google.cloud.dialogflowcx_v3beta1.proto import version_pb2
from google.cloud.dialogflowcx_v3beta1.proto import webhook_pb2
from google.longrunning import operations_pb2
from google.protobuf import any_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import struct_pb2
from google.protobuf import timestamp_pb2
from google.rpc import status_pb2
from google.type import latlng_pb2


_shared_modules = [
    operations_pb2,
    any_pb2,
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    struct_pb2,
    timestamp_pb2,
    status_pb2,
    latlng_pb2,
]

_local_modules = [
    agent_pb2,
    audio_config_pb2,
    entity_type_pb2,
    environment_pb2,
    flow_pb2,
    fulfillment_pb2,
    intent_pb2,
    page_pb2,
    response_message_pb2,
    session_entity_type_pb2,
    session_pb2,
    transition_route_group_pb2,
    version_pb2,
    webhook_pb2,
]

names = []

for module in _shared_modules:  # pragma: NO COVER
    for name, message in get_messages(module).items():
        setattr(sys.modules[__name__], name, message)
        names.append(name)
for module in _local_modules:
    for name, message in get_messages(module).items():
        message.__module__ = "google.cloud.dialogflowcx_v3beta1.types"
        setattr(sys.modules[__name__], name, message)
        names.append(name)


__all__ = tuple(sorted(names))
