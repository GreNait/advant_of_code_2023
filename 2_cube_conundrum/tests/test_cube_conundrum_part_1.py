import pathlib
from src.cube_conundrum import CubeConundrum
from src.cube_conundrum import LoadGames
import pytest

test_batch = {
    "Game 1": [(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")],
    "Game 2": [(1, "blue"),(2, "green"), (3, "green"), (4, "blue"), (1, "red"),  (1, "green"), (1, "blue")],
    "Game 3": [(8, "green"), (6, "blue"), (20, "red"), (5, "blue"), (4, "red"), (13, "green"), (5, "green"), (1, "red")],
    "Game 4": [(1, "green"), (3, "red"), (6, "blue"), (3, "green"), (6, "red"), (3, "green"), (15, "blue"), (14, "red")],
    "Game 5": [(6, "red"), (1, "blue"), (3, "green"), (2, "blue"), (1, "red"), (2, "green")],
    }

test_limits = [
    (12, "red"),
    (13, "green"),
    (14, "blue"),
]

test_validation = [True,True,False,False,True]

def test_possible_game():
    cube_conundrum = CubeConundrum()
    for game, validates in zip(test_batch.items(), test_validation):
        assert cube_conundrum._valid_game(game=game[1], limits=test_limits) == validates

def test_dict_of_games():
    cube_conundrum = CubeConundrum(games=test_batch, limits=test_limits)
    assert cube_conundrum.validates == test_validation

def test_format_load_games():
    load_games = LoadGames()
    assert load_games.format_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {"Game 1": [(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")]}

def test_load_list_of_games_by_path():
    path_to_list = pathlib.Path("tests/list_of_test_games.txt")
    assert path_to_list.is_file()

    load_games = LoadGames()
    loaded_games = load_games._load_list_of_games(path_to_list)

    assert loaded_games == test_batch

    load_games = LoadGames(path_to_list)
    assert load_games.games == test_batch

def test_load_list_of_games_with_limits():
    path_to_list = pathlib.Path("tests/list_of_test_games.txt")
    assert path_to_list.is_file()

    load_games = LoadGames(path_to_list)
    cube_conundrum = CubeConundrum(games=load_games.games, limits=test_limits)
    assert cube_conundrum.validates == test_validation

def test_calculate_ids():
    cube_conundrum = CubeConundrum(games=test_batch, limits=test_limits)
    assert cube_conundrum._calculate_ids(validations=test_validation) == 8

    cube_conundrum = CubeConundrum(games=test_batch, limits=test_limits)
    assert cube_conundrum.sum_ids == 8