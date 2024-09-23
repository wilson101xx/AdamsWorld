import asyncio
import os
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.utils.author_role import AuthorRole
from semantic_kernel.contents import ChatHistory
from semantic_kernel.kernel import Kernel

from dotenv import load_dotenv

load_dotenv()

HOST_NAME = "AdamWilson"
HOST_INSTRUCTIONS = """You are Adam Wilson, you answer questions about yourself. To find information, you use the ask_adam function. 
If you do not know an answer, respond with 'Sorry, this information is not available. Maybe ask about my past career or experience.'
Keep the conversation interesting and brief."""

class AgentWrapper:
    def __init__(self):
        self.streaming = True
        self.service_id = "agent"
        self.chat = ChatHistory()

        # Create kernel
        self.kernel = self.create_kernel(self.service_id)
        # Create settings
        self.settings = self.create_settings(self.kernel, self.service_id)
        # Add plugins
        self.kernel = self.plugins(self.kernel)
        # Create agent
        self.agent = ChatCompletionAgent(
            service_id=self.service_id,
            kernel=self.kernel,
            name=HOST_NAME,
            instructions=HOST_INSTRUCTIONS,
            execution_settings=self.settings
        )

    def create_kernel(self, service_id):
        deployment = os.getenv("azure_openai_4o")
        api_key = os.getenv("azure_openai_key")
        endpoint = os.getenv("azure_openai")

        print(f"deployment: {deployment}")

        chat_service = AzureChatCompletion(
            service_id=service_id,
            api_key=api_key,
            endpoint=endpoint,
            deployment_name=deployment
        )

        kernel = Kernel()
        kernel.add_service(chat_service)
        return kernel

    def create_settings(self, kernel: Kernel, service_id: str):
        settings = kernel.get_prompt_execution_settings_from_service_id(service_id=service_id)
        settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
        return settings

    def plugins(self, kernel: Kernel):
        script_directory = os.path.dirname(__file__)
        plugins_directory = os.path.join(script_directory, "plugins")
        kernel.add_plugin(parent_directory=plugins_directory, plugin_name="kernel_memory_rag")
        return kernel

    async def invoke_agent(self, user_message: str):
        self.chat.add_user_message(user_message)
        print(f"# {AuthorRole.USER}: '{user_message}'")
        if "Adam" in user_message:
            pass
        else:
            user_message = f"This question is about Adam {user_message}"

        if self.streaming:
            contents = []
            content_name = ""
            async for content in self.agent.invoke_stream(self.chat):
                content_name = content.name
                contents.append(content)
            message_content = "".join([content.content for content in contents])
            self.chat.add_assistant_message(message_content)
            return message_content

    async def ask(self, user_message):
        answer = await self.invoke_agent(user_message)
        return answer

