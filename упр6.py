import re


class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players: list) -> str:
    counter = len(players)

    if counter != 2:
        raise WrongNumberOfPlayersError

    if not is_rps_suitable(players[0][1]) or not is_rps_suitable(players[1][1]):
        raise NoSuchStrategyError

    if players[0][1] == 'R' and players[1][1] == "S":
        return " ".join(players[0])
    elif players[0][1] == "S" and players[1][1] == "R":
        return " ".join(players[1])
    elif players[0][1] == "S" and players[1][1] == "P":
        return " ".join(players[0])
    elif players[0][1] == "P" and players[1][1] == "S":
        return " ".join(players[1])
    elif players[0][1] == "P" and players[1][1] == "R":
        return " ".join(players[0])
    elif players[0][1] == "R" and players[1][1] == "P":
        return " ".join(players[1])
    elif players[0][1] == players[1][1]:
        return " ".join(players[0])


def is_rps_suitable(players: str) -> bool:
    return re.fullmatch(r"[RPS]", players) is not None

def tests():
    try:
        rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])  #= > WrongNumberOfPlayersError
    except WrongNumberOfPlayersError:
        print("WrongNumberOfPlayersError")

    try:
        rps_game_winner([['player1', 'P'], ['player2', 'A']])  #= > NoSuchStrategyError
    except NoSuchStrategyError:
        print("NoSuchStrategyError")

    try:
        result = rps_game_winner([['player1', 'P'], ['player2', 'S']])  #= > 'player2 S'
        print(result)
    except Exception as e:
        print(e)

    try:
        result = rps_game_winner([['player1', 'P'], ['player2', 'P']])  #= > 'player1 P'
        print(result)
    except Exception as e:
        print(e)


tests()