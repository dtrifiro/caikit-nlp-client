from caikit_nlp_client.generated.caikit.runtime.Nlp import textgenerationtasktextgenerationtrainparameters_pb2 as _textgenerationtasktextgenerationtrainparameters_pb2
from caikit_nlp_client.generated.caikit_data_model.common import s3path_pb2 as _s3path_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenerationTaskTextGenerationTrainRequest(_message.Message):
    __slots__ = ["model_name", "output_path", "parameters"]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    output_path: _s3path_pb2.S3Path
    parameters: _textgenerationtasktextgenerationtrainparameters_pb2.TextGenerationTaskTextGenerationTrainParameters
    def __init__(self, model_name: _Optional[str] = ..., output_path: _Optional[_Union[_s3path_pb2.S3Path, _Mapping]] = ..., parameters: _Optional[_Union[_textgenerationtasktextgenerationtrainparameters_pb2.TextGenerationTaskTextGenerationTrainParameters, _Mapping]] = ...) -> None: ...
