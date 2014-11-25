FROM consul-agent
MAINTAINER Givi Khojanashvili <gigovich@gmail.com>

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver keyserver.ubuntu.com \
--recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > \
/etc/apt/sources.list.d/pgdg.list

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.3
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
python-software-properties \
software-properties-common \
pgbouncer

RUN mkdir /var/run/pgbouncer && chown postgres:postgres /var/run/pgbouncer
RUN mkdir /var/log/pgbouncer && chown postgres:postgres /var/log/pgbouncer

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
USER postgres

ADD pgbouncer.ini /etc/pgbouncer/pgbouncer.ini

# Add service disocvery config file
ADD consul/pgbouncer.json /etc/consul/consul.d/pgbouncer.json

# Expose the PostgreSQL port
EXPOSE 6432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/pgbouncer", "/var/run/pgbouncer", "/var/log/pgbouncer"]

USER root
# Set the default command to run when starting the container
CMD ["/usr/bin/supervisord"]
