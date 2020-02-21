#!/bin/bash
# production

echo "[info]start"
#MYSQL_SCHEMA="sal"
ROOT_DIRECTORY="/var/tmp"
CMD_MYSQL="mysql --defaults-extra-file=$ROOT_DIRECTORY/mysql.conf -t --show-warnings $MYSQL_SCHEMA"

QUERY="SELECT imagedata FROM imagelist"

VALUE='echo ${QUERY} | ${CMD_MYSQL}'

RESULT=$?
echo $VALUE

if [ $RESULT -eq 0 ];then
  echo "[INFO] end"
  exit 0
else
  echo "[error]"
  exit 1
fi
