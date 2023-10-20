from caikit_nlp_client.generated.caikit.runtime.Nlp import datastreamsourcegenerationtrainrecordjsondata_pb2 as _datastreamsourcegenerationtrainrecordjsondata_pb2
from caikit_nlp_client.generated.caikit_data_model.common import directory_pb2 as _directory_pb2
from caikit_nlp_client.generated.caikit_data_model.common import file_pb2 as _file_pb2
from caikit_nlp_client.generated.caikit_data_model.common import listoffiles_pb2 as _listoffiles_pb2
from caikit_nlp_client.generated.caikit_data_model.common import s3files_pb2 as _s3files_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataStreamSourceGenerationTrainRecord(_message.Message):
    __slots__ = ["jsondata", "file", "listoffiles", "directory", "s3files"]
    JSONDATA_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    LISTOFFILES_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    S3FILES_FIELD_NUMBER: _ClassVar[int]
    jsondata: _datastreamsourcegenerationtrainrecordjsondata_pb2.DataStreamSourceGenerationTrainRecordJsonData
    file: _file_pb2.File
    listoffiles: _listoffiles_pb2.ListOfFiles
    directory: _directory_pb2.Directory
    s3files: _s3files_pb2.S3Files
    def __init__(self, jsondata: _Optional[_Union[_datastreamsourcegenerationtrainrecordjsondata_pb2.DataStreamSourceGenerationTrainRecordJsonData, _Mapping]] = ..., file: _Optional[_Union[_file_pb2.File, _Mapping]] = ..., listoffiles: _Optional[_Union[_listoffiles_pb2.ListOfFiles, _Mapping]] = ..., directory: _Optional[_Union[_directory_pb2.Directory, _Mapping]] = ..., s3files: _Optional[_Union[_s3files_pb2.S3Files, _Mapping]] = ...) -> None: ...
