# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: favicon_image_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='favicon_image_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x1d\x66\x61vicon_image_specifics.proto\x12\x07sync_pb\"=\n\x0b\x46\x61viconData\x12\x0f\n\x07\x66\x61vicon\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\"\xf1\x01\n\x15\x46\x61viconImageSpecifics\x12\x13\n\x0b\x66\x61vicon_url\x18\x01 \x01(\t\x12)\n\x0b\x66\x61vicon_web\x18\x02 \x01(\x0b\x32\x14.sync_pb.FaviconData\x12,\n\x0e\x66\x61vicon_web_32\x18\x03 \x01(\x0b\x32\x14.sync_pb.FaviconData\x12.\n\x10\x66\x61vicon_touch_64\x18\x04 \x01(\x0b\x32\x14.sync_pb.FaviconData\x12:\n\x1c\x66\x61vicon_touch_precomposed_64\x18\x05 \x01(\x0b\x32\x14.sync_pb.FaviconDataB\x02H\x03')
)




_FAVICONDATA = _descriptor.Descriptor(
  name='FaviconData',
  full_name='sync_pb.FaviconData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='favicon', full_name='sync_pb.FaviconData.favicon', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='sync_pb.FaviconData.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='sync_pb.FaviconData.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=42,
  serialized_end=103,
)


_FAVICONIMAGESPECIFICS = _descriptor.Descriptor(
  name='FaviconImageSpecifics',
  full_name='sync_pb.FaviconImageSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='favicon_url', full_name='sync_pb.FaviconImageSpecifics.favicon_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_web', full_name='sync_pb.FaviconImageSpecifics.favicon_web', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_web_32', full_name='sync_pb.FaviconImageSpecifics.favicon_web_32', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_touch_64', full_name='sync_pb.FaviconImageSpecifics.favicon_touch_64', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favicon_touch_precomposed_64', full_name='sync_pb.FaviconImageSpecifics.favicon_touch_precomposed_64', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=106,
  serialized_end=347,
)

_FAVICONIMAGESPECIFICS.fields_by_name['favicon_web'].message_type = _FAVICONDATA
_FAVICONIMAGESPECIFICS.fields_by_name['favicon_web_32'].message_type = _FAVICONDATA
_FAVICONIMAGESPECIFICS.fields_by_name['favicon_touch_64'].message_type = _FAVICONDATA
_FAVICONIMAGESPECIFICS.fields_by_name['favicon_touch_precomposed_64'].message_type = _FAVICONDATA
DESCRIPTOR.message_types_by_name['FaviconData'] = _FAVICONDATA
DESCRIPTOR.message_types_by_name['FaviconImageSpecifics'] = _FAVICONIMAGESPECIFICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaviconData = _reflection.GeneratedProtocolMessageType('FaviconData', (_message.Message,), dict(
  DESCRIPTOR = _FAVICONDATA,
  __module__ = 'favicon_image_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.FaviconData)
  ))
_sym_db.RegisterMessage(FaviconData)

FaviconImageSpecifics = _reflection.GeneratedProtocolMessageType('FaviconImageSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _FAVICONIMAGESPECIFICS,
  __module__ = 'favicon_image_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.FaviconImageSpecifics)
  ))
_sym_db.RegisterMessage(FaviconImageSpecifics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
