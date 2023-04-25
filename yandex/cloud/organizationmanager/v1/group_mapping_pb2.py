# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/group_mapping.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/group_mapping.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7yandex/cloud/organizationmanager/v1/group_mapping.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1dyandex/cloud/validation.proto\"f\n\x10GroupMappingItem\x12)\n\x11\x65xternal_group_id\x18\x01 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1000\x12\'\n\x11internal_group_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x0cGroupMapping\x12\x15\n\rfederation_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x42\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GROUPMAPPINGITEM = _descriptor.Descriptor(
  name='GroupMappingItem',
  full_name='yandex.cloud.organizationmanager.v1.GroupMappingItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='external_group_id', full_name='yandex.cloud.organizationmanager.v1.GroupMappingItem.external_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='internal_group_id', full_name='yandex.cloud.organizationmanager.v1.GroupMappingItem.internal_group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=229,
)


_GROUPMAPPING = _descriptor.Descriptor(
  name='GroupMapping',
  full_name='yandex.cloud.organizationmanager.v1.GroupMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.organizationmanager.v1.GroupMapping.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.organizationmanager.v1.GroupMapping.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=285,
)

DESCRIPTOR.message_types_by_name['GroupMappingItem'] = _GROUPMAPPINGITEM
DESCRIPTOR.message_types_by_name['GroupMapping'] = _GROUPMAPPING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GroupMappingItem = _reflection.GeneratedProtocolMessageType('GroupMappingItem', (_message.Message,), {
  'DESCRIPTOR' : _GROUPMAPPINGITEM,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GroupMappingItem)
  })
_sym_db.RegisterMessage(GroupMappingItem)

GroupMapping = _reflection.GeneratedProtocolMessageType('GroupMapping', (_message.Message,), {
  'DESCRIPTOR' : _GROUPMAPPING,
  '__module__' : 'yandex.cloud.organizationmanager.v1.group_mapping_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.GroupMapping)
  })
_sym_db.RegisterMessage(GroupMapping)


DESCRIPTOR._options = None
_GROUPMAPPINGITEM.fields_by_name['external_group_id']._options = None
_GROUPMAPPINGITEM.fields_by_name['internal_group_id']._options = None
# @@protoc_insertion_point(module_scope)