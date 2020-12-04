from itertools import combinations


def solution(l):

    l.sort(reverse=True)
    for i in reversed(range(1, len(l)+1)):
        for comb in combinations(l, i):
            if(sum(comb) % 3 == 0):
                return int(''.join(map(str, comb)))
    return 0


if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))
