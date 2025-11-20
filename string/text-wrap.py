
# def wrap(string, max_width):
#     list_string = list(string)
#     new_string = []
#     i = 0
#     for i in range(len(list_string) // max_width):
#         new_string += list_string[i*max_width:(i+1)*max_width]
#         new_string += '\n'
#     new_string += list_string[(i+1)*max_width:]
#     return ''.join(new_string)

def wrap(string, max_width):
    lines = []
    for i in range(0, len(string), max_width):
        lines.append(string[i:i + max_width])
    return "\n".join(lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
