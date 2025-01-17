FROM python:3.10-slim

WORKDIR /Service
COPY requirements.txt /Service/requirements.txt
COPY start.sh /Service/start.sh
COPY .env /Service/.env

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN 
WORKDIR /Service/app
COPY ./app/ /Service/app

WORKDIR /Service
CMD ["sh", "start.sh"]