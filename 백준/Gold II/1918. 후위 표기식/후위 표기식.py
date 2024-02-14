def postcal(cal):
    st = []
    result = []
    icp ={'+':1, '-':1, '*':2, '/':2, '(':3}
    isp ={'+':1, '-':1, '*':2, '/':2, '(':0}
    for ele in cal :
        if ele != '+' and ele != '-' and ele != '*' and ele != '/' and ele !='(' and ele != ')' :
            result.append(ele)
        elif ele == ')':
            while st[-1] != '(' :
                result.append(st.pop())
            st.pop()
        else :
            if st and icp[ele] > isp[st[-1]] :
                st.append(ele)
            else:
                while st and icp[ele] <= isp[st[-1]] :
                    result.append(st.pop())
                st.append(ele)
    while st :
        result.append(st.pop())
    return result

calc = input()
result = postcal(calc)
print(''.join(map(str, result)))