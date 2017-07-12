#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import time
import sbb_rs485
from datetime import datetime

SBB_MODULE_ADDR_HOUR = 55
SBB_MODULE_ADDR_MIN  = 56


def main():
    parser = argparse.ArgumentParser(
        description="Show a clock on SBB panels",
    )
    parser.add_argument(
        '--port',
        '-p',
        help="Serial port",
        type=str,
        default='/dev/ttyUSB0',
    )
    parser.add_argument(
        '--hour-address',
        '-h',
        help="Address of hour module",
        type=int,
        default=0,
    )
    parser.add_argument(
        '--minute-address',
        '-m',
        help="Address of minute module",
        type=int,
        default=1,
    )
    args = parser.parse_args()

    clock = sbb_rs485.PanelClockControl(
        port=args.port,
        addr_hour=args.hour_address,
        addr_min=args.minute_address,
    )
    clock.connect()

    while True:
        clock.set_time_now()
        ts = datetime.utcnow()
        sleeptime = 60 - (ts.second + ts.microsecond / 1000000.0)
        time.sleep(sleeptime)


if __name__ == '__main__':
    main()
