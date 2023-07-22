

N = int(input())
team1 = 0
team2 = 0 

// before라는 변수를 활용한다는 점이 중요하다 
before = 0 
team1Time = 0
team2Time = 0 

for i in range(N):
    
    info = input().split()
    time = info[1].split(":")
    hour = int(time[0])
    minute = int(time[1])
    
    total = hour*60+minute 

    // 누가 이기고 있는지 판단하는 것이 중요하다 
    if team1 > team2:
        team1Time += (total-before)    
    elif team1 < team2: 
        team2Time += (total-before)
    
    if info[0] == '1':
        team1 += 1 
    elif info[0] == '2':
        team2 += 1 
        
    before = total 
    
    
if team1 > team2:
    team1Time += (48*60-before)
elif team1 < team2:
    team2Time += (48*60-before)
    
    
team1Hour = int(team1Time // 60)
team1Minute = team1Time % 60
team2Hour = int(team2Time // 60)
team2Minute = team2Time % 60
    
str1Hour = ''
str1Minute =''
str2Hour = ''
str2Minute = ''

if 0<=team1Hour and team1Hour <=9:
    str1Hour = '0' + str(team1Hour)
else:
    str1Hour = str(team1Hour)


if 0<=team1Minute and team1Minute <=9:
    str1Minute = '0' + str(team1Minute)
else:
    str1Minute = str(team1Minute)
    
        
if 0<=team2Hour and team2Hour <=9:
    str2Hour = '0' + str(team2Hour)
else:
    str2Hour = str(team2Hour)


if 0<=team2Minute and team2Minute <=9:
    str2Minute = '0' + str(team2Minute)
else:
    str2Minute = str(team2Minute)
    
        
    

print(str1Hour + ":" + str1Minute)
print(str2Hour + ":" + str2Minute)
        
        
        
