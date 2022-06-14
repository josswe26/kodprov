import json


def list_sorted_tracks(driver_data):
    tracks = []
    for race_start in driver_data:
        if race_start["track"] not in tracks:
            tracks.append(race_start["track"])

    tracks.sort()
    return tracks


with open("goop.json") as file:
    goop_data = json.load(file)

for track in list_sorted_tracks(goop_data):
    print(track)
