#!/usr/bin/env python3
import argparse
import random
import datetime
import json

import dateparser

parser = argparse.ArgumentParser()

parser.add_argument(
    "--from",
    dest="date_from",
    type=str,
    help="Start date",
    default="2 hours ago"
)

parser.add_argument(
    "--to",
    dest="date_to",
    type=str,
    help="End date",
    default="now"
)

parser.add_argument(
    "--number-rows",
    type=int,
    help="Number log entries to generate",
    default=100
)

args = parser.parse_args()

args.date_from = dateparser.parse(
    args.date_from,
    settings={'RETURN_AS_TIMEZONE_AWARE': True}
)
args.date_to = dateparser.parse(
    args.date_to,
    settings={'RETURN_AS_TIMEZONE_AWARE': True}
)

timestamp_list = []

distance = (args.date_to - args.date_from).total_seconds()

i = 0
while True:
    t = random.randint(0, int(distance))
    if t not in timestamp_list:
        timestamp_list.append(t)
        i += 1

    if i == args.number_rows:
        break

timestamp_list.sort()

for i, t in enumerate(timestamp_list):
    row = json.dumps({
        "log": "Msg %i\n" % i,
        "stream": random.choice(("stdout", "stderr")),
        "time":
            (
                args.date_from + datetime.timedelta(seconds=t)
            ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    })
    print(row)
