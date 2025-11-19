# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    index = string.find(sub_string)
    string = string[index + 1:]
    count = 0
    while index > -1:
        count += 1
        index = string.find(sub_string)
        string = string[index+1:]
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)