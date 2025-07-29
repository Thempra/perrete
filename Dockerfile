FROM python:3.14.0rc1-slim

RUN pip install python-telegram-bot

ADD src  /perrete/

WORKDIR /perrete/

ENTRYPOINT /perrete/perrete.py

