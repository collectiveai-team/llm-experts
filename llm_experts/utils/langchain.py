from langchain_community.callbacks import OpenAICallbackHandler


def parse_openai_callback(callback: OpenAICallbackHandler) -> dict:
    parsed_callback = {
        "completion_tokens": callback.completion_tokens,
        "prompt_tokens": callback.prompt_tokens,
        "total_tokens": callback.total_tokens,
        "total_cost": callback.total_cost,
    }

    return parsed_callback
