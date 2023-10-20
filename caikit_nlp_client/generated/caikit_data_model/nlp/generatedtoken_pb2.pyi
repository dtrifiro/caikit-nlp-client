from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratedToken(_message.Message):
    __slots__ = ["text", "logprob"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LOGPROB_FIELD_NUMBER: _ClassVar[int]
    text: str
    logprob: float
    def __init__(self, text: _Optional[str] = ..., logprob: _Optional[float] = ...) -> None: ...
