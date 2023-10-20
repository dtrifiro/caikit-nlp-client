from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExponentialDecayLengthPenalty(_message.Message):
    __slots__ = ["start_index", "decay_factor"]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    DECAY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    decay_factor: float
    def __init__(self, start_index: _Optional[int] = ..., decay_factor: _Optional[float] = ...) -> None: ...
