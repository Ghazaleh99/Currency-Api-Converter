FROM python:3.8.10
LABEL maintainer = "GH-Bitycle"

ENV PYTHONUNBUFFERED 1

WORKDIR /app 

COPY requirements.txt ./data/requirements.txt
COPY ./app /app

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    rm -rf /tmp && \
    adduser \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user