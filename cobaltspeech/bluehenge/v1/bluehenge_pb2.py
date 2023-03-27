# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/bluehenge/v1/bluehenge.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cobaltspeech.diatheke.v3 import diatheke_pb2 as cobaltspeech_dot_diatheke_dot_v3_dot_diatheke__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cobaltspeech/bluehenge/v1/bluehenge.proto\x12\x19\x63obaltspeech.bluehenge.v1\x1a\'cobaltspeech/diatheke/v3/diatheke.proto\"\x10\n\x0eVersionRequest\"\x96\x01\n\x0fVersionResponse\x12\x1c\n\tbluehenge\x18\x01 \x01(\tR\tbluehenge\x12\x65\n\x19\x64iatheke_version_response\x18\x02 \x01(\x0b\x32).cobaltspeech.diatheke.v3.VersionResponseR\x17\x64iathekeVersionResponse\"\x81\x01\n\x11ListModelsRequest\x12l\n\x1c\x64iatheke_list_models_request\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.ListModelsRequestR\x19\x64iathekeListModelsRequest\"\x85\x01\n\x12ListModelsResponse\x12o\n\x1d\x64iatheke_list_models_response\x18\x01 \x01(\x0b\x32,.cobaltspeech.diatheke.v3.ListModelsResponseR\x1a\x64iathekeListModelsResponse\"\x8d\x01\n\x14\x43reateSessionRequest\x12u\n\x1f\x64iatheke_create_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.CreateSessionRequestR\x1c\x64iathekeCreateSessionRequest\"\x91\x01\n\x15\x43reateSessionResponse\x12x\n diatheke_create_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.CreateSessionResponseR\x1d\x64iathekeCreateSessionResponse\"\x8d\x01\n\x14\x44\x65leteSessionRequest\x12u\n\x1f\x64iatheke_delete_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.DeleteSessionRequestR\x1c\x64iathekeDeleteSessionRequest\"\x91\x01\n\x15\x44\x65leteSessionResponse\x12x\n diatheke_delete_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.DeleteSessionResponseR\x1d\x64iathekeDeleteSessionResponse\"\x8d\x01\n\x14UpdateSessionRequest\x12u\n\x1f\x64iatheke_update_session_request\x18\x01 \x01(\x0b\x32..cobaltspeech.diatheke.v3.UpdateSessionRequestR\x1c\x64iathekeUpdateSessionRequest\"\x91\x01\n\x15UpdateSessionResponse\x12x\n diatheke_update_session_response\x18\x01 \x01(\x0b\x32/.cobaltspeech.diatheke.v3.UpdateSessionResponseR\x1d\x64iathekeUpdateSessionResponse\"}\n\x10StreamASRRequest\x12i\n\x1b\x64iatheke_stream_asr_request\x18\x01 \x01(\x0b\x32*.cobaltspeech.diatheke.v3.StreamASRRequestR\x18\x64iathekeStreamAsrRequest\"\x81\x01\n\x11StreamASRResponse\x12l\n\x1c\x64iatheke_stream_asr_response\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.StreamASRResponseR\x19\x64iathekeStreamAsrResponse\"}\n\x10StreamTTSRequest\x12i\n\x1b\x64iatheke_stream_tts_request\x18\x01 \x01(\x0b\x32*.cobaltspeech.diatheke.v3.StreamTTSRequestR\x18\x64iathekeStreamTtsRequest\"\x81\x01\n\x11StreamTTSResponse\x12l\n\x1c\x64iatheke_stream_tts_response\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.StreamTTSResponseR\x19\x64iathekeStreamTtsResponse\"\x80\x01\n\x11TranscribeRequest\x12k\n\x1b\x64iatheke_transcribe_request\x18\x01 \x01(\x0b\x32+.cobaltspeech.diatheke.v3.TranscribeRequestR\x19\x64iathekeTranscribeRequest\"\x84\x01\n\x12TranscribeResponse\x12n\n\x1c\x64iatheke_transcribe_response\x18\x01 \x01(\x0b\x32,.cobaltspeech.diatheke.v3.TranscribeResponseR\x1a\x64iathekeTranscribeResponse\"6\n\x0fGetImageRequest\x12#\n\rrelative_path\x18\x01 \x01(\tR\x0crelativePath\"1\n\x10GetImageResponse\x12\x1d\n\nfile_chunk\x18\x01 \x01(\x0cR\tfileChunk\"\x17\n\x15ListProceduresRequest\"j\n\x16ListProceduresResponse\x12P\n\nprocedures\x18\x01 \x03(\x0b\x32\x30.cobaltspeech.bluehenge.v1.GetProceduresResponseR\nprocedures\"&\n\x14GetProceduresRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\xb5\x02\n\x15GetProceduresResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12)\n\x10procedure_number\x18\x03 \x01(\tR\x0fprocedureNumber\x12)\n\x10\x61\x64\x64itional_names\x18\x04 \x01(\tR\x0f\x61\x64\x64itionalNames\x12)\n\x10input_conditions\x18\x05 \x01(\tR\x0finputConditions\x12<\n\x1aprerequisites_warning_text\x18\x06 \x01(\tR\x18prerequisitesWarningText\x12\x39\n\x05tasks\x18\x07 \x03(\x0b\x32#.cobaltspeech.bluehenge.v1.TaskDataR\x05tasks\"\xef\x01\n\x12InputConditionData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12$\n\rapplicability\x18\x02 \x01(\tR\rapplicability\x12/\n\x13required_conditions\x18\x03 \x01(\tR\x12requiredConditions\x12\x1c\n\tpersonnel\x18\x04 \x01(\tR\tpersonnel\x12+\n\x11support_equipment\x18\x05 \x01(\tR\x10supportEquipment\x12\'\n\x0f\x61\x64\x64itional_data\x18\x06 \x01(\tR\x0e\x61\x64\x64itionalData\"\xe1\x01\n\x08TaskData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\ttask_name\x18\x02 \x01(\tR\x08taskName\x12\x1f\n\x0btask_number\x18\x03 \x01(\tR\ntaskNumber\x12)\n\x10\x61\x64\x64itional_names\x18\x04 \x01(\tR\x0f\x61\x64\x64itionalNames\x12!\n\x0cwarning_text\x18\x05 \x01(\tR\x0bwarningText\x12\x39\n\x05steps\x18\x06 \x03(\x0b\x32#.cobaltspeech.bluehenge.v1.StepDataR\x05steps\"\x90\x02\n\x08StepData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x10instruction_text\x18\x02 \x01(\tR\x0finstructionText\x12!\n\x0csummary_text\x18\x03 \x01(\tR\x0bsummaryText\x12\x16\n\x06person\x18\x04 \x01(\tR\x06person\x12\x1f\n\x0btask_number\x18\x05 \x01(\tR\ntaskNumber\x12\x1f\n\x0bstep_number\x18\x06 \x01(\tR\nstepNumber\x12\x14\n\x05image\x18\x07 \x01(\tR\x05image\x12\x36\n\x05notes\x18\x08 \x03(\x0b\x32 .cobaltspeech.bluehenge.v1.NotesR\x05notes\"\x1b\n\x05Notes\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\">\n\x0fSaveNoteRequest\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x17\n\x07step_id\x18\x02 \x01(\tR\x06stepId\"\x12\n\x10SaveNoteResponse\"\'\n\x15GetEntityImageRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"f\n\x16GetEntityImageResponse\x12L\n\x0fimage_data_list\x18\x01 \x03(\x0b\x32$.cobaltspeech.bluehenge.v1.ImageDataR\rimageDataList\"R\n\tImageData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tfile_path\x18\x02 \x01(\tR\x08\x66ilePath\x12\x18\n\x07\x63\x61ption\x18\x03 \x01(\tR\x07\x63\x61ption2\xc6\x0b\n\x10\x42luehengeService\x12\x62\n\x07Version\x12).cobaltspeech.bluehenge.v1.VersionRequest\x1a*.cobaltspeech.bluehenge.v1.VersionResponse\"\x00\x12k\n\nListModels\x12,.cobaltspeech.bluehenge.v1.ListModelsRequest\x1a-.cobaltspeech.bluehenge.v1.ListModelsResponse\"\x00\x12t\n\rCreateSession\x12/.cobaltspeech.bluehenge.v1.CreateSessionRequest\x1a\x30.cobaltspeech.bluehenge.v1.CreateSessionResponse\"\x00\x12t\n\rDeleteSession\x12/.cobaltspeech.bluehenge.v1.DeleteSessionRequest\x1a\x30.cobaltspeech.bluehenge.v1.DeleteSessionResponse\"\x00\x12t\n\rUpdateSession\x12/.cobaltspeech.bluehenge.v1.UpdateSessionRequest\x1a\x30.cobaltspeech.bluehenge.v1.UpdateSessionResponse\"\x00\x12j\n\tStreamASR\x12+.cobaltspeech.bluehenge.v1.StreamASRRequest\x1a,.cobaltspeech.bluehenge.v1.StreamASRResponse\"\x00(\x01\x12j\n\tStreamTTS\x12+.cobaltspeech.bluehenge.v1.StreamTTSRequest\x1a,.cobaltspeech.bluehenge.v1.StreamTTSResponse\"\x00\x30\x01\x12o\n\nTranscribe\x12,.cobaltspeech.bluehenge.v1.TranscribeRequest\x1a-.cobaltspeech.bluehenge.v1.TranscribeResponse\"\x00(\x01\x30\x01\x12w\n\x0eListProcedures\x12\x30.cobaltspeech.bluehenge.v1.ListProceduresRequest\x1a\x31.cobaltspeech.bluehenge.v1.ListProceduresResponse\"\x00\x12t\n\rGetProcedures\x12/.cobaltspeech.bluehenge.v1.GetProceduresRequest\x1a\x30.cobaltspeech.bluehenge.v1.GetProceduresResponse\"\x00\x12\x65\n\x08SaveNote\x12*.cobaltspeech.bluehenge.v1.SaveNoteRequest\x1a+.cobaltspeech.bluehenge.v1.SaveNoteResponse\"\x00\x12w\n\x0eGetEntityImage\x12\x30.cobaltspeech.bluehenge.v1.GetEntityImageRequest\x1a\x31.cobaltspeech.bluehenge.v1.GetEntityImageResponse\"\x00\x12g\n\x08GetImage\x12*.cobaltspeech.bluehenge.v1.GetImageRequest\x1a+.cobaltspeech.bluehenge.v1.GetImageResponse\"\x00\x30\x01\x42\x80\x02\n\x1d\x63om.cobaltspeech.bluehenge.v1B\x0e\x42luehengeProtoP\x01ZIgithub.com/cobaltspeech/go-genproto/cobaltspeech/bluehenge/v1;bluehengev1\xa2\x02\x03\x43\x42X\xaa\x02\x19\x43obaltspeech.Bluehenge.V1\xca\x02\x19\x43obaltspeech\\Bluehenge\\V1\xe2\x02%Cobaltspeech\\Bluehenge\\V1\\GPBMetadata\xea\x02\x1b\x43obaltspeech::Bluehenge::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.bluehenge.v1.bluehenge_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.cobaltspeech.bluehenge.v1B\016BluehengeProtoP\001ZIgithub.com/cobaltspeech/go-genproto/cobaltspeech/bluehenge/v1;bluehengev1\242\002\003CBX\252\002\031Cobaltspeech.Bluehenge.V1\312\002\031Cobaltspeech\\Bluehenge\\V1\342\002%Cobaltspeech\\Bluehenge\\V1\\GPBMetadata\352\002\033Cobaltspeech::Bluehenge::V1'
  _globals['_VERSIONREQUEST']._serialized_start=113
  _globals['_VERSIONREQUEST']._serialized_end=129
  _globals['_VERSIONRESPONSE']._serialized_start=132
  _globals['_VERSIONRESPONSE']._serialized_end=282
  _globals['_LISTMODELSREQUEST']._serialized_start=285
  _globals['_LISTMODELSREQUEST']._serialized_end=414
  _globals['_LISTMODELSRESPONSE']._serialized_start=417
  _globals['_LISTMODELSRESPONSE']._serialized_end=550
  _globals['_CREATESESSIONREQUEST']._serialized_start=553
  _globals['_CREATESESSIONREQUEST']._serialized_end=694
  _globals['_CREATESESSIONRESPONSE']._serialized_start=697
  _globals['_CREATESESSIONRESPONSE']._serialized_end=842
  _globals['_DELETESESSIONREQUEST']._serialized_start=845
  _globals['_DELETESESSIONREQUEST']._serialized_end=986
  _globals['_DELETESESSIONRESPONSE']._serialized_start=989
  _globals['_DELETESESSIONRESPONSE']._serialized_end=1134
  _globals['_UPDATESESSIONREQUEST']._serialized_start=1137
  _globals['_UPDATESESSIONREQUEST']._serialized_end=1278
  _globals['_UPDATESESSIONRESPONSE']._serialized_start=1281
  _globals['_UPDATESESSIONRESPONSE']._serialized_end=1426
  _globals['_STREAMASRREQUEST']._serialized_start=1428
  _globals['_STREAMASRREQUEST']._serialized_end=1553
  _globals['_STREAMASRRESPONSE']._serialized_start=1556
  _globals['_STREAMASRRESPONSE']._serialized_end=1685
  _globals['_STREAMTTSREQUEST']._serialized_start=1687
  _globals['_STREAMTTSREQUEST']._serialized_end=1812
  _globals['_STREAMTTSRESPONSE']._serialized_start=1815
  _globals['_STREAMTTSRESPONSE']._serialized_end=1944
  _globals['_TRANSCRIBEREQUEST']._serialized_start=1947
  _globals['_TRANSCRIBEREQUEST']._serialized_end=2075
  _globals['_TRANSCRIBERESPONSE']._serialized_start=2078
  _globals['_TRANSCRIBERESPONSE']._serialized_end=2210
  _globals['_GETIMAGEREQUEST']._serialized_start=2212
  _globals['_GETIMAGEREQUEST']._serialized_end=2266
  _globals['_GETIMAGERESPONSE']._serialized_start=2268
  _globals['_GETIMAGERESPONSE']._serialized_end=2317
  _globals['_LISTPROCEDURESREQUEST']._serialized_start=2319
  _globals['_LISTPROCEDURESREQUEST']._serialized_end=2342
  _globals['_LISTPROCEDURESRESPONSE']._serialized_start=2344
  _globals['_LISTPROCEDURESRESPONSE']._serialized_end=2450
  _globals['_GETPROCEDURESREQUEST']._serialized_start=2452
  _globals['_GETPROCEDURESREQUEST']._serialized_end=2490
  _globals['_GETPROCEDURESRESPONSE']._serialized_start=2493
  _globals['_GETPROCEDURESRESPONSE']._serialized_end=2802
  _globals['_INPUTCONDITIONDATA']._serialized_start=2805
  _globals['_INPUTCONDITIONDATA']._serialized_end=3044
  _globals['_TASKDATA']._serialized_start=3047
  _globals['_TASKDATA']._serialized_end=3272
  _globals['_STEPDATA']._serialized_start=3275
  _globals['_STEPDATA']._serialized_end=3547
  _globals['_NOTES']._serialized_start=3549
  _globals['_NOTES']._serialized_end=3576
  _globals['_SAVENOTEREQUEST']._serialized_start=3578
  _globals['_SAVENOTEREQUEST']._serialized_end=3640
  _globals['_SAVENOTERESPONSE']._serialized_start=3642
  _globals['_SAVENOTERESPONSE']._serialized_end=3660
  _globals['_GETENTITYIMAGEREQUEST']._serialized_start=3662
  _globals['_GETENTITYIMAGEREQUEST']._serialized_end=3701
  _globals['_GETENTITYIMAGERESPONSE']._serialized_start=3703
  _globals['_GETENTITYIMAGERESPONSE']._serialized_end=3805
  _globals['_IMAGEDATA']._serialized_start=3807
  _globals['_IMAGEDATA']._serialized_end=3889
  _globals['_BLUEHENGESERVICE']._serialized_start=3892
  _globals['_BLUEHENGESERVICE']._serialized_end=5370
# @@protoc_insertion_point(module_scope)