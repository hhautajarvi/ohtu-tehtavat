from playerreader import PlayerReader
from playerstats import PlayerStats
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    nat = "FIN"
    datenow = datetime.now()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nat)

    print(f"Players from {nat} {datenow.isoformat(' ')} \n")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
