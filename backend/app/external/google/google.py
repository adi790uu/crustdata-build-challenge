import google.generativeai as genai
from app.core.config import settings
from app.prompts.prompts import (
    chat_with_agent_base_prompt,
    chat_with_agent_with_tools_base_prompt,
    agent_description,
    api_endpoints_description,
)


def query_analyzer(api_endpoint_name: str):
    f"""This function determines which api endpoints name does the user query is referencing
        or need information about, choose the api names required carefully.

    Here is the api descriptions: {api_endpoints_description}


    Args:
        api_endpoint_name: str of api_endpoint name user query needs else empty list

    Returns:
        A dictionary containing the api_endpoints field.
    """  # noqa
    return {"api_endpoint_name": api_endpoint_name}


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
            system_instruction=agent_description,
        )

    async def chat_with_agent(self, prompt: str, api_end_point):

        prompt = chat_with_agent_base_prompt(
            user_query=prompt,
            api_endpoint_name=api_end_point,
        )
        response = await self.model.generate_content_async(
            [prompt],
        )
        return response.candidates[0].content.parts[0].text

    async def chat_with_agent_with_tools(self, user_query: str):
        prompt = chat_with_agent_with_tools_base_prompt(user_query=user_query)
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
