from os import getenv

import clickhouse_connect
from aiogram import Router

router = Router(name=__name__)

client = clickhouse_connect.get_client(host='clickhouse', port=8123, username=getenv('CLICKHOUSE_USER'),
                                       password=getenv('CLICKHOUSE_PASSWORD'), database='go')
