FROM python:3.10-slim

WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
