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
import warnings

from google.cloud.dialogflowcx_v3beta1 import types
from google.cloud.dialogflowcx_v3beta1.gapic import agents_client
from google.cloud.dialogflowcx_v3beta1.gapic import entity_types_client
from google.cloud.dialogflowcx_v3beta1.gapic import enums
from google.cloud.dialogflowcx_v3beta1.gapic import environments_client
from google.cloud.dialogflowcx_v3beta1.gapic import flows_client
from google.cloud.dialogflowcx_v3beta1.gapic import intents_client
from google.cloud.dialogflowcx_v3beta1.gapic import pages_client
from google.cloud.dialogflowcx_v3beta1.gapic import session_entity_types_client
from google.cloud.dialogflowcx_v3beta1.gapic import sessions_client
from google.cloud.dialogflowcx_v3beta1.gapic import transition_route_groups_client
from google.cloud.dialogflowcx_v3beta1.gapic import versions_client
from google.cloud.dialogflowcx_v3beta1.gapic import webhooks_client


if sys.version_info[:2] == (2, 7):
    message = (
        "A future version of this library will drop support for Python 2.7. "
        "More details about Python 2 support for Google Cloud Client Libraries "
        "can be found at https://cloud.google.com/python/docs/python2-sunset/"
    )
    warnings.warn(message, DeprecationWarning)


class PagesClient(pages_client.PagesClient):
    __doc__ = pages_client.PagesClient.__doc__
    enums = enums


class FlowsClient(flows_client.FlowsClient):
    __doc__ = flows_client.FlowsClient.__doc__
    enums = enums


class AgentsClient(agents_client.AgentsClient):
    __doc__ = agents_client.AgentsClient.__doc__
    enums = enums


class EntityTypesClient(entity_types_client.EntityTypesClient):
    __doc__ = entity_types_client.EntityTypesClient.__doc__
    enums = enums


class EnvironmentsClient(environments_client.EnvironmentsClient):
    __doc__ = environments_client.EnvironmentsClient.__doc__
    enums = enums


class IntentsClient(intents_client.IntentsClient):
    __doc__ = intents_client.IntentsClient.__doc__
    enums = enums


class SessionEntityTypesClient(session_entity_types_client.SessionEntityTypesClient):
    __doc__ = session_entity_types_client.SessionEntityTypesClient.__doc__
    enums = enums


class SessionsClient(sessions_client.SessionsClient):
    __doc__ = sessions_client.SessionsClient.__doc__
    enums = enums


class TransitionRouteGroupsClient(
    transition_route_groups_client.TransitionRouteGroupsClient
):
    __doc__ = transition_route_groups_client.TransitionRouteGroupsClient.__doc__
    enums = enums


class VersionsClient(versions_client.VersionsClient):
    __doc__ = versions_client.VersionsClient.__doc__
    enums = enums


class WebhooksClient(webhooks_client.WebhooksClient):
    __doc__ = webhooks_client.WebhooksClient.__doc__
    enums = enums


__all__ = (
    "enums",
    "types",
    "PagesClient",
    "FlowsClient",
    "AgentsClient",
    "EntityTypesClient",
    "EnvironmentsClient",
    "IntentsClient",
    "SessionEntityTypesClient",
    "SessionsClient",
    "TransitionRouteGroupsClient",
    "VersionsClient",
    "WebhooksClient",
)
