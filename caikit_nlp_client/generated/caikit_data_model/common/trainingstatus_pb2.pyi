from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TrainingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PLACEHOLDER_UNSET: _ClassVar[TrainingStatus]
    QUEUED: _ClassVar[TrainingStatus]
    RUNNING: _ClassVar[TrainingStatus]
    COMPLETED: _ClassVar[TrainingStatus]
    CANCELED: _ClassVar[TrainingStatus]
    ERRORED: _ClassVar[TrainingStatus]
PLACEHOLDER_UNSET: TrainingStatus
QUEUED: TrainingStatus
RUNNING: TrainingStatus
COMPLETED: TrainingStatus
CANCELED: TrainingStatus
ERRORED: TrainingStatus
