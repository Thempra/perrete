FROM python:3.13.0b3-slim

RUN pip install python-telegram-bot

ADD src  /perrete/

WORKDIR /perrete/

ENTRYPOINT /perrete/perrete.py

