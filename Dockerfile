FROM python:3.10

ARG PORT

RUN echo "${NAME}, ${PORT}"


WORKDIR /app

RUN apt update && apt install netcat postgresql-client dnsutils -y

RUN pip install --upgrade pip


RUN pip install --upgrade pip

RUN pip freeze > requirements.txt
COPY requirements.txt "/app"

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE ${PORT}

COPY . .

COPY entrypoint.sh "/app"
RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]

CMD uvicorn main:app --port $PORT --reload