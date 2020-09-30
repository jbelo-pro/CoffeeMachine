offset = int(input())
london = 10.5

if london + offset > 24:
    print('Wednesday')
elif london + offset < 0:
    print("Monday")
elif 0 <= london + offset <= 24:
    print("Tuesday")
