# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/host_type_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.compute.v1 import host_type_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/host_type_service.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/yandex/cloud/compute/v1/host_type_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a\'yandex/cloud/compute/v1/host_type.proto\x1a\x1dyandex/cloud/validation.proto\"8\n\x12GetHostTypeRequest\x12\"\n\x0chost_type_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"T\n\x14ListHostTypesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x15ListHostTypesResponse\x12\x35\n\nhost_types\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.HostType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9e\x02\n\x0fHostTypeService\x12\x83\x01\n\x03Get\x12+.yandex.cloud.compute.v1.GetHostTypeRequest\x1a!.yandex.cloud.compute.v1.HostType\",\x82\xd3\xe4\x93\x02&\x12$/compute/v1/hostTypes/{host_type_id}\x12\x84\x01\n\x04List\x12-.yandex.cloud.compute.v1.ListHostTypesRequest\x1a..yandex.cloud.compute.v1.ListHostTypesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/compute/v1/hostTypesBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETHOSTTYPEREQUEST = _descriptor.Descriptor(
  name='GetHostTypeRequest',
  full_name='yandex.cloud.compute.v1.GetHostTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_type_id', full_name='yandex.cloud.compute.v1.GetHostTypeRequest.host_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=178,
  serialized_end=234,
)


_LISTHOSTTYPESREQUEST = _descriptor.Descriptor(
  name='ListHostTypesRequest',
  full_name='yandex.cloud.compute.v1.ListHostTypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.compute.v1.ListHostTypesRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.compute.v1.ListHostTypesRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=236,
  serialized_end=320,
)


_LISTHOSTTYPESRESPONSE = _descriptor.Descriptor(
  name='ListHostTypesResponse',
  full_name='yandex.cloud.compute.v1.ListHostTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_types', full_name='yandex.cloud.compute.v1.ListHostTypesResponse.host_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.compute.v1.ListHostTypesResponse.next_page_token', index=1,
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
  serialized_start=322,
  serialized_end=425,
)

_LISTHOSTTYPESRESPONSE.fields_by_name['host_types'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2._HOSTTYPE
DESCRIPTOR.message_types_by_name['GetHostTypeRequest'] = _GETHOSTTYPEREQUEST
DESCRIPTOR.message_types_by_name['ListHostTypesRequest'] = _LISTHOSTTYPESREQUEST
DESCRIPTOR.message_types_by_name['ListHostTypesResponse'] = _LISTHOSTTYPESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetHostTypeRequest = _reflection.GeneratedProtocolMessageType('GetHostTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETHOSTTYPEREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.host_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.GetHostTypeRequest)
  })
_sym_db.RegisterMessage(GetHostTypeRequest)

ListHostTypesRequest = _reflection.GeneratedProtocolMessageType('ListHostTypesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOSTTYPESREQUEST,
  '__module__' : 'yandex.cloud.compute.v1.host_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListHostTypesRequest)
  })
_sym_db.RegisterMessage(ListHostTypesRequest)

ListHostTypesResponse = _reflection.GeneratedProtocolMessageType('ListHostTypesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOSTTYPESRESPONSE,
  '__module__' : 'yandex.cloud.compute.v1.host_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListHostTypesResponse)
  })
_sym_db.RegisterMessage(ListHostTypesResponse)


DESCRIPTOR._options = None
_GETHOSTTYPEREQUEST.fields_by_name['host_type_id']._options = None
_LISTHOSTTYPESREQUEST.fields_by_name['page_size']._options = None
_LISTHOSTTYPESREQUEST.fields_by_name['page_token']._options = None

_HOSTTYPESERVICE = _descriptor.ServiceDescriptor(
  name='HostTypeService',
  full_name='yandex.cloud.compute.v1.HostTypeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=428,
  serialized_end=714,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.compute.v1.HostTypeService.Get',
    index=0,
    containing_service=None,
    input_type=_GETHOSTTYPEREQUEST,
    output_type=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2._HOSTTYPE,
    serialized_options=b'\202\323\344\223\002&\022$/compute/v1/hostTypes/{host_type_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.compute.v1.HostTypeService.List',
    index=1,
    containing_service=None,
    input_type=_LISTHOSTTYPESREQUEST,
    output_type=_LISTHOSTTYPESRESPONSE,
    serialized_options=b'\202\323\344\223\002\027\022\025/compute/v1/hostTypes',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HOSTTYPESERVICE)

DESCRIPTOR.services_by_name['HostTypeService'] = _HOSTTYPESERVICE

# @@protoc_insertion_point(module_scope)
