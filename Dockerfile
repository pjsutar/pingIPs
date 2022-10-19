FROM python:latest

RUN apt-get install fping

WORKDIR /usr/app/src

COPY . .

RUN pip3 install -r requirements.txt


CMD [ "python", "demo.py"]