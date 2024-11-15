# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cobaltspeech/bluehenge/v2/bluehenge.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'cobaltspeech/bluehenge/v2/bluehenge.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cobaltspeech.diatheke.v3 import diatheke_pb2 as cobaltspeech_dot_diatheke_dot_v3_dot_diatheke__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cobaltspeech/bluehenge/v2/bluehenge.proto\x12\x19\x63obaltspeech.bluehenge.v2\x1a\'cobaltspeech/diatheke/v3/diatheke.proto\"\x10\n\x0eVersionRequest\"\xfe\x01\n\x0fVersionResponse\x12\x1c\n\tbluehenge\x18\x01 \x01(\tR\tbluehenge\x12\x65\n\x19\x64iatheke_version_response\x18\x02 \x01(\x0b\x32).cobaltspeech.diatheke.v3.VersionResponseR\x17\x64iathekeVersionResponse\x12.\n\x13source_data_version\x18\x03 \x01(\tR\x11sourceDataVersion\x12\x36\n\x17knowledge_graph_version\x18\x04 \x01(\tR\x15knowledgeGraphVersion\"\x81\x01\n\x11ListModelsRequest\x12l\n\x1c\x64iatheke_list_models_request\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.ListModelsRequestR\x19\x64iathekeListModelsRequest\"\x85\x01\n\x12ListModelsResponse\x12o\n\x1d\x64iatheke_list_models_response\x18\x01 \x01(\x0b\x32,.cobaltspeech.diatheke.v3.ListModelsResponseR\x1a\x64iathekeListModelsResponse\"\x8d\x01\n\x14\x43reateSessionRequest\x12u\n\x1f\x64iatheke_create_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.CreateSessionRequestR\x1c\x64iathekeCreateSessionRequest\"\x91\x01\n\x15\x43reateSessionResponse\x12x\n diatheke_create_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.CreateSessionResponseR\x1d\x64iathekeCreateSessionResponse\"\x8d\x01\n\x14\x44\x65leteSessionRequest\x12u\n\x1f\x64iatheke_delete_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.DeleteSessionRequestR\x1c\x64iathekeDeleteSessionRequest\"\x91\x01\n\x15\x44\x65leteSessionResponse\x12x\n diatheke_delete_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.DeleteSessionResponseR\x1d\x64iathekeDeleteSessionResponse\"\x8d\x01\n\x14UpdateSessionRequest\x12u\n\x1f\x64iatheke_update_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.UpdateSessionRequestR\x1c\x64iathekeUpdateSessionRequest\"\x91\x01\n\x15UpdateSessionResponse\x12x\n diatheke_update_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.UpdateSessionResponseR\x1d\x64iathekeUpdateSessionResponse\"}\n\x10StreamASRRequest\x12i\n\x1b\x64iatheke_stream_asr_request\x18\x01 \x01(\x0b\x32*.cobaltspeech.diatheke.v3.StreamASRRequestR\x18\x64iathekeStreamAsrRequest\"\x81\x01\n\x11StreamASRResponse\x12l\n\x1c\x64iatheke_stream_asr_response\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.StreamASRResponseR\x19\x64iathekeStreamAsrResponse\"}\n\x10StreamTTSRequest\x12i\n\x1b\x64iatheke_stream_tts_request\x18\x01 \x01(\x0b\x32*.cobaltspeech.diatheke.v3.StreamTTSRequestR\x18\x64iathekeStreamTtsRequest\")\n\x11StreamTTSResponse\x12\x14\n\x05\x61udio\x18\x01 \x01(\x0cR\x05\x61udio\"\x80\x01\n\x11TranscribeRequest\x12k\n\x1b\x64iatheke_transcribe_request\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.TranscribeRequestR\x19\x64iathekeTranscribeRequest\"\x84\x01\n\x12TranscribeResponse\x12n\n\x1c\x64iatheke_transcribe_response\x18\x01 \x01(\x0b\x32,.cobaltspeech.diatheke.v3.TranscribeResponseR\x1a\x64iathekeTranscribeResponse\"\x17\n\x15ListProceduresRequest\"b\n\x16ListProceduresResponse\x12H\n\nprocedures\x18\x01 \x03(\x0b\x32(.cobaltspeech.bluehenge.v2.ProcedureLiteR\nprocedures\"\x12\n\x10ListTreesRequest\"N\n\x11ListTreesResponse\x12\x39\n\x05trees\x18\x01 \x03(\x0b\x32#.cobaltspeech.bluehenge.v2.TreeLiteR\x05trees\")\n\x13GetProcedureRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"Z\n\x14GetProcedureResponse\x12\x42\n\tprocedure\x18\x01 \x01(\x0b\x32$.cobaltspeech.bluehenge.v2.ProcedureR\tprocedure\" \n\x0eGetTaskRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"F\n\x0fGetTaskResponse\x12\x33\n\x04task\x18\x01 \x01(\x0b\x32\x1f.cobaltspeech.bluehenge.v2.TaskR\x04task\"$\n\x0eGetTreeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"F\n\x0fGetTreeResponse\x12\x33\n\x04tree\x18\x01 \x01(\x0b\x32\x1f.cobaltspeech.bluehenge.v2.TreeR\x04tree\"\xc0\x01\n\rProcedureLite\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12%\n\x0eprocedure_name\x18\x02 \x01(\tR\rprocedureName\x12\x12\n\x04page\x18\x03 \x01(\tR\x04page\x12)\n\x10procedure_number\x18\x04 \x01(\tR\x0fprocedureNumber\x12\x39\n\x05tasks\x18\x05 \x03(\x0b\x32#.cobaltspeech.bluehenge.v2.TaskLiteR\x05tasks\"X\n\x08TaskLite\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\ttask_name\x18\x02 \x01(\tR\x08taskName\x12\x1f\n\x0btask_number\x18\x03 \x01(\tR\ntaskNumber\"X\n\x08TreeLite\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\ttree_name\x18\x02 \x01(\tR\x08treeName\x12\x1f\n\x0btree_number\x18\x03 \x01(\tR\ntreeNumber\"\xfa\x01\n\tProcedure\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12)\n\x10procedure_number\x18\x03 \x01(\tR\x0fprocedureNumber\x12)\n\x10\x61\x64\x64itional_names\x18\x04 \x03(\tR\x0f\x61\x64\x64itionalNames\x12<\n\x1aprerequisites_warning_text\x18\x05 \x01(\tR\x18prerequisitesWarningText\x12\x35\n\x05tasks\x18\x06 \x03(\x0b\x32\x1f.cobaltspeech.bluehenge.v2.TaskR\x05tasks\"\xdd\x01\n\x04Task\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\ttask_name\x18\x02 \x01(\tR\x08taskName\x12\x1f\n\x0btask_number\x18\x03 \x01(\tR\ntaskNumber\x12)\n\x10\x61\x64\x64itional_names\x18\x04 \x03(\tR\x0f\x61\x64\x64itionalNames\x12!\n\x0cwarning_text\x18\x05 \x01(\tR\x0bwarningText\x12\x39\n\x05steps\x18\x06 \x03(\x0b\x32#.cobaltspeech.bluehenge.v2.StepDataR\x05steps\"\xdc\x02\n\x08StepData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x10instruction_text\x18\x02 \x01(\tR\x0finstructionText\x12!\n\x0csummary_text\x18\x03 \x01(\tR\x0bsummaryText\x12\x16\n\x06person\x18\x04 \x01(\tR\x06person\x12\x1f\n\x0btask_number\x18\x05 \x01(\tR\ntaskNumber\x12\x1f\n\x0bstep_number\x18\x06 \x01(\tR\nstepNumber\x12\x12\n\x04page\x18\x07 \x01(\tR\x04page\x12!\n\x0csegment_type\x18\x08 \x01(\tR\x0bsegmentType\x12\x14\n\x05image\x18\t \x03(\tR\x05image\x12\x14\n\x05parts\x18\x0b \x03(\tR\x05parts\x12\x35\n\x05notes\x18\n \x03(\x0b\x32\x1f.cobaltspeech.bluehenge.v2.NoteR\x05notes\"\xf8\x01\n\x04Tree\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\ttree_name\x18\x02 \x01(\tR\x08treeName\x12\x1f\n\x0btree_number\x18\x03 \x01(\tR\ntreeNumber\x12)\n\x10\x61\x64\x64itional_names\x18\x04 \x03(\tR\x0f\x61\x64\x64itionalNames\x12<\n\x1aprerequisites_warning_text\x18\x05 \x01(\tR\x18prerequisitesWarningText\x12\x39\n\x05nodes\x18\x06 \x03(\x0b\x32#.cobaltspeech.bluehenge.v2.TreeNodeR\x05nodes\"\x8c\x02\n\x08TreeNode\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nnode_index\x18\x02 \x01(\tR\tnodeIndex\x12)\n\x10instruction_text\x18\x03 \x01(\tR\x0finstructionText\x12\x43\n\x07options\x18\x04 \x03(\x0b\x32).cobaltspeech.bluehenge.v2.TroubleOptionsR\x07options\x12\x14\n\x05image\x18\x05 \x03(\tR\x05image\x12\x14\n\x05parts\x18\x06 \x03(\tR\x05parts\x12\x35\n\x05notes\x18\x07 \x03(\x0b\x32\x1f.cobaltspeech.bluehenge.v2.NoteR\x05notes\"P\n\x0eTroubleOptions\x12\x1c\n\tcondition\x18\x01 \x01(\tR\tcondition\x12 \n\x0b\x64\x65stination\x18\x02 \x01(\tR\x0b\x64\x65stination\"\x1a\n\x04Note\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\">\n\x0fSaveNoteRequest\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x17\n\x07step_id\x18\x02 \x01(\tR\x06stepId\"\x12\n\x10SaveNoteResponse\"\x15\n\x13ListEntitiesRequest\"U\n\x14ListEntitiesResponse\x12=\n\x08\x65ntities\x18\x01 \x03(\x0b\x32!.cobaltspeech.bluehenge.v2.EntityR\x08\x65ntities\"R\n GetExtractionRelationshipRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08relation\x18\x02 \x01(\tR\x08relation\"j\n!GetExtractionRelationshipResponse\x12\x45\n\nextraction\x18\x01 \x01(\x0b\x32%.cobaltspeech.bluehenge.v2.ExtractionR\nextraction\"\xd5\x01\n\nExtraction\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12;\n\x07subject\x18\x02 \x01(\x0b\x32!.cobaltspeech.bluehenge.v2.EntityR\x07subject\x12\x39\n\x06object\x18\x03 \x01(\x0b\x32!.cobaltspeech.bluehenge.v2.EntityR\x06object\x12?\n\x08relation\x18\x04 \x01(\x0b\x32#.cobaltspeech.bluehenge.v2.RelationR\x08relation\"&\n\x10GetEntityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"N\n\x11GetEntityResponse\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.cobaltspeech.bluehenge.v2.EntityR\x06\x65ntity\"\xbe\x01\n\x06\x45ntity\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12>\n\x08mentions\x18\x02 \x01(\x0b\x32\".cobaltspeech.bluehenge.v2.MentionR\x08mentions\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08location\x18\x05 \x01(\tR\x08location\x12\x12\n\x04page\x18\x06 \x01(\tR\x04page\"Z\n\x08Relation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12>\n\x08mentions\x18\x02 \x01(\x0b\x32\".cobaltspeech.bluehenge.v2.MentionR\x08mentions\"\x1d\n\x07Mention\x12\x12\n\x04text\x18\x01 \x03(\tR\x04text\"+\n\x19GetEntityImageDataRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"j\n\x1aGetEntityImageDataResponse\x12L\n\x0fimage_data_list\x18\x01 \x03(\x0b\x32$.cobaltspeech.bluehenge.v2.ImageDataR\rimageDataList\"R\n\tImageData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\thttp_path\x18\x02 \x01(\tR\x08httpPath\x12\x18\n\x07\x63\x61ption\x18\x03 \x01(\tR\x07\x63\x61ption2\x91\x10\n\x10\x42luehengeService\x12\x62\n\x07Version\x12).cobaltspeech.bluehenge.v2.VersionRequest\x1a*.cobaltspeech.bluehenge.v2.VersionResponse\"\x00\x12k\n\nListModels\x12,.cobaltspeech.bluehenge.v2.ListModelsRequest\x1a-.cobaltspeech.bluehenge.v2.ListModelsResponse\"\x00\x12t\n\rCreateSession\x12/.cobaltspeech.bluehenge.v2.CreateSessionRequest\x1a\x30.cobaltspeech.bluehenge.v2.CreateSessionResponse\"\x00\x12t\n\rDeleteSession\x12/.cobaltspeech.bluehenge.v2.DeleteSessionRequest\x1a\x30.cobaltspeech.bluehenge.v2.DeleteSessionResponse\"\x00\x12t\n\rUpdateSession\x12/.cobaltspeech.bluehenge.v2.UpdateSessionRequest\x1a\x30.cobaltspeech.bluehenge.v2.UpdateSessionResponse\"\x00\x12j\n\tStreamASR\x12+.cobaltspeech.bluehenge.v2.StreamASRRequest\x1a,.cobaltspeech.bluehenge.v2.StreamASRResponse\"\x00(\x01\x12j\n\tStreamTTS\x12+.cobaltspeech.bluehenge.v2.StreamTTSRequest\x1a,.cobaltspeech.bluehenge.v2.StreamTTSResponse\"\x00\x30\x01\x12o\n\nTranscribe\x12,.cobaltspeech.bluehenge.v2.TranscribeRequest\x1a-.cobaltspeech.bluehenge.v2.TranscribeResponse\"\x00(\x01\x30\x01\x12w\n\x0eListProcedures\x12\x30.cobaltspeech.bluehenge.v2.ListProceduresRequest\x1a\x31.cobaltspeech.bluehenge.v2.ListProceduresResponse\"\x00\x12h\n\tListTrees\x12+.cobaltspeech.bluehenge.v2.ListTreesRequest\x1a,.cobaltspeech.bluehenge.v2.ListTreesResponse\"\x00\x12q\n\x0cListEntities\x12..cobaltspeech.bluehenge.v2.ListEntitiesRequest\x1a/.cobaltspeech.bluehenge.v2.ListEntitiesResponse\"\x00\x12q\n\x0cGetProcedure\x12..cobaltspeech.bluehenge.v2.GetProcedureRequest\x1a/.cobaltspeech.bluehenge.v2.GetProcedureResponse\"\x00\x12\x62\n\x07GetTask\x12).cobaltspeech.bluehenge.v2.GetTaskRequest\x1a*.cobaltspeech.bluehenge.v2.GetTaskResponse\"\x00\x12\x62\n\x07GetTree\x12).cobaltspeech.bluehenge.v2.GetTreeRequest\x1a*.cobaltspeech.bluehenge.v2.GetTreeResponse\"\x00\x12\x65\n\x08SaveNote\x12*.cobaltspeech.bluehenge.v2.SaveNoteRequest\x1a+.cobaltspeech.bluehenge.v2.SaveNoteResponse\"\x00\x12\x98\x01\n\x19GetExtractionRelationship\x12;.cobaltspeech.bluehenge.v2.GetExtractionRelationshipRequest\x1a<.cobaltspeech.bluehenge.v2.GetExtractionRelationshipResponse\"\x00\x12h\n\tGetEntity\x12+.cobaltspeech.bluehenge.v2.GetEntityRequest\x1a,.cobaltspeech.bluehenge.v2.GetEntityResponse\"\x00\x12\x83\x01\n\x12GetEntityImageData\x12\x34.cobaltspeech.bluehenge.v2.GetEntityImageDataRequest\x1a\x35.cobaltspeech.bluehenge.v2.GetEntityImageDataResponse\"\x00\x42\x80\x02\n\x1d\x63om.cobaltspeech.bluehenge.v2B\x0e\x42luehengeProtoP\x01ZIgithub.com/cobaltspeech/go-genproto/cobaltspeech/bluehenge/v2;bluehengev2\xa2\x02\x03\x43\x42X\xaa\x02\x19\x43obaltspeech.Bluehenge.V2\xca\x02\x19\x43obaltspeech\\Bluehenge\\V2\xe2\x02%Cobaltspeech\\Bluehenge\\V2\\GPBMetadata\xea\x02\x1b\x43obaltspeech::Bluehenge::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.bluehenge.v2.bluehenge_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.cobaltspeech.bluehenge.v2B\016BluehengeProtoP\001ZIgithub.com/cobaltspeech/go-genproto/cobaltspeech/bluehenge/v2;bluehengev2\242\002\003CBX\252\002\031Cobaltspeech.Bluehenge.V2\312\002\031Cobaltspeech\\Bluehenge\\V2\342\002%Cobaltspeech\\Bluehenge\\V2\\GPBMetadata\352\002\033Cobaltspeech::Bluehenge::V2'
  _globals['_VERSIONREQUEST']._serialized_start=113
  _globals['_VERSIONREQUEST']._serialized_end=129
  _globals['_VERSIONRESPONSE']._serialized_start=132
  _globals['_VERSIONRESPONSE']._serialized_end=386
  _globals['_LISTMODELSREQUEST']._serialized_start=389
  _globals['_LISTMODELSREQUEST']._serialized_end=518
  _globals['_LISTMODELSRESPONSE']._serialized_start=521
  _globals['_LISTMODELSRESPONSE']._serialized_end=654
  _globals['_CREATESESSIONREQUEST']._serialized_start=657
  _globals['_CREATESESSIONREQUEST']._serialized_end=798
  _globals['_CREATESESSIONRESPONSE']._serialized_start=801
  _globals['_CREATESESSIONRESPONSE']._serialized_end=946
  _globals['_DELETESESSIONREQUEST']._serialized_start=949
  _globals['_DELETESESSIONREQUEST']._serialized_end=1090
  _globals['_DELETESESSIONRESPONSE']._serialized_start=1093
  _globals['_DELETESESSIONRESPONSE']._serialized_end=1238
  _globals['_UPDATESESSIONREQUEST']._serialized_start=1241
  _globals['_UPDATESESSIONREQUEST']._serialized_end=1382
  _globals['_UPDATESESSIONRESPONSE']._serialized_start=1385
  _globals['_UPDATESESSIONRESPONSE']._serialized_end=1530
  _globals['_STREAMASRREQUEST']._serialized_start=1532
  _globals['_STREAMASRREQUEST']._serialized_end=1657
  _globals['_STREAMASRRESPONSE']._serialized_start=1660
  _globals['_STREAMASRRESPONSE']._serialized_end=1789
  _globals['_STREAMTTSREQUEST']._serialized_start=1791
  _globals['_STREAMTTSREQUEST']._serialized_end=1916
  _globals['_STREAMTTSRESPONSE']._serialized_start=1918
  _globals['_STREAMTTSRESPONSE']._serialized_end=1959
  _globals['_TRANSCRIBEREQUEST']._serialized_start=1962
  _globals['_TRANSCRIBEREQUEST']._serialized_end=2090
  _globals['_TRANSCRIBERESPONSE']._serialized_start=2093
  _globals['_TRANSCRIBERESPONSE']._serialized_end=2225
  _globals['_LISTPROCEDURESREQUEST']._serialized_start=2227
  _globals['_LISTPROCEDURESREQUEST']._serialized_end=2250
  _globals['_LISTPROCEDURESRESPONSE']._serialized_start=2252
  _globals['_LISTPROCEDURESRESPONSE']._serialized_end=2350
  _globals['_LISTTREESREQUEST']._serialized_start=2352
  _globals['_LISTTREESREQUEST']._serialized_end=2370
  _globals['_LISTTREESRESPONSE']._serialized_start=2372
  _globals['_LISTTREESRESPONSE']._serialized_end=2450
  _globals['_GETPROCEDUREREQUEST']._serialized_start=2452
  _globals['_GETPROCEDUREREQUEST']._serialized_end=2493
  _globals['_GETPROCEDURERESPONSE']._serialized_start=2495
  _globals['_GETPROCEDURERESPONSE']._serialized_end=2585
  _globals['_GETTASKREQUEST']._serialized_start=2587
  _globals['_GETTASKREQUEST']._serialized_end=2619
  _globals['_GETTASKRESPONSE']._serialized_start=2621
  _globals['_GETTASKRESPONSE']._serialized_end=2691
  _globals['_GETTREEREQUEST']._serialized_start=2693
  _globals['_GETTREEREQUEST']._serialized_end=2729
  _globals['_GETTREERESPONSE']._serialized_start=2731
  _globals['_GETTREERESPONSE']._serialized_end=2801
  _globals['_PROCEDURELITE']._serialized_start=2804
  _globals['_PROCEDURELITE']._serialized_end=2996
  _globals['_TASKLITE']._serialized_start=2998
  _globals['_TASKLITE']._serialized_end=3086
  _globals['_TREELITE']._serialized_start=3088
  _globals['_TREELITE']._serialized_end=3176
  _globals['_PROCEDURE']._serialized_start=3179
  _globals['_PROCEDURE']._serialized_end=3429
  _globals['_TASK']._serialized_start=3432
  _globals['_TASK']._serialized_end=3653
  _globals['_STEPDATA']._serialized_start=3656
  _globals['_STEPDATA']._serialized_end=4004
  _globals['_TREE']._serialized_start=4007
  _globals['_TREE']._serialized_end=4255
  _globals['_TREENODE']._serialized_start=4258
  _globals['_TREENODE']._serialized_end=4526
  _globals['_TROUBLEOPTIONS']._serialized_start=4528
  _globals['_TROUBLEOPTIONS']._serialized_end=4608
  _globals['_NOTE']._serialized_start=4610
  _globals['_NOTE']._serialized_end=4636
  _globals['_SAVENOTEREQUEST']._serialized_start=4638
  _globals['_SAVENOTEREQUEST']._serialized_end=4700
  _globals['_SAVENOTERESPONSE']._serialized_start=4702
  _globals['_SAVENOTERESPONSE']._serialized_end=4720
  _globals['_LISTENTITIESREQUEST']._serialized_start=4722
  _globals['_LISTENTITIESREQUEST']._serialized_end=4743
  _globals['_LISTENTITIESRESPONSE']._serialized_start=4745
  _globals['_LISTENTITIESRESPONSE']._serialized_end=4830
  _globals['_GETEXTRACTIONRELATIONSHIPREQUEST']._serialized_start=4832
  _globals['_GETEXTRACTIONRELATIONSHIPREQUEST']._serialized_end=4914
  _globals['_GETEXTRACTIONRELATIONSHIPRESPONSE']._serialized_start=4916
  _globals['_GETEXTRACTIONRELATIONSHIPRESPONSE']._serialized_end=5022
  _globals['_EXTRACTION']._serialized_start=5025
  _globals['_EXTRACTION']._serialized_end=5238
  _globals['_GETENTITYREQUEST']._serialized_start=5240
  _globals['_GETENTITYREQUEST']._serialized_end=5278
  _globals['_GETENTITYRESPONSE']._serialized_start=5280
  _globals['_GETENTITYRESPONSE']._serialized_end=5358
  _globals['_ENTITY']._serialized_start=5361
  _globals['_ENTITY']._serialized_end=5551
  _globals['_RELATION']._serialized_start=5553
  _globals['_RELATION']._serialized_end=5643
  _globals['_MENTION']._serialized_start=5645
  _globals['_MENTION']._serialized_end=5674
  _globals['_GETENTITYIMAGEDATAREQUEST']._serialized_start=5676
  _globals['_GETENTITYIMAGEDATAREQUEST']._serialized_end=5719
  _globals['_GETENTITYIMAGEDATARESPONSE']._serialized_start=5721
  _globals['_GETENTITYIMAGEDATARESPONSE']._serialized_end=5827
  _globals['_IMAGEDATA']._serialized_start=5829
  _globals['_IMAGEDATA']._serialized_end=5911
  _globals['_BLUEHENGESERVICE']._serialized_start=5914
  _globals['_BLUEHENGESERVICE']._serialized_end=7979
# @@protoc_insertion_point(module_scope)
