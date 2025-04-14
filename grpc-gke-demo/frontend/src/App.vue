<template>
  <div>
    <h1>GKE Manager</h1>
    <button @click="create">Create Cluster</button>
    <button @click="loadLogs">Load Logs</button>
    <pre>{{ logs }}</pre>
  </div>
</template>

<script setup>
import { createCluster, getLogs } from './api.js'
import { ref } from 'vue'

const logs = ref('')

const create = async () => {
  const res = await createCluster('demo-project', 'us-central1', 'demo-cluster', 1)
  console.log('Cluster created:', res.data)
}

const loadLogs = async () => {
  const res = await getLogs('demo-project', 'demo-cluster', 'default', 'demo-pod')
  logs.value = res.data.logs.join('\n')
}
</script>
