def solution(schedules, timelogs, startday):
    answer = 0
    for i, schedule in enumerate(schedules) :
        wanted_time = schedule + 10
        wanted_minutes = wanted_time % 100
        wanted_hours = wanted_time // 100
        
        add_hours = wanted_minutes // 60
        
        minutes = wanted_minutes % 60
        wanted_time = (wanted_hours + add_hours)*100 + minutes
        for i, time in enumerate(timelogs[i]) :
            if (startday + i) % 7 in [6, 0] :
                continue
            if time > wanted_time :
                break
        else :
            answer += 1
    return answer