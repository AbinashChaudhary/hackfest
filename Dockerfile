FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /django

ADD . /django

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

