import os
import requests
import json
from semantic_kernel.functions.kernel_function_decorator import kernel_function

class KernelMemoryRag:
    @kernel_function(
        description="This function is used to ask questions about Adam",
        name="ask_adam",
    )
    def get_response(self, usermessage: str) -> str:
        print("User message:", usermessage)
        question = {"question": usermessage}
        print("Question:", question)

        try:
                # Use 'kernel_memory' as the hostname
                response = requests.post("http://kernel_memory:9001/ask", json=question)
                print("Response status code:", response.status_code)
                print("Response text:", response.text)

                response.raise_for_status()

                response_json = response.json()
                print("Response JSON:", response_json)

                if "text" in response_json:
                        return response_json["text"]
                else:
                        return "No 'text' field in the response."

        except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
                return "An HTTP error occurred."
        except requests.exceptions.RequestException as req_err:
                print(f"Request exception occurred: {req_err}")
                return "A request error occurred."
        except Exception as err:
                print(f"An error occurred: {err}")
                return "An unexpected error occurred."


if __name__ == "__main__":
        KernelMemoryRag().get_response("What is your name?")