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
        h1, h2, h3 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        p, li {
            font-size: 16px;
            line-height: 1.5;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .multi-column {
            column-count: 2;
            -webkit-column-count: 2; /* Safari and Chrome */
            -moz-column-count: 2; /* Firefox */
            column-gap: 40px;
        }
        .contact-info {
            margin-bottom: 20px;
        }
        .section {
            margin-bottom: 30px;
        }
        .subsection {
            margin-bottom: 20px;
        }
        .job-title {
            font-weight: bold;
            font-size: 18px;
        }
        .company-date {
            font-style: italic;
            margin-bottom: 10px;
        }
        .award-title {
            font-weight: bold;
        }
    </style>

    <h1>Adam Wilson</h1>
    <p class="contact-info">
        <strong>Mobile:</strong> 07940369813<br>
        <strong>E-mail:</strong> <a href="mailto:wilsonadam15@gmail.com">wilsonadam15@gmail.com</a>
    </p>

    <div class="section">
        <h2>Profile</h2>
        <p>Self-motivated with a passion for learning new technologies. Hands-on experience in full life cycle management delivery and implementation under tight deadlines. Proven ability to translate customer business requirements into technical designs and communicate them effectively to peers and management. Experienced in Agile teams, enthusiastic about sharing knowledge, and confident in providing technical training across all levels. Initiated and founded the AI projects that evolved into company departments. Adaptable to new situations, always seeking opportunities to face new challenges and enhance skill sets.</p>
    </div>

    <div class="section">
        <h2>Key Skills</h2>
        <div class="multi-column">
            <ul>
                <li>Autogen</li>
                <li>Web Design (HTML, CSS)</li>
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
        </div>
    </div>

    <div class="section">
        <h2>Employment</h2>

        <div class="subsection">
            <p class="job-title">AI and Data Technical Lead</p>
            <p class="company-date">Mouser Electronics, EPM | April 2021 – Present</p>
            <ul>
                <li><strong>AI Platform Team Leadership:</strong>
                    <ul>
                        <li>Led the development of an AI platform and managed the technical direction of the AI team. Architected a scalable AI core using semantic kernel that enables growth. Created the Terraform repositories that deploy the infrastructure.</li>
                    </ul>
                </li>
                <li><strong>Semantic Kernel Core Development:</strong>
                    <ul>
                        <li>Designed and implemented a Semantic Kernel core, providing users with an endpoint that dynamically determines the best course of action using available plugins. Established development policies for future plugins and built GitLab pipelines that handle build, scan, and deployment processes for Azure Function Apps.</li>
                    </ul>
                </li>
                <li><strong>AI Chatbot Development:</strong>
                    <ul>
                        <li>Developed an AI chatbot leveraging the Semantic Kernel to facilitate end-to-end conversations with users, helping them find the right products based on their needs, which will be going live in December 2024.</li>
                    </ul>
                </li>
                <li><strong>AI Translation Tool:</strong>
                    <ul>
                        <li>Created an AI-powered translation tool that reduced annual translation costs from $1.5 million. This tool scans website updates, translates content into five languages, and sends it for in-house review before publishing it on the website.</li>
                    </ul>
                </li>
                <li><strong>Document Intelligence for Sales Automation:</strong>
                    <ul>
                        <li>Developed an image scanning tool that automates the process of reading and entering sales forms, previously performed manually, using document intelligence to streamline data entry.</li>
                    </ul>
                </li>
                <li><strong>Developers Helping Hand:</strong>
                    <ul>
                        <li>Using Autogen, created an application named "Developers Helping Hand" linked to GitLab, allowing developers to program in natural language.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div class="subsection">
            <p class="job-title">Senior DevOps/Automation Engineer</p>
            <p class="company-date">Mouser Electronics, EPM | August 2021 – April 2023</p>
            <ul>
                <li><strong>ITSM Automation:</strong>
                    <ul>
                        <li>Designed and implemented automation workflows for the ITSM system, streamlining processes such as new user account creation in Active Directory and automatic equipment orders. Integrated paging duty alerts to notify teams of critical tickets.</li>
                    </ul>
                </li>
                <li><strong>Key Migration Project:</strong>
                    <ul>
                        <li>Led the migration of security keys from KeyPass to Centrify, ensuring secure and efficient key management across the organization.</li>
                    </ul>
                </li>
                <li><strong>Anomaly Detection & Monitoring:</strong>
                    <ul>
                        <li>Developed an anomaly detection tool using Prometheus to monitor server health. Replaced email flood notifications with a streamlined system that only triggered alerts for anomalies, improving response time and reducing noise.</li>
                    </ul>
                </li>
                <li><strong>"MUBI" System Development:</strong>
                    <ul>
                        <li>Created the "MUBI" automation system for maintaining base images like Python and Java within Red Hat OpenShift. The system pulled the latest releases, performed containerized builds, ran security scans, and updated the base image repository upon passing scans. Unsafe images were destroyed automatically, ensuring a secure and up-to-date image repository.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div class="subsection">
            <p class="job-title">Automation Software Engineer</p>
            <p class="company-date">System Interface, British Telecom | April 2021 – August 2022</p>
            <ul>
                <li><strong>Operation Galaxy - Huawei Equipment Removal:</strong>
                    <ul>
                        <li>Contributed to "Operation Galaxy," a critical project aimed at removing Huawei equipment from the network. Ensured that all container images containing necessary software were uploaded in accordance with CI/CD policies, facilitating smooth software updates and deployments.</li>
                    </ul>
                </li>
                <li><strong>Network Anomaly Detection Tool:</strong>
                    <ul>
                        <li>Developed a network anomaly detection tool to address discrepancies in traffic and failure reporting during public holidays. The tool ensured that alerts during peak traffic periods were accurate, improving network reliability and reducing false alarms.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div class="subsection">
            <p class="job-title">Infrastructure Engineer Apprentice</p>
            <p class="company-date">British Telecom | September 2019 – April 2021</p>
            <ul>
                <li>Designed and maintained in-house monitoring tools for customer networks.</li>
                <li>Developed a machine learning anomaly detection tool for network monitoring and auto troubleshooting.</li>
                <li>Worked on national security projects with government services.</li>
            </ul>
        </div>

        <div class="subsection">
            <p class="job-title">Founder & Website Designer</p>
            <p class="company-date">Self-Employed | May 2017 – August 2019</p>
            <ul>
                <li>Founded AW Website Designs to experience the challenges of growing a business while staying technical. Learned how to communicate effectively at both high and low levels.</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>Awards</h2>
        <ul>
            <li><span class="award-title">Employee of the Year at Mouser:</span>
                <ul>
                    <li>Awarded by the CEO of Mouser Electronics for starting and leading the AI team.</li>
                </ul>
            </li>
            <li><span class="award-title">BT Apprentice of the Year:</span>
                <ul>
                    <li>Out of 300 apprentices studying around the UK at BT while attending Bristol University. Recognized for university work, being the BT Apprentice ambassador, and leading the ML anomaly detection tool.</li>
                </ul>
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Leadership, Mentorship, and Personal Interests</h2>
        <p>Within BT, was selected to be the Head of Attraction ambassador for BT Bristol, involving promoting and interviewing potential new apprentices and graduates to BT.</p>
        <p>Outside of BT, provides Python tutoring, reinforcing knowledge while passing it on to aspiring programmers.</p>
        <p>Enjoys trying various sports with friends, fostering a competitive spirit. Keen mountain biker attending races around the UK and plays rugby as number 10.</p>
    </div>

    <div class="section">
        <h2>Key Certifications</h2>
        <ul>
            <li>3 A Levels: Engineering, Physics, and Computer Science</li>
            <li>BT Apprentice while studying at the University of Bristol</li>
            <li>2020 - Microsoft Technology Associate Cloud Fundamentals</li>
            <li>2020 - BSC Level 3 Coding and Logic</li>
            <li>2020 - Microsoft Technology Associate Networking Fundamentals</li>
            <li>2020 - Microsoft Technology Associate Device Fundamentals</li>
            <li>2020 - Microsoft Technology Associate Networking Materials</li>
        </ul>
    </div>
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
