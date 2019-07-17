# -*- coding: utf-8 -*-
# 한글 사용시 깨지는 오류가 있어 인코딩 방식을 강제로 utf-8로 지정
all = [] #전체 성적 배열 생성
i = 0 #응시자 수 초기화
top = 0 #최고 점수 초기화
total = 0 #총점 초기화
topname = 0 #최고 점수 응시자 이름 초기화
korean_total = 0 #국어 총점 초기화
math_total = 0 #수학 총점 초기화
english_total = 0 #영어 총점 초기화
while True: #무한반복 시작
    student = [] #학생 성적 배열 생성
    print("<Q혹은q를 누르면 종료합니다.>")
    name = input('%d번 학생의 이름을 입력해주세요: '%(i+1)) #이름 변수에 입력받은 이름 저장
    if name == "q" or name == "Q": #Q 혹은 q 입력시 종료
        print('종료합니다.')
        break
    student.append(name) #학생 성적 배열에 이름 저장

    korean = input('%d번 학생의 국어 점수를 입력해주세요: '%(i+1)) #국어 점수 변수에 입력받은 점수 저장
    if korean == "q" or korean == "Q": #Q 혹은 q 입력시 종료
        print('종료합니다.')
        break
    student.append(korean) #학생 성적 배열에 국어 점수 저장

    math = input('%d번 학생의 수학 점수를 입력해주세요: '%(i+1)) #수학 점수 변수에 입력받은 점수 저장
    if math == "q" or math == "Q": #Q혹은 q 입력시 종료
        print('종료합니다.')
        break
    student.append(math) #학생 성적 배열에 수학 점수 저장

    english = input('%d번 학생의 영어 점수를 입력해주세요: '%(i+1)) #영어 점수 변수에 입력받은 점수 저장
    if english == "q" or english == "Q": #Q혹은 q 입력시 종료
        print('종료합니다.')
        break
    student.append(english) #학생 성적 배열에 영어 점수 저장
    all.append(student) #all 배열에 student배열(개인 성적) 전체 입력
    total = int(all[i][1]) + int(all[i][2]) + int(all[i][3]) #학생의 점수들을 모두 더하여 total에 저장
    if total > top: #1위 총점 점수보다 이 학생의 총점이 더 높다면
        top = total #1위 총점 점수에 이 학생의 총점 저장
        topname = all[i][0] #1위 이름에 이 학생의 이름 저장
    korean_total += int(all[i][1]) #학생들의 국어 총점에 이 학생의 국어 점수 더함
    math_total += int(all[i][2]) #학생들의 수학 총점에 이 학생의 수학 점수 더함
    english_total += int(all[i][3]) #학생들의 영어 총점에 이 학생의 영어 점수 더함
    #각 과목의 총점을 따로 변수 선언하여, 사용자가 입력중에 Q를 입력해도 완벽히 입력되지 않은 학생의 점수는 반영하지 않도록 하였음.
    i = i + 1 #응시자 수 한명 추가
    print('\n') #다음 학생의 점수를 입력하기 위해 줄바꿈

#반복문인 while문에서 사용자가 정지 명령을 내려 반복문 정지
print('=======')
print('전체 응시자:%d명'%(i)) #전체 응시자 출력
print('국어 평균:%.2f점'%(korean_total/i)) #국어 총점에서 응시자 수를 나누어 국어 평균 출력
print('수학 평균:%.2f점'%(math_total/i)) #수학 총점에서 응시자 수를 나누어 수학 평균 출력
print('영어 평균:%.2f점'%(english_total/i)) #영어 총점에서 응시자 수를 나누어 영어 평균 출력
print('=======')
print('1등 이름:%s'%topname) #1등의 이름을 출력
print('1등 총점:%d점'%top) #1등의 총점을 출력
print('=======')
f = open('exam.txt', 'w+t') #파일을 저장하기 위해 exam.txt라는 새로운 파일을 생성
f.write('이름\t국어\t수학\t영어\n') #학생들의 성적을 구분하기 위한 분류
for j in range(i): #응시자 수 만큼 반복
    data = all[j][0] #이름을 data변수에 저장
    for k in range(1,4):
        data +='\t%d'%int(all[j][k]) #국어 점수, 수학 점수, 영어 점수를 tab칸씩 분류하여 data변수에 중복 저장
    data += '\n' #다음 응시자 저장을 위한 줄바꿈
    f.write(data) #학생들의 성적을 파일에 저장
print('파일 저장중...')
f.close() #파일 저장 세션 종료
print('파일 저장 완료!(.py가 속한 폴더에 생성되었습니다. (exam.txt)')
