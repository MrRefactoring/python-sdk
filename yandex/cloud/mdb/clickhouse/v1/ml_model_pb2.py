# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/ml_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/ml_model.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-yandex/cloud/mdb/clickhouse/v1/ml_model.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\"s\n\x07MlModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32+.yandex.cloud.mdb.clickhouse.v1.MlModelType\x12\x0b\n\x03uri\x18\x04 \x01(\t*H\n\x0bMlModelType\x12\x1d\n\x19ML_MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16ML_MODEL_TYPE_CATBOOST\x10\x01\x42s\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3'
)

_MLMODELTYPE = _descriptor.EnumDescriptor(
  name='MlModelType',
  full_name='yandex.cloud.mdb.clickhouse.v1.MlModelType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ML_MODEL_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ML_MODEL_TYPE_CATBOOST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=198,
  serialized_end=270,
)
_sym_db.RegisterEnumDescriptor(_MLMODELTYPE)

MlModelType = enum_type_wrapper.EnumTypeWrapper(_MLMODELTYPE)
ML_MODEL_TYPE_UNSPECIFIED = 0
ML_MODEL_TYPE_CATBOOST = 1



_MLMODEL = _descriptor.Descriptor(
  name='MlModel',
  full_name='yandex.cloud.mdb.clickhouse.v1.MlModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.clickhouse.v1.MlModel.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.MlModel.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.clickhouse.v1.MlModel.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.MlModel.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=81,
  serialized_end=196,
)

_MLMODEL.fields_by_name['type'].enum_type = _MLMODELTYPE
DESCRIPTOR.message_types_by_name['MlModel'] = _MLMODEL
DESCRIPTOR.enum_types_by_name['MlModelType'] = _MLMODELTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MlModel = _reflection.GeneratedProtocolMessageType('MlModel', (_message.Message,), {
  'DESCRIPTOR' : _MLMODEL,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.MlModel)
  })
_sym_db.RegisterMessage(MlModel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
