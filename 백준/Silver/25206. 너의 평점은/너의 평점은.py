import sys
input = sys.stdin.readline

gradeDict = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}

num = 0 # 분자
sumCredit = 0 # 분모

for _ in range(20) :
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade != 'P' :
        sumCredit += credit
        num += gradeDict[grade] * credit

print(num/sumCredit)