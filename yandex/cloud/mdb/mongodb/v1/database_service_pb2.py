# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/database_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.mongodb.v1 import database_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mongodb/v1/database_service.proto',
  package='yandex.cloud.mdb.mongodb.v1',
  syntax='proto3',
  serialized_options=b'\n\037yandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2yandex/cloud/mdb/mongodb/v1/database_service.proto\x12\x1byandex.cloud.mdb.mongodb.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/mdb/mongodb/v1/database.proto\"m\n\x12GetDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rdatabase_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"v\n\x14ListDatabasesRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"j\n\x15ListDatabasesResponse\x12\x38\n\tdatabases\x18\x01 \x03(\x0b\x32%.yandex.cloud.mdb.mongodb.v1.Database\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x81\x01\n\x15\x43reateDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x46\n\rdatabase_spec\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.mongodb.v1.DatabaseSpecB\x04\xe8\xc7\x31\x01\"C\n\x16\x43reateDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t\"p\n\x15\x44\x65leteDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rdatabase_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"C\n\x16\x44\x65leteDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t2\x95\x06\n\x0f\x44\x61tabaseService\x12\xaa\x01\n\x03Get\x12/.yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest\x1a%.yandex.cloud.mdb.mongodb.v1.Database\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}\x12\xaa\x01\n\x04List\x12\x31.yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest\x1a\x32.yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/managed-mongodb/v1/clusters/{cluster_id}/databases\x12\xc5\x01\n\x06\x43reate\x12\x32.yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"d\x82\xd3\xe4\x93\x02\x38\"3/managed-mongodb/v1/clusters/{cluster_id}/databases:\x01*\xb2\xd2*\"\n\x16\x43reateDatabaseMetadata\x12\x08\x44\x61tabase\x12\xdf\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"~\x82\xd3\xe4\x93\x02\x45*C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}\xb2\xd2*/\n\x16\x44\x65leteDatabaseMetadata\x12\x15google.protobuf.EmptyBj\n\x1fyandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodbb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2.DESCRIPTOR,])




_GETDATABASEREQUEST = _descriptor.Descriptor(
  name='GetDatabaseRequest',
  full_name='yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=262,
  serialized_end=371,
)


_LISTDATABASESREQUEST = _descriptor.Descriptor(
  name='ListDatabasesRequest',
  full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=373,
  serialized_end=491,
)


_LISTDATABASESRESPONSE = _descriptor.Descriptor(
  name='ListDatabasesResponse',
  full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='databases', full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse.databases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse.next_page_token', index=1,
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
  serialized_start=493,
  serialized_end=599,
)


_CREATEDATABASEREQUEST = _descriptor.Descriptor(
  name='CreateDatabaseRequest',
  full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_spec', full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest.database_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=602,
  serialized_end=731,
)


_CREATEDATABASEMETADATA = _descriptor.Descriptor(
  name='CreateDatabaseMetadata',
  full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mongodb.v1.CreateDatabaseMetadata.database_name', index=1,
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
  serialized_start=733,
  serialized_end=800,
)


_DELETEDATABASEREQUEST = _descriptor.Descriptor(
  name='DeleteDatabaseRequest',
  full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest.database_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=802,
  serialized_end=914,
)


_DELETEDATABASEMETADATA = _descriptor.Descriptor(
  name='DeleteDatabaseMetadata',
  full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mongodb.v1.DeleteDatabaseMetadata.database_name', index=1,
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
  serialized_start=916,
  serialized_end=983,
)

_LISTDATABASESRESPONSE.fields_by_name['databases'].message_type = yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2._DATABASE
_CREATEDATABASEREQUEST.fields_by_name['database_spec'].message_type = yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2._DATABASESPEC
DESCRIPTOR.message_types_by_name['GetDatabaseRequest'] = _GETDATABASEREQUEST
DESCRIPTOR.message_types_by_name['ListDatabasesRequest'] = _LISTDATABASESREQUEST
DESCRIPTOR.message_types_by_name['ListDatabasesResponse'] = _LISTDATABASESRESPONSE
DESCRIPTOR.message_types_by_name['CreateDatabaseRequest'] = _CREATEDATABASEREQUEST
DESCRIPTOR.message_types_by_name['CreateDatabaseMetadata'] = _CREATEDATABASEMETADATA
DESCRIPTOR.message_types_by_name['DeleteDatabaseRequest'] = _DELETEDATABASEREQUEST
DESCRIPTOR.message_types_by_name['DeleteDatabaseMetadata'] = _DELETEDATABASEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDatabaseRequest = _reflection.GeneratedProtocolMessageType('GetDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATABASEREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest)
  })
_sym_db.RegisterMessage(GetDatabaseRequest)

ListDatabasesRequest = _reflection.GeneratedProtocolMessageType('ListDatabasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABASESREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest)
  })
_sym_db.RegisterMessage(ListDatabasesRequest)

ListDatabasesResponse = _reflection.GeneratedProtocolMessageType('ListDatabasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABASESRESPONSE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse)
  })
_sym_db.RegisterMessage(ListDatabasesResponse)

CreateDatabaseRequest = _reflection.GeneratedProtocolMessageType('CreateDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATABASEREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest)
  })
_sym_db.RegisterMessage(CreateDatabaseRequest)

CreateDatabaseMetadata = _reflection.GeneratedProtocolMessageType('CreateDatabaseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATABASEMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.CreateDatabaseMetadata)
  })
_sym_db.RegisterMessage(CreateDatabaseMetadata)

DeleteDatabaseRequest = _reflection.GeneratedProtocolMessageType('DeleteDatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATABASEREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest)
  })
_sym_db.RegisterMessage(DeleteDatabaseRequest)

DeleteDatabaseMetadata = _reflection.GeneratedProtocolMessageType('DeleteDatabaseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATABASEMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.database_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.DeleteDatabaseMetadata)
  })
_sym_db.RegisterMessage(DeleteDatabaseMetadata)


DESCRIPTOR._options = None
_GETDATABASEREQUEST.fields_by_name['cluster_id']._options = None
_GETDATABASEREQUEST.fields_by_name['database_name']._options = None
_LISTDATABASESREQUEST.fields_by_name['cluster_id']._options = None
_LISTDATABASESREQUEST.fields_by_name['page_size']._options = None
_LISTDATABASESREQUEST.fields_by_name['page_token']._options = None
_CREATEDATABASEREQUEST.fields_by_name['cluster_id']._options = None
_CREATEDATABASEREQUEST.fields_by_name['database_spec']._options = None
_DELETEDATABASEREQUEST.fields_by_name['cluster_id']._options = None
_DELETEDATABASEREQUEST.fields_by_name['database_name']._options = None

_DATABASESERVICE = _descriptor.ServiceDescriptor(
  name='DatabaseService',
  full_name='yandex.cloud.mdb.mongodb.v1.DatabaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=986,
  serialized_end=1775,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.mongodb.v1.DatabaseService.Get',
    index=0,
    containing_service=None,
    input_type=_GETDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2._DATABASE,
    serialized_options=b'\202\323\344\223\002E\022C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.mongodb.v1.DatabaseService.List',
    index=1,
    containing_service=None,
    input_type=_LISTDATABASESREQUEST,
    output_type=_LISTDATABASESRESPONSE,
    serialized_options=b'\202\323\344\223\0025\0223/managed-mongodb/v1/clusters/{cluster_id}/databases',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.mdb.mongodb.v1.DatabaseService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\0028\"3/managed-mongodb/v1/clusters/{cluster_id}/databases:\001*\262\322*\"\n\026CreateDatabaseMetadata\022\010Database',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.mdb.mongodb.v1.DatabaseService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEDATABASEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002E*C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}\262\322*/\n\026DeleteDatabaseMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASESERVICE)

DESCRIPTOR.services_by_name['DatabaseService'] = _DATABASESERVICE

# @@protoc_insertion_point(module_scope)
