# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: android_channel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import client_protocol_pb2 as client__protocol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='android_channel.proto',
  package='ipc.invalidation',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x15\x61ndroid_channel.proto\x12\x10ipc.invalidation\x1a\x15\x63lient_protocol.proto\"\x9f\x01\n\nEndpointId\x12\x1c\n\x14\x63\x32\x64m_registration_id\x18\x02 \x01(\t\x12\x12\n\nclient_key\x18\x03 \x01(\t\x12\x15\n\tsender_id\x18\x04 \x01(\tB\x02\x18\x01\x12\x32\n\x0f\x63hannel_version\x18\x05 \x01(\x0b\x32\x19.ipc.invalidation.Version\x12\x14\n\x0cpackage_name\x18\x06 \x01(\t\">\n\x17\x41\x64\x64ressedAndroidMessage\x12\x12\n\nclient_key\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"d\n\x1c\x41\x64\x64ressedAndroidMessageBatch\x12\x44\n\x11\x61\x64\x64ressed_message\x18\x01 \x03(\x0b\x32).ipc.invalidation.AddressedAndroidMessage*]\n\x0cMajorVersion\x12\x0b\n\x07INITIAL\x10\x00\x12\t\n\x05\x42\x41TCH\x10\x01\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x11\n\rMIN_SUPPORTED\x10\x00\x12\x11\n\rMAX_SUPPORTED\x10\x01\x1a\x02\x10\x01\x42\x02H\x03')
  ,
  dependencies=[client__protocol__pb2.DESCRIPTOR,])

_MAJORVERSION = _descriptor.EnumDescriptor(
  name='MajorVersion',
  full_name='ipc.invalidation.MajorVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATCH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=2, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_SUPPORTED', index=3, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_SUPPORTED', index=4, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=394,
  serialized_end=487,
)
_sym_db.RegisterEnumDescriptor(_MAJORVERSION)

MajorVersion = enum_type_wrapper.EnumTypeWrapper(_MAJORVERSION)
INITIAL = 0
BATCH = 1
DEFAULT = 0
MIN_SUPPORTED = 0
MAX_SUPPORTED = 1



_ENDPOINTID = _descriptor.Descriptor(
  name='EndpointId',
  full_name='ipc.invalidation.EndpointId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2dm_registration_id', full_name='ipc.invalidation.EndpointId.c2dm_registration_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_key', full_name='ipc.invalidation.EndpointId.client_key', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='ipc.invalidation.EndpointId.sender_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_version', full_name='ipc.invalidation.EndpointId.channel_version', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_name', full_name='ipc.invalidation.EndpointId.package_name', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=226,
)


_ADDRESSEDANDROIDMESSAGE = _descriptor.Descriptor(
  name='AddressedAndroidMessage',
  full_name='ipc.invalidation.AddressedAndroidMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_key', full_name='ipc.invalidation.AddressedAndroidMessage.client_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ipc.invalidation.AddressedAndroidMessage.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=290,
)


_ADDRESSEDANDROIDMESSAGEBATCH = _descriptor.Descriptor(
  name='AddressedAndroidMessageBatch',
  full_name='ipc.invalidation.AddressedAndroidMessageBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addressed_message', full_name='ipc.invalidation.AddressedAndroidMessageBatch.addressed_message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=392,
)

_ENDPOINTID.fields_by_name['channel_version'].message_type = client__protocol__pb2._VERSION
_ADDRESSEDANDROIDMESSAGEBATCH.fields_by_name['addressed_message'].message_type = _ADDRESSEDANDROIDMESSAGE
DESCRIPTOR.message_types_by_name['EndpointId'] = _ENDPOINTID
DESCRIPTOR.message_types_by_name['AddressedAndroidMessage'] = _ADDRESSEDANDROIDMESSAGE
DESCRIPTOR.message_types_by_name['AddressedAndroidMessageBatch'] = _ADDRESSEDANDROIDMESSAGEBATCH
DESCRIPTOR.enum_types_by_name['MajorVersion'] = _MAJORVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndpointId = _reflection.GeneratedProtocolMessageType('EndpointId', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINTID,
  __module__ = 'android_channel_pb2'
  # @@protoc_insertion_point(class_scope:ipc.invalidation.EndpointId)
  ))
_sym_db.RegisterMessage(EndpointId)

AddressedAndroidMessage = _reflection.GeneratedProtocolMessageType('AddressedAndroidMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSEDANDROIDMESSAGE,
  __module__ = 'android_channel_pb2'
  # @@protoc_insertion_point(class_scope:ipc.invalidation.AddressedAndroidMessage)
  ))
_sym_db.RegisterMessage(AddressedAndroidMessage)

AddressedAndroidMessageBatch = _reflection.GeneratedProtocolMessageType('AddressedAndroidMessageBatch', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSEDANDROIDMESSAGEBATCH,
  __module__ = 'android_channel_pb2'
  # @@protoc_insertion_point(class_scope:ipc.invalidation.AddressedAndroidMessageBatch)
  ))
_sym_db.RegisterMessage(AddressedAndroidMessageBatch)


DESCRIPTOR._options = None
_MAJORVERSION._options = None
_ENDPOINTID.fields_by_name['sender_id']._options = None
# @@protoc_insertion_point(module_scope)
