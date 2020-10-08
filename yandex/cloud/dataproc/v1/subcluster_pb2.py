# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/subcluster.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.dataproc.v1 import common_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/v1/subcluster.proto',
  package='yandex.cloud.dataproc.v1',
  syntax='proto3',
  serialized_options=b'\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)yandex/cloud/dataproc/v1/subcluster.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%yandex/cloud/dataproc/v1/common.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf2\x02\n\x11\x41utoscalingConfig\x12\"\n\x0fmax_hosts_count\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100\x12\x13\n\x0bpreemptible\x18\x02 \x01(\x08\x12G\n\x14measurement_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0e\xe8\xc7\x31\x01\xfa\xc7\x31\x06\x31m-10m\x12=\n\x0fwarmup_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=10m\x12\x45\n\x16stabilization_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\xc7\x31\x06\x31m-30m\x12*\n\x16\x63pu_utilization_target\x18\x06 \x01(\x01\x42\n\xfa\xc7\x31\x06\x31\x30-100\x12)\n\x14\x64\x65\x63ommission_timeout\x18\x07 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\"\xec\x02\n\nSubcluster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x31-63\x12,\n\x04role\x18\x05 \x01(\x0e\x32\x1e.yandex.cloud.dataproc.v1.Role\x12\x36\n\tresources\x18\x06 \x01(\x0b\x32#.yandex.cloud.dataproc.v1.Resources\x12\x11\n\tsubnet_id\x18\x07 \x01(\t\x12\x13\n\x0bhosts_count\x18\x08 \x01(\x03\x12G\n\x12\x61utoscaling_config\x18\n \x01(\x0b\x32+.yandex.cloud.dataproc.v1.AutoscalingConfig\x12\x19\n\x11instance_group_id\x18\x0b \x01(\tJ\x04\x08\t\x10\n\"\xa8\x01\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsubcluster_id\x18\x02 \x01(\t\x12\x30\n\x06health\x18\x03 \x01(\x0e\x32 .yandex.cloud.dataproc.v1.Health\x12\x1b\n\x13\x63ompute_instance_id\x18\x04 \x01(\t\x12,\n\x04role\x18\x05 \x01(\x0e\x32\x1e.yandex.cloud.dataproc.v1.Role*K\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0e\n\nMASTERNODE\x10\x01\x12\x0c\n\x08\x44\x41TANODE\x10\x02\x12\x0f\n\x0b\x43OMPUTENODE\x10\x03\x42\x65\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='yandex.cloud.dataproc.v1.Role',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROLE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MASTERNODE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATANODE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPUTENODE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1117,
  serialized_end=1192,
)
_sym_db.RegisterEnumDescriptor(_ROLE)

Role = enum_type_wrapper.EnumTypeWrapper(_ROLE)
ROLE_UNSPECIFIED = 0
MASTERNODE = 1
DATANODE = 2
COMPUTENODE = 3



_AUTOSCALINGCONFIG = _descriptor.Descriptor(
  name='AutoscalingConfig',
  full_name='yandex.cloud.dataproc.v1.AutoscalingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_hosts_count', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.max_hosts_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0051-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preemptible', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.preemptible', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measurement_duration', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.measurement_duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\372\3071\0061m-10m', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warmup_duration', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.warmup_duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\005<=10m', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stabilization_duration', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.stabilization_duration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0061m-30m', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu_utilization_target', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.cpu_utilization_target', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\00610-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decommission_timeout', full_name='yandex.cloud.dataproc.v1.AutoscalingConfig.decommission_timeout', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0070-86400', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=207,
  serialized_end=577,
)


_SUBCLUSTER = _descriptor.Descriptor(
  name='Subcluster',
  full_name='yandex.cloud.dataproc.v1.Subcluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.dataproc.v1.Subcluster.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.dataproc.v1.Subcluster.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.dataproc.v1.Subcluster.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.v1.Subcluster.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\0041-63', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='yandex.cloud.dataproc.v1.Subcluster.role', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.dataproc.v1.Subcluster.resources', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.dataproc.v1.Subcluster.subnet_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hosts_count', full_name='yandex.cloud.dataproc.v1.Subcluster.hosts_count', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoscaling_config', full_name='yandex.cloud.dataproc.v1.Subcluster.autoscaling_config', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance_group_id', full_name='yandex.cloud.dataproc.v1.Subcluster.instance_group_id', index=9,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=580,
  serialized_end=944,
)


_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='yandex.cloud.dataproc.v1.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.v1.Host.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcluster_id', full_name='yandex.cloud.dataproc.v1.Host.subcluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.dataproc.v1.Host.health', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_instance_id', full_name='yandex.cloud.dataproc.v1.Host.compute_instance_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='yandex.cloud.dataproc.v1.Host.role', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=947,
  serialized_end=1115,
)

_AUTOSCALINGCONFIG.fields_by_name['measurement_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_AUTOSCALINGCONFIG.fields_by_name['warmup_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_AUTOSCALINGCONFIG.fields_by_name['stabilization_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SUBCLUSTER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SUBCLUSTER.fields_by_name['role'].enum_type = _ROLE
_SUBCLUSTER.fields_by_name['resources'].message_type = yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2._RESOURCES
_SUBCLUSTER.fields_by_name['autoscaling_config'].message_type = _AUTOSCALINGCONFIG
_HOST.fields_by_name['health'].enum_type = yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2._HEALTH
_HOST.fields_by_name['role'].enum_type = _ROLE
DESCRIPTOR.message_types_by_name['AutoscalingConfig'] = _AUTOSCALINGCONFIG
DESCRIPTOR.message_types_by_name['Subcluster'] = _SUBCLUSTER
DESCRIPTOR.message_types_by_name['Host'] = _HOST
DESCRIPTOR.enum_types_by_name['Role'] = _ROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AutoscalingConfig = _reflection.GeneratedProtocolMessageType('AutoscalingConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSCALINGCONFIG,
  '__module__' : 'yandex.cloud.dataproc.v1.subcluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.AutoscalingConfig)
  })
_sym_db.RegisterMessage(AutoscalingConfig)

Subcluster = _reflection.GeneratedProtocolMessageType('Subcluster', (_message.Message,), {
  'DESCRIPTOR' : _SUBCLUSTER,
  '__module__' : 'yandex.cloud.dataproc.v1.subcluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Subcluster)
  })
_sym_db.RegisterMessage(Subcluster)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'yandex.cloud.dataproc.v1.subcluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Host)
  })
_sym_db.RegisterMessage(Host)


DESCRIPTOR._options = None
_AUTOSCALINGCONFIG.fields_by_name['max_hosts_count']._options = None
_AUTOSCALINGCONFIG.fields_by_name['measurement_duration']._options = None
_AUTOSCALINGCONFIG.fields_by_name['warmup_duration']._options = None
_AUTOSCALINGCONFIG.fields_by_name['stabilization_duration']._options = None
_AUTOSCALINGCONFIG.fields_by_name['cpu_utilization_target']._options = None
_AUTOSCALINGCONFIG.fields_by_name['decommission_timeout']._options = None
_SUBCLUSTER.fields_by_name['name']._options = None
# @@protoc_insertion_point(module_scope)
