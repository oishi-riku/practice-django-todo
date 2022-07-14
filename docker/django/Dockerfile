FROM python:3.10.5

COPY requirements.txt .

RUN apt update && \
    pip install --upgrade pip && \
    pip install -r requirements.txt