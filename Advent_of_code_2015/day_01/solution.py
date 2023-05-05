def solution() -> (int, int):
    count = position = position_basement = 0
    with open("input.txt", 'r') as f:
        for char in f.read():
            position += 1
            if char == "(":
                count += 1
            elif count == 0 and position_basement == 0:
                position_basement = position
                count -= 1
            else:
                count -= 1
        return count, position_basement


def main():
    part_01, part_02 = solution()
    print(f"{part_01 = }\n{part_02 = }")


if __name__ == "__main__":
    main()
