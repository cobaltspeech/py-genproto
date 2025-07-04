# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cobaltspeech/interact/v3/interact.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'cobaltspeech/interact/v3/interact.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cobaltspeech.chosun.v2 import chosun_pb2 as cobaltspeech_dot_chosun_dot_v2_dot_chosun__pb2
from cobaltspeech.cubic.v5 import cubic_pb2 as cobaltspeech_dot_cubic_dot_v5_dot_cubic__pb2
from cobaltspeech.voicegen.v1 import voicegen_pb2 as cobaltspeech_dot_voicegen_dot_v1_dot_voicegen__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cobaltspeech/interact/v3/interact.proto\x12\x18\x63obaltspeech.interact.v3\x1a#cobaltspeech/chosun/v2/chosun.proto\x1a!cobaltspeech/cubic/v5/cubic.proto\x1a\'cobaltspeech/voicegen/v1/voicegen.proto\"\x10\n\x0eVersionRequest\"o\n\x0fVersionResponse\x12\x1a\n\x08\x64iatheke\x18\x01 \x01(\tR\x08\x64iatheke\x12\x16\n\x06\x63hosun\x18\x02 \x01(\tR\x06\x63hosun\x12\x14\n\x05\x63ubic\x18\x03 \x01(\tR\x05\x63ubic\x12\x12\n\x04luna\x18\x04 \x01(\tR\x04luna\"\x13\n\x11ListModelsRequest\"Q\n\x12ListModelsResponse\x12;\n\x06models\x18\x01 \x03(\x0b\x32#.cobaltspeech.interact.v3.ModelInfoR\x06models\"\xc0\x02\n\x14\x43reateSessionRequest\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x1a\n\x08wakeword\x18\x02 \x01(\tR\x08wakeword\x12\x45\n\x08metadata\x18\x03 \x01(\x0b\x32).cobaltspeech.interact.v3.SessionMetadataR\x08metadata\x12S\n\x12input_audio_format\x18\x04 \x01(\x0b\x32%.cobaltspeech.interact.v3.AudioFormatR\x10inputAudioFormat\x12U\n\x13output_audio_format\x18\x05 \x01(\x0b\x32%.cobaltspeech.interact.v3.AudioFormatR\x11outputAudioFormat\"g\n\x15\x43reateSessionResponse\x12N\n\x0esession_output\x18\x01 \x01(\x0b\x32\'.cobaltspeech.interact.v3.SessionOutputR\rsessionOutput\"Z\n\x14\x44\x65leteSessionRequest\x12\x42\n\ntoken_data\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\ttokenData\"\x17\n\x15\x44\x65leteSessionResponse\"c\n\x14UpdateSessionRequest\x12K\n\rsession_input\x18\x01 \x01(\x0b\x32&.cobaltspeech.interact.v3.SessionInputR\x0csessionInput\"g\n\x15UpdateSessionResponse\x12N\n\x0esession_output\x18\x01 \x01(\x0b\x32\'.cobaltspeech.interact.v3.SessionOutputR\rsessionOutput\"\xed\x01\n\x10StreamTTSRequest\x12H\n\x0creply_action\x18\x01 \x01(\x0b\x32%.cobaltspeech.interact.v3.ReplyActionR\x0breplyAction\x12\x39\n\x05token\x18\x02 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\x05token\x12T\n\x10synthesis_config\x18\x03 \x01(\x0b\x32).cobaltspeech.voicegen.v1.SynthesisConfigR\x0fsynthesisConfig\")\n\x11StreamTTSResponse\x12\x14\n\x05\x61udio\x18\x01 \x01(\x0cR\x05\x61udio\"\xf8\x01\n\tModelInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08language\x18\x03 \x01(\tR\x08language\x12&\n\x0f\x61sr_sample_rate\x18\x04 \x01(\rR\rasrSampleRate\x12&\n\x0ftts_sample_rate\x18\x05 \x01(\rR\rttsSampleRate\x12[\n\x14tts_model_attributes\x18\x06 \x03(\x0b\x32).cobaltspeech.voicegen.v1.ModelAttributesR\x12ttsModelAttributes\"\xbf\x02\n\x0cSessionInput\x12\x39\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\x05token\x12\x39\n\x04text\x18\x02 \x01(\x0b\x32#.cobaltspeech.interact.v3.TextInputH\x00R\x04text\x12\x37\n\x03\x61sr\x18\x03 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultH\x00R\x03\x61sr\x12;\n\x03\x63md\x18\x04 \x01(\x0b\x32\'.cobaltspeech.interact.v3.CommandResultH\x00R\x03\x63md\x12:\n\x05story\x18\x05 \x01(\x0b\x32\".cobaltspeech.interact.v3.SetStoryH\x00R\x05storyB\x07\n\x05input\"K\n\tTokenData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\"\x1f\n\tTextInput\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\"\xda\x01\n\rCommandResult\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x61\n\x0eout_parameters\x18\x02 \x03(\x0b\x32:.cobaltspeech.interact.v3.CommandResult.OutParametersEntryR\routParameters\x12\x14\n\x05\x65rror\x18\x03 \x01(\tR\x05\x65rror\x1a@\n\x12OutParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb8\x01\n\x08SetStory\x12\x19\n\x08story_id\x18\x01 \x01(\tR\x07storyId\x12R\n\nparameters\x18\x02 \x03(\x0b\x32\x32.cobaltspeech.interact.v3.SetStory.ParametersEntryR\nparameters\x1a=\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x91\x01\n\rSessionOutput\x12\x39\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataR\x05token\x12\x45\n\x0b\x61\x63tion_list\x18\x02 \x03(\x0b\x32$.cobaltspeech.interact.v3.ActionDataR\nactionList\"\xad\x02\n\nActionData\x12\x43\n\x05input\x18\x01 \x01(\x0b\x32+.cobaltspeech.interact.v3.WaitForUserActionH\x00R\x05input\x12\x43\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\'.cobaltspeech.interact.v3.CommandActionH\x00R\x07\x63ommand\x12=\n\x05reply\x18\x03 \x01(\x0b\x32%.cobaltspeech.interact.v3.ReplyActionH\x00R\x05reply\x12L\n\ntranscribe\x18\x04 \x01(\x0b\x32*.cobaltspeech.interact.v3.TranscribeActionH\x00R\ntranscribeB\x08\n\x06\x61\x63tion\"_\n\x11WaitForUserAction\x12,\n\x12requires_wake_word\x18\x01 \x01(\x08R\x10requiresWakeWord\x12\x1c\n\timmediate\x18\x02 \x01(\x08R\timmediate\"\x92\x02\n\rCommandAction\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12g\n\x10input_parameters\x18\x02 \x03(\x0b\x32<.cobaltspeech.interact.v3.CommandAction.InputParametersEntryR\x0finputParameters\x12\x44\n\nnlu_result\x18\x03 \x01(\x0b\x32%.cobaltspeech.chosun.v2.ParseResponseR\tnluResult\x1a\x42\n\x14InputParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"@\n\x0bReplyAction\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1d\n\nluna_model\x18\x02 \x01(\tR\tlunaModel\"t\n\x10TranscribeAction\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12$\n\x0e\x63ubic_model_id\x18\x02 \x01(\tR\x0c\x63ubicModelId\x12*\n\x11\x64iatheke_model_id\x18\x03 \x01(\tR\x0f\x64iathekeModelId\"o\n\x10StreamASRRequest\x12;\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataH\x00R\x05token\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"W\n\x11StreamASRResponse\x12\x42\n\nasr_result\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultR\tasrResult\"{\n\x1cStreamASRWithPartialsRequest\x12;\n\x05token\x18\x01 \x01(\x0b\x32#.cobaltspeech.interact.v3.TokenDataH\x00R\x05token\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"\x95\x02\n\x1dStreamASRWithPartialsResponse\x12Q\n\x0epartial_result\x18\x01 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultH\x00R\rpartialResult\x12\x44\n\nasr_result\x18\x02 \x01(\x0b\x32#.cobaltspeech.interact.v3.ASRResultH\x00R\tasrResult\x12S\n\x0fwakeword_result\x18\x03 \x01(\x0b\x32(.cobaltspeech.interact.v3.WakewordResultH\x00R\x0ewakewordResultB\x06\n\x04\x64\x61ta\"\xa9\x01\n\tASRResult\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x1b\n\ttimed_out\x18\x03 \x01(\x08R\x08timedOut\x12K\n\x0c\x63ubic_result\x18\x04 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultR\x0b\x63ubicResult\"3\n\x0eWakewordResult\x12!\n\x0ctimestamp_ms\x18\x01 \x01(\x04R\x0btimestampMs\"y\n\x11TranscribeRequest\x12\x44\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32*.cobaltspeech.interact.v3.TranscribeActionH\x00R\x06\x61\x63tion\x12\x16\n\x05\x61udio\x18\x02 \x01(\x0cH\x00R\x05\x61udioB\x06\n\x04\x64\x61ta\"\xb4\x01\n\x12TranscribeResponse\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x1d\n\nis_partial\x18\x03 \x01(\x08R\tisPartial\x12K\n\x0c\x63ubic_result\x18\x04 \x01(\x0b\x32(.cobaltspeech.cubic.v5.RecognitionResultR\x0b\x63ubicResult\"j\n\x0fSessionMetadata\x12\'\n\x0f\x63ustom_metadata\x18\x01 \x01(\tR\x0e\x63ustomMetadata\x12.\n\x13storage_file_prefix\x18\x02 \x01(\tR\x11storageFilePrefix\"\xac\x02\n\x0b\x41udioFormat\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\rR\nsampleRate\x12\x1a\n\x08\x63hannels\x18\x02 \x01(\rR\x08\x63hannels\x12\x1b\n\tbit_depth\x18\x03 \x01(\rR\x08\x62itDepth\x12:\n\x05\x63odec\x18\x04 \x01(\x0e\x32$.cobaltspeech.interact.v3.AudioCodecR\x05\x63odec\x12\x43\n\x08\x65ncoding\x18\x05 \x01(\x0e\x32\'.cobaltspeech.interact.v3.AudioEncodingR\x08\x65ncoding\x12\x42\n\nbyte_order\x18\x06 \x01(\x0e\x32#.cobaltspeech.interact.v3.ByteOrderR\tbyteOrder*`\n\tByteOrder\x12\x1a\n\x16\x42YTE_ORDER_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x42YTE_ORDER_LITTLE_ENDIAN\x10\x01\x12\x19\n\x15\x42YTE_ORDER_BIG_ENDIAN\x10\x02*\xb8\x01\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41UDIO_ENCODING_SIGNED\x10\x01\x12\x1b\n\x17\x41UDIO_ENCODING_UNSIGNED\x10\x02\x12\x1d\n\x19\x41UDIO_ENCODING_IEEE_FLOAT\x10\x03\x12\x17\n\x13\x41UDIO_ENCODING_ULAW\x10\x04\x12\x17\n\x13\x41UDIO_ENCODING_ALAW\x10\x05*\x98\x01\n\nAudioCodec\x12\x1b\n\x17\x41UDIO_CODEC_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x41UDIO_CODEC_RAW\x10\x01\x12\x13\n\x0f\x41UDIO_CODEC_WAV\x10\x02\x12\x13\n\x0f\x41UDIO_CODEC_MP3\x10\x03\x12\x14\n\x10\x41UDIO_CODEC_FLAC\x10\x04\x12\x18\n\x14\x41UDIO_CODEC_OGG_OPUS\x10\x05\x32\x8e\x08\n\x0fInteractService\x12`\n\x07Version\x12(.cobaltspeech.interact.v3.VersionRequest\x1a).cobaltspeech.interact.v3.VersionResponse\"\x00\x12i\n\nListModels\x12+.cobaltspeech.interact.v3.ListModelsRequest\x1a,.cobaltspeech.interact.v3.ListModelsResponse\"\x00\x12r\n\rCreateSession\x12..cobaltspeech.interact.v3.CreateSessionRequest\x1a/.cobaltspeech.interact.v3.CreateSessionResponse\"\x00\x12r\n\rDeleteSession\x12..cobaltspeech.interact.v3.DeleteSessionRequest\x1a/.cobaltspeech.interact.v3.DeleteSessionResponse\"\x00\x12r\n\rUpdateSession\x12..cobaltspeech.interact.v3.UpdateSessionRequest\x1a/.cobaltspeech.interact.v3.UpdateSessionResponse\"\x00\x12h\n\tStreamASR\x12*.cobaltspeech.interact.v3.StreamASRRequest\x1a+.cobaltspeech.interact.v3.StreamASRResponse\"\x00(\x01\x12\x8e\x01\n\x15StreamASRWithPartials\x12\x36.cobaltspeech.interact.v3.StreamASRWithPartialsRequest\x1a\x37.cobaltspeech.interact.v3.StreamASRWithPartialsResponse\"\x00(\x01\x30\x01\x12m\n\nTranscribe\x12+.cobaltspeech.interact.v3.TranscribeRequest\x1a,.cobaltspeech.interact.v3.TranscribeResponse\"\x00(\x01\x30\x01\x12h\n\tStreamTTS\x12*.cobaltspeech.interact.v3.StreamTTSRequest\x1a+.cobaltspeech.interact.v3.StreamTTSResponse\"\x00\x30\x01\x42\xf8\x01\n\x1c\x63om.cobaltspeech.interact.v3B\rInteractProtoP\x01ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/interact/v3;interactv3\xa2\x02\x03\x43IX\xaa\x02\x18\x43obaltspeech.Interact.V3\xca\x02\x18\x43obaltspeech\\Interact\\V3\xe2\x02$Cobaltspeech\\Interact\\V3\\GPBMetadata\xea\x02\x1a\x43obaltspeech::Interact::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.interact.v3.interact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.cobaltspeech.interact.v3B\rInteractProtoP\001ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/interact/v3;interactv3\242\002\003CIX\252\002\030Cobaltspeech.Interact.V3\312\002\030Cobaltspeech\\Interact\\V3\342\002$Cobaltspeech\\Interact\\V3\\GPBMetadata\352\002\032Cobaltspeech::Interact::V3'
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._loaded_options = None
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_SETSTORY_PARAMETERSENTRY']._loaded_options = None
  _globals['_SETSTORY_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._loaded_options = None
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_BYTEORDER']._serialized_start=5101
  _globals['_BYTEORDER']._serialized_end=5197
  _globals['_AUDIOENCODING']._serialized_start=5200
  _globals['_AUDIOENCODING']._serialized_end=5384
  _globals['_AUDIOCODEC']._serialized_start=5387
  _globals['_AUDIOCODEC']._serialized_end=5539
  _globals['_VERSIONREQUEST']._serialized_start=182
  _globals['_VERSIONREQUEST']._serialized_end=198
  _globals['_VERSIONRESPONSE']._serialized_start=200
  _globals['_VERSIONRESPONSE']._serialized_end=311
  _globals['_LISTMODELSREQUEST']._serialized_start=313
  _globals['_LISTMODELSREQUEST']._serialized_end=332
  _globals['_LISTMODELSRESPONSE']._serialized_start=334
  _globals['_LISTMODELSRESPONSE']._serialized_end=415
  _globals['_CREATESESSIONREQUEST']._serialized_start=418
  _globals['_CREATESESSIONREQUEST']._serialized_end=738
  _globals['_CREATESESSIONRESPONSE']._serialized_start=740
  _globals['_CREATESESSIONRESPONSE']._serialized_end=843
  _globals['_DELETESESSIONREQUEST']._serialized_start=845
  _globals['_DELETESESSIONREQUEST']._serialized_end=935
  _globals['_DELETESESSIONRESPONSE']._serialized_start=937
  _globals['_DELETESESSIONRESPONSE']._serialized_end=960
  _globals['_UPDATESESSIONREQUEST']._serialized_start=962
  _globals['_UPDATESESSIONREQUEST']._serialized_end=1061
  _globals['_UPDATESESSIONRESPONSE']._serialized_start=1063
  _globals['_UPDATESESSIONRESPONSE']._serialized_end=1166
  _globals['_STREAMTTSREQUEST']._serialized_start=1169
  _globals['_STREAMTTSREQUEST']._serialized_end=1406
  _globals['_STREAMTTSRESPONSE']._serialized_start=1408
  _globals['_STREAMTTSRESPONSE']._serialized_end=1449
  _globals['_MODELINFO']._serialized_start=1452
  _globals['_MODELINFO']._serialized_end=1700
  _globals['_SESSIONINPUT']._serialized_start=1703
  _globals['_SESSIONINPUT']._serialized_end=2022
  _globals['_TOKENDATA']._serialized_start=2024
  _globals['_TOKENDATA']._serialized_end=2099
  _globals['_TEXTINPUT']._serialized_start=2101
  _globals['_TEXTINPUT']._serialized_end=2132
  _globals['_COMMANDRESULT']._serialized_start=2135
  _globals['_COMMANDRESULT']._serialized_end=2353
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._serialized_start=2289
  _globals['_COMMANDRESULT_OUTPARAMETERSENTRY']._serialized_end=2353
  _globals['_SETSTORY']._serialized_start=2356
  _globals['_SETSTORY']._serialized_end=2540
  _globals['_SETSTORY_PARAMETERSENTRY']._serialized_start=2479
  _globals['_SETSTORY_PARAMETERSENTRY']._serialized_end=2540
  _globals['_SESSIONOUTPUT']._serialized_start=2543
  _globals['_SESSIONOUTPUT']._serialized_end=2688
  _globals['_ACTIONDATA']._serialized_start=2691
  _globals['_ACTIONDATA']._serialized_end=2992
  _globals['_WAITFORUSERACTION']._serialized_start=2994
  _globals['_WAITFORUSERACTION']._serialized_end=3089
  _globals['_COMMANDACTION']._serialized_start=3092
  _globals['_COMMANDACTION']._serialized_end=3366
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._serialized_start=3300
  _globals['_COMMANDACTION_INPUTPARAMETERSENTRY']._serialized_end=3366
  _globals['_REPLYACTION']._serialized_start=3368
  _globals['_REPLYACTION']._serialized_end=3432
  _globals['_TRANSCRIBEACTION']._serialized_start=3434
  _globals['_TRANSCRIBEACTION']._serialized_end=3550
  _globals['_STREAMASRREQUEST']._serialized_start=3552
  _globals['_STREAMASRREQUEST']._serialized_end=3663
  _globals['_STREAMASRRESPONSE']._serialized_start=3665
  _globals['_STREAMASRRESPONSE']._serialized_end=3752
  _globals['_STREAMASRWITHPARTIALSREQUEST']._serialized_start=3754
  _globals['_STREAMASRWITHPARTIALSREQUEST']._serialized_end=3877
  _globals['_STREAMASRWITHPARTIALSRESPONSE']._serialized_start=3880
  _globals['_STREAMASRWITHPARTIALSRESPONSE']._serialized_end=4157
  _globals['_ASRRESULT']._serialized_start=4160
  _globals['_ASRRESULT']._serialized_end=4329
  _globals['_WAKEWORDRESULT']._serialized_start=4331
  _globals['_WAKEWORDRESULT']._serialized_end=4382
  _globals['_TRANSCRIBEREQUEST']._serialized_start=4384
  _globals['_TRANSCRIBEREQUEST']._serialized_end=4505
  _globals['_TRANSCRIBERESPONSE']._serialized_start=4508
  _globals['_TRANSCRIBERESPONSE']._serialized_end=4688
  _globals['_SESSIONMETADATA']._serialized_start=4690
  _globals['_SESSIONMETADATA']._serialized_end=4796
  _globals['_AUDIOFORMAT']._serialized_start=4799
  _globals['_AUDIOFORMAT']._serialized_end=5099
  _globals['_INTERACTSERVICE']._serialized_start=5542
  _globals['_INTERACTSERVICE']._serialized_end=6580
# @@protoc_insertion_point(module_scope)
