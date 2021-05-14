# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dialogflowcx_v3beta1.services.webhooks import pagers
from google.cloud.dialogflowcx_v3beta1.types import webhook
from google.cloud.dialogflowcx_v3beta1.types import webhook as gcdc_webhook
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import WebhooksTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import WebhooksGrpcAsyncIOTransport
from .client import WebhooksClient


class WebhooksAsyncClient:
    """Service for managing
    [Webhooks][google.cloud.dialogflow.cx.v3beta1.Webhook].
    """

    _client: WebhooksClient

    DEFAULT_ENDPOINT = WebhooksClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WebhooksClient.DEFAULT_MTLS_ENDPOINT

    service_path = staticmethod(WebhooksClient.service_path)
    parse_service_path = staticmethod(WebhooksClient.parse_service_path)
    webhook_path = staticmethod(WebhooksClient.webhook_path)
    parse_webhook_path = staticmethod(WebhooksClient.parse_webhook_path)
    common_billing_account_path = staticmethod(
        WebhooksClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        WebhooksClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(WebhooksClient.common_folder_path)
    parse_common_folder_path = staticmethod(WebhooksClient.parse_common_folder_path)
    common_organization_path = staticmethod(WebhooksClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        WebhooksClient.parse_common_organization_path
    )
    common_project_path = staticmethod(WebhooksClient.common_project_path)
    parse_common_project_path = staticmethod(WebhooksClient.parse_common_project_path)
    common_location_path = staticmethod(WebhooksClient.common_location_path)
    parse_common_location_path = staticmethod(WebhooksClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebhooksAsyncClient: The constructed client.
        """
        return WebhooksClient.from_service_account_info.__func__(WebhooksAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebhooksAsyncClient: The constructed client.
        """
        return WebhooksClient.from_service_account_file.__func__(WebhooksAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> WebhooksTransport:
        """Returns the transport used by the client instance.

        Returns:
            WebhooksTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(WebhooksClient).get_transport_class, type(WebhooksClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, WebhooksTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the webhooks client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.WebhooksTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = WebhooksClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_webhooks(
        self,
        request: webhook.ListWebhooksRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListWebhooksAsyncPager:
        r"""Returns the list of all webhooks in the specified
        agent.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.ListWebhooksRequest`):
                The request object. The request message for
                [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks].
            parent (:class:`str`):
                Required. The agent to list all webhooks for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.services.webhooks.pagers.ListWebhooksAsyncPager:
                The response message for
                [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webhook.ListWebhooksRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_webhooks,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListWebhooksAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_webhook(
        self,
        request: webhook.GetWebhookRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> webhook.Webhook:
        r"""Retrieves the specified webhook.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.GetWebhookRequest`):
                The request object. The request message for
                [Webhooks.GetWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.GetWebhook].
            name (:class:`str`):
                Required. The name of the webhook. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/webhooks/<Webhook ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.types.Webhook:
                Webhooks host the developer's
                business logic. During a session,
                webhooks allow the developer to use the
                data extracted by Dialogflow's natural
                language processing to generate dynamic
                responses, validate collected data, or
                trigger actions on the backend.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webhook.GetWebhookRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_webhook,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_webhook(
        self,
        request: gcdc_webhook.CreateWebhookRequest = None,
        *,
        parent: str = None,
        webhook: gcdc_webhook.Webhook = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_webhook.Webhook:
        r"""Creates a webhook in the specified agent.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.CreateWebhookRequest`):
                The request object. The request message for
                [Webhooks.CreateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook].
            parent (:class:`str`):
                Required. The agent to create a webhook for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            webhook (:class:`google.cloud.dialogflowcx_v3beta1.types.Webhook`):
                Required. The webhook to create.
                This corresponds to the ``webhook`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.types.Webhook:
                Webhooks host the developer's
                business logic. During a session,
                webhooks allow the developer to use the
                data extracted by Dialogflow's natural
                language processing to generate dynamic
                responses, validate collected data, or
                trigger actions on the backend.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, webhook])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcdc_webhook.CreateWebhookRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if webhook is not None:
            request.webhook = webhook

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_webhook,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_webhook(
        self,
        request: gcdc_webhook.UpdateWebhookRequest = None,
        *,
        webhook: gcdc_webhook.Webhook = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_webhook.Webhook:
        r"""Updates the specified webhook.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.UpdateWebhookRequest`):
                The request object. The request message for
                [Webhooks.UpdateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook].
            webhook (:class:`google.cloud.dialogflowcx_v3beta1.types.Webhook`):
                Required. The webhook to update.
                This corresponds to the ``webhook`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The mask to control which fields get
                updated. If the mask is not present, all
                fields will be updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.types.Webhook:
                Webhooks host the developer's
                business logic. During a session,
                webhooks allow the developer to use the
                data extracted by Dialogflow's natural
                language processing to generate dynamic
                responses, validate collected data, or
                trigger actions on the backend.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([webhook, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcdc_webhook.UpdateWebhookRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if webhook is not None:
            request.webhook = webhook
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_webhook,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("webhook.name", request.webhook.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_webhook(
        self,
        request: webhook.DeleteWebhookRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified webhook.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.DeleteWebhookRequest`):
                The request object. The request message for
                [Webhooks.DeleteWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.DeleteWebhook].
            name (:class:`str`):
                Required. The name of the webhook to delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/webhooks/<Webhook ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webhook.DeleteWebhookRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_webhook,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflowcx",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("WebhooksAsyncClient",)
