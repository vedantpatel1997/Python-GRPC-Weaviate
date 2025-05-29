# import os
# import weaviate
# from weaviate.classes.init import Auth, AdditionalConfig, Timeout
# from weaviate.connect import ConnectionParams

# # Public-facing domain of your Weaviate App Service
# weaviate_url = "temp-grpc.azurewebsites.net"
# weaviate_api_key = os.getenv("WEAVIATE_API_KEY")  # If using authentication

# # Dummy HTTP values (required, but unused)
# connection_params = ConnectionParams.from_params(
#     http_host=weaviate_url,
#     http_port=443,
#     http_secure=False,
#     grpc_host=weaviate_url,
#     grpc_port=443,  # Azure exposes gRPC over 443
#     grpc_secure=True,
# )

# # Optional authentication
# auth_credentials = Auth.api_key(weaviate_api_key) if weaviate_api_key else None

# # Optional config
# additional_config = AdditionalConfig(timeout=Timeout(init=10))

# # Initialize client
# client = weaviate.WeaviateClient(
#     connection_params=connection_params,
#     auth_client_secret=auth_credentials,
#     additional_config=additional_config,
# )

# # ✅ Important: Connect first!
# client.connect()

# try:
#     if client.is_ready():
#         print("✅ Successfully connected to Weaviate via gRPC!")
#         print("Collections:", client.collections.list_all())
#     else:
#         print("❌ Failed to connect to Weaviate.")
# except Exception as e:
#     print("❌ Error occurred:", e)

# client.close()


import weaviate
from weaviate.classes.init import Auth

# Best practice: store your credentials in environment variables
# weaviate_url = "temp-grpc.azurewebsites.net"
weaviate_url = "localhost:8080"
weaviate_api_key = "WEAVIATE_API_KEY"

# Connect to Weaviate Cloud
# client = weaviate.connect_to_weaviate_cloud(
#     cluster_url=weaviate_url,
#     auth_credentials=Auth.api_key(weaviate_api_key),
# )
client = weaviate.connect_to_custom(
    http_host="temp-grpc.azurewebsites.net",
    http_port=443,
    http_secure=True,
    grpc_host="temp-grpc.azurewebsites.net",
    grpc_port=50051,   # or whatever port your gRPC is actually running on
    grpc_secure=True
)


print(client.is_ready())  # Should print: `True`

client.close()  # Free up resources