# syntax=docker/dockerfile:1
FROM python:3.11

RUN <<eot
  apt update
  apt install -y xmlsec1 libxmlsec1-openssl libpq-dev python3-deve
  pip install -U pip
eot


COPY requirements.txt .
RUN <<eot
  pip install -r requirements.txt
eot

COPY . .