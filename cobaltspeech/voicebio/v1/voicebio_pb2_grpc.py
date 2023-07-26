# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cobaltspeech.voicebio.v1 import voicebio_pb2 as cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2


class VoiceBioServiceStub(object):
    """Service that implements the Cobalt VoiceBio API.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Version = channel.unary_unary(
                '/cobaltspeech.voicebio.v1.VoiceBioService/Version',
                request_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionResponse.FromString,
                )
        self.ListModels = channel.unary_unary(
                '/cobaltspeech.voicebio.v1.VoiceBioService/ListModels',
                request_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsResponse.FromString,
                )
        self.StreamingEnroll = channel.stream_unary(
                '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingEnroll',
                request_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollResponse.FromString,
                )
        self.StreamingVerify = channel.stream_unary(
                '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingVerify',
                request_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyResponse.FromString,
                )
        self.StreamingIdentify = channel.stream_unary(
                '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingIdentify',
                request_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyResponse.FromString,
                )


class VoiceBioServiceServicer(object):
    """Service that implements the Cobalt VoiceBio API.
    """

    def Version(self, request, context):
        """Returns version information from the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """Returns information about the models available on the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingEnroll(self, request_iterator, context):
        """Uses new audio data to perform enrollment of new users, or to update
        enrollment of existing users. Returns a new or updated voiceprint.

        Clients should store the returned voiceprint against the ID of the user
        that provided the audio. This voiceprint can be provided later, with the
        Verify or Identify requests to match new audio against known speakers.

        If this call is used to update an existing user's voiceprint, the old
        voiceprint can be discarded and only the new one can be stored for that
        user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingVerify(self, request_iterator, context):
        """Compares audio data against the provided voiceprint and verifies whether or
        not the audio matches against the voiceprint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingIdentify(self, request_iterator, context):
        """Compares audio data against the provided list of voiceprints and identifies
        which (or none) of the voiceprints is a match for the given audio.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoiceBioServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsResponse.SerializeToString,
            ),
            'StreamingEnroll': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamingEnroll,
                    request_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollResponse.SerializeToString,
            ),
            'StreamingVerify': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamingVerify,
                    request_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyResponse.SerializeToString,
            ),
            'StreamingIdentify': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamingIdentify,
                    request_deserializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyRequest.FromString,
                    response_serializer=cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cobaltspeech.voicebio.v1.VoiceBioService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VoiceBioService(object):
    """Service that implements the Cobalt VoiceBio API.
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
        return grpc.experimental.unary_unary(request, target, '/cobaltspeech.voicebio.v1.VoiceBioService/Version',
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionRequest.SerializeToString,
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.VersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/cobaltspeech.voicebio.v1.VoiceBioService/ListModels',
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsRequest.SerializeToString,
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.ListModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingEnroll(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingEnroll',
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollRequest.SerializeToString,
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingEnrollResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingVerify(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingVerify',
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyRequest.SerializeToString,
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingVerifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingIdentify(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/cobaltspeech.voicebio.v1.VoiceBioService/StreamingIdentify',
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyRequest.SerializeToString,
            cobaltspeech_dot_voicebio_dot_v1_dot_voicebio__pb2.StreamingIdentifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
