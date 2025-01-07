get_people_profile_api = """
{
  "endpoint": "/screener/person/enrich",
  "method": "GET",
  "description": "Enrich data for one or more individuals using LinkedIn profile URLs or business email addresses.",
  "request": {
    "query_parameters": {
      "linkedin_profile_url": {
        "type": "string",
        "description": "Comma-separated list of LinkedIn profile URLs. Optional.",
        "required": false
      },
      "business_email": {
        "type": "string",
        "description": "Business email address. Optional. Only one email can be provided per request.",
        "required": false
      },
      "enrich_realtime": {
        "type": "boolean",
        "description": "If True, performs a real-time search from the web if data is not found in the database.",
        "default": false,
        "required": false
      },
      "fields": {
        "type": "string",
        "description": "Comma-separated list of fields to include in the response.",
        "required": false
      }
    }
  },
  "response": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the enrichment request was successful.",
      "example": true
    },
    "profiles": {
      "type": "array",
      "description": "List of enriched profiles.",
      "items": {
        "type": "object",
        "properties": {
          "linkedin_profile_url": {
            "type": "string",
            "description": "The URL of the LinkedIn profile."
          },
          "linkedin_flagship_url": {
            "type": "string",
            "description": "The flagship LinkedIn URL for the profile."
          },
          "name": {
            "type": "string",
            "description": "Full name of the person."
          },
          "location": {
            "type": "string",
            "description": "Location of the individual."
          },
          "email": {
            "type": "string",
            "description": "Email address of the individual."
          },
          "title": {
            "type": "string",
            "description": "Current job title of the individual."
          },
          "last_updated": {
            "type": "string",
            "description": "Timestamp when the profile was last updated."
          },
          "headline": {
            "type": "string",
            "description": "Headline of the individual’s LinkedIn profile."
          },
          "summary": {
            "type": "string",
            "description": "Summary or bio from the LinkedIn profile."
          },
          "num_of_connections": {
            "type": "string",
            "description": "Number of LinkedIn connections."
          },
          "skills": {
            "type": "array",
            "description": "List of skills from the LinkedIn profile.",
            "items": {
              "type": "string"
            }
          },
          "profile_picture_url": {
            "type": "string",
            "description": "URL to the profile picture."
          },
          "twitter_handle": {
            "type": "string",
            "description": "Twitter handle if available."
          },
          "languages": {
            "type": "array",
            "description": "List of languages spoken.",
            "items": {
              "type": "string"
            }
          },
          "linkedin_open_to_cards": {
            "type": "array",
            "description": "Information regarding whether the person is open to job opportunities.",
            "items": {
              "type": "string"
            }
          },
          "all_employers": {
            "type": "array",
            "description": "List of all past and current employers.",
            "items": {
              "type": "object",
              "properties": {
                "company_name": {
                  "type": "string",
                  "description": "Employer’s name."
                },
                "job_title": {
                  "type": "string",
                  "description": "Job title at this employer."
                },
                "start_date": {
                  "type": "string",
                  "description": "Start date of employment."
                },
                "end_date": {
                  "type": "string",
                  "description": "End date of employment."
                }
              }
            }
          },
          "education_background": {
            "type": "array",
            "description": "Educational background.",
            "items": {
              "type": "object",
              "properties": {
                "degree_name": {
                  "type": "string",
                  "description": "Degree obtained."
                },
                "field_of_study": {
                  "type": "string",
                  "description": "Field of study."
                },
                "institute_name": {
                  "type": "string",
                  "description": "Name of the educational institution."
                },
                "start_date": {
                  "type": "string",
                  "description": "Start date of education."
                },
                "end_date": {
                  "type": "string",
                  "description": "End date of education."
                }
              }
            }
          }
        }
      }
    },
    "errors": {
      "type": "array",
      "description": "List of errors encountered during the enrichment process.",
      "items": {
        "type": "object",
        "properties": {
          "profile": {
            "type": "string",
            "description": "The LinkedIn profile URL or email that caused the error."
          },
          "error_message": {
            "type": "string",
            "description": "Description of the error."
          }
        }
      }
    },
    "pagination": {
      "type": "object",
      "description": "Pagination details for large result sets.",
      "properties": {
        "current_page": {
          "type": "integer",
          "description": "Current page number."
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages."
        }
      }
    }
  },
  "example": {
    "request": {
      "linkedin_profile_url": "https://www.linkedin.com/in/johndoe/,https://www.linkedin.com/in/janedoe/",
      "enrich_realtime": true,
      "fields": "name,location,email,title,skills,all_employers,education_background"
    },
    "response": {
      "success": true,
      "profiles": [
        {
          "linkedin_profile_url": "https://www.linkedin.com/in/johndoe/",
          "linkedin_flagship_url": "https://www.linkedin.com/in/johndoe",
          "name": "John Doe",
          "location": "San Francisco, CA",
          "email": "johndoe@example.com",
          "title": "Software Engineer at XYZ Corp",
          "last_updated": "2024-01-01",
          "headline": "Experienced software engineer with a passion for coding.",
          "summary": "John has been working in the software industry for 5 years, specializing in web development.",
          "num_of_connections": "500+",
          "skills": ["JavaScript", "React", "Node.js"],
          "profile_picture_url": "https://example.com/profile.jpg",
          "twitter_handle": "@johndoe",
          "languages": ["English", "Spanish"],
          "linkedin_open_to_cards": ["Job opportunities", "Networking"],
          "all_employers": [
            {
              "company_name": "XYZ Corp",
              "job_title": "Software Engineer",
              "start_date": "2020-01-01",
              "end_date": "Present"
            }
          ],
          "education_background": [
            {
              "degree_name": "BSc in Computer Science",
              "field_of_study": "Computer Science",
              "institute_name": "University of California",
              "start_date": "2015-08-01",
              "end_date": "2019-05-01"
            }
          ]
        }
      ],
      "errors": [],
      "pagination": {
        "current_page": 1,
        "total_pages": 1
      }
    }
  }
}

"""  # noqa

get_people_search_api = """
{
  "description": "Search for people profiles based on either a direct LinkedIn Sales Navigator search URL or custom search criteria.",
  "endpoint": "https://api.crustdata.com/screener/person/search",
  "authentication": {
    "auth_token": "required"
  },
  "request_body": {
    "linkedin_sales_navigator_search_url": "string (optional)",
    "filters": {
      "filter_type": "string",
      "type": "string",
      "value": ["string"] 
    },
    "page": "integer (optional)",
    "preview": "boolean (optional)"
  },
  "examples": [
    {
      "example_description": "Via LinkedIn Sales Navigator URL",
      "example_request": {
        "method": "POST",
        "url": "https://api.crustdata.com/screener/person/search",
        "headers": {
          "Content-Type": "application/json",
          "Accept": "application/json, text/plain, */*",
          "Accept-Language": "en-US,en;q=0.9",
          "Authorization": "Token $auth_token"
        },
        "body": {
          "linkedin_sales_navigator_search_url": "https://www.linkedin.com/sales/search/people?query=(recentSearchParam%3A(id%3A3940840412%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)%2C(id%3AB%2Ctext%3A1-10%2CselectionType%3AINCLUDED)%2C(id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)%2C(id%3AE%2Ctext%3A201-500%2CselectionType%3AINCLUDED)%2C(id%3AF%2Ctext%3A501-1000%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A41%2Ctext%3ABanking%2CselectionType%3AINCLUDED)%2C(id%3A43%2Ctext%3AFinancial%20Services%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY_HEADQUARTERS%2Cvalues%3AList((id%3A105912732%2Ctext%3ABelize%2CselectionType%3AINCLUDED)%2C(id%3A101739942%2Ctext%3ACosta%20Rica%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A110%2Ctext%3AEntry%20Level%2CselectionType%3AEXCLUDED)%2C(id%3A100%2Ctext%3AIn%20Training%2CselectionType%3AEXCLUDED)))"
        }
      }
    },
    {
      "example_description": "Via Custom Search Filters",
      "example_request": {
        "method": "POST",
        "url": "https://api.crustdata.com/screener/person/search",
        "headers": {
          "Content-Type": "application/json",
          "Accept": "application/json, text/plain, */*",
          "Authorization": "Token $auth_token"
        },
        "body": {
          "filters": [
            {
              "filter_type": "CURRENT_COMPANY",
              "type": "in",
              "value": ["Google", "Microsoft"]
            },
            {
              "filter_type": "CURRENT_TITLE",
              "type": "not in",
              "value": ["Software Engineer", "Data Scientist"]
            },
            {
              "filter_type": "COMPANY_HEADQUARTERS",
              "type": "in",
              "value": ["United States", "Canada"]
            },
            {
              "filter_type": "INDUSTRY",
              "type": "in",
              "value": ["Software Development", "Hospitals and Health Care"]
            },
            {
              "filter_type": "REGION",
              "type": "not in",
              "value": ["California, United States", "New York, United States"]
            }
          ],
          "page": 1
        }
      }
    }
  ],
  "response_schema": {
    "total_display_count": "integer",
    "results": [
      {
        "profile": {
          "name": "string",
          "current_company": "string",
          "current_title": "string",
          "location": "string",
          "linkedin_url": "string"
        }
      }
    ],
    "pagination": {
      "page": "integer",
      "page_size": "integer"
    }
  },
  "pagination_details": {
    "max_results_per_page": 25,
    "credits_per_page": 25,
    "preview_credits_per_page": 5
  },
  "note": "Each page returns up to 25 results. If more results are needed, pagination can be used by updating the page parameter."
}

"""  # noqa


get_linkedin_posts_by_person_api = """
    {
  "request": {
    "person_linkedin_url": "https://linkedin.com/in/abhilash-chowdhary",
    "fields": "total_reactions,total_comments,text,share_urn,share_url,reactions_by_type_PRAISE,reactions_by_type_LIKE,reactions_by_type_INTEREST,reactions_by_type_ENTERTAINMENT,reactions_by_type_EMPATHY,reactions_by_type_CURIOUS,reactions_by_type_APPRECIATION,reactions_by_type,num_shares,hyperlinks_person_linkedin_urls,hyperlinks_other_urls,hyperlinks_company_linkedin_urls,hyperlinks,date_posted,backend_urn,actor_name,year_founded",
    "page": 1,
    "limit": 5,
    "post_types": "repost,original"
  },
  "response": {
    "posts": [
      {
        "backend_urn": "urn:li:activity:7236812027275419648",
        "share_urn": "urn:li:share:7236812026038083584",
        "share_url": "https://www.linkedin.com/posts/crustdata_y-combinators-most-popular-startups-from-activity-7236812027275419648-4fyw?utm_source=combined_share_message&utm_medium=member_desktop",
        "text": "Y Combinator’s most popular startups.\nFrom the current S24 batch.\n\nHow do you gauge the buzz around these startups when most are pre-product?\n\nWe’ve defined web traffic as the metric to go by.\n\nHere are the most popular startups from YC S24:  \n\n1. NexUI: Founded by Junior Garcia\n2. Wordware: Filip Kozera, Robert Chandler\n3. Unriddle: Naveed Janmohamed\n4. Undermind: Thomas Hartke, Joshua Ramette\n5. Comfydploy: Nick Kao, Benny Kok\n6. Beebettor: Jordan Murphy, Matthew Wolfe\n7. Merse: Kumar A., Mark Rachapoom\n8. Laminar: Robert Kim, Din Mailibay, Temirlan Myrzakhmetov\n9. MitoHealth: Kenneth Lou, Tee-Ming C., Joel Kek, Ryan Ware\n10. Autarc: Etienne-Noel Krause,Thies Hansen, Marius Seufzer\n\nInterested in reading more about the YC S24 batch?\nRead our full breakdown from the link in the comments 👇",
        "actor_name": "Crustdata",
        "hyperlinks": {
          "company_linkedin_urls": [],
          "person_linkedin_urls": [
            "https://www.linkedin.com/in/ACoAAAKoldoBqSsiXY_DHsXdSk1slibabeTvDDY"
          ],
          "other_urls": []
        },
        "date_posted": "2024-09-03",
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
            "additional_info": "3rd+",
            "location": "San Francisco, California, United States",
            "linkedin_profile_urn": "ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
            "default_position_title": "GTM @ Arc (YC W22)",
            "default_position_company_linkedin_id": "74725230",
            "default_position_is_decision_maker": false,
            "flagship_profile_url": "https://www.linkedin.com/in/courtney-may-8a178b172",
            "profile_picture_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL_c5H9Zg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1690558480623?e=1730937600&v=beta&t=vHg233746zA00m3q2vHKSFcthL3YKiagTtVEZt1qqJI",
            "headline": "GTM @ Arc (YC W22)",
            "summary": null,
            "num_of_connections": 786,
            "related_colleague_company_id": 74725230,
            "skills": [
              "Marketing Strategy",
              "Product Support",
              "SOC 2"
            ],
            "employer": [
              {
                "title": "GTM @ Arc (YC W22)",
                "company_name": "Arc",
                "company_linkedin_id": "74725230",
                "start_date": "2024-07-01T00:00:00",
                "end_date": null,
                "description": null,
                "location": "San Francisco, California, United States",
                "rich_media": []
              },
              {
                "title": "Product Marketing & Operations Lead",
                "company_name": "Bits of Stock™",
                "company_linkedin_id": "10550545",
                "start_date": "2023-03-01T00:00:00",
                "end_date": "2024-07-01T00:00:00",
                "description": "● Spearheaded SOC 2 Certification and oversaw compliance organization for internal and external needs.\n● Leads a weekly operations call to manage customer support, new user onboarding, and other outstanding operational matters.\n● Wrote & launched: Product Blog with 6 different featured pieces; 2 Pricing Thought-Leadership pieces; & 2 Partner Press Releases; two of which were featured in the WSJ.\n● Managed marketing and logistics for 11 conferences and events all over the world, producing over 150 B2B qualified leads.\n● Created a company-wide marketing strategy and implemented it across the blog, LinkedIn, & Twitter leading to a 125% increased engagement rate & a 29% increase in followers.\n● Aided in sales and partner relations by preparing a Partner Marketing Guide, creating the user support section of the website and inbound email system, and investing education guide.",
                "location": "San Francisco Bay Area",
                "rich_media": []
              }
            ],
            "education_background": [
              {
                "degree_name": "Bachelor of Applied Science - BASc",
                "institute_name": "Texas Christian University",
                "field_of_study": "Economics",
                "start_date": "2016-01-01T00:00:00",
                "end_date": "2020-01-01T00:00:00"
              }
            ],
            "emails": [
              "email@example.com"
            ],
            "websites": [],
            "twitter_handle": null,
            "languages": [],
            "pronoun": null,
            "current_title": "GTM @ Arc (YC W22)"
          }
        ]
      }
    ]
  }
}

"""  # noqa


get_remaining_credits_api = """ 
{
  "request": {
    "method": "GET",
    "url": "https://api.crustdata.com/user/credits",
    "headers": {
      "Accept": "application/json, text/plain, */*",
      "Accept-Language": "en-US,en;q=0.9",
      "Authorization": "Token $auth_token",
      "Content-Type": "application/json"
    }
  },
  "response": {
    "credits": 1000000
  }
}

"""  # noqa
