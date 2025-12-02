def before_an_exam(ranges, time_studied):
    min_time = 0
    max_time = 0
    days = len(ranges)
    min_time_string = ""
    max_time_string = ""
    min_time_array = []
    max_time_array = []
    schedule = [0] * days
    for index, day in enumerate(ranges):
        min_time += day[0]
        min_time_array.append((day[0], index))
        min_time_string += str(day[0]) + " "
        max_time += day[1]
        max_time_array.append((day[1], index))
        max_time_string += str(day[1]) + " "
    min_time_string = min_time_string.strip()
    max_time_string = max_time_string.strip()
    if time_studied < min_time or time_studied > max_time:
        print("NO")
        return
    else:
        print("YES")
    if time_studied == max_time:
        print(max_time_string)
    elif time_studied == min_time:
        print(min_time_string)
    elif time_studied > min_time:
        difference = time_studied - min_time
        a = difference // days
        b = difference % days
        max_time_array.sort()
        while b >= 0:
            for each_arr in max_time_array:
                if ranges[each_arr[1]][0] + a + b < each_arr[0]:
                    schedule[each_arr[1]] = ranges[each_arr[1]][0] + a + b
                    b = 0
                elif ranges[each_arr[1]][0] + a > each_arr[0]:
                    b+= (ranges[each_arr[1]][0] + a - each_arr[0])
                    schedule[each_arr[1]] = each_arr[0]
                elif ranges[each_arr[1]][0] + a <= each_arr[0]:
                    diff = each_arr[0] - ranges[each_arr[1]][0] - a
                    schedule[each_arr[1]] = ranges[each_arr[1]][0] + a + diff
                    b-= diff
            if b == 0:
                break
        schedule = list(map(str, schedule))
        schedule = " ".join(schedule)
        print(schedule)

day_limits = []
num_days,sumTime = map(int,input().split())
for _ in range(num_days):
    minTime, maxTime = map(int,input().split())
    day_limits.append([minTime,maxTime])
before_an_exam(day_limits, sumTime)
