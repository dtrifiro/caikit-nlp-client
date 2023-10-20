from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BidiStreamingTokenClassificationTaskRequest(_message.Message):
    __slots__ = ["text_stream", "threshold"]
    TEXT_STREAM_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    text_stream: str
    threshold: float
    def __init__(self, text_stream: _Optional[str] = ..., threshold: _Optional[float] = ...) -> None: ...
