import gradio as gr
from src.basic_rag import runner

# Define a simple chatbot function that responds to user input
def chatbot(user_input, chat_history=[]):
    message = runner(user_input)
    chat_history.append(("User: " + user_input, "Bot: " + message))
    return chat_history, chat_history

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
    <p>Self-motivated with a passion for learning new technologies. Hands-on experience in full life cycle management delivery and implementation under tight deadlines. Proven ability to translate customer business requirements into technical designs and communicate them effectively to peers and management. Experienced in Agile teams, enthusiastic about sharing knowledge, and confident in providing technical training across all levels. Initiated and founded AI projects that evolved into company departments. Adaptable to new situations, always seeking opportunities to face new challenges and enhance skill sets.</p>

    <h2>Key Skills</h2>
    <ul class="multi-column">
        <li>Autogen</li>
        <li>Web Design (HTML CSS)</li>
        <li>Programming</li>
        <li>Semantic Kernel</li>
        <li>CI/CD</li>
        <li>AI</li>
        <li>Automation Development</li>
        <li>Cloud Networking</li>
        <li>MySQL</li>
        <li>Microsoft Azure Cloud</li>
        <li>Azure OpenAI</li>
        <li>Training/Coaching</li>
        <li>Python</li>
        <li>Agile Working</li>
        <li>Database Development</li>
        <li>Flask</li>
        <li>Terraform</li>
        <li>Docker</li>
        <li>DevOps</li>
        <li>Network Cloud</li>
        <li>Mentoring</li>
    </ul>

    <h2>Employment</h2>

    <h3>AI and Data Technical Lead – Mouser Electronics EPM | April 2021 – Present:</h3>
    <ul>
        <li>Led the development of an AI platform and managed the technical direction of the AI team. Architected a scalable AI core using Semantic Kernel that enables growth. Created Terraform repositories that deploy infrastructure.</li>
        <li>Designed and implemented a Semantic Kernel core providing users with an endpoint that dynamically determines the best course of action using available plugins. Established development policies for future plugins and built GitLab pipelines for Azure Function Apps.</li>
        <li>Developed an AI chatbot leveraging Semantic Kernel for user conversations, going live in December 2024.</li>
        <li>Created an AI-powered translation tool reducing annual translation costs from $1.5 million.</li>
        <li>Developed an image scanning tool for sales form automation.</li>
        <li>Using Autogen, created "Developers helping hand" linked to GitLab for programming in natural language.</li>
    </ul>

    <h3>Senior DevOps/Automation Engineer – Mouser Electronics EPM | August 2021 – April 2023:</h3>
    <ul>
        <li>Designed automation workflows for ITSM systems, streamlining processes like new user account creation and equipment orders.</li>
        <li>Led the migration of security keys from KeyPass to Centrify.</li>
        <li>Developed a Prometheus-based anomaly detection tool for server health monitoring.</li>
        <li>Created the "MUBI" system for maintaining base images within Red Hat OpenShift.</li>
    </ul>

    <h2>Awards</h2>
    <ul>
        <li>Employee of the Year at Mouser Electronics</li>
        <li>BT Apprentice of the Year</li>
    </ul>

    <h2>Certifications</h2>
    <ul>
        <li>3 A Levels: Engineering, Physics, and Computer Science</li>
        <li>Microsoft Technology Associate (Cloud Fundamentals, Networking Fundamentals, Device Fundamentals)</li>
        <li>BSC Level 3 Coding and Logic</li>
    </ul>
    """

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
        user_input = gr.Textbox(placeholder="Type your message here...")
        clear = gr.Button("Clear")
        
        user_input.submit(chatbot, inputs=[user_input, chatbot_ui], outputs=[chatbot_ui, chatbot_ui])
        clear.click(lambda: None, None, chatbot_ui)

    # Button actions to toggle visibility of sections
    cv_button.click(lambda: (gr.update(visible=True), gr.update(visible=False)),
                    outputs=[cv_section, chatbot_section])

    chatbot_button.click(lambda: (gr.update(visible=True), gr.update(visible=False)),
                        outputs=[chatbot_section, cv_section])

# Launch the homepage
homepage.launch()