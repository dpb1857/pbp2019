#!/usr/bin/env python3

import os
import json
import time

import requests

def get_rider_times(pid):

    payload = {
        "appid": "592479603a4c925a288b4567",
        "token": "B714F968F812FEDCA917",
        "max": 2000,
        "loc": 1,
        "catloc": 1,
        "etimes": 1,
        "units": "metric",
        "source": "webtracker",
    }

    return requests.post("https://api.rtrt.me/events/PBP-2019/profiles/%s/splits" % pid, data=payload).json()

def get_rider_info(frame):
    print("Requesting rider info for frame %s" % frame)

    payload = {
        "max": 100,
        "failonmax": 1,
        "total": 1,
        "appid": "592479603a4c925a288b4567",
        "token": "B714F968F812FEDCA917",
        "search": frame,
        "source": "webtracker",
        }

    r = requests.post("https://api.rtrt.me/events/PBP-2019/profiles", data=payload).json()
    if "list" in r:
        return r["list"][0]

    return None

def main():

    for group in range(ord('A'), ord('Z')+1):
        print("processing group", chr(group))
        failcount = 0
        for i in range(600):
            frame = "%s%03d" % (chr(group), (i+1))

            if os.path.exists("data/%s.rider" % frame):
                continue

            rider_info = get_rider_info(frame)
            if rider_info is None:
                failcount += 1
                if failcount >= 20:
                    break
                else:
                    continue

            failcount = 0
            rider_times = get_rider_times(rider_info["pid"])
            with open("data/%s.rider" % frame, "w") as f:
                f.write(json.dumps(rider_info))
            with open("data/%s.time" % frame, "w") as f:
                f.write(json.dumps(rider_times))
            time.sleep(0.5)


if __name__ == "__main__":
    main()
