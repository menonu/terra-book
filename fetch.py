#!/usr/bin/env python3

import sys
from datetime import datetime


def run(address: str, begin_utc: datetime, end_utc: datetime):
    pass


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Too few args')
        print('  Usage: ./fetch.py terra_address begin_date_utc end_date_utc')
        print('example: ./fetch.py terra1dp0taj85ruc299rkdvzp4z5pfg6z6swaed74e6 20210906 20210907')
        sys.exit(1)

    run(sys.argv[1], sys.argv[2], sys.argv[3])
