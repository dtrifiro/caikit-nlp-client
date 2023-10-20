from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass


class PredictionServiceStub(object):
    """open source marker; do not remove
    PredictionService provides access to machine-learned models loaded by
    model_servers.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        desc_pool = DescriptorPool(reflection_db)
        self.TextGenerationTaskRequest = GetMessageClass(
            desc_pool.FindMessageTypeByName('caikit.runtime.Nlp.TextGenerationTaskRequest'))()
        self.GeneratedTextResult = GetMessageClass(
            desc_pool.FindMessageTypeByName('caikit_data_model.nlp.GeneratedTextResult'))()
        self.TextGenerationTaskPredict = channel.unary_unary(
            '/caikit.runtime.Nlp.NlpService/TextGenerationTaskPredict',
            request_serializer=self.TextGenerationTaskRequest.SerializeToString,
            response_deserializer=self.GeneratedTextResult.FromString,
        )
        self.ServerStreamingTextGenerationTaskPredict = channel.unary_stream(
            '/caikit.runtime.Nlp.NlpService/ServerStreamingTextGenerationTaskPredict',
            request_serializer=self.TextGenerationTaskRequest.SerializeToString,
            response_deserializer=self.GeneratedTextResult.FromString,
        )
