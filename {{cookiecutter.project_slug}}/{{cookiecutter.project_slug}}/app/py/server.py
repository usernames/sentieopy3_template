import os
import sys

import grpc
from concurrent import futures

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join('.', os.pardir))

paths = [ROOT_PATH, PROJECT_ROOT]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

from sentieo.proto.{{cookiecutter.project_team}}.{cookiecutter.project_name}}.v1 import helloworld_pb2, helloworld_pb2_grpc
from {{cookiecutter.project_slug}}.app.py.services.{{cookiecutter.project_name}}.service import NotesServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_pb2_grpc.add_HelloworldServicer_to_server(HelloworldServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
