#!/usr/bin/env sh
RUN="-d"
SET_NAME="--name sentry"
if [ "$1" != "" ]; then
  $RUN="--rm -i -t"
  $SET_NAME=""
fi
sudo docker run \
--link pgbouncer:db \
--link suspicious_archimedes:mail \
-e "SENTRY_URL=" \
-e "SENTRY_DB_USER=" \
-e "SENTRY_DB_PASS=" \
-e "SENTRY_MAIL_USER=" \
-e "SENTRY_MAIL_PASSWORD=" \
$SET_NAME $RUN \
localhost:5000/sentry $1
