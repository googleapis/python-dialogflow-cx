# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.dialogflow_cx_v3beta1.proto import (
    page_pb2 as google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PagesStub(object):
    """Service for managing [Pages][google.cloud.dialogflow.cx.v3beta1.Page].
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPages = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Pages/ListPages",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesResponse.FromString,
        )
        self.GetPage = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Pages/GetPage",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.GetPageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
        )
        self.CreatePage = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Pages/CreatePage",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.CreatePageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
        )
        self.UpdatePage = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Pages/UpdatePage",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.UpdatePageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
        )
        self.DeletePage = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Pages/DeletePage",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.DeletePageRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class PagesServicer(object):
    """Service for managing [Pages][google.cloud.dialogflow.cx.v3beta1.Page].
    """

    def ListPages(self, request, context):
        """Returns the list of all pages in the specified flow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetPage(self, request, context):
        """Retrieves the specified page.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreatePage(self, request, context):
        """Creates a page in the specified flow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdatePage(self, request, context):
        """Updates the specified page.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeletePage(self, request, context):
        """Deletes the specified page.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListPages": grpc.unary_unary_rpc_method_handler(
            servicer.ListPages,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesResponse.SerializeToString,
        ),
        "GetPage": grpc.unary_unary_rpc_method_handler(
            servicer.GetPage,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.GetPageRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.SerializeToString,
        ),
        "CreatePage": grpc.unary_unary_rpc_method_handler(
            servicer.CreatePage,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.CreatePageRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.SerializeToString,
        ),
        "UpdatePage": grpc.unary_unary_rpc_method_handler(
            servicer.UpdatePage,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.UpdatePageRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.SerializeToString,
        ),
        "DeletePage": grpc.unary_unary_rpc_method_handler(
            servicer.DeletePage,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.DeletePageRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.cx.v3beta1.Pages", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Pages(object):
    """Service for managing [Pages][google.cloud.dialogflow.cx.v3beta1.Page].
    """

    @staticmethod
    def ListPages(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Pages/ListPages",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.ListPagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetPage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Pages/GetPage",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.GetPageRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreatePage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Pages/CreatePage",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.CreatePageRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdatePage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Pages/UpdatePage",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.UpdatePageRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.Page.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeletePage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Pages/DeletePage",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_page__pb2.DeletePageRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
