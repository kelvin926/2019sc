# -*- coding: utf-8 -*-
import random  # 랜덤 모듈 사용 선언
while True: #while 반복문 사용
    count = 0 #기회 변호 초기화
    diff = input('난이도를 입력해주세요.(쉬움:0, 보통:1, 어려움:2):') #난이도 입력을 변수에 저장
    if diff == '0': #쉬움 난이도 선택
        count = 10
        print('쉬움 난이도를 선택하셨습니다.\n기회가 10번 주어집니다.')
        break #while문 빠져나감
    elif diff == '1': #보통 난이도 선택
        count = 7
        print('보통 난이도를 선택하셨습니다.\n기회가 7번 주어집니다.')
        break #while문 빠져나감
    elif diff == '2': #어려움 난이도 선택
        count = 4
        print('어려움 난이도를 선택하셨습니다.\n기회가 4번 주어집니다.')
        break #while문 빠져나감
    else: #해당되지 않은 다른 값을 입력했을경우 (오류 상황)
        print('정확한 값을 입력해주세요.')
        continue #다시 난이도 입력으로 돌아감

min = int(input('최소값을 입력해주세요:'))  # 랜덤값이 존재할 수 있는 범위의 최소값 지정
max = int(input('최대값을 입력해주세요:'))  # 랜덤값이 존재할 수 있는 범위의 최대값 지정
i = random.randint(min, max)  # i = 최소값~최대값 사이의 랜덤값
print('설정 완료!')
while True:  # while 반복문 사용
    if count == 0: #기회가 모두 소진된 경우
        print('기회가 모두 소진되었습니다.\n게임을 종료합니다.')
        break #프로그램 정지
    else: #기회가 남아있는 경우
        try:  # try ~ except 오류 처리 구문 사용
            guess = int(input('제 숫자를 맞춰보세요!:'))  # guess = 사용자의 추리 숫자
            if guess == i:  # 랜덤값과 추리숫자가 같을 경우
                print('맞추셨습니다!')
                break  # 프로그램 정지
            elif guess > i and guess <= max:  # 최대,최소 범위 내에서 랜덤값이 추리값보다 작을 경우
                print('너무 높아요!')
                count -= 1 #기회에서 1 감소
                print('기회가 %d번 남았습니다.'%count) #남은 기회 출력
            elif guess < i and guess >= min:  # 최대,최소 범위 내에서 랜덤값이 추리값보다 클 경우
                print('너무 낮아요!')
                count -= 1 #기회에서 1 감소
                print('기회가 %d번 남았습니다.'%count) # 남은 기회 출력
            else:  # 그 외의 상황 : 최대,최소 범위 내의 숫자를 입력하지 않았을 때
                print('최소값~최대값 사이의 숫자를 입력해주세요!')
        except:  # try ~except 구문의 오류(숫자가 아닌 다른 문자를 입력하였을 때) 상태 처리
            print('숫자만 입력해주세요!')
