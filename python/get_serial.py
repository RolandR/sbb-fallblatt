#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sbb_rs485

LOG_OK = 1
LOG_FAIL = 4


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(level, message):
    if (level == 1):
        pf = "[{0}{1}{2}] ".format(bcolors.OKGREEN, "OK", bcolors.ENDC)
    if (level == 4):
        pf = "[{0}{1}{2}]".format(bcolors.FAIL, "FAIL", bcolors.ENDC)
    print("{0} {1}".format(pf, message))


def fmt_ser(ser):
    ss = "{0}{1}{2}{3}".format(
        str(hex(ser[0]))[2:].upper(),
        str(hex(ser[1]))[2:].upper(),
        str(hex(ser[2]))[2:].upper(),
        str(hex(ser[3]))[2:].upper(),
    )
    return ss


def main():
    parser = argparse.ArgumentParser(
        description="Get serial number from SBB panel",
    )
    parser.add_argument(
        '--port',
        '-p',
        help="Serial port",
        type=str,
        default='/dev/ttyUSB0',
    )
    parser.add_argument(
        '--address',
        '-a',
        help="Address",
        type=int,
        default=0,
    )
    args = parser.parse_args()

    cc = sbb_rs485.PanelControl(port=args.port)
    cc.connect()
    cc.serial.timeout = 0.1

    serial = cc.get_serial_number(args.address)
    if len(serial) == 4:
        log(LOG_OK, "reading serial ({0})".format(fmt_ser(serial)))
    else:
        log(LOG_FAIL, "reading serial")


if __name__ == '__main__':
    main()
