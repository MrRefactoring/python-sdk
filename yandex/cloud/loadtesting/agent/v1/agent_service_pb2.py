# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/agent/v1/agent_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadtesting/agent/v1/agent_service.proto',
  package='yandex.cloud.loadtesting.agent.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5yandex/cloud/loadtesting/agent/v1/agent_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\"\xef\x01\n\x17\x43laimAgentStatusRequest\x12\x19\n\x11\x61gent_instance_id\x18\x01 \x01(\t\x12Q\n\x06status\x18\x02 \x01(\x0e\x32\x41.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest.Status\"f\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eREADY_FOR_TEST\x10\x01\x12\x12\n\x0ePREPARING_TEST\x10\x02\x12\x0b\n\x07TESTING\x10\x03\x12\x0f\n\x0bTANK_FAILED\x10\x04\"(\n\x18\x43laimAgentStatusResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x32\xe0\x01\n\x0c\x41gentService\x12\xcf\x01\n\x0b\x43laimStatus\x12:.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest\x1a;.yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusResponse\"G\x82\xd3\xe4\x93\x02\x41\"</loadtesting/agent/v1/agents/{agent_instance_id}/claimStatus:\x01*Bt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CLAIMAGENTSTATUSREQUEST_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest.Status',
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
      name='READY_FOR_TEST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PREPARING_TEST', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TESTING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TANK_FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=260,
  serialized_end=362,
)
_sym_db.RegisterEnumDescriptor(_CLAIMAGENTSTATUSREQUEST_STATUS)


_CLAIMAGENTSTATUSREQUEST = _descriptor.Descriptor(
  name='ClaimAgentStatusRequest',
  full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_instance_id', full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest.agent_instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLAIMAGENTSTATUSREQUEST_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=362,
)


_CLAIMAGENTSTATUSRESPONSE = _descriptor.Descriptor(
  name='ClaimAgentStatusResponse',
  full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusResponse.code', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=364,
  serialized_end=404,
)

_CLAIMAGENTSTATUSREQUEST.fields_by_name['status'].enum_type = _CLAIMAGENTSTATUSREQUEST_STATUS
_CLAIMAGENTSTATUSREQUEST_STATUS.containing_type = _CLAIMAGENTSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ClaimAgentStatusRequest'] = _CLAIMAGENTSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ClaimAgentStatusResponse'] = _CLAIMAGENTSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimAgentStatusRequest = _reflection.GeneratedProtocolMessageType('ClaimAgentStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMAGENTSTATUSREQUEST,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.agent_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusRequest)
  })
_sym_db.RegisterMessage(ClaimAgentStatusRequest)

ClaimAgentStatusResponse = _reflection.GeneratedProtocolMessageType('ClaimAgentStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMAGENTSTATUSRESPONSE,
  '__module__' : 'yandex.cloud.loadtesting.agent.v1.agent_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.agent.v1.ClaimAgentStatusResponse)
  })
_sym_db.RegisterMessage(ClaimAgentStatusResponse)


DESCRIPTOR._options = None

_AGENTSERVICE = _descriptor.ServiceDescriptor(
  name='AgentService',
  full_name='yandex.cloud.loadtesting.agent.v1.AgentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=407,
  serialized_end=631,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClaimStatus',
    full_name='yandex.cloud.loadtesting.agent.v1.AgentService.ClaimStatus',
    index=0,
    containing_service=None,
    input_type=_CLAIMAGENTSTATUSREQUEST,
    output_type=_CLAIMAGENTSTATUSRESPONSE,
    serialized_options=b'\202\323\344\223\002A\"</loadtesting/agent/v1/agents/{agent_instance_id}/claimStatus:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENTSERVICE)

DESCRIPTOR.services_by_name['AgentService'] = _AGENTSERVICE

# @@protoc_insertion_point(module_scope)