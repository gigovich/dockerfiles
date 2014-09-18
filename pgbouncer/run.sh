#!/bin/env sh

# Prepare template by envirement variables
/usr/bin/python /home/docker/template.py

# Run pgbouncer with generated config
/usr/sbin/pgbouncer /etc/pgbouncer/pgbouncer.ini
