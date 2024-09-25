FROM python:3.12-slim

WORKDIR /app
COPY  . /app

RUN pip install -r requirements.txt

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python3", "main.py"]
# CMD ["bash", "-c", "cd kernel_memory/service/Service/ && dotnet run & cd /app && python3 user_interface.py"]
