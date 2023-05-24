FROM python:3.9-slim-buster as builder

RUN apt-get install -y --no-install-recommends \
    build-essential= \
    gcc= \
    git= \
    python3-pip= \
    && rm -rf /var/lib/apt/lists/*