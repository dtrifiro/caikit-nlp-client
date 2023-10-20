from caikit_nlp_client.generated.caikit_data_model.caikit_nlp import generationtrainrecord_pb2 as _generationtrainrecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataStreamSourceGenerationTrainRecordJsonData(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_generationtrainrecord_pb2.GenerationTrainRecord]
    def __init__(self, data: _Optional[_Iterable[_Union[_generationtrainrecord_pb2.GenerationTrainRecord, _Mapping]]] = ...) -> None: ...
