
def solution(fees, records):
    answer = [0]*10000
    totalTime = [0]*10000
    finalAnswer = []
    
    info = {}
    
    for i in range(len(records)):
        
        record = records[i].split(" ")
        time = record[0]
        number = record[1]
        action = record[2]
        
        timeSplit = time.split(":")
        intTime = 60*int(timeSplit[0])+int(timeSplit[1])
        
        if action == "IN":
            info[number] = intTime
        elif action == "OUT":
            gap = intTime - info[number]
            totalTime[int(number)] += gap
            info[number] = -1 
            
            
    for key in info:
        if info[key] != -1:
            gap = 1439-info[key]
            totalTime[int(key)] += gap 
            
    
    for i in range(0, 10000):
        if totalTime[i] != 0:
            fee = 0 
            time = totalTime[i]
            if 0<= time and time <= fees[0]:
                fee = fees[1]
            else:
                fee += fees[1] 
                time -= fees[0]
                
                if time % fees[2] == 0:
                    fee += (time // fees[2])*fees[3]
                else:
                    fee += (time // fees[2])*fees[3] + fees[3]
            
            answer[i] = fee
            
    
    for i in range(0, 10000):
        if totalTime[i] != 0:
            finalAnswer.append(answer[i])
    
    
    return finalAnswer
