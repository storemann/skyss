#!/usr/bin/env python

import time
import requests
import logging

logging.captureWarnings(True)

API = "https://skyss.giantleap.no/public/departures?Hours=1&StopIdentifiers={}"

STOP_SANDSLI = "12017667"
STOP_SANDSLI_BYBANE = "12017645"


def get_times(stops):
    r = requests.get(API.format(",".join(stops)), verify=False)
    r.raise_for_status()
    js = r.json()
    if not "PassingTimes" in js:
        raise KeyError(js["errorMessage"] + " " + ",".join(stops))
    return js


def print_routes(stops):
    data = get_times(stops)
    items = data.get("PassingTimes")
    stops = data.get("Stops")
    stops_str = ' and '.join([stops[i]["Description"] for i in stops])

    print("{} timetable {}\n".format(stops_str, time.strftime("%d.%m.%Y %H:%M:%S")))
    print("Departure:  Line:  From:                          Destination:")
    for item in items:
        stop_id = item["StopIdentifier"]
        desc = stops[stop_id]["Description"]
        print(
            "{:<11} {:<6} {:<30} {:}".format(
                item["DisplayTime"],
                item["RoutePublicIdentifier"],
                desc,
                item["TripDestination"],
            )
        )


def main():
    import sys

    if len(sys.argv) == 1:
        print_routes([STOP_SANDSLI, STOP_SANDSLI_BYBANE])
    else:
        print_routes(sys.argv[1:])


if __name__ == "__main__":
    main()
