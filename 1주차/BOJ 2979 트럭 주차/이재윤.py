// 문제의 조건에 유의해야 한다
// 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.
// -> 두 대를 주차할 때는, 1분에 '한 대당' B원, 세 대를 주차할 때는 1분에 '한 대당' C원을 내야 한다
// end는 떠나는 시간이므로 포함하지 않아야 한다 

A, B, C = map(int, input().split())

arr = [0]*110
cost = 0 

for i in range(3):
    start, end = map(int,input().split())
    
    for i in range(start, end):
        arr[i] += 1
        
for i in range(1, 101):
    if arr[i] == 1:
        cost += A
    elif arr[i] == 2:
        cost += 2*B
    elif arr[i] == 3:
        cost += 3*C
        
        
print(cost) 
