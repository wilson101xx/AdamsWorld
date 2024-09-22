FROM python:3.12.6-windowsservercore-ltsc2022

WORKDIR /app
COPY  . /app

RUN pip install -r requirements.txt


EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "user_interface.py"]