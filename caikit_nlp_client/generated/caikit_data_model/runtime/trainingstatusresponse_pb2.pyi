from caikit_nlp_client.generated.caikit_data_model.common import trainingstatus_pb2 as _trainingstatus_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrainingStatusResponse(_message.Message):
    __slots__ = ["training_id", "state", "submission_timestamp", "completion_timestamp", "reasons"]
    TRAINING_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    training_id: str
    state: _trainingstatus_pb2.TrainingStatus
    submission_timestamp: _timestamp_pb2.Timestamp
    completion_timestamp: _timestamp_pb2.Timestamp
    reasons: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, training_id: _Optional[str] = ..., state: _Optional[_Union[_trainingstatus_pb2.TrainingStatus, str]] = ..., submission_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reasons: _Optional[_Iterable[str]] = ...) -> None: ...
