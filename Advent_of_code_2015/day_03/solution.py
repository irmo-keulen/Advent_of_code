def part_01() -> int:
    pos: dict = {"x": 0, "y": 0}
    
    with open("input.txt", "r") as f:
        unique = [(pos["x"], pos["y"])]
        for symbol in f.read():
            update_pos(pos, symbol)
            if (pos["x"], pos["y"]) not in unique:
                unique.append((pos["x"], pos["y"]))
        return len(unique)


def part_02() -> int:
    pos_robo: dict = {"x": 0, "y":0}
    pos_santa: dict = {"x": 0, "y":0}

    with open("input.txt", "r") as f:
        unique = [(pos_santa["x"], pos_santa['y'])]
        for idx, symbol in enumerate(f.read()):
            if idx % 2 == 0:
                update_pos(pos_santa, symbol)
                if (pos_santa['x'], pos_santa["y"]) not in unique:
                    unique.append((pos_santa['x'], pos_santa["y"]))
            else:
                update_pos(pos_robo, symbol)
                if (pos_robo['x'], pos_robo["y"]) not in unique:
                    unique.append((pos_robo['x'], pos_robo["y"]))

        return len(unique)
                

def update_pos(pos: dict, symbol: str) -> None:
    match symbol.lower():
            case "<":
                pos["x"] -= 1

            case ">":
                pos["x"] += 1

            case "^":
                pos["y"] += 1

            case "v":
                pos["y"] -= 1


def main() -> None:
    print(part_01())
    print(part_02())


if __name__ == "__main__":
    main()
