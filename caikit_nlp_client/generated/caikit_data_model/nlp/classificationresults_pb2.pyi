from caikit_nlp_client.generated.caikit_data_model.nlp import classificationresult_pb2 as _classificationresult_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClassificationResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_classificationresult_pb2.ClassificationResult]
    def __init__(self, results: _Optional[_Iterable[_Union[_classificationresult_pb2.ClassificationResult, _Mapping]]] = ...) -> None: ...
