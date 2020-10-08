# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/disk.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"yandex/cloud/compute/v1/disk.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xeb\x04\n\x04\x44isk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x39\n\x06labels\x18\x06 \x03(\x0b\x32).yandex.cloud.compute.v1.Disk.LabelsEntry\x12\x0f\n\x07type_id\x18\x07 \x01(\t\x12\x0f\n\x07zone_id\x18\x08 \x01(\t\x12\x0c\n\x04size\x18\t \x01(\x03\x12\x12\n\nblock_size\x18\x0f \x01(\x03\x12\x13\n\x0bproduct_ids\x18\n \x03(\t\x12\x34\n\x06status\x18\x0b \x01(\x0e\x32$.yandex.cloud.compute.v1.Disk.Status\x12\x19\n\x0fsource_image_id\x18\x0c \x01(\tH\x00\x12\x1c\n\x12source_snapshot_id\x18\r \x01(\tH\x00\x12\x14\n\x0cinstance_ids\x18\x0e \x03(\t\x12K\n\x15\x64isk_placement_policy\x18\x10 \x01(\x0b\x32,.yandex.cloud.compute.v1.DiskPlacementPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"R\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x42\x08\n\x06source\"1\n\x13\x44iskPlacementPolicy\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\tBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_DISK_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.compute.v1.Disk.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=624,
  serialized_end=706,
)
_sym_db.RegisterEnumDescriptor(_DISK_STATUS)


_DISK_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.compute.v1.Disk.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.Disk.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.Disk.LabelsEntry.value', index=1,
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
  serialized_start=577,
  serialized_end=622,
)

_DISK = _descriptor.Descriptor(
  name='Disk',
  full_name='yandex.cloud.compute.v1.Disk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.compute.v1.Disk.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.compute.v1.Disk.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.compute.v1.Disk.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.compute.v1.Disk.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.Disk.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.compute.v1.Disk.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type_id', full_name='yandex.cloud.compute.v1.Disk.type_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.compute.v1.Disk.zone_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='yandex.cloud.compute.v1.Disk.size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_size', full_name='yandex.cloud.compute.v1.Disk.block_size', index=9,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_ids', full_name='yandex.cloud.compute.v1.Disk.product_ids', index=10,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.compute.v1.Disk.status', index=11,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_image_id', full_name='yandex.cloud.compute.v1.Disk.source_image_id', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_snapshot_id', full_name='yandex.cloud.compute.v1.Disk.source_snapshot_id', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance_ids', full_name='yandex.cloud.compute.v1.Disk.instance_ids', index=14,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disk_placement_policy', full_name='yandex.cloud.compute.v1.Disk.disk_placement_policy', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DISK_LABELSENTRY, ],
  enum_types=[
    _DISK_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='yandex.cloud.compute.v1.Disk.source',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=97,
  serialized_end=716,
)


_DISKPLACEMENTPOLICY = _descriptor.Descriptor(
  name='DiskPlacementPolicy',
  full_name='yandex.cloud.compute.v1.DiskPlacementPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='placement_group_id', full_name='yandex.cloud.compute.v1.DiskPlacementPolicy.placement_group_id', index=0,
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
  serialized_start=718,
  serialized_end=767,
)

_DISK_LABELSENTRY.containing_type = _DISK
_DISK.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DISK.fields_by_name['labels'].message_type = _DISK_LABELSENTRY
_DISK.fields_by_name['status'].enum_type = _DISK_STATUS
_DISK.fields_by_name['disk_placement_policy'].message_type = _DISKPLACEMENTPOLICY
_DISK_STATUS.containing_type = _DISK
_DISK.oneofs_by_name['source'].fields.append(
  _DISK.fields_by_name['source_image_id'])
_DISK.fields_by_name['source_image_id'].containing_oneof = _DISK.oneofs_by_name['source']
_DISK.oneofs_by_name['source'].fields.append(
  _DISK.fields_by_name['source_snapshot_id'])
_DISK.fields_by_name['source_snapshot_id'].containing_oneof = _DISK.oneofs_by_name['source']
DESCRIPTOR.message_types_by_name['Disk'] = _DISK
DESCRIPTOR.message_types_by_name['DiskPlacementPolicy'] = _DISKPLACEMENTPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Disk = _reflection.GeneratedProtocolMessageType('Disk', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DISK_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.disk_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Disk.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DISK,
  '__module__' : 'yandex.cloud.compute.v1.disk_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Disk)
  })
_sym_db.RegisterMessage(Disk)
_sym_db.RegisterMessage(Disk.LabelsEntry)

DiskPlacementPolicy = _reflection.GeneratedProtocolMessageType('DiskPlacementPolicy', (_message.Message,), {
  'DESCRIPTOR' : _DISKPLACEMENTPOLICY,
  '__module__' : 'yandex.cloud.compute.v1.disk_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DiskPlacementPolicy)
  })
_sym_db.RegisterMessage(DiskPlacementPolicy)


DESCRIPTOR._options = None
_DISK_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
