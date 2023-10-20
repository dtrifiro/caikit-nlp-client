from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Token(_message.Message):
    __slots__ = ["start", "end", "text"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    text: str
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
