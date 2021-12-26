from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess) <3 :
        print('{}번째 숫자를 입력하세요:'.format(len(new_guess)+1))
        num = input()
        if num not in new_guess:
            if num<10:
                new_guess.append(num)
            else:
                print('범위를 벗어나는 숫자입니다. 다시 입력하세요')
        else:
            print('중복되는 숫자입니다. 다시 입력하세요.')


def get_score(guesses, solution):
    def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    
    i=0
    while i<3:
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count+=1
                i+=1
            elif guesses[i] != solution[i]:
                ball_count+=1
                i+=1
        else:
            i+=1
    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
