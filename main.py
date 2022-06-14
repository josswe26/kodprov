import json


def list_sorted_tracks(driver_data):
    tracks = []
    for race_start in driver_data:
        if race_start["track"] not in tracks:
            tracks.append(race_start["track"])

    tracks.sort()
    return tracks


def start_method_counter(driver_data, start_method):
    counter = 0
    for race_start in driver_data:
        if race_start["startMethod"] == start_method:
            counter += 1

    return counter





with open("goop.json") as file:
    goop_data = json.load(file)

print("\n***** Fråga 1 *****")
print("\nLista av travbanor i alfabetisk ordning:\n")
for track in list_sorted_tracks(goop_data):
    print("- ", track)

print("\n***** Fråga 2 *****")
print(f"\nDet kördes {start_method_counter(goop_data, 'A')} med Autostart.")


