FROM python:3.8-alpine
RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libpq

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
RUN pip install -r requirements.txt
