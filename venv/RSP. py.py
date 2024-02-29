import random

# 승패 횟수
win_count = 0
lose_count = 0
draw_count = 0

def play_game():
    global win_count, lose_count, draw_count  # 전역 변수로 사용할 것임을 명시
    print("가위, 바위, 보 시작~!")
    choices = ["가위", "바위", "보"]
    count = 0
    while True:
        if count == 0:
            user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        else:
            user_choice = input("한번 더 가위, 바위, 보: ")
        PC_choice = random.choice(choices)
        print(f"Your choice: {user_choice}")
        print(f"PC's choice: {PC_choice}")
        if user_choice == PC_choice:
            result = "비겼다!"
            draw_count += 1  # 무승부 횟수 증가
            print(result)
            count += 1
            continue
        elif (user_choice == "가위" and PC_choice == "바위") or \
                (user_choice == "바위" and PC_choice == "보") or \
                (user_choice == "보" and PC_choice == "가위"):
            result = "졌다!"
            lose_count += 1  # 진 횟수 증가
            print(result)
            break
        else:
            result = "이겼다!"
            win_count += 1  # 이긴 횟수 증가
            print(result)
            break
    return result

# 첫 실행 시에만 물어보는 함수
play_game()

# 한 판 더 하는 함수
while True:
    play_again = input("한 판 더 하시겠습니까? (y/n):")
    if play_again in ('y'):
        print("게임시작")
        play_game()
    elif play_again in ('n'):
        print("게임종료")
        break

# 승, 패, 무승부의 횟수를 통계
print("통계:")
print(f"이긴 횟수: {win_count}")
print(f"진 횟수: {lose_count}")
print(f"비긴 횟수: {draw_count}")
