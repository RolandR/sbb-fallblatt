#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sbb_rs485


POS_A = 0
POS_E = 4
POS_Z = 25
POS_5 = 32

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
        pf = "[{0}{1}{2}] ".format(
            bcolors.OKGREEN,
            "OK",
            bcolors.ENDC,
        )
    if (level == 4):
        pf = "[{0}{1}{2}]".format(
            bcolors.FAIL,
            "FAIL",
            bcolors.ENDC,
        )
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
        description="Find SBB panel addresses",
    )
    parser.add_argument(
        '--port',
        '-p',
        help="Serial port",
        type=str,
        default='/dev/ttyUSB0',
    )
    parser.add_argument(
        '--start',
        '-s',
        help="Start address",
        type=int,
        default=0,
    )
    parser.add_argument(
        '--end',
        '-e',
        help="End address",
        type=int,
        default=255,
    )
    args = parser.parse_args()

    cc = sbb_rs485.PanelControl(port=args.port)
    cc.connect()
    cc.serial.timeout = 0.05

    try:
        for i in range(args.start, args.end + 1):
            print("Trying address {0}{1}{2}".format(
                bcolors.BOLD,
                i,
                bcolors.ENDC,
            ))
            serial = cc.get_serial_number(i)
            if len(serial) == 4:
                print("Module address is: {0}{1}{2}".format(
                    bcolors.BOLD,
                    i,
                    bcolors.ENDC,
                ))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
