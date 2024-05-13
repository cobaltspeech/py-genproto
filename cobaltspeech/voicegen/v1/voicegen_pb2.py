# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/voicegen/v1/voicegen.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cobaltspeech/voicegen/v1/voicegen.proto\x12\x18\x63obaltspeech.voicegen.v1\"\x10\n\x0eVersionRequest\"+\n\x0fVersionResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\"\x13\n\x11ListModelsRequest\"Q\n\x12ListModelsResponse\x12;\n\x06models\x18\x01 \x03(\x0b\x32#.cobaltspeech.voicegen.v1.ModelInfoR\x06models\"\x9c\x01\n\x1aStreamingSynthesizeRequest\x12\x41\n\x06\x63onfig\x18\x01 \x01(\x0b\x32).cobaltspeech.voicegen.v1.SynthesisConfigR\x06\x63onfig\x12;\n\x04text\x18\x02 \x01(\x0b\x32\'.cobaltspeech.voicegen.v1.SynthesisTextR\x04text\"_\n\x1bStreamingSynthesizeResponse\x12@\n\x05\x61udio\x18\x01 \x01(\x0b\x32*.cobaltspeech.voicegen.v1.SynthesizedAudioR\x05\x61udio\"z\n\tModelInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12I\n\nattributes\x18\x03 \x01(\x0b\x32).cobaltspeech.voicegen.v1.ModelAttributesR\nattributes\"\xe0\x02\n\x0fModelAttributes\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12?\n\tphone_set\x18\x02 \x01(\x0e\x32\".cobaltspeech.voicegen.v1.PhoneSetR\x08phoneSet\x12U\n\x13native_audio_format\x18\x03 \x01(\x0b\x32%.cobaltspeech.voicegen.v1.AudioFormatR\x11nativeAudioFormat\x12V\n\x12supported_features\x18\x04 \x01(\x0b\x32\'.cobaltspeech.voicegen.v1.ModelFeaturesR\x11supportedFeatures\x12\x41\n\x08speakers\x18\x05 \x03(\x0b\x32%.cobaltspeech.voicegen.v1.SpeakerInfoR\x08speakers\"Y\n\rModelFeatures\x12\x1f\n\x0bspeech_rate\x18\x01 \x01(\x08R\nspeechRate\x12\'\n\x0fvariation_scale\x18\x02 \x01(\x08R\x0evariationScale\"\xa0\x01\n\x0bSpeakerInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12K\n\nattributes\x18\x04 \x01(\x0b\x32+.cobaltspeech.voicegen.v1.SpeakerAttributesR\nattributes\"/\n\x11SpeakerAttributes\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\"\xdf\x01\n\x0fSynthesisConfig\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x1d\n\nspeaker_id\x18\x02 \x01(\tR\tspeakerId\x12H\n\x0c\x61udio_format\x18\x03 \x01(\x0b\x32%.cobaltspeech.voicegen.v1.AudioFormatR\x0b\x61udioFormat\x12\x1f\n\x0bspeech_rate\x18\x04 \x01(\x02R\nspeechRate\x12\'\n\x0fvariation_scale\x18\x05 \x01(\x02R\x0evariationScale\"\xac\x02\n\x0b\x41udioFormat\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\rR\nsampleRate\x12\x1a\n\x08\x63hannels\x18\x02 \x01(\rR\x08\x63hannels\x12\x1b\n\tbit_depth\x18\x03 \x01(\rR\x08\x62itDepth\x12:\n\x05\x63odec\x18\x04 \x01(\x0e\x32$.cobaltspeech.voicegen.v1.AudioCodecR\x05\x63odec\x12\x43\n\x08\x65ncoding\x18\x05 \x01(\x0e\x32\'.cobaltspeech.voicegen.v1.AudioEncodingR\x08\x65ncoding\x12\x42\n\nbyte_order\x18\x06 \x01(\x0e\x32#.cobaltspeech.voicegen.v1.ByteOrderR\tbyteOrder\"#\n\rSynthesisText\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\"&\n\x10SynthesizedAudio\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta*e\n\x08PhoneSet\x12\x19\n\x15PHONE_SET_UNSPECIFIED\x10\x00\x12\x11\n\rPHONE_SET_IPA\x10\x01\x12\x14\n\x10PHONE_SET_XSAMPA\x10\x02\x12\x15\n\x11PHONE_SET_ARPABET\x10\x03*`\n\tByteOrder\x12\x1a\n\x16\x42YTE_ORDER_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x42YTE_ORDER_LITTLE_ENDIAN\x10\x01\x12\x19\n\x15\x42YTE_ORDER_BIG_ENDIAN\x10\x02*\xb8\x01\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41UDIO_ENCODING_SIGNED\x10\x01\x12\x1b\n\x17\x41UDIO_ENCODING_UNSIGNED\x10\x02\x12\x1d\n\x19\x41UDIO_ENCODING_IEEE_FLOAT\x10\x03\x12\x17\n\x13\x41UDIO_ENCODING_ULAW\x10\x04\x12\x17\n\x13\x41UDIO_ENCODING_ALAW\x10\x05*S\n\nAudioCodec\x12\x1b\n\x17\x41UDIO_CODEC_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x41UDIO_CODEC_RAW\x10\x02\x12\x13\n\x0f\x41UDIO_CODEC_WAV\x10\x01\x32\xe7\x02\n\x0fVoiceGenService\x12`\n\x07Version\x12(.cobaltspeech.voicegen.v1.VersionRequest\x1a).cobaltspeech.voicegen.v1.VersionResponse\"\x00\x12i\n\nListModels\x12+.cobaltspeech.voicegen.v1.ListModelsRequest\x1a,.cobaltspeech.voicegen.v1.ListModelsResponse\"\x00\x12\x86\x01\n\x13StreamingSynthesize\x12\x34.cobaltspeech.voicegen.v1.StreamingSynthesizeRequest\x1a\x35.cobaltspeech.voicegen.v1.StreamingSynthesizeResponse\"\x00\x30\x01\x42\xf8\x01\n\x1c\x63om.cobaltspeech.voicegen.v1B\rVoicegenProtoP\x01ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/voicegen/v1;voicegenv1\xa2\x02\x03\x43VX\xaa\x02\x18\x43obaltspeech.Voicegen.V1\xca\x02\x18\x43obaltspeech\\Voicegen\\V1\xe2\x02$Cobaltspeech\\Voicegen\\V1\\GPBMetadata\xea\x02\x1a\x43obaltspeech::Voicegen::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.voicegen.v1.voicegen_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.cobaltspeech.voicegen.v1B\rVoicegenProtoP\001ZGgithub.com/cobaltspeech/go-genproto/cobaltspeech/voicegen/v1;voicegenv1\242\002\003CVX\252\002\030Cobaltspeech.Voicegen.V1\312\002\030Cobaltspeech\\Voicegen\\V1\342\002$Cobaltspeech\\Voicegen\\V1\\GPBMetadata\352\002\032Cobaltspeech::Voicegen::V1'
  _globals['_PHONESET']._serialized_start=1880
  _globals['_PHONESET']._serialized_end=1981
  _globals['_BYTEORDER']._serialized_start=1983
  _globals['_BYTEORDER']._serialized_end=2079
  _globals['_AUDIOENCODING']._serialized_start=2082
  _globals['_AUDIOENCODING']._serialized_end=2266
  _globals['_AUDIOCODEC']._serialized_start=2268
  _globals['_AUDIOCODEC']._serialized_end=2351
  _globals['_VERSIONREQUEST']._serialized_start=69
  _globals['_VERSIONREQUEST']._serialized_end=85
  _globals['_VERSIONRESPONSE']._serialized_start=87
  _globals['_VERSIONRESPONSE']._serialized_end=130
  _globals['_LISTMODELSREQUEST']._serialized_start=132
  _globals['_LISTMODELSREQUEST']._serialized_end=151
  _globals['_LISTMODELSRESPONSE']._serialized_start=153
  _globals['_LISTMODELSRESPONSE']._serialized_end=234
  _globals['_STREAMINGSYNTHESIZEREQUEST']._serialized_start=237
  _globals['_STREAMINGSYNTHESIZEREQUEST']._serialized_end=393
  _globals['_STREAMINGSYNTHESIZERESPONSE']._serialized_start=395
  _globals['_STREAMINGSYNTHESIZERESPONSE']._serialized_end=490
  _globals['_MODELINFO']._serialized_start=492
  _globals['_MODELINFO']._serialized_end=614
  _globals['_MODELATTRIBUTES']._serialized_start=617
  _globals['_MODELATTRIBUTES']._serialized_end=969
  _globals['_MODELFEATURES']._serialized_start=971
  _globals['_MODELFEATURES']._serialized_end=1060
  _globals['_SPEAKERINFO']._serialized_start=1063
  _globals['_SPEAKERINFO']._serialized_end=1223
  _globals['_SPEAKERATTRIBUTES']._serialized_start=1225
  _globals['_SPEAKERATTRIBUTES']._serialized_end=1272
  _globals['_SYNTHESISCONFIG']._serialized_start=1275
  _globals['_SYNTHESISCONFIG']._serialized_end=1498
  _globals['_AUDIOFORMAT']._serialized_start=1501
  _globals['_AUDIOFORMAT']._serialized_end=1801
  _globals['_SYNTHESISTEXT']._serialized_start=1803
  _globals['_SYNTHESISTEXT']._serialized_end=1838
  _globals['_SYNTHESIZEDAUDIO']._serialized_start=1840
  _globals['_SYNTHESIZEDAUDIO']._serialized_end=1878
  _globals['_VOICEGENSERVICE']._serialized_start=2354
  _globals['_VOICEGENSERVICE']._serialized_end=2713
# @@protoc_insertion_point(module_scope)
