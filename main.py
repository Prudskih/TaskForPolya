import calendar

def make_calendar(lst: list):
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
    next_month = calendar.monthcalendar(yy, next_mm)[0]
    previous_month = calendar.monthcalendar(yy, previous_mm)[-1]
    for i in range(7):
        if month[0][i] == 0:
            for a in range(len(previous_month)):
                if previous_month[a] != 0:
                    month[0][i] = previous_month[i]
        if month[-1][i] == 0:
            for a in range(len(next_month)):
                if next_month[a] != 0:
                    month[-1][i] = next_month[i]
    return month


with open('input.txt', 'r') as input_file:
    arg = input_file.readline().split(', ')
    lst = []
    for j in arg:
        lst.append(int(j))

with open('output.txt', 'w') as output_file:
    output_file.write(repr(make_calendar(lst)))