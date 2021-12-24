def count_matching_numbers(numbers, winning_numbers):
    same=0
    for one in numbers:
        for two in winning_numbers:
            if one==two:
                same = same+1
    return same


def check(numbers, winning_numbers):
    same = count_matching_numbers(numbers,winning_numbers[:6])
    bonus = count_matching_numbers(numbers,winning_numbers[6:])
    if same==6:
        return 10000000000
    elif same==5 and bonus==1:
        return 50000000
    elif same==5:
        return 1000000 
    elif same==4:
        return 50000
    elif same==3:
        return 5000
    else: return 0


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))