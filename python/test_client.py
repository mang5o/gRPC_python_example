from __future__ import print_function

import grpc

from python.proto import test_pb2 as test_pb2
from python.proto import test_pb2_grpc as test_pb2_grpc


def test(test_request):
    channel = grpc.insecure_channel('localhost:1106')
    stub = test_pb2_grpc.TestServiceStub(channel)
    response = stub.Test(test_request)
    print("Test client received: " + response.response_string)


def testStream(test_requests):
    channel = grpc.insecure_channel('localhost:1106')
    stub = test_pb2_grpc.TestServiceStub(channel)
    responses = stub.TestStream(streamYield(test_requests))
    for response in responses:
        print("Test client received: " + response.response_string)


def streamYield(test_requests):
    for test_request in test_requests:
        yield test_request


if __name__ == '__main__':

    testRequestParam = test_pb2.TestRequest(
        test_double=1.1,
        test_string="test",
        test_enum=1,
        test_repeat_string=["A","b","c"]
    )

    testRequestParam2 = test_pb2.TestRequest(
        test_double=2.2,
        test_string="testB",
        test_enum=2,
        test_repeat_string=["a", "B", "c"]
    )

    testRequestParam3 = test_pb2.TestRequest(
        test_double=3.3,
        test_string="testC",
        test_enum=3,
        test_repeat_string=["a", "b", "C"]
    )

    # test(testRequestParam)
    # testStream([testRequestParam,testRequestParam2,testRequestParam3])
