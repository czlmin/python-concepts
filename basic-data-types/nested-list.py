# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    student_list = []
    score_list = []
    second_score = -1
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        student = [name, score]
        student_list.append(student)

    # sorted_list = sorted(student_list, key=lambda x: x[1])
    # print(sorted_list)
    score_set = set(score_list)
    sorted_scores = sorted(score_set)
    if len(sorted_scores) > 1:
        second_score = sorted_scores[1]
    students = [student[0] for student in student_list if student[1] == second_score]
    sorted_students = sorted(students)
    print('\n'.join(sorted_students))