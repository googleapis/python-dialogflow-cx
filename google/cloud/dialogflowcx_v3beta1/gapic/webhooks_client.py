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

"""Accesses the google.cloud.dialogflow.cx.v3beta1 Webhooks API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.dialogflowcx_v3beta1.gapic import enums
from google.cloud.dialogflowcx_v3beta1.gapic import webhooks_client_config
from google.cloud.dialogflowcx_v3beta1.gapic.transports import webhooks_grpc_transport
from google.cloud.dialogflowcx_v3beta1.proto import agent_pb2
from google.cloud.dialogflowcx_v3beta1.proto import agent_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import audio_config_pb2
from google.cloud.dialogflowcx_v3beta1.proto import entity_type_pb2
from google.cloud.dialogflowcx_v3beta1.proto import entity_type_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import environment_pb2
from google.cloud.dialogflowcx_v3beta1.proto import environment_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import flow_pb2
from google.cloud.dialogflowcx_v3beta1.proto import flow_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import intent_pb2
from google.cloud.dialogflowcx_v3beta1.proto import intent_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import page_pb2
from google.cloud.dialogflowcx_v3beta1.proto import page_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import session_entity_type_pb2
from google.cloud.dialogflowcx_v3beta1.proto import session_entity_type_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import session_pb2
from google.cloud.dialogflowcx_v3beta1.proto import session_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import transition_route_group_pb2
from google.cloud.dialogflowcx_v3beta1.proto import transition_route_group_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import version_pb2
from google.cloud.dialogflowcx_v3beta1.proto import version_pb2_grpc
from google.cloud.dialogflowcx_v3beta1.proto import webhook_pb2
from google.cloud.dialogflowcx_v3beta1.proto import webhook_pb2_grpc
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import struct_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-dialogflow-cx",
).version


class WebhooksClient(object):
    """Service for managing ``Webhooks``."""

    SERVICE_ADDRESS = "dialogflow.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.dialogflow.cx.v3beta1.Webhooks"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebhooksClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def agent_path(cls, project, location, agent):
        """Return a fully-qualified agent string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/agents/{agent}",
            project=project,
            location=location,
            agent=agent,
        )

    @classmethod
    def webhook_path(cls, project, location, agent, webhook):
        """Return a fully-qualified webhook string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/agents/{agent}/webhooks/{webhook}",
            project=project,
            location=location,
            agent=agent,
            webhook=webhook,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.WebhooksGrpcTransport,
                    Callable[[~.Credentials, type], ~.WebhooksGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = webhooks_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=webhooks_grpc_transport.WebhooksGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = webhooks_grpc_transport.WebhooksGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_webhooks(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns the list of all webhooks in the specified agent.

        Example:
            >>> from google.cloud import dialogflowcx_v3beta1
            >>>
            >>> client = dialogflowcx_v3beta1.WebhooksClient()
            >>>
            >>> parent = client.agent_path('[PROJECT]', '[LOCATION]', '[AGENT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_webhooks(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_webhooks(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The agent to list all webhooks for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_webhooks" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_webhooks"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_webhooks,
                default_retry=self._method_configs["ListWebhooks"].retry,
                default_timeout=self._method_configs["ListWebhooks"].timeout,
                client_info=self._client_info,
            )

        request = webhook_pb2.ListWebhooksRequest(parent=parent, page_size=page_size,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_webhooks"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="webhooks",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_webhook(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves the specified webhook.

        Example:
            >>> from google.cloud import dialogflowcx_v3beta1
            >>>
            >>> client = dialogflowcx_v3beta1.WebhooksClient()
            >>>
            >>> name = client.webhook_path('[PROJECT]', '[LOCATION]', '[AGENT]', '[WEBHOOK]')
            >>>
            >>> response = client.get_webhook(name)

        Args:
            name (str): Required. The name of the webhook. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/webhooks/<Webhook ID>``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_webhook" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_webhook"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_webhook,
                default_retry=self._method_configs["GetWebhook"].retry,
                default_timeout=self._method_configs["GetWebhook"].timeout,
                client_info=self._client_info,
            )

        request = webhook_pb2.GetWebhookRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_webhook"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_webhook(
        self,
        parent,
        webhook,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a webhook in the specified agent.

        Example:
            >>> from google.cloud import dialogflowcx_v3beta1
            >>>
            >>> client = dialogflowcx_v3beta1.WebhooksClient()
            >>>
            >>> parent = client.agent_path('[PROJECT]', '[LOCATION]', '[AGENT]')
            >>>
            >>> # TODO: Initialize `webhook`:
            >>> webhook = {}
            >>>
            >>> response = client.create_webhook(parent, webhook)

        Args:
            parent (str): Required. The agent to create a webhook for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
            webhook (Union[dict, ~google.cloud.dialogflowcx_v3beta1.types.Webhook]): Required. The webhook to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_webhook" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_webhook"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_webhook,
                default_retry=self._method_configs["CreateWebhook"].retry,
                default_timeout=self._method_configs["CreateWebhook"].timeout,
                client_info=self._client_info,
            )

        request = webhook_pb2.CreateWebhookRequest(parent=parent, webhook=webhook,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_webhook"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_webhook(
        self,
        webhook,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates the specified webhook.

        Example:
            >>> from google.cloud import dialogflowcx_v3beta1
            >>>
            >>> client = dialogflowcx_v3beta1.WebhooksClient()
            >>>
            >>> # TODO: Initialize `webhook`:
            >>> webhook = {}
            >>>
            >>> response = client.update_webhook(webhook)

        Args:
            webhook (Union[dict, ~google.cloud.dialogflowcx_v3beta1.types.Webhook]): Required. The webhook to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook`
            update_mask (Union[dict, ~google.cloud.dialogflowcx_v3beta1.types.FieldMask]): The mask to control which fields get updated. If the mask is not present,
                all fields will be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflowcx_v3beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.dialogflowcx_v3beta1.types.Webhook` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_webhook" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_webhook"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_webhook,
                default_retry=self._method_configs["UpdateWebhook"].retry,
                default_timeout=self._method_configs["UpdateWebhook"].timeout,
                client_info=self._client_info,
            )

        request = webhook_pb2.UpdateWebhookRequest(
            webhook=webhook, update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("webhook.name", webhook.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_webhook"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_webhook(
        self,
        name,
        force=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes the specified webhook.

        Example:
            >>> from google.cloud import dialogflowcx_v3beta1
            >>>
            >>> client = dialogflowcx_v3beta1.WebhooksClient()
            >>>
            >>> name = client.webhook_path('[PROJECT]', '[LOCATION]', '[AGENT]', '[WEBHOOK]')
            >>>
            >>> client.delete_webhook(name)

        Args:
            name (str): Required. The name of the webhook to delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/webhooks/<Webhook ID>``.
            force (bool): This field has no effect for webhook not being used. For webhooks
                that are used by pages/flows/transition route groups:

                -  If ``force`` is set to false, an error will be returned with message
                   indicating the referenced resources.
                -  If ``force`` is set to true, Dialogflow will remove the webhook, as
                   well as any references to the webhook (i.e. ``Webhook`` and
                   ``tag``\ in fulfillments that point to this webhook will be removed).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_webhook" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_webhook"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_webhook,
                default_retry=self._method_configs["DeleteWebhook"].retry,
                default_timeout=self._method_configs["DeleteWebhook"].timeout,
                client_info=self._client_info,
            )

        request = webhook_pb2.DeleteWebhookRequest(name=name, force=force,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_webhook"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
