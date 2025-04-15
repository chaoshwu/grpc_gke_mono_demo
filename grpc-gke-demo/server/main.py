from concurrent import futures
import grpc
from server.cluster_service import ClusterService
import proto.cluster_service_pb2_grpc as pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ClusterServiceServicer_to_server(ClusterService(), server)
    import os
    port = os.environ.get('PORT', '8080')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
