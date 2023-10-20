from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClassificationTrainRecord(_message.Message):
    __slots__ = ["text", "labels"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    text: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
