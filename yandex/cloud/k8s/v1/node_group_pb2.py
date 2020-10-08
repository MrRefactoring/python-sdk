# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/node_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.k8s.v1 import maintenance_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_maintenance__pb2
from yandex.cloud.k8s.v1 import node_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2
from yandex.cloud.k8s.v1 import version_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/k8s/v1/node_group.proto',
  package='yandex.cloud.k8s.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$yandex/cloud/k8s/v1/node_group.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%yandex/cloud/k8s/v1/maintenance.proto\x1a\x1eyandex/cloud/k8s/v1/node.proto\x1a!yandex/cloud/k8s/v1/version.proto\x1a\x1dyandex/cloud/validation.proto\"\xa0\x08\n\tNodeGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12:\n\x06labels\x18\x06 \x03(\x0b\x32*.yandex.cloud.k8s.v1.NodeGroup.LabelsEntry\x12\x35\n\x06status\x18\x07 \x01(\x0e\x32%.yandex.cloud.k8s.v1.NodeGroup.Status\x12\x38\n\rnode_template\x18\x08 \x01(\x0b\x32!.yandex.cloud.k8s.v1.NodeTemplate\x12\x36\n\x0cscale_policy\x18\t \x01(\x0b\x32 .yandex.cloud.k8s.v1.ScalePolicy\x12I\n\x11\x61llocation_policy\x18\n \x01(\x0b\x32..yandex.cloud.k8s.v1.NodeGroupAllocationPolicy\x12\x38\n\rdeploy_policy\x18\x12 \x01(\x0b\x32!.yandex.cloud.k8s.v1.DeployPolicy\x12\x19\n\x11instance_group_id\x18\x0b \x01(\t\x12\x14\n\x0cnode_version\x18\x0c \x01(\t\x12\x36\n\x0cversion_info\x18\r \x01(\x0b\x32 .yandex.cloud.k8s.v1.VersionInfo\x12K\n\x12maintenance_policy\x18\x0e \x01(\x0b\x32/.yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy\x12\x1e\n\x16\x61llowed_unsafe_sysctls\x18\x0f \x03(\t\x12/\n\x0bnode_taints\x18\x10 \x03(\x0b\x32\x1a.yandex.cloud.k8s.v1.Taint\x12\x43\n\x0bnode_labels\x18\x11 \x03(\x0b\x32..yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fNodeLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0f\n\x0bRECONCILING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0c\n\x08\x44\x45LETING\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"\xb6\x02\n\x0bScalePolicy\x12\x42\n\x0b\x66ixed_scale\x18\x01 \x01(\x0b\x32+.yandex.cloud.k8s.v1.ScalePolicy.FixedScaleH\x00\x12@\n\nauto_scale\x18\x02 \x01(\x0b\x32*.yandex.cloud.k8s.v1.ScalePolicy.AutoScaleH\x00\x1a%\n\nFixedScale\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x1a\x66\n\tAutoScale\x12\x1b\n\x08min_size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1b\n\x08max_size\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1f\n\x0cinitial_size\x18\x03 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100B\x12\n\nscale_type\x12\x04\xc0\xc1\x31\x01\"V\n\x19NodeGroupAllocationPolicy\x12\x39\n\tlocations\x18\x01 \x03(\x0b\x32&.yandex.cloud.k8s.v1.NodeGroupLocation\"=\n\x11NodeGroupLocation\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\"\x8b\x01\n\x1aNodeGroupMaintenancePolicy\x12\x14\n\x0c\x61uto_upgrade\x18\x01 \x01(\x08\x12\x13\n\x0b\x61uto_repair\x18\x02 \x01(\x08\x12\x42\n\x12maintenance_window\x18\x03 \x01(\x0b\x32&.yandex.cloud.k8s.v1.MaintenanceWindow\"T\n\x0c\x44\x65ployPolicy\x12\"\n\x0fmax_unavailable\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12 \n\rmax_expansion\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100BV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_k8s_dot_v1_dot_maintenance__pb2.DESCRIPTOR,yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2.DESCRIPTOR,yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_NODEGROUP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.k8s.v1.NodeGroup.Status',
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
      name='PROVISIONING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECONCILING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1153,
  serialized_end=1288,
)
_sym_db.RegisterEnumDescriptor(_NODEGROUP_STATUS)


_NODEGROUP_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.k8s.v1.NodeGroup.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.k8s.v1.NodeGroup.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.k8s.v1.NodeGroup.LabelsEntry.value', index=1,
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
  serialized_start=1054,
  serialized_end=1099,
)

_NODEGROUP_NODELABELSENTRY = _descriptor.Descriptor(
  name='NodeLabelsEntry',
  full_name='yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry.value', index=1,
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
  serialized_start=1101,
  serialized_end=1150,
)

_NODEGROUP = _descriptor.Descriptor(
  name='NodeGroup',
  full_name='yandex.cloud.k8s.v1.NodeGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.k8s.v1.NodeGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.k8s.v1.NodeGroup.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.k8s.v1.NodeGroup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.k8s.v1.NodeGroup.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.k8s.v1.NodeGroup.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.k8s.v1.NodeGroup.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.k8s.v1.NodeGroup.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_template', full_name='yandex.cloud.k8s.v1.NodeGroup.node_template', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scale_policy', full_name='yandex.cloud.k8s.v1.NodeGroup.scale_policy', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allocation_policy', full_name='yandex.cloud.k8s.v1.NodeGroup.allocation_policy', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deploy_policy', full_name='yandex.cloud.k8s.v1.NodeGroup.deploy_policy', index=10,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance_group_id', full_name='yandex.cloud.k8s.v1.NodeGroup.instance_group_id', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_version', full_name='yandex.cloud.k8s.v1.NodeGroup.node_version', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_info', full_name='yandex.cloud.k8s.v1.NodeGroup.version_info', index=13,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_policy', full_name='yandex.cloud.k8s.v1.NodeGroup.maintenance_policy', index=14,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_unsafe_sysctls', full_name='yandex.cloud.k8s.v1.NodeGroup.allowed_unsafe_sysctls', index=15,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_taints', full_name='yandex.cloud.k8s.v1.NodeGroup.node_taints', index=16,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_labels', full_name='yandex.cloud.k8s.v1.NodeGroup.node_labels', index=17,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NODEGROUP_LABELSENTRY, _NODEGROUP_NODELABELSENTRY, ],
  enum_types=[
    _NODEGROUP_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=1288,
)


_SCALEPOLICY_FIXEDSCALE = _descriptor.Descriptor(
  name='FixedScale',
  full_name='yandex.cloud.k8s.v1.ScalePolicy.FixedScale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='yandex.cloud.k8s.v1.ScalePolicy.FixedScale.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1440,
  serialized_end=1477,
)

_SCALEPOLICY_AUTOSCALE = _descriptor.Descriptor(
  name='AutoScale',
  full_name='yandex.cloud.k8s.v1.ScalePolicy.AutoScale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_size', full_name='yandex.cloud.k8s.v1.ScalePolicy.AutoScale.min_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_size', full_name='yandex.cloud.k8s.v1.ScalePolicy.AutoScale.max_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_size', full_name='yandex.cloud.k8s.v1.ScalePolicy.AutoScale.initial_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1479,
  serialized_end=1581,
)

_SCALEPOLICY = _descriptor.Descriptor(
  name='ScalePolicy',
  full_name='yandex.cloud.k8s.v1.ScalePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixed_scale', full_name='yandex.cloud.k8s.v1.ScalePolicy.fixed_scale', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_scale', full_name='yandex.cloud.k8s.v1.ScalePolicy.auto_scale', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCALEPOLICY_FIXEDSCALE, _SCALEPOLICY_AUTOSCALE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='scale_type', full_name='yandex.cloud.k8s.v1.ScalePolicy.scale_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=1291,
  serialized_end=1601,
)


_NODEGROUPALLOCATIONPOLICY = _descriptor.Descriptor(
  name='NodeGroupAllocationPolicy',
  full_name='yandex.cloud.k8s.v1.NodeGroupAllocationPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='yandex.cloud.k8s.v1.NodeGroupAllocationPolicy.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1603,
  serialized_end=1689,
)


_NODEGROUPLOCATION = _descriptor.Descriptor(
  name='NodeGroupLocation',
  full_name='yandex.cloud.k8s.v1.NodeGroupLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.k8s.v1.NodeGroupLocation.zone_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.k8s.v1.NodeGroupLocation.subnet_id', index=1,
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
  serialized_start=1691,
  serialized_end=1752,
)


_NODEGROUPMAINTENANCEPOLICY = _descriptor.Descriptor(
  name='NodeGroupMaintenancePolicy',
  full_name='yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auto_upgrade', full_name='yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy.auto_upgrade', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_repair', full_name='yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy.auto_repair', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_window', full_name='yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy.maintenance_window', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1755,
  serialized_end=1894,
)


_DEPLOYPOLICY = _descriptor.Descriptor(
  name='DeployPolicy',
  full_name='yandex.cloud.k8s.v1.DeployPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_unavailable', full_name='yandex.cloud.k8s.v1.DeployPolicy.max_unavailable', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_expansion', full_name='yandex.cloud.k8s.v1.DeployPolicy.max_expansion', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1896,
  serialized_end=1980,
)

_NODEGROUP_LABELSENTRY.containing_type = _NODEGROUP
_NODEGROUP_NODELABELSENTRY.containing_type = _NODEGROUP
_NODEGROUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NODEGROUP.fields_by_name['labels'].message_type = _NODEGROUP_LABELSENTRY
_NODEGROUP.fields_by_name['status'].enum_type = _NODEGROUP_STATUS
_NODEGROUP.fields_by_name['node_template'].message_type = yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2._NODETEMPLATE
_NODEGROUP.fields_by_name['scale_policy'].message_type = _SCALEPOLICY
_NODEGROUP.fields_by_name['allocation_policy'].message_type = _NODEGROUPALLOCATIONPOLICY
_NODEGROUP.fields_by_name['deploy_policy'].message_type = _DEPLOYPOLICY
_NODEGROUP.fields_by_name['version_info'].message_type = yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2._VERSIONINFO
_NODEGROUP.fields_by_name['maintenance_policy'].message_type = _NODEGROUPMAINTENANCEPOLICY
_NODEGROUP.fields_by_name['node_taints'].message_type = yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2._TAINT
_NODEGROUP.fields_by_name['node_labels'].message_type = _NODEGROUP_NODELABELSENTRY
_NODEGROUP_STATUS.containing_type = _NODEGROUP
_SCALEPOLICY_FIXEDSCALE.containing_type = _SCALEPOLICY
_SCALEPOLICY_AUTOSCALE.containing_type = _SCALEPOLICY
_SCALEPOLICY.fields_by_name['fixed_scale'].message_type = _SCALEPOLICY_FIXEDSCALE
_SCALEPOLICY.fields_by_name['auto_scale'].message_type = _SCALEPOLICY_AUTOSCALE
_SCALEPOLICY.oneofs_by_name['scale_type'].fields.append(
  _SCALEPOLICY.fields_by_name['fixed_scale'])
_SCALEPOLICY.fields_by_name['fixed_scale'].containing_oneof = _SCALEPOLICY.oneofs_by_name['scale_type']
_SCALEPOLICY.oneofs_by_name['scale_type'].fields.append(
  _SCALEPOLICY.fields_by_name['auto_scale'])
_SCALEPOLICY.fields_by_name['auto_scale'].containing_oneof = _SCALEPOLICY.oneofs_by_name['scale_type']
_NODEGROUPALLOCATIONPOLICY.fields_by_name['locations'].message_type = _NODEGROUPLOCATION
_NODEGROUPMAINTENANCEPOLICY.fields_by_name['maintenance_window'].message_type = yandex_dot_cloud_dot_k8s_dot_v1_dot_maintenance__pb2._MAINTENANCEWINDOW
DESCRIPTOR.message_types_by_name['NodeGroup'] = _NODEGROUP
DESCRIPTOR.message_types_by_name['ScalePolicy'] = _SCALEPOLICY
DESCRIPTOR.message_types_by_name['NodeGroupAllocationPolicy'] = _NODEGROUPALLOCATIONPOLICY
DESCRIPTOR.message_types_by_name['NodeGroupLocation'] = _NODEGROUPLOCATION
DESCRIPTOR.message_types_by_name['NodeGroupMaintenancePolicy'] = _NODEGROUPMAINTENANCEPOLICY
DESCRIPTOR.message_types_by_name['DeployPolicy'] = _DEPLOYPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeGroup = _reflection.GeneratedProtocolMessageType('NodeGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODEGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroup.LabelsEntry)
    })
  ,

  'NodeLabelsEntry' : _reflection.GeneratedProtocolMessageType('NodeLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODEGROUP_NODELABELSENTRY,
    '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry)
    })
  ,
  'DESCRIPTOR' : _NODEGROUP,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroup)
  })
_sym_db.RegisterMessage(NodeGroup)
_sym_db.RegisterMessage(NodeGroup.LabelsEntry)
_sym_db.RegisterMessage(NodeGroup.NodeLabelsEntry)

ScalePolicy = _reflection.GeneratedProtocolMessageType('ScalePolicy', (_message.Message,), {

  'FixedScale' : _reflection.GeneratedProtocolMessageType('FixedScale', (_message.Message,), {
    'DESCRIPTOR' : _SCALEPOLICY_FIXEDSCALE,
    '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ScalePolicy.FixedScale)
    })
  ,

  'AutoScale' : _reflection.GeneratedProtocolMessageType('AutoScale', (_message.Message,), {
    'DESCRIPTOR' : _SCALEPOLICY_AUTOSCALE,
    '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ScalePolicy.AutoScale)
    })
  ,
  'DESCRIPTOR' : _SCALEPOLICY,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ScalePolicy)
  })
_sym_db.RegisterMessage(ScalePolicy)
_sym_db.RegisterMessage(ScalePolicy.FixedScale)
_sym_db.RegisterMessage(ScalePolicy.AutoScale)

NodeGroupAllocationPolicy = _reflection.GeneratedProtocolMessageType('NodeGroupAllocationPolicy', (_message.Message,), {
  'DESCRIPTOR' : _NODEGROUPALLOCATIONPOLICY,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroupAllocationPolicy)
  })
_sym_db.RegisterMessage(NodeGroupAllocationPolicy)

NodeGroupLocation = _reflection.GeneratedProtocolMessageType('NodeGroupLocation', (_message.Message,), {
  'DESCRIPTOR' : _NODEGROUPLOCATION,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroupLocation)
  })
_sym_db.RegisterMessage(NodeGroupLocation)

NodeGroupMaintenancePolicy = _reflection.GeneratedProtocolMessageType('NodeGroupMaintenancePolicy', (_message.Message,), {
  'DESCRIPTOR' : _NODEGROUPMAINTENANCEPOLICY,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy)
  })
_sym_db.RegisterMessage(NodeGroupMaintenancePolicy)

DeployPolicy = _reflection.GeneratedProtocolMessageType('DeployPolicy', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYPOLICY,
  '__module__' : 'yandex.cloud.k8s.v1.node_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.DeployPolicy)
  })
_sym_db.RegisterMessage(DeployPolicy)


DESCRIPTOR._options = None
_NODEGROUP_LABELSENTRY._options = None
_NODEGROUP_NODELABELSENTRY._options = None
_SCALEPOLICY_FIXEDSCALE.fields_by_name['size']._options = None
_SCALEPOLICY_AUTOSCALE.fields_by_name['min_size']._options = None
_SCALEPOLICY_AUTOSCALE.fields_by_name['max_size']._options = None
_SCALEPOLICY_AUTOSCALE.fields_by_name['initial_size']._options = None
_SCALEPOLICY.oneofs_by_name['scale_type']._options = None
_NODEGROUPLOCATION.fields_by_name['zone_id']._options = None
_DEPLOYPOLICY.fields_by_name['max_unavailable']._options = None
_DEPLOYPOLICY.fields_by_name['max_expansion']._options = None
# @@protoc_insertion_point(module_scope)
