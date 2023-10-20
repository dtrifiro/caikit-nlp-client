import abc

from .model.text_generation import TextGenerationTask, TextGenerationTaskResult


class CaikitNlpClient(abc.ABC):
    @abc.abstractmethod
    def create_text_generation_task(self, request: TextGenerationTask) -> TextGenerationTaskResult:
        pass
