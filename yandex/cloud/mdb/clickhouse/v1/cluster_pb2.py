# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud.mdb.clickhouse.v1.config import clickhouse_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_config_dot_clickhouse__pb2
from yandex.cloud.mdb.clickhouse.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_maintenance__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/mdb/clickhouse/v1/cluster.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x36yandex/cloud/mdb/clickhouse/v1/config/clickhouse.proto\x1a\x30yandex/cloud/mdb/clickhouse/v1/maintenance.proto\x1a\x1dyandex/cloud/validation.proto\"\xc8\x08\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x43\n\x06labels\x18\x06 \x03(\x0b\x32\x33.yandex.cloud.mdb.clickhouse.v1.Cluster.LabelsEntry\x12H\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32\x33.yandex.cloud.mdb.clickhouse.v1.Cluster.Environment\x12>\n\nmonitoring\x18\x08 \x03(\x0b\x32*.yandex.cloud.mdb.clickhouse.v1.Monitoring\x12=\n\x06\x63onfig\x18\t \x01(\x0b\x32-.yandex.cloud.mdb.clickhouse.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12>\n\x06health\x18\x0b \x01(\x0e\x32..yandex.cloud.mdb.clickhouse.v1.Cluster.Health\x12>\n\x06status\x18\x0c \x01(\x0e\x32..yandex.cloud.mdb.clickhouse.v1.Cluster.Status\x12\x1a\n\x12service_account_id\x18\r \x01(\t\x12M\n\x12maintenance_window\x18\x0e \x01(\x0b\x32\x31.yandex.cloud.mdb.clickhouse.v1.MaintenanceWindow\x12O\n\x11planned_operation\x18\x0f \x01(\x0b\x32\x34.yandex.cloud.mdb.clickhouse.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x10 \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x11 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xfb\x05\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12L\n\nclickhouse\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.clickhouse.v1.ClusterConfig.Clickhouse\x12J\n\tzookeeper\x18\x03 \x01(\x0b\x32\x37.yandex.cloud.mdb.clickhouse.v1.ClusterConfig.Zookeeper\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x36\n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0b\x32&.yandex.cloud.mdb.clickhouse.v1.Access\x12\x43\n\rcloud_storage\x18\x06 \x01(\x0b\x32,.yandex.cloud.mdb.clickhouse.v1.CloudStorage\x12;\n\x17sql_database_management\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x13sql_user_management\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f\x65mbedded_keeper\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a\x96\x01\n\nClickhouse\x12J\n\x06\x63onfig\x18\x01 \x01(\x0b\x32:.yandex.cloud.mdb.clickhouse.v1.config.ClickhouseConfigSet\x12<\n\tresources\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.Resources\x1aI\n\tZookeeper\x12<\n\tresources\x18\x01 \x01(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.Resources\"f\n\x05Shard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12;\n\x06\x63onfig\x18\x03 \x01(\x0b\x32+.yandex.cloud.mdb.clickhouse.v1.ShardConfig\"X\n\nShardGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x13\n\x0bshard_names\x18\x04 \x03(\t\"\x9f\x02\n\x0bShardConfig\x12J\n\nclickhouse\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.clickhouse.v1.ShardConfig.Clickhouse\x1a\xc3\x01\n\nClickhouse\x12J\n\x06\x63onfig\x18\x01 \x01(\x0b\x32:.yandex.cloud.mdb.clickhouse.v1.config.ClickhouseConfigSet\x12<\n\tresources\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.Resources\x12+\n\x06weight\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xe0\x03\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x37\n\x04type\x18\x04 \x01(\x0e\x32).yandex.cloud.mdb.clickhouse.v1.Host.Type\x12<\n\tresources\x18\x05 \x01(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.Resources\x12;\n\x06health\x18\x06 \x01(\x0e\x32+.yandex.cloud.mdb.clickhouse.v1.Host.Health\x12\x39\n\x08services\x18\x07 \x03(\x0b\x32\'.yandex.cloud.mdb.clickhouse.v1.Service\x12\x11\n\tsubnet_id\x18\x08 \x01(\t\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\x12\x12\n\nshard_name\x18\n \x01(\t\";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCLICKHOUSE\x10\x01\x12\r\n\tZOOKEEPER\x10\x02\"8\n\x06Health\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"\xee\x01\n\x07Service\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.yandex.cloud.mdb.clickhouse.v1.Service.Type\x12>\n\x06health\x18\x02 \x01(\x0e\x32..yandex.cloud.mdb.clickhouse.v1.Service.Health\";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCLICKHOUSE\x10\x01\x12\r\n\tZOOKEEPER\x10\x02\"*\n\x06Health\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"~\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x12\x0f\n\x07web_sql\x18\x02 \x01(\x08\x12\x0f\n\x07metrika\x18\x03 \x01(\x08\x12\x12\n\nserverless\x18\x04 \x01(\x08\x12\x15\n\rdata_transfer\x18\x05 \x01(\x08\x12\x14\n\x0cyandex_query\x18\x06 \x01(\x08\"\x86\x02\n\x0c\x43loudStorage\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12:\n\x0bmove_factor\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x07\xfa\xc7\x31\x03\x30-1\x12\x36\n\x12\x64\x61ta_cache_enabled\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x13\x64\x61ta_cache_max_size\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x13prefer_not_to_merge\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValueBs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.clickhouse.v1.cluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'
  _CLUSTER_LABELSENTRY._options = None
  _CLUSTER_LABELSENTRY._serialized_options = b'8\001'
  _CLOUDSTORAGE.fields_by_name['move_factor']._options = None
  _CLOUDSTORAGE.fields_by_name['move_factor']._serialized_options = b'\372\3071\0030-1'
  _globals['_CLUSTER']._serialized_start=312
  _globals['_CLUSTER']._serialized_end=1408
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1100
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1145
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1147
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1220
  _globals['_CLUSTER_HEALTH']._serialized_start=1222
  _globals['_CLUSTER_HEALTH']._serialized_end=1285
  _globals['_CLUSTER_STATUS']._serialized_start=1287
  _globals['_CLUSTER_STATUS']._serialized_end=1408
  _globals['_MONITORING']._serialized_start=1410
  _globals['_MONITORING']._serialized_end=1471
  _globals['_CLUSTERCONFIG']._serialized_start=1474
  _globals['_CLUSTERCONFIG']._serialized_end=2237
  _globals['_CLUSTERCONFIG_CLICKHOUSE']._serialized_start=2012
  _globals['_CLUSTERCONFIG_CLICKHOUSE']._serialized_end=2162
  _globals['_CLUSTERCONFIG_ZOOKEEPER']._serialized_start=2164
  _globals['_CLUSTERCONFIG_ZOOKEEPER']._serialized_end=2237
  _globals['_SHARD']._serialized_start=2239
  _globals['_SHARD']._serialized_end=2341
  _globals['_SHARDGROUP']._serialized_start=2343
  _globals['_SHARDGROUP']._serialized_end=2431
  _globals['_SHARDCONFIG']._serialized_start=2434
  _globals['_SHARDCONFIG']._serialized_end=2721
  _globals['_SHARDCONFIG_CLICKHOUSE']._serialized_start=2526
  _globals['_SHARDCONFIG_CLICKHOUSE']._serialized_end=2721
  _globals['_HOST']._serialized_start=2724
  _globals['_HOST']._serialized_end=3204
  _globals['_HOST_TYPE']._serialized_start=3087
  _globals['_HOST_TYPE']._serialized_end=3146
  _globals['_HOST_HEALTH']._serialized_start=3148
  _globals['_HOST_HEALTH']._serialized_end=3204
  _globals['_SERVICE']._serialized_start=3207
  _globals['_SERVICE']._serialized_end=3445
  _globals['_SERVICE_TYPE']._serialized_start=3087
  _globals['_SERVICE_TYPE']._serialized_end=3146
  _globals['_SERVICE_HEALTH']._serialized_start=3148
  _globals['_SERVICE_HEALTH']._serialized_end=3190
  _globals['_RESOURCES']._serialized_start=3447
  _globals['_RESOURCES']._serialized_end=3527
  _globals['_ACCESS']._serialized_start=3529
  _globals['_ACCESS']._serialized_end=3655
  _globals['_CLOUDSTORAGE']._serialized_start=3658
  _globals['_CLOUDSTORAGE']._serialized_end=3920
# @@protoc_insertion_point(module_scope)
