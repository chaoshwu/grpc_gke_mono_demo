# Build stage
FROM python:3.11-slim-bullseye as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim-bullseye

WORKDIR /app

# Copy only what's needed from builder
COPY --from=builder /root/.local /root/.local
COPY server/ ./server/
COPY proto/ ./proto/
COPY entrypoint.sh .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Install runtime dependencies and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Compile protobufs
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/googleapis/googleapis
RUN python -m grpc_tools.protoc -I./proto -I./googleapis --python_out=./server --grpc_python_out=./server ./proto/cluster_service.proto

EXPOSE 9090
CMD ["bash", "entrypoint.sh"]
