FROM python:3.9-slim

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y wget
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
RUN unzip ngrok-stable-linux-amd64.zip
RUN chmod +x ngrok

EXPOSE 5000
EXPOSE 4040

CMD bash -c "flask run & sleep 5 && ./ngrok http 5000"

