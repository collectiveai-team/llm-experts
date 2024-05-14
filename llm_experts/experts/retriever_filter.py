from typing import Optional

from redis_cache import RedisCache
from llm_experts.logger import get_logger
from llm_experts.utils.json_data import get_pretty
from llm_experts.meta import (
    OpenAIChatExpert,
    RretrieverFilterExpertInput,
    RretrieverFilterExpertInputWrapper,
    RretrieverFilterExpertOutput,
)


logger = get_logger(__name__)


class RetrieverFilterExpert(OpenAIChatExpert):
    def __init__(
        self,
        conf_path: str = "/resources/llm-experts/retriever-filter.yaml",
        max_concurrency: int = 10,
        cache: Optional[RedisCache] = None,
    ):
        super().__init__(
            conf_path=conf_path,
            expert_output=RretrieverFilterExpertOutput,
            max_concurrency=max_concurrency,
            cache=cache,
        )

    def expert_input_wrapper(
        self,
        expert_input: RretrieverFilterExpertInput,
    ) -> RretrieverFilterExpertInputWrapper:
        expert_input_dict = expert_input.model_dump()
        return RretrieverFilterExpertInputWrapper(
            text_chunks=get_pretty(obj=expert_input_dict["text_chunks"]),
            query_text=expert_input_dict["query_text"],
        )

    def generate(
        self,
        expert_input: RretrieverFilterExpertInput,
    ) -> RretrieverFilterExpertOutput:
        return self._generate(
            self.expert_input_wrapper(expert_input=expert_input)
        )
