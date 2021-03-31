# Basic Construction

> Code reference : https://grpc.io/docs/languages/python/quickstart/
>
> Data reference : https://developers.google.com/protocol-buffers/docs/proto3



### pip install

```shell
pip install grpcio
pip install grpcio-tools
```



### Generate gRPC python script

```shell
python -m grpc_tools.protoc -I. --python_out=<pb2_script_output_directory> --grpc_python_out=<pb2_grpc_script_output_directory> <proto_directory>
```



### Make server.py

```python
from concurrent import futures
import time

import grpc

import <generated_pb2>
import <generated_pb2_grpc>


class <service_name>(<Servicer>):
    <functions for rpc>


def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    <servicer_to_server>
    server.add_insecure_port('<ip:port>')
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    start_server()
```



### Make client.py

```Python
from __future__ import print_function

import grpc

import <generated_pb2>
import <generated_pb2_grpc>

def run():
    channel = grpc.insecure_channel('<ip:port>')
    <grpc_stub>
    response = stub.<function for rpc>(<struct in proto>)
    print("Test client received: " + response.<response_variable>)


if __name__ == '__main__':
    run()
```



### Customizing

The classes and functions are renamed by the services you define as shown below (When service name is "TestService"). There are many other things besides the contents below.

| Target             | renamed                               |
| ------------------ | ------------------------------------- |
| Servicer           | **TestService**Servicer               |
| Servicer to server | add_**TestService**Servicer_to_server |
| Stub               | **TestService**Stub                   |


