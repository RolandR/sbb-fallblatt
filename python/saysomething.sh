#!/usr/bin/env bash

text="$@"

python3 ./show_text.py -s 1 -e 30 -t "${text}"
