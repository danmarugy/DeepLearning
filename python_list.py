
# 리스트 생성
a = [1,2,3,4,5]

#리스트 내용 출력
print(a) #[1, 2, 3, 4, 5]

#리스트 길이 출력
print(len(a)) #5

#원소 접근
print(a[1]) #2

#값 대입1
a[4] = 99
print(a) #[1, 2, 3, 4, 99]

#값 대입2
a[4] = 'A'
print(a) #[1, 2, 3, 4, 'A']

#데이터 타입
print(type(a)) #<class 'list'>
print(type(a[0])) #<class 'int'>
print(type(a[4])) #<class 'str'>

#슬라이싱
#인덱스 0부터 2까지(2는 포함 X)
print(a[0:2]) #[1, 2]

# 인덱스 1부터 마지막까지
print(a[1:]) #[2, 3, 4, 'A']

#처음부터 인덱스 3까지 얻기(3은 포함X)
print(a[:3]) #[1, 2, 3]

# 처음부터 마지막 원소의 1개 앞까지 얻기
# -1은 마지막 원소, -2는 끝에서 한개 앞의 원소에 해당
print(a[:-1]) #[1, 2, 3, 4]
# 처음부터 마지막 원소의 2개 앞까지 얻기
print(a[:-2]) #[1, 2, 3]

print(a[-2:]) #[4, 'A']   ==a[3:]

print(a[-1:]) #['A']       ==print(a[4:])

