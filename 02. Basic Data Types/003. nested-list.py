# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    lst1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    grade_sec = sorted(set([score for [name, score] in students]))[1]
    students_sec = sorted([i[0] for i in students if i[1] == grade_sec])
    for i in students_sec:
        print(i)
        
