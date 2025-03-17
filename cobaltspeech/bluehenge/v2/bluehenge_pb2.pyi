from cobaltspeech.diatheke.v3 import diatheke_pb2 as _diatheke_pb2
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
    __slots__ = ("bluehenge", "diatheke_version_response", "source_data_version", "knowledge_graph_version")
    BLUEHENGE_FIELD_NUMBER: _ClassVar[int]
    DIATHEKE_VERSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_GRAPH_VERSION_FIELD_NUMBER: _ClassVar[int]
    bluehenge: str
    diatheke_version_response: _diatheke_pb2.VersionResponse
    source_data_version: str
    knowledge_graph_version: str
    def __init__(self, bluehenge: _Optional[str] = ..., diatheke_version_response: _Optional[_Union[_diatheke_pb2.VersionResponse, _Mapping]] = ..., source_data_version: _Optional[str] = ..., knowledge_graph_version: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("audio",)
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    def __init__(self, audio: _Optional[bytes] = ...) -> None: ...

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

class ListProceduresRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProceduresResponse(_message.Message):
    __slots__ = ("procedures",)
    PROCEDURES_FIELD_NUMBER: _ClassVar[int]
    procedures: _containers.RepeatedCompositeFieldContainer[ProcedureLite]
    def __init__(self, procedures: _Optional[_Iterable[_Union[ProcedureLite, _Mapping]]] = ...) -> None: ...

class ListTreesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTreesResponse(_message.Message):
    __slots__ = ("trees",)
    TREES_FIELD_NUMBER: _ClassVar[int]
    trees: _containers.RepeatedCompositeFieldContainer[TreeLite]
    def __init__(self, trees: _Optional[_Iterable[_Union[TreeLite, _Mapping]]] = ...) -> None: ...

class GetProcedureRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetProcedureResponse(_message.Message):
    __slots__ = ("procedure",)
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    procedure: Procedure
    def __init__(self, procedure: _Optional[_Union[Procedure, _Mapping]] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class GetTreeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTreeResponse(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: Tree
    def __init__(self, tree: _Optional[_Union[Tree, _Mapping]] = ...) -> None: ...

class ProcedureLite(_message.Message):
    __slots__ = ("id", "procedure_name", "page", "procedure_number", "tasks")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    procedure_name: str
    page: str
    procedure_number: str
    tasks: _containers.RepeatedCompositeFieldContainer[TaskLite]
    def __init__(self, id: _Optional[str] = ..., procedure_name: _Optional[str] = ..., page: _Optional[str] = ..., procedure_number: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[TaskLite, _Mapping]]] = ...) -> None: ...

class TaskLite(_message.Message):
    __slots__ = ("id", "task_name", "task_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    task_name: str
    task_number: str
    def __init__(self, id: _Optional[str] = ..., task_name: _Optional[str] = ..., task_number: _Optional[str] = ...) -> None: ...

class TreeLite(_message.Message):
    __slots__ = ("id", "tree_name", "tree_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    TREE_NAME_FIELD_NUMBER: _ClassVar[int]
    TREE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    tree_name: str
    tree_number: str
    def __init__(self, id: _Optional[str] = ..., tree_name: _Optional[str] = ..., tree_number: _Optional[str] = ...) -> None: ...

class Procedure(_message.Message):
    __slots__ = ("id", "name", "procedure_number", "additional_names", "prerequisites_warning_text", "tasks")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITES_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    procedure_number: str
    additional_names: _containers.RepeatedScalarFieldContainer[str]
    prerequisites_warning_text: str
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., procedure_number: _Optional[str] = ..., additional_names: _Optional[_Iterable[str]] = ..., prerequisites_warning_text: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class Task(_message.Message):
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
    additional_names: _containers.RepeatedScalarFieldContainer[str]
    warning_text: str
    steps: _containers.RepeatedCompositeFieldContainer[StepData]
    def __init__(self, id: _Optional[str] = ..., task_name: _Optional[str] = ..., task_number: _Optional[str] = ..., additional_names: _Optional[_Iterable[str]] = ..., warning_text: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[StepData, _Mapping]]] = ...) -> None: ...

class StepData(_message.Message):
    __slots__ = ("id", "instruction_text", "summary_text", "person", "task_number", "step_number", "page", "segment_type", "image", "parts", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STEP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    instruction_text: str
    summary_text: str
    person: str
    task_number: str
    step_number: str
    page: str
    segment_type: str
    image: _containers.RepeatedScalarFieldContainer[str]
    parts: _containers.RepeatedScalarFieldContainer[str]
    notes: _containers.RepeatedCompositeFieldContainer[Note]
    def __init__(self, id: _Optional[str] = ..., instruction_text: _Optional[str] = ..., summary_text: _Optional[str] = ..., person: _Optional[str] = ..., task_number: _Optional[str] = ..., step_number: _Optional[str] = ..., page: _Optional[str] = ..., segment_type: _Optional[str] = ..., image: _Optional[_Iterable[str]] = ..., parts: _Optional[_Iterable[str]] = ..., notes: _Optional[_Iterable[_Union[Note, _Mapping]]] = ...) -> None: ...

class Tree(_message.Message):
    __slots__ = ("id", "tree_name", "tree_number", "additional_names", "prerequisites_warning_text", "nodes")
    ID_FIELD_NUMBER: _ClassVar[int]
    TREE_NAME_FIELD_NUMBER: _ClassVar[int]
    TREE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITES_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    id: str
    tree_name: str
    tree_number: str
    additional_names: _containers.RepeatedScalarFieldContainer[str]
    prerequisites_warning_text: str
    nodes: _containers.RepeatedCompositeFieldContainer[TreeNode]
    def __init__(self, id: _Optional[str] = ..., tree_name: _Optional[str] = ..., tree_number: _Optional[str] = ..., additional_names: _Optional[_Iterable[str]] = ..., prerequisites_warning_text: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[TreeNode, _Mapping]]] = ...) -> None: ...

class TreeNode(_message.Message):
    __slots__ = ("id", "node_index", "instruction_text", "options", "image", "parts", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    node_index: str
    instruction_text: str
    options: _containers.RepeatedCompositeFieldContainer[TroubleOptions]
    image: _containers.RepeatedScalarFieldContainer[str]
    parts: _containers.RepeatedScalarFieldContainer[str]
    notes: _containers.RepeatedCompositeFieldContainer[Note]
    def __init__(self, id: _Optional[str] = ..., node_index: _Optional[str] = ..., instruction_text: _Optional[str] = ..., options: _Optional[_Iterable[_Union[TroubleOptions, _Mapping]]] = ..., image: _Optional[_Iterable[str]] = ..., parts: _Optional[_Iterable[str]] = ..., notes: _Optional[_Iterable[_Union[Note, _Mapping]]] = ...) -> None: ...

class TroubleOptions(_message.Message):
    __slots__ = ("condition", "destination")
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    condition: str
    destination: str
    def __init__(self, condition: _Optional[str] = ..., destination: _Optional[str] = ...) -> None: ...

class Note(_message.Message):
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

class ListEntitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEntitiesResponse(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class GetExtractionRelationshipRequest(_message.Message):
    __slots__ = ("name", "relation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    relation: str
    def __init__(self, name: _Optional[str] = ..., relation: _Optional[str] = ...) -> None: ...

class GetExtractionRelationshipResponse(_message.Message):
    __slots__ = ("extraction",)
    EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    extraction: Extraction
    def __init__(self, extraction: _Optional[_Union[Extraction, _Mapping]] = ...) -> None: ...

class Extraction(_message.Message):
    __slots__ = ("id", "subject", "object", "relation")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    subject: Entity
    object: Entity
    relation: Relation
    def __init__(self, id: _Optional[str] = ..., subject: _Optional[_Union[Entity, _Mapping]] = ..., object: _Optional[_Union[Entity, _Mapping]] = ..., relation: _Optional[_Union[Relation, _Mapping]] = ...) -> None: ...

class GetEntityRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEntityResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("id", "mentions", "name", "description", "location", "page")
    ID_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    mentions: Mention
    name: str
    description: str
    location: str
    page: str
    def __init__(self, id: _Optional[str] = ..., mentions: _Optional[_Union[Mention, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., location: _Optional[str] = ..., page: _Optional[str] = ...) -> None: ...

class Relation(_message.Message):
    __slots__ = ("id", "mentions")
    ID_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    mentions: Mention
    def __init__(self, id: _Optional[str] = ..., mentions: _Optional[_Union[Mention, _Mapping]] = ...) -> None: ...

class Mention(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEntityImageDataRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetEntityImageDataResponse(_message.Message):
    __slots__ = ("image_data_list",)
    IMAGE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    image_data_list: _containers.RepeatedCompositeFieldContainer[ImageData]
    def __init__(self, image_data_list: _Optional[_Iterable[_Union[ImageData, _Mapping]]] = ...) -> None: ...

class ImageData(_message.Message):
    __slots__ = ("id", "http_path", "caption")
    ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_PATH_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    http_path: str
    caption: str
    def __init__(self, id: _Optional[str] = ..., http_path: _Optional[str] = ..., caption: _Optional[str] = ...) -> None: ...
