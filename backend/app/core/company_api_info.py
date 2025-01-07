get_company_data_api_info = """
    {
  "api_name": "Enrichment: Company Data API",
  "overview": "This endpoint enriches company data by retrieving detailed information about one or multiple companies using either their domain, name, or ID.",
  "authentication": {
    "type": "auth_token",
    "required": true
  },
  "parameters": {
    "company_domain": {
      "type": "string",
      "description": "The domain(s) of the company(ies) you want to retrieve data for.",
      "example": "company_domain=hubspot.com,google.com",
      "limit": 25
    },
    "company_name": {
      "type": "string",
      "description": "The name(s) of the company(ies) you want to retrieve data for.",
      "example": "company_name=\"Acme, Inc.\",\"Widget Co\"",
      "limit": 25
    },
    "company_linkedin_url": {
      "type": "string",
      "description": "The LinkedIn URL(s) of the company(ies).",
      "example": "company_linkedin_url=https://linkedin.com/company/hubspot,https://linkedin.com/company/clay-hq",
      "limit": 25
    },
    "company_id": {
      "type": "integer",
      "description": "The unique ID(s) of the company(ies) you want to retrieve data for.",
      "example": "company_id=12345,67890",
      "limit": 25
    },
    "fields": {
      "type": "string",
      "description": "Specifies the fields you want to include in the response. Supports nested fields up to a certain level.",
      "example": "fields=company_name,company_domain,glassdoor.glassdoor_review_count"
    },
    "enrich_realtime": {
      "type": "boolean",
      "description": "When True and the requested company is not present in Crustdata’s database, the company is enriched within 10 minutes of the request.",
      "default": false
    }
  },
  "field_notes": {
    "nested_fields": "You can specify nested fields up to the levels defined in the response structure.",
    "default_fields": {
      "top_level": "All top-level non-object fields are included if the 'fields' parameter is not specified.",
      "object_fields": "Not included by default; must be explicitly requested."
    },
    "user_permissions": "Access to certain fields may be restricted based on user permissions."
  },
  "examples": [
    {
      "use_case": "Retrieve data by company domain.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_domain=hubspot.com,google.com' --header 'Authorization: Token $token'"
    },
    {
      "use_case": "Retrieve data by company name.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_name=\"HubSpot\",\"Google, Inc.\"' --header 'Authorization: Token $token'"
    },
    {
      "use_case": "Retrieve data by LinkedIn URL.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_linkedin_url=https://linkedin.com/company/hubspot,https://linkedin.com/company/clay-hq' --header 'Authorization: Token $token'"
    },
    {
      "use_case": "Retrieve data by company ID.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_id=631480,789001' --header 'Authorization: Token $token'"
    },
    {
      "use_case": "Retrieve specific fields.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_domain=swiggy.com&fields=company_name,headcount.linkedin_headcount' --header 'Authorization: Token $token'"
    },
    {
      "use_case": "Enable real-time enrichment.",
      "request": "curl 'https://api.crustdata.com/screener/company?company_linkedin_url=https://linkedin.com/company/usebramble&enrich_realtime=True' --header 'Authorization: Token $token'"
    }
  ],
  "response_structure": {
    "top_level_fields": [
      "company_id",
      "company_name",
      "linkedin_profile_url",
      "linkedin_id",
      "linkedin_logo_url",
      "company_twitter_url",
      "company_website_domain",
      "hq_country",
      "headquarters",
      "largest_headcount_country",
      "hq_street_address",
      "company_website",
      "year_founded",
      "fiscal_year_end",
      "estimated_revenue_lower_bound_usd",
      "estimated_revenue_higher_bound_usd",
      "employee_count_range",
      "company_type",
      "linkedin_company_description",
      "acquisition_status",
      "ceo_location"
    ],
    "nested_objects": {
      "all_office_addresses": "array of strings",
      "markets": "array of strings",
      "stock_symbols": "array of strings",
      "taxonomy": {
        "linkedin_specialities": "array of strings",
        "linkedin_industries": "array of strings",
        "crunchbase_categories": "array of strings"
      },
      "competitors": {
        "competitor_website_domains": "array of strings",
        "paid_seo_competitors_website_domains": "array of strings",
        "organic_seo_competitors_website_domains": "array of strings"
      },
      "headcount": {
        "linkedin_headcount": "integer",
        "linkedin_headcount_total_growth_percent": {
          "mom": "float",
          "qoq": "float",
          "six_months": "float",
          "yoy": "float",
          "two_years": "float"
        }
      },
      "web_traffic": {
        "monthly_visitors": "integer",
        "monthly_visitor_mom_pct": "float",
        "monthly_visitor_qoq_pct": "float"
      },
      "glassdoor": {
        "glassdoor_overall_rating": "float",
        "glassdoor_ceo_approval_pct": "integer",
        "glassdoor_business_outlook_pct": "integer",
        "glassdoor_review_count": "integer"
      },
      "g2": {
        "g2_review_count": "integer",
        "g2_average_rating": "float"
      },
      "linkedin_followers": {
        "linkedin_followers": "integer",
        "linkedin_follower_count_timeseries": "array of objects"
      }
    }
  }
}

"""  # noqa


get_screening_api_info = """
    {
  "api_name": "Company Screening API",
  "overview": "Allows screening and filtering of companies based on growth and firmographic criteria.",
  "authorization": {
    "type": "authentication token",
    "required_key": "auth_token"
  },
  "endpoints": [
    {
      "url": "https://api.crustdata.com/screener/screen/",
      "method": "POST",
      "headers": {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "Token $auth_token",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://crustdata.com"
      },
      "body": {
        "metrics": [
          {
            "metric_name": "linkedin_headcount_and_glassdoor_ceo_approval_and_g2"
          }
        ],
        "filters": {
          "op": "and",
          "conditions": [
            {
              "column": "crunchbase_total_investment_usd",
              "type": "=>",
              "value": 5000000,
              "allow_null": false
            },
            {
              "column": "linkedin_headcount",
              "type": "=>",
              "value": 50,
              "allow_null": false
            },
            {
              "column": "largest_headcount_country",
              "type": "(.)",
              "value": "USA",
              "allow_null": false
            }
          ]
        },
        "hidden_columns": [],
        "offset": 0,
        "count": 100,
        "sorts": []
      }
    }
  ],
  "parameters": {
    "metrics": {
      "description": "Specifies columns in the response.",
      "required": true,
      "example": [
        {
          "metric_name": "linkedin_headcount_and_glassdoor_ceo_approval_and_g2"
        }
      ]
    },
    "filters": {
      "description": "Defines filter conditions.",
      "required": true,
      "example": {
        "op": "and",
        "conditions": [
          {
            "op": "or",
            "conditions": [
              {
                "hq_country": {
                  "type": "(.)",
                  "value": "USA"
                }
              },
              {
                "hq_country": {
                  "type": "(.)",
                  "value": "IND"
                }
              }
            ]
          },
          {
            "column": "crunchbase_total_investment_usd",
            "type": "=>",
            "value": 5000000
          },
          {
            "column": "largest_headcount_country",
            "type": "(.)",
            "value": "USA"
          }
        ]
      }
    },
    "offset": {
      "description": "Starting point of the result set.",
      "required": true,
      "default": 0
    },
    "count": {
      "description": "Number of results per request.",
      "required": true,
      "max_value": 100,
      "default": 100
    },
    "sorts": {
      "description": "Sorting criteria.",
      "required": false,
      "example": []
    }
  },
  "response": {
    "schema": {
      "fields": [
        {
          "type": "string",
          "api_name": "company_name",
          "hidden": false
        },
        {
          "type": "number",
          "api_name": "valuation_usd",
          "hidden": false
        },
        {
          "type": "number",
          "api_name": "crunchbase_total_investment_usd",
          "hidden": false
        }
      ],
      "rows": [
        [
          "Example Company",
          null,
          20000000
        ]
      ]
    },
    "fields_description": [
      "The ith value in a row corresponds to the ith field in the fields array."
    ]
  }
}

"""  # noqa


get_identification_api_info = """
    {
  "api_name": "Company Identification API",
  "description": "Identify companies in Crustdata's database using the company name, website, or LinkedIn profile URL.",
  "endpoint": "https://api.crustdata.com/screener/identify/",
  "method": "POST",
  "headers": {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "Token $api_token",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://crustdata.com"
  },
  "payload": {
    "query_fields": {
      "query_company_name": {
        "description": "Name of the company.",
        "required": false
      },
      "query_company_website": {
        "description": "Website URL of the company.",
        "required": false
      },
      "query_company_linkedin_url": {
        "description": "LinkedIn profile URL of the company.",
        "required": false
      },
      "count": {
        "description": "Maximum number of results to return. Default value is 10.",
        "required": false,
        "default": 10
      }
    },
    "example": {
      "query_company_website": "serverobotics.com",
      "count": 1
    }
  },
  "response": {
    "description": "An array of matched company records ranked by matching score.",
    "example": [
      {
        "company_id": 628895,
        "company_name": "Serve Robotics",
        "company_website_domain": "serverobotics.com",
        "company_website": "http://www.serverobotics.com",
        "linkedin_profile_url": "https://www.linkedin.com/company/serverobotics",
        "linkedin_headcount": 82,
        "acquisition_status": null,
        "score": 0.3
      }
    ],
    "fields": {
      "company_id": {
        "description": "Unique identifier for the company in Crustdata’s database."
      },
      "company_name": {
        "description": "Name of the company as recorded in Crustdata’s database."
      },
      "company_website_domain": {
        "description": "Website domain of the company, as specified on its LinkedIn page."
      },
      "company_website": {
        "description": "Website URL of the company."
      },
      "linkedin_profile_url": {
        "description": "LinkedIn profile URL of the company."
      },
      "linkedin_headcount": {
        "description": "Latest headcount of the company in Crustdata’s database."
      },
      "acquisition_status": {
        "description": "Acquisition status of the company, either 'acquired' or null."
      },
      "score": {
        "description": "Relative matching score based on the provided query parameters."
      }
    }
  },
  "notes": [
    "At least one of the query fields (name, website, LinkedIn URL) is required in the payload.",
    "Results are ranked by matching score, with the highest score appearing first.",
    "Providing all query fields increases the matching accuracy."
  ]
}
"""  # noqa


get_dataset_api_info = """ 
  {
  "job_listings": {
    "dataset": {
      "name": "job_listings",
      "id": "joblisting"
    },
    "filters": {
      "op": "and",
      "conditions": [
        {"column": "company_id", "type": "in", "value": [680992, 673947, 631280, 636304, 631811]},
        {"column": "date_updated", "type": ">", "value": "2024-02-01"}
      ]
    },
    "offset": 0,
    "limit": 100,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/job_listings/Table/ --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"and\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"in\",\"value\":[680992,673947,631280,636304,631811]},{\"column\":\"date_updated\",\"type\":\">\",\"value\":\"2024-02-01\"}]}\"}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"and\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"in\", \"value\": [680992, 673947, 631280, 636304, 631811]}, {\"column\": \"date_updated\", \"type\": \">\", \"value\": \"2024-02-01\"}]}, \"offset\": 0, \"limit\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/job_listings/Table/', headers=headers, json=json_data)"
    }
  },

  "funding_milestones": {
    "filters": {
      "op": "or",
      "conditions": [
        {"column": "company_id", "type": "in", "value": [637158, 674265, 674657]}
      ]
    },
    "offset": 0,
    "count": 1000,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/funding_milestone_timeseries/ --header 'Authorization: Token $auth_token' --data '{\"filters\":{\"op\":\"or\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"in\",\"value\":[637158,674265,674657]}]},\"offset\":0,\"count\":1000}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"or\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"in\", \"value\": [637158, 674265, 674657]}]}, \"offset\": 0, \"count\": 1000}\nresponse = requests.post('https://api.crustdata.com/data_lab/funding_milestone_timeseries/', headers=headers, json=json_data)"
    }
  },

  "decision_makers": {
    "filters": {
      "op": "and",
      "conditions": [
        {"column": "company_id", "type": "in", "value": [632328]}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header 'Authorization: Token $auth_token' --data '{\"filters\":{\"op\":\"and\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"in\",\"value\":[632328]}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"and\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"in\", \"value\": [632328]}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/decision_makers/', headers=headers, json=json_data)"
    }
  },

  "linkedin_employee_headcount": {
    "filters": {
      "op": "or",
      "conditions": [
        {"column": "company_id", "type": "=", "value": 634995},
        {"column": "company_id", "type": "=", "value": 680992},
        {"column": "company_id", "type": "=", "value": 673947},
        {"column": "company_id", "type": "=", "value": 631811}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/headcount_timeseries/ --header 'Authorization: Token $auth_token' --data '{\"filters\":{\"op\":\"or\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"=\",\"value\":634995},{\"column\":\"company_id\",\"type\":\"=\",\"value\":680992},{\"column\":\"company_id\",\"type\":\"=\",\"value\":673947},{\"column\":\"company_id\",\"type\":\"=\",\"value\":631811}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"or\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"=\", \"value\": 634995}, {\"column\": \"company_id\", \"type\": \"=\", \"value\": 680992}, {\"column\": \"company_id\", \"type\": \"=\", \"value\": 673947}, {\"column\": \"company_id\", \"type\": \"=\", \"value\": 631811}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/headcount_timeseries/', headers=headers, json=json_data)"
    }
  },

  "employee_headcount_by_function": {
    "filters": {
      "op": "and",
      "conditions": [
        {"column": "company_id", "type": "in", "value": [680992, 673947, 631280]}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/linkedin_headcount_by_facet/Table/ --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"and\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"in\",\"value\":[680992,673947,631280]}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"and\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"in\", \"value\": [680992, 673947, 631280]}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/linkedin_headcount_by_facet/Table/', headers=headers, json=json_data)"
    }
  },

  "glassdoor_profile_metrics": {
    "dataset": {
      "name": "glassdoor_profile_metric",
      "id": "glassdoorprofilemetric"
    },
    "filters": {
      "op": "and",
      "conditions": [
        {"column": "company_id", "type": "in", "value": [680992, 673947, 631280, 636304, 631811], "allow_null": false}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/ --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"and\",\"conditions\":[{\"column\":\"company_id\",\"type\":\"in\",\"value\":[680992,673947,631280,636304,631811],\"allow_null\":false}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"and\", \"conditions\": [{\"column\": \"company_id\", \"type\": \"in\", \"value\": [680992, 673947, 631280, 636304, 631811], \"allow_null\": false}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/', headers=headers, json=json_data)"
    }
  },

  "g2_profile_metrics": {
    "dataset": {
      "name": "g2_profile_metrics",
      "id": "g2profilemetric"
    },
    "filters": {
      "op": "or",
      "conditions": [
        {"column": "company_website_domain", "type": "=", "value": "microstrategy.com", "allow_null": false},
        {"column": "company_website_domain", "type": "=", "value": "lacework.com", "allow_null": false},
        {"column": "company_website_domain", "type": "=", "value": "jumpcloud.com", "allow_null": false}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url http://api.crustdata.com/data_lab/g2_profile_metrics/Table/ --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"or\",\"conditions\":[{\"column\":\"company_website_domain\",\"type\":\"=\",\"value\":\"microstrategy.com\",\"allow_null\":false},{\"column\":\"company_website_domain\",\"type\":\"=\",\"value\":\"lacework.com\",\"allow_null\":false},{\"column\":\"company_website_domain\",\"type\":\"=\",\"value\":\"jumpcloud.com\",\"allow_null\":false}]}},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"or\", \"conditions\": [{\"column\": \"company_website_domain\", \"type\": \"=\", \"value\": \"microstrategy.com\", \"allow_null\": false}, {\"column\": \"company_website_domain\", \"type\": \"=\", \"value\": \"lacework.com\", \"allow_null\": false}, {\"column\": \"company_website_domain\", \"type\": \"=\", \"value\": \"jumpcloud.com\", \"allow_null\": false}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('http://api.crustdata.com/data_lab/g2_profile_metrics/Table/', headers=headers, json=json_data)"
    }
  },

  "web_traffic": {
    "filters": {
      "op": "or",
      "conditions": [
        {"column": "company_website", "type": "(.)", "value": "wefitanyfurniture.com"}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url 'https://api.crustdata.com/data_lab/webtraffic/' --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"or\",\"conditions\":[{\"column\":\"company_website\",\"type\":\"(.)\",\"value\":\"wefitanyfurniture.com\"}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"or\", \"conditions\": [{\"column\": \"company_website\", \"type\": \"(.)\", \"value\": \"wefitanyfurniture.com\"}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/webtraffic/', headers=headers, json=json_data)"
    }
  },

  "investor_portfolio": {
    "filters": {
      "op": "or",
      "conditions": [
        {"column": "investor_uuid", "type": "=", "value": "ce91bad7-b6d8-e56e-0f45-4763c6c5ca29"},
        {"column": "investor_name", "type": "=", "value": "Sequoia Capital"}
      ]
    },
    "offset": 0,
    "count": 100,
    "example": {
      "curl": "curl --request POST --url 'https://api.crustdata.com/data_lab/investor_portfolio/' --header 'Authorization: Token $token' --data '{\"filters\":{\"op\":\"or\",\"conditions\":[{\"column\":\"investor_uuid\",\"type\":\"=\",\"value\":\"ce91bad7-b6d8-e56e-0f45-4763c6c5ca29\"},{\"column\":\"investor_name\",\"type\":\"=\",\"value\":\"Sequoia Capital\"}]},\"offset\":0,\"count\":100}'",
      "python": "import requests\nheaders = {'Authorization': 'Token $auth_token'}\njson_data = {\"filters\": {\"op\": \"or\", \"conditions\": [{\"column\": \"investor_uuid\", \"type\": \"=\", \"value\": \"ce91bad7-b6d8-e56e-0f45-4763c6c5ca29\"}, {\"column\": \"investor_name\", \"type\": \"=\", \"value\": \"Sequoia Capital\"}]}, \"offset\": 0, \"count\": 100}\nresponse = requests.post('https://api.crustdata.com/data_lab/investor_portfolio/', headers=headers, json=json_data)"
    }
  }
}

"""  # noqa


get_linkedin_company_search_api = """ 
  {
  "endpoint": "POST /screener/company/search",
  "description": "Search for company profiles using either directly a LinkedIn Sales Navigator account's search URL or custom search criteria as a filter. Returns detailed information about companies matching specific criteria.",
  "authentication": {
    "auth_token": "string",
    "required": true
  },
  "request": {
    "description": "Search request can either use a Sales Navigator search URL or custom filter criteria.",
    "body": {
      "linkedin_sales_navigator_search_url": {
        "description": "URL of the Sales Navigator Accounts search from your browser",
        "type": "string",
        "example": "https://www.linkedin.com/sales/search/company?query=(filters%3AList((type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A103323778%2Ctext%3AMexico%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A25%2Ctext%3AManufacturing%2CselectionType%3AINCLUDED)))))&sessionId=8TR8HMz%2BTVOYaeivK9p%2Bpg%3D%3D&viewAllFilters=true"
      },
      "filters": {
        "description": "Search criteria as a JSON object defining the filters to apply for the search",
        "type": "array",
        "items": {
          "filter_type": {
            "description": "The filter type",
            "type": "string",
            "example": "COMPANY_HEADCOUNT"
          },
          "type": {
            "description": "Filter type: 'in' for inclusion, 'not in' for exclusion",
            "type": "string",
            "example": "in"
          },
          "value": {
            "description": "Value or list of values to apply in the filter",
            "type": "array",
            "example": ["10,001+", "1,001-5,000"]
          },
          "sub_filter": {
            "description": "Optional sub-filter for additional context (if applicable)",
            "type": "string",
            "example": "USD"
          }
        },
        "example": [
          {
            "filter_type": "COMPANY_HEADCOUNT",
            "type": "in",
            "value": ["10,001+", "1,001-5,000"]
          },
          {
            "filter_type": "ANNUAL_REVENUE",
            "type": "between",
            "value": {"min": 1, "max": 500},
            "sub_filter": "USD"
          },
          {
            "filter_type": "REGION",
            "type": "not in",
            "value": ["United States"]
          }
        ]
      },
      "page": {
        "description": "Page number for pagination",
        "type": "integer",
        "example": 2
      }
    },
    "example_request": {
      "linkedin_sales_navigator_search_url": "https://www.linkedin.com/sales/search/company?query=(filters%3AList((type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A103323778%2Ctext%3AMexico%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A25%2Ctext%3AManufacturing%2CselectionType%3AINCLUDED)))))&sessionId=8TR8HMz%2BTVOYaeivK9p%2Bpg%3D%3D&viewAllFilters=true"
    }
  },
  "response": {
    "description": "The API will return the search results in real-time from LinkedIn, with pagination options if necessary.",
    "schema": {
      "total_display_count": {
        "description": "Total number of results matching the criteria",
        "type": "integer",
        "example": 100
      },
      "results": {
        "description": "List of company profiles matching the search criteria",
        "type": "array",
        "items": {
          "company_name": {
            "type": "string",
            "example": "Acme Corp"
          },
          "company_id": {
            "type": "string",
            "example": "acme-corp-id"
          },
          "headcount": {
            "type": "string",
            "example": "10,001+"
          },
          "revenue": {
            "type": "string",
            "example": "$300 million USD"
          }
        }
      }
    },
    "example_response": {
      "total_display_count": 100,
      "results": [
        {
          "company_name": "Acme Corp",
          "company_id": "acme-corp-id",
          "headcount": "10,001+",
          "revenue": "$300 million USD"
        },
        {
          "company_name": "Beta Ltd.",
          "company_id": "beta-ltd-id",
          "headcount": "1,001-5,000",
          "revenue": "$150 million USD"
        }
      ]
    }
  },
  "pagination": {
    "description": "Each request returns up to 25 results. To paginate, provide the 'page' parameter in subsequent requests.",
    "example": {
      "page": 2
    }
  },
  "credits": {
    "description": "Each page request costs 25 credits."
  },
  "latency": {
    "description": "The latency for this endpoint is between 10 to 30 seconds."
  }
}

"""  # noqa


get_linkedin_posts_company_api = """ 
{
  "request": {
    "description": "Fetch recent LinkedIn posts and engagement metrics for a specified company.",
    "parameters": {
      "company_name": "string (optional)",
      "company_domain": "string (optional)",
      "company_id": "string (optional)",
      "company_linkedin_url": "string (optional)",
      "fields": "string (optional, default: all fields)",
      "page": "integer (optional, default: 1)",
      "limit": "integer (optional, default: 5)",
      "post_types": "string (optional, default: repost, original)"
    },
    "example_requests": [
      {
        "curl": "curl 'https://api.crustdata.com/screener/linkedin_posts?company_domain=https://crustdata.com&page=1' --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token'"
      },
      {
        "curl": "curl 'https://api.crustdata.com/screener/linkedin_posts?company_domain=https://crustdata.com&page=1&fields=reactors' --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token'"
      },
      {
        "curl": "curl 'https://api.crustdata.com/screener/linkedin_posts?company_domain=https://crustdata.com&page=1&post_types=repost%2C%20original' --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token'"
      }
    ]
  },
  "response": {
    "description": "Returns a list of recent LinkedIn posts with engagement metrics and details about reactors.",
    "structure": {
      "posts": [
        {
          "backend_urn": "urn:li:activity:7236812027275419648",
          "share_urn": "urn:li:share:7236812026038083584",
          "share_url": "https://www.linkedin.com/posts/crustdata_y-combinators-most-popular-startups-from-activity-7236812027275419648-4fyw?utm_source=combined_share_message&utm_medium=member_desktop",
          "text": "Y Combinator’s most popular startups. From the current S24 batch. How do you gauge the buzz around these startups when most are pre-product? We’ve defined web traffic as the metric to go by. Here are the most popular startups from YC S24...",
          "actor_name": "Crustdata",
          "date_posted": "2024-09-03",
          "hyperlinks": {
            "company_linkedin_urls": [],
            "person_linkedin_urls": [
              "https://www.linkedin.com/in/ACoAAAKoldoBqSsiXY_DHsXdSk1slibabeTvDDY"
            ],
            "other_urls": []
          },
          "total_reactions": 37,
          "total_comments": 7,
          "reactions_by_type": {
            "LIKE": 28,
            "EMPATHY": 4,
            "PRAISE": 4,
            "INTEREST": 1
          },
          "num_shares": 5,
          "reactors": [
            {
              "name": "Courtney May",
              "linkedin_profile_url": "https://www.linkedin.com/in/ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
              "reaction_type": "LIKE",
              "profile_image_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL_c5H9Zg/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1690558480623?e=1730937600&v=beta&t=Lm2hHLTFiEVlHWdTt-Vh3vDYevK8U8SlPqaFdNu3R6A",
              "title": "GTM @ Arc (YC W22)",
              "location": "San Francisco, California, United States",
              "linkedin_profile_urn": "ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
              "num_of_connections": 786,
              "current_title": "GTM @ Arc (YC W22)"
            }
          ]
        }
      ]
    },
    "example_response": {
      "posts": [
        {
          "backend_urn": "urn:li:activity:7236812027275419648",
          "share_urn": "urn:li:share:7236812026038083584",
          "share_url": "https://www.linkedin.com/posts/crustdata_y-combinators-most-popular-startups-from-activity-7236812027275419648-4fyw?utm_source=combined_share_message&utm_medium=member_desktop",
          "text": "Y Combinator’s most popular startups. From the current S24 batch. How do you gauge the buzz around these startups when most are pre-product? We’ve defined web traffic as the metric to go by. Here are the most popular startups from YC S24...",
          "actor_name": "Crustdata",
          "date_posted": "2024-09-03",
          "hyperlinks": {
            "company_linkedin_urls": [],
            "person_linkedin_urls": [
              "https://www.linkedin.com/in/ACoAAAKoldoBqSsiXY_DHsXdSk1slibabeTvDDY"
            ],
            "other_urls": []
          },
          "total_reactions": 37,
          "total_comments": 7,
          "reactions_by_type": {
            "LIKE": 28,
            "EMPATHY": 4,
            "PRAISE": 4,
            "INTEREST": 1
          },
          "num_shares": 5,
          "reactors": [
            {
              "name": "Courtney May",
              "linkedin_profile_url": "https://www.linkedin.com/in/ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
              "reaction_type": "LIKE",
              "profile_image_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL_c5H9Zg/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1690558480623?e=1730937600&v=beta&t=Lm2hHLTFiEVlHWdTt-Vh3vDYevK8U8SlPqaFdNu3R6A",
              "title": "GTM @ Arc (YC W22)",
              "location": "San Francisco, California, United States",
              "linkedin_profile_urn": "ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
              "num_of_connections": 786,
              "current_title": "GTM @ Arc (YC W22)"
            }
          ]
        }
      ]
    }
  },
  "pagination": {
    "page": "integer",
    "limit": "integer",
    "max_pages": 20
  },
  "credits": {
    "default": 5,
    "with_reactors": 25
  },
  "latency": "30-60 seconds"
}

"""  # noqa


get_linkedin_posts_keyword_api = """
{
  "endpoint": "/screener/linkedin_posts/keyword_search/",
  "method": "POST",
  "description": "Retrieve LinkedIn posts containing specified keywords along with engagement metrics.",
  "request": {
    "headers": {
      "Authorization": "Token $auth_token",
      "Accept": "application/json, text/plain, */*",
      "Content-Type": "application/json"
    },
    "body": {
      "keyword": {
        "type": "string",
        "description": "The keyword or phrase to search for in LinkedIn posts.",
        "required": true
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1,
        "required": true
      },
      "limit": {
        "type": "integer",
        "description": "Limit the number of posts in a page.",
        "default": 5,
        "required": false
      },
      "sort_by": {
        "type": "string",
        "description": "Defines the sorting order of results (e.g., 'relevance', 'date_posted').",
        "default": "date_posted",
        "required": false,
        "enum": ["relevance", "date_posted"]
      },
      "date_posted": {
        "type": "string",
        "description": "Filters posts by the date they were posted.",
        "default": "past-24h",
        "required": false,
        "enum": [
          "past-24h", "past-week", "past-month", "past-quarter", "past-year"
        ]
      }
    }
  },
  "response": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the request was successful.",
      "example": true
    },
    "posts": {
      "type": "array",
      "description": "A list of LinkedIn posts matching the search criteria.",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the post."
          },
          "content": {
            "type": "string",
            "description": "The content of the post."
          },
          "engagement_metrics": {
            "type": "object",
            "properties": {
              "likes": {
                "type": "integer",
                "description": "Number of likes the post received."
              },
              "comments": {
                "type": "integer",
                "description": "Number of comments on the post."
              },
              "shares": {
                "type": "integer",
                "description": "Number of shares of the post."
              }
            }
          },
          "actor_type": {
            "type": "string",
            "description": "Type of actor who posted (e.g., 'person', 'company').",
            "enum": ["person", "company"]
          },
          "actor_name": {
            "type": "string",
            "description": "The name of the actor (person or company) who made the post."
          },
          "posted_at": {
            "type": "string",
            "description": "The timestamp of when the post was made."
          }
        }
      }
    },
    "pagination": {
      "type": "object",
      "properties": {
        "current_page": {
          "type": "integer",
          "description": "Current page number."
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages."
        },
        "next_page": {
          "type": "integer",
          "description": "The next page number if available."
        }
      }
    }
  },
  "example": {
    "request": {
      "keyword": "LLM Evaluation",
      "page": 1,
      "sort_by": "relevance",
      "date_posted": "past-quarter"
    },
    "response": {
      "success": true,
      "posts": [
        {
          "id": "1",
          "content": "Exploring the latest LLM evaluation methods for AI development.",
          "engagement_metrics": {
            "likes": 100,
            "comments": 25,
            "shares": 10
          },
          "actor_type": "person",
          "actor_name": "John Doe",
          "posted_at": "2024-10-15"
        },
        {
          "id": "2",
          "content": "LLM evaluation in the tech industry: a deep dive.",
          "engagement_metrics": {
            "likes": 150,
            "comments": 50,
            "shares": 20
          },
          "actor_type": "company",
          "actor_name": "Tech Innovations Inc.",
          "posted_at": "2024-11-01"
        }
      ],
      "pagination": {
        "current_page": 1,
        "total_pages": 5,
        "next_page": 2
      }
    }
  }
}

"""  # noqa
