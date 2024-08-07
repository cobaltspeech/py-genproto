# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cobaltspeech.cubic.v1 import cubic_pb2 as cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CubicStub(object):
    """Service that implements the Cobalt Cubic Speech Recognition API
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Version = channel.unary_unary(
                '/cobaltspeech.cubic.Cubic/Version',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.VersionResponse.FromString,
                _registered_method=True)
        self.ListModels = channel.unary_unary(
                '/cobaltspeech.cubic.Cubic/ListModels',
                request_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsResponse.FromString,
                _registered_method=True)
        self.Recognize = channel.unary_unary(
                '/cobaltspeech.cubic.Cubic/Recognize',
                request_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognizeRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.FromString,
                _registered_method=True)
        self.StreamingRecognize = channel.stream_stream(
                '/cobaltspeech.cubic.Cubic/StreamingRecognize',
                request_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.StreamingRecognizeRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.FromString,
                _registered_method=True)
        self.CompileContext = channel.unary_unary(
                '/cobaltspeech.cubic.Cubic/CompileContext',
                request_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextRequest.SerializeToString,
                response_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextResponse.FromString,
                _registered_method=True)


class CubicServicer(object):
    """Service that implements the Cobalt Cubic Speech Recognition API
    """

    def Version(self, request, context):
        """Queries the Version of the Server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """Retrieves a list of available speech recognition models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recognize(self, request, context):
        """Performs synchronous speech recognition: receive results after all audio
        has been sent and processed.  It is expected that this request be typically
        used for short audio content: less than a minute long.  For longer content,
        the `StreamingRecognize` method should be preferred.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingRecognize(self, request_iterator, context):
        """Performs bidirectional streaming speech recognition.  Receive results while
        sending audio.  This method is only available via GRPC and not via
        HTTP+JSON. However, a web browser may use websockets to use this service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompileContext(self, request, context):
        """Compiles recognition context information, such as a specialized list of
        words or phrases, into a compact, efficient form to send with subsequent
        `Recognize` or `StreamingRecognize` requests to customize speech
        recognition. For example, a list of contact names may be compiled in a
        mobile app and sent with each recognition request so that the app user's
        contact names are more likely to be recognized than arbitrary names. This
        pre-compilation ensures that there is no added latency for the recognition
        request. It is important to note that in order to compile context for a
        model, that model has to support context in the first place, which can be
        verified by checking its `ModelAttributes.ContextInfo` obtained via the
        `ListModels` method. Also, the compiled data will be model specific; that
        is, the data compiled for one model will generally not be usable with a
        different model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CubicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.VersionResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsRequest.FromString,
                    response_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsResponse.SerializeToString,
            ),
            'Recognize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognizeRequest.FromString,
                    response_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.SerializeToString,
            ),
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.StreamingRecognizeRequest.FromString,
                    response_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.SerializeToString,
            ),
            'CompileContext': grpc.unary_unary_rpc_method_handler(
                    servicer.CompileContext,
                    request_deserializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextRequest.FromString,
                    response_serializer=cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cobaltspeech.cubic.Cubic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cobaltspeech.cubic.Cubic', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Cubic(object):
    """Service that implements the Cobalt Cubic Speech Recognition API
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
            '/cobaltspeech.cubic.Cubic/Version',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.VersionResponse.FromString,
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
            '/cobaltspeech.cubic.Cubic/ListModels',
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsRequest.SerializeToString,
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.ListModelsResponse.FromString,
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
    def Recognize(request,
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
            '/cobaltspeech.cubic.Cubic/Recognize',
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognizeRequest.SerializeToString,
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.FromString,
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
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/cobaltspeech.cubic.Cubic/StreamingRecognize',
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.StreamingRecognizeRequest.SerializeToString,
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.RecognitionResponse.FromString,
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
    def CompileContext(request,
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
            '/cobaltspeech.cubic.Cubic/CompileContext',
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextRequest.SerializeToString,
            cobaltspeech_dot_cubic_dot_v1_dot_cubic__pb2.CompileContextResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
