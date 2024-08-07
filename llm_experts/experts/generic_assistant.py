from typing import Optional
from common.logger import get_logger

from llm_experts.conf import experts
from llm_experts.store import MongoStore
from llm_experts.meta import (
    OpenAIChatExpert,
    GenericAssistantInput,
    GenericAssistantOutput,
)


logger = get_logger(__name__)


class GenericAssistant(OpenAIChatExpert):
    def __init__(
        self,
        max_concurrency: int = 10,
        mongo_store: Optional[MongoStore] = None,
    ):
        super().__init__(
            conf_path=f"{experts.__path__[0]}/generic-assistant.yaml",
            expert_output=GenericAssistantOutput,
            with_message_history=True,
            input_messages_key="user_query",
            max_messages=20,
            max_concurrency=max_concurrency,
            mongo_store=mongo_store,
        )

    def generate(
        self,
        expert_input: GenericAssistantInput,
    ) -> GenericAssistantOutput:
        return self._generate(expert_input=expert_input)
