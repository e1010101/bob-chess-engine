import numpy as np


# Possible improvement: use numpy arrays for game board
class GameState():
    def __init__(self):
        self.board = np.array(
            [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
             ["--", "--", "--", "--", "--", "--", "--", "--"], ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"], ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"], ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]])

        self.whiteToMove = True
        self.moveLog = []
