# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preference_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='preference_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x1apreference_specifics.proto\x12\x07sync_pb\"2\n\x13PreferenceSpecifics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x02H\x03')
)




_PREFERENCESPECIFICS = _descriptor.Descriptor(
  name='PreferenceSpecifics',
  full_name='sync_pb.PreferenceSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sync_pb.PreferenceSpecifics.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.PreferenceSpecifics.value', index=1,
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
  serialized_start=39,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['PreferenceSpecifics'] = _PREFERENCESPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreferenceSpecifics = _reflection.GeneratedProtocolMessageType('PreferenceSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _PREFERENCESPECIFICS,
  __module__ = 'preference_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.PreferenceSpecifics)
  ))
_sym_db.RegisterMessage(PreferenceSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
