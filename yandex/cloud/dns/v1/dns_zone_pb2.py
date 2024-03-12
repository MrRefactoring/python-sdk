# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dns/v1/dns_zone.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"yandex/cloud/dns/v1/dns_zone.proto\x12\x13yandex.cloud.dns.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x95\x03\n\x07\x44nsZone\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x38\n\x06labels\x18\x06 \x03(\x0b\x32(.yandex.cloud.dns.v1.DnsZone.LabelsEntry\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12\x42\n\x12private_visibility\x18\x08 \x01(\x0b\x32&.yandex.cloud.dns.v1.PrivateVisibility\x12@\n\x11public_visibility\x18\t \x01(\x0b\x32%.yandex.cloud.dns.v1.PublicVisibility\x12\x1b\n\x13\x64\x65letion_protection\x18\n \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x81\x01\n\tRecordSet\x12\x17\n\x04name\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05\x31-254\x12\x16\n\x04type\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04\x31-20\x12\x1d\n\x03ttl\x18\x03 \x01(\x03\x42\x10\xfa\xc7\x31\x0c\x30-2147483647\x12$\n\x04\x64\x61ta\x18\x04 \x03(\tB\x16\x82\xc8\x31\x05\x31-100\x8a\xc8\x31\x05\x31-255\x90\xc8\x31\x01\"=\n\x11PrivateVisibility\x12(\n\x0bnetwork_ids\x18\x01 \x03(\tB\x13\x82\xc8\x31\x05\x30-100\x8a\xc8\x31\x02\x32\x30\x90\xc8\x31\x01\"\x12\n\x10PublicVisibilityBV\n\x17yandex.cloud.api.dns.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/dns/v1;dnsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dns.v1.dns_zone_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.dns.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/dns/v1;dns'
  _DNSZONE_LABELSENTRY._options = None
  _DNSZONE_LABELSENTRY._serialized_options = b'8\001'
  _RECORDSET.fields_by_name['name']._options = None
  _RECORDSET.fields_by_name['name']._serialized_options = b'\212\3101\0051-254'
  _RECORDSET.fields_by_name['type']._options = None
  _RECORDSET.fields_by_name['type']._serialized_options = b'\212\3101\0041-20'
  _RECORDSET.fields_by_name['ttl']._options = None
  _RECORDSET.fields_by_name['ttl']._serialized_options = b'\372\3071\0140-2147483647'
  _RECORDSET.fields_by_name['data']._options = None
  _RECORDSET.fields_by_name['data']._serialized_options = b'\202\3101\0051-100\212\3101\0051-255\220\3101\001'
  _PRIVATEVISIBILITY.fields_by_name['network_ids']._options = None
  _PRIVATEVISIBILITY.fields_by_name['network_ids']._serialized_options = b'\202\3101\0050-100\212\3101\00220\220\3101\001'
  _globals['_DNSZONE']._serialized_start=124
  _globals['_DNSZONE']._serialized_end=529
  _globals['_DNSZONE_LABELSENTRY']._serialized_start=484
  _globals['_DNSZONE_LABELSENTRY']._serialized_end=529
  _globals['_RECORDSET']._serialized_start=532
  _globals['_RECORDSET']._serialized_end=661
  _globals['_PRIVATEVISIBILITY']._serialized_start=663
  _globals['_PRIVATEVISIBILITY']._serialized_end=724
  _globals['_PUBLICVISIBILITY']._serialized_start=726
  _globals['_PUBLICVISIBILITY']._serialized_end=744
# @@protoc_insertion_point(module_scope)
