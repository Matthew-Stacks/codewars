FROM python:3.11-alpine as builder

WORKDIR /tmp

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev && \
    pip install --no-cache-dir hatch

COPY ./pyproject.toml /tmp/

RUN adduser --disabled-password --gecos '' hatch && \
    chown -R hatch:hatch /tmp