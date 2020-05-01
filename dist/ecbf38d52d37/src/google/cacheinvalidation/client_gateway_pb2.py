# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_gateway.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_gateway.proto',
  package='ipc.invalidation',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x14\x63lient_gateway.proto\x12\x10ipc.invalidation\"\x82\x01\n\x14\x43lientGatewayMessage\x12\x1b\n\x13is_client_to_server\x18\x01 \x01(\x08\x12\x17\n\x0fservice_context\x18\x02 \x01(\x0c\x12\x1b\n\x13rpc_scheduling_hash\x18\x03 \x01(\x03\x12\x17\n\x0fnetwork_message\x18\x04 \x01(\x0c\x42\x02H\x03')
)




_CLIENTGATEWAYMESSAGE = _descriptor.Descriptor(
  name='ClientGatewayMessage',
  full_name='ipc.invalidation.ClientGatewayMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_client_to_server', full_name='ipc.invalidation.ClientGatewayMessage.is_client_to_server', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_context', full_name='ipc.invalidation.ClientGatewayMessage.service_context', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rpc_scheduling_hash', full_name='ipc.invalidation.ClientGatewayMessage.rpc_scheduling_hash', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_message', full_name='ipc.invalidation.ClientGatewayMessage.network_message', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=43,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['ClientGatewayMessage'] = _CLIENTGATEWAYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientGatewayMessage = _reflection.GeneratedProtocolMessageType('ClientGatewayMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTGATEWAYMESSAGE,
  __module__ = 'client_gateway_pb2'
  # @@protoc_insertion_point(class_scope:ipc.invalidation.ClientGatewayMessage)
  ))
_sym_db.RegisterMessage(ClientGatewayMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
