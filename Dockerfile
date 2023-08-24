FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT=1
RUN mkdir /pizzeria_api
WORKDIR /pizzeria_api
COPY  . /pizzeria_api/
RUN pip install -r requirements.txt



