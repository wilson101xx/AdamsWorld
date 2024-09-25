import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import json
from semantic_kernel.functions.kernel_function_decorator import kernel_function

load_dotenv()




class KernelMemoryRag:
    @kernel_function(
        description="This function is used to ask questions about Adam",
        name="ask_adam_rag",
    )
    def chatbot_feature(self, message: str) -> str:

        endpoint = os.getenv("azure_openai")
        endpoint_key = os.getenv("azure_openai_key")
        deployment = os.getenv("azure_openai_4o")
        search_endpoint = os.getenv("azure_ai_search")
        search_key = os.getenv("azure_ai_search_key")

        client = AzureOpenAI(
            azure_endpoint = endpoint,
            api_key = endpoint_key,
            api_version = "2024-05-01-preview",
        )

        completion = client.chat.completions.create(
            model=deployment,
            messages= [
            {
                "role": "system",
                "content": """You should respond too the following question asked by the user friendly and in a professional manner, you should not make your answers too long, if the message says you it means Adam Wilson"""
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



if __name__ == "__main__":
    KernelMemoryRag.chatbot_feature("What is adams expeirence in ai")