# -*- coding: utf-8 -*-
# 한글 사용시 깨지는 오류가 있어 강제 인코딩 문구를 삽입

namelist = [] #이름 리스트 선언
koreanlist = [] #국어 점수 리스트 선언
englishlist = [] #영어 점수 리스트 선언
mathlist = [] #수학 점수 리스트 선언

def average(list):
    return (sum(list) / len(list)) #평균 함수 정의

top = 0 #최고 점수 초기화
total = 0 #점수 총합 초기화
topname = 0 #최고 점수 이름 초기화
stu = 1 #응시자 수 초기화
while True: #무한 반복 선언
    print("<Q혹은 q를 입력하면 성적 입력을 끝냅니다>")
    name = input("%d번 학생의 이름을 입력해주세요: " % stu) #이름 입력
    if name == "q" or name == "Q": #q혹은 Q을 입력 시 종료
        print("종료합니다.")
        break
    korean = input("%d번 학생의 국어점수를 입력해주세요: " % stu) #국어 점수 입력
    if korean == "q" or korean == "Q": #q혹은 Q을 입력 시 종료
        print("종료합니다.")
        break
    english = input("%d번 학생의 영어점수를 입력해주세요: " % stu) #영어 점수 입력
    if english == "q" or english == "Q": #q혹은 Q을 입력 시 종료
        print("종료합니다.")
        break
    math = input("%d번 학생의 수학점수를 입력해주세요: " % stu) #수학 점수 입력
    if math == "q" or math == "Q": #q혹은 Q을 입력 시 종료
        print("종료합니다.")
        break
    stu = stu + 1 #응시자 수 한명 추가
    print('\n') #다음 응시자로 인한 줄 바꿈
    namelist.append(name) #이름 리스트에 응시자의 이름을 추가
    koreanlist.append(korean) #국어 점수 리스트에 응시자의 국어 점수 추가
    englishlist.append(english) #영어 점수 리스트에 응시자의 영어 점수 추가
    mathlist.append(math) #수학 점수 리스트에 응사지의 수학 점수 추가
    total = int(korean) + int(english) + int(math) #해당 응시자의 총점 계산
    if total > top: #해당 응시자의 총점이 현재 1등 응시자의 총점보다 높다면 변경
        top = total
        topname = name
englishlist = list(map(float, englishlist))
mathlist = list(map(float, mathlist))
koreanlist = list(map(float, koreanlist))
print("\n") #결과 출력을 위한 줄바꿈
print("====================================================")
print("전체 응시자:%d명" % (stu - 1)) #마지막 계산에 응시자가 실제보다 한명 더 추가되었으므로 -1 계산
print("국어 평균:%.2f" % average(koreanlist)) #평균 함수를 이용한 국어 평균 계산값 출력
print("수학 평균:%.2f점" % average(mathlist)) #평균 함수를 이용한 수학 평균 계산값 출력
print("영어 평균:%.2f점" % +average(englishlist)) #평균 함수를 이용한 영어 평균 계산값 출력
print("====================================================")
print("1등 이름:%s" % topname) #1등 성적의 이름 출력
print("1등 총점:%d점" % top) #1등의 총점을 출력
print("====================================================")
