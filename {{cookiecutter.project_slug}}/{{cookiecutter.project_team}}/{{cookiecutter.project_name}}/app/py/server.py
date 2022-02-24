import grpc
from concurrent import futures

from sentieo.proto.{{cookiecutter.project_team}}.{{cookiecutter.project_name}}.v1 import helloworld_pb2, helloworld_pb2_grpc
from {{cookiecutter.project_team}}.{{cookiecutter.project_name}}.app.py.services.{{cookiecutter.project_name}}.service import GreeterServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
