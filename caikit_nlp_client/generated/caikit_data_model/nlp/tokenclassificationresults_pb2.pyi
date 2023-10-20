from caikit_nlp_client.generated.caikit_data_model.nlp import tokenclassificationresult_pb2 as _tokenclassificationresult_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenClassificationResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_tokenclassificationresult_pb2.TokenClassificationResult]
    def __init__(self, results: _Optional[_Iterable[_Union[_tokenclassificationresult_pb2.TokenClassificationResult, _Mapping]]] = ...) -> None: ...
