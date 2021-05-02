FROM python:3.6.9-alpine

RUN mkdir /communication
WORKDIR /communication

ADD requirements.txt /communication/requirements.txt
RUN pip install -r requirements.txt

ADD . /communication

EXPOSE 9000

CMD ["python", "/communication/communication.py"]