# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='sequence.proto',
  package='fullcircle',
  serialized_pb='\n\x0esequence.proto\x12\nfullcircle\"\x85\x01\n\x16\x42inarySequenceMetadata\x12\x19\n\x11\x66rames_per_second\x18\x01 \x02(\r\x12\r\n\x05width\x18\x02 \x02(\r\x12\x0e\n\x06height\x18\x03 \x02(\r\x12\x16\n\x0egenerator_name\x18\x04 \x02(\t\x12\x19\n\x11generator_version\x18\x05 \x02(\t\"J\n\x08RGBValue\x12\x0b\n\x03red\x18\x01 \x02(\r\x12\r\n\x05green\x18\x02 \x02(\r\x12\x0c\n\x04\x62lue\x18\x03 \x02(\r\x12\t\n\x01x\x18\x04 \x02(\r\x12\t\n\x01y\x18\x05 \x02(\r\"2\n\x0b\x42inaryFrame\x12#\n\x05pixel\x18\x01 \x03(\x0b\x32\x14.fullcircle.RGBValue\"n\n\x0e\x42inarySequence\x12\x34\n\x08metadata\x18\x01 \x02(\x0b\x32\".fullcircle.BinarySequenceMetadata\x12&\n\x05\x66rame\x18\x02 \x03(\x0b\x32\x17.fullcircle.BinaryFrame\"\xcf\x08\n\x04Snip\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.fullcircle.Snip.SnipType\x12,\n\tping_snip\x18\x0b \x01(\x0b\x32\x19.fullcircle.Snip.PingSnip\x12,\n\tpong_snip\x18\x0c \x01(\x0b\x32\x19.fullcircle.Snip.PongSnip\x12.\n\nerror_snip\x18\r \x01(\x0b\x32\x1a.fullcircle.Snip.ErrorSnip\x12.\n\x08req_snip\x18\x0e \x01(\x0b\x32\x1c.fullcircle.Snip.RequestSnip\x12.\n\nstart_snip\x18\x0f \x01(\x0b\x32\x1a.fullcircle.Snip.StartSnip\x12.\n\nframe_snip\x18\x10 \x01(\x0b\x32\x1a.fullcircle.Snip.FrameSnip\x12*\n\x08\x61\x63k_snip\x18\x11 \x01(\x0b\x32\x18.fullcircle.Snip.AckSnip\x12,\n\tnack_snip\x18\x12 \x01(\x0b\x32\x19.fullcircle.Snip.NackSnip\x12\x32\n\x0ctimeout_snip\x18\x13 \x01(\x0b\x32\x1c.fullcircle.Snip.TimeoutSnip\x12.\n\nabort_snip\x18\x14 \x01(\x0b\x32\x1a.fullcircle.Snip.AbortSnip\x12*\n\x08\x65os_snip\x18\x15 \x01(\x0b\x32\x18.fullcircle.Snip.EosSnip\x1a\x19\n\x08PingSnip\x12\r\n\x05\x63ount\x18\x01 \x02(\r\x1a\x19\n\x08PongSnip\x12\r\n\x05\x63ount\x18\x01 \x02(\r\x1aS\n\tErrorSnip\x12\x31\n\terrorcode\x18\x01 \x02(\x0e\x32\x1e.fullcircle.Snip.ErrorCodeType\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x1a]\n\x0bRequestSnip\x12\r\n\x05\x63olor\x18\x01 \x02(\t\x12\r\n\x05seqId\x18\x02 \x02(\r\x12\x30\n\x04meta\x18\x03 \x02(\x0b\x32\".fullcircle.BinarySequenceMetadata\x1a\x0b\n\tStartSnip\x1a\x33\n\tFrameSnip\x12&\n\x05\x66rame\x18\x01 \x02(\x0b\x32\x17.fullcircle.BinaryFrame\x1a\t\n\x07\x41\x63kSnip\x1a\n\n\x08NackSnip\x1a\r\n\x0bTimeoutSnip\x1a\x0b\n\tAbortSnip\x1a\t\n\x07\x45osSnip\"\x80\x01\n\x08SnipType\x12\x08\n\x04PING\x10\x01\x12\x08\n\x04PONG\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0b\n\x07REQUEST\x10\x04\x12\t\n\x05START\x10\x05\x12\t\n\x05\x46RAME\x10\x06\x12\x07\n\x03\x41\x43K\x10\x07\x12\x08\n\x04NACK\x10\x08\x12\x0b\n\x07TIMEOUT\x10\t\x12\t\n\x05\x41\x42ORT\x10\n\x12\x07\n\x03\x45OS\x10\x0b\"+\n\rErrorCodeType\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0e\x44\x45\x43ODING_ERROR\x10\x02')



_SNIP_SNIPTYPE = descriptor.EnumDescriptor(
  name='SnipType',
  full_name='fullcircle.Snip.SnipType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='PING', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PONG', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='REQUEST', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='START', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FRAME', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACK', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NACK', index=7, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=8, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ABORT', index=9, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EOS', index=10, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1337,
  serialized_end=1465,
)

_SNIP_ERRORCODETYPE = descriptor.EnumDescriptor(
  name='ErrorCodeType',
  full_name='fullcircle.Snip.ErrorCodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OK', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DECODING_ERROR', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1467,
  serialized_end=1510,
)


_BINARYSEQUENCEMETADATA = descriptor.Descriptor(
  name='BinarySequenceMetadata',
  full_name='fullcircle.BinarySequenceMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='frames_per_second', full_name='fullcircle.BinarySequenceMetadata.frames_per_second', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='fullcircle.BinarySequenceMetadata.width', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='height', full_name='fullcircle.BinarySequenceMetadata.height', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator_name', full_name='fullcircle.BinarySequenceMetadata.generator_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator_version', full_name='fullcircle.BinarySequenceMetadata.generator_version', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=31,
  serialized_end=164,
)


_RGBVALUE = descriptor.Descriptor(
  name='RGBValue',
  full_name='fullcircle.RGBValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='red', full_name='fullcircle.RGBValue.red', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='green', full_name='fullcircle.RGBValue.green', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='blue', full_name='fullcircle.RGBValue.blue', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='fullcircle.RGBValue.x', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='fullcircle.RGBValue.y', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=166,
  serialized_end=240,
)


_BINARYFRAME = descriptor.Descriptor(
  name='BinaryFrame',
  full_name='fullcircle.BinaryFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pixel', full_name='fullcircle.BinaryFrame.pixel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=242,
  serialized_end=292,
)


_BINARYSEQUENCE = descriptor.Descriptor(
  name='BinarySequence',
  full_name='fullcircle.BinarySequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='metadata', full_name='fullcircle.BinarySequence.metadata', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame', full_name='fullcircle.BinarySequence.frame', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=294,
  serialized_end=404,
)


_SNIP_PINGSNIP = descriptor.Descriptor(
  name='PingSnip',
  full_name='fullcircle.Snip.PingSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count', full_name='fullcircle.Snip.PingSnip.count', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=974,
  serialized_end=999,
)

_SNIP_PONGSNIP = descriptor.Descriptor(
  name='PongSnip',
  full_name='fullcircle.Snip.PongSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count', full_name='fullcircle.Snip.PongSnip.count', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=1001,
  serialized_end=1026,
)

_SNIP_ERRORSNIP = descriptor.Descriptor(
  name='ErrorSnip',
  full_name='fullcircle.Snip.ErrorSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='errorcode', full_name='fullcircle.Snip.ErrorSnip.errorcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='fullcircle.Snip.ErrorSnip.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1028,
  serialized_end=1111,
)

_SNIP_REQUESTSNIP = descriptor.Descriptor(
  name='RequestSnip',
  full_name='fullcircle.Snip.RequestSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='color', full_name='fullcircle.Snip.RequestSnip.color', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seqId', full_name='fullcircle.Snip.RequestSnip.seqId', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='meta', full_name='fullcircle.Snip.RequestSnip.meta', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=1113,
  serialized_end=1206,
)

_SNIP_STARTSNIP = descriptor.Descriptor(
  name='StartSnip',
  full_name='fullcircle.Snip.StartSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1208,
  serialized_end=1219,
)

_SNIP_FRAMESNIP = descriptor.Descriptor(
  name='FrameSnip',
  full_name='fullcircle.Snip.FrameSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='frame', full_name='fullcircle.Snip.FrameSnip.frame', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=1221,
  serialized_end=1272,
)

_SNIP_ACKSNIP = descriptor.Descriptor(
  name='AckSnip',
  full_name='fullcircle.Snip.AckSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1274,
  serialized_end=1283,
)

_SNIP_NACKSNIP = descriptor.Descriptor(
  name='NackSnip',
  full_name='fullcircle.Snip.NackSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1285,
  serialized_end=1295,
)

_SNIP_TIMEOUTSNIP = descriptor.Descriptor(
  name='TimeoutSnip',
  full_name='fullcircle.Snip.TimeoutSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1297,
  serialized_end=1310,
)

_SNIP_ABORTSNIP = descriptor.Descriptor(
  name='AbortSnip',
  full_name='fullcircle.Snip.AbortSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1312,
  serialized_end=1323,
)

_SNIP_EOSSNIP = descriptor.Descriptor(
  name='EosSnip',
  full_name='fullcircle.Snip.EosSnip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1325,
  serialized_end=1334,
)

_SNIP = descriptor.Descriptor(
  name='Snip',
  full_name='fullcircle.Snip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='fullcircle.Snip.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ping_snip', full_name='fullcircle.Snip.ping_snip', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pong_snip', full_name='fullcircle.Snip.pong_snip', index=2,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_snip', full_name='fullcircle.Snip.error_snip', index=3,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='req_snip', full_name='fullcircle.Snip.req_snip', index=4,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_snip', full_name='fullcircle.Snip.start_snip', index=5,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frame_snip', full_name='fullcircle.Snip.frame_snip', index=6,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ack_snip', full_name='fullcircle.Snip.ack_snip', index=7,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nack_snip', full_name='fullcircle.Snip.nack_snip', index=8,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout_snip', full_name='fullcircle.Snip.timeout_snip', index=9,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='abort_snip', full_name='fullcircle.Snip.abort_snip', index=10,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='eos_snip', full_name='fullcircle.Snip.eos_snip', index=11,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SNIP_PINGSNIP, _SNIP_PONGSNIP, _SNIP_ERRORSNIP, _SNIP_REQUESTSNIP, _SNIP_STARTSNIP, _SNIP_FRAMESNIP, _SNIP_ACKSNIP, _SNIP_NACKSNIP, _SNIP_TIMEOUTSNIP, _SNIP_ABORTSNIP, _SNIP_EOSSNIP, ],
  enum_types=[
    _SNIP_SNIPTYPE,
    _SNIP_ERRORCODETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=407,
  serialized_end=1510,
)

_BINARYFRAME.fields_by_name['pixel'].message_type = _RGBVALUE
_BINARYSEQUENCE.fields_by_name['metadata'].message_type = _BINARYSEQUENCEMETADATA
_BINARYSEQUENCE.fields_by_name['frame'].message_type = _BINARYFRAME
_SNIP_PINGSNIP.containing_type = _SNIP;
_SNIP_PONGSNIP.containing_type = _SNIP;
_SNIP_ERRORSNIP.fields_by_name['errorcode'].enum_type = _SNIP_ERRORCODETYPE
_SNIP_ERRORSNIP.containing_type = _SNIP;
_SNIP_REQUESTSNIP.fields_by_name['meta'].message_type = _BINARYSEQUENCEMETADATA
_SNIP_REQUESTSNIP.containing_type = _SNIP;
_SNIP_STARTSNIP.containing_type = _SNIP;
_SNIP_FRAMESNIP.fields_by_name['frame'].message_type = _BINARYFRAME
_SNIP_FRAMESNIP.containing_type = _SNIP;
_SNIP_ACKSNIP.containing_type = _SNIP;
_SNIP_NACKSNIP.containing_type = _SNIP;
_SNIP_TIMEOUTSNIP.containing_type = _SNIP;
_SNIP_ABORTSNIP.containing_type = _SNIP;
_SNIP_EOSSNIP.containing_type = _SNIP;
_SNIP.fields_by_name['type'].enum_type = _SNIP_SNIPTYPE
_SNIP.fields_by_name['ping_snip'].message_type = _SNIP_PINGSNIP
_SNIP.fields_by_name['pong_snip'].message_type = _SNIP_PONGSNIP
_SNIP.fields_by_name['error_snip'].message_type = _SNIP_ERRORSNIP
_SNIP.fields_by_name['req_snip'].message_type = _SNIP_REQUESTSNIP
_SNIP.fields_by_name['start_snip'].message_type = _SNIP_STARTSNIP
_SNIP.fields_by_name['frame_snip'].message_type = _SNIP_FRAMESNIP
_SNIP.fields_by_name['ack_snip'].message_type = _SNIP_ACKSNIP
_SNIP.fields_by_name['nack_snip'].message_type = _SNIP_NACKSNIP
_SNIP.fields_by_name['timeout_snip'].message_type = _SNIP_TIMEOUTSNIP
_SNIP.fields_by_name['abort_snip'].message_type = _SNIP_ABORTSNIP
_SNIP.fields_by_name['eos_snip'].message_type = _SNIP_EOSSNIP
_SNIP_SNIPTYPE.containing_type = _SNIP;
_SNIP_ERRORCODETYPE.containing_type = _SNIP;
DESCRIPTOR.message_types_by_name['BinarySequenceMetadata'] = _BINARYSEQUENCEMETADATA
DESCRIPTOR.message_types_by_name['RGBValue'] = _RGBVALUE
DESCRIPTOR.message_types_by_name['BinaryFrame'] = _BINARYFRAME
DESCRIPTOR.message_types_by_name['BinarySequence'] = _BINARYSEQUENCE
DESCRIPTOR.message_types_by_name['Snip'] = _SNIP

class BinarySequenceMetadata(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BINARYSEQUENCEMETADATA
  
  # @@protoc_insertion_point(class_scope:fullcircle.BinarySequenceMetadata)

class RGBValue(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RGBVALUE
  
  # @@protoc_insertion_point(class_scope:fullcircle.RGBValue)

class BinaryFrame(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BINARYFRAME
  
  # @@protoc_insertion_point(class_scope:fullcircle.BinaryFrame)

class BinarySequence(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BINARYSEQUENCE
  
  # @@protoc_insertion_point(class_scope:fullcircle.BinarySequence)

class Snip(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class PingSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_PINGSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.PingSnip)
  
  class PongSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_PONGSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.PongSnip)
  
  class ErrorSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_ERRORSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.ErrorSnip)
  
  class RequestSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_REQUESTSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.RequestSnip)
  
  class StartSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_STARTSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.StartSnip)
  
  class FrameSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_FRAMESNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.FrameSnip)
  
  class AckSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_ACKSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.AckSnip)
  
  class NackSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_NACKSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.NackSnip)
  
  class TimeoutSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_TIMEOUTSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.TimeoutSnip)
  
  class AbortSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_ABORTSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.AbortSnip)
  
  class EosSnip(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SNIP_EOSSNIP
    
    # @@protoc_insertion_point(class_scope:fullcircle.Snip.EosSnip)
  DESCRIPTOR = _SNIP
  
  # @@protoc_insertion_point(class_scope:fullcircle.Snip)

# @@protoc_insertion_point(module_scope)
