from typing import List, Tuple


type Config = dict[str, int]

class Turn():
    def __init__(self, color: str, count: int) -> None:
        self.color = color
        self.count = count

class Game():
    def __init__(self, id: int, turns: List[List[Turn]]):
        self.id = id
        self.turns = turns

    def is_valid(self, cfg: Config) -> bool:
        return all(cfg[indiv_turn.color] >= indiv_turn.count for turn in self.turns for indiv_turn in turn)


class Solution():
    def __init__(self, filename: str = "input", config: Tuple[int, int, int] = (12, 13, 14)) -> None:
        red, green, blue = config
        self._config = {
            "red": red,
            "green": green,
            "blue": blue
        }

        self._games = []
        with open(filename) as f:
            for line in f:
                game_str, turn_str = line.rstrip("\n").split(": ")
                game_id = int(game_str.split(" ")[1])
                indiv_turns = turn_str.split("; ")
                turn_groups = []
                for it in indiv_turns:
                    turns = []
                    moves = it.split(", ")
                    for move in moves:
                        count, color = move.split(" ")
                        count = int(count)
                        turns.append(Turn(color, count))
                    turn_groups.append(turns)

                self._games.append(Game(game_id, turn_groups))

    def sum_valid_game_ids(self):
        return sum(game.id for game in self._games if game.is_valid(self._config))

def main():
    sln = Solution()
    act_sum = sln.sum_valid_game_ids()
    print(f"Sum of valid game IDs: {act_sum}")

if __name__ == "__main__":
    main()
