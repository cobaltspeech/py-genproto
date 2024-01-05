from cobaltspeech.diatheke.v3 import diatheke_pb2 as _diatheke_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("bluehenge", "diatheke_version_response")
    BLUEHENGE_FIELD_NUMBER: _ClassVar[int]
    DIATHEKE_VERSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    bluehenge: str
    diatheke_version_response: _diatheke_pb2.VersionResponse
    def __init__(self, bluehenge: _Optional[str] = ..., diatheke_version_response: _Optional[_Union[_diatheke_pb2.VersionResponse, _Mapping]] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("diatheke_list_models_request",)
    DIATHEKE_LIST_MODELS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_list_models_request: _diatheke_pb2.ListModelsRequest
    def __init__(self, diatheke_list_models_request: _Optional[_Union[_diatheke_pb2.ListModelsRequest, _Mapping]] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("diatheke_list_models_response",)
    DIATHEKE_LIST_MODELS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_list_models_response: _diatheke_pb2.ListModelsResponse
    def __init__(self, diatheke_list_models_response: _Optional[_Union[_diatheke_pb2.ListModelsResponse, _Mapping]] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("diatheke_create_session_request",)
    DIATHEKE_CREATE_SESSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_create_session_request: _diatheke_pb2.CreateSessionRequest
    def __init__(self, diatheke_create_session_request: _Optional[_Union[_diatheke_pb2.CreateSessionRequest, _Mapping]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("diatheke_create_session_response",)
    DIATHEKE_CREATE_SESSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_create_session_response: _diatheke_pb2.CreateSessionResponse
    def __init__(self, diatheke_create_session_response: _Optional[_Union[_diatheke_pb2.CreateSessionResponse, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("diatheke_delete_session_request",)
    DIATHEKE_DELETE_SESSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_delete_session_request: _diatheke_pb2.DeleteSessionRequest
    def __init__(self, diatheke_delete_session_request: _Optional[_Union[_diatheke_pb2.DeleteSessionRequest, _Mapping]] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = ("diatheke_delete_session_response",)
    DIATHEKE_DELETE_SESSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_delete_session_response: _diatheke_pb2.DeleteSessionResponse
    def __init__(self, diatheke_delete_session_response: _Optional[_Union[_diatheke_pb2.DeleteSessionResponse, _Mapping]] = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ("diatheke_update_session_request",)
    DIATHEKE_UPDATE_SESSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_update_session_request: _diatheke_pb2.UpdateSessionRequest
    def __init__(self, diatheke_update_session_request: _Optional[_Union[_diatheke_pb2.UpdateSessionRequest, _Mapping]] = ...) -> None: ...

class UpdateSessionResponse(_message.Message):
    __slots__ = ("diatheke_update_session_response",)
    DIATHEKE_UPDATE_SESSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_update_session_response: _diatheke_pb2.UpdateSessionResponse
    def __init__(self, diatheke_update_session_response: _Optional[_Union[_diatheke_pb2.UpdateSessionResponse, _Mapping]] = ...) -> None: ...

class StreamASRRequest(_message.Message):
    __slots__ = ("diatheke_stream_asr_request",)
    DIATHEKE_STREAM_ASR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_stream_asr_request: _diatheke_pb2.StreamASRRequest
    def __init__(self, diatheke_stream_asr_request: _Optional[_Union[_diatheke_pb2.StreamASRRequest, _Mapping]] = ...) -> None: ...

class StreamASRResponse(_message.Message):
    __slots__ = ("diatheke_stream_asr_response",)
    DIATHEKE_STREAM_ASR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_stream_asr_response: _diatheke_pb2.StreamASRResponse
    def __init__(self, diatheke_stream_asr_response: _Optional[_Union[_diatheke_pb2.StreamASRResponse, _Mapping]] = ...) -> None: ...

class StreamTTSRequest(_message.Message):
    __slots__ = ("diatheke_stream_tts_request",)
    DIATHEKE_STREAM_TTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_stream_tts_request: _diatheke_pb2.StreamTTSRequest
    def __init__(self, diatheke_stream_tts_request: _Optional[_Union[_diatheke_pb2.StreamTTSRequest, _Mapping]] = ...) -> None: ...

class StreamTTSResponse(_message.Message):
    __slots__ = ("diatheke_stream_tts_response",)
    DIATHEKE_STREAM_TTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_stream_tts_response: _diatheke_pb2.StreamTTSResponse
    def __init__(self, diatheke_stream_tts_response: _Optional[_Union[_diatheke_pb2.StreamTTSResponse, _Mapping]] = ...) -> None: ...

class TranscribeRequest(_message.Message):
    __slots__ = ("diatheke_transcribe_request",)
    DIATHEKE_TRANSCRIBE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    diatheke_transcribe_request: _diatheke_pb2.TranscribeRequest
    def __init__(self, diatheke_transcribe_request: _Optional[_Union[_diatheke_pb2.TranscribeRequest, _Mapping]] = ...) -> None: ...

class TranscribeResponse(_message.Message):
    __slots__ = ("diatheke_transcribe_response",)
    DIATHEKE_TRANSCRIBE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    diatheke_transcribe_response: _diatheke_pb2.TranscribeResponse
    def __init__(self, diatheke_transcribe_response: _Optional[_Union[_diatheke_pb2.TranscribeResponse, _Mapping]] = ...) -> None: ...

class GetImageRequest(_message.Message):
    __slots__ = ("relative_path",)
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    relative_path: str
    def __init__(self, relative_path: _Optional[str] = ...) -> None: ...

class GetImageResponse(_message.Message):
    __slots__ = ("file_chunk",)
    FILE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    file_chunk: bytes
    def __init__(self, file_chunk: _Optional[bytes] = ...) -> None: ...

class ListProceduresRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProceduresResponse(_message.Message):
    __slots__ = ("procedures",)
    PROCEDURES_FIELD_NUMBER: _ClassVar[int]
    procedures: _containers.RepeatedCompositeFieldContainer[GetProceduresResponse]
    def __init__(self, procedures: _Optional[_Iterable[_Union[GetProceduresResponse, _Mapping]]] = ...) -> None: ...

class GetProceduresRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProceduresResponse(_message.Message):
    __slots__ = ("id", "name", "procedure_number", "additional_names", "input_conditions", "prerequisites_warning_text", "tasks")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITES_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    procedure_number: str
    additional_names: str
    input_conditions: str
    prerequisites_warning_text: str
    tasks: _containers.RepeatedCompositeFieldContainer[TaskData]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., procedure_number: _Optional[str] = ..., additional_names: _Optional[str] = ..., input_conditions: _Optional[str] = ..., prerequisites_warning_text: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[TaskData, _Mapping]]] = ...) -> None: ...

class InputConditionData(_message.Message):
    __slots__ = ("id", "applicability", "required_conditions", "personnel", "support_equipment", "additional_data")
    ID_FIELD_NUMBER: _ClassVar[int]
    APPLICABILITY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PERSONNEL_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_EQUIPMENT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    applicability: str
    required_conditions: str
    personnel: str
    support_equipment: str
    additional_data: str
    def __init__(self, id: _Optional[str] = ..., applicability: _Optional[str] = ..., required_conditions: _Optional[str] = ..., personnel: _Optional[str] = ..., support_equipment: _Optional[str] = ..., additional_data: _Optional[str] = ...) -> None: ...

class TaskData(_message.Message):
    __slots__ = ("id", "task_name", "task_number", "additional_names", "warning_text", "steps")
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    task_name: str
    task_number: str
    additional_names: str
    warning_text: str
    steps: _containers.RepeatedCompositeFieldContainer[StepData]
    def __init__(self, id: _Optional[str] = ..., task_name: _Optional[str] = ..., task_number: _Optional[str] = ..., additional_names: _Optional[str] = ..., warning_text: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[StepData, _Mapping]]] = ...) -> None: ...

class StepData(_message.Message):
    __slots__ = ("id", "instruction_text", "summary_text", "person", "task_number", "step_number", "image", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STEP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    instruction_text: str
    summary_text: str
    person: str
    task_number: str
    step_number: str
    image: str
    notes: _containers.RepeatedCompositeFieldContainer[Notes]
    def __init__(self, id: _Optional[str] = ..., instruction_text: _Optional[str] = ..., summary_text: _Optional[str] = ..., person: _Optional[str] = ..., task_number: _Optional[str] = ..., step_number: _Optional[str] = ..., image: _Optional[str] = ..., notes: _Optional[_Iterable[_Union[Notes, _Mapping]]] = ...) -> None: ...

class Notes(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class SaveNoteRequest(_message.Message):
    __slots__ = ("text", "step_id")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    step_id: str
    def __init__(self, text: _Optional[str] = ..., step_id: _Optional[str] = ...) -> None: ...

class SaveNoteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetEntityImageRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetEntityImageResponse(_message.Message):
    __slots__ = ("image_data_list",)
    IMAGE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    image_data_list: _containers.RepeatedCompositeFieldContainer[ImageData]
    def __init__(self, image_data_list: _Optional[_Iterable[_Union[ImageData, _Mapping]]] = ...) -> None: ...

class ImageData(_message.Message):
    __slots__ = ("id", "file_path", "caption")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_path: str
    caption: str
    def __init__(self, id: _Optional[str] = ..., file_path: _Optional[str] = ..., caption: _Optional[str] = ...) -> None: ...
