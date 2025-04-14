package main

import (
    "context"
    "log"
    "net/http"

    "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
    "google.golang.org/grpc"
    pb "proto"
)

func main() {
    ctx := context.Background()
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()

    mux := runtime.NewServeMux()
    opts := []grpc.DialOption{grpc.WithInsecure()}

    err := pb.RegisterClusterServiceHandlerFromEndpoint(ctx, mux, "localhost:9090", opts)
    if err != nil {
        log.Fatalf("failed to start HTTP gateway: %v", err)
    }

    log.Println("gRPC-Gateway running on :8080")
    http.ListenAndServe(":8080", mux)
}
