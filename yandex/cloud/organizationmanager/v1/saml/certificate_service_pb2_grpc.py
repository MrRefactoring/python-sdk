# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.organizationmanager.v1.saml import certificate_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__pb2
from yandex.cloud.organizationmanager.v1.saml import certificate_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2


class CertificateServiceStub(object):
    """A set of methods for managing certificates.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Get',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.GetCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__pb2.Certificate.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/List',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Create',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.CreateCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Update',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.UpdateCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Delete',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.DeleteCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.CertificateService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsResponse.FromString,
                )


class CertificateServiceServicer(object):
    """A set of methods for managing certificates.
    """

    def Get(self, request, context):
        """Returns the specified certificate.

        To get the list of available certificates, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of certificates in the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a certificate in the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CertificateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.GetCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__pb2.Certificate.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.CreateCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.UpdateCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.DeleteCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.saml.CertificateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CertificateService(object):
    """A set of methods for managing certificates.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Get',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.GetCertificateRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__pb2.Certificate.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/List',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificatesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Create',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.CreateCertificateRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Update',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.UpdateCertificateRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/Delete',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.DeleteCertificateRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.saml.CertificateService/ListOperations',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_certificate__service__pb2.ListCertificateOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)