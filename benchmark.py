import csv
import time
from collections import deque

COUNTS = [5_000, 20_000, 80_000]
METHODS = ["list", "deque", "reverse"]


def list_front(count):
    items = []
    for number in range(count):
        items.insert(0, number)
    return items


def deque_front(count):
    items = deque()
    for number in range(count):
        items.appendleft(number)
    return items


def reverse_front(count):
    items = list(range(count))
    items.reverse()
    return items


FUNCTIONS = {
    "list": list_front,
    "deque": deque_front,
    "reverse": reverse_front,
}


def moves_for(method, count):
    if method == "list":
        return count * (count - 1) // 2
    if method == "deque":
        return count
    return count * 2


def repeats_for(count):
    if count <= 5_000:
        return 20
    if count <= 20_000:
        return 5
    return 1


def main():
    rows = []
    for count in COUNTS:
        repeats = repeats_for(count)
        for method in METHODS:
            started = time.perf_counter()
            for _ in range(repeats):
                FUNCTIONS[method](count)
            seconds = (time.perf_counter() - started) / repeats
            moves = moves_for(method, count)
            rows.append([
                method,
                count,
                repeats,
                round(seconds, 6),
                moves,
                round(count / seconds, 1),
            ])

    with open("benchmark_results.csv", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["method", "count", "repeats", "seconds", "moves", "items_per_second"])
        writer.writerows(rows)

    print(len(rows), "measurements written")


if __name__ == "__main__":
    main()
