import proto.cluster_service_pb2_grpc as pb2_grpc
import proto.cluster_service_pb2 as pb2
from google.cloud import container_v1, logging_v2

class ClusterService(pb2_grpc.ClusterServiceServicer):
    def CreateCluster(self, request, context):
        client = container_v1.ClusterManagerClient()
        cluster = {
            "name": request.cluster_name,
            "initial_node_count": request.node_count,
        }

        operation = client.create_cluster(
            project_id=request.project_id,
            zone=request.region,
            cluster=cluster
        )

        return pb2.OperationStatus(
            operation_id=operation.name,
            status="PENDING",
            message="Cluster creation started"
        )

    def GetClusterLogs(self, request, context):
        client = logging_v2.LoggingServiceV2Client()
        filter_str = f'resource.labels.cluster_name="{request.cluster_name}" '                      f'AND resource.labels.namespace_name="{request.namespace}" '                      f'AND resource.labels.pod_name="{request.pod_name}"'

        entries = client.list_log_entries(resource_names=[f"projects/{request.project_id}"], filter=filter_str)
        logs = [entry.text_payload for entry in entries]

        return pb2.LogList(logs=logs)
