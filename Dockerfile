FROM python:3.12-slim
WORKDIR /app
COPY  . /app

RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["python", "src/user_interface.py"]
