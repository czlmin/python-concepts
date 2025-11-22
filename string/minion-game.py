# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    n = len(string)
    kevin_count = 0
    stuart_count = 0
    lower_string = string.lower()
    ind = -1
    for s in lower_string:
        ind += 1
        if s in "aeiou":
            kevin_count += n - ind
        else:
            stuart_count += n - ind

    if stuart_count == kevin_count:
        print("Draw")
    elif stuart_count > kevin_count:
        print(f"Stuart {stuart_count}")
    else:
        print(f"Kevin {kevin_count}")

def minion_game2(string):
    n = len(string)
    kevin_count = 0
    stuart_count = 0
    vowels = "aeiou"

    for i in range(n):
        if string.lower()[i] in vowels:
            kevin_count += n - i
        else:
            stuart_count += n - i

    if stuart_count == kevin_count:
        print("Draw")
    elif stuart_count > kevin_count:
        print(f"Stuart {stuart_count}")
    else:
        print(f"Kevin {kevin_count}")

if __name__ == '__main__':
    s = input()
    # minion_game(s)
    minion_game2(s)