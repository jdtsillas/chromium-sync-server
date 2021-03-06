# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_engine_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_engine_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x1dsearch_engine_specifics.proto\x12\x07sync_pb\"\xea\x04\n\x15SearchEngineSpecifics\x12\x12\n\nshort_name\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\x13\n\x0b\x66\x61vicon_url\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x1c\n\x14safe_for_autoreplace\x18\x05 \x01(\x08\x12\x17\n\x0foriginating_url\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x61te_created\x18\x07 \x01(\x03\x12\x17\n\x0finput_encodings\x18\x08 \x01(\t\x12+\n\x1f\x64\x65precated_show_in_default_list\x18\t \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0fsuggestions_url\x18\n \x01(\t\x12\x16\n\x0eprepopulate_id\x18\x0b \x01(\x05\x12\x1c\n\x14\x61utogenerate_keyword\x18\x0c \x01(\x08\x12\x13\n\x0binstant_url\x18\x0f \x01(\t\x12\x15\n\rlast_modified\x18\x11 \x01(\x03\x12\x11\n\tsync_guid\x18\x12 \x01(\t\x12\x16\n\x0e\x61lternate_urls\x18\x13 \x03(\t\x12$\n\x1csearch_terms_replacement_key\x18\x14 \x01(\t\x12\x11\n\timage_url\x18\x15 \x01(\t\x12\x1e\n\x16search_url_post_params\x18\x16 \x01(\t\x12#\n\x1bsuggestions_url_post_params\x18\x17 \x01(\t\x12\x1f\n\x17instant_url_post_params\x18\x18 \x01(\t\x12\x1d\n\x15image_url_post_params\x18\x19 \x01(\t\x12\x13\n\x0bnew_tab_url\x18\x1a \x01(\tB\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHENGINESPECIFICS = _descriptor.Descriptor(
  name='SearchEngineSpecifics',
  full_name='sync_pb.SearchEngineSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='short_name', full_name='sync_pb.SearchEngineSpecifics.short_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='sync_pb.SearchEngineSpecifics.keyword', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favicon_url', full_name='sync_pb.SearchEngineSpecifics.favicon_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='sync_pb.SearchEngineSpecifics.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='safe_for_autoreplace', full_name='sync_pb.SearchEngineSpecifics.safe_for_autoreplace', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='originating_url', full_name='sync_pb.SearchEngineSpecifics.originating_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_created', full_name='sync_pb.SearchEngineSpecifics.date_created', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_encodings', full_name='sync_pb.SearchEngineSpecifics.input_encodings', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deprecated_show_in_default_list', full_name='sync_pb.SearchEngineSpecifics.deprecated_show_in_default_list', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='suggestions_url', full_name='sync_pb.SearchEngineSpecifics.suggestions_url', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prepopulate_id', full_name='sync_pb.SearchEngineSpecifics.prepopulate_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autogenerate_keyword', full_name='sync_pb.SearchEngineSpecifics.autogenerate_keyword', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instant_url', full_name='sync_pb.SearchEngineSpecifics.instant_url', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='sync_pb.SearchEngineSpecifics.last_modified', index=13,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_guid', full_name='sync_pb.SearchEngineSpecifics.sync_guid', index=14,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_urls', full_name='sync_pb.SearchEngineSpecifics.alternate_urls', index=15,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_terms_replacement_key', full_name='sync_pb.SearchEngineSpecifics.search_terms_replacement_key', index=16,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='sync_pb.SearchEngineSpecifics.image_url', index=17,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_url_post_params', full_name='sync_pb.SearchEngineSpecifics.search_url_post_params', index=18,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suggestions_url_post_params', full_name='sync_pb.SearchEngineSpecifics.suggestions_url_post_params', index=19,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instant_url_post_params', full_name='sync_pb.SearchEngineSpecifics.instant_url_post_params', index=20,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url_post_params', full_name='sync_pb.SearchEngineSpecifics.image_url_post_params', index=21,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_tab_url', full_name='sync_pb.SearchEngineSpecifics.new_tab_url', index=22,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=661,
)

DESCRIPTOR.message_types_by_name['SearchEngineSpecifics'] = _SEARCHENGINESPECIFICS

SearchEngineSpecifics = _reflection.GeneratedProtocolMessageType('SearchEngineSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHENGINESPECIFICS,
  __module__ = 'search_engine_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.SearchEngineSpecifics)
  ))
_sym_db.RegisterMessage(SearchEngineSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_SEARCHENGINESPECIFICS.fields_by_name['deprecated_show_in_default_list'].has_options = True
_SEARCHENGINESPECIFICS.fields_by_name['deprecated_show_in_default_list']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
