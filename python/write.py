#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sbb_rs485
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Show text on SBB panels")
    parser.add_argument(
        '--port',
        '-p',
        help="Serial port",
        type=str,
        default='/dev/ttyUSB0',
    )
    parser.add_argument(
        '--text',
        '-t',
        help="End address",
        type=str,
        required=True
    )
    args = parser.parse_args()

    addrs = [96, 17, 7, 37, 38, 78, 35, 11, 14, 52, 36, 21, 10, 44, 5, 40] #woo hardcoded
    cc = sbb_rs485.PanelAlphanumControl(addresses=addrs, port=args.port)
    cc.connect()
    cc.set_text(args.text)
    cc.serial.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
