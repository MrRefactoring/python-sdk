# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/stream_line.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/video/v1/stream_line.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8f\x06\n\nStreamLine\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x04 \x01(\t\x12:\n\trtmp_push\x18\xe8\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.RTMPPushInputH\x00\x12\x38\n\x08srt_push\x18\xe9\x07 \x01(\x0b\x32#.yandex.cloud.video.v1.SRTPushInputH\x00\x12:\n\trtmp_pull\x18\xea\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.RTMPPullInputH\x00\x12\x38\n\x08srt_pull\x18\xeb\x07 \x01(\x0b\x32#.yandex.cloud.video.v1.SRTPullInputH\x00\x12\x38\n\x08tcp_pull\x18\xec\x07 \x01(\x0b\x32#.yandex.cloud.video.v1.TCPPullInputH\x00\x12:\n\trtsp_pull\x18\xee\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.RTSPPullInputH\x00\x12\x39\n\x0bmanual_line\x18\xd0\x0f \x01(\x0b\x32!.yandex.cloud.video.v1.ManualLineH\x01\x12\x35\n\tauto_line\x18\xd1\x0f \x01(\x0b\x32\x1f.yandex.cloud.video.v1.AutoLineH\x01\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x06labels\x18\xc8\x01 \x03(\x0b\x32-.yandex.cloud.video.v1.StreamLine.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0c\n\ninput_typeB\x0b\n\tline_type\"\x1c\n\rPushStreamKey\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\rRTMPPushInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1b\n\x0cSRTPushInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\rRTMPPullInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1b\n\x0cSRTPullInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1b\n\x0cTCPPullInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\rRTSPPullInput\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x0c\n\nManualLine\"\x9b\x01\n\x08\x41utoLine\x12>\n\x06status\x18\x01 \x01(\x0e\x32..yandex.cloud.video.v1.AutoLine.AutoLineStatus\"O\n\x0e\x41utoLineStatus\x12 \n\x1c\x41UTO_LINE_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x44\x45\x41\x43TIVATED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x42\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.stream_line_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _STREAMLINE_LABELSENTRY._options = None
  _STREAMLINE_LABELSENTRY._serialized_options = b'8\001'
  _globals['_STREAMLINE']._serialized_start=100
  _globals['_STREAMLINE']._serialized_end=883
  _globals['_STREAMLINE_LABELSENTRY']._serialized_start=811
  _globals['_STREAMLINE_LABELSENTRY']._serialized_end=856
  _globals['_PUSHSTREAMKEY']._serialized_start=885
  _globals['_PUSHSTREAMKEY']._serialized_end=913
  _globals['_RTMPPUSHINPUT']._serialized_start=915
  _globals['_RTMPPUSHINPUT']._serialized_end=943
  _globals['_SRTPUSHINPUT']._serialized_start=945
  _globals['_SRTPUSHINPUT']._serialized_end=972
  _globals['_RTMPPULLINPUT']._serialized_start=974
  _globals['_RTMPPULLINPUT']._serialized_end=1002
  _globals['_SRTPULLINPUT']._serialized_start=1004
  _globals['_SRTPULLINPUT']._serialized_end=1031
  _globals['_TCPPULLINPUT']._serialized_start=1033
  _globals['_TCPPULLINPUT']._serialized_end=1060
  _globals['_RTSPPULLINPUT']._serialized_start=1062
  _globals['_RTSPPULLINPUT']._serialized_end=1090
  _globals['_MANUALLINE']._serialized_start=1092
  _globals['_MANUALLINE']._serialized_end=1104
  _globals['_AUTOLINE']._serialized_start=1107
  _globals['_AUTOLINE']._serialized_end=1262
  _globals['_AUTOLINE_AUTOLINESTATUS']._serialized_start=1183
  _globals['_AUTOLINE_AUTOLINESTATUS']._serialized_end=1262
# @@protoc_insertion_point(module_scope)
