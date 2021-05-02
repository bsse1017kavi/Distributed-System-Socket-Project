FROM python:3.6.9-alpine

RUN mkdir /ratings
WORKDIR /ratings

ADD requirements.txt /ratings/requirements.txt
#RUN apk update && apk upgrade
#RUN apk add --no-cache bash\
#                       #pkgconfig \
#                       #git \
#                       gcc \
#                       #libcurl \
#                       #gpgme-dev \
#                       #libc-dev \
#    && rm -rf /var/cache/apk/*
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
#RUN apk -q --no-cache add mariadb-client-libs
RUN apk add build-base
#RUN apk add libmysqlclient-dev
RUN pip install -r requirements.txt
RUN apk del build-deps

ADD . /ratings

EXPOSE 7000

CMD ["python", "/ratings/rating.py"]