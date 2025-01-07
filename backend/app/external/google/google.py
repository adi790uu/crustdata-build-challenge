import google.generativeai as genai
from app.core.config import settings


def get_base_prompt(api_endpoint_names, user_query):
    return f"""
        You are a customer support agent which answers users questions about Crustdata's APIs, you have to answer the user query
        with the API information which we have provided to you.
     
        Here is the api description for answering the user query: {api_endpoint_names}
        User query: {user_query}
        
        - Provide examples in curl if possible and structure the response in a clear and professional way.
        - Keep the responses to the point and don't try to overhelp the user.
    """  # noqa


api_endpoints_description = """
### COMPANY API ENDPOINTS

1. - **Name:** get_company_data_api_info
   - **Description:** This endpoint enriches company data by retrieving detailed information about one or multiple companies using either their domain, name, or ID.
   - **Endpoint:** `ttps://api.crustdata.com/screener/company/`

2. - **Name:** get_screening_api_info
   - **Description:** Allows screening and filtering of companies based on growth and firmographic criteria.
   - **Endpoint:** `https://api.crustdata.com/screener/screen/` (Method: POST)

3. - **Name:** get_identification_api_info
   - **Description:** Identify companies in Crustdata's database using the company name, website, or LinkedIn profile URL.
   - **Endpoint:** `https://api.crustdata.com/screener/identify/` (Method: POST)

4. - **Name:** get_dataset_api_info
   - **Description:** Retrieve job listings based on specified filters.
   - **Endpoint:** `https://api.crustdata.com/data_lab/job_listings/Table/`, `https://api.crustdata.com/data_lab/funding_milestone_timeseries/`,
                `https://api.crustdata.com/data_lab/decision_makers/`, `https://api.crustdata.com/data_lab/headcount_timeseries/`, 
                `https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/`, `http://api.crustdata.com/data_lab/g2_profile_metrics/Table/`,
                `https://api.crustdata.com/data_lab/webtraffic/`, `https://api.crustdata.com/data_lab/investor_portfolio/`.

5. - **Name:** get_linkedin_company_search_api_info
    - **Description:** Search for company profiles using either a LinkedIn Sales Navigator account's search URL or custom search criteria as a filter.
    - **Endpoint:** `POST /screener/company/search`

6. - **Name:** get_linkedin_posts_company_api_info
    - **Description:** Fetch recent LinkedIn posts and engagement metrics for a specified company.
    - **Endpoint:** `https://api.crustdata.com/screener/linkedin_posts` (Method: GET)

7. - **Name:** get_linkedin_posts_keyword_api_info
    - **Description:** Retrieve LinkedIn posts containing specified keywords along with engagement metrics.
    - **Endpoint:** `/screener/linkedin_posts/keyword_search/` (Method: POST)
    
    ### PEOPLE API ENDPOINTS

1. - **Name:** get_people_profile_api_info
   - **Description**: Enrich data for one or more individuals using LinkedIn profile URLs or business email addresses.
   - **Endpoint**: `/screener/person/enrich`

2. - **Name:** get_people_search_api_info
   - **Description**: Search for people profiles based on either a direct LinkedIn Sales Navigator search URL or custom search criteria.
   - **Endpoint**: `https://api.crustdata.com/screener/person/search`

3. - **Name:** get_linkedin_posts_by_person_api_info
   - **Description**: Retrieve posts made by a specific person on LinkedIn.
   - **Endpoint**: https://api.crustdata.com/screener/linkedin_posts?person_linkedin_url=<person linkedin url>.

4. - **Name:** get_remaining_credits_api_info
   - **Description**: Check the remaining credits for the user.
   - **Endpoint**: `https://api.crustdata.com/user/credits`
    
"""  # noqa


def query_analyzer(api_endpoints: str):
    f"""This function determines which api endpoints name does the user query is referencing
        or need information about, choose the api names required carefully.

    Here is the api descriptions: {api_endpoints_description}


    Args:
        api_endpoints: str of api_endpoints name user query needs else empty list

    Returns:
        A dictionary containing the api_endpoints field.
    """  # noqa
    return {"api_endpoints": api_endpoints}


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
            system_instruction=api_endpoints_description,
        )

    async def chat_with_agent(self, prompt: str, api_end_point):

        prompt = get_base_prompt(
            user_query=prompt,
            api_endpoint_names=api_end_point,
        )
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
