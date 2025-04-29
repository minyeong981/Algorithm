def solution(phone_book):
    phone_book.sort()
    dic = {}
    answer = True
    n = len(phone_book[0])
    for i in range(len(phone_book)) :
        if dic.get(phone_book[i][:n], 0) == 0 :
            dic[phone_book[i]] = 1
            n = len(phone_book[i])
        else :
            answer = False
            break                     
    return answer