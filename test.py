import unittest
from rover import Rover


class Tests(unittest.TestCase):
    def test_move_R(self):
        r = Rover()
        r.move("R")
        self.assertEqual(r.facing, "E")

    def test_move_F(self):
        r = Rover()
        r.move("F")
        self.assertEqual(r.position[0], 0)
        self.assertEqual(r.position[1], 1)

    def test_run_L(self):
        r = Rover()
        r.run("LL")
        self.assertEqual(r.get_communication(), "0 0 S")

    def test_run_B(self):
        r = Rover()
        r.run("BBBBBBBBB")
        self.assertEqual(r.get_communication(), "0 -9 N")

    def test_full_run(self):
        r = Rover()
        r.run("LBLFRRLBRLFBRL\nLBBBFRLBLLLFR\nLBRLBLLLL")
        self.assertEqual(r.get_communication(), "2 -1 W\n1 2 N\n3 2 W")

    def test_bad_instructions(self):
        r = Rover()
        with self.assertRaises(ValueError):
            r.run("aezrcuazerc")

    def test_assignement_part_1(self):
        r = Rover()
        r.run("RFFFFLFFFF")
        self.assertEqual(r.get_communication(), "4 4 N")

    def test_assignement_full(self):
        r = Rover()
        r.run("RFFFFLFFFF\nLFFL")
        self.assertEqual(r.get_communication(), "4 4 N\n2 4 S")


if __name__ == '__main__':
    unittest.main()
