#!/usr/bin/env python3

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

    if False:
        for i in range(1):
            frame = "A%03d" % (i+1)
            print (frame)
            get_rider_info(frame)

    rider_info = get_rider_info("V041")
    rider_times = None
    if rider_info:
        rider_times = get_rider_times(rider_info["pid"])
    print(rider_info)
    print(rider_times)

if __name__ == "__main__":
    main()
