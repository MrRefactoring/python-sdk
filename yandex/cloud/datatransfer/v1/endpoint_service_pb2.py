# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.datatransfer.v1 import endpoint_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint_service.proto',
  package='yandex.cloud.datatransfer.v1',
  syntax='proto3',
  serialized_options=b'\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransfer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3yandex/cloud/datatransfer/v1/endpoint_service.proto\x12\x1cyandex.cloud.datatransfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a+yandex/cloud/datatransfer/v1/endpoint.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\")\n\x12GetEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"P\n\x14ListEndpointsRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"k\n\x15ListEndpointsResponse\x12\x39\n\tendpoints\x18\x01 \x03(\x0b\x32&.yandex.cloud.datatransfer.v1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8f\x02\n\x15\x43reateEndpointRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12O\n\x06labels\x18\x04 \x03(\x0b\x32?.yandex.cloud.datatransfer.v1.CreateEndpointRequest.LabelsEntry\x12@\n\x08settings\x18\x34 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.EndpointSettings\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x16\x43reateEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"\xc2\x02\n\x15UpdateEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\n \x01(\t\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12O\n\x06labels\x18\r \x03(\x0b\x32?.yandex.cloud.datatransfer.v1.UpdateEndpointRequest.LabelsEntry\x12@\n\x08settings\x18\x34 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.EndpointSettings\x12/\n\x0bupdate_mask\x18< \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x16UpdateEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\",\n\x15\x44\x65leteEndpointRequest\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t\"-\n\x16\x44\x65leteEndpointMetadata\x12\x13\n\x0b\x65ndpoint_id\x18\x01 \x01(\t2\xbd\x06\n\x0f\x45ndpointService\x12\x83\x01\n\x03Get\x12\x30.yandex.cloud.datatransfer.v1.GetEndpointRequest\x1a&.yandex.cloud.datatransfer.v1.Endpoint\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/endpoint/{endpoint_id}\x12\x97\x01\n\x04List\x12\x32.yandex.cloud.datatransfer.v1.ListEndpointsRequest\x1a\x33.yandex.cloud.datatransfer.v1.ListEndpointsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/endpoints/list/{folder_id}\x12\x9f\x01\n\x06\x43reate\x12\x33.yandex.cloud.datatransfer.v1.CreateEndpointRequest\x1a!.yandex.cloud.operation.Operation\"=\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/endpoint:\x01*\xb2\xd2*\"\n\x16\x43reateEndpointMetadata\x12\x08\x45ndpoint\x12\xad\x01\n\x06Update\x12\x33.yandex.cloud.datatransfer.v1.UpdateEndpointRequest\x1a!.yandex.cloud.operation.Operation\"K\x82\xd3\xe4\x93\x02\x1f\x32\x1a/v1/endpoint/{endpoint_id}:\x01*\xb2\xd2*\"\n\x16UpdateEndpointMetadata\x12\x08\x45ndpoint\x12\xb7\x01\n\x06\x44\x65lete\x12\x33.yandex.cloud.datatransfer.v1.DeleteEndpointRequest\x1a!.yandex.cloud.operation.Operation\"U\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/endpoint/{endpoint_id}\xb2\xd2*/\n\x16\x44\x65leteEndpointMetadata\x12\x15google.protobuf.EmptyBq\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransferb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,])




_GETENDPOINTREQUEST = _descriptor.Descriptor(
  name='GetEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.GetEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.GetEndpointRequest.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=268,
  serialized_end=309,
)


_LISTENDPOINTSREQUEST = _descriptor.Descriptor(
  name='ListEndpointsRequest',
  full_name='yandex.cloud.datatransfer.v1.ListEndpointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datatransfer.v1.ListEndpointsRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.datatransfer.v1.ListEndpointsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.datatransfer.v1.ListEndpointsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=311,
  serialized_end=391,
)


_LISTENDPOINTSRESPONSE = _descriptor.Descriptor(
  name='ListEndpointsResponse',
  full_name='yandex.cloud.datatransfer.v1.ListEndpointsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='yandex.cloud.datatransfer.v1.ListEndpointsResponse.endpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.datatransfer.v1.ListEndpointsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=393,
  serialized_end=500,
)


_CREATEENDPOINTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=774,
)

_CREATEENDPOINTREQUEST = _descriptor.Descriptor(
  name='CreateEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.CreateEndpointRequest.settings', index=4,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CREATEENDPOINTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=774,
)


_CREATEENDPOINTMETADATA = _descriptor.Descriptor(
  name='CreateEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.CreateEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.CreateEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=776,
  serialized_end=821,
)


_UPDATEENDPOINTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=774,
)

_UPDATEENDPOINTREQUEST = _descriptor.Descriptor(
  name='UpdateEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.endpoint_id', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.name', index=1,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.description', index=2,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.labels', index=3,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.settings', index=4,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointRequest.update_mask', index=5,
      number=60, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEENDPOINTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=1146,
)


_UPDATEENDPOINTMETADATA = _descriptor.Descriptor(
  name='UpdateEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.UpdateEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.UpdateEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1148,
  serialized_end=1193,
)


_DELETEENDPOINTREQUEST = _descriptor.Descriptor(
  name='DeleteEndpointRequest',
  full_name='yandex.cloud.datatransfer.v1.DeleteEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.DeleteEndpointRequest.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1195,
  serialized_end=1239,
)


_DELETEENDPOINTMETADATA = _descriptor.Descriptor(
  name='DeleteEndpointMetadata',
  full_name='yandex.cloud.datatransfer.v1.DeleteEndpointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='yandex.cloud.datatransfer.v1.DeleteEndpointMetadata.endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1241,
  serialized_end=1286,
)

_LISTENDPOINTSRESPONSE.fields_by_name['endpoints'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINT
_CREATEENDPOINTREQUEST_LABELSENTRY.containing_type = _CREATEENDPOINTREQUEST
_CREATEENDPOINTREQUEST.fields_by_name['labels'].message_type = _CREATEENDPOINTREQUEST_LABELSENTRY
_CREATEENDPOINTREQUEST.fields_by_name['settings'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINTSETTINGS
_UPDATEENDPOINTREQUEST_LABELSENTRY.containing_type = _UPDATEENDPOINTREQUEST
_UPDATEENDPOINTREQUEST.fields_by_name['labels'].message_type = _UPDATEENDPOINTREQUEST_LABELSENTRY
_UPDATEENDPOINTREQUEST.fields_by_name['settings'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINTSETTINGS
_UPDATEENDPOINTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['GetEndpointRequest'] = _GETENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['ListEndpointsRequest'] = _LISTENDPOINTSREQUEST
DESCRIPTOR.message_types_by_name['ListEndpointsResponse'] = _LISTENDPOINTSRESPONSE
DESCRIPTOR.message_types_by_name['CreateEndpointRequest'] = _CREATEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['CreateEndpointMetadata'] = _CREATEENDPOINTMETADATA
DESCRIPTOR.message_types_by_name['UpdateEndpointRequest'] = _UPDATEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['UpdateEndpointMetadata'] = _UPDATEENDPOINTMETADATA
DESCRIPTOR.message_types_by_name['DeleteEndpointRequest'] = _DELETEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['DeleteEndpointMetadata'] = _DELETEENDPOINTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetEndpointRequest = _reflection.GeneratedProtocolMessageType('GetEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.GetEndpointRequest)
  })
_sym_db.RegisterMessage(GetEndpointRequest)

ListEndpointsRequest = _reflection.GeneratedProtocolMessageType('ListEndpointsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENDPOINTSREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.ListEndpointsRequest)
  })
_sym_db.RegisterMessage(ListEndpointsRequest)

ListEndpointsResponse = _reflection.GeneratedProtocolMessageType('ListEndpointsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENDPOINTSRESPONSE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.ListEndpointsResponse)
  })
_sym_db.RegisterMessage(ListEndpointsResponse)

CreateEndpointRequest = _reflection.GeneratedProtocolMessageType('CreateEndpointRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEENDPOINTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.CreateEndpointRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.CreateEndpointRequest)
  })
_sym_db.RegisterMessage(CreateEndpointRequest)
_sym_db.RegisterMessage(CreateEndpointRequest.LabelsEntry)

CreateEndpointMetadata = _reflection.GeneratedProtocolMessageType('CreateEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.CreateEndpointMetadata)
  })
_sym_db.RegisterMessage(CreateEndpointMetadata)

UpdateEndpointRequest = _reflection.GeneratedProtocolMessageType('UpdateEndpointRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEENDPOINTREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.UpdateEndpointRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.UpdateEndpointRequest)
  })
_sym_db.RegisterMessage(UpdateEndpointRequest)
_sym_db.RegisterMessage(UpdateEndpointRequest.LabelsEntry)

UpdateEndpointMetadata = _reflection.GeneratedProtocolMessageType('UpdateEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.UpdateEndpointMetadata)
  })
_sym_db.RegisterMessage(UpdateEndpointMetadata)

DeleteEndpointRequest = _reflection.GeneratedProtocolMessageType('DeleteEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTREQUEST,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.DeleteEndpointRequest)
  })
_sym_db.RegisterMessage(DeleteEndpointRequest)

DeleteEndpointMetadata = _reflection.GeneratedProtocolMessageType('DeleteEndpointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTMETADATA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.DeleteEndpointMetadata)
  })
_sym_db.RegisterMessage(DeleteEndpointMetadata)


DESCRIPTOR._options = None
_CREATEENDPOINTREQUEST_LABELSENTRY._options = None
_UPDATEENDPOINTREQUEST_LABELSENTRY._options = None

_ENDPOINTSERVICE = _descriptor.ServiceDescriptor(
  name='EndpointService',
  full_name='yandex.cloud.datatransfer.v1.EndpointService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1289,
  serialized_end=2118,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Get',
    index=0,
    containing_service=None,
    input_type=_GETENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2._ENDPOINT,
    serialized_options=b'\202\323\344\223\002\034\022\032/v1/endpoint/{endpoint_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.List',
    index=1,
    containing_service=None,
    input_type=_LISTENDPOINTSREQUEST,
    output_type=_LISTENDPOINTSRESPONSE,
    serialized_options=b'\202\323\344\223\002 \022\036/v1/endpoints/list/{folder_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\021\"\014/v1/endpoint:\001*\262\322*\"\n\026CreateEndpointMetadata\022\010Endpoint',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\0372\032/v1/endpoint/{endpoint_id}:\001*\262\322*\"\n\026UpdateEndpointMetadata\022\010Endpoint',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.datatransfer.v1.EndpointService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\034*\032/v1/endpoint/{endpoint_id}\262\322*/\n\026DeleteEndpointMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENDPOINTSERVICE)

DESCRIPTOR.services_by_name['EndpointService'] = _ENDPOINTSERVICE

# @@protoc_insertion_point(module_scope)