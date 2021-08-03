# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ydb/v1/backup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ydb/v1/backup.proto',
  package='yandex.cloud.ydb.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n yandex/cloud/ydb/v1/backup.proto\x12\x13yandex.cloud.ydb.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1dyandex/cloud/validation.proto\"\xc2\x02\n\x0e\x42\x61\x63kupSchedule\x12I\n\x15\x64\x61ily_backup_schedule\x18\x01 \x01(\x0b\x32(.yandex.cloud.ydb.v1.DailyBackupScheduleH\x00\x12K\n\x16weekly_backup_schedule\x18\x02 \x01(\x0b\x32).yandex.cloud.ydb.v1.WeeklyBackupScheduleH\x00\x12Q\n\x19recurring_backup_schedule\x18\x04 \x01(\x0b\x32,.yandex.cloud.ydb.v1.RecurringBackupScheduleH\x00\x12\x35\n\x11next_execute_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0e\n\x06policy\x12\x04\xc0\xc1\x31\x01\"i\n\x17RecurringBackupSchedule\x12\x34\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12\x18\n\nrecurrence\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"}\n\x18\x44\x61ysOfWeekBackupSchedule\x12-\n\x04\x64\x61ys\x18\x01 \x03(\x0e\x32\x16.google.type.DayOfWeekB\x07\x82\xc8\x31\x03\x31-7\x12\x32\n\x0c\x65xecute_time\x18\x02 \x01(\x0b\x32\x16.google.type.TimeOfDayB\x04\xe8\xc7\x31\x01\"d\n\x14WeeklyBackupSchedule\x12L\n\x0c\x64\x61ys_of_week\x18\x01 \x03(\x0b\x32-.yandex.cloud.ydb.v1.DaysOfWeekBackupScheduleB\x07\x82\xc8\x31\x03\x31-7\"I\n\x13\x44\x61ilyBackupSchedule\x12\x32\n\x0c\x65xecute_time\x18\x01 \x01(\x0b\x32\x16.google.type.TimeOfDayB\x04\xe8\xc7\x31\x01\"\xfe\x04\n\x0e\x42\x61\x63kupSettings\x12\x17\n\x04name\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12<\n\x0f\x62\x61\x63kup_schedule\x18\x03 \x01(\x0b\x32#.yandex.cloud.ydb.v1.BackupSchedule\x12\x36\n\x13\x62\x61\x63kup_time_to_live\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1f\n\x0csource_paths\x18\x05 \x03(\tB\t\x82\xc8\x31\x05<=256\x12*\n\x17source_paths_to_exclude\x18\x06 \x03(\tB\t\x82\xc8\x31\x05<=256\x12\x36\n\x04type\x18\x07 \x01(\x0e\x32(.yandex.cloud.ydb.v1.BackupSettings.Type\x12G\n\rstorage_class\x18\x08 \x01(\x0e\x32\x30.yandex.cloud.ydb.v1.BackupSettings.StorageClass\"2\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x08\n\x04USER\x10\x02\"\xba\x01\n\x0cStorageClass\x12\x1d\n\x19STORAGE_CLASS_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x16\n\x12REDUCED_REDUNDANCY\x10\x02\x12\x0f\n\x0bSTANDARD_IA\x10\x03\x12\x0e\n\nONEZONE_IA\x10\x04\x12\x17\n\x13INTELLIGENT_TIERING\x10\x05\x12\x0b\n\x07GLACIER\x10\x06\x12\x10\n\x0c\x44\x45\x45P_ARCHIVE\x10\x07\x12\x0c\n\x08OUTPOSTS\x10\x08\"L\n\x0c\x42\x61\x63kupConfig\x12<\n\x0f\x62\x61\x63kup_settings\x18\x01 \x03(\x0b\x32#.yandex.cloud.ydb.v1.BackupSettings\"\xaa\x04\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tfolder_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x63ompleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x06status\x18\t \x01(\x0e\x32\".yandex.cloud.ydb.v1.Backup.Status\x12<\n\x0f\x62\x61\x63kup_settings\x18\n \x01(\x0b\x32#.yandex.cloud.ydb.v1.BackupSettings\x12.\n\x04type\x18\x0b \x01(\x0e\x32 .yandex.cloud.ydb.v1.Backup.Type\x12\x0c\n\x04size\x18\x0c \x01(\x03\"S\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\r\n\tCANCELLED\x10\x04\"2\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x08\n\x04USER\x10\x02\x42V\n\x17yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydbb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_type_dot_timeofday__pb2.DESCRIPTOR,google_dot_type_dot_dayofweek__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_BACKUPSETTINGS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.ydb.v1.BackupSettings.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1347,
  serialized_end=1397,
)
_sym_db.RegisterEnumDescriptor(_BACKUPSETTINGS_TYPE)

_BACKUPSETTINGS_STORAGECLASS = _descriptor.EnumDescriptor(
  name='StorageClass',
  full_name='yandex.cloud.ydb.v1.BackupSettings.StorageClass',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORAGE_CLASS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCED_REDUNDANCY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STANDARD_IA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONEZONE_IA', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTELLIGENT_TIERING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GLACIER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEEP_ARCHIVE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUTPOSTS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1400,
  serialized_end=1586,
)
_sym_db.RegisterEnumDescriptor(_BACKUPSETTINGS_STORAGECLASS)

_BACKUP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.ydb.v1.Backup.Status',
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
      name='CANCELLED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2086,
  serialized_end=2169,
)
_sym_db.RegisterEnumDescriptor(_BACKUP_STATUS)

_BACKUP_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.ydb.v1.Backup.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1347,
  serialized_end=1397,
)
_sym_db.RegisterEnumDescriptor(_BACKUP_TYPE)


_BACKUPSCHEDULE = _descriptor.Descriptor(
  name='BackupSchedule',
  full_name='yandex.cloud.ydb.v1.BackupSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_backup_schedule', full_name='yandex.cloud.ydb.v1.BackupSchedule.daily_backup_schedule', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weekly_backup_schedule', full_name='yandex.cloud.ydb.v1.BackupSchedule.weekly_backup_schedule', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recurring_backup_schedule', full_name='yandex.cloud.ydb.v1.BackupSchedule.recurring_backup_schedule', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_execute_time', full_name='yandex.cloud.ydb.v1.BackupSchedule.next_execute_time', index=3,
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
    _descriptor.OneofDescriptor(
      name='policy', full_name='yandex.cloud.ydb.v1.BackupSchedule.policy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=212,
  serialized_end=534,
)


_RECURRINGBACKUPSCHEDULE = _descriptor.Descriptor(
  name='RecurringBackupSchedule',
  full_name='yandex.cloud.ydb.v1.RecurringBackupSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='yandex.cloud.ydb.v1.RecurringBackupSchedule.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recurrence', full_name='yandex.cloud.ydb.v1.RecurringBackupSchedule.recurrence', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=536,
  serialized_end=641,
)


_DAYSOFWEEKBACKUPSCHEDULE = _descriptor.Descriptor(
  name='DaysOfWeekBackupSchedule',
  full_name='yandex.cloud.ydb.v1.DaysOfWeekBackupSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='days', full_name='yandex.cloud.ydb.v1.DaysOfWeekBackupSchedule.days', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\0031-7', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execute_time', full_name='yandex.cloud.ydb.v1.DaysOfWeekBackupSchedule.execute_time', index=1,
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
  serialized_start=643,
  serialized_end=768,
)


_WEEKLYBACKUPSCHEDULE = _descriptor.Descriptor(
  name='WeeklyBackupSchedule',
  full_name='yandex.cloud.ydb.v1.WeeklyBackupSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='days_of_week', full_name='yandex.cloud.ydb.v1.WeeklyBackupSchedule.days_of_week', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\0031-7', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=770,
  serialized_end=870,
)


_DAILYBACKUPSCHEDULE = _descriptor.Descriptor(
  name='DailyBackupSchedule',
  full_name='yandex.cloud.ydb.v1.DailyBackupSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='execute_time', full_name='yandex.cloud.ydb.v1.DailyBackupSchedule.execute_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=872,
  serialized_end=945,
)


_BACKUPSETTINGS = _descriptor.Descriptor(
  name='BackupSettings',
  full_name='yandex.cloud.ydb.v1.BackupSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.ydb.v1.BackupSettings.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.ydb.v1.BackupSettings.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_schedule', full_name='yandex.cloud.ydb.v1.BackupSettings.backup_schedule', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_time_to_live', full_name='yandex.cloud.ydb.v1.BackupSettings.backup_time_to_live', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_paths', full_name='yandex.cloud.ydb.v1.BackupSettings.source_paths', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_paths_to_exclude', full_name='yandex.cloud.ydb.v1.BackupSettings.source_paths_to_exclude', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.ydb.v1.BackupSettings.type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_class', full_name='yandex.cloud.ydb.v1.BackupSettings.storage_class', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BACKUPSETTINGS_TYPE,
    _BACKUPSETTINGS_STORAGECLASS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=948,
  serialized_end=1586,
)


_BACKUPCONFIG = _descriptor.Descriptor(
  name='BackupConfig',
  full_name='yandex.cloud.ydb.v1.BackupConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backup_settings', full_name='yandex.cloud.ydb.v1.BackupConfig.backup_settings', index=0,
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
  serialized_start=1588,
  serialized_end=1664,
)


_BACKUP = _descriptor.Descriptor(
  name='Backup',
  full_name='yandex.cloud.ydb.v1.Backup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.ydb.v1.Backup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.ydb.v1.Backup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.ydb.v1.Backup.folder_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database_id', full_name='yandex.cloud.ydb.v1.Backup.database_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.ydb.v1.Backup.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.ydb.v1.Backup.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='yandex.cloud.ydb.v1.Backup.started_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed_at', full_name='yandex.cloud.ydb.v1.Backup.completed_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.ydb.v1.Backup.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_settings', full_name='yandex.cloud.ydb.v1.Backup.backup_settings', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.ydb.v1.Backup.type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='yandex.cloud.ydb.v1.Backup.size', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BACKUP_STATUS,
    _BACKUP_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1667,
  serialized_end=2221,
)

_BACKUPSCHEDULE.fields_by_name['daily_backup_schedule'].message_type = _DAILYBACKUPSCHEDULE
_BACKUPSCHEDULE.fields_by_name['weekly_backup_schedule'].message_type = _WEEKLYBACKUPSCHEDULE
_BACKUPSCHEDULE.fields_by_name['recurring_backup_schedule'].message_type = _RECURRINGBACKUPSCHEDULE
_BACKUPSCHEDULE.fields_by_name['next_execute_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUPSCHEDULE.oneofs_by_name['policy'].fields.append(
  _BACKUPSCHEDULE.fields_by_name['daily_backup_schedule'])
_BACKUPSCHEDULE.fields_by_name['daily_backup_schedule'].containing_oneof = _BACKUPSCHEDULE.oneofs_by_name['policy']
_BACKUPSCHEDULE.oneofs_by_name['policy'].fields.append(
  _BACKUPSCHEDULE.fields_by_name['weekly_backup_schedule'])
_BACKUPSCHEDULE.fields_by_name['weekly_backup_schedule'].containing_oneof = _BACKUPSCHEDULE.oneofs_by_name['policy']
_BACKUPSCHEDULE.oneofs_by_name['policy'].fields.append(
  _BACKUPSCHEDULE.fields_by_name['recurring_backup_schedule'])
_BACKUPSCHEDULE.fields_by_name['recurring_backup_schedule'].containing_oneof = _BACKUPSCHEDULE.oneofs_by_name['policy']
_RECURRINGBACKUPSCHEDULE.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DAYSOFWEEKBACKUPSCHEDULE.fields_by_name['days'].enum_type = google_dot_type_dot_dayofweek__pb2._DAYOFWEEK
_DAYSOFWEEKBACKUPSCHEDULE.fields_by_name['execute_time'].message_type = google_dot_type_dot_timeofday__pb2._TIMEOFDAY
_WEEKLYBACKUPSCHEDULE.fields_by_name['days_of_week'].message_type = _DAYSOFWEEKBACKUPSCHEDULE
_DAILYBACKUPSCHEDULE.fields_by_name['execute_time'].message_type = google_dot_type_dot_timeofday__pb2._TIMEOFDAY
_BACKUPSETTINGS.fields_by_name['backup_schedule'].message_type = _BACKUPSCHEDULE
_BACKUPSETTINGS.fields_by_name['backup_time_to_live'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_BACKUPSETTINGS.fields_by_name['type'].enum_type = _BACKUPSETTINGS_TYPE
_BACKUPSETTINGS.fields_by_name['storage_class'].enum_type = _BACKUPSETTINGS_STORAGECLASS
_BACKUPSETTINGS_TYPE.containing_type = _BACKUPSETTINGS
_BACKUPSETTINGS_STORAGECLASS.containing_type = _BACKUPSETTINGS
_BACKUPCONFIG.fields_by_name['backup_settings'].message_type = _BACKUPSETTINGS
_BACKUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUP.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUP.fields_by_name['completed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUP.fields_by_name['status'].enum_type = _BACKUP_STATUS
_BACKUP.fields_by_name['backup_settings'].message_type = _BACKUPSETTINGS
_BACKUP.fields_by_name['type'].enum_type = _BACKUP_TYPE
_BACKUP_STATUS.containing_type = _BACKUP
_BACKUP_TYPE.containing_type = _BACKUP
DESCRIPTOR.message_types_by_name['BackupSchedule'] = _BACKUPSCHEDULE
DESCRIPTOR.message_types_by_name['RecurringBackupSchedule'] = _RECURRINGBACKUPSCHEDULE
DESCRIPTOR.message_types_by_name['DaysOfWeekBackupSchedule'] = _DAYSOFWEEKBACKUPSCHEDULE
DESCRIPTOR.message_types_by_name['WeeklyBackupSchedule'] = _WEEKLYBACKUPSCHEDULE
DESCRIPTOR.message_types_by_name['DailyBackupSchedule'] = _DAILYBACKUPSCHEDULE
DESCRIPTOR.message_types_by_name['BackupSettings'] = _BACKUPSETTINGS
DESCRIPTOR.message_types_by_name['BackupConfig'] = _BACKUPCONFIG
DESCRIPTOR.message_types_by_name['Backup'] = _BACKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackupSchedule = _reflection.GeneratedProtocolMessageType('BackupSchedule', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSCHEDULE,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.BackupSchedule)
  })
_sym_db.RegisterMessage(BackupSchedule)

RecurringBackupSchedule = _reflection.GeneratedProtocolMessageType('RecurringBackupSchedule', (_message.Message,), {
  'DESCRIPTOR' : _RECURRINGBACKUPSCHEDULE,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.RecurringBackupSchedule)
  })
_sym_db.RegisterMessage(RecurringBackupSchedule)

DaysOfWeekBackupSchedule = _reflection.GeneratedProtocolMessageType('DaysOfWeekBackupSchedule', (_message.Message,), {
  'DESCRIPTOR' : _DAYSOFWEEKBACKUPSCHEDULE,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.DaysOfWeekBackupSchedule)
  })
_sym_db.RegisterMessage(DaysOfWeekBackupSchedule)

WeeklyBackupSchedule = _reflection.GeneratedProtocolMessageType('WeeklyBackupSchedule', (_message.Message,), {
  'DESCRIPTOR' : _WEEKLYBACKUPSCHEDULE,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.WeeklyBackupSchedule)
  })
_sym_db.RegisterMessage(WeeklyBackupSchedule)

DailyBackupSchedule = _reflection.GeneratedProtocolMessageType('DailyBackupSchedule', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBACKUPSCHEDULE,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.DailyBackupSchedule)
  })
_sym_db.RegisterMessage(DailyBackupSchedule)

BackupSettings = _reflection.GeneratedProtocolMessageType('BackupSettings', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSETTINGS,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.BackupSettings)
  })
_sym_db.RegisterMessage(BackupSettings)

BackupConfig = _reflection.GeneratedProtocolMessageType('BackupConfig', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPCONFIG,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.BackupConfig)
  })
_sym_db.RegisterMessage(BackupConfig)

Backup = _reflection.GeneratedProtocolMessageType('Backup', (_message.Message,), {
  'DESCRIPTOR' : _BACKUP,
  '__module__' : 'yandex.cloud.ydb.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.Backup)
  })
_sym_db.RegisterMessage(Backup)


DESCRIPTOR._options = None
_BACKUPSCHEDULE.oneofs_by_name['policy']._options = None
_RECURRINGBACKUPSCHEDULE.fields_by_name['start_time']._options = None
_RECURRINGBACKUPSCHEDULE.fields_by_name['recurrence']._options = None
_DAYSOFWEEKBACKUPSCHEDULE.fields_by_name['days']._options = None
_DAYSOFWEEKBACKUPSCHEDULE.fields_by_name['execute_time']._options = None
_WEEKLYBACKUPSCHEDULE.fields_by_name['days_of_week']._options = None
_DAILYBACKUPSCHEDULE.fields_by_name['execute_time']._options = None
_BACKUPSETTINGS.fields_by_name['name']._options = None
_BACKUPSETTINGS.fields_by_name['description']._options = None
_BACKUPSETTINGS.fields_by_name['source_paths']._options = None
_BACKUPSETTINGS.fields_by_name['source_paths_to_exclude']._options = None
# @@protoc_insertion_point(module_scope)
