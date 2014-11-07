FROM ubuntu:trusty

RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" > /etc/apt/sources.list.d/multiverse.list
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty multiverse" > /etc/apt/sources.list.d/multiverse-src.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libpq5
RUN apt-get install -y libpq-dev
RUN apt-get install -y postgresql-client-common
RUN apt-get install -y postgresql-server-dev-9.3
RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-setuptools


RUN easy_install pip
RUN pip install psycopg2
RUN pip install sentry
RUN pip install eventlet

EXPOSE 9000/tcp 9001/udp

ADD sentry.conf.py /sentry.conf.py

ENTRYPOINT ["/usr/local/bin/sentry", "--config=/sentry.conf.py"]
CMD ["start", "udp"]
