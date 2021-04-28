from __future__ import print_function

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "proto"))

import grpc
from python.file_stream_util import get_file_chunks, save_chunks_to_file
from python.proto import test_pb2 as test_pb2, import_pb2
from python.proto import test_pb2_grpc as test_pb2_grpc
from python.proto.test_pb2 import TestRequest

channel = grpc.insecure_channel('localhost:1106')
stub = test_pb2_grpc.TestServiceStub(channel)


def test(test_request):
    response = stub.Test(test_request)
    print("Test client received: " + response.response_string)


def test_stream(test_requests):
    responses = stub.TestStream(streamYield(test_requests))
    for response in responses:
        print("Test client received: " + response.response_string)


def streamYield(test_requests):
    for test_request in test_requests:
        yield test_request


def upload(filepath):
    file_chunk_generator = get_file_chunks(filepath)
    response = stub.Upload(file_chunk_generator)
    return response


def download(filename):
    response = stub.Download(TestRequest(test_string=filename))
    save_chunks_to_file(response, "output/client_" + filename)


def nested_test(nested_data):
    response = stub.NestedTest(nested_data)
    print("Test client received: " + response.nested_elem.nested_string)
    for i in response.nested_elem.nested_repeated_string:
        print("Test client received: " + i)


def ref_nested_test(nested_data):
    response = stub.NestedTest(nested_data)
    print("Test client received: " + response.nested_elem.nested_string)
    for i in response.nested_elem.nested_repeated_string:
        print("Test client received: " + i)


def one_of_test(one_of_data):
    response = stub.OneOfTest(one_of_data)
    try:
        print("Test client received: " + response.one_of_string)
    except AttributeError:
        print("Test client received: " + response.one_of_float)


def not_filled_test(not_filled_data):
    response = stub.NotFilledTest(not_filled_data)
    print("Test client received: " + response.first)
    print("Test client received: " + str(response.second))


def map_test(map_data):
    response = stub.MapTest(map_data)
    for i in response.firstMap:
        print(i + " : " + str(response.firstMap[i]))


def import_test(import_msg_data):
    response = stub.ImportTest(import_msg_data)
    print("Test client received: " + response.imported_message.imported_string)


if __name__ == '__main__':

    # Test Block For
    # : rpc Test(TestRequest) returns (TestResponse);
    """
    test_request_param = test_pb2.TestRequest(
        test_double=1.1,
        test_string="test",
        test_enum=1,
        test_repeat_string=["A","b","c"]
    )
    test(test_request_param)
    """

    # Test Block For
    # :   rpc TestStream(stream TestRequest) returns (stream TestResponse);
    """
    test_request_param = test_pb2.TestRequest(
        test_double=1.1,
        test_string="test",
        test_enum=1,
        test_repeat_string=["A","b","c"]
    )
    test_request_param2 = test_pb2.TestRequest(
        test_double=2.2,
        test_string="testB",
        test_enum=2,
        test_repeat_string=["a", "B", "c"]
    )

    test_request_param3 = test_pb2.TestRequest(
        test_double=3.3,
        test_string="testC",
        test_enum=3,
        test_repeat_string=["a", "b", "C"]
    )
    test_stream([test_request_param,test_request_param2,test_request_param3])
    """

    # Test Block for
    # :   rpc Upload(stream FileChunk) returns(TestResponse);
    #     rpc Download(TestRequest) returns(stream FileChunk);
    """ 
    filename = upload("./won.jpg").response_string
    print("FILE : " + filename)
    download(filename)
    """

    # Test Block for
    # :  rpc NestedTest(NestedData) returns (NestedData);
    """
    nested_elem = test_pb2.NestedData.NestedElem(
        nested_string="aa",
        nested_repeated_string=["A","B","C"]
    )
    nested_data = test_pb2.NestedData(
        nested_elem=nested_elem
    )
    nested_test(nested_data)
    """

    # Test Block for
    # :  rpc RefNestedTest(RefNested) returns (RefNested);
    """
    nested_elem = test_pb2.NestedData.NestedElem(
        nested_string="aa",
        nested_repeated_string=["A", "B", "C"]
    )
    nested_data = test_pb2.NestedData(
        nested_elem=nested_elem
    )
    ref_nested_test(nested_data)
    """

    # Test block for
    # :  rpc OneOfTest(OneOf) returns (OneOf);
    """
    one_of = test_pb2.OneOf(
        one_of_float=1.1,
        one_of_string="abcd"
    )
    print(one_of)  # it's just "one_of_string"
    one_of = test_pb2.OneOf(
        one_of_string="abcd",
        one_of_float=1.1
    )
    print(one_of)  # it's just "one_of_float"

    one_of_test(one_of)
    """

    # Test block for
    # :  rpc NotFilledTest(NotFilled) returns (NotFilled);
    """
    not_filled = test_pb2.NotFilled(
        first="first string",
        second=1.99
    )
    not_filled_test(not_filled)
    """

    # Test block for
    # :  rpc MapTest(MapMsg) returns (MapMsg);
    """
    map_msg_data = test_pb2.MapMsg(
        firstMap={
            "key1":0,
            "key2":3,
            "key3":9
        }
    )
    map_test(map_msg_data)
    """

    # Test block for
    # :  rpc importTest(importMsg) returns (importMsg);
    """
    import_msg = import_pb2.importedMessage(
        imported_string="imported container"
    )
    import_test(test_pb2.importMsg(
        imported_message=import_msg
    ))
    """


