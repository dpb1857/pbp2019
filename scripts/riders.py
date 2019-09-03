#!/usr/bin/env python3

import requests

def get_frame(frame):
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

    r = requests.post("https://api.rtrt.me/events/PBP-2019/profiles", data=payload)
    riderData = r.json()["list"][0]
    print(riderData)

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

    response = requests.post("https://api.rtrt.me/events/PBP-2019/profiles/%s/splits" % riderData["pid"], data=payload)
    print (response.text)


def main():

    info = get_frame("V041")
    print(info)
if __name__ == "__main__":
    main()
