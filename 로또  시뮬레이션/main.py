from random import randint


def generate_numbers(n):
    list=[]
    while len(list) < n:
        num = randint(1, 45)  # 무작위
        if num not in list: # 중복 값 제외
            list.append(num)
    return list



def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print(draw_winning_numbers())
    