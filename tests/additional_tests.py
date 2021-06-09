import unittest

from game.logic import GameLogic
from game.cheat_logic import CheatGameLogic


class AdditionalTests(unittest.TestCase):
    def test_2_bad_pos_2_hit_hacked(self):
        game = CheatGameLogic()
        test = []

        while game.secret_code[2] == game.secret_code[3]:
            game.setup_game()

        test = list(game.secret_code)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"KOD: {game.secret_code}")
        print(f"Input: {test}")
        self.assertEqual(game.interact(test), (0, 0))


if __name__ == '__main__':
    unittest.main()
