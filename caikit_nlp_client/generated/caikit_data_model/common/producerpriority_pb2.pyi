from caikit_nlp_client.generated.caikit_data_model.common import producerid_pb2 as _producerid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProducerPriority(_message.Message):
    __slots__ = ["producers"]
    PRODUCERS_FIELD_NUMBER: _ClassVar[int]
    producers: _containers.RepeatedCompositeFieldContainer[_producerid_pb2.ProducerId]
    def __init__(self, producers: _Optional[_Iterable[_Union[_producerid_pb2.ProducerId, _Mapping]]] = ...) -> None: ...
