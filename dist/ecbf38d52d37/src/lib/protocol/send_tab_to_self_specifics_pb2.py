# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_tab_to_self_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='send_tab_to_self_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n send_tab_to_self_specifics.proto\x12\x07sync_pb\"\x81\x01\n\x16SendTabToSelfSpecifics\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x18\n\x10shared_time_usec\x18\x03 \x01(\x03\x12\x31\n\x0b\x66rom_device\x18\x04 \x01(\x0b\x32\x1c.sync_pb.SendTabToSelfDevice\"D\n\x13SendTabToSelfDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x17signin_scoped_device_id\x18\x02 \x01(\tB\x02H\x03')
)




_SENDTABTOSELFSPECIFICS = _descriptor.Descriptor(
  name='SendTabToSelfSpecifics',
  full_name='sync_pb.SendTabToSelfSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='sync_pb.SendTabToSelfSpecifics.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='sync_pb.SendTabToSelfSpecifics.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_time_usec', full_name='sync_pb.SendTabToSelfSpecifics.shared_time_usec', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_device', full_name='sync_pb.SendTabToSelfSpecifics.from_device', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=46,
  serialized_end=175,
)


_SENDTABTOSELFDEVICE = _descriptor.Descriptor(
  name='SendTabToSelfDevice',
  full_name='sync_pb.SendTabToSelfDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sync_pb.SendTabToSelfDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signin_scoped_device_id', full_name='sync_pb.SendTabToSelfDevice.signin_scoped_device_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=177,
  serialized_end=245,
)

_SENDTABTOSELFSPECIFICS.fields_by_name['from_device'].message_type = _SENDTABTOSELFDEVICE
DESCRIPTOR.message_types_by_name['SendTabToSelfSpecifics'] = _SENDTABTOSELFSPECIFICS
DESCRIPTOR.message_types_by_name['SendTabToSelfDevice'] = _SENDTABTOSELFDEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendTabToSelfSpecifics = _reflection.GeneratedProtocolMessageType('SendTabToSelfSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _SENDTABTOSELFSPECIFICS,
  __module__ = 'send_tab_to_self_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SendTabToSelfSpecifics)
  ))
_sym_db.RegisterMessage(SendTabToSelfSpecifics)

SendTabToSelfDevice = _reflection.GeneratedProtocolMessageType('SendTabToSelfDevice', (_message.Message,), dict(
  DESCRIPTOR = _SENDTABTOSELFDEVICE,
  __module__ = 'send_tab_to_self_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SendTabToSelfDevice)
  ))
_sym_db.RegisterMessage(SendTabToSelfDevice)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)