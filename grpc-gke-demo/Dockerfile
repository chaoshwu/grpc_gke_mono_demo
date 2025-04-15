FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server .
COPY proto ./proto

CMD ["python", "server/main.py"]
