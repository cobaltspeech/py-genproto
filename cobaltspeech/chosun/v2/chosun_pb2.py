# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cobaltspeech/chosun/v2/chosun.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cobaltspeech/chosun/v2/chosun.proto\x12\x16\x63obaltspeech.chosun.v2\"\x10\n\x0eVersionRequest\")\n\x0fVersionResponse\x12\x16\n\x06\x63hosun\x18\x01 \x01(\tR\x06\x63hosun\"\x13\n\x11ListModelsRequest\"\x94\x01\n\x12ListModelsResponse\x12\x43\n\x0b\x64omain_sets\x18\x01 \x03(\x0b\x32\".cobaltspeech.chosun.v2.DomainInfoR\ndomainSets\x12\x39\n\x06models\x18\x02 \x03(\x0b\x32!.cobaltspeech.chosun.v2.ModelInfoR\x06models\"\xb7\x01\n\nDomainInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12I\n\x07\x64omains\x18\x03 \x03(\x0b\x32/.cobaltspeech.chosun.v2.DomainInfo.DomainsEntryR\x07\x64omains\x1a:\n\x0c\x44omainsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"/\n\tModelInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xea\x03\n\x0cParseRequest\x12\x19\n\x08model_id\x18\x01 \x01(\tR\x07modelId\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x14\n\x04text\x18\x03 \x01(\tH\x00R\x04text\x12\x35\n\x05nbest\x18\x04 \x01(\x0b\x32\x1d.cobaltspeech.chosun.v2.NBestH\x00R\x05nbest\x12\x32\n\x04\x63net\x18\x05 \x01(\x0b\x32\x1c.cobaltspeech.chosun.v2.CNetH\x00R\x04\x63net\x12H\n\x0cnbest_tokens\x18\x06 \x01(\x0b\x32#.cobaltspeech.chosun.v2.NBestTokensH\x00R\x0bnbestTokens\x12\x64\n\x10\x63ontext_features\x18\x07 \x03(\x0b\x32\x39.cobaltspeech.chosun.v2.ParseRequest.ContextFeaturesEntryR\x0f\x63ontextFeatures\x12)\n\x10intent_whitelist\x18\x08 \x03(\tR\x0fintentWhitelist\x1a\x42\n\x14\x43ontextFeaturesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x02\x38\x01\x42\x07\n\x05query\"K\n\x05NBest\x12\x42\n\nhypotheses\x18\x01 \x03(\x0b\x32\".cobaltspeech.chosun.v2.HypothesisR\nhypotheses\"@\n\nHypothesis\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\"V\n\x0bNBestTokens\x12G\n\nhypotheses\x18\x01 \x03(\x0b\x32\'.cobaltspeech.chosun.v2.TokenHypothesisR\nhypotheses\"j\n\x0fTokenHypothesis\x12\x37\n\x06tokens\x18\x01 \x03(\x0b\x32\x1f.cobaltspeech.chosun.v2.CNetArcR\x06tokens\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\">\n\x04\x43Net\x12\x36\n\x05links\x18\x01 \x03(\x0b\x32 .cobaltspeech.chosun.v2.CNetLinkR\x05links\"?\n\x08\x43NetLink\x12\x33\n\x04\x61rcs\x18\x01 \x03(\x0b\x32\x1f.cobaltspeech.chosun.v2.CNetArcR\x04\x61rcs\"=\n\x07\x43NetArc\x12\x12\n\x04word\x18\x01 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\"I\n\rParseResponse\x12\x38\n\x07intents\x18\x01 \x03(\x0b\x32\x1e.cobaltspeech.chosun.v2.IntentR\x07intents\"\xa0\x01\n\x06Intent\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x1e\n\nconfidence\x18\x03 \x01(\x01R\nconfidence\x12:\n\x08\x65ntities\x18\x04 \x03(\x0b\x32\x1e.cobaltspeech.chosun.v2.EntityR\x08\x65ntities\x12\x12\n\x04text\x18\x05 \x01(\tR\x04text\"v\n\x06\x45ntity\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x14\n\x05start\x18\x03 \x01(\rR\x05start\x12\x10\n\x03\x65nd\x18\x04 \x01(\rR\x03\x65nd\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence2\xac\x02\n\rChosunService\x12\\\n\x07Version\x12&.cobaltspeech.chosun.v2.VersionRequest\x1a\'.cobaltspeech.chosun.v2.VersionResponse\"\x00\x12\x65\n\nListModels\x12).cobaltspeech.chosun.v2.ListModelsRequest\x1a*.cobaltspeech.chosun.v2.ListModelsResponse\"\x00\x12V\n\x05Parse\x12$.cobaltspeech.chosun.v2.ParseRequest\x1a%.cobaltspeech.chosun.v2.ParseResponse\"\x00\x42\xe8\x01\n\x1a\x63om.cobaltspeech.chosun.v2B\x0b\x43hosunProtoP\x01ZCgithub.com/cobaltspeech/go-genproto/cobaltspeech/chosun/v2;chosunv2\xa2\x02\x03\x43\x43X\xaa\x02\x16\x43obaltspeech.Chosun.V2\xca\x02\x16\x43obaltspeech\\Chosun\\V2\xe2\x02\"Cobaltspeech\\Chosun\\V2\\GPBMetadata\xea\x02\x18\x43obaltspeech::Chosun::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cobaltspeech.chosun.v2.chosun_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cobaltspeech.chosun.v2B\013ChosunProtoP\001ZCgithub.com/cobaltspeech/go-genproto/cobaltspeech/chosun/v2;chosunv2\242\002\003CCX\252\002\026Cobaltspeech.Chosun.V2\312\002\026Cobaltspeech\\Chosun\\V2\342\002\"Cobaltspeech\\Chosun\\V2\\GPBMetadata\352\002\030Cobaltspeech::Chosun::V2'
  _globals['_DOMAININFO_DOMAINSENTRY']._options = None
  _globals['_DOMAININFO_DOMAINSENTRY']._serialized_options = b'8\001'
  _globals['_PARSEREQUEST_CONTEXTFEATURESENTRY']._options = None
  _globals['_PARSEREQUEST_CONTEXTFEATURESENTRY']._serialized_options = b'8\001'
  _globals['_VERSIONREQUEST']._serialized_start=63
  _globals['_VERSIONREQUEST']._serialized_end=79
  _globals['_VERSIONRESPONSE']._serialized_start=81
  _globals['_VERSIONRESPONSE']._serialized_end=122
  _globals['_LISTMODELSREQUEST']._serialized_start=124
  _globals['_LISTMODELSREQUEST']._serialized_end=143
  _globals['_LISTMODELSRESPONSE']._serialized_start=146
  _globals['_LISTMODELSRESPONSE']._serialized_end=294
  _globals['_DOMAININFO']._serialized_start=297
  _globals['_DOMAININFO']._serialized_end=480
  _globals['_DOMAININFO_DOMAINSENTRY']._serialized_start=422
  _globals['_DOMAININFO_DOMAINSENTRY']._serialized_end=480
  _globals['_MODELINFO']._serialized_start=482
  _globals['_MODELINFO']._serialized_end=529
  _globals['_PARSEREQUEST']._serialized_start=532
  _globals['_PARSEREQUEST']._serialized_end=1022
  _globals['_PARSEREQUEST_CONTEXTFEATURESENTRY']._serialized_start=947
  _globals['_PARSEREQUEST_CONTEXTFEATURESENTRY']._serialized_end=1013
  _globals['_NBEST']._serialized_start=1024
  _globals['_NBEST']._serialized_end=1099
  _globals['_HYPOTHESIS']._serialized_start=1101
  _globals['_HYPOTHESIS']._serialized_end=1165
  _globals['_NBESTTOKENS']._serialized_start=1167
  _globals['_NBESTTOKENS']._serialized_end=1253
  _globals['_TOKENHYPOTHESIS']._serialized_start=1255
  _globals['_TOKENHYPOTHESIS']._serialized_end=1361
  _globals['_CNET']._serialized_start=1363
  _globals['_CNET']._serialized_end=1425
  _globals['_CNETLINK']._serialized_start=1427
  _globals['_CNETLINK']._serialized_end=1490
  _globals['_CNETARC']._serialized_start=1492
  _globals['_CNETARC']._serialized_end=1553
  _globals['_PARSERESPONSE']._serialized_start=1555
  _globals['_PARSERESPONSE']._serialized_end=1628
  _globals['_INTENT']._serialized_start=1631
  _globals['_INTENT']._serialized_end=1791
  _globals['_ENTITY']._serialized_start=1793
  _globals['_ENTITY']._serialized_end=1911
  _globals['_CHOSUNSERVICE']._serialized_start=1914
  _globals['_CHOSUNSERVICE']._serialized_end=2214
# @@protoc_insertion_point(module_scope)
