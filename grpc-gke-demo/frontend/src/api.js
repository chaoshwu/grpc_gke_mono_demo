import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8080',
  headers: { 'Content-Type': 'application/json' }
});

export const createCluster = (projectId, region, name, count) => {
  return api.post('/v1/cluster', {
    project_id: projectId,
    region,
    cluster_name: name,
    node_count: count
  });
};

export const getLogs = (projectId, clusterName, ns, pod) => {
  return api.get('/v1/logs', {
    params: {
      project_id: projectId,
      cluster_name: clusterName,
      namespace: ns,
      pod_name: pod
    }
  });
};
