import calendar

def make_calendar(lst:list):
    yy, mm = lst[0], lst[1]
    if mm == 1:
        previous_mm = 12
    else:
        previous_mm = mm - 1
    if mm == 12:
        next_mm = 1
    else:
        next_mm = mm + 1
    month = calendar.monthcalendar(yy, mm)
    next_month = calendar.monthcalendar(yy, next_mm)
    previous_month = calendar.monthcalendar(yy, previous_mm)
    previous_month[0] = previous_month[-1]
    for i in range(7):
        if month[0][i] == 0:
            for a in range(len(previous_month[0])):
                if previous_month[0][a] != 0:
                    month[0][i] = previous_month[-1][i]
        if month[-1][i] == 0:
            for a in range(len(next_month[0])):
                if next_month[0][a] != 0:
                    month[-1][i] = next_month[0][i]
    return month


with open('input.txt', 'r') as input_file:
    arg = input_file.readline().split(', ')
    lst = []
    for i in arg:
        lst.append(int(i))

with open('output.txt', 'w') as output_file:
    output_file.write(repr(make_calendar(lst)))