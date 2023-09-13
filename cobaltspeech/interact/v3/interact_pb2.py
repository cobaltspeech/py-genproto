# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/interact/v3/interact.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cobaltspeech.chosun.v2 import chosun_pb2 as cobaltspeech_dot_chosun_dot_v2_dot_chosun__pb2
from cobaltspeech.cubic.v5 import cubic_pb2 as cobaltspeech_dot_cubic_dot_v5_dot_cubic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cobaltspeech/interact/v3/interact.proto\x12\x18\x63obaltspeech.interact.v3\x1a#cobaltspeech/chosun/v2/chosun.proto\x1a!cobaltspeech/cubic/v5/cubic.proto\"\x10\n\x0eVersionRequest\"o\n\x0fVersionResponse\x12\x1a\n\x08\x64iatheke\x18\x01 \x01(\tR\x08\x64iatheke\x12\x16\n\x06\x63hosun\x18\x02 \x01(\tR\x06\x63hosun\x12\x14\n\x05\x63ubic\x18\x03 \x01(\tR\x05\x63ubic\x12\x12\n\x04luna\x18\x04 \x01(\tR\x04luna\"\x13\n\x11ListModelsRequest\"Q\n\x12ListModelsResponse\x12;\n\x06models\x18\x01 \x03(\x0b\x32#.cobaltspeech.interact.v3.ModelInfoR\x06models\"\x94\x01\n\x14\x43reateSessionRequest\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x1a\n\x08wakeword\x18\x02 \x01(\tR\x08wakeword\x12\x45\n\x08metadata\x18\x03 \x01(\x0b\x32).cobaltspeech.interact.v3.SessionMetadataR\x08metadata\"g\n\x15\x43reateSessionResponse\x12N\n\x0esession_output\x18\x01 \x01(\x0b\x32\'.cobaltspeech.interact.v3.SessionOutputR\rsessionOutput\"Z\n\x14\x44\x65leteSessionRequest\x12\x42\n\ntoken_data\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\ttokenData\"\x17\n\x15\x44\x65leteSessionResponse\"c\n\x14UpdateSessionRequest\x12K\n\rsession_input\x18\x01 \x01(\x0b\x32&.cobaltspeech.interact.v3.SessionInputR\x0csessionInput\"g\n\x15UpdateSessionResponse\x12N\n\x0esession_output\x18\x01 \x01(\x0b\x32\'.cobaltspeech.interact.v3.SessionOutputR\rsessionOutput\"\\\n\x10StreamTTSRequest\x12H\n\x0creply_action\x18\x01 \x01(\x0b\x32%.cobaltspeech.interact.v3.ReplyActionR\x0breplyAction\")\n\x11StreamTTSResponse\x12\x14\n\x05\x61udio\x18\x01 \x01(\x0cR\x05\x61udio\"\x9b\x01\n\tModelInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08language\x18\x03 \x01(\tR\x08language\x12&\n\x0f\x61sr_sample_rate\x18\x04 \x01(\rR\rasrSampleRate\x12&\n\x0ftts_sample_rate\x18\x05 \x01(\rR\rttsSampleRate\"\xbf\x02\n\x0cSessionInput\x12\x39\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\x05token\x12\x39\n\x04text\x18\x02 \x01(\x0b\x32#.cobaltspeech.interact.v3.TextInputH\x00R\x04text\x12\x37\n\x03\x61sr\x18\x03 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultH\x00R\x03\x61sr\x12;\n\x03\x63md\x18\x04 \x01(\x0b\x32\'.cobaltspeech.interact.v3.CommandResultH\x00R\x03\x63md\x12:\n\x05story\x18\x05 \x01(\x0b\x32\".cobaltspeech.interact.v3.SetStoryH\x00R\x05storyB\x07\n\x05input\"K\n\tTokenData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\"\x1f\n\tTextInput\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\"\xda\x01\n\rCommandResult\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x61\n\x0eout_parameters\x18\x02 \x03(\x0b\x32:.cobaltspeech.interact.v3.CommandResult.OutParametersEntryR\routParameters\x12\x14\n\x05\x65rror\x18\x03 \x01(\tR\x05\x65rror\x1a@\n\x12OutParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb8\x01\n\x08SetStory\x12\x19\n\x08story_id\x18\x01 \x01(\tR\x07storyId\x12R\n\nparameters\x18\x02 \x03(\x0b\x32\x32.cobaltspeech.interact.v3.SetStory.ParametersEntryR\nparameters\x1a=\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x91\x01\n\rSessionOutput\x12\x39\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\x05token\x12\x45\n\x0b\x61\x63tion_list\x18\x02 \x03(\x0b\x32$.cobaltspeech.interact.v3.ActionDataR\nactionList\"\xad\x02\n\nActionData\x12\x43\n\x05input\x18\x01 \x01(\x0b\x32+.cobaltspeech.interact.v3.WaitForUserActionH\x00R\x05input\x12\x43\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\'.cobaltspeech.interact.v3.CommandActionH\x00R\x07\x63ommand\x12=\n\x05reply\x18\x03 \x01(\x0b\x32%.cobaltspeech.interact.v3.ReplyActionH\x00R\x05reply\x12L\n\ntranscribe\x18\x04 \x01(\x0b\x32*.cobaltspeech.interact.v3.TranscribeActionH\x00R\ntranscribeB\x08\n\x06\x61\x63tion\"_\n\x11WaitForUserAction\x12,\n\x12requires_wake_word\x18\x01 \x01(\x08R\x10requiresWakeWord\x12\x1c\n\timmediate\x18\x02 \x01(\x08R\timmediate\"\x92\x02\n\rCommandAction\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12g\n\x10input_parameters\x18\x02 \x03(\x0b\x32<.cobaltspeech.interact.v3.CommandAction.InputParametersEntryR\x0finputParameters\x12\x44\n\nnlu_result\x18\x03 \x01(\x0b\x32%.cobaltspeech.chosun.v2.ParseResponseR\tnluResult\x1a\x42\n\x14InputParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"@\n\x0bReplyAction\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1d\n\nluna_model\x18\x02 \x01(\tR\tlunaModel\"t\n\x10TranscribeAction\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12$\n\x0e\x63ubic_model_id\x18\x02 \x01(\tR\x0c\x63ubicModelId\x12*\n\x11\x64iatheke_model_id\x18\x03 \x01(\tR\x0f\x64iathekeModelId\"o\n\x10StreamASRRequest\x12;\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataH\x00R\x05token\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"W\n\x11StreamASRResponse\x12\x42\n\nasr_result\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultR\tasrResult\"{\n\x1cStreamASRWithPartialsRequest\x12;\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataH\x00R\x05token\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"\xc0\x01\n\x1dStreamASRWithPartialsResponse\x12Q\n\x0epartial_result\x18\x01 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultH\x00R\rpartialResult\x12\x44\n\nasr_result\x18\x02 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultH\x00R\tasrResultB\x06\n\x04\x64\x61ta\"\xa9\x01\n\tASRResult\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x1b\n\ttimed_out\x18\x03 \x01(\x08R\x08timedOut\x12K\n\x0c\x63ubic_result\x18\x04 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultR\x0b\x63ubicResult\"y\n\x11TranscribeRequest\x12\x44\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32*.cobaltspeech.interact.v3.TranscribeActionH\x00R\x06\x61\x63tion\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"\xb4\x01\n\x12TranscribeResponse\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x1d\n\nis_partial\x18\x03 \x01(\x08R\tisPartial\x12K\n\x0c\x63ubic_result\x18\x04 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultR\x0b\x63ubicResult\"j\n\x0fSessionMetadata\x12\'\n\x0f\x63ustom_metadata\x18\x01 \x01(\tR\x0e\x63ustomMetadata\x12.\n\x13storage_file_prefix\x18\x02 \x01(\tR\x11storageFilePrefix2\x8e\x08\n\x0fInteractService\x12`\n\x07Version\x12(.cobaltspeech.interact.v3.VersionRequest\x1a).cobaltspeech.interact.v3.VersionResponse\"\x00\x12i\n\nListModels\x12+.cobaltspeech.interact.v3.ListModelsRequest\x1a,.cobaltspeech.interact.v3.ListModelsResponse\"\x00\x12r\n\rCreateSession\x12..cobaltspeech.interact.v3.CreateSessionRequest\x1a/.cobaltspeech.interact.v3.CreateSessionResponse\"\x00\x12r\n\rDeleteSession\x12..cobaltspeech.interact.v3.DeleteSessionRequest\x1a/.cobaltspeech.interact.v3.DeleteSessionResponse\"\x00\x12r\n\rUpdateSession\x12..cobaltspeech.interact.v3.UpdateSessionRequest\x1a/.cobaltspeech.interact.v3.UpdateSessionResponse\"\x00\x12h\n\tStreamASR\x12*.cobaltspeech.interact.v3.StreamASRRequest\x1a+.cobaltspeech.interact.v3.StreamASRResponse\"\x00(\x01\x12h\n\tStreamTTS\x12*.cobaltspeech.interact.v3.StreamTTSRequest\x1a+.cobaltspeech.interact.v3.StreamTTSResponse\"\x00\x30\x01\x12m\n\nTranscribe\x12+.cobaltspeech.interact.v3.TranscribeRequest\x1a,.cobaltspeech.interact.v3.TranscribeResponse\"\x00(\x01\x30\x01\x12\x8e\x01\n\x15StreamASRWithPartials\x12\x36.cobaltspeech.interact.v3.StreamASRWithPartialsRequest\x1a\x37.cobaltspeech.interact.v3.StreamASRWithPartialsResponse\"\x00(\x01\x30\x01\x42\xf8\x01\n\x1c\x63om.cobaltspeech.interact.v3B\rInteractProtoP\x01ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/interact/v3;interactv3\xa2\x02\x03\x43IX\xaa\x02\x18\x43obaltspeech.Interact.V3\xca\x02\x18\x43obaltspeech\\Interact\\V3\xe2\x02$Cobaltspeech\\Interact\\V3\\GPBMetadata\xea\x02\x1a\x43obaltspeech::Interact::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.interact.v3.interact_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.cobaltspeech.interact.v3B\rInteractProtoP\001ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/interact/v3;interactv3\242\002\003CIX\252\002\030Cobaltspeech.Interact.V3\312\002\030Cobaltspeech\\Interact\\V3\342\002$Cobaltspeech\\Interact\\V3\\GPBMetadata\352\002\032Cobaltspeech::Interact::V3'
  _COMMANDRESULT_OUTPARAMETERSENTRY._options = None
  _COMMANDRESULT_OUTPARAMETERSENTRY._serialized_options = b'8\001'
  _SETSTORY_PARAMETERSENTRY._options = None
  _SETSTORY_PARAMETERSENTRY._serialized_options = b'8\001'
  _COMMANDACTION_INPUTPARAMETERSENTRY._options = None
  _COMMANDACTION_INPUTPARAMETERSENTRY._serialized_options = b'8\001'
  _globals['_VERSIONREQUEST']._serialized_start=141
  _globals['_VERSIONREQUEST']._serialized_end=157
  _globals['_VERSIONRESPONSE']._serialized_start=159
  _globals['_VERSIONRESPONSE']._serialized_end=270
  _globals['_LISTMODELSREQUEST']._serialized_start=272
  _globals['_LISTMODELSREQUEST']._serialized_end=291
  _globals['_LISTMODELSRESPONSE']._serialized_start=293
  _globals['_LISTMODELSRESPONSE']._serialized_end=374
  _globals['_CREATESESSIONREQUEST']._serialized_start=377
  _globals['_CREATESESSIONREQUEST']._serialized_end=525
  _globals['_CREATESESSIONRESPONSE']._serialized_start=527
  _globals['_CREATESESSIONRESPONSE']._serialized_end=630
  _globals['_DELETESESSIONREQUEST']._serialized_start=632
  _globals['_DELETESESSIONREQUEST']._serialized_end=722
  _globals['_DELETESESSIONRESPONSE']._serialized_start=724
  _globals['_DELETESESSIONRESPONSE']._serialized_end=747
  _globals['_UPDATESESSIONREQUEST']._serialized_start=749
  _globals['_UPDATESESSIONREQUEST']._serialized_end=848
  _globals['_UPDATESESSIONRESPONSE']._serialized_start=850
  _globals['_UPDATESESSIONRESPONSE']._serialized_end=953
  _globals['_STREAMTTSREQUEST']._serialized_start=955
  _globals['_STREAMTTSREQUEST']._serialized_end=1047
  _globals['_STREAMTTSRESPONSE']._serialized_start=1049
  _globals['_STREAMTTSRESPONSE']._serialized_end=1090
  _globals['_MODELINFO']._serialized_start=1093
  _globals['_MODELINFO']._serialized_end=1248
  _globals['_SESSIONINPUT']._serialized_start=1251
  _globals['_SESSIONINPUT']._serialized_end=1570
  _globals['_TOKENDATA']._serialized_start=1572
  _globals['_TOKENDATA']._serialized_end=1647
  _globals['_TEXTINPUT']._serialized_start=1649
  _globals['_TEXTINPUT']._serialized_end=1680
  _globals['_COMMANDRESULT']._serialized_start=1683
  _globals['_COMMANDRESULT']._serialized_end=1901
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._serialized_start=1837
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._serialized_end=1901
  _globals['_SETSTORY']._serialized_start=1904
  _globals['_SETSTORY']._serialized_end=2088
  _globals['_SETSTORY_PARAMETERSENTRY']._serialized_start=2027
  _globals['_SETSTORY_PARAMETERSENTRY']._serialized_end=2088
  _globals['_SESSIONOUTPUT']._serialized_start=2091
  _globals['_SESSIONOUTPUT']._serialized_end=2236
  _globals['_ACTIONDATA']._serialized_start=2239
  _globals['_ACTIONDATA']._serialized_end=2540
  _globals['_WAITFORUSERACTION']._serialized_start=2542
  _globals['_WAITFORUSERACTION']._serialized_end=2637
  _globals['_COMMANDACTION']._serialized_start=2640
  _globals['_COMMANDACTION']._serialized_end=2914
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._serialized_start=2848
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._serialized_end=2914
  _globals['_REPLYACTION']._serialized_start=2916
  _globals['_REPLYACTION']._serialized_end=2980
  _globals['_TRANSCRIBEACTION']._serialized_start=2982
  _globals['_TRANSCRIBEACTION']._serialized_end=3098
  _globals['_STREAMASRREQUEST']._serialized_start=3100
  _globals['_STREAMASRREQUEST']._serialized_end=3211
  _globals['_STREAMASRRESPONSE']._serialized_start=3213
  _globals['_STREAMASRRESPONSE']._serialized_end=3300
  _globals['_STREAMASRWITHPARTIALSREQUEST']._serialized_start=3302
  _globals['_STREAMASRWITHPARTIALSREQUEST']._serialized_end=3425
  _globals['_STREAMASRWITHPARTIALSRESPONSE']._serialized_start=3428
  _globals['_STREAMASRWITHPARTIALSRESPONSE']._serialized_end=3620
  _globals['_ASRRESULT']._serialized_start=3623
  _globals['_ASRRESULT']._serialized_end=3792
  _globals['_TRANSCRIBEREQUEST']._serialized_start=3794
  _globals['_TRANSCRIBEREQUEST']._serialized_end=3915
  _globals['_TRANSCRIBERESPONSE']._serialized_start=3918
  _globals['_TRANSCRIBERESPONSE']._serialized_end=4098
  _globals['_SESSIONMETADATA']._serialized_start=4100
  _globals['_SESSIONMETADATA']._serialized_end=4206
  _globals['_INTERACTSERVICE']._serialized_start=4209
  _globals['_INTERACTSERVICE']._serialized_end=5247
# @@protoc_insertion_point(module_scope)