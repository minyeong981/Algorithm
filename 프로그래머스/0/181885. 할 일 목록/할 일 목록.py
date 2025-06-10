def solution(todo_list, finished):
    answer = []
    for todo, result in zip(todo_list, finished) :
        if not result :
            answer.append(todo)
    return answer