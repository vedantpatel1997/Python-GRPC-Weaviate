# import weaviate, os
# from weaviate.classes.init import Auth
# from weaviate.config import AdditionalConfig, Timeout

# # Best practice: store your credentials in environment variables
# http_host = "temp-grpc.azurewebsites.net"
# grpc_host = "temp-grpc.azurewebsites.net"
# weaviate_api_key = "WEAVIATE_API_KEY"

# client = weaviate.connect_to_custom(
#     http_host=http_host,        # Hostname for the HTTP API connection
#     http_port=443,              # Default is 80, WCD uses 443
#     http_secure=True,           # Whether to use https (secure) for the HTTP API connection
#     grpc_host=grpc_host,        # Hostname for the gRPC API connection
#     grpc_port=50051,            # Default is 50051, WCD uses 443
#     grpc_secure=True,           # Whether to use a secure channel for the gRPC API connection
#     # auth_credentials=Auth.api_key(weaviate_api_key),    # API key for authentication
# )

# print(client.is_ready())



# import weaviate
# client = weaviate.connect_to_local()
# print(client.is_ready())
# client.close()  # <- fix that resource warning


# import weaviate
# from weaviate.connect import ConnectionParams
# from weaviate.classes.init import AdditionalConfig, Timeout, Auth
# import os

# # Load your secrets securely
# http_host = "temp-grpc.azurewebsites.net"   # Replace with your actual App Service domain if different
# grpc_host = "temp-grpc.azurewebsites.net"   # Same as HTTP host for most setups

# # Construct the client
# client = weaviate.WeaviateClient(
#     connection_params=ConnectionParams.from_params(
#         http_host=http_host,
#         http_port=443,
#         http_secure=True,
#         grpc_host=None,   # No gRPC
#         grpc_port=None,
#         grpc_secure=True,
#     ),
#     skip_init_checks=True
# )

# # Manually initiate connection
# client.connect()

# # Check if Weaviate is reachable and ready
# print("Is Weaviate ready?", client.is_ready())

# # Always close after use to avoid warnings
# client.close()





import weaviate
from weaviate.connect import ConnectionParams
from weaviate.classes.init import AdditionalConfig, Timeout

# App Service default HTTPS endpoint
http_host = "temp-grpc-http.azurewebsites.net"
grpc_host = "temp-grpc.azurewebsites.net"

client = weaviate.WeaviateClient(
    connection_params=ConnectionParams.from_params(
        http_host=http_host,
        http_port=443,
        http_secure=True,
        grpc_host=grpc_host,
        grpc_port=443,           # ✅ Use 443 instead of 50051
        grpc_secure=True,        # ✅ Must be True for TLS
    ),
    additional_config=AdditionalConfig(
        timeout=Timeout(init=30, query=60, insert=120),
    ),
    skip_init_checks=True     # or True if you want to skip health check
)

try:
    client.connect()
    print("Is Weaviate ready?", client.is_ready())
finally:
    client.close()
