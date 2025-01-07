from fastapi import FastAPI
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.chat import ChatRequest
from app.external.google.google import Agent
from app.core import company_api_info
from app.core import people_api_info


app = FastAPI(
    title=settings.APP_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}


@app.post("/api/chat")
async def chat_with_agent(request: ChatRequest):
    agent = Agent(model_name=settings.MODEL_NAME)
    api_endpoints = await agent.chat_with_agent_with_tools(
        prompt=request.user_query,
    )

    func_map = {
        "get_company_data_api_info": company_api_info.get_company_data_api_info,
        "get_screening_api_info": company_api_info.get_screening_api_info,
        "get_identification_api_info": company_api_info.get_identification_api_info,
        "get_dataset_api_info": company_api_info.get_dataset_api_info,
        "get_linkedin_company_search_api_info": company_api_info.get_linkedin_company_search_api,
        "get_linkedin_posts_company_api_info": company_api_info.get_linkedin_posts_company_api,
        "get_linkedin_posts_keyword_api_info": company_api_info.get_linkedin_posts_keyword_api,
        "get_people_profile_api_info": people_api_info.get_people_profile_api,
        "get_people_search_api_info": people_api_info.get_people_search_api,
        "get_linkedin_posts_by_person_api_info": people_api_info.get_linkedin_posts_by_person_api,
        "get_remaining_credits_api_info": people_api_info.get_remaining_credits_api,
    }
    response = await agent.chat_with_agent(
        prompt=request.user_query, api_end_point=func_map[api_endpoints]
    )
    return response
