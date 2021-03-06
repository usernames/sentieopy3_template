import logging

from sentieo.proto.{{cookiecutter.project_team}}.{{cookiecutter.project_name}}.v1 import helloworld_pb2, helloworld_pb2_grpc

LOGGER = logging.getLogger(__name__)


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        request_name = request.name or "World"
        return helloworld_pb2.HelloReply(message=f"Hello, {request_name}!")
