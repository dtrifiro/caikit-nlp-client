from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrainingInfoRequest(_message.Message):
    __slots__ = ["training_id"]
    TRAINING_ID_FIELD_NUMBER: _ClassVar[int]
    training_id: str
    def __init__(self, training_id: _Optional[str] = ...) -> None: ...
