FROM python:3.9-slim

COPY ./app /app/fastapi-tutorial
COPY ./requirements.txt /app
WORKDIR /app