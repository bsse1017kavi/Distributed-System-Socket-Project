FROM python:3.6.9-alpine

RUN mkdir /ride_sharing
WORKDIR /ride_sharing

ADD requirements.txt /ride_sharing/requirements.txt
RUN pip install -r requirements.txt

ADD . /ride_sharing

EXPOSE 8000

CMD ["python", "/ride_sharing/ride_sharing.py"]