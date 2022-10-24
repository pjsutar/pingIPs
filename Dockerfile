FROM python:latest

RUN sudo apt install -y fping

WORKDIR /usr/app/src

COPY . .

RUN pip3 install -r requirements.txt


CMD [ "python", "demo.py"]
