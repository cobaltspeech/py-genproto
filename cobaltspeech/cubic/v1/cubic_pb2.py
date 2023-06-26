# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/cubic/v1/cubic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cobaltspeech/cubic/v1/cubic.proto\x12\x12\x63obaltspeech.cubic\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x13\n\x11ListModelsRequest\"\x8d\x01\n\x10RecognizeRequest\x12=\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.cobaltspeech.cubic.RecognitionConfigR\x06\x63onfig\x12:\n\x05\x61udio\x18\x02 \x01(\x0b\x32$.cobaltspeech.cubic.RecognitionAudioR\x05\x61udio\"\xa5\x01\n\x19StreamingRecognizeRequest\x12?\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.cobaltspeech.cubic.RecognitionConfigH\x00R\x06\x63onfig\x12<\n\x05\x61udio\x18\x02 \x01(\x0b\x32$.cobaltspeech.cubic.RecognitionAudioH\x00R\x05\x61udioB\t\n\x07request\"\x85\x01\n\x15\x43ompileContextRequest\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\x12;\n\x07phrases\x18\x03 \x03(\x0b\x32!.cobaltspeech.cubic.ContextPhraseR\x07phrases\"?\n\x0fVersionResponse\x12\x14\n\x05\x63ubic\x18\x01 \x01(\tR\x05\x63ubic\x12\x16\n\x06server\x18\x02 \x01(\tR\x06server\"G\n\x12ListModelsResponse\x12\x31\n\x06models\x18\x01 \x03(\x0b\x32\x19.cobaltspeech.cubic.ModelR\x06models\"V\n\x13RecognitionResponse\x12?\n\x07results\x18\x01 \x03(\x0b\x32%.cobaltspeech.cubic.RecognitionResultR\x07results\"W\n\x16\x43ompileContextResponse\x12=\n\x07\x63ontext\x18\x01 \x01(\x0b\x32#.cobaltspeech.cubic.CompiledContextR\x07\x63ontext\"\xbb\x05\n\x11RecognitionConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12U\n\x0e\x61udio_encoding\x18\x02 \x01(\x0e\x32..cobaltspeech.cubic.RecognitionConfig.EncodingR\raudioEncoding\x12<\n\x0cidle_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bidleTimeout\x12\x37\n\x18\x65nable_word_time_offsets\x18\x04 \x01(\x08R\x15\x65nableWordTimeOffsets\x12\x34\n\x16\x65nable_word_confidence\x18\x05 \x01(\x08R\x14\x65nableWordConfidence\x12\x32\n\x15\x65nable_raw_transcript\x18\x06 \x01(\x08R\x13\x65nableRawTranscript\x12\x38\n\x18\x65nable_confusion_network\x18\x07 \x01(\x08R\x16\x65nableConfusionNetwork\x12%\n\x0e\x61udio_channels\x18\x08 \x03(\rR\raudioChannels\x12\x43\n\x08metadata\x18\t \x01(\x0b\x32\'.cobaltspeech.cubic.RecognitionMetadataR\x08metadata\x12@\n\x07\x63ontext\x18\n \x01(\x0b\x32&.cobaltspeech.cubic.RecognitionContextR\x07\x63ontext\"k\n\x08\x45ncoding\x12\x10\n\x0cRAW_LINEAR16\x10\x00\x12\x07\n\x03WAV\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x08\n\x04\x46LAC\x10\x03\x12\x0b\n\x07VOX8000\x10\x04\x12\x0c\n\x08ULAW8000\x10\x05\x12\x0c\n\x08\x41LAW8000\x10\x06\x12\x08\n\x04OPUS\x10\x07\">\n\x13RecognitionMetadata\x12\'\n\x0f\x63ustom_metadata\x18\x01 \x01(\tR\x0e\x63ustomMetadata\"U\n\x12RecognitionContext\x12?\n\x08\x63ompiled\x18\x01 \x03(\x0b\x32#.cobaltspeech.cubic.CompiledContextR\x08\x63ompiled\"%\n\x0f\x43ompiledContext\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"9\n\rContextPhrase\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x14\n\x05\x62oost\x18\x02 \x01(\x02R\x05\x62oost\"&\n\x10RecognitionAudio\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"p\n\x05Model\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x43\n\nattributes\x18\x03 \x01(\x0b\x32#.cobaltspeech.cubic.ModelAttributesR\nattributes\"v\n\x0fModelAttributes\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\rR\nsampleRate\x12\x42\n\x0c\x63ontext_info\x18\x02 \x01(\x0b\x32\x1f.cobaltspeech.cubic.ContextInfoR\x0b\x63ontextInfo\"n\n\x0b\x43ontextInfo\x12)\n\x10supports_context\x18\x01 \x01(\x08R\x0fsupportsContext\x12\x34\n\x16\x61llowed_context_tokens\x18\x02 \x03(\tR\x14\x61llowedContextTokens\"\xec\x01\n\x11RecognitionResult\x12N\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32*.cobaltspeech.cubic.RecognitionAlternativeR\x0c\x61lternatives\x12\x1d\n\nis_partial\x18\x02 \x01(\x08R\tisPartial\x12\x43\n\x04\x63net\x18\x03 \x01(\x0b\x32/.cobaltspeech.cubic.RecognitionConfusionNetworkR\x04\x63net\x12#\n\raudio_channel\x18\x04 \x01(\rR\x0c\x61udioChannel\"\xdf\x02\n\x16RecognitionAlternative\x12\x1e\n\ntranscript\x18\x01 \x01(\tR\ntranscript\x12%\n\x0eraw_transcript\x18\x06 \x01(\tR\rrawTranscript\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x32\n\x05words\x18\x03 \x03(\x0b\x32\x1c.cobaltspeech.cubic.WordInfoR\x05words\x12\x39\n\traw_words\x18\x07 \x03(\x0b\x32\x1c.cobaltspeech.cubic.WordInfoR\x08rawWords\x12\x38\n\nstart_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\tstartTime\x12\x35\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\"\xaf\x01\n\x08WordInfo\x12\x12\n\x04word\x18\x01 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\x38\n\nstart_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\tstartTime\x12\x35\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\"]\n\x1bRecognitionConfusionNetwork\x12>\n\x05links\x18\x01 \x03(\x0b\x32(.cobaltspeech.cubic.ConfusionNetworkLinkR\x05links\"\xc4\x01\n\x14\x43onfusionNetworkLink\x12\x38\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\tstartTime\x12\x35\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\x12;\n\x04\x61rcs\x18\x03 \x03(\x0b\x32\'.cobaltspeech.cubic.ConfusionNetworkArcR\x04\x61rcs\"I\n\x13\x43onfusionNetworkArc\x12\x12\n\x04word\x18\x01 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence2\xe4\x04\n\x05\x43ubic\x12\\\n\x07Version\x12\x16.google.protobuf.Empty\x1a#.cobaltspeech.cubic.VersionResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/version\x12t\n\nListModels\x12%.cobaltspeech.cubic.ListModelsRequest\x1a&.cobaltspeech.cubic.ListModelsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/api/listmodels\x12u\n\tRecognize\x12$.cobaltspeech.cubic.RecognizeRequest\x1a\'.cobaltspeech.cubic.RecognitionResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/api/recognize:\x01*\x12\x85\x01\n\x12StreamingRecognize\x12-.cobaltspeech.cubic.StreamingRecognizeRequest\x1a\'.cobaltspeech.cubic.RecognitionResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/api/stream(\x01\x30\x01\x12\x87\x01\n\x0e\x43ompileContext\x12).cobaltspeech.cubic.CompileContextRequest\x1a*.cobaltspeech.cubic.CompileContextResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/api/compilecontext:\x01*B\xc8\x01\n\x16\x63om.cobaltspeech.cubicB\nCubicProtoP\x01Z9github.com/cobaltspeech/go-genproto/cobaltspeech/cubic/v1\xa2\x02\x03\x43\x43X\xaa\x02\x12\x43obaltspeech.Cubic\xca\x02\x12\x43obaltspeech\\Cubic\xe2\x02\x1e\x43obaltspeech\\Cubic\\GPBMetadata\xea\x02\x13\x43obaltspeech::Cubicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.cubic.v1.cubic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.cobaltspeech.cubicB\nCubicProtoP\001Z9github.com/cobaltspeech/go-genproto/cobaltspeech/cubic/v1\242\002\003CCX\252\002\022Cobaltspeech.Cubic\312\002\022Cobaltspeech\\Cubic\342\002\036Cobaltspeech\\Cubic\\GPBMetadata\352\002\023Cobaltspeech::Cubic'
  _CUBIC.methods_by_name['Version']._options = None
  _CUBIC.methods_by_name['Version']._serialized_options = b'\202\323\344\223\002\016\022\014/api/version'
  _CUBIC.methods_by_name['ListModels']._options = None
  _CUBIC.methods_by_name['ListModels']._serialized_options = b'\202\323\344\223\002\021\022\017/api/listmodels'
  _CUBIC.methods_by_name['Recognize']._options = None
  _CUBIC.methods_by_name['Recognize']._serialized_options = b'\202\323\344\223\002\023\"\016/api/recognize:\001*'
  _CUBIC.methods_by_name['StreamingRecognize']._options = None
  _CUBIC.methods_by_name['StreamingRecognize']._serialized_options = b'\202\323\344\223\002\r\022\013/api/stream'
  _CUBIC.methods_by_name['CompileContext']._options = None
  _CUBIC.methods_by_name['CompileContext']._serialized_options = b'\202\323\344\223\002\030\"\023/api/compilecontext:\001*'
  _globals['_LISTMODELSREQUEST']._serialized_start=148
  _globals['_LISTMODELSREQUEST']._serialized_end=167
  _globals['_RECOGNIZEREQUEST']._serialized_start=170
  _globals['_RECOGNIZEREQUEST']._serialized_end=311
  _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_start=314
  _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_end=479
  _globals['_COMPILECONTEXTREQUEST']._serialized_start=482
  _globals['_COMPILECONTEXTREQUEST']._serialized_end=615
  _globals['_VERSIONRESPONSE']._serialized_start=617
  _globals['_VERSIONRESPONSE']._serialized_end=680
  _globals['_LISTMODELSRESPONSE']._serialized_start=682
  _globals['_LISTMODELSRESPONSE']._serialized_end=753
  _globals['_RECOGNITIONRESPONSE']._serialized_start=755
  _globals['_RECOGNITIONRESPONSE']._serialized_end=841
  _globals['_COMPILECONTEXTRESPONSE']._serialized_start=843
  _globals['_COMPILECONTEXTRESPONSE']._serialized_end=930
  _globals['_RECOGNITIONCONFIG']._serialized_start=933
  _globals['_RECOGNITIONCONFIG']._serialized_end=1632
  _globals['_RECOGNITIONCONFIG_ENCODING']._serialized_start=1525
  _globals['_RECOGNITIONCONFIG_ENCODING']._serialized_end=1632
  _globals['_RECOGNITIONMETADATA']._serialized_start=1634
  _globals['_RECOGNITIONMETADATA']._serialized_end=1696
  _globals['_RECOGNITIONCONTEXT']._serialized_start=1698
  _globals['_RECOGNITIONCONTEXT']._serialized_end=1783
  _globals['_COMPILEDCONTEXT']._serialized_start=1785
  _globals['_COMPILEDCONTEXT']._serialized_end=1822
  _globals['_CONTEXTPHRASE']._serialized_start=1824
  _globals['_CONTEXTPHRASE']._serialized_end=1881
  _globals['_RECOGNITIONAUDIO']._serialized_start=1883
  _globals['_RECOGNITIONAUDIO']._serialized_end=1921
  _globals['_MODEL']._serialized_start=1923
  _globals['_MODEL']._serialized_end=2035
  _globals['_MODELATTRIBUTES']._serialized_start=2037
  _globals['_MODELATTRIBUTES']._serialized_end=2155
  _globals['_CONTEXTINFO']._serialized_start=2157
  _globals['_CONTEXTINFO']._serialized_end=2267
  _globals['_RECOGNITIONRESULT']._serialized_start=2270
  _globals['_RECOGNITIONRESULT']._serialized_end=2506
  _globals['_RECOGNITIONALTERNATIVE']._serialized_start=2509
  _globals['_RECOGNITIONALTERNATIVE']._serialized_end=2860
  _globals['_WORDINFO']._serialized_start=2863
  _globals['_WORDINFO']._serialized_end=3038
  _globals['_RECOGNITIONCONFUSIONNETWORK']._serialized_start=3040
  _globals['_RECOGNITIONCONFUSIONNETWORK']._serialized_end=3133
  _globals['_CONFUSIONNETWORKLINK']._serialized_start=3136
  _globals['_CONFUSIONNETWORKLINK']._serialized_end=3332
  _globals['_CONFUSIONNETWORKARC']._serialized_start=3334
  _globals['_CONFUSIONNETWORKARC']._serialized_end=3407
  _globals['_CUBIC']._serialized_start=3410
  _globals['_CUBIC']._serialized_end=4022
# @@protoc_insertion_point(module_scope)
