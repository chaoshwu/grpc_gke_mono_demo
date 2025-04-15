#!/bin/bash
python3 -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/cluster_service.proto
export PYTHONPATH=$PYTHONPATH:/app
python3 server/main.py
