FROM ubuntu:latest

RUN apt-get update && apt-get -y install wget unzip supervisor
RUN wget https://dl.bintray.com/mitchellh/consul/0.4.1_linux_amd64.zip
RUN unzip 0.4.1_linux_amd64.zip
RUN cp consul /usr/local/bin/
RUN mkdir -p /etc/consul/consul.d

ADD supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD supervisor/consul.conf /etc/supervisor/conf.d/consul.conf

CMD ["/usr/bin/supervisord"]
