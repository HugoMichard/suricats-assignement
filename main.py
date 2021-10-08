from rover import Rover


if __name__ == '__main__':
    instructions = ""
    input_text = "Input instruction line (or multiple instruction lines separated by \\n)\nIf no more instructions to give, hit Enter \n"
    user_input = input(input_text)
    while user_input != "":
        instructions += user_input + "\n"
        user_input = input(input_text)
    instructions = instructions.rstrip().replace("\\n", "\n")

    print("Moving rover with following instructions :")
    print(instructions)
    r = Rover()
    try:
        r.run(instructions)
        print("Rover outputs are : ")
        print(r.get_communication())
    except ValueError as e:
        print(e)

