from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NOT_FINISHED: _ClassVar[FinishReason]
    MAX_TOKENS: _ClassVar[FinishReason]
    EOS_TOKEN: _ClassVar[FinishReason]
    CANCELLED: _ClassVar[FinishReason]
    TIME_LIMIT: _ClassVar[FinishReason]
    STOP_SEQUENCE: _ClassVar[FinishReason]
    TOKEN_LIMIT: _ClassVar[FinishReason]
    ERROR: _ClassVar[FinishReason]
NOT_FINISHED: FinishReason
MAX_TOKENS: FinishReason
EOS_TOKEN: FinishReason
CANCELLED: FinishReason
TIME_LIMIT: FinishReason
STOP_SEQUENCE: FinishReason
TOKEN_LIMIT: FinishReason
ERROR: FinishReason
