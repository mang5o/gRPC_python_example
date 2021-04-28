import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "proto"))

import uuid
from concurrent import futures
import time

import grpc

from python.file_stream_util import save_chunks_to_file, get_file_chunks
from python.proto import test_pb2 as test_pb2, import_pb2
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

    def Upload(self, request_iterator, context):
        newfile = str(uuid.uuid4())
        save_chunks_to_file(request_iterator, "output/" + newfile)
        return test_pb2.TestResponse(response_string=newfile)

    def Download(self, request, context):
        return get_file_chunks("output/" + request.test_string)

    def NestedTest(self, request, context):
        print("\nNestedTest Input\n")
        print(request)
        return_repeated_string = ["serverA", "serverB", "serverC", "serverD"]
        return_nested_elem = test_pb2.NestedData.NestedElem(nested_string="nested_string_server",
                                                            nested_repeated_string=return_repeated_string)
        return test_pb2.NestedData(nested_elem=return_nested_elem)

    def RefNestedTest(self, request, context):
        print("\nRefNestedTest Input\n")
        print(request)
        return_repeated_string = ["serverE", "serverF", "serverG", "serverH"]
        return_nested_elem = test_pb2.NestedData.NestedElem(nested_string="nested_string_server",
                                                            nested_repeated_string=return_repeated_string)
        return return_nested_elem

    def OneOfTest(self, request, context):
        print("\nOneOfTest Input\n")
        print(request)
        return test_pb2.OneOf(one_of_string="oneOfString", one_of_float=1.1)

    def NotFilledTest(self, request, context):
        print("\nNotFilledTest Input\n")
        print(request)
        return test_pb2.NotFilled(first="first_one_of", second=2.2)

    def MapTest(self, request, context):
        print("\nMapTest Input\n")
        print(request)
        return test_pb2.MapMsg(
            firstMap={
                "key4": 1111,
                "key5": 5555
            }
        )

    def ImportTest(self, request, context):
        print("\nimportTest Input\n")
        print(request)
        return test_pb2.importMsg(
            imported_message=import_pb2.importedMessage(
                imported_string="imported container by server"
                )
            )


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
