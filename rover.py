import numpy as np

R_moves = {"N": "E", "E": "S", "S": "W", "W": "N"}
L_moves = {v: k for k, v in R_moves.items()}
F_moves = {
    "N": np.array([0, 1]),
    "E": np.array([1, 0]),
    "S": np.array([0, -1]),
    "W": np.array([-1, 0])
}
available_instructions = "LRFB\n"


class Rover:
    def __init__(self):
        self.position = np.array([0, 0])
        self.facing = "N"
        self.communication = ""

    def move(self, instruction):
        if instruction == "R":
            self.facing = R_moves[self.facing]
        elif instruction == "L":
            self.facing = L_moves[self.facing]
        else:
            direction = 1 if instruction == "F" else -1
            self.position += direction * F_moves[self.facing]

    def run(self, instructions):
        if not all(i in available_instructions for i in instructions):
            raise ValueError("The rover did not understand your instructions, are you sure you only entered F, R, L, B and \\n in your instructions ?")
        else:
            instruction_line = instructions.split("\n")
            for line in instruction_line:
                for instruction in line:
                    self.move(instruction)
                self.communication += self.get_position() + "\n"
            self.communication = self.communication[:-1]

    def get_position(self):
        return f"{self.position[0]} {self.position[1]} {self.facing}"

    def get_communication(self):
        return self.communication
