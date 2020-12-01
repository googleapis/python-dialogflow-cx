# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.dialogflow_cx_v3beta1.proto import (
    agent_pb2 as google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AgentsStub(object):
    """Service for managing [Agents][google.cloud.dialogflow.cx.v3beta1.Agent].
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAgents = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/ListAgents",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsResponse.FromString,
        )
        self.GetAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/GetAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.GetAgentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
        )
        self.CreateAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/CreateAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.CreateAgentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
        )
        self.UpdateAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/UpdateAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.UpdateAgentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
        )
        self.DeleteAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/DeleteAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.DeleteAgentRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ExportAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/ExportAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ExportAgentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.RestoreAgent = channel.unary_unary(
            "/google.cloud.dialogflow.cx.v3beta1.Agents/RestoreAgent",
            request_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.RestoreAgentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class AgentsServicer(object):
    """Service for managing [Agents][google.cloud.dialogflow.cx.v3beta1.Agent].
    """

    def ListAgents(self, request, context):
        """Returns the list of all agents in the specified location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAgent(self, request, context):
        """Retrieves the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateAgent(self, request, context):
        """Creates an agent in the specified location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateAgent(self, request, context):
        """Updates the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAgent(self, request, context):
        """Deletes the specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportAgent(self, request, context):
        """Exports the specified agent to a binary file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RestoreAgent(self, request, context):
        """Restores the specified agent from a binary file.

        Replaces the current agent with a new one. Note that all existing resources
        in agent (e.g. intents, entity types, flows) will be removed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AgentsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListAgents": grpc.unary_unary_rpc_method_handler(
            servicer.ListAgents,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsResponse.SerializeToString,
        ),
        "GetAgent": grpc.unary_unary_rpc_method_handler(
            servicer.GetAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.GetAgentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.SerializeToString,
        ),
        "CreateAgent": grpc.unary_unary_rpc_method_handler(
            servicer.CreateAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.CreateAgentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.SerializeToString,
        ),
        "UpdateAgent": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.UpdateAgentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.SerializeToString,
        ),
        "DeleteAgent": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.DeleteAgentRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ExportAgent": grpc.unary_unary_rpc_method_handler(
            servicer.ExportAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ExportAgentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "RestoreAgent": grpc.unary_unary_rpc_method_handler(
            servicer.RestoreAgent,
            request_deserializer=google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.RestoreAgentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.cx.v3beta1.Agents", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Agents(object):
    """Service for managing [Agents][google.cloud.dialogflow.cx.v3beta1.Agent].
    """

    @staticmethod
    def ListAgents(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/ListAgents",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ListAgentsResponse.FromString,
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
    def GetAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/GetAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.GetAgentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
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
    def CreateAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/CreateAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.CreateAgentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
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
    def UpdateAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/UpdateAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.UpdateAgentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.Agent.FromString,
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
    def DeleteAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/DeleteAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.DeleteAgentRequest.SerializeToString,
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

    @staticmethod
    def ExportAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/ExportAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.ExportAgentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
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
    def RestoreAgent(
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
            "/google.cloud.dialogflow.cx.v3beta1.Agents/RestoreAgent",
            google_dot_cloud_dot_dialogflow__cx__v3beta1_dot_proto_dot_agent__pb2.RestoreAgentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
