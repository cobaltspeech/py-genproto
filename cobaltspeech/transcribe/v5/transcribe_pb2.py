# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cobaltspeech/transcribe/v5/transcribe.proto
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
    'cobaltspeech/transcribe/v5/transcribe.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+cobaltspeech/transcribe/v5/transcribe.proto\x12\x1a\x63obaltspeech.transcribe.v5\"\x10\n\x0eVersionRequest\"+\n\x0fVersionResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\"\x13\n\x11ListModelsRequest\"O\n\x12ListModelsResponse\x12\x39\n\x06models\x18\x01 \x03(\x0b\x32!.cobaltspeech.transcribe.v5.ModelR\x06models\"\xb5\x01\n\x19StreamingRecognizeRequest\x12G\n\x06\x63onfig\x18\x01 \x01(\x0b\x32-.cobaltspeech.transcribe.v5.RecognitionConfigH\x00R\x06\x63onfig\x12\x44\n\x05\x61udio\x18\x02 \x01(\x0b\x32,.cobaltspeech.transcribe.v5.RecognitionAudioH\x00R\x05\x61udioB\t\n\x07request\"\xa7\x01\n\x1aStreamingRecognizeResponse\x12\x45\n\x06result\x18\x01 \x01(\x0b\x32-.cobaltspeech.transcribe.v5.RecognitionResultR\x06result\x12\x42\n\x05\x65rror\x18\x02 \x01(\x0b\x32,.cobaltspeech.transcribe.v5.RecognitionErrorR\x05\x65rror\"\x8d\x01\n\x15\x43ompileContextRequest\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\x12\x43\n\x07phrases\x18\x03 \x03(\x0b\x32).cobaltspeech.transcribe.v5.ContextPhraseR\x07phrases\"_\n\x16\x43ompileContextResponse\x12\x45\n\x07\x63ontext\x18\x01 \x01(\x0b\x32+.cobaltspeech.transcribe.v5.CompiledContextR\x07\x63ontext\"\xe7\x04\n\x11RecognitionConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12V\n\x10\x61udio_format_raw\x18\x02 \x01(\x0b\x32*.cobaltspeech.transcribe.v5.AudioFormatRAWH\x00R\x0e\x61udioFormatRaw\x12\x65\n\x15\x61udio_format_headered\x18\x03 \x01(\x0e\x32/.cobaltspeech.transcribe.v5.AudioFormatHeaderedH\x00R\x13\x61udioFormatHeadered\x12\x36\n\x17selected_audio_channels\x18\x04 \x03(\rR\x15selectedAudioChannels\x12/\n\x14\x61udio_time_offset_ms\x18\x05 \x01(\x04R\x11\x61udioTimeOffsetMs\x12.\n\x13\x65nable_word_details\x18\x06 \x01(\x08R\x11\x65nableWordDetails\x12\x38\n\x18\x65nable_confusion_network\x18\x07 \x01(\x08R\x16\x65nableConfusionNetwork\x12K\n\x08metadata\x18\x08 \x01(\x0b\x32/.cobaltspeech.transcribe.v5.RecognitionMetadataR\x08metadata\x12H\n\x07\x63ontext\x18\t \x01(\x0b\x32..cobaltspeech.transcribe.v5.RecognitionContextR\x07\x63ontextB\x0e\n\x0c\x61udio_format\"\xf7\x01\n\x0e\x41udioFormatRAW\x12\x45\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32).cobaltspeech.transcribe.v5.AudioEncodingR\x08\x65ncoding\x12\x1b\n\tbit_depth\x18\x02 \x01(\rR\x08\x62itDepth\x12\x44\n\nbyte_order\x18\x03 \x01(\x0e\x32%.cobaltspeech.transcribe.v5.ByteOrderR\tbyteOrder\x12\x1f\n\x0bsample_rate\x18\x04 \x01(\rR\nsampleRate\x12\x1a\n\x08\x63hannels\x18\x05 \x01(\rR\x08\x63hannels\"[\n\x13RecognitionMetadata\x12\'\n\x0f\x63ustom_metadata\x18\x01 \x01(\tR\x0e\x63ustomMetadata\x12\x1b\n\tcustom_id\x18\x02 \x01(\tR\x08\x63ustomId\"]\n\x12RecognitionContext\x12G\n\x08\x63ompiled\x18\x01 \x03(\x0b\x32+.cobaltspeech.transcribe.v5.CompiledContextR\x08\x63ompiled\"%\n\x0f\x43ompiledContext\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"9\n\rContextPhrase\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x14\n\x05\x62oost\x18\x02 \x01(\x02R\x05\x62oost\"&\n\x10RecognitionAudio\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"x\n\x05Model\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12K\n\nattributes\x18\x03 \x01(\x0b\x32+.cobaltspeech.transcribe.v5.ModelAttributesR\nattributes\"\xb4\x01\n\x0fModelAttributes\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\rR\nsampleRate\x12J\n\x0c\x63ontext_info\x18\x02 \x01(\x0b\x32\'.cobaltspeech.transcribe.v5.ContextInfoR\x0b\x63ontextInfo\x12\x34\n\x16supported_sample_rates\x18\x03 \x03(\rR\x14supportedSampleRates\"n\n\x0b\x43ontextInfo\x12)\n\x10supports_context\x18\x01 \x01(\x08R\x0fsupportsContext\x12\x34\n\x16\x61llowed_context_tokens\x18\x02 \x03(\tR\x14\x61llowedContextTokens\"\xfc\x01\n\x11RecognitionResult\x12V\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x32.cobaltspeech.transcribe.v5.RecognitionAlternativeR\x0c\x61lternatives\x12\x1d\n\nis_partial\x18\x02 \x01(\x08R\tisPartial\x12K\n\x04\x63net\x18\x03 \x01(\x0b\x32\x37.cobaltspeech.transcribe.v5.RecognitionConfusionNetworkR\x04\x63net\x12#\n\raudio_channel\x18\x04 \x01(\rR\x0c\x61udioChannel\",\n\x10RecognitionError\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\"\xa3\x02\n\x16RecognitionAlternative\x12\x31\n\x14transcript_formatted\x18\x01 \x01(\tR\x13transcriptFormatted\x12%\n\x0etranscript_raw\x18\x02 \x01(\tR\rtranscriptRaw\x12\"\n\rstart_time_ms\x18\x03 \x01(\x04R\x0bstartTimeMs\x12\x1f\n\x0b\x64uration_ms\x18\x04 \x01(\x04R\ndurationMs\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12J\n\x0cword_details\x18\x06 \x01(\x0b\x32\'.cobaltspeech.transcribe.v5.WordDetailsR\x0bwordDetails\"\x89\x01\n\x0bWordDetails\x12\x42\n\tformatted\x18\x01 \x03(\x0b\x32$.cobaltspeech.transcribe.v5.WordInfoR\tformatted\x12\x36\n\x03raw\x18\x02 \x03(\x0b\x32$.cobaltspeech.transcribe.v5.WordInfoR\x03raw\"\x83\x01\n\x08WordInfo\x12\x12\n\x04word\x18\x01 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12\"\n\rstart_time_ms\x18\x03 \x01(\x04R\x0bstartTimeMs\x12\x1f\n\x0b\x64uration_ms\x18\x04 \x01(\x04R\ndurationMs\"e\n\x1bRecognitionConfusionNetwork\x12\x46\n\x05links\x18\x01 \x03(\x0b\x32\x30.cobaltspeech.transcribe.v5.ConfusionNetworkLinkR\x05links\"\xa0\x01\n\x14\x43onfusionNetworkLink\x12\"\n\rstart_time_ms\x18\x01 \x01(\x04R\x0bstartTimeMs\x12\x1f\n\x0b\x64uration_ms\x18\x02 \x01(\x04R\ndurationMs\x12\x43\n\x04\x61rcs\x18\x03 \x03(\x0b\x32/.cobaltspeech.transcribe.v5.ConfusionNetworkArcR\x04\x61rcs\"\x9e\x01\n\x13\x43onfusionNetworkArc\x12\x12\n\x04word\x18\x01 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence\x12S\n\x08\x66\x65\x61tures\x18\x03 \x01(\x0b\x32\x37.cobaltspeech.transcribe.v5.ConfusionNetworkArcFeaturesR\x08\x66\x65\x61tures\"\xc5\x01\n\x1b\x43onfusionNetworkArcFeatures\x12g\n\nconfidence\x18\x01 \x03(\x0b\x32G.cobaltspeech.transcribe.v5.ConfusionNetworkArcFeatures.ConfidenceEntryR\nconfidence\x1a=\n\x0f\x43onfidenceEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01*`\n\tByteOrder\x12\x1a\n\x16\x42YTE_ORDER_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x42YTE_ORDER_LITTLE_ENDIAN\x10\x01\x12\x19\n\x15\x42YTE_ORDER_BIG_ENDIAN\x10\x02*\xb8\x01\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41UDIO_ENCODING_SIGNED\x10\x01\x12\x1b\n\x17\x41UDIO_ENCODING_UNSIGNED\x10\x02\x12\x1d\n\x19\x41UDIO_ENCODING_IEEE_FLOAT\x10\x03\x12\x17\n\x13\x41UDIO_ENCODING_ULAW\x10\x04\x12\x17\n\x13\x41UDIO_ENCODING_ALAW\x10\x05*\xbe\x01\n\x13\x41udioFormatHeadered\x12%\n!AUDIO_FORMAT_HEADERED_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x41UDIO_FORMAT_HEADERED_WAV\x10\x01\x12\x1d\n\x19\x41UDIO_FORMAT_HEADERED_MP3\x10\x02\x12\x1e\n\x1a\x41UDIO_FORMAT_HEADERED_FLAC\x10\x03\x12\"\n\x1e\x41UDIO_FORMAT_HEADERED_OGG_OPUS\x10\x04\x32\xef\x03\n\x11TranscribeService\x12\x64\n\x07Version\x12*.cobaltspeech.transcribe.v5.VersionRequest\x1a+.cobaltspeech.transcribe.v5.VersionResponse\"\x00\x12m\n\nListModels\x12-.cobaltspeech.transcribe.v5.ListModelsRequest\x1a..cobaltspeech.transcribe.v5.ListModelsResponse\"\x00\x12\x89\x01\n\x12StreamingRecognize\x12\x35.cobaltspeech.transcribe.v5.StreamingRecognizeRequest\x1a\x36.cobaltspeech.transcribe.v5.StreamingRecognizeResponse\"\x00(\x01\x30\x01\x12y\n\x0e\x43ompileContext\x12\x31.cobaltspeech.transcribe.v5.CompileContextRequest\x1a\x32.cobaltspeech.transcribe.v5.CompileContextResponse\"\x00\x42\x88\x02\n\x1e\x63om.cobaltspeech.transcribe.v5B\x0fTranscribeProtoP\x01ZKgithub.com/cobaltspeech/go-genproto/cobaltspeech/transcribe/v5;transcribev5\xa2\x02\x03\x43TX\xaa\x02\x1a\x43obaltspeech.Transcribe.V5\xca\x02\x1a\x43obaltspeech\\Transcribe\\V5\xe2\x02&Cobaltspeech\\Transcribe\\V5\\GPBMetadata\xea\x02\x1c\x43obaltspeech::Transcribe::V5b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.transcribe.v5.transcribe_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.cobaltspeech.transcribe.v5B\017TranscribeProtoP\001ZKgithub.com/cobaltspeech/go-genproto/cobaltspeech/transcribe/v5;transcribev5\242\002\003CTX\252\002\032Cobaltspeech.Transcribe.V5\312\002\032Cobaltspeech\\Transcribe\\V5\342\002&Cobaltspeech\\Transcribe\\V5\\GPBMetadata\352\002\034Cobaltspeech::Transcribe::V5'
  _globals['_CONFUSIONNETWORKARCFEATURES_CONFIDENCEENTRY']._loaded_options = None
  _globals['_CONFUSIONNETWORKARCFEATURES_CONFIDENCEENTRY']._serialized_options = b'8\001'
  _globals['_BYTEORDER']._serialized_start=3942
  _globals['_BYTEORDER']._serialized_end=4038
  _globals['_AUDIOENCODING']._serialized_start=4041
  _globals['_AUDIOENCODING']._serialized_end=4225
  _globals['_AUDIOFORMATHEADERED']._serialized_start=4228
  _globals['_AUDIOFORMATHEADERED']._serialized_end=4418
  _globals['_VERSIONREQUEST']._serialized_start=75
  _globals['_VERSIONREQUEST']._serialized_end=91
  _globals['_VERSIONRESPONSE']._serialized_start=93
  _globals['_VERSIONRESPONSE']._serialized_end=136
  _globals['_LISTMODELSREQUEST']._serialized_start=138
  _globals['_LISTMODELSREQUEST']._serialized_end=157
  _globals['_LISTMODELSRESPONSE']._serialized_start=159
  _globals['_LISTMODELSRESPONSE']._serialized_end=238
  _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_start=241
  _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_end=422
  _globals['_STREAMINGRECOGNIZERESPONSE']._serialized_start=425
  _globals['_STREAMINGRECOGNIZERESPONSE']._serialized_end=592
  _globals['_COMPILECONTEXTREQUEST']._serialized_start=595
  _globals['_COMPILECONTEXTREQUEST']._serialized_end=736
  _globals['_COMPILECONTEXTRESPONSE']._serialized_start=738
  _globals['_COMPILECONTEXTRESPONSE']._serialized_end=833
  _globals['_RECOGNITIONCONFIG']._serialized_start=836
  _globals['_RECOGNITIONCONFIG']._serialized_end=1451
  _globals['_AUDIOFORMATRAW']._serialized_start=1454
  _globals['_AUDIOFORMATRAW']._serialized_end=1701
  _globals['_RECOGNITIONMETADATA']._serialized_start=1703
  _globals['_RECOGNITIONMETADATA']._serialized_end=1794
  _globals['_RECOGNITIONCONTEXT']._serialized_start=1796
  _globals['_RECOGNITIONCONTEXT']._serialized_end=1889
  _globals['_COMPILEDCONTEXT']._serialized_start=1891
  _globals['_COMPILEDCONTEXT']._serialized_end=1928
  _globals['_CONTEXTPHRASE']._serialized_start=1930
  _globals['_CONTEXTPHRASE']._serialized_end=1987
  _globals['_RECOGNITIONAUDIO']._serialized_start=1989
  _globals['_RECOGNITIONAUDIO']._serialized_end=2027
  _globals['_MODEL']._serialized_start=2029
  _globals['_MODEL']._serialized_end=2149
  _globals['_MODELATTRIBUTES']._serialized_start=2152
  _globals['_MODELATTRIBUTES']._serialized_end=2332
  _globals['_CONTEXTINFO']._serialized_start=2334
  _globals['_CONTEXTINFO']._serialized_end=2444
  _globals['_RECOGNITIONRESULT']._serialized_start=2447
  _globals['_RECOGNITIONRESULT']._serialized_end=2699
  _globals['_RECOGNITIONERROR']._serialized_start=2701
  _globals['_RECOGNITIONERROR']._serialized_end=2745
  _globals['_RECOGNITIONALTERNATIVE']._serialized_start=2748
  _globals['_RECOGNITIONALTERNATIVE']._serialized_end=3039
  _globals['_WORDDETAILS']._serialized_start=3042
  _globals['_WORDDETAILS']._serialized_end=3179
  _globals['_WORDINFO']._serialized_start=3182
  _globals['_WORDINFO']._serialized_end=3313
  _globals['_RECOGNITIONCONFUSIONNETWORK']._serialized_start=3315
  _globals['_RECOGNITIONCONFUSIONNETWORK']._serialized_end=3416
  _globals['_CONFUSIONNETWORKLINK']._serialized_start=3419
  _globals['_CONFUSIONNETWORKLINK']._serialized_end=3579
  _globals['_CONFUSIONNETWORKARC']._serialized_start=3582
  _globals['_CONFUSIONNETWORKARC']._serialized_end=3740
  _globals['_CONFUSIONNETWORKARCFEATURES']._serialized_start=3743
  _globals['_CONFUSIONNETWORKARCFEATURES']._serialized_end=3940
  _globals['_CONFUSIONNETWORKARCFEATURES_CONFIDENCEENTRY']._serialized_start=3879
  _globals['_CONFUSIONNETWORKARCFEATURES_CONFIDENCEENTRY']._serialized_end=3940
  _globals['_TRANSCRIBESERVICE']._serialized_start=4421
  _globals['_TRANSCRIBESERVICE']._serialized_end=4916
# @@protoc_insertion_point(module_scope)
