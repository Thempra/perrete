FROM python:3.14.0a3-slim

RUN pip install python-telegram-bot

ADD src  /perrete/

WORKDIR /perrete/

ENTRYPOINT /perrete/perrete.py

