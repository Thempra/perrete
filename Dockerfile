FROM python:3.14.2-slim

RUN pip install python-telegram-bot

ADD src  /perrete/

WORKDIR /perrete/

ENTRYPOINT /perrete/perrete.py

