from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class RedactTextRequest(_message.Message):
    __slots__ = ("config", "text")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    config: RedactionConfig
    text: str
    def __init__(self, config: _Optional[_Union[RedactionConfig, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class RedactTextResponse(_message.Message):
    __slots__ = ("text", "redacted_tokens")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    REDACTED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    text: str
    redacted_tokens: _containers.RepeatedCompositeFieldContainer[RedactedToken]
    def __init__(self, text: _Optional[str] = ..., redacted_tokens: _Optional[_Iterable[_Union[RedactedToken, _Mapping]]] = ...) -> None: ...

class RedactTranscriptRequest(_message.Message):
    __slots__ = ("config", "transcript")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    config: RedactionConfig
    transcript: Transcript
    def __init__(self, config: _Optional[_Union[RedactionConfig, _Mapping]] = ..., transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class RedactTranscriptResponse(_message.Message):
    __slots__ = ("transcript",)
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    transcript: Transcript
    def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class StreamingRedactTranscribedAudioRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: RedactTranscribedAudioConfig
    audio: bytes
    def __init__(self, config: _Optional[_Union[RedactTranscribedAudioConfig, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class StreamingRedactTranscribedAudioResponse(_message.Message):
    __slots__ = ("utterance", "audio")
    UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    utterance: Utterance
    audio: bytes
    def __init__(self, utterance: _Optional[_Union[Utterance, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class StreamingTranscribeAndRedactRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: TranscribeAndRedactConfig
    audio: bytes
    def __init__(self, config: _Optional[_Union[TranscribeAndRedactConfig, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class StreamingTranscribeAndRedactResponse(_message.Message):
    __slots__ = ("utterance", "audio")
    UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    utterance: TranscribeAndRedactUtterance
    audio: bytes
    def __init__(self, utterance: _Optional[_Union[TranscribeAndRedactUtterance, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class ModelInfo(_message.Message):
    __slots__ = ("id", "name", "redaction_classes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CLASSES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    redaction_classes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., redaction_classes: _Optional[_Iterable[str]] = ...) -> None: ...

class RedactTranscribedAudioConfig(_message.Message):
    __slots__ = ("redaction_config", "transcript")
    REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    redaction_config: RedactionConfig
    transcript: Transcript
    def __init__(self, redaction_config: _Optional[_Union[RedactionConfig, _Mapping]] = ..., transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class TranscribeAndRedactConfig(_message.Message):
    __slots__ = ("redaction_config", "enable_unredacted_transcript")
    REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_UNREDACTED_TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    redaction_config: RedactionConfig
    enable_unredacted_transcript: bool
    def __init__(self, redaction_config: _Optional[_Union[RedactionConfig, _Mapping]] = ..., enable_unredacted_transcript: bool = ...) -> None: ...

class CustomClass(_message.Message):
    __slots__ = ("redaction_class", "pattern")
    REDACTION_CLASS_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    redaction_class: str
    pattern: str
    def __init__(self, redaction_class: _Optional[str] = ..., pattern: _Optional[str] = ...) -> None: ...

class RedactionConfig(_message.Message):
    __slots__ = ("model_id", "redaction_classes", "disable_streaming", "custom_classes", "custom_unredacted_classes", "disabled_classes")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CLASSES_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STREAMING_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_UNREDACTED_CLASSES_FIELD_NUMBER: _ClassVar[int]
    DISABLED_CLASSES_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    redaction_classes: _containers.RepeatedScalarFieldContainer[str]
    disable_streaming: bool
    custom_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]
    custom_unredacted_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]
    disabled_classes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model_id: _Optional[str] = ..., redaction_classes: _Optional[_Iterable[str]] = ..., disable_streaming: bool = ..., custom_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]] = ..., custom_unredacted_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]] = ..., disabled_classes: _Optional[_Iterable[str]] = ...) -> None: ...

class Transcript(_message.Message):
    __slots__ = ("utterances",)
    UTTERANCES_FIELD_NUMBER: _ClassVar[int]
    utterances: _containers.RepeatedCompositeFieldContainer[Utterance]
    def __init__(self, utterances: _Optional[_Iterable[_Union[Utterance, _Mapping]]] = ...) -> None: ...

class TranscribeAndRedactUtterance(_message.Message):
    __slots__ = ("redacted", "unredacted")
    REDACTED_FIELD_NUMBER: _ClassVar[int]
    UNREDACTED_FIELD_NUMBER: _ClassVar[int]
    redacted: Utterance
    unredacted: Utterance
    def __init__(self, redacted: _Optional[_Union[Utterance, _Mapping]] = ..., unredacted: _Optional[_Union[Utterance, _Mapping]] = ...) -> None: ...

class Utterance(_message.Message):
    __slots__ = ("audio_channel", "start_time_ms", "duration_ms", "asr_confidence", "words")
    AUDIO_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ASR_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    audio_channel: int
    start_time_ms: int
    duration_ms: int
    asr_confidence: float
    words: _containers.RepeatedCompositeFieldContainer[Word]
    def __init__(self, audio_channel: _Optional[int] = ..., start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., asr_confidence: _Optional[float] = ..., words: _Optional[_Iterable[_Union[Word, _Mapping]]] = ...) -> None: ...

class Word(_message.Message):
    __slots__ = ("text", "asr_confidence", "start_time_ms", "duration_ms", "is_redacted", "redaction_class", "redaction_confidence")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ASR_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    IS_REDACTED_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CLASS_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    text: str
    asr_confidence: float
    start_time_ms: int
    duration_ms: int
    is_redacted: bool
    redaction_class: str
    redaction_confidence: float
    def __init__(self, text: _Optional[str] = ..., asr_confidence: _Optional[float] = ..., start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., is_redacted: bool = ..., redaction_class: _Optional[str] = ..., redaction_confidence: _Optional[float] = ...) -> None: ...

class RedactedToken(_message.Message):
    __slots__ = ("original_text", "original_offset", "original_length", "redaction_class", "redaction_confidence")
    ORIGINAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CLASS_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    original_text: str
    original_offset: int
    original_length: int
    redaction_class: str
    redaction_confidence: float
    def __init__(self, original_text: _Optional[str] = ..., original_offset: _Optional[int] = ..., original_length: _Optional[int] = ..., redaction_class: _Optional[str] = ..., redaction_confidence: _Optional[float] = ...) -> None: ...
