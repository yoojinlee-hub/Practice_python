with open('data/chicken.txt','r') as chicken:
    total = 0
    avg = 0
    days = 0
    for day in chicken:
        chicken_list = day.strip().split() 
        total = total + (int)(chicken_list[1])
        days = days +1
    avg = total / days
print(avg)