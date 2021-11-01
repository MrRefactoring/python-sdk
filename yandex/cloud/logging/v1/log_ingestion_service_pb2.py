# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/logging/v1/log_ingestion_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud.logging.v1 import log_resource_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/logging/v1/log_ingestion_service.proto',
  package='yandex.cloud.logging.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3yandex/cloud/logging/v1/log_ingestion_service.proto\x12\x17yandex.cloud.logging.v1\x1a\x17google/rpc/status.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a*yandex/cloud/logging/v1/log_resource.proto\x1a\x1dyandex/cloud/validation.proto\"\x90\x02\n\x0cWriteRequest\x12?\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32$.yandex.cloud.logging.v1.DestinationB\x04\xe8\xc7\x31\x01\x12;\n\x08resource\x18\x02 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryResource\x12\x45\n\x07\x65ntries\x18\x03 \x03(\x0b\x32).yandex.cloud.logging.v1.IncomingLogEntryB\t\x82\xc8\x31\x05\x31-100\x12;\n\x08\x64\x65\x66\x61ults\x18\x04 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryDefaults\"\x96\x01\n\rWriteResponse\x12\x42\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x32.yandex.cloud.logging.v1.WriteResponse.ErrorsEntry\x1a\x41\n\x0b\x45rrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status:\x02\x38\x01\x32m\n\x13LogIngestionService\x12V\n\x05Write\x12%.yandex.cloud.logging.v1.WriteRequest\x1a&.yandex.cloud.logging.v1.WriteResponseBb\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3'
  ,
  dependencies=[google_dot_rpc_dot_status__pb2.DESCRIPTOR,yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2.DESCRIPTOR,yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='yandex.cloud.logging.v1.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='yandex.cloud.logging.v1.WriteRequest.destination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='yandex.cloud.logging.v1.WriteRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entries', full_name='yandex.cloud.logging.v1.WriteRequest.entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\0051-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defaults', full_name='yandex.cloud.logging.v1.WriteRequest.defaults', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=222,
  serialized_end=494,
)


_WRITERESPONSE_ERRORSENTRY = _descriptor.Descriptor(
  name='ErrorsEntry',
  full_name='yandex.cloud.logging.v1.WriteResponse.ErrorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.logging.v1.WriteResponse.ErrorsEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.logging.v1.WriteResponse.ErrorsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=647,
)

_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='yandex.cloud.logging.v1.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errors', full_name='yandex.cloud.logging.v1.WriteResponse.errors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_WRITERESPONSE_ERRORSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=647,
)

_WRITEREQUEST.fields_by_name['destination'].message_type = yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2._DESTINATION
_WRITEREQUEST.fields_by_name['resource'].message_type = yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2._LOGENTRYRESOURCE
_WRITEREQUEST.fields_by_name['entries'].message_type = yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2._INCOMINGLOGENTRY
_WRITEREQUEST.fields_by_name['defaults'].message_type = yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2._LOGENTRYDEFAULTS
_WRITERESPONSE_ERRORSENTRY.fields_by_name['value'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_WRITERESPONSE_ERRORSENTRY.containing_type = _WRITERESPONSE
_WRITERESPONSE.fields_by_name['errors'].message_type = _WRITERESPONSE_ERRORSENTRY
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'yandex.cloud.logging.v1.log_ingestion_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {

  'ErrorsEntry' : _reflection.GeneratedProtocolMessageType('ErrorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _WRITERESPONSE_ERRORSENTRY,
    '__module__' : 'yandex.cloud.logging.v1.log_ingestion_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.WriteResponse.ErrorsEntry)
    })
  ,
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'yandex.cloud.logging.v1.log_ingestion_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)
_sym_db.RegisterMessage(WriteResponse.ErrorsEntry)


DESCRIPTOR._options = None
_WRITEREQUEST.fields_by_name['destination']._options = None
_WRITEREQUEST.fields_by_name['entries']._options = None
_WRITERESPONSE_ERRORSENTRY._options = None

_LOGINGESTIONSERVICE = _descriptor.ServiceDescriptor(
  name='LogIngestionService',
  full_name='yandex.cloud.logging.v1.LogIngestionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=649,
  serialized_end=758,
  methods=[
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='yandex.cloud.logging.v1.LogIngestionService.Write',
    index=0,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGINGESTIONSERVICE)

DESCRIPTOR.services_by_name['LogIngestionService'] = _LOGINGESTIONSERVICE

# @@protoc_insertion_point(module_scope)
