from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Directory(_message.Message):
    __slots__ = ["dirname", "extension"]
    DIRNAME_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    dirname: str
    extension: str
    def __init__(self, dirname: _Optional[str] = ..., extension: _Optional[str] = ...) -> None: ...
