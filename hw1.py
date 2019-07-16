# -*- coding: utf-8 -*-
import random  # 랜덤 모듈 사용 선언
min = int(input('최소값을 입력해주세요:'))  # 랜덤값이 존재할 수 있는 범위의 최소값 지정
max = int(input('최대값을 입력해주세요:'))  # 랜덤값이 존재할 수 있는 범위의 최대값 지정
i = random.randint(min, max)  # i = 최소값~최대값 사이의 랜덤값
print('설정 완료!')
while True:  # while 반복문 사용
    try:  # try ~ except 오류 처리 구문 사용
        guess = int(input('제 숫자를 맞춰보세요!:'))  # guess = 사용자의 추리 숫자
        if guess == i:  # 랜덤값과 추리숫자가 같을 경우
            print('맞추셨습니다!')
            break  # 프로그램 정지
        elif guess > i and guess <= max:  # 최대,최소 범위 내에서 랜덤값이 추리값보다 작을 경우
            print('너무 높아요!')
        elif guess < i and guess >= min:  # 최대,최소 범위 내에서 랜덤값이 추리값보다 클 경우
            print('너무 낮아요!')
        else:  # 그 외의 상황 : 최대,최소 범위 내의 숫자를 입력하지 않았을 때
            print('최소값~최대값 사이의 숫자를 입력해주세요!')
    except:  # try ~except 구문의 오류(숫자가 아닌 다른 문자를 입력하였을 때) 상태 처리
        print('숫자만 입력해주세요!') #okay
