def calculate_time(n):
    time = 800
    for i in range(1, n + 1):
        time += 12
        for k in range(9, i + 4):
            time += 6 * k
    return time

def fsm(input_string):
    try:
        count = 0
        state = 0
        input_string = [int(s) for s in input_string]
        delta = dict({((0, 0), "e0"), ((0, 1), "e1"),
                      (("e0", 0), "e00"), (("e0", 1), "e01"),
                      (("e1", 0), "e10"), (("e1", 1), "e11"),
                      (("e00", 0), "e000"), (("e00", 1), "e01"),
                      (("e01", 0), "e10"), (("e01", 1), "e011"),
                      (("e10", 0), "e100"), (("e10", 1), "e01"),
                      (("e11", 0), "e10"), (("e11", 1), "e111"),
                      (("e000", 0), "e0000"), (("e000", 1), "e01"),
                      (("e011", 0), "e0110"), (("e011", 1), "e111"),
                      (("e100", 0), "e000"), (("e100", 1), "e1001"),
                      (("e111", 0), "e10"), (("e111", 1), "e1111"),
                      (("e0000", 0), "e0000"), (("e0000", 1), "e01"),
                      (("e0110", 0), "e100"), (("e0110", 1), "e01"),
                      (("e1001", 0), "e10"), (("e1001", 1), "e011"),
                      (("e1111", 0), "e10"), (("e1111", 1), "e1111")})

        accepted_state = ["e0000", "e0110", "e1001", "e1111"]
        for symbol in input_string:
            state = delta[(state, symbol)]
            if state in accepted_state:
                count += 1
        return count

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Q1 - b
    print(fsm("011001011100"))

    # Q1 - c
    file = 'BINARY_DIGITS_OF_E.txt'
    with open(file, 'r') as file:
        file_content = file.read()
        file_content = file_content.replace('\n', '')
    print(fsm(file_content))


if __name__ == '__main__':
    main()
