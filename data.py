import weaviate

client = weaviate.connect_to_local(host="localhost", port=8080, grpc_port=50051)

schema = {
    "class": "TestItem",
    "description": "A test schema class",
    "properties": [
        {
            "name": "name",
            "dataType": ["string"],
            "description": "Name of the item"
        }
    ]
}

client.schema.create_class(schema)
print("Schema created!")

collections = client.collections.list_all()
print("Collections after creation:", collections)

client.close()
