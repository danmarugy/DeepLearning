# 언패킹시 특정값을 무시

x, _, y = {1,2,3} # x=1, y=3
print(x,_,y)

# 여러개의 값 무시
x, *_, y = {1,2,3,4,5} # x=1, y=5
print(*_)
print(x,y)

