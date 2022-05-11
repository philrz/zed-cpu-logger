#!/usr/bin/env python3

import datetime
import json
import psutil
import sys
import zed

FLUSH_INTERVAL = 5
POOL_NAME = 'default'

client = zed.Client()

pool_exists = False
for pool in client.query('from :pools | cut name'):
    if pool['name'] == POOL_NAME:
        pool_exists = True

if pool_exists:
    print('Loading data to existing pool "' + POOL_NAME + '"', end='')
else:
    client.create_pool(POOL_NAME)
    print('Loading data to newly-created pool "' + POOL_NAME + '"', end='')
sys.stdout.flush()

lastflush = datetime.datetime.now(datetime.timezone.utc)
batch = ''

while True:
    busy = str(100 - psutil.cpu_times_percent(interval=1, percpu=False).idle)
    now = datetime.datetime.now(datetime.timezone.utc)
    batch += '{ts:' + now.isoformat().replace('+00:00', 'Z') + ',value:' + busy + '}\n'
    if ((now - lastflush).total_seconds() >= FLUSH_INTERVAL):
        client.load(POOL_NAME, batch)
        print('.', end='')
        sys.stdout.flush()
        batch = ''
        lastflush = now
