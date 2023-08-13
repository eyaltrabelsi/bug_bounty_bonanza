FROM python:3.9-slim

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN apt-get update && \
    apt-get install -y wget unzip libglib2.0-0 libsm6 libxrender1 libxext6 && \
    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip && \
    chmod +x ngrok

RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . /app

EXPOSE 5000
EXPOSE 4040

CMD bash -c "flask run & sleep 5 && ./ngrok http 5000"

