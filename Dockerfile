FROM python:3

ADD src  /perrete/

RUN pip install python-telegram-bot

CMD [ "python", "/perrete/perrete.py" ]
