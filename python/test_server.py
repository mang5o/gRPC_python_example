from concurrent import futures
import time

import grpc

from python.proto import test_pb2 as test_pb2
from python.proto import test_pb2_grpc as test_pb2_grpc


class TestService(test_pb2_grpc.TestServiceServicer):
    def Test(self, request, context):
        print("\nTest input\n")
        print(request)
        return test_pb2.TestResponse(response_string="Success")

    def TestStream(self, request_iterator, context):
        print("\nTestStream input\n")
        for request in request_iterator:
            print(request)
        for test_string in ["Test1", "Test2", "Test3"]:
            yield test_pb2.TestResponse(response_string=test_string)


def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    server.add_insecure_port('localhost:1106')
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    start_server()
