# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import channel_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_channel__pb2
from yandex.cloud.video.v1 import channel_service_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2


class ChannelServiceStub(object):
    """Channel management service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.video.v1.ChannelService/Get',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.GetChannelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__pb2.Channel.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.video.v1.ChannelService/List',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.video.v1.ChannelService/Create',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.CreateChannelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.video.v1.ChannelService/Update',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.UpdateChannelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.video.v1.ChannelService/Delete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.DeleteChannelRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ChannelServiceServicer(object):
    """Channel management service.
    """

    def Get(self, request, context):
        """Returns the specific channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List channels for organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChannelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.GetChannelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__pb2.Channel.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.CreateChannelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.UpdateChannelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.DeleteChannelRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.video.v1.ChannelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChannelService(object):
    """Channel management service.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.ChannelService/Get',
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.GetChannelRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__pb2.Channel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.ChannelService/List',
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.ListChannelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.ChannelService/Create',
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.CreateChannelRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.ChannelService/Update',
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.UpdateChannelRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.ChannelService/Delete',
            yandex_dot_cloud_dot_video_dot_v1_dot_channel__service__pb2.DeleteChannelRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
