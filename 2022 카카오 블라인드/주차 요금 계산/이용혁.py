import math
def time_to_str(tm):
    hh, mm = tm.split(":")
    return int(hh)*60 + int(mm)

def solution(fees, records):
    base_time, base_fare, add_time, add_fare = fees
    a = [False] * 10000
    b = [0] * 10000
    c = [0] * 10000
    fare = [0] * 10000
    for i in records:
        tm, plate, state = i.split()
        plate = int(plate)
        if state == "IN":
            a[plate] = True
            b[plate] = time_to_str(tm)
        else:
            a[plate] = False
            c[plate] += time_to_str(tm) - b[plate]
    # 출차기록이 없는 차량의 시간 계산
    for i in range(10000):
        if a[i] == True:
            c[i]+=time_to_str("23:59")-b[i]

    for i in range(10000):
        if c[i]:
            fare[i] += (base_fare + math.ceil((c[i]-base_time) / add_time) * add_fare if c[i] > base_time else base_fare)

    answer = []
    for i in range(len(c)):
        if c[i]:
            answer.append(fare[i])

    return answer


if __name__ == "__main__":
    ret = solution([180, 5000, 10, 600], \
             ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
              "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
              "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
    print(ret)
    # answer: [14600, 34400, 5000]
