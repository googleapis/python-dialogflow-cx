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

from google.cloud.dialogflowcx_v3beta1.services.pages import pagers
from google.cloud.dialogflowcx_v3beta1.types import fulfillment
from google.cloud.dialogflowcx_v3beta1.types import page
from google.cloud.dialogflowcx_v3beta1.types import page as gcdc_page
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import PagesTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import PagesGrpcAsyncIOTransport
from .client import PagesClient


class PagesAsyncClient:
    """Service for managing
    [Pages][google.cloud.dialogflow.cx.v3beta1.Page].
    """

    _client: PagesClient

    DEFAULT_ENDPOINT = PagesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PagesClient.DEFAULT_MTLS_ENDPOINT

    entity_type_path = staticmethod(PagesClient.entity_type_path)
    parse_entity_type_path = staticmethod(PagesClient.parse_entity_type_path)
    flow_path = staticmethod(PagesClient.flow_path)
    parse_flow_path = staticmethod(PagesClient.parse_flow_path)
    intent_path = staticmethod(PagesClient.intent_path)
    parse_intent_path = staticmethod(PagesClient.parse_intent_path)
    page_path = staticmethod(PagesClient.page_path)
    parse_page_path = staticmethod(PagesClient.parse_page_path)
    transition_route_group_path = staticmethod(PagesClient.transition_route_group_path)
    parse_transition_route_group_path = staticmethod(
        PagesClient.parse_transition_route_group_path
    )
    webhook_path = staticmethod(PagesClient.webhook_path)
    parse_webhook_path = staticmethod(PagesClient.parse_webhook_path)
    common_billing_account_path = staticmethod(PagesClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(
        PagesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(PagesClient.common_folder_path)
    parse_common_folder_path = staticmethod(PagesClient.parse_common_folder_path)
    common_organization_path = staticmethod(PagesClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        PagesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(PagesClient.common_project_path)
    parse_common_project_path = staticmethod(PagesClient.parse_common_project_path)
    common_location_path = staticmethod(PagesClient.common_location_path)
    parse_common_location_path = staticmethod(PagesClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PagesAsyncClient: The constructed client.
        """
        return PagesClient.from_service_account_info.__func__(PagesAsyncClient, info, *args, **kwargs)  # type: ignore

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
            PagesAsyncClient: The constructed client.
        """
        return PagesClient.from_service_account_file.__func__(PagesAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> PagesTransport:
        """Returns the transport used by the client instance.

        Returns:
            PagesTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PagesClient).get_transport_class, type(PagesClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, PagesTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the pages client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PagesTransport]): The
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
        self._client = PagesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_pages(
        self,
        request: page.ListPagesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPagesAsyncPager:
        r"""Returns the list of all pages in the specified flow.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.ListPagesRequest`):
                The request object. The request message for
                [Pages.ListPages][google.cloud.dialogflow.cx.v3beta1.Pages.ListPages].
            parent (:class:`str`):
                Required. The flow to list all pages for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.services.pages.pagers.ListPagesAsyncPager:
                The response message for
                [Pages.ListPages][google.cloud.dialogflow.cx.v3beta1.Pages.ListPages].

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

        request = page.ListPagesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_pages,
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
        response = pagers.ListPagesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_page(
        self,
        request: page.GetPageRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> page.Page:
        r"""Retrieves the specified page.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.GetPageRequest`):
                The request object. The request message for
                [Pages.GetPage][google.cloud.dialogflow.cx.v3beta1.Pages.GetPage].
            name (:class:`str`):
                Required. The name of the page. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>/pages/<Page ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.types.Page:
                A Dialogflow CX conversation (session) can be described and visualized as a
                   state machine. The states of a CX session are
                   represented by pages.

                   For each flow, you define many pages, where your
                   combined pages can handle a complete conversation on
                   the topics the flow is designed for. At any given
                   moment, exactly one page is the current page, the
                   current page is considered active, and the flow
                   associated with that page is considered active. Every
                   flow has a special start page. When a flow initially
                   becomes active, the start page page becomes the
                   current page. For each conversational turn, the
                   current page will either stay the same or transition
                   to another page.

                   You configure each page to collect information from
                   the end-user that is relevant for the conversational
                   state represented by the page.

                   For more information, see the [Page
                   guide](\ https://cloud.google.com/dialogflow/cx/docs/concept/page).

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

        request = page.GetPageRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_page,
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

    async def create_page(
        self,
        request: gcdc_page.CreatePageRequest = None,
        *,
        parent: str = None,
        page: gcdc_page.Page = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_page.Page:
        r"""Creates a page in the specified flow.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.CreatePageRequest`):
                The request object. The request message for
                [Pages.CreatePage][google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage].
            parent (:class:`str`):
                Required. The flow to create a page for. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            page (:class:`google.cloud.dialogflowcx_v3beta1.types.Page`):
                Required. The page to create.
                This corresponds to the ``page`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflowcx_v3beta1.types.Page:
                A Dialogflow CX conversation (session) can be described and visualized as a
                   state machine. The states of a CX session are
                   represented by pages.

                   For each flow, you define many pages, where your
                   combined pages can handle a complete conversation on
                   the topics the flow is designed for. At any given
                   moment, exactly one page is the current page, the
                   current page is considered active, and the flow
                   associated with that page is considered active. Every
                   flow has a special start page. When a flow initially
                   becomes active, the start page page becomes the
                   current page. For each conversational turn, the
                   current page will either stay the same or transition
                   to another page.

                   You configure each page to collect information from
                   the end-user that is relevant for the conversational
                   state represented by the page.

                   For more information, see the [Page
                   guide](\ https://cloud.google.com/dialogflow/cx/docs/concept/page).

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, page])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcdc_page.CreatePageRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if page is not None:
            request.page = page

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_page,
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

    async def update_page(
        self,
        request: gcdc_page.UpdatePageRequest = None,
        *,
        page: gcdc_page.Page = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcdc_page.Page:
        r"""Updates the specified page.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.UpdatePageRequest`):
                The request object. The request message for
                [Pages.UpdatePage][google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage].
            page (:class:`google.cloud.dialogflowcx_v3beta1.types.Page`):
                Required. The page to update.
                This corresponds to the ``page`` field
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
            google.cloud.dialogflowcx_v3beta1.types.Page:
                A Dialogflow CX conversation (session) can be described and visualized as a
                   state machine. The states of a CX session are
                   represented by pages.

                   For each flow, you define many pages, where your
                   combined pages can handle a complete conversation on
                   the topics the flow is designed for. At any given
                   moment, exactly one page is the current page, the
                   current page is considered active, and the flow
                   associated with that page is considered active. Every
                   flow has a special start page. When a flow initially
                   becomes active, the start page page becomes the
                   current page. For each conversational turn, the
                   current page will either stay the same or transition
                   to another page.

                   You configure each page to collect information from
                   the end-user that is relevant for the conversational
                   state represented by the page.

                   For more information, see the [Page
                   guide](\ https://cloud.google.com/dialogflow/cx/docs/concept/page).

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([page, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcdc_page.UpdatePageRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if page is not None:
            request.page = page
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_page,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("page.name", request.page.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_page(
        self,
        request: page.DeletePageRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified page.

        Args:
            request (:class:`google.cloud.dialogflowcx_v3beta1.types.DeletePageRequest`):
                The request object. The request message for
                [Pages.DeletePage][google.cloud.dialogflow.cx.v3beta1.Pages.DeletePage].
            name (:class:`str`):
                Required. The name of the page to delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/Flows/<flow ID>/pages/<Page ID>``.

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

        request = page.DeletePageRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_page,
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


__all__ = ("PagesAsyncClient",)
