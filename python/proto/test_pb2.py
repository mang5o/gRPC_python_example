# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import import_pb2 as import__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\x1a\x0cimport.proto\"\xd2\x03\n\x0bTestRequest\x12\x13\n\x0btest_double\x18\x01 \x01(\x01\x12\x12\n\ntest_float\x18\x02 \x01(\x02\x12\x12\n\ntest_int32\x18\x03 \x01(\x05\x12\x12\n\ntest_int64\x18\x04 \x01(\x03\x12\x13\n\x0btest_uint32\x18\x05 \x01(\r\x12\x13\n\x0btest_uint64\x18\x06 \x01(\x04\x12\x13\n\x0btest_sint32\x18\x07 \x01(\x11\x12\x13\n\x0btest_sint64\x18\x08 \x01(\x12\x12\x14\n\x0ctest_fixed32\x18\t \x01(\x07\x12\x14\n\x0ctest_fixed64\x18\n \x01(\x06\x12\x15\n\rtest_sfixed32\x18\x0b \x01(\x0f\x12\x15\n\rtest_sfixed64\x18\x0c \x01(\x10\x12\x11\n\ttest_bool\x18\r \x01(\x08\x12\x13\n\x0btest_string\x18\x0e \x01(\t\x12\x12\n\ntest_bytes\x18\x0f \x01(\x0c\x12(\n\ttest_enum\x18\x10 \x01(\x0e\x32\x15.TestRequest.TestEnum\x12\x1a\n\x12test_repeat_string\x18\x11 \x03(\t\"B\n\x08TestEnum\x12\x0c\n\x08\x45NUMVAL1\x10\x00\x12\x0c\n\x08\x45NUMVAL2\x10\x01\x12\x0c\n\x08\x45NUMVAL3\x10\x02\x12\x0c\n\x08\x45NUMVAL4\x10\x03\"\'\n\x0cTestResponse\x12\x17\n\x0fresponse_string\x18\x01 \x01(\t\"\x1f\n\tFileChunk\x12\x12\n\nfile_bytes\x18\x01 \x01(\x0c\"~\n\nNestedData\x12+\n\x0bnested_elem\x18\x01 \x01(\x0b\x32\x16.NestedData.NestedElem\x1a\x43\n\nNestedElem\x12\x15\n\rnested_string\x18\x01 \x01(\t\x12\x1e\n\x16nested_repeated_string\x18\x02 \x03(\t\"8\n\tRefNested\x12+\n\x0bnested_elem\x18\x01 \x01(\x0b\x32\x16.NestedData.NestedElem\"F\n\x05OneOf\x12\x17\n\rone_of_string\x18\x01 \x01(\tH\x00\x12\x16\n\x0cone_of_float\x18\x02 \x01(\x02H\x00\x42\x0c\n\noneof_test\"*\n\tNotFilled\x12\r\n\x05\x66irst\x18\x04 \x01(\t\x12\x0e\n\x06second\x18\n \x01(\x02\"b\n\x06MapMsg\x12\'\n\x08\x66irstMap\x18\x01 \x03(\x0b\x32\x15.MapMsg.FirstMapEntry\x1a/\n\rFirstMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"D\n\timportMsg\x12\x37\n\x10imported_message\x18\x01 \x01(\x0b\x32\x1d.import_proto.importedMessage2\x8a\x03\n\x0bTestService\x12#\n\x04Test\x12\x0c.TestRequest\x1a\r.TestResponse\x12-\n\nTestStream\x12\x0c.TestRequest\x1a\r.TestResponse(\x01\x30\x01\x12%\n\x06Upload\x12\n.FileChunk\x1a\r.TestResponse(\x01\x12&\n\x08\x44ownload\x12\x0c.TestRequest\x1a\n.FileChunk0\x01\x12&\n\nNestedTest\x12\x0b.NestedData\x1a\x0b.NestedData\x12\'\n\rRefNestedTest\x12\n.RefNested\x1a\n.RefNested\x12\x1b\n\tOneOfTest\x12\x06.OneOf\x1a\x06.OneOf\x12\'\n\rNotFilledTest\x12\n.NotFilled\x1a\n.NotFilled\x12\x1b\n\x07MapTest\x12\x07.MapMsg\x1a\x07.MapMsg\x12$\n\nImportTest\x12\n.importMsg\x1a\n.importMsg2f\n\x0cTestService2\x12%\n\x04Test\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x12/\n\nTestStream\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[import__pb2.DESCRIPTOR,])



_TESTREQUEST_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='TestRequest.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUMVAL1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUMVAL2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUMVAL3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUMVAL4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=429,
  serialized_end=495,
)
_sym_db.RegisterEnumDescriptor(_TESTREQUEST_TESTENUM)


_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_double', full_name='TestRequest.test_double', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_float', full_name='TestRequest.test_float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_int32', full_name='TestRequest.test_int32', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_int64', full_name='TestRequest.test_int64', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_uint32', full_name='TestRequest.test_uint32', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_uint64', full_name='TestRequest.test_uint64', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_sint32', full_name='TestRequest.test_sint32', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_sint64', full_name='TestRequest.test_sint64', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_fixed32', full_name='TestRequest.test_fixed32', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_fixed64', full_name='TestRequest.test_fixed64', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_sfixed32', full_name='TestRequest.test_sfixed32', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_sfixed64', full_name='TestRequest.test_sfixed64', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_bool', full_name='TestRequest.test_bool', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_string', full_name='TestRequest.test_string', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_bytes', full_name='TestRequest.test_bytes', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_enum', full_name='TestRequest.test_enum', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_repeat_string', full_name='TestRequest.test_repeat_string', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TESTREQUEST_TESTENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=495,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_string', full_name='TestResponse.response_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=536,
)


_FILECHUNK = _descriptor.Descriptor(
  name='FileChunk',
  full_name='FileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_bytes', full_name='FileChunk.file_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=569,
)


_NESTEDDATA_NESTEDELEM = _descriptor.Descriptor(
  name='NestedElem',
  full_name='NestedData.NestedElem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nested_string', full_name='NestedData.NestedElem.nested_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_repeated_string', full_name='NestedData.NestedElem.nested_repeated_string', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=697,
)

_NESTEDDATA = _descriptor.Descriptor(
  name='NestedData',
  full_name='NestedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nested_elem', full_name='NestedData.nested_elem', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NESTEDDATA_NESTEDELEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=697,
)


_REFNESTED = _descriptor.Descriptor(
  name='RefNested',
  full_name='RefNested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nested_elem', full_name='RefNested.nested_elem', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=755,
)


_ONEOF = _descriptor.Descriptor(
  name='OneOf',
  full_name='OneOf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_of_string', full_name='OneOf.one_of_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='one_of_float', full_name='OneOf.one_of_float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='oneof_test', full_name='OneOf.oneof_test',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=757,
  serialized_end=827,
)


_NOTFILLED = _descriptor.Descriptor(
  name='NotFilled',
  full_name='NotFilled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='NotFilled.first', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='NotFilled.second', index=1,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=871,
)


_MAPMSG_FIRSTMAPENTRY = _descriptor.Descriptor(
  name='FirstMapEntry',
  full_name='MapMsg.FirstMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MapMsg.FirstMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='MapMsg.FirstMapEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=971,
)

_MAPMSG = _descriptor.Descriptor(
  name='MapMsg',
  full_name='MapMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstMap', full_name='MapMsg.firstMap', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MAPMSG_FIRSTMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=873,
  serialized_end=971,
)


_IMPORTMSG = _descriptor.Descriptor(
  name='importMsg',
  full_name='importMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imported_message', full_name='importMsg.imported_message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=973,
  serialized_end=1041,
)

_TESTREQUEST.fields_by_name['test_enum'].enum_type = _TESTREQUEST_TESTENUM
_TESTREQUEST_TESTENUM.containing_type = _TESTREQUEST
_NESTEDDATA_NESTEDELEM.containing_type = _NESTEDDATA
_NESTEDDATA.fields_by_name['nested_elem'].message_type = _NESTEDDATA_NESTEDELEM
_REFNESTED.fields_by_name['nested_elem'].message_type = _NESTEDDATA_NESTEDELEM
_ONEOF.oneofs_by_name['oneof_test'].fields.append(
  _ONEOF.fields_by_name['one_of_string'])
_ONEOF.fields_by_name['one_of_string'].containing_oneof = _ONEOF.oneofs_by_name['oneof_test']
_ONEOF.oneofs_by_name['oneof_test'].fields.append(
  _ONEOF.fields_by_name['one_of_float'])
_ONEOF.fields_by_name['one_of_float'].containing_oneof = _ONEOF.oneofs_by_name['oneof_test']
_MAPMSG_FIRSTMAPENTRY.containing_type = _MAPMSG
_MAPMSG.fields_by_name['firstMap'].message_type = _MAPMSG_FIRSTMAPENTRY
_IMPORTMSG.fields_by_name['imported_message'].message_type = import__pb2._IMPORTEDMESSAGE
DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
DESCRIPTOR.message_types_by_name['FileChunk'] = _FILECHUNK
DESCRIPTOR.message_types_by_name['NestedData'] = _NESTEDDATA
DESCRIPTOR.message_types_by_name['RefNested'] = _REFNESTED
DESCRIPTOR.message_types_by_name['OneOf'] = _ONEOF
DESCRIPTOR.message_types_by_name['NotFilled'] = _NOTFILLED
DESCRIPTOR.message_types_by_name['MapMsg'] = _MAPMSG
DESCRIPTOR.message_types_by_name['importMsg'] = _IMPORTMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)

FileChunk = _reflection.GeneratedProtocolMessageType('FileChunk', (_message.Message,), {
  'DESCRIPTOR' : _FILECHUNK,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:FileChunk)
  })
_sym_db.RegisterMessage(FileChunk)

NestedData = _reflection.GeneratedProtocolMessageType('NestedData', (_message.Message,), {

  'NestedElem' : _reflection.GeneratedProtocolMessageType('NestedElem', (_message.Message,), {
    'DESCRIPTOR' : _NESTEDDATA_NESTEDELEM,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:NestedData.NestedElem)
    })
  ,
  'DESCRIPTOR' : _NESTEDDATA,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:NestedData)
  })
_sym_db.RegisterMessage(NestedData)
_sym_db.RegisterMessage(NestedData.NestedElem)

RefNested = _reflection.GeneratedProtocolMessageType('RefNested', (_message.Message,), {
  'DESCRIPTOR' : _REFNESTED,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:RefNested)
  })
_sym_db.RegisterMessage(RefNested)

OneOf = _reflection.GeneratedProtocolMessageType('OneOf', (_message.Message,), {
  'DESCRIPTOR' : _ONEOF,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:OneOf)
  })
_sym_db.RegisterMessage(OneOf)

NotFilled = _reflection.GeneratedProtocolMessageType('NotFilled', (_message.Message,), {
  'DESCRIPTOR' : _NOTFILLED,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:NotFilled)
  })
_sym_db.RegisterMessage(NotFilled)

MapMsg = _reflection.GeneratedProtocolMessageType('MapMsg', (_message.Message,), {

  'FirstMapEntry' : _reflection.GeneratedProtocolMessageType('FirstMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPMSG_FIRSTMAPENTRY,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:MapMsg.FirstMapEntry)
    })
  ,
  'DESCRIPTOR' : _MAPMSG,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:MapMsg)
  })
_sym_db.RegisterMessage(MapMsg)
_sym_db.RegisterMessage(MapMsg.FirstMapEntry)

importMsg = _reflection.GeneratedProtocolMessageType('importMsg', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTMSG,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:importMsg)
  })
_sym_db.RegisterMessage(importMsg)


_MAPMSG_FIRSTMAPENTRY._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1044,
  serialized_end=1438,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='TestService.Test',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestStream',
    full_name='TestService.TestStream',
    index=1,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='TestService.Upload',
    index=2,
    containing_service=None,
    input_type=_FILECHUNK,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='TestService.Download',
    index=3,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_FILECHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NestedTest',
    full_name='TestService.NestedTest',
    index=4,
    containing_service=None,
    input_type=_NESTEDDATA,
    output_type=_NESTEDDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RefNestedTest',
    full_name='TestService.RefNestedTest',
    index=5,
    containing_service=None,
    input_type=_REFNESTED,
    output_type=_REFNESTED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OneOfTest',
    full_name='TestService.OneOfTest',
    index=6,
    containing_service=None,
    input_type=_ONEOF,
    output_type=_ONEOF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NotFilledTest',
    full_name='TestService.NotFilledTest',
    index=7,
    containing_service=None,
    input_type=_NOTFILLED,
    output_type=_NOTFILLED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MapTest',
    full_name='TestService.MapTest',
    index=8,
    containing_service=None,
    input_type=_MAPMSG,
    output_type=_MAPMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImportTest',
    full_name='TestService.ImportTest',
    index=9,
    containing_service=None,
    input_type=_IMPORTMSG,
    output_type=_IMPORTMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE


_TESTSERVICE2 = _descriptor.ServiceDescriptor(
  name='TestService2',
  full_name='TestService2',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1440,
  serialized_end=1542,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='TestService2.Test',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestStream',
    full_name='TestService2.TestStream',
    index=1,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE2)

DESCRIPTOR.services_by_name['TestService2'] = _TESTSERVICE2

# @@protoc_insertion_point(module_scope)
