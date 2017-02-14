# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiments_specifics.proto

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
  name='experiments_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x1b\x65xperiments_specifics.proto\x12\x07sync_pb\"*\n\x17KeystoreEncryptionFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"*\n\x17HistoryDeleteDirectives\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\'\n\x14\x41utofillCullingFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"D\n\x10\x46\x61viconSyncFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1f\n\x12\x66\x61vicon_sync_limit\x18\x02 \x01(\x05:\x03\x32\x30\x30\"0\n\x1dPreCommitUpdateAvoidanceFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\"\n\x0fGcmChannelFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"?\n\x16\x45nhancedBookmarksFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x14\n\x0c\x65xtension_id\x18\x02 \x01(\t\"(\n\x15GcmInvalidationsFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\"\n\x0fWalletSyncFlags\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\xb9\x04\n\x14\x45xperimentsSpecifics\x12=\n\x13keystore_encryption\x18\x01 \x01(\x0b\x32 .sync_pb.KeystoreEncryptionFlags\x12\x43\n\x19history_delete_directives\x18\x02 \x01(\x0b\x32 .sync_pb.HistoryDeleteDirectives\x12\x37\n\x10\x61utofill_culling\x18\x03 \x01(\x0b\x32\x1d.sync_pb.AutofillCullingFlags\x12/\n\x0c\x66\x61vicon_sync\x18\x04 \x01(\x0b\x32\x19.sync_pb.FaviconSyncFlags\x12K\n\x1bpre_commit_update_avoidance\x18\x05 \x01(\x0b\x32&.sync_pb.PreCommitUpdateAvoidanceFlags\x12-\n\x0bgcm_channel\x18\x06 \x01(\x0b\x32\x18.sync_pb.GcmChannelFlags\x12\x44\n\x1bobsolete_enhanced_bookmarks\x18\x07 \x01(\x0b\x32\x1f.sync_pb.EnhancedBookmarksFlags\x12\x39\n\x11gcm_invalidations\x18\x08 \x01(\x0b\x32\x1e.sync_pb.GcmInvalidationsFlags\x12\x36\n\x14obsolete_wallet_sync\x18\t \x01(\x0b\x32\x18.sync_pb.WalletSyncFlagsB\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_KEYSTOREENCRYPTIONFLAGS = _descriptor.Descriptor(
  name='KeystoreEncryptionFlags',
  full_name='sync_pb.KeystoreEncryptionFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.KeystoreEncryptionFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=40,
  serialized_end=82,
)


_HISTORYDELETEDIRECTIVES = _descriptor.Descriptor(
  name='HistoryDeleteDirectives',
  full_name='sync_pb.HistoryDeleteDirectives',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.HistoryDeleteDirectives.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=84,
  serialized_end=126,
)


_AUTOFILLCULLINGFLAGS = _descriptor.Descriptor(
  name='AutofillCullingFlags',
  full_name='sync_pb.AutofillCullingFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.AutofillCullingFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=128,
  serialized_end=167,
)


_FAVICONSYNCFLAGS = _descriptor.Descriptor(
  name='FaviconSyncFlags',
  full_name='sync_pb.FaviconSyncFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.FaviconSyncFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favicon_sync_limit', full_name='sync_pb.FaviconSyncFlags.favicon_sync_limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
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
  serialized_start=169,
  serialized_end=237,
)


_PRECOMMITUPDATEAVOIDANCEFLAGS = _descriptor.Descriptor(
  name='PreCommitUpdateAvoidanceFlags',
  full_name='sync_pb.PreCommitUpdateAvoidanceFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.PreCommitUpdateAvoidanceFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=239,
  serialized_end=287,
)


_GCMCHANNELFLAGS = _descriptor.Descriptor(
  name='GcmChannelFlags',
  full_name='sync_pb.GcmChannelFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.GcmChannelFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=289,
  serialized_end=323,
)


_ENHANCEDBOOKMARKSFLAGS = _descriptor.Descriptor(
  name='EnhancedBookmarksFlags',
  full_name='sync_pb.EnhancedBookmarksFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.EnhancedBookmarksFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension_id', full_name='sync_pb.EnhancedBookmarksFlags.extension_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=325,
  serialized_end=388,
)


_GCMINVALIDATIONSFLAGS = _descriptor.Descriptor(
  name='GcmInvalidationsFlags',
  full_name='sync_pb.GcmInvalidationsFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.GcmInvalidationsFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=390,
  serialized_end=430,
)


_WALLETSYNCFLAGS = _descriptor.Descriptor(
  name='WalletSyncFlags',
  full_name='sync_pb.WalletSyncFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='sync_pb.WalletSyncFlags.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=432,
  serialized_end=466,
)


_EXPERIMENTSSPECIFICS = _descriptor.Descriptor(
  name='ExperimentsSpecifics',
  full_name='sync_pb.ExperimentsSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keystore_encryption', full_name='sync_pb.ExperimentsSpecifics.keystore_encryption', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='history_delete_directives', full_name='sync_pb.ExperimentsSpecifics.history_delete_directives', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autofill_culling', full_name='sync_pb.ExperimentsSpecifics.autofill_culling', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favicon_sync', full_name='sync_pb.ExperimentsSpecifics.favicon_sync', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_commit_update_avoidance', full_name='sync_pb.ExperimentsSpecifics.pre_commit_update_avoidance', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gcm_channel', full_name='sync_pb.ExperimentsSpecifics.gcm_channel', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obsolete_enhanced_bookmarks', full_name='sync_pb.ExperimentsSpecifics.obsolete_enhanced_bookmarks', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gcm_invalidations', full_name='sync_pb.ExperimentsSpecifics.gcm_invalidations', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obsolete_wallet_sync', full_name='sync_pb.ExperimentsSpecifics.obsolete_wallet_sync', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=469,
  serialized_end=1038,
)

_EXPERIMENTSSPECIFICS.fields_by_name['keystore_encryption'].message_type = _KEYSTOREENCRYPTIONFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['history_delete_directives'].message_type = _HISTORYDELETEDIRECTIVES
_EXPERIMENTSSPECIFICS.fields_by_name['autofill_culling'].message_type = _AUTOFILLCULLINGFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['favicon_sync'].message_type = _FAVICONSYNCFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['pre_commit_update_avoidance'].message_type = _PRECOMMITUPDATEAVOIDANCEFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['gcm_channel'].message_type = _GCMCHANNELFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['obsolete_enhanced_bookmarks'].message_type = _ENHANCEDBOOKMARKSFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['gcm_invalidations'].message_type = _GCMINVALIDATIONSFLAGS
_EXPERIMENTSSPECIFICS.fields_by_name['obsolete_wallet_sync'].message_type = _WALLETSYNCFLAGS
DESCRIPTOR.message_types_by_name['KeystoreEncryptionFlags'] = _KEYSTOREENCRYPTIONFLAGS
DESCRIPTOR.message_types_by_name['HistoryDeleteDirectives'] = _HISTORYDELETEDIRECTIVES
DESCRIPTOR.message_types_by_name['AutofillCullingFlags'] = _AUTOFILLCULLINGFLAGS
DESCRIPTOR.message_types_by_name['FaviconSyncFlags'] = _FAVICONSYNCFLAGS
DESCRIPTOR.message_types_by_name['PreCommitUpdateAvoidanceFlags'] = _PRECOMMITUPDATEAVOIDANCEFLAGS
DESCRIPTOR.message_types_by_name['GcmChannelFlags'] = _GCMCHANNELFLAGS
DESCRIPTOR.message_types_by_name['EnhancedBookmarksFlags'] = _ENHANCEDBOOKMARKSFLAGS
DESCRIPTOR.message_types_by_name['GcmInvalidationsFlags'] = _GCMINVALIDATIONSFLAGS
DESCRIPTOR.message_types_by_name['WalletSyncFlags'] = _WALLETSYNCFLAGS
DESCRIPTOR.message_types_by_name['ExperimentsSpecifics'] = _EXPERIMENTSSPECIFICS

KeystoreEncryptionFlags = _reflection.GeneratedProtocolMessageType('KeystoreEncryptionFlags', (_message.Message,), dict(
  DESCRIPTOR = _KEYSTOREENCRYPTIONFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.KeystoreEncryptionFlags)
  ))
_sym_db.RegisterMessage(KeystoreEncryptionFlags)

HistoryDeleteDirectives = _reflection.GeneratedProtocolMessageType('HistoryDeleteDirectives', (_message.Message,), dict(
  DESCRIPTOR = _HISTORYDELETEDIRECTIVES,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.HistoryDeleteDirectives)
  ))
_sym_db.RegisterMessage(HistoryDeleteDirectives)

AutofillCullingFlags = _reflection.GeneratedProtocolMessageType('AutofillCullingFlags', (_message.Message,), dict(
  DESCRIPTOR = _AUTOFILLCULLINGFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AutofillCullingFlags)
  ))
_sym_db.RegisterMessage(AutofillCullingFlags)

FaviconSyncFlags = _reflection.GeneratedProtocolMessageType('FaviconSyncFlags', (_message.Message,), dict(
  DESCRIPTOR = _FAVICONSYNCFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.FaviconSyncFlags)
  ))
_sym_db.RegisterMessage(FaviconSyncFlags)

PreCommitUpdateAvoidanceFlags = _reflection.GeneratedProtocolMessageType('PreCommitUpdateAvoidanceFlags', (_message.Message,), dict(
  DESCRIPTOR = _PRECOMMITUPDATEAVOIDANCEFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.PreCommitUpdateAvoidanceFlags)
  ))
_sym_db.RegisterMessage(PreCommitUpdateAvoidanceFlags)

GcmChannelFlags = _reflection.GeneratedProtocolMessageType('GcmChannelFlags', (_message.Message,), dict(
  DESCRIPTOR = _GCMCHANNELFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.GcmChannelFlags)
  ))
_sym_db.RegisterMessage(GcmChannelFlags)

EnhancedBookmarksFlags = _reflection.GeneratedProtocolMessageType('EnhancedBookmarksFlags', (_message.Message,), dict(
  DESCRIPTOR = _ENHANCEDBOOKMARKSFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.EnhancedBookmarksFlags)
  ))
_sym_db.RegisterMessage(EnhancedBookmarksFlags)

GcmInvalidationsFlags = _reflection.GeneratedProtocolMessageType('GcmInvalidationsFlags', (_message.Message,), dict(
  DESCRIPTOR = _GCMINVALIDATIONSFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.GcmInvalidationsFlags)
  ))
_sym_db.RegisterMessage(GcmInvalidationsFlags)

WalletSyncFlags = _reflection.GeneratedProtocolMessageType('WalletSyncFlags', (_message.Message,), dict(
  DESCRIPTOR = _WALLETSYNCFLAGS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.WalletSyncFlags)
  ))
_sym_db.RegisterMessage(WalletSyncFlags)

ExperimentsSpecifics = _reflection.GeneratedProtocolMessageType('ExperimentsSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTSSPECIFICS,
  __module__ = 'experiments_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.ExperimentsSpecifics)
  ))
_sym_db.RegisterMessage(ExperimentsSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)