#!/bin/bash -x
rsync -avz --exclude .git \
    --exclude *.pyc \
    --exclude .idea \
    --exclude *.sqlite3 \
    --exclude settings-az.py \
    ./ zemonweb@zemon.name:parashabytes.zemon.name

ssh zemonweb@zemon.name 'cd parashabytes.zemon.name && ./restartwsgi.sh'
