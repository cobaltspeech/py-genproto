# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cobaltspeech.voicegen.v1 import voicegen_pb2 as cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2


class VoiceGenServiceStub(object):
    """Service that implements the Cobalt VoiceGen API.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Version = channel.unary_unary(
                '/cobaltspeech.voicegen.v1.VoiceGenService/Version',
                request_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionResponse.FromString,
                _registered_method=True)
        self.ListModels = channel.unary_unary(
                '/cobaltspeech.voicegen.v1.VoiceGenService/ListModels',
                request_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsResponse.FromString,
                _registered_method=True)
        self.StreamingSynthesize = channel.unary_stream(
                '/cobaltspeech.voicegen.v1.VoiceGenService/StreamingSynthesize',
                request_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeResponse.FromString,
                _registered_method=True)


class VoiceGenServiceServicer(object):
    """Service that implements the Cobalt VoiceGen API.
    """

    def Version(self, request, context):
        """Returns version information from the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """ListModels returns information about the models the server can access.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingSynthesize(self, request, context):
        """Performs text to speech synthesis and stream synthesized audio. This
        method is only available via GRPC and not via HTTP+JSON. However, a
        web browser may use websockets to use this service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoiceGenServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsResponse.SerializeToString,
            ),
            'StreamingSynthesize': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamingSynthesize,
                    request_deserializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cobaltspeech.voicegen.v1.VoiceGenService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VoiceGenService(object):
    """Service that implements the Cobalt VoiceGen API.
    """

    @staticmethod
    def Version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cobaltspeech.voicegen.v1.VoiceGenService/Version',
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionRequest.SerializeToString,
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.VersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cobaltspeech.voicegen.v1.VoiceGenService/ListModels',
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsRequest.SerializeToString,
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.ListModelsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamingSynthesize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/cobaltspeech.voicegen.v1.VoiceGenService/StreamingSynthesize',
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeRequest.SerializeToString,
            cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2.StreamingSynthesizeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
