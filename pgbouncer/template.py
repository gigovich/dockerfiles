#!/env/bin/python

import sys
import os

HOST, PORT = os.getenv('DB_PORT').split('//')[1].split(':')

config_template = '''
[databases]
* = host=%(HOST)s port=%(PORT)s

[pgbouncer]
logfile = /var/log/pgbouncer/pgbouncer.log
pidfile = /var/run/pgbouncer/pgbouncer.pid

listen_addr = 0.0.0.0
listen_port = 6432

unix_socket_dir = /var/run/postgresql

auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
admin_users = docker
stats_users = docker

pool_mode = session

server_reset_query = DISCARD ALL
max_client_conn = 100

default_pool_size = 20
''' % {'HOST': HOST, 'PORT': PORT}

fh = open('/etc/pgbouncer/pgbouncer.ini', 'w+')
fh.writelines(config_template)
fh.close()
sys.exit()
