# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/instancegroup/instance_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/compute/v1/instancegroup/instance_group.proto\x12%yandex.cloud.compute.v1.instancegroup\x1a\x1dyandex/cloud/validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xb5\x0b\n\rInstanceGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12P\n\x06labels\x18\x06 \x03(\x0b\x32@.yandex.cloud.compute.v1.instancegroup.InstanceGroup.LabelsEntry\x12R\n\x11instance_template\x18\x07 \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.InstanceTemplate\x12H\n\x0cscale_policy\x18\x08 \x01(\x0b\x32\x32.yandex.cloud.compute.v1.instancegroup.ScalePolicy\x12J\n\rdeploy_policy\x18\t \x01(\x0b\x32\x33.yandex.cloud.compute.v1.instancegroup.DeployPolicy\x12R\n\x11\x61llocation_policy\x18\n \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.AllocationPolicy\x12U\n\x13load_balancer_state\x18\x0b \x01(\x0b\x32\x38.yandex.cloud.compute.v1.instancegroup.LoadBalancerState\x12]\n\x17managed_instances_state\x18\x0c \x01(\x0b\x32<.yandex.cloud.compute.v1.instancegroup.ManagedInstancesState\x12S\n\x12load_balancer_spec\x18\x0e \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.LoadBalancerSpec\x12S\n\x12health_checks_spec\x18\x0f \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.HealthChecksSpec\x12\x1a\n\x12service_account_id\x18\x10 \x01(\t\x12K\n\x06status\x18\x11 \x01(\x0e\x32;.yandex.cloud.compute.v1.instancegroup.InstanceGroup.Status\x12\x42\n\tvariables\x18\x12 \x03(\x0b\x32/.yandex.cloud.compute.v1.instancegroup.Variable\x12\x1b\n\x13\x64\x65letion_protection\x18\x13 \x01(\x08\x12j\n\x1e\x61pplication_load_balancer_spec\x18\x14 \x01(\x0b\x32\x42.yandex.cloud.compute.v1.instancegroup.ApplicationLoadBalancerSpec\x12l\n\x1f\x61pplication_load_balancer_state\x18\x15 \x01(\x0b\x32\x43.yandex.cloud.compute.v1.instancegroup.ApplicationLoadBalancerState\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"o\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x0c\n\x08\x44\x45LETING\x10\x05\x12\n\n\x06PAUSED\x10\x06\"O\n\x1c\x41pplicationLoadBalancerState\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\"O\n\x08Variable\x12)\n\x03key\x18\x01 \x01(\tB\x1c\xf2\xc7\x31\x0f[a-zA-Z0-9._-]*\x8a\xc8\x31\x05\x31-128\x12\x18\n\x05value\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=128\"D\n\x11LoadBalancerState\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\"\xbf\x02\n\x15ManagedInstancesState\x12\x13\n\x0btarget_size\x18\x01 \x01(\x03\x12\x1c\n\x14running_actual_count\x18\x04 \x01(\x03\x12\x1e\n\x16running_outdated_count\x18\x05 \x01(\x03\x12\x18\n\x10processing_count\x18\x06 \x01(\x03\x1a\xb8\x01\n\x08Statuses\x12\x10\n\x08\x63reating\x18\x01 \x01(\x03\x12\x10\n\x08starting\x18\x02 \x01(\x03\x12\x0f\n\x07opening\x18\x03 \x01(\x03\x12\x0f\n\x07warming\x18\x04 \x01(\x03\x12\x0f\n\x07running\x18\x05 \x01(\x03\x12\x0f\n\x07\x63losing\x18\x06 \x01(\x03\x12\x10\n\x08stopping\x18\x07 \x01(\x03\x12\x10\n\x08updating\x18\x08 \x01(\x03\x12\x10\n\x08\x64\x65leting\x18\t \x01(\x03\x12\x0e\n\x06\x66\x61iled\x18\n \x01(\x03\"\x96\x0e\n\x0bScalePolicy\x12T\n\x0b\x66ixed_scale\x18\x01 \x01(\x0b\x32=.yandex.cloud.compute.v1.instancegroup.ScalePolicy.FixedScaleH\x00\x12R\n\nauto_scale\x18\x02 \x01(\x0b\x32<.yandex.cloud.compute.v1.instancegroup.ScalePolicy.AutoScaleH\x00\x12U\n\x0ftest_auto_scale\x18\x03 \x01(\x0b\x32<.yandex.cloud.compute.v1.instancegroup.ScalePolicy.AutoScale\x1a\xa7\x05\n\tAutoScale\x12 \n\rmin_zone_size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1b\n\x08max_size\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x43\n\x14measurement_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\xc7\x31\x06\x31m-10m\x12=\n\x0fwarmup_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=10m\x12\x45\n\x16stabilization_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\xc7\x31\x06\x31m-30m\x12\x1d\n\x0cinitial_size\x18\x06 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=1\x12\x63\n\x14\x63pu_utilization_rule\x18\x07 \x01(\x0b\x32\x45.yandex.cloud.compute.v1.instancegroup.ScalePolicy.CpuUtilizationRule\x12\\\n\x0c\x63ustom_rules\x18\x08 \x03(\x0b\x32=.yandex.cloud.compute.v1.instancegroup.ScalePolicy.CustomRuleB\x07\x82\xc8\x31\x03<=3\x12\x63\n\x0f\x61uto_scale_type\x18\t \x01(\x0e\x32J.yandex.cloud.compute.v1.instancegroup.ScalePolicy.AutoScale.AutoScaleType\"I\n\rAutoScaleType\x12\x1f\n\x1b\x41UTO_SCALE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ZONAL\x10\x01\x12\x0c\n\x08REGIONAL\x10\x02\x1a<\n\x12\x43puUtilizationRule\x12&\n\x12utilization_target\x18\x01 \x01(\x01\x42\n\xfa\xc7\x31\x06\x31\x30-100\x1a\xe2\x05\n\nCustomRule\x12_\n\trule_type\x18\x01 \x01(\x0e\x32\x46.yandex.cloud.compute.v1.instancegroup.ScalePolicy.CustomRule.RuleTypeB\x04\xe8\xc7\x31\x01\x12\x63\n\x0bmetric_type\x18\x02 \x01(\x0e\x32H.yandex.cloud.compute.v1.instancegroup.ScalePolicy.CustomRule.MetricTypeB\x04\xe8\xc7\x31\x01\x12O\n\x0bmetric_name\x18\x03 \x01(\tB:\xe8\xc7\x31\x01\xf2\xc7\x31\x32[a-zA-Z0-9./@_][ 0-9a-zA-Z./@_,:;()\\[\\]<>-]{0,198}\x12\xb3\x01\n\x06labels\x18\x05 \x03(\x0b\x32I.yandex.cloud.compute.v1.instancegroup.ScalePolicy.CustomRule.LabelsEntryBX\xf2\xc7\x31\x32[a-zA-Z0-9./@_][ 0-9a-zA-Z./@_,:;()\\[\\]<>-]{0,198}\xb2\xc8\x31\x1e\x12\x1c^[a-zA-Z][0-9a-zA-Z_]{0,31}$\x12\x16\n\x06target\x18\x04 \x01(\x01\x42\x06\xfa\xc7\x31\x02>0\x12\x1b\n\tfolder_id\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1a\n\x07service\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=200\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\x08RuleType\x12\x19\n\x15RULE_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUTILIZATION\x10\x01\x12\x0c\n\x08WORKLOAD\x10\x02\"A\n\nMetricType\x12\x1b\n\x17METRIC_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\x0b\n\x07\x43OUNTER\x10\x02\x1a%\n\nFixedScale\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100B\x12\n\nscale_type\x12\x04\xc0\xc1\x31\x01\"\xee\x02\n\x0c\x44\x65ployPolicy\x12\"\n\x0fmax_unavailable\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1f\n\x0cmax_deleting\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1f\n\x0cmax_creating\x18\x03 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12 \n\rmax_expansion\x18\x06 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12>\n\x10startup_duration\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x30m-1h\x12N\n\x08strategy\x18\x08 \x01(\x0e\x32<.yandex.cloud.compute.v1.instancegroup.DeployPolicy.Strategy\"F\n\x08Strategy\x12\x18\n\x14STRATEGY_UNSPECIFIED\x10\x00\x12\r\n\tPROACTIVE\x10\x01\x12\x11\n\rOPPORTUNISTIC\x10\x02\"\xb1\x01\n\x10\x41llocationPolicy\x12T\n\x05zones\x18\x01 \x03(\x0b\x32<.yandex.cloud.compute.v1.instancegroup.AllocationPolicy.ZoneB\x07\x82\xc8\x31\x03>=1\x1aG\n\x04Zone\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x12instance_tags_pool\x18\x02 \x03(\tB\x0c\x8a\xc8\x31\x04\x33-50\x90\xc8\x31\x01\"\xd6\t\n\x10InstanceTemplate\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x86\x01\n\x06labels\x18\x02 \x03(\x0b\x32\x43.yandex.cloud.compute.v1.instancegroup.InstanceTemplate.LabelsEntryB1\x82\xc8\x31\x04<=64\x8a\xc8\x31\x05<=128\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x19\n\x0bplatform_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\x12R\n\x0eresources_spec\x18\x04 \x01(\x0b\x32\x34.yandex.cloud.compute.v1.instancegroup.ResourcesSpecB\x04\xe8\xc7\x31\x01\x12\x8a\x01\n\x08metadata\x18\x05 \x03(\x0b\x32\x45.yandex.cloud.compute.v1.instancegroup.InstanceTemplate.MetadataEntryB1\x82\xc8\x31\x05<=128\x8a\xc8\x31\x08<=262144\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12U\n\x0e\x62oot_disk_spec\x18\x06 \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.AttachedDiskSpecB\x04\xe8\xc7\x31\x01\x12^\n\x14secondary_disk_specs\x18\x07 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.AttachedDiskSpecB\x07\x82\xc8\x31\x03<=3\x12\x63\n\x17network_interface_specs\x18\x08 \x03(\x0b\x32;.yandex.cloud.compute.v1.instancegroup.NetworkInterfaceSpecB\x05\x82\xc8\x31\x01\x31\x12R\n\x11scheduling_policy\x18\t \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.SchedulingPolicy\x12\x1a\n\x12service_account_id\x18\n \x01(\t\x12P\n\x10network_settings\x18\x0b \x01(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.NetworkSettings\x12\x17\n\x04name\x18\x0c \x01(\tB\t\x8a\xc8\x31\x05<=128\x12\x1b\n\x08hostname\x18\r \x01(\tB\t\x8a\xc8\x31\x05<=128\x12P\n\x10placement_policy\x18\x0e \x01(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.PlacementPolicy\x12W\n\x10\x66ilesystem_specs\x18\x0f \x03(\x0b\x32=.yandex.cloud.compute.v1.instancegroup.AttachedFilesystemSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8f\x02\n\x16\x41ttachedFilesystemSpec\x12P\n\x04mode\x18\x01 \x01(\x0e\x32\x42.yandex.cloud.compute.v1.instancegroup.AttachedFilesystemSpec.Mode\x12/\n\x0b\x64\x65vice_name\x18\x02 \x01(\tB\x1a\xf2\xc7\x31\x16|[a-z][-_0-9a-z]{0,19}\x12\x35\n\rfilesystem_id\x18\x03 \x01(\tB\x1e\xf2\xc7\x31\x11[-a-zA-Z0-9._{}]*\x8a\xc8\x31\x05<=128\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\"\xdd\x02\n\x0fPlacementPolicy\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\x12\x64\n\x13host_affinity_rules\x18\x02 \x03(\x0b\x32G.yandex.cloud.compute.v1.instancegroup.PlacementPolicy.HostAffinityRule\x1a\xc7\x01\n\x10HostAffinityRule\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\\\n\x02op\x18\x02 \x01(\x0e\x32P.yandex.cloud.compute.v1.instancegroup.PlacementPolicy.HostAffinityRule.Operator\x12\x0e\n\x06values\x18\x03 \x03(\t\"8\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x06\n\x02IN\x10\x01\x12\n\n\x06NOT_IN\x10\x02\"\xdf\x01\n\rResourcesSpec\x12\"\n\x06memory\x18\x01 \x01(\x03\x42\x12\xfa\xc7\x31\x0e<=824633720832\x12\x65\n\x05\x63ores\x18\x02 \x01(\x03\x42V\xfa\xc7\x31R2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64,68,72,76,80\x12(\n\rcore_fraction\x18\x03 \x01(\x03\x42\x11\xfa\xc7\x31\r0,5,20,50,100\x12\x19\n\x04gpus\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30,1,2,4\"\xdc\x04\n\x10\x41ttachedDiskSpec\x12P\n\x04mode\x18\x01 \x01(\x0e\x32<.yandex.cloud.compute.v1.instancegroup.AttachedDiskSpec.ModeB\x04\xe8\xc7\x31\x01\x12/\n\x0b\x64\x65vice_name\x18\x02 \x01(\tB\x1a\xf2\xc7\x31\x16|[a-z][-_0-9a-z]{0,19}\x12Y\n\tdisk_spec\x18\x03 \x01(\x0b\x32@.yandex.cloud.compute.v1.instancegroup.AttachedDiskSpec.DiskSpecB\x04\xe8\xc7\x31\x01\x12/\n\x07\x64isk_id\x18\x04 \x01(\tB\x1e\xf2\xc7\x31\x11[-a-zA-Z0-9._{}]*\x8a\xc8\x31\x05<=128\x12\x17\n\x04name\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=128\x1a\xe2\x01\n\x08\x44iskSpec\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x15\n\x07type_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x04size\x18\x03 \x01(\x03\x42\x1a\xfa\xc7\x31\x16\x34\x31\x39\x34\x33\x30\x34-28587302322176\x12\x1c\n\x08image_id\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1f\n\x0bsnapshot_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12&\n\x1epreserve_after_instance_delete\x18\x06 \x01(\x08\x42\x0e\n\x0csource_oneof\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\"\x92\x02\n\x14NetworkInterfaceSpec\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x12\n\nsubnet_ids\x18\x02 \x03(\t\x12Z\n\x17primary_v4_address_spec\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.compute.v1.instancegroup.PrimaryAddressSpec\x12Z\n\x17primary_v6_address_spec\x18\x04 \x01(\x0b\x32\x39.yandex.cloud.compute.v1.instancegroup.PrimaryAddressSpec\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\"\xca\x01\n\x12PrimaryAddressSpec\x12S\n\x13one_to_one_nat_spec\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.OneToOneNatSpec\x12N\n\x10\x64ns_record_specs\x18\x02 \x03(\x0b\x32\x34.yandex.cloud.compute.v1.instancegroup.DnsRecordSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\xb8\x01\n\x0fOneToOneNatSpec\x12\x44\n\nip_version\x18\x01 \x01(\x0e\x32\x30.yandex.cloud.compute.v1.instancegroup.IpVersion\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12N\n\x10\x64ns_record_specs\x18\x03 \x03(\x0b\x32\x34.yandex.cloud.compute.v1.instancegroup.DnsRecordSpec\"_\n\rDnsRecordSpec\x12\x12\n\x04\x66qdn\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x64ns_zone_id\x18\x02 \x01(\t\x12\x18\n\x03ttl\x18\x03 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\x12\x0b\n\x03ptr\x18\x04 \x01(\x08\"\'\n\x10SchedulingPolicy\x12\x13\n\x0bpreemptible\x18\x01 \x01(\x08\"\xbc\x01\n\x0fNetworkSettings\x12I\n\x04type\x18\x01 \x01(\x0e\x32;.yandex.cloud.compute.v1.instancegroup.NetworkSettings.Type\"^\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x18\n\x14SOFTWARE_ACCELERATED\x10\x02\x12\x18\n\x14HARDWARE_ACCELERATED\x10\x03\"\xce\x01\n\x10LoadBalancerSpec\x12Q\n\x11target_group_spec\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.TargetGroupSpec\x12I\n\x1cmax_opening_traffic_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\xc7\x31\x04>=1s\x12\x1c\n\x14ignore_health_checks\x18\x04 \x01(\x08\"\xae\x02\n\x0fTargetGroupSpec\x12\x32\n\x04name\x18\x01 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x97\x01\n\x06labels\x18\x03 \x03(\x0b\x32\x42.yandex.cloud.compute.v1.instancegroup.TargetGroupSpec.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xea\x01\n\x1b\x41pplicationLoadBalancerSpec\x12\x62\n\x11target_group_spec\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.compute.v1.instancegroup.ApplicationTargetGroupSpecB\x04\xe8\xc7\x31\x01\x12I\n\x1cmax_opening_traffic_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\xc7\x31\x04>=1s\x12\x1c\n\x14ignore_health_checks\x18\x03 \x01(\x08\"\xcd\x01\n\x1a\x41pplicationTargetGroupSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12]\n\x06labels\x18\x03 \x03(\x0b\x32M.yandex.cloud.compute.v1.instancegroup.ApplicationTargetGroupSpec.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x01\n\x10HealthChecksSpec\x12[\n\x12health_check_specs\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.HealthCheckSpecB\x07\x82\xc8\x31\x03>=1\x12I\n\x1cmax_checking_health_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\xc7\x31\x04>=1s\"\xa4\x04\n\x0fHealthCheckSpec\x12\x38\n\x08interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\xc7\x31\x07\x31s-300s\x12\x36\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\xc7\x31\x06\x31s-60s\x12\x35\n\x13unhealthy_threshold\x18\x03 \x01(\x03\x42\x18\xfa\xc7\x31\x14\x30,2,3,4,5,6,7,8,9,10\x12\x33\n\x11healthy_threshold\x18\x04 \x01(\x03\x42\x18\xfa\xc7\x31\x14\x30,2,3,4,5,6,7,8,9,10\x12X\n\x0btcp_options\x18\x05 \x01(\x0b\x32\x41.yandex.cloud.compute.v1.instancegroup.HealthCheckSpec.TcpOptionsH\x00\x12Z\n\x0chttp_options\x18\x06 \x01(\x0b\x32\x42.yandex.cloud.compute.v1.instancegroup.HealthCheckSpec.HttpOptionsH\x00\x1a\'\n\nTcpOptions\x12\x19\n\x04port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65535\x1a\x36\n\x0bHttpOptions\x12\x19\n\x04port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65535\x12\x0c\n\x04path\x18\x02 \x01(\tB\x1c\n\x14health_check_options\x12\x04\xc0\xc1\x31\x01\"\xd7\x05\n\x0fManagedInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12M\n\x06status\x18\x02 \x01(\x0e\x32=.yandex.cloud.compute.v1.instancegroup.ManagedInstance.Status\x12\x13\n\x0binstance_id\x18\x03 \x01(\t\x12\x0c\n\x04\x66qdn\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x16\n\x0estatus_message\x18\x06 \x01(\t\x12\x0f\n\x07zone_id\x18\x07 \x01(\t\x12S\n\x12network_interfaces\x18\x08 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.NetworkInterface\x12\x35\n\x11status_changed_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cinstance_tag\x18\x0e \x01(\t\"\xec\x02\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11\x43REATING_INSTANCE\x10\x0b\x12\x15\n\x11UPDATING_INSTANCE\x10\x0c\x12\x15\n\x11\x44\x45LETING_INSTANCE\x10\r\x12\x15\n\x11STARTING_INSTANCE\x10\x0e\x12\x15\n\x11STOPPING_INSTANCE\x10\x0f\x12\x1d\n\x19\x41WAITING_STARTUP_DURATION\x10\x10\x12\x13\n\x0f\x43HECKING_HEALTH\x10\x11\x12\x13\n\x0fOPENING_TRAFFIC\x10\x12\x12\x1c\n\x18\x41WAITING_WARMUP_DURATION\x10\x13\x12\x13\n\x0f\x43LOSING_TRAFFIC\x10\x14\x12\x12\n\x0eRUNNING_ACTUAL\x10\x15\x12\x14\n\x10RUNNING_OUTDATED\x10\x16\x12\x0b\n\x07STOPPED\x10\x17\x12\x0b\n\x07\x44\x45LETED\x10\x18\x12\x17\n\x13PREPARING_RESOURCES\x10\x19\"\xef\x01\n\x10NetworkInterface\x12\r\n\x05index\x18\x01 \x01(\t\x12\x13\n\x0bmac_address\x18\x02 \x01(\t\x12\x11\n\tsubnet_id\x18\x03 \x01(\t\x12Q\n\x12primary_v4_address\x18\x04 \x01(\x0b\x32\x35.yandex.cloud.compute.v1.instancegroup.PrimaryAddress\x12Q\n\x12primary_v6_address\x18\x05 \x01(\x0b\x32\x35.yandex.cloud.compute.v1.instancegroup.PrimaryAddress\"\xb4\x01\n\x0ePrimaryAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12J\n\x0eone_to_one_nat\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.compute.v1.instancegroup.OneToOneNat\x12\x45\n\x0b\x64ns_records\x18\x03 \x03(\x0b\x32\x30.yandex.cloud.compute.v1.instancegroup.DnsRecord\"\xab\x01\n\x0bOneToOneNat\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x44\n\nip_version\x18\x02 \x01(\x0e\x32\x30.yandex.cloud.compute.v1.instancegroup.IpVersion\x12\x45\n\x0b\x64ns_records\x18\x03 \x03(\x0b\x32\x30.yandex.cloud.compute.v1.instancegroup.DnsRecord\"[\n\tDnsRecord\x12\x12\n\x04\x66qdn\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x64ns_zone_id\x18\x02 \x01(\t\x12\x18\n\x03ttl\x18\x03 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\x12\x0b\n\x03ptr\x18\x04 \x01(\x08\"K\n\tLogRecord\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07message\x18\x02 \x01(\t*;\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42\x84\x01\n)yandex.cloud.api.compute.v1.instancegroupZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1/instancegroup;instancegroupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.instancegroup.instance_group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.compute.v1.instancegroupZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1/instancegroup;instancegroup'
  _INSTANCEGROUP_LABELSENTRY._options = None
  _INSTANCEGROUP_LABELSENTRY._serialized_options = b'8\001'
  _VARIABLE.fields_by_name['key']._options = None
  _VARIABLE.fields_by_name['key']._serialized_options = b'\362\3071\017[a-zA-Z0-9._-]*\212\3101\0051-128'
  _VARIABLE.fields_by_name['value']._options = None
  _VARIABLE.fields_by_name['value']._serialized_options = b'\212\3101\005<=128'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['min_zone_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['min_zone_size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['max_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['max_size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['measurement_duration']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['measurement_duration']._serialized_options = b'\372\3071\0061m-10m'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['warmup_duration']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['warmup_duration']._serialized_options = b'\372\3071\005<=10m'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['stabilization_duration']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['stabilization_duration']._serialized_options = b'\372\3071\0061m-30m'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['initial_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['initial_size']._serialized_options = b'\372\3071\003>=1'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['custom_rules']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['custom_rules']._serialized_options = b'\202\3101\003<=3'
  _SCALEPOLICY_CPUUTILIZATIONRULE.fields_by_name['utilization_target']._options = None
  _SCALEPOLICY_CPUUTILIZATIONRULE.fields_by_name['utilization_target']._serialized_options = b'\372\3071\00610-100'
  _SCALEPOLICY_CUSTOMRULE_LABELSENTRY._options = None
  _SCALEPOLICY_CUSTOMRULE_LABELSENTRY._serialized_options = b'8\001'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['rule_type']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['rule_type']._serialized_options = b'\350\3071\001'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['metric_type']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['metric_type']._serialized_options = b'\350\3071\001'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['metric_name']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['metric_name']._serialized_options = b'\350\3071\001\362\30712[a-zA-Z0-9./@_][ 0-9a-zA-Z./@_,:;()\\[\\]<>-]{0,198}'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['labels']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['labels']._serialized_options = b'\362\30712[a-zA-Z0-9./@_][ 0-9a-zA-Z./@_,:;()\\[\\]<>-]{0,198}\262\3101\036\022\034^[a-zA-Z][0-9a-zA-Z_]{0,31}$'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['target']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['target']._serialized_options = b'\372\3071\002>0'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['folder_id']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['service']._options = None
  _SCALEPOLICY_CUSTOMRULE.fields_by_name['service']._serialized_options = b'\212\3101\005<=200'
  _SCALEPOLICY_FIXEDSCALE.fields_by_name['size']._options = None
  _SCALEPOLICY_FIXEDSCALE.fields_by_name['size']._serialized_options = b'\372\3071\0051-100'
  _SCALEPOLICY.oneofs_by_name['scale_type']._options = None
  _SCALEPOLICY.oneofs_by_name['scale_type']._serialized_options = b'\300\3011\001'
  _DEPLOYPOLICY.fields_by_name['max_unavailable']._options = None
  _DEPLOYPOLICY.fields_by_name['max_unavailable']._serialized_options = b'\372\3071\0050-100'
  _DEPLOYPOLICY.fields_by_name['max_deleting']._options = None
  _DEPLOYPOLICY.fields_by_name['max_deleting']._serialized_options = b'\372\3071\0050-100'
  _DEPLOYPOLICY.fields_by_name['max_creating']._options = None
  _DEPLOYPOLICY.fields_by_name['max_creating']._serialized_options = b'\372\3071\0050-100'
  _DEPLOYPOLICY.fields_by_name['max_expansion']._options = None
  _DEPLOYPOLICY.fields_by_name['max_expansion']._serialized_options = b'\372\3071\0050-100'
  _DEPLOYPOLICY.fields_by_name['startup_duration']._options = None
  _DEPLOYPOLICY.fields_by_name['startup_duration']._serialized_options = b'\372\3071\0050m-1h'
  _ALLOCATIONPOLICY_ZONE.fields_by_name['zone_id']._options = None
  _ALLOCATIONPOLICY_ZONE.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _ALLOCATIONPOLICY_ZONE.fields_by_name['instance_tags_pool']._options = None
  _ALLOCATIONPOLICY_ZONE.fields_by_name['instance_tags_pool']._serialized_options = b'\212\3101\0043-50\220\3101\001'
  _ALLOCATIONPOLICY.fields_by_name['zones']._options = None
  _ALLOCATIONPOLICY.fields_by_name['zones']._serialized_options = b'\202\3101\003>=1'
  _INSTANCETEMPLATE_LABELSENTRY._options = None
  _INSTANCETEMPLATE_LABELSENTRY._serialized_options = b'8\001'
  _INSTANCETEMPLATE_METADATAENTRY._options = None
  _INSTANCETEMPLATE_METADATAENTRY._serialized_options = b'8\001'
  _INSTANCETEMPLATE.fields_by_name['description']._options = None
  _INSTANCETEMPLATE.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _INSTANCETEMPLATE.fields_by_name['labels']._options = None
  _INSTANCETEMPLATE.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\005<=128\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _INSTANCETEMPLATE.fields_by_name['platform_id']._options = None
  _INSTANCETEMPLATE.fields_by_name['platform_id']._serialized_options = b'\350\3071\001'
  _INSTANCETEMPLATE.fields_by_name['resources_spec']._options = None
  _INSTANCETEMPLATE.fields_by_name['resources_spec']._serialized_options = b'\350\3071\001'
  _INSTANCETEMPLATE.fields_by_name['metadata']._options = None
  _INSTANCETEMPLATE.fields_by_name['metadata']._serialized_options = b'\202\3101\005<=128\212\3101\010<=262144\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _INSTANCETEMPLATE.fields_by_name['boot_disk_spec']._options = None
  _INSTANCETEMPLATE.fields_by_name['boot_disk_spec']._serialized_options = b'\350\3071\001'
  _INSTANCETEMPLATE.fields_by_name['secondary_disk_specs']._options = None
  _INSTANCETEMPLATE.fields_by_name['secondary_disk_specs']._serialized_options = b'\202\3101\003<=3'
  _INSTANCETEMPLATE.fields_by_name['network_interface_specs']._options = None
  _INSTANCETEMPLATE.fields_by_name['network_interface_specs']._serialized_options = b'\202\3101\0011'
  _INSTANCETEMPLATE.fields_by_name['name']._options = None
  _INSTANCETEMPLATE.fields_by_name['name']._serialized_options = b'\212\3101\005<=128'
  _INSTANCETEMPLATE.fields_by_name['hostname']._options = None
  _INSTANCETEMPLATE.fields_by_name['hostname']._serialized_options = b'\212\3101\005<=128'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['device_name']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['device_name']._serialized_options = b'\362\3071\026|[a-z][-_0-9a-z]{0,19}'
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['filesystem_id']._options = None
  _ATTACHEDFILESYSTEMSPEC.fields_by_name['filesystem_id']._serialized_options = b'\362\3071\021[-a-zA-Z0-9._{}]*\212\3101\005<=128'
  _RESOURCESSPEC.fields_by_name['memory']._options = None
  _RESOURCESSPEC.fields_by_name['memory']._serialized_options = b'\372\3071\016<=824633720832'
  _RESOURCESSPEC.fields_by_name['cores']._options = None
  _RESOURCESSPEC.fields_by_name['cores']._serialized_options = b'\372\3071R2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64,68,72,76,80'
  _RESOURCESSPEC.fields_by_name['core_fraction']._options = None
  _RESOURCESSPEC.fields_by_name['core_fraction']._serialized_options = b'\372\3071\r0,5,20,50,100'
  _RESOURCESSPEC.fields_by_name['gpus']._options = None
  _RESOURCESSPEC.fields_by_name['gpus']._serialized_options = b'\372\3071\0070,1,2,4'
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['description']._options = None
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['type_id']._options = None
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['type_id']._serialized_options = b'\350\3071\001'
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['size']._options = None
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['size']._serialized_options = b'\372\3071\0264194304-28587302322176'
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['image_id']._options = None
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['image_id']._serialized_options = b'\212\3101\004<=50'
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['snapshot_id']._options = None
  _ATTACHEDDISKSPEC_DISKSPEC.fields_by_name['snapshot_id']._serialized_options = b'\212\3101\004<=50'
  _ATTACHEDDISKSPEC.fields_by_name['mode']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['mode']._serialized_options = b'\350\3071\001'
  _ATTACHEDDISKSPEC.fields_by_name['device_name']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['device_name']._serialized_options = b'\362\3071\026|[a-z][-_0-9a-z]{0,19}'
  _ATTACHEDDISKSPEC.fields_by_name['disk_spec']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['disk_spec']._serialized_options = b'\350\3071\001'
  _ATTACHEDDISKSPEC.fields_by_name['disk_id']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['disk_id']._serialized_options = b'\362\3071\021[-a-zA-Z0-9._{}]*\212\3101\005<=128'
  _ATTACHEDDISKSPEC.fields_by_name['name']._options = None
  _ATTACHEDDISKSPEC.fields_by_name['name']._serialized_options = b'\212\3101\005<=128'
  _DNSRECORDSPEC.fields_by_name['fqdn']._options = None
  _DNSRECORDSPEC.fields_by_name['fqdn']._serialized_options = b'\350\3071\001'
  _DNSRECORDSPEC.fields_by_name['ttl']._options = None
  _DNSRECORDSPEC.fields_by_name['ttl']._serialized_options = b'\372\3071\0070-86400'
  _LOADBALANCERSPEC.fields_by_name['max_opening_traffic_duration']._options = None
  _LOADBALANCERSPEC.fields_by_name['max_opening_traffic_duration']._serialized_options = b'\372\3071\004>=1s'
  _TARGETGROUPSPEC_LABELSENTRY._options = None
  _TARGETGROUPSPEC_LABELSENTRY._serialized_options = b'8\001'
  _TARGETGROUPSPEC.fields_by_name['name']._options = None
  _TARGETGROUPSPEC.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _TARGETGROUPSPEC.fields_by_name['description']._options = None
  _TARGETGROUPSPEC.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _TARGETGROUPSPEC.fields_by_name['labels']._options = None
  _TARGETGROUPSPEC.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _APPLICATIONLOADBALANCERSPEC.fields_by_name['target_group_spec']._options = None
  _APPLICATIONLOADBALANCERSPEC.fields_by_name['target_group_spec']._serialized_options = b'\350\3071\001'
  _APPLICATIONLOADBALANCERSPEC.fields_by_name['max_opening_traffic_duration']._options = None
  _APPLICATIONLOADBALANCERSPEC.fields_by_name['max_opening_traffic_duration']._serialized_options = b'\372\3071\004>=1s'
  _APPLICATIONTARGETGROUPSPEC_LABELSENTRY._options = None
  _APPLICATIONTARGETGROUPSPEC_LABELSENTRY._serialized_options = b'8\001'
  _HEALTHCHECKSSPEC.fields_by_name['health_check_specs']._options = None
  _HEALTHCHECKSSPEC.fields_by_name['health_check_specs']._serialized_options = b'\202\3101\003>=1'
  _HEALTHCHECKSSPEC.fields_by_name['max_checking_health_duration']._options = None
  _HEALTHCHECKSSPEC.fields_by_name['max_checking_health_duration']._serialized_options = b'\372\3071\004>=1s'
  _HEALTHCHECKSPEC_TCPOPTIONS.fields_by_name['port']._options = None
  _HEALTHCHECKSPEC_TCPOPTIONS.fields_by_name['port']._serialized_options = b'\372\3071\0071-65535'
  _HEALTHCHECKSPEC_HTTPOPTIONS.fields_by_name['port']._options = None
  _HEALTHCHECKSPEC_HTTPOPTIONS.fields_by_name['port']._serialized_options = b'\372\3071\0071-65535'
  _HEALTHCHECKSPEC.oneofs_by_name['health_check_options']._options = None
  _HEALTHCHECKSPEC.oneofs_by_name['health_check_options']._serialized_options = b'\300\3011\001'
  _HEALTHCHECKSPEC.fields_by_name['interval']._options = None
  _HEALTHCHECKSPEC.fields_by_name['interval']._serialized_options = b'\372\3071\0071s-300s'
  _HEALTHCHECKSPEC.fields_by_name['timeout']._options = None
  _HEALTHCHECKSPEC.fields_by_name['timeout']._serialized_options = b'\372\3071\0061s-60s'
  _HEALTHCHECKSPEC.fields_by_name['unhealthy_threshold']._options = None
  _HEALTHCHECKSPEC.fields_by_name['unhealthy_threshold']._serialized_options = b'\372\3071\0240,2,3,4,5,6,7,8,9,10'
  _HEALTHCHECKSPEC.fields_by_name['healthy_threshold']._options = None
  _HEALTHCHECKSPEC.fields_by_name['healthy_threshold']._serialized_options = b'\372\3071\0240,2,3,4,5,6,7,8,9,10'
  _DNSRECORD.fields_by_name['fqdn']._options = None
  _DNSRECORD.fields_by_name['fqdn']._serialized_options = b'\350\3071\001'
  _DNSRECORD.fields_by_name['ttl']._options = None
  _DNSRECORD.fields_by_name['ttl']._serialized_options = b'\372\3071\0070-86400'
  _globals['_IPVERSION']._serialized_start=11477
  _globals['_IPVERSION']._serialized_end=11536
  _globals['_INSTANCEGROUP']._serialized_start=198
  _globals['_INSTANCEGROUP']._serialized_end=1659
  _globals['_INSTANCEGROUP_LABELSENTRY']._serialized_start=1501
  _globals['_INSTANCEGROUP_LABELSENTRY']._serialized_end=1546
  _globals['_INSTANCEGROUP_STATUS']._serialized_start=1548
  _globals['_INSTANCEGROUP_STATUS']._serialized_end=1659
  _globals['_APPLICATIONLOADBALANCERSTATE']._serialized_start=1661
  _globals['_APPLICATIONLOADBALANCERSTATE']._serialized_end=1740
  _globals['_VARIABLE']._serialized_start=1742
  _globals['_VARIABLE']._serialized_end=1821
  _globals['_LOADBALANCERSTATE']._serialized_start=1823
  _globals['_LOADBALANCERSTATE']._serialized_end=1891
  _globals['_MANAGEDINSTANCESSTATE']._serialized_start=1894
  _globals['_MANAGEDINSTANCESSTATE']._serialized_end=2213
  _globals['_MANAGEDINSTANCESSTATE_STATUSES']._serialized_start=2029
  _globals['_MANAGEDINSTANCESSTATE_STATUSES']._serialized_end=2213
  _globals['_SCALEPOLICY']._serialized_start=2216
  _globals['_SCALEPOLICY']._serialized_end=4030
  _globals['_SCALEPOLICY_AUTOSCALE']._serialized_start=2489
  _globals['_SCALEPOLICY_AUTOSCALE']._serialized_end=3168
  _globals['_SCALEPOLICY_AUTOSCALE_AUTOSCALETYPE']._serialized_start=3095
  _globals['_SCALEPOLICY_AUTOSCALE_AUTOSCALETYPE']._serialized_end=3168
  _globals['_SCALEPOLICY_CPUUTILIZATIONRULE']._serialized_start=3170
  _globals['_SCALEPOLICY_CPUUTILIZATIONRULE']._serialized_end=3230
  _globals['_SCALEPOLICY_CUSTOMRULE']._serialized_start=3233
  _globals['_SCALEPOLICY_CUSTOMRULE']._serialized_end=3971
  _globals['_SCALEPOLICY_CUSTOMRULE_LABELSENTRY']._serialized_start=1501
  _globals['_SCALEPOLICY_CUSTOMRULE_LABELSENTRY']._serialized_end=1546
  _globals['_SCALEPOLICY_CUSTOMRULE_RULETYPE']._serialized_start=3836
  _globals['_SCALEPOLICY_CUSTOMRULE_RULETYPE']._serialized_end=3904
  _globals['_SCALEPOLICY_CUSTOMRULE_METRICTYPE']._serialized_start=3906
  _globals['_SCALEPOLICY_CUSTOMRULE_METRICTYPE']._serialized_end=3971
  _globals['_SCALEPOLICY_FIXEDSCALE']._serialized_start=3973
  _globals['_SCALEPOLICY_FIXEDSCALE']._serialized_end=4010
  _globals['_DEPLOYPOLICY']._serialized_start=4033
  _globals['_DEPLOYPOLICY']._serialized_end=4399
  _globals['_DEPLOYPOLICY_STRATEGY']._serialized_start=4329
  _globals['_DEPLOYPOLICY_STRATEGY']._serialized_end=4399
  _globals['_ALLOCATIONPOLICY']._serialized_start=4402
  _globals['_ALLOCATIONPOLICY']._serialized_end=4579
  _globals['_ALLOCATIONPOLICY_ZONE']._serialized_start=4508
  _globals['_ALLOCATIONPOLICY_ZONE']._serialized_end=4579
  _globals['_INSTANCETEMPLATE']._serialized_start=4582
  _globals['_INSTANCETEMPLATE']._serialized_end=5820
  _globals['_INSTANCETEMPLATE_LABELSENTRY']._serialized_start=1501
  _globals['_INSTANCETEMPLATE_LABELSENTRY']._serialized_end=1546
  _globals['_INSTANCETEMPLATE_METADATAENTRY']._serialized_start=5773
  _globals['_INSTANCETEMPLATE_METADATAENTRY']._serialized_end=5820
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_start=5823
  _globals['_ATTACHEDFILESYSTEMSPEC']._serialized_end=6094
  _globals['_ATTACHEDFILESYSTEMSPEC_MODE']._serialized_start=6035
  _globals['_ATTACHEDFILESYSTEMSPEC_MODE']._serialized_end=6094
  _globals['_PLACEMENTPOLICY']._serialized_start=6097
  _globals['_PLACEMENTPOLICY']._serialized_end=6446
  _globals['_PLACEMENTPOLICY_HOSTAFFINITYRULE']._serialized_start=6247
  _globals['_PLACEMENTPOLICY_HOSTAFFINITYRULE']._serialized_end=6446
  _globals['_PLACEMENTPOLICY_HOSTAFFINITYRULE_OPERATOR']._serialized_start=6390
  _globals['_PLACEMENTPOLICY_HOSTAFFINITYRULE_OPERATOR']._serialized_end=6446
  _globals['_RESOURCESSPEC']._serialized_start=6449
  _globals['_RESOURCESSPEC']._serialized_end=6672
  _globals['_ATTACHEDDISKSPEC']._serialized_start=6675
  _globals['_ATTACHEDDISKSPEC']._serialized_end=7279
  _globals['_ATTACHEDDISKSPEC_DISKSPEC']._serialized_start=6992
  _globals['_ATTACHEDDISKSPEC_DISKSPEC']._serialized_end=7218
  _globals['_ATTACHEDDISKSPEC_MODE']._serialized_start=6035
  _globals['_ATTACHEDDISKSPEC_MODE']._serialized_end=6094
  _globals['_NETWORKINTERFACESPEC']._serialized_start=7282
  _globals['_NETWORKINTERFACESPEC']._serialized_end=7556
  _globals['_PRIMARYADDRESSSPEC']._serialized_start=7559
  _globals['_PRIMARYADDRESSSPEC']._serialized_end=7761
  _globals['_ONETOONENATSPEC']._serialized_start=7764
  _globals['_ONETOONENATSPEC']._serialized_end=7948
  _globals['_DNSRECORDSPEC']._serialized_start=7950
  _globals['_DNSRECORDSPEC']._serialized_end=8045
  _globals['_SCHEDULINGPOLICY']._serialized_start=8047
  _globals['_SCHEDULINGPOLICY']._serialized_end=8086
  _globals['_NETWORKSETTINGS']._serialized_start=8089
  _globals['_NETWORKSETTINGS']._serialized_end=8277
  _globals['_NETWORKSETTINGS_TYPE']._serialized_start=8183
  _globals['_NETWORKSETTINGS_TYPE']._serialized_end=8277
  _globals['_LOADBALANCERSPEC']._serialized_start=8280
  _globals['_LOADBALANCERSPEC']._serialized_end=8486
  _globals['_TARGETGROUPSPEC']._serialized_start=8489
  _globals['_TARGETGROUPSPEC']._serialized_end=8791
  _globals['_TARGETGROUPSPEC_LABELSENTRY']._serialized_start=1501
  _globals['_TARGETGROUPSPEC_LABELSENTRY']._serialized_end=1546
  _globals['_APPLICATIONLOADBALANCERSPEC']._serialized_start=8794
  _globals['_APPLICATIONLOADBALANCERSPEC']._serialized_end=9028
  _globals['_APPLICATIONTARGETGROUPSPEC']._serialized_start=9031
  _globals['_APPLICATIONTARGETGROUPSPEC']._serialized_end=9236
  _globals['_APPLICATIONTARGETGROUPSPEC_LABELSENTRY']._serialized_start=1501
  _globals['_APPLICATIONTARGETGROUPSPEC_LABELSENTRY']._serialized_end=1546
  _globals['_HEALTHCHECKSSPEC']._serialized_start=9239
  _globals['_HEALTHCHECKSSPEC']._serialized_end=9425
  _globals['_HEALTHCHECKSPEC']._serialized_start=9428
  _globals['_HEALTHCHECKSPEC']._serialized_end=9976
  _globals['_HEALTHCHECKSPEC_TCPOPTIONS']._serialized_start=9851
  _globals['_HEALTHCHECKSPEC_TCPOPTIONS']._serialized_end=9890
  _globals['_HEALTHCHECKSPEC_HTTPOPTIONS']._serialized_start=9892
  _globals['_HEALTHCHECKSPEC_HTTPOPTIONS']._serialized_end=9946
  _globals['_MANAGEDINSTANCE']._serialized_start=9979
  _globals['_MANAGEDINSTANCE']._serialized_end=10706
  _globals['_MANAGEDINSTANCE_STATUS']._serialized_start=10342
  _globals['_MANAGEDINSTANCE_STATUS']._serialized_end=10706
  _globals['_NETWORKINTERFACE']._serialized_start=10709
  _globals['_NETWORKINTERFACE']._serialized_end=10948
  _globals['_PRIMARYADDRESS']._serialized_start=10951
  _globals['_PRIMARYADDRESS']._serialized_end=11131
  _globals['_ONETOONENAT']._serialized_start=11134
  _globals['_ONETOONENAT']._serialized_end=11305
  _globals['_DNSRECORD']._serialized_start=11307
  _globals['_DNSRECORD']._serialized_end=11398
  _globals['_LOGRECORD']._serialized_start=11400
  _globals['_LOGRECORD']._serialized_end=11475
# @@protoc_insertion_point(module_scope)
