import grpc
import logging

from .client import CaikitNlpClient
from .model.text_generation import TextGenerationTask, TextGenerationTaskResult
from .generated.nlpservice_pb2_grpc import NlpServiceStub
from .generated.caikit.runtime.Nlp.textgenerationtaskrequest_pb2 import TextGenerationTaskRequest


class GrpcCaikitNlpClient(CaikitNlpClient):

    def __init__(self, channel: grpc.Channel) -> None:
        self.stub = NlpServiceStub(channel)

    def create_text_generation_task(self, task: TextGenerationTask) -> TextGenerationTaskResult:
        logging.info("Calling CreateTextGenerationTask")
        try:
            if task.model_id == "":
                raise ValueError("request must have a model id")

            metadata = [("mm-model-id", task.model_id)]

            request = TextGenerationTaskRequest()
            request.text = task.text
            request.preserve_input_text = False
            request.max_new_tokens = 200
            request.min_new_tokens = 10

            response = self.stub.TextGenerationTaskPredict(request=request, metadata=metadata)
            logging.debug(f"Response response: {response}")
            result = TextGenerationTaskResult(response.generated_text)
            return result
        except Exception as exc:
            logging.error(f"Caught exception {exc}, rethrowing")
            raise exc
