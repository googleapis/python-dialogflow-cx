# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.dialogflow_cx_v3beta1.proto import (
    session_pb2 as google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2,
)


class SessionsStub(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent] method to determine
    user intent and respond.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetectIntent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/DetectIntent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentResponse.FromString,
        )
        self.StreamingDetectIntent = channel.stream_stream(
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/StreamingDetectIntent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentResponse.FromString,
        )
        self.MatchIntent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/MatchIntent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentResponse.FromString,
        )
        self.FulfillIntent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/FulfillIntent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentResponse.FromString,
        )


class SessionsServicer(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent] method to determine
    user intent and respond.
    """

    def DetectIntent(self, request, context):
        """Processes a natural language query and returns structured, actionable data
        as a result. This method is not idempotent, because it may cause session
        entity types to be updated, which in turn might affect results of future
        queries.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamingDetectIntent(self, request_iterator, context):
        """Processes a natural language query in audio format in a streaming fashion
        and returns structured, actionable data as a result. This method is only
        available via the gRPC API (not REST).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MatchIntent(self, request, context):
        """Returns preliminary intent match results, doesn't change the session
        status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FulfillIntent(self, request, context):
        """Fulfills a matched intent returned by [MatchIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.MatchIntent].
        Must be called after [MatchIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.MatchIntent], with input from
        [MatchIntentResponse][google.cloud.dialogflow.cx.v3beta1.MatchIntentResponse]. Otherwise, the behavior is undefined.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SessionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DetectIntent": grpc.unary_unary_rpc_method_handler(
            servicer.DetectIntent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentResponse.SerializeToString,
        ),
        "StreamingDetectIntent": grpc.stream_stream_rpc_method_handler(
            servicer.StreamingDetectIntent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentResponse.SerializeToString,
        ),
        "MatchIntent": grpc.unary_unary_rpc_method_handler(
            servicer.MatchIntent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentResponse.SerializeToString,
        ),
        "FulfillIntent": grpc.unary_unary_rpc_method_handler(
            servicer.FulfillIntent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.cx.v3beta1.Sessions", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Sessions(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent] method to determine
    user intent and respond.
    """

    @staticmethod
    def DetectIntent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/DetectIntent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.DetectIntentResponse.FromString,
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
    def StreamingDetectIntent(
        request_iterator,
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
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/StreamingDetectIntent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.StreamingDetectIntentResponse.FromString,
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
    def MatchIntent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/MatchIntent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.MatchIntentResponse.FromString,
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
    def FulfillIntent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Sessions/FulfillIntent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_session__pb2.FulfillIntentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
