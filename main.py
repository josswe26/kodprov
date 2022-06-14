import json
import datetime as dt


def list_sorted_tracks(driver_data):
    """ Return list of tracks in alphabetical order from driver data"""
    tracks = []
    for race_start in driver_data:
        if race_start["track"] not in tracks:
            tracks.append(race_start["track"])

    tracks.sort()
    return tracks


def start_method_counter(driver_data, start_method):
    """ Return a counter for a specific start method"""
    counter = 0
    for race_start in driver_data:
        if race_start["startMethod"] == start_method:
            counter += 1

    return counter


def calcutale_bets(driver_data):
    """ Calculate betting win/loss under 2019 """
    start_date = dt.datetime(2019, 1, 1)
    end_date = dt.datetime(2019, 12, 31)
    stake = 0
    winnings = 0

    for race_start in driver_data:
        race_date = dt.datetime.strptime(
            race_start["startTime"].split(".")[0], "%Y-%m-%d %H:%M:%S")
        if race_date >= start_date and race_date <= end_date:
            stake += 100
            if race_start["place"] == 1:
                winnings += 100 * (race_start["odds"]/100)

    total_winnings = winnings - stake

    return total_winnings


with open("goop.json") as file:
    goop_data = json.load(file)

print("\n***** Fråga 1 *****")
print("\nLista av travbanor i alfabetisk ordning:\n")
for track in list_sorted_tracks(goop_data):
    print("- ", track)

print("\n***** Fråga 2 *****")
print(f"\nDet kördes {start_method_counter(goop_data, 'A')} med Autostart.")

print("\n***** Fråga 3 *****")
print(f"Om man spelar 100kr på Björn Goops alla lopp 2019, \
blir det en förlust på {int(-(calcutale_bets(goop_data)))}kr.")
