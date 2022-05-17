FROM python:latest
ENV PYTHONUNDUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD uvicorn app:app --reload --host 0.0.0.0 --port 8000