
info = {}


def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    for i in range(0, len(id_list)):
        info[id_list[i]] = i 
        
        
    report2 = [[] for _ in range(len(id_list))]
    
    
    for i in range(0, len(report)):
        
        names = report[i].split(" ")
        
        a = info.get(names[0])
        b = info.get(names[1])
        
        if a not in report2[b]:
            report2[b].append(a)
            
    
    
    for i in range(0, len(id_list)):
        if len(report2[i]) >= k:
            
            for num in report2[i]:
                answer[num] += 1 
    
    
    
    return answer
    
