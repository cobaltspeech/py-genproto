from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_SET_UNSPECIFIED: _ClassVar[PhoneSet]
    PHONE_SET_IPA: _ClassVar[PhoneSet]
    PHONE_SET_XSAMPA: _ClassVar[PhoneSet]
    PHONE_SET_ARPABET: _ClassVar[PhoneSet]

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

class AudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_CODEC_UNSPECIFIED: _ClassVar[AudioCodec]
    AUDIO_CODEC_RAW: _ClassVar[AudioCodec]
    AUDIO_CODEC_WAV: _ClassVar[AudioCodec]
PHONE_SET_UNSPECIFIED: PhoneSet
PHONE_SET_IPA: PhoneSet
PHONE_SET_XSAMPA: PhoneSet
PHONE_SET_ARPABET: PhoneSet
BYTE_ORDER_UNSPECIFIED: ByteOrder
BYTE_ORDER_LITTLE_ENDIAN: ByteOrder
BYTE_ORDER_BIG_ENDIAN: ByteOrder
AUDIO_ENCODING_UNSPECIFIED: AudioEncoding
AUDIO_ENCODING_SIGNED: AudioEncoding
AUDIO_ENCODING_UNSIGNED: AudioEncoding
AUDIO_ENCODING_IEEE_FLOAT: AudioEncoding
AUDIO_ENCODING_ULAW: AudioEncoding
AUDIO_ENCODING_ALAW: AudioEncoding
AUDIO_CODEC_UNSPECIFIED: AudioCodec
AUDIO_CODEC_RAW: AudioCodec
AUDIO_CODEC_WAV: AudioCodec

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
    models: _containers.RepeatedCompositeFieldContainer[ModelInfo]
    def __init__(self, models: _Optional[_Iterable[_Union[ModelInfo, _Mapping]]] = ...) -> None: ...

class StreamingSynthesizeRequest(_message.Message):
    __slots__ = ("config", "text")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    config: SynthesisConfig
    text: SynthesisText
    def __init__(self, config: _Optional[_Union[SynthesisConfig, _Mapping]] = ..., text: _Optional[_Union[SynthesisText, _Mapping]] = ...) -> None: ...

class StreamingSynthesizeResponse(_message.Message):
    __slots__ = ("audio",)
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    audio: SynthesizedAudio
    def __init__(self, audio: _Optional[_Union[SynthesizedAudio, _Mapping]] = ...) -> None: ...

class ModelInfo(_message.Message):
    __slots__ = ("id", "name", "attributes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    attributes: ModelAttributes
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., attributes: _Optional[_Union[ModelAttributes, _Mapping]] = ...) -> None: ...

class ModelAttributes(_message.Message):
    __slots__ = ("language", "phone_set", "native_audio_format", "supported_features", "speakers")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PHONE_SET_FIELD_NUMBER: _ClassVar[int]
    NATIVE_AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    language: str
    phone_set: PhoneSet
    native_audio_format: AudioFormat
    supported_features: ModelFeatures
    speakers: _containers.RepeatedCompositeFieldContainer[SpeakerInfo]
    def __init__(self, language: _Optional[str] = ..., phone_set: _Optional[_Union[PhoneSet, str]] = ..., native_audio_format: _Optional[_Union[AudioFormat, _Mapping]] = ..., supported_features: _Optional[_Union[ModelFeatures, _Mapping]] = ..., speakers: _Optional[_Iterable[_Union[SpeakerInfo, _Mapping]]] = ...) -> None: ...

class ModelFeatures(_message.Message):
    __slots__ = ("speech_rate", "variation_scale")
    SPEECH_RATE_FIELD_NUMBER: _ClassVar[int]
    VARIATION_SCALE_FIELD_NUMBER: _ClassVar[int]
    speech_rate: bool
    variation_scale: bool
    def __init__(self, speech_rate: bool = ..., variation_scale: bool = ...) -> None: ...

class SpeakerInfo(_message.Message):
    __slots__ = ("id", "name", "description", "attributes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    attributes: SpeakerAttributes
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Union[SpeakerAttributes, _Mapping]] = ...) -> None: ...

class SpeakerAttributes(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    def __init__(self, language: _Optional[str] = ...) -> None: ...

class SynthesisConfig(_message.Message):
    __slots__ = ("model_id", "speaker_id", "audio_format", "speech_rate", "variation_scale")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SPEECH_RATE_FIELD_NUMBER: _ClassVar[int]
    VARIATION_SCALE_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    speaker_id: str
    audio_format: AudioFormat
    speech_rate: float
    variation_scale: float
    def __init__(self, model_id: _Optional[str] = ..., speaker_id: _Optional[str] = ..., audio_format: _Optional[_Union[AudioFormat, _Mapping]] = ..., speech_rate: _Optional[float] = ..., variation_scale: _Optional[float] = ...) -> None: ...

class AudioFormat(_message.Message):
    __slots__ = ("sample_rate", "channels", "bit_depth", "codec", "encoding", "byte_order")
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    BYTE_ORDER_FIELD_NUMBER: _ClassVar[int]
    sample_rate: int
    channels: int
    bit_depth: int
    codec: AudioCodec
    encoding: AudioEncoding
    byte_order: ByteOrder
    def __init__(self, sample_rate: _Optional[int] = ..., channels: _Optional[int] = ..., bit_depth: _Optional[int] = ..., codec: _Optional[_Union[AudioCodec, str]] = ..., encoding: _Optional[_Union[AudioEncoding, str]] = ..., byte_order: _Optional[_Union[ByteOrder, str]] = ...) -> None: ...

class SynthesisText(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class SynthesizedAudio(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...
