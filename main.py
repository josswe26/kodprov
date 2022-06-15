import json
import datetime as dt
from collections import Counter


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


def calculate_bets(driver_data):
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
            elif race_start["place"] == 0:
                winnings += 100

    total_winnings = winnings - stake

    return total_winnings


def list_tracks_by_victory_percentage(driver_data):
    """ 
    Calculate victory percentage per track
    and return a list
    """
    tracks_by_victory_percentage = {}

    races_per_track = dict(Counter(race_start["track"]
                           for race_start in driver_data 
                           if race_start["place"] != 0))

    victories_per_track = dict(Counter(race_start["track"]
                               for race_start in driver_data
                               if race_start["place"] == 1))

    for track in races_per_track:
        if track in victories_per_track:
            tracks_by_victory_percentage[track] = float("{:.2f}".format(
                victories_per_track[track] / races_per_track[track] * 100))
        else:
            tracks_by_victory_percentage[track] = 0

    tracks_by_victory_percentage = sorted(
        tracks_by_victory_percentage.items(),
        key=lambda x: x[1], reverse=True)

    return tracks_by_victory_percentage


def calculate_prize_money(driver_data):
    """ Calculate prize money under Q4 2019 """
    start_date = dt.datetime(2019, 10, 1)
    end_date = dt.datetime(2019, 12, 31)
    prize_money = 0

    for race_start in driver_data:
        race_date = dt.datetime.strptime(
            race_start["startTime"].split(".")[0], "%Y-%m-%d %H:%M:%S")
        if race_date >= start_date and race_date <= end_date:
            if (race_start["place"] == 1 and
                    race_start["firstPrize"] is not None):
                prize_money += race_start["firstPrize"]

    return prize_money

with open("goop.json") as file:
    goop_data = json.load(file)

print("\n***** Fråga 1 *****")
print("\nLista av travbanor i alfabetisk ordning:\n")
for track in list_sorted_tracks(goop_data):
    print("- ", track)

print("\n***** Fråga 2 *****")
print(f"\nDet kördes {start_method_counter(goop_data, 'A')} med Autostart.")

print("\n***** Fråga 3 *****")
print(f"\nOm man spelar 100kr på Björn Goops alla lopp 2019, "
      f"blir det en förlust på {int(-(calculate_bets(goop_data)))}kr.")

print("\n***** Fråga 4 *****")
print("\nLista av Björn Goops segerprocent per bana 2019:\n")
for track in list_tracks_by_victory_percentage(goop_data):
    print(f"-  {track[0]}: {track[1]} %")

print("\n***** Fråga 5 *****")
print(f"\nBjörn Goop tjänade {calculate_prize_money(goop_data)}kr"
      " i prispengar under Q4 2019.\n")
