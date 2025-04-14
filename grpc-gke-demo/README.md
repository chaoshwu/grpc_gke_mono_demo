# grpc-gke-demo

一个运行在 GCP Cloud Run 上的 gRPC + grpc-gateway + Vue 前后端一体化项目示例，实现 GKE 集群的创建与日志访问功能。

---

## 🧩 项目结构

```
grpc-gke-demo/
├── proto/                    # gRPC proto 文件（包含 HTTP 映射）
├── server/                   # gRPC 服务实现 (Python)
├── gateway/                  # grpc-gateway 入口 (Go)
├── frontend/                 # Vue3 前端项目
├── terraform/                # Terraform 脚本部署到 GCP Cloud Run
├── Dockerfile                # 构建 Python gRPC 服务镜像
├── docker-compose.yml        # 本地一键运行
├── entrypoint.sh             # 服务启动脚本 (自动编译 proto)
└── requirements.txt          # Python 依赖
```

---

## 🚀 本地运行

### 前置条件

- 安装 Docker & Docker Compose
- 安装 Node.js（用于前端）与 npm
- 安装 Go（用于编译 grpc-gateway）

### 启动服务

```bash
# 启动 gRPC 服务 + grpc-gateway + 前端
docker-compose up --build
```

访问前端页面：

```
http://localhost:5173
```

---

## 🌐 API 示例

gRPC 接口通过 grpc-gateway 暴露为 HTTP：

| 功能          | HTTP 方法 | 路径         | 请求字段                              |
|---------------|------------|--------------|----------------------------------------|
| 创建集群      | POST       | `/v1/cluster` | `project_id`, `region`, `cluster_name`, `node_count` |
| 获取集群日志  | GET        | `/v1/logs`    | `project_id`, `cluster_name`, `namespace`, `pod_name` |

---

## 🛠️ 构建与推送 GCR 镜像

```bash
# 构建镜像
docker build -t gcr.io/[PROJECT_ID]/grpc-api .

# 推送到 GCR
docker push gcr.io/[PROJECT_ID]/grpc-api
```

替换 `[PROJECT_ID]` 为你的 GCP 项目 ID。

---

## ☁️ 使用 Terraform 部署到 GCP Cloud Run

### 配置变量

编辑 `terraform/terraform.tfvars`：

```hcl
project_id = "your-gcp-project-id"
image      = "gcr.io/your-gcp-project-id/grpc-api"
region     = "us-central1"
```

### 初始化并部署

```bash
cd terraform
terraform init
terraform apply
```

部署成功后会输出访问地址。

---

## 📦 前端调用说明

位于 `frontend/src/api.js`：

```js
createCluster(projectId, region, name, count)
getLogs(projectId, clusterName, namespace, pod)
```

前端由 `App.vue` 提供按钮交互，可手动调用 API 验证功能。

---

## ✅ 依赖版本

- Python 3.11
- grpcio / grpcio-tools 1.64
- google-cloud-container / logging
- Go 1.21
- grpc-gateway v2
- Vue 3
- Axios

---

## 📜 License

MIT
