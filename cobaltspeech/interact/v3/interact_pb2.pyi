from cobaltspeech.chosun.v2 import chosun_pb2 as _chosun_pb2
from cobaltspeech.cubic.v5 import cubic_pb2 as _cubic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ["diatheke", "chosun", "cubic", "luna"]
    DIATHEKE_FIELD_NUMBER: _ClassVar[int]
    CHOSUN_FIELD_NUMBER: _ClassVar[int]
    CUBIC_FIELD_NUMBER: _ClassVar[int]
    LUNA_FIELD_NUMBER: _ClassVar[int]
    diatheke: str
    chosun: str
    cubic: str
    luna: str
    def __init__(self, diatheke: _Optional[str] = ..., chosun: _Optional[str] = ..., cubic: _Optional[str] = ..., luna: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ["models"]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ModelInfo]
    def __init__(self, models: _Optional[_Iterable[_Union[ModelInfo, _Mapping]]] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ["model_id", "wakeword"]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    WAKEWORD_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    wakeword: str
    def __init__(self, model_id: _Optional[str] = ..., wakeword: _Optional[str] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ["session_output"]
    SESSION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    session_output: SessionOutput
    def __init__(self, session_output: _Optional[_Union[SessionOutput, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ["token_data"]
    TOKEN_DATA_FIELD_NUMBER: _ClassVar[int]
    token_data: TokenData
    def __init__(self, token_data: _Optional[_Union[TokenData, _Mapping]] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ["session_input"]
    SESSION_INPUT_FIELD_NUMBER: _ClassVar[int]
    session_input: SessionInput
    def __init__(self, session_input: _Optional[_Union[SessionInput, _Mapping]] = ...) -> None: ...

class UpdateSessionResponse(_message.Message):
    __slots__ = ["session_output"]
    SESSION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    session_output: SessionOutput
    def __init__(self, session_output: _Optional[_Union[SessionOutput, _Mapping]] = ...) -> None: ...

class StreamTTSRequest(_message.Message):
    __slots__ = ["reply_action"]
    REPLY_ACTION_FIELD_NUMBER: _ClassVar[int]
    reply_action: ReplyAction
    def __init__(self, reply_action: _Optional[_Union[ReplyAction, _Mapping]] = ...) -> None: ...

class StreamTTSResponse(_message.Message):
    __slots__ = ["audio"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    def __init__(self, audio: _Optional[bytes] = ...) -> None: ...

class ModelInfo(_message.Message):
    __slots__ = ["id", "name", "language", "asr_sample_rate", "tts_sample_rate"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ASR_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    TTS_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    language: str
    asr_sample_rate: int
    tts_sample_rate: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., language: _Optional[str] = ..., asr_sample_rate: _Optional[int] = ..., tts_sample_rate: _Optional[int] = ...) -> None: ...

class SessionInput(_message.Message):
    __slots__ = ["token", "text", "asr", "cmd", "story"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ASR_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    STORY_FIELD_NUMBER: _ClassVar[int]
    token: TokenData
    text: TextInput
    asr: ASRResult
    cmd: CommandResult
    story: SetStory
    def __init__(self, token: _Optional[_Union[TokenData, _Mapping]] = ..., text: _Optional[_Union[TextInput, _Mapping]] = ..., asr: _Optional[_Union[ASRResult, _Mapping]] = ..., cmd: _Optional[_Union[CommandResult, _Mapping]] = ..., story: _Optional[_Union[SetStory, _Mapping]] = ...) -> None: ...

class TokenData(_message.Message):
    __slots__ = ["data", "id", "metadata"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    id: str
    metadata: str
    def __init__(self, data: _Optional[bytes] = ..., id: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class TextInput(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class CommandResult(_message.Message):
    __slots__ = ["id", "out_parameters", "error"]
    class OutParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    out_parameters: _containers.ScalarMap[str, str]
    error: str
    def __init__(self, id: _Optional[str] = ..., out_parameters: _Optional[_Mapping[str, str]] = ..., error: _Optional[str] = ...) -> None: ...

class SetStory(_message.Message):
    __slots__ = ["story_id", "parameters"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    story_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, story_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SessionOutput(_message.Message):
    __slots__ = ["token", "action_list"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    token: TokenData
    action_list: _containers.RepeatedCompositeFieldContainer[ActionData]
    def __init__(self, token: _Optional[_Union[TokenData, _Mapping]] = ..., action_list: _Optional[_Iterable[_Union[ActionData, _Mapping]]] = ...) -> None: ...

class ActionData(_message.Message):
    __slots__ = ["input", "command", "reply", "transcribe"]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIBE_FIELD_NUMBER: _ClassVar[int]
    input: WaitForUserAction
    command: CommandAction
    reply: ReplyAction
    transcribe: TranscribeAction
    def __init__(self, input: _Optional[_Union[WaitForUserAction, _Mapping]] = ..., command: _Optional[_Union[CommandAction, _Mapping]] = ..., reply: _Optional[_Union[ReplyAction, _Mapping]] = ..., transcribe: _Optional[_Union[TranscribeAction, _Mapping]] = ...) -> None: ...

class WaitForUserAction(_message.Message):
    __slots__ = ["requires_wake_word", "immediate"]
    REQUIRES_WAKE_WORD_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_FIELD_NUMBER: _ClassVar[int]
    requires_wake_word: bool
    immediate: bool
    def __init__(self, requires_wake_word: bool = ..., immediate: bool = ...) -> None: ...

class CommandAction(_message.Message):
    __slots__ = ["id", "input_parameters", "nlu_result"]
    class InputParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    NLU_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    input_parameters: _containers.ScalarMap[str, str]
    nlu_result: _chosun_pb2.ParseResponse
    def __init__(self, id: _Optional[str] = ..., input_parameters: _Optional[_Mapping[str, str]] = ..., nlu_result: _Optional[_Union[_chosun_pb2.ParseResponse, _Mapping]] = ...) -> None: ...

class ReplyAction(_message.Message):
    __slots__ = ["text", "luna_model"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LUNA_MODEL_FIELD_NUMBER: _ClassVar[int]
    text: str
    luna_model: str
    def __init__(self, text: _Optional[str] = ..., luna_model: _Optional[str] = ...) -> None: ...

class TranscribeAction(_message.Message):
    __slots__ = ["id", "cubic_model_id", "diatheke_model_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CUBIC_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DIATHEKE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    cubic_model_id: str
    diatheke_model_id: str
    def __init__(self, id: _Optional[str] = ..., cubic_model_id: _Optional[str] = ..., diatheke_model_id: _Optional[str] = ...) -> None: ...

class StreamASRRequest(_message.Message):
    __slots__ = ["token", "audio"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    token: TokenData
    audio: bytes
    def __init__(self, token: _Optional[_Union[TokenData, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class StreamASRResponse(_message.Message):
    __slots__ = ["asr_result"]
    ASR_RESULT_FIELD_NUMBER: _ClassVar[int]
    asr_result: ASRResult
    def __init__(self, asr_result: _Optional[_Union[ASRResult, _Mapping]] = ...) -> None: ...

class StreamASRWithPartialsRequest(_message.Message):
    __slots__ = ["token", "audio"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    token: TokenData
    audio: bytes
    def __init__(self, token: _Optional[_Union[TokenData, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class StreamASRWithPartialsResponse(_message.Message):
    __slots__ = ["partial_result", "asr_result"]
    PARTIAL_RESULT_FIELD_NUMBER: _ClassVar[int]
    ASR_RESULT_FIELD_NUMBER: _ClassVar[int]
    partial_result: _cubic_pb2.RecognitionResult
    asr_result: ASRResult
    def __init__(self, partial_result: _Optional[_Union[_cubic_pb2.RecognitionResult, _Mapping]] = ..., asr_result: _Optional[_Union[ASRResult, _Mapping]] = ...) -> None: ...

class ASRResult(_message.Message):
    __slots__ = ["text", "confidence", "timed_out", "cubic_result"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    CUBIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    text: str
    confidence: float
    timed_out: bool
    cubic_result: _cubic_pb2.RecognitionResult
    def __init__(self, text: _Optional[str] = ..., confidence: _Optional[float] = ..., timed_out: bool = ..., cubic_result: _Optional[_Union[_cubic_pb2.RecognitionResult, _Mapping]] = ...) -> None: ...

class TranscribeRequest(_message.Message):
    __slots__ = ["action", "audio"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    action: TranscribeAction
    audio: bytes
    def __init__(self, action: _Optional[_Union[TranscribeAction, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class TranscribeResponse(_message.Message):
    __slots__ = ["text", "confidence", "is_partial", "cubic_result"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    CUBIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    text: str
    confidence: float
    is_partial: bool
    cubic_result: _cubic_pb2.RecognitionResult
    def __init__(self, text: _Optional[str] = ..., confidence: _Optional[float] = ..., is_partial: bool = ..., cubic_result: _Optional[_Union[_cubic_pb2.RecognitionResult, _Mapping]] = ...) -> None: ...
