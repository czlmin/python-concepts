# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()
    results = ['False', 'False', 'False', 'False', 'False']
    for char in s: 
        if char.isalnum() and results[0] == 'False':
            results[0] = 'True'
        if char.isalpha() and results[1] == 'False':
            results[1] = 'True'
        if char.isdigit() and results[2] == 'False':
            results[2] = 'True'
        if char.islower() and results[3] == 'False':
            results[3] = 'True'
        if char.isupper() and results[4] == 'False':
            results[4] = 'True'
    
    for result in results:
        print(result)