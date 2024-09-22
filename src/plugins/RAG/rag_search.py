import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import json

load_dotenv()

def create_client() -> AzureOpenAI:
    endpoint = os.getenv("azure_openai")
    endpoint_key = os.getenv("azure_openai_key")


    client = AzureOpenAI(
        azure_endpoint = endpoint,
        api_key = endpoint_key,
        api_version = "2024-05-01-preview",
    )

    return client

def chatbot_feature(message, client):
    deployment = os.getenv("azure_openai_4o")
    search_endpoint = os.getenv("azure_ai_search")
    search_key = os.getenv("azure_ai_search_key")

    completion = client.chat.completions.create(
        model=deployment,
        messages= [
        {
            "role": "system",
            "content": """You are Adam Wilson, an experienced AI and Data Technical Lead. 
                            Respond in a happy and clear tone, while being direct. You should express the knowledge and insights that Adam has based on his expertise, 
                            background, and experiences. 
                            Engage with the user as Adam would, showing confidence in AI solutions, DevOps, and automation while maintaining a professional and friendly demeanor."""
        },
        {
            "role": "user",
            "content": message
        }
    ],
        max_tokens=800,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    ,
        extra_body={
        "data_sources": [{
            "type": "azure_search",
            "parameters": {
                "endpoint": f"{search_endpoint}",
                "index_name": "document_test-index-vector",
                "semantic_configuration": "my-semantic-config",
                "query_type": "vector_semantic_hybrid",
                "fields_mapping": {
                "content_fields_separator": "\n",
                "content_fields": [
                    "content"
                ],
                "filepath_field": None,
                "title_field": None,
                "url_field": None,
                "vector_fields": [
                    "Content_vector"
                ]
                },
                "in_scope": True,
                "role_information": "You are an AI assistant that helps people find information.",
                "filter": None,
                "strictness": 3,
                "top_n_documents": 5,
                "authentication": {
                "type": "api_key",
                "key": f"{search_key}"
                },
                "embedding_dependency": {
                "type": "deployment_name",
                "deployment_name": "text-embedding-ada-002"
                }
            }
            }]
        })

    answer = completion.choices[0].message.content
    # print(type(answer))
    return answer
