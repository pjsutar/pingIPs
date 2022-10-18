FROM python:latest
RUN apt-get update && apt-get install -y iputils-ping
WORKDIR /usr/app/src

COPY . .

RUN pip3 install -r requirements.txt


CMD [ "python", "demo.py"]