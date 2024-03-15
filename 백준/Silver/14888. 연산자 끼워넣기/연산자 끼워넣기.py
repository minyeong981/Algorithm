def calc(v1, v2, oper):
    if oper == '+':
        return v1 + v2
    elif oper == '-':
        return v1 - v2
    elif oper == '*':
        return v1 * v2
    elif oper == '/':
        if v1 < 0:
            return -((-v1) // v2)
        else:
            return v1 // v2

def oper_cadi(k, n, lst, num, op_input):
    global results
    if k == n:
        cal_num = num[0]
        for i in range(n):
            cal_num = calc(cal_num, num[i + 1], lst[i])
        results.append(cal_num)
        return
    for i in range(4):
        if op_input[i] > 0:
            op_input[i] -= 1
            lst.append(operations[i])
            oper_cadi(k + 1, n, lst, num, op_input)
            lst.pop()
            op_input[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
operations = ['+', '-', '*', '/']
op_input = list(map(int, input().split()))  # + - * / 개수

results = []
oper_cadi(0, sum(op_input), [], numbers, op_input)

print(max(results))
print(min(results))

