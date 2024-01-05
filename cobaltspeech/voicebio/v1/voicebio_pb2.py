# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/voicebio/v1/voicebio.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cobaltspeech/voicebio/v1/voicebio.proto\x12\x18\x63obaltspeech.voicebio.v1\"\x10\n\x0eVersionRequest\"+\n\x0fVersionResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\"\x13\n\x11ListModelsRequest\"M\n\x12ListModelsResponse\x12\x37\n\x06models\x18\x01 \x03(\x0b\x32\x1f.cobaltspeech.voicebio.v1.ModelR\x06models\"\xa2\x01\n\x16StreamingEnrollRequest\x12\x44\n\x06\x63onfig\x18\x01 \x01(\x0b\x32*.cobaltspeech.voicebio.v1.EnrollmentConfigH\x00R\x06\x63onfig\x12\x37\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1f.cobaltspeech.voicebio.v1.AudioH\x00R\x05\x61udioB\t\n\x07request\"\xb8\x01\n\x17StreamingEnrollResponse\x12\x44\n\nvoiceprint\x18\x01 \x01(\x0b\x32$.cobaltspeech.voicebio.v1.VoiceprintR\nvoiceprint\x12W\n\x11\x65nrollment_status\x18\x02 \x01(\x0b\x32*.cobaltspeech.voicebio.v1.EnrollmentStatusR\x10\x65nrollmentStatus\"\xce\x01\n\x10\x45nrollmentConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12H\n\x0c\x61udio_format\x18\x02 \x01(\x0b\x32%.cobaltspeech.voicebio.v1.AudioFormatR\x0b\x61udioFormat\x12U\n\x13previous_voiceprint\x18\x03 \x01(\x0b\x32$.cobaltspeech.voicebio.v1.VoiceprintR\x12previousVoiceprint\"\x8e\x01\n\x10\x45nrollmentStatus\x12/\n\x13\x65nrollment_complete\x18\x01 \x01(\x08R\x12\x65nrollmentComplete\x12I\n!additional_audio_required_seconds\x18\x02 \x01(\rR\x1e\x61\x64\x64itionalAudioRequiredSeconds\"\xa4\x01\n\x16StreamingVerifyRequest\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32,.cobaltspeech.voicebio.v1.VerificationConfigH\x00R\x06\x63onfig\x12\x37\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1f.cobaltspeech.voicebio.v1.AudioH\x00R\x05\x61udioB\t\n\x07request\"g\n\x17StreamingVerifyResponse\x12L\n\x06result\x18\x01 \x01(\x0b\x32\x34.cobaltspeech.voicebio.v1.VoiceprintComparisonResultR\x06result\"b\n\x1aVoiceprintComparisonResult\x12\x19\n\x08is_match\x18\x01 \x01(\x08R\x07isMatch\x12)\n\x10similarity_score\x18\x02 \x01(\x02R\x0fsimilarityScore\"\xbf\x01\n\x12VerificationConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12H\n\x0c\x61udio_format\x18\x02 \x01(\x0b\x32%.cobaltspeech.voicebio.v1.AudioFormatR\x0b\x61udioFormat\x12\x44\n\nvoiceprint\x18\x03 \x01(\x0b\x32$.cobaltspeech.voicebio.v1.VoiceprintR\nvoiceprint\"\xa8\x01\n\x18StreamingIdentifyRequest\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32..cobaltspeech.voicebio.v1.IdentificationConfigH\x00R\x06\x63onfig\x12\x37\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1f.cobaltspeech.voicebio.v1.AudioH\x00R\x05\x61udioB\t\n\x07request\"\xbf\x01\n\x19StreamingIdentifyResponse\x12(\n\x10\x62\x65st_match_index\x18\x01 \x01(\x05R\x0e\x62\x65stMatchIndex\x12x\n\x1dvoiceprint_comparison_results\x18\x02 \x03(\x0b\x32\x34.cobaltspeech.voicebio.v1.VoiceprintComparisonResultR\x1bvoiceprintComparisonResults\"\xc3\x01\n\x14IdentificationConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12H\n\x0c\x61udio_format\x18\x02 \x01(\x0b\x32%.cobaltspeech.voicebio.v1.AudioFormatR\x0b\x61udioFormat\x12\x46\n\x0bvoiceprints\x18\x03 \x03(\x0b\x32$.cobaltspeech.voicebio.v1.VoiceprintR\x0bvoiceprints\" \n\nVoiceprint\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\"\xd8\x01\n\x0b\x41udioFormat\x12T\n\x10\x61udio_format_raw\x18\x02 \x01(\x0b\x32(.cobaltspeech.voicebio.v1.AudioFormatRAWH\x00R\x0e\x61udioFormatRaw\x12\x63\n\x15\x61udio_format_headered\x18\x03 \x01(\x0e\x32-.cobaltspeech.voicebio.v1.AudioFormatHeaderedH\x00R\x13\x61udioFormatHeaderedB\x0e\n\x0c\x61udio_format\"\xf3\x01\n\x0e\x41udioFormatRAW\x12\x43\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32\'.cobaltspeech.voicebio.v1.AudioEncodingR\x08\x65ncoding\x12\x1b\n\tbit_depth\x18\x02 \x01(\rR\x08\x62itDepth\x12\x42\n\nbyte_order\x18\x03 \x01(\x0e\x32#.cobaltspeech.voicebio.v1.ByteOrderR\tbyteOrder\x12\x1f\n\x0bsample_rate\x18\x04 \x01(\rR\nsampleRate\x12\x1a\n\x08\x63hannels\x18\x05 \x01(\rR\x08\x63hannels\"\x1b\n\x05\x41udio\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"v\n\x05Model\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12I\n\nattributes\x18\x03 \x01(\x0b\x32).cobaltspeech.voicebio.v1.ModelAttributesR\nattributes\"2\n\x0fModelAttributes\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\rR\nsampleRate*`\n\tByteOrder\x12\x1a\n\x16\x42YTE_ORDER_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x42YTE_ORDER_LITTLE_ENDIAN\x10\x01\x12\x19\n\x15\x42YTE_ORDER_BIG_ENDIAN\x10\x02*\xb8\x01\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41UDIO_ENCODING_SIGNED\x10\x01\x12\x1b\n\x17\x41UDIO_ENCODING_UNSIGNED\x10\x02\x12\x1d\n\x19\x41UDIO_ENCODING_IEEE_FLOAT\x10\x03\x12\x17\n\x13\x41UDIO_ENCODING_ULAW\x10\x04\x12\x17\n\x13\x41UDIO_ENCODING_ALAW\x10\x05*\xbe\x01\n\x13\x41udioFormatHeadered\x12%\n!AUDIO_FORMAT_HEADERED_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x41UDIO_FORMAT_HEADERED_WAV\x10\x01\x12\x1d\n\x19\x41UDIO_FORMAT_HEADERED_MP3\x10\x02\x12\x1e\n\x1a\x41UDIO_FORMAT_HEADERED_FLAC\x10\x03\x12\"\n\x1e\x41UDIO_FORMAT_HEADERED_OGG_OPUS\x10\x04\x32\xd9\x04\n\x0fVoiceBioService\x12`\n\x07Version\x12(.cobaltspeech.voicebio.v1.VersionRequest\x1a).cobaltspeech.voicebio.v1.VersionResponse\"\x00\x12i\n\nListModels\x12+.cobaltspeech.voicebio.v1.ListModelsRequest\x1a,.cobaltspeech.voicebio.v1.ListModelsResponse\"\x00\x12z\n\x0fStreamingEnroll\x12\x30.cobaltspeech.voicebio.v1.StreamingEnrollRequest\x1a\x31.cobaltspeech.voicebio.v1.StreamingEnrollResponse\"\x00(\x01\x12z\n\x0fStreamingVerify\x12\x30.cobaltspeech.voicebio.v1.StreamingVerifyRequest\x1a\x31.cobaltspeech.voicebio.v1.StreamingVerifyResponse\"\x00(\x01\x12\x80\x01\n\x11StreamingIdentify\x12\x32.cobaltspeech.voicebio.v1.StreamingIdentifyRequest\x1a\x33.cobaltspeech.voicebio.v1.StreamingIdentifyResponse\"\x00(\x01\x42\xf8\x01\n\x1c\x63om.cobaltspeech.voicebio.v1B\rVoicebioProtoP\x01ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/voicebio/v1;voicebiov1\xa2\x02\x03\x43VX\xaa\x02\x18\x43obaltspeech.Voicebio.V1\xca\x02\x18\x43obaltspeech\\Voicebio\\V1\xe2\x02$Cobaltspeech\\Voicebio\\V1\\GPBMetadata\xea\x02\x1a\x43obaltspeech::Voicebio::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.voicebio.v1.voicebio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.cobaltspeech.voicebio.v1B\rVoicebioProtoP\001ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/voicebio/v1;voicebiov1\242\002\003CVX\252\002\030Cobaltspeech.Voicebio.V1\312\002\030Cobaltspeech\\Voicebio\\V1\342\002$Cobaltspeech\\Voicebio\\V1\\GPBMetadata\352\002\032Cobaltspeech::Voicebio::V1'
  _globals['_BYTEORDER']._serialized_start=2767
  _globals['_BYTEORDER']._serialized_end=2863
  _globals['_AUDIOENCODING']._serialized_start=2866
  _globals['_AUDIOENCODING']._serialized_end=3050
  _globals['_AUDIOFORMATHEADERED']._serialized_start=3053
  _globals['_AUDIOFORMATHEADERED']._serialized_end=3243
  _globals['_VERSIONREQUEST']._serialized_start=69
  _globals['_VERSIONREQUEST']._serialized_end=85
  _globals['_VERSIONRESPONSE']._serialized_start=87
  _globals['_VERSIONRESPONSE']._serialized_end=130
  _globals['_LISTMODELSREQUEST']._serialized_start=132
  _globals['_LISTMODELSREQUEST']._serialized_end=151
  _globals['_LISTMODELSRESPONSE']._serialized_start=153
  _globals['_LISTMODELSRESPONSE']._serialized_end=230
  _globals['_STREAMINGENROLLREQUEST']._serialized_start=233
  _globals['_STREAMINGENROLLREQUEST']._serialized_end=395
  _globals['_STREAMINGENROLLRESPONSE']._serialized_start=398
  _globals['_STREAMINGENROLLRESPONSE']._serialized_end=582
  _globals['_ENROLLMENTCONFIG']._serialized_start=585
  _globals['_ENROLLMENTCONFIG']._serialized_end=791
  _globals['_ENROLLMENTSTATUS']._serialized_start=794
  _globals['_ENROLLMENTSTATUS']._serialized_end=936
  _globals['_STREAMINGVERIFYREQUEST']._serialized_start=939
  _globals['_STREAMINGVERIFYREQUEST']._serialized_end=1103
  _globals['_STREAMINGVERIFYRESPONSE']._serialized_start=1105
  _globals['_STREAMINGVERIFYRESPONSE']._serialized_end=1208
  _globals['_VOICEPRINTCOMPARISONRESULT']._serialized_start=1210
  _globals['_VOICEPRINTCOMPARISONRESULT']._serialized_end=1308
  _globals['_VERIFICATIONCONFIG']._serialized_start=1311
  _globals['_VERIFICATIONCONFIG']._serialized_end=1502
  _globals['_STREAMINGIDENTIFYREQUEST']._serialized_start=1505
  _globals['_STREAMINGIDENTIFYREQUEST']._serialized_end=1673
  _globals['_STREAMINGIDENTIFYRESPONSE']._serialized_start=1676
  _globals['_STREAMINGIDENTIFYRESPONSE']._serialized_end=1867
  _globals['_IDENTIFICATIONCONFIG']._serialized_start=1870
  _globals['_IDENTIFICATIONCONFIG']._serialized_end=2065
  _globals['_VOICEPRINT']._serialized_start=2067
  _globals['_VOICEPRINT']._serialized_end=2099
  _globals['_AUDIOFORMAT']._serialized_start=2102
  _globals['_AUDIOFORMAT']._serialized_end=2318
  _globals['_AUDIOFORMATRAW']._serialized_start=2321
  _globals['_AUDIOFORMATRAW']._serialized_end=2564
  _globals['_AUDIO']._serialized_start=2566
  _globals['_AUDIO']._serialized_end=2593
  _globals['_MODEL']._serialized_start=2595
  _globals['_MODEL']._serialized_end=2713
  _globals['_MODELATTRIBUTES']._serialized_start=2715
  _globals['_MODELATTRIBUTES']._serialized_end=2765
  _globals['_VOICEBIOSERVICE']._serialized_start=3246
  _globals['_VOICEBIOSERVICE']._serialized_end=3847
# @@protoc_insertion_point(module_scope)
