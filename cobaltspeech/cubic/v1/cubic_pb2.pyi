from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecognizeRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    audio: RecognitionAudio
    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]] = ..., audio: _Optional[_Union[RecognitionAudio, _Mapping]] = ...) -> None: ...

class StreamingRecognizeRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    audio: RecognitionAudio
    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]] = ..., audio: _Optional[_Union[RecognitionAudio, _Mapping]] = ...) -> None: ...

class CompileContextRequest(_message.Message):
    __slots__ = ("model_id", "token", "phrases")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    token: str
    phrases: _containers.RepeatedCompositeFieldContainer[ContextPhrase]
    def __init__(self, model_id: _Optional[str] = ..., token: _Optional[str] = ..., phrases: _Optional[_Iterable[_Union[ContextPhrase, _Mapping]]] = ...) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("cubic", "server")
    CUBIC_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    cubic: str
    server: str
    def __init__(self, cubic: _Optional[str] = ..., server: _Optional[str] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class RecognitionResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[RecognitionResult]
    def __init__(self, results: _Optional[_Iterable[_Union[RecognitionResult, _Mapping]]] = ...) -> None: ...

class CompileContextResponse(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: CompiledContext
    def __init__(self, context: _Optional[_Union[CompiledContext, _Mapping]] = ...) -> None: ...

class RecognitionConfig(_message.Message):
    __slots__ = ("model_id", "audio_encoding", "idle_timeout", "enable_word_time_offsets", "enable_word_confidence", "enable_raw_transcript", "enable_confusion_network", "audio_channels", "metadata", "context")
    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAW_LINEAR16: _ClassVar[RecognitionConfig.Encoding]
        WAV: _ClassVar[RecognitionConfig.Encoding]
        MP3: _ClassVar[RecognitionConfig.Encoding]
        FLAC: _ClassVar[RecognitionConfig.Encoding]
        VOX8000: _ClassVar[RecognitionConfig.Encoding]
        ULAW8000: _ClassVar[RecognitionConfig.Encoding]
        ALAW8000: _ClassVar[RecognitionConfig.Encoding]
        OPUS: _ClassVar[RecognitionConfig.Encoding]
    RAW_LINEAR16: RecognitionConfig.Encoding
    WAV: RecognitionConfig.Encoding
    MP3: RecognitionConfig.Encoding
    FLAC: RecognitionConfig.Encoding
    VOX8000: RecognitionConfig.Encoding
    ULAW8000: RecognitionConfig.Encoding
    ALAW8000: RecognitionConfig.Encoding
    OPUS: RecognitionConfig.Encoding
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_TIME_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RAW_TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONFUSION_NETWORK_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    audio_encoding: RecognitionConfig.Encoding
    idle_timeout: _duration_pb2.Duration
    enable_word_time_offsets: bool
    enable_word_confidence: bool
    enable_raw_transcript: bool
    enable_confusion_network: bool
    audio_channels: _containers.RepeatedScalarFieldContainer[int]
    metadata: RecognitionMetadata
    context: RecognitionContext
    def __init__(self, model_id: _Optional[str] = ..., audio_encoding: _Optional[_Union[RecognitionConfig.Encoding, str]] = ..., idle_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., enable_word_time_offsets: bool = ..., enable_word_confidence: bool = ..., enable_raw_transcript: bool = ..., enable_confusion_network: bool = ..., audio_channels: _Optional[_Iterable[int]] = ..., metadata: _Optional[_Union[RecognitionMetadata, _Mapping]] = ..., context: _Optional[_Union[RecognitionContext, _Mapping]] = ...) -> None: ...

class RecognitionMetadata(_message.Message):
    __slots__ = ("custom_metadata",)
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    custom_metadata: str
    def __init__(self, custom_metadata: _Optional[str] = ...) -> None: ...

class RecognitionContext(_message.Message):
    __slots__ = ("compiled",)
    COMPILED_FIELD_NUMBER: _ClassVar[int]
    compiled: _containers.RepeatedCompositeFieldContainer[CompiledContext]
    def __init__(self, compiled: _Optional[_Iterable[_Union[CompiledContext, _Mapping]]] = ...) -> None: ...

class CompiledContext(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ContextPhrase(_message.Message):
    __slots__ = ("text", "boost")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    text: str
    boost: float
    def __init__(self, text: _Optional[str] = ..., boost: _Optional[float] = ...) -> None: ...

class RecognitionAudio(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("id", "name", "attributes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    attributes: ModelAttributes
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., attributes: _Optional[_Union[ModelAttributes, _Mapping]] = ...) -> None: ...

class ModelAttributes(_message.Message):
    __slots__ = ("sample_rate", "context_info")
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_INFO_FIELD_NUMBER: _ClassVar[int]
    sample_rate: int
    context_info: ContextInfo
    def __init__(self, sample_rate: _Optional[int] = ..., context_info: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ContextInfo(_message.Message):
    __slots__ = ("supports_context", "allowed_context_tokens")
    SUPPORTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    supports_context: bool
    allowed_context_tokens: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, supports_context: bool = ..., allowed_context_tokens: _Optional[_Iterable[str]] = ...) -> None: ...

class RecognitionResult(_message.Message):
    __slots__ = ("alternatives", "is_partial", "cnet", "audio_channel")
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    CNET_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[RecognitionAlternative]
    is_partial: bool
    cnet: RecognitionConfusionNetwork
    audio_channel: int
    def __init__(self, alternatives: _Optional[_Iterable[_Union[RecognitionAlternative, _Mapping]]] = ..., is_partial: bool = ..., cnet: _Optional[_Union[RecognitionConfusionNetwork, _Mapping]] = ..., audio_channel: _Optional[int] = ...) -> None: ...

class RecognitionAlternative(_message.Message):
    __slots__ = ("transcript", "raw_transcript", "confidence", "words", "raw_words", "start_time", "duration")
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    RAW_TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    RAW_WORDS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    transcript: str
    raw_transcript: str
    confidence: float
    words: _containers.RepeatedCompositeFieldContainer[WordInfo]
    raw_words: _containers.RepeatedCompositeFieldContainer[WordInfo]
    start_time: _duration_pb2.Duration
    duration: _duration_pb2.Duration
    def __init__(self, transcript: _Optional[str] = ..., raw_transcript: _Optional[str] = ..., confidence: _Optional[float] = ..., words: _Optional[_Iterable[_Union[WordInfo, _Mapping]]] = ..., raw_words: _Optional[_Iterable[_Union[WordInfo, _Mapping]]] = ..., start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class WordInfo(_message.Message):
    __slots__ = ("word", "confidence", "start_time", "duration")
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    word: str
    confidence: float
    start_time: _duration_pb2.Duration
    duration: _duration_pb2.Duration
    def __init__(self, word: _Optional[str] = ..., confidence: _Optional[float] = ..., start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RecognitionConfusionNetwork(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[ConfusionNetworkLink]
    def __init__(self, links: _Optional[_Iterable[_Union[ConfusionNetworkLink, _Mapping]]] = ...) -> None: ...

class ConfusionNetworkLink(_message.Message):
    __slots__ = ("start_time", "duration", "arcs")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ARCS_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    duration: _duration_pb2.Duration
    arcs: _containers.RepeatedCompositeFieldContainer[ConfusionNetworkArc]
    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., arcs: _Optional[_Iterable[_Union[ConfusionNetworkArc, _Mapping]]] = ...) -> None: ...

class ConfusionNetworkArc(_message.Message):
    __slots__ = ("word", "confidence")
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    word: str
    confidence: float
    def __init__(self, word: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...
