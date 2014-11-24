FROM ubuntu:latest

RUN apt-get update && apt-get -y install wget unzip supervisor
RUN wget https://dl.bintray.com/mitchellh/consul/0.4.1_linux_amd64.zip
RUN unzip 0.4.1_linux_amd64.zip
RUN cp consul /usr/local/bin/

ADD supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD supervisor/consul.conf /etc/supervisor/conf.d/consul.conf

ADD consul/dns.json /etc/consul/consul.d/dns.json

CMD ["/usr/bin/supervisord"]
