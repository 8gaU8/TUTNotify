#!/usr/bin/python3

import datetime as dt
import json
import os
import sys
from pathlib import Path

from message_senders import LineSender


def get_schedule(schedule: dict) -> dict:
    dates = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    today = dt.date.today().weekday()
    today = dates[today]
    return schedule[today]


def base_msg(time: str, s: dict) -> str:
    return "{time}限: {title}@{room}".format(
        time=time,
        title=s["title"],
        room=s["room"],
    )


def build_current_msg(today_sch: dict, time: str):
    current_sch = today_sch.get(time, None)
    if current_sch is None:
        return None
    return base_msg(time, current_sch)


def build_today_msg(today_sch: dict):
    times = [s for s in today_sch.keys()]
    subjs = [s for s in today_sch.values()]
    today_sch_list = zip(times, subjs)
    today_sch_str = [base_msg(t, s) for t, s in today_sch_list]
    msg = "\n" + "\n".join(today_sch_str)
    return msg


def main():
    with open("./schedule.json") as fp:
        schedule = json.load(fp)

    today_sch = get_schedule(schedule)
    if len(sys.argv) < 2:
        msg = build_today_msg(today_sch)
    else:
        time = sys.argv[1].strip()[0]
        msg = build_current_msg(today_sch, time)

    if msg is None or msg.strip() == "":
        return

    with open("./token.txt") as fp:
        token = fp.read()
    token = token.strip()
    sender = LineSender(token)
    sender.send(msg)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()
