FROM python:3

RUN pip install python-telegram-bot

ADD src  /perrete/

WORKDIR /perrete/

ENTRYPOINT /perrete/perrete.py

