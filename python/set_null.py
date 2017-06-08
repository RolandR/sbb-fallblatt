#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sbb_rs485


def main():
    cc = sbb_rs485.PanelClockControl()
    cc.connect()
    cc.serial.timeout = 2

    input("Press any key")
    msg =  b"\xFF"
    msg += CMD_ZERO
    cc.send_msg(msg)


if __name__ == '__main__':
    main()
