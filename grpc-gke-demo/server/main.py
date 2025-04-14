from concurrent import futures
import grpc
from server.cluster_service import ClusterService
import proto.cluster_service_pb2_grpc as pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ClusterServiceServicer_to_server(ClusterService(), server)
    server.add_insecure_port('[::]:9090')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
