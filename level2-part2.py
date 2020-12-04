def solution(s):
    r = ans = 0
    for char in s:
        if char == '>':
            r += 1
        elif char == '<' and r > 0:
            ans += (r * 2)

    return ans

if __name__ == "__main__":
    print(solution("<<>><"))
    print(solution(">----<"))
