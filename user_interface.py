import gradio as gr
from src.basic_agent import AgentWrapper
import asyncio

agent_wrapper = AgentWrapper()

# Define a simple chatbot function that responds to user input
async def chatbot(user_input, history):
    history = history or []
    message = await agent_wrapper.ask(user_input)
    history.append(("User", user_input))
    history.append(("Bot", message))
    return history, history

def display_cv():
    return """
    <style>
        h1, h2, h3, p {
            font-size: 18px;
        }
        .multi-column {
            column-count: 2;
            -webkit-column-count: 2; /* Safari and Chrome */
            -moz-column-count: 2; /* Firefox */
        }
    </style>

    <h1>Adam Wilson</h1>

    <p><strong>Mobile:</strong> 07940369813<br>
    <strong>E-mail:</strong> wilsonadam15@gmail.com</p>

    <h2>Profile</h2>
    <p>Self-motivated with a passion for learning new technologies. Hands-on experience in full life cycle management delivery and implementation under tight deadlines...</p>

    <!-- Rest of your CV content -->
    """

def start_applications():
    print("Application Started")

    # Create the homepage interface
    with gr.Blocks() as homepage:
        with gr.Row():
            gr.Image("documents/aiSummit.jpg", width=400, height=400)
            gr.Image("documents/Friends.jpg", width=400, height=400)
        gr.Markdown("# Welcome to Adam Wilson's Portfolio")

        # Add your image here
        gr.Markdown("Click a button below to proceed:")

        # Buttons for CV and Chatbot
        with gr.Row():
            cv_button = gr.Button("View CV")
            chatbot_button = gr.Button("Chatbot")

        # CV interface
        with gr.Column(visible=False) as cv_section:
            gr.Markdown("# CV Page")
            gr.HTML(display_cv())  # Display the CV content

        # Chatbot interface
        with gr.Column(visible=False) as chatbot_section:
            gr.Markdown("# Chat with Me")
            chatbot_ui = gr.Chatbot()
            state = gr.State([])  # Initialize state for chat history
            user_input = gr.Textbox(placeholder="Type your message here...")
            clear = gr.Button("Clear")

            # Update the submit method to include state
            user_input.submit(
                chatbot,
                inputs=[user_input, state],
                outputs=[chatbot_ui, state],
            )
            clear.click(
                lambda: ([], []),
                inputs=None,
                outputs=[chatbot_ui, state],
                queue=False
            )

        # Button actions to toggle visibility of sections
        cv_button.click(
            lambda: (gr.update(visible=True), gr.update(visible=False)),
            inputs=None,
            outputs=[cv_section, chatbot_section]
        )

        chatbot_button.click(
            lambda: (gr.update(visible=True), gr.update(visible=False)),
            inputs=None,
            outputs=[chatbot_section, cv_section]
        )

    # Launch the homepage
    homepage.launch()


if __name__ == "__main__":
    start_applications()
