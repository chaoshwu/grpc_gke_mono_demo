FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install grpcio-tools
RUN pip install googleapis-common-protos

COPY server /app/server
COPY proto /app/proto

RUN python -m grpc_tools.protoc -I. --python_out=/app/server --grpc_python_out=/app/server /app/proto/cluster_service.proto

ENV PYTHONPATH /app
CMD ["python", "/app/server/main.py"]
