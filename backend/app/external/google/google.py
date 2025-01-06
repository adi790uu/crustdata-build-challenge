import google.generativeai as genai
from app.prompts import prompts
from google.ai.generativelanguage_v1beta.types import content
from app.core.config import settings


def query_analyzer(is_component: bool):
    """This function determines whether the user wants to create a UI component or a complete website.

    Args:
        is_component: True if the user wants to create a UI component, False otherwise.

    Returns:
        A dictionary containing the is_component field.
    """
    return {"is_component": is_component}


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}


class Agent:
    def __init__(self, model_name: str, chat_history=None):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            system_instruction=prompts.get_prompt(chat_history=chat_history),
        )

    async def chat_with_agent(self, prompt: str):
        response = await self.model.generate_content_async(
            [prompt],
        )
        return response.candidates[0].content.parts[0].text

    async def chat_with_agent_with_tools(self, prompt: str):
        response = await self.model.generate_content_async(
            [prompt],
            tools=[query_analyzer],
            tool_config={
                "function_calling_config": {
                    "mode": "ANY",
                },
            },
        )
        for part in response.parts:
            if fn := part.function_call:
                for _, val in fn.args.items():
                    return val
