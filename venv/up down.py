import random

def 숫자맞추기():
    random_num = random.randint(1, 100)
    user_input = int(input("1-100사이 숫자를 입력: "))
    count = 0

    while random_num != user_input:
        if random_num > user_input:
            print("UP")
        else:
            print("DOWN")
        user_input = int(input("1-100사이 숫자를 입력: "))
        count += 1

    print(f"숫자는 {user_input}!!!. \n{count + 1}번 만에 성공!")

# 첫 시작 시에만 적용하는 함수
숫자맞추기()

     # 한 판 더하는 함수
while True:
        play_again = input("한 판 더 하시겠습니까? (y/n):")
        if play_again in ('y'):
            print("게임시작")
            숫자맞추기()

        elif play_again in ('n'):
            print("게임종료")
            break
