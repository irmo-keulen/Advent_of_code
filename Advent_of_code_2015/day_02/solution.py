def part_01():
    paper: [int] = 0
    total: int = 0
    with open("input.txt", "r") as f:
        for ln in f.readlines():
            l, w, h = [int(x) for x in ln.split("x")]
            paper = [(l * w), (w * h), (h * l)]
            extra_paper = min(paper)
            total += sum(paper*2) + extra_paper
    print(total)


def solution():
    part_01()


if __name__ == "__main__":
    solution()
