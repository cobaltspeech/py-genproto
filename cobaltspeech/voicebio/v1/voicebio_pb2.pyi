from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ByteOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BYTE_ORDER_UNSPECIFIED: _ClassVar[ByteOrder]
    BYTE_ORDER_LITTLE_ENDIAN: _ClassVar[ByteOrder]
    BYTE_ORDER_BIG_ENDIAN: _ClassVar[ByteOrder]

class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_ENCODING_UNSPECIFIED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_SIGNED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_UNSIGNED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_IEEE_FLOAT: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_ULAW: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_ALAW: _ClassVar[AudioEncoding]

class AudioFormatHeadered(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_FORMAT_HEADERED_UNSPECIFIED: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_WAV: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_MP3: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_FLAC: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_OGG_OPUS: _ClassVar[AudioFormatHeadered]
BYTE_ORDER_UNSPECIFIED: ByteOrder
BYTE_ORDER_LITTLE_ENDIAN: ByteOrder
BYTE_ORDER_BIG_ENDIAN: ByteOrder
AUDIO_ENCODING_UNSPECIFIED: AudioEncoding
AUDIO_ENCODING_SIGNED: AudioEncoding
AUDIO_ENCODING_UNSIGNED: AudioEncoding
AUDIO_ENCODING_IEEE_FLOAT: AudioEncoding
AUDIO_ENCODING_ULAW: AudioEncoding
AUDIO_ENCODING_ALAW: AudioEncoding
AUDIO_FORMAT_HEADERED_UNSPECIFIED: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_WAV: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_MP3: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_FLAC: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_OGG_OPUS: AudioFormatHeadered

class VersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class StreamingEnrollRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: EnrollmentConfig
    audio: Audio
    def __init__(self, config: _Optional[_Union[EnrollmentConfig, _Mapping]] = ..., audio: _Optional[_Union[Audio, _Mapping]] = ...) -> None: ...

class StreamingEnrollResponse(_message.Message):
    __slots__ = ("voiceprint", "enrollment_status")
    VOICEPRINT_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    voiceprint: Voiceprint
    enrollment_status: EnrollmentStatus
    def __init__(self, voiceprint: _Optional[_Union[Voiceprint, _Mapping]] = ..., enrollment_status: _Optional[_Union[EnrollmentStatus, _Mapping]] = ...) -> None: ...

class EnrollmentConfig(_message.Message):
    __slots__ = ("model_id", "audio_format", "previous_voiceprint")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VOICEPRINT_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    audio_format: AudioFormat
    previous_voiceprint: Voiceprint
    def __init__(self, model_id: _Optional[str] = ..., audio_format: _Optional[_Union[AudioFormat, _Mapping]] = ..., previous_voiceprint: _Optional[_Union[Voiceprint, _Mapping]] = ...) -> None: ...

class EnrollmentStatus(_message.Message):
    __slots__ = ("enrollment_complete", "additional_audio_required_seconds")
    ENROLLMENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_AUDIO_REQUIRED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    enrollment_complete: bool
    additional_audio_required_seconds: int
    def __init__(self, enrollment_complete: bool = ..., additional_audio_required_seconds: _Optional[int] = ...) -> None: ...

class StreamingVerifyRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: VerificationConfig
    audio: Audio
    def __init__(self, config: _Optional[_Union[VerificationConfig, _Mapping]] = ..., audio: _Optional[_Union[Audio, _Mapping]] = ...) -> None: ...

class StreamingVerifyResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: VoiceprintComparisonResult
    def __init__(self, result: _Optional[_Union[VoiceprintComparisonResult, _Mapping]] = ...) -> None: ...

class VoiceprintComparisonResult(_message.Message):
    __slots__ = ("is_match", "similarity_score")
    IS_MATCH_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    is_match: bool
    similarity_score: float
    def __init__(self, is_match: bool = ..., similarity_score: _Optional[float] = ...) -> None: ...

class VerificationConfig(_message.Message):
    __slots__ = ("model_id", "audio_format", "voiceprint")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VOICEPRINT_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    audio_format: AudioFormat
    voiceprint: Voiceprint
    def __init__(self, model_id: _Optional[str] = ..., audio_format: _Optional[_Union[AudioFormat, _Mapping]] = ..., voiceprint: _Optional[_Union[Voiceprint, _Mapping]] = ...) -> None: ...

class StreamingIdentifyRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: IdentificationConfig
    audio: Audio
    def __init__(self, config: _Optional[_Union[IdentificationConfig, _Mapping]] = ..., audio: _Optional[_Union[Audio, _Mapping]] = ...) -> None: ...

class StreamingIdentifyResponse(_message.Message):
    __slots__ = ("best_match_index", "voiceprint_comparison_results")
    BEST_MATCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    VOICEPRINT_COMPARISON_RESULTS_FIELD_NUMBER: _ClassVar[int]
    best_match_index: int
    voiceprint_comparison_results: _containers.RepeatedCompositeFieldContainer[VoiceprintComparisonResult]
    def __init__(self, best_match_index: _Optional[int] = ..., voiceprint_comparison_results: _Optional[_Iterable[_Union[VoiceprintComparisonResult, _Mapping]]] = ...) -> None: ...

class IdentificationConfig(_message.Message):
    __slots__ = ("model_id", "audio_format", "voiceprints")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VOICEPRINTS_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    audio_format: AudioFormat
    voiceprints: _containers.RepeatedCompositeFieldContainer[Voiceprint]
    def __init__(self, model_id: _Optional[str] = ..., audio_format: _Optional[_Union[AudioFormat, _Mapping]] = ..., voiceprints: _Optional[_Iterable[_Union[Voiceprint, _Mapping]]] = ...) -> None: ...

class Voiceprint(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class AudioFormat(_message.Message):
    __slots__ = ("audio_format_raw", "audio_format_headered")
    AUDIO_FORMAT_RAW_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_HEADERED_FIELD_NUMBER: _ClassVar[int]
    audio_format_raw: AudioFormatRAW
    audio_format_headered: AudioFormatHeadered
    def __init__(self, audio_format_raw: _Optional[_Union[AudioFormatRAW, _Mapping]] = ..., audio_format_headered: _Optional[_Union[AudioFormatHeadered, str]] = ...) -> None: ...

class AudioFormatRAW(_message.Message):
    __slots__ = ("encoding", "bit_depth", "byte_order", "sample_rate", "channels")
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    BYTE_ORDER_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    encoding: AudioEncoding
    bit_depth: int
    byte_order: ByteOrder
    sample_rate: int
    channels: int
    def __init__(self, encoding: _Optional[_Union[AudioEncoding, str]] = ..., bit_depth: _Optional[int] = ..., byte_order: _Optional[_Union[ByteOrder, str]] = ..., sample_rate: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class Audio(_message.Message):
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
    __slots__ = ("sample_rate",)
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    sample_rate: int
    def __init__(self, sample_rate: _Optional[int] = ...) -> None: ...
